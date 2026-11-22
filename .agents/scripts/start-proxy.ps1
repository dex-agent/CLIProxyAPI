# start-proxy.ps1 - inicia o CLIProxyAPI desacoplado do shell (sobrevive ao fechamento do host)
# Uso: powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1
# Idempotente: se a porta 8317 ja responde, nao duplica processo (R14 IDEMPOTENCIA).
$repoRoot   = 'C:\CodexProjetos\CLIProxyAPI'
$proxyPath  = Join-Path $repoRoot 'cli-proxy-api.exe'
$configPath = Join-Path $repoRoot 'config.yaml'
$logDir     = Join-Path $repoRoot '.agents\receipts'
$logOut     = Join-Path $logDir 'proxy-run.log'
$logErr     = Join-Path $logDir 'proxy-run.err.log'

if (-not (Test-Path -LiteralPath $proxyPath))  { throw "binario ausente: $proxyPath" }
if (-not (Test-Path -LiteralPath $configPath)) { throw "config ausente: $configPath" }

# guard de idempotencia: porta respondendo = ja esta no ar
try {
    $probe = Invoke-WebRequest -Uri 'http://127.0.0.1:8317/v1/models' -Headers @{ Authorization = 'Bearer <PROXY-KEY>' } -TimeoutSec 4 -UseBasicParsing
    if ($probe.StatusCode -eq 200) { Write-Output 'JA_ATIVO http=200'; exit 0 }
} catch { }

# detached: Start-Process desacopla do shell chamador (nao morre com o host)
Start-Process -FilePath $proxyPath `
    -ArgumentList '--config', $configPath `
    -WorkingDirectory $repoRoot `
    -WindowStyle Hidden `
    -RedirectStandardOutput $logOut `
    -RedirectStandardError $logErr | Out-Null

for ($i = 0; $i -lt 20; $i++) {
    Start-Sleep -Milliseconds 500
    try {
        $probe = Invoke-WebRequest -Uri 'http://127.0.0.1:8317/v1/models' -Headers @{ Authorization = 'Bearer <PROXY-KEY>' } -TimeoutSec 2 -UseBasicParsing
        if ($probe.StatusCode -eq 200) { Write-Output "INICIADO http=200 log=$logOut"; exit 0 }
    } catch { }
}
Write-Output "FALHOU_APOS_10S ver=$logErr"
exit 1
