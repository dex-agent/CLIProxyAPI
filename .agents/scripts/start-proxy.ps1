# start-proxy.ps1 - starts CLIProxyAPI outside the host's process tree and without a window.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1
#
# Why WMI instead of Start-Process: a process created by Start-Process inherits the job of the
# shell/host that launched it and dies with it when ZCode closes (measured 2026-11-22/23).
# Win32_Process.Create is born from the WMI service, outside that job.
# Why ShowWindow = 0: the previous instance, created without it, died together with the
# cmd.exe wrapper a few minutes after starting, with no panic in stderr (2026-11-23). A visible
# console window being closed is the PROBABLE cause, not proven. Surviving a ZCode restart is
# also not proven yet: check with Test-ProxyUp after the next restart.
# Idempotent (R14): if port 8317 already answers, no second process is created.
# The access key comes from access.api-keys in config.yaml; the value never lives in this script.

$ProgressPreference = 'SilentlyContinue'

$repoRoot   = 'C:\CodexProjetos\CLIProxyAPI'
$proxyPath  = Join-Path $repoRoot 'cli-proxy-api.exe'
$configPath = Join-Path $repoRoot 'config.yaml'
$logDir     = Join-Path $repoRoot '.agents\receipts'
$logOut     = Join-Path $logDir 'proxy-run.log'
$errLog     = Join-Path $logDir 'proxy-run.err.log'
$probeUrl   = 'http://127.0.0.1:8317/v1/models'

function Get-AccessKey {
    # First list item under the top-level "access:" block of the proxy config.
    $inAccess = $false
    foreach ($line in (Get-Content -LiteralPath $configPath -Encoding UTF8)) {
        if ($line -match '^access:\s*$') { $inAccess = $true; continue }
        if ($inAccess -and $line -match '^\S') { break }
        if ($inAccess -and $line -match '^\s*-\s*["'']?([^"''\s#]+)') { return $Matches[1] }
    }
    throw "chave de acesso ausente em $configPath (access.api-keys)"
}

$probeHdr   = @{ Authorization = ('Bearer ' + (Get-AccessKey)) }

function Test-ProxyUp {
    try {
        $resp = Invoke-WebRequest -Uri $probeUrl -Headers $probeHdr -TimeoutSec 3 -UseBasicParsing
        return ($resp.StatusCode -eq 200)
    } catch { return $false }
}

function Get-ProxyPid {
    $conn = Get-NetTCPConnection -State Listen -LocalPort 8317 -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($conn) { return $conn.OwningProcess }
    return $null
}

if (-not (Test-Path -LiteralPath $proxyPath))  { throw "binario ausente: $proxyPath" }
if (-not (Test-Path -LiteralPath $configPath)) { throw "config ausente: $configPath" }
if (Test-ProxyUp) { Write-Output ('JA_ATIVO http=200 pid=' + (Get-ProxyPid)); exit 0 }
if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

# /s: cmd strips the outer quotes; the paths stay quoted
$cmdLine = 'cmd.exe /s /c ""{0}" --config "{1}" > "{2}" 2> "{3}""' -f $proxyPath, $configPath, $logOut, $errLog
$startup = New-CimInstance -ClassName Win32_ProcessStartup -ClientOnly -Property @{ ShowWindow = [uint16]0 }
$spawn = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{
    CommandLine            = $cmdLine
    CurrentDirectory       = $repoRoot
    ProcessStartupInformation = $startup
}
if ($spawn.ReturnValue -ne 0) { Write-Output ('FALHOU_WMI rc=' + $spawn.ReturnValue); exit 1 }

for ($i = 0; $i -lt 30; $i++) {
    Start-Sleep -Milliseconds 500
    if (Test-ProxyUp) { Write-Output ('INICIADO http=200 pid=' + (Get-ProxyPid) + ' (wrapper ' + $spawn.ProcessId + ')'); exit 0 }
}
Write-Output "FALHOU_APOS_15S ver=$errLog"
exit 1
