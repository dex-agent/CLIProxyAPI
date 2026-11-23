# start-proxy.ps1 - inicia o CLIProxyAPI por fora da arvore de processos do host e sem janela.
# Uso: powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1
#
# Por que WMI e nao Start-Process: o processo criado por Start-Process herda a job do
# shell/host que o lancou e morre junto quando o ZCode fecha (medido em 2026-11-22/23).
# Win32_Process.Create nasce do servico WMI, fora dessa job.
# Por que ShowWindow = 0: a instancia anterior, criada sem essa opcao, morreu junto com o
# wrapper cmd.exe poucos minutos depois de subir, sem panico no stderr (2026-11-23). Janela
# de console visivel sendo fechada e a causa PROVAVEL, nao provada. Sobreviver a um restart
# do ZCode tambem ainda nao foi provado: confira com Test-ProxyUp depois do proximo restart.
# Idempotente (R14): se a porta 8317 ja responde, nao cria segundo processo.

$ProgressPreference = 'SilentlyContinue'

$repoRoot   = 'C:\CodexProjetos\CLIProxyAPI'
$proxyPath  = Join-Path $repoRoot 'cli-proxy-api.exe'
$configPath = Join-Path $repoRoot 'config.yaml'
$logDir     = Join-Path $repoRoot '.agents\receipts'
$logOut     = Join-Path $logDir 'proxy-run.log'
$errLog     = Join-Path $logDir 'proxy-run.err.log'
$probeUrl   = 'http://127.0.0.1:8317/v1/models'
$probeHdr   = @{ Authorization = 'Bearer <PROXY-KEY>' }

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

# /s: cmd remove as aspas externas; o resto fica com os caminhos entre aspas
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
