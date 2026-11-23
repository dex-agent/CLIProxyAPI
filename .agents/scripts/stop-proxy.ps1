# stop-proxy.ps1 - stops the CLIProxyAPI instance that belongs to this repository.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\stop-proxy.ps1
#
# Only processes whose executable path is the proxy binary of this repo are stopped, so
# whatever else listens on port 8317 is never killed by mistake.
# Idempotent (R14): if nothing is running, it answers JA_PARADO and exits 0.
# To restart: run this script and then start-proxy.ps1. The hot-reload of the proxy does not
# remove models, so a config change that removes one needs this pair.

$ProgressPreference = 'SilentlyContinue'

$repoRoot  = 'C:\CodexProjetos\CLIProxyAPI'
$proxyPath = Join-Path $repoRoot 'cli-proxy-api.exe'

function Get-PortOwner {
    $conn = Get-NetTCPConnection -State Listen -LocalPort 8317 -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($conn) { return $conn.OwningProcess }
    return $null
}

function Get-ProxyProcesses {
    return @(Get-Process -Name 'cli-proxy-api' -ErrorAction SilentlyContinue | Where-Object { $_.Path -eq $proxyPath })
}

$procs = Get-ProxyProcesses
if ($procs.Count -eq 0) { Write-Output 'JA_PARADO'; exit 0 }

$ids = ($procs | ForEach-Object { $_.Id }) -join ','
foreach ($p in $procs) { Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue }
for ($i = 0; $i -lt 20; $i++) {
    Start-Sleep -Milliseconds 250
    if ((Get-ProxyProcesses).Count -eq 0) { break }
}

$owner = Get-PortOwner
if ($owner) {
    $name = (Get-Process -Id $owner -ErrorAction SilentlyContinue).ProcessName
    Write-Output ("PORTA_8317_OCUPADA_POR pid=$owner nome=$name (nao e este proxy; nada mais foi encerrado)")
    exit 1
}
Write-Output ('PARADO pid=' + $ids + ' porta=8317 livre')
exit 0
