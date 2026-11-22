# ACTIVE — CLIProxyAPI Arqueologia (sessão 2026-11-22)

**Missão**: arqueologia completa W-1..W10 (`arqueologia-warmup-base`), tier decidido no W0, read-only no fonte até W6 verde com receipt JSON.

## Estado vivo
- **Commit de fechamento**: 04671df9 (docs archaeology, 6 arquivos raiz)
- **Fase**: W-1 concluído (padrão instalado, capacidade inventariada)
- **Tier**: decidir no W0 (denominador = arquivos Go)
- **Toolchain**: Go 1.26.10 em `%USERPROFILE%\go\pkg\mod\golang.org\toolchain@v0.0.1-go1.26.10.windows-amd64\bin\go.exe` (NÃO está no PATH — usar path absoluto ou exportar)
- **CRG**: code-review-graph 2.4.0+dex.3 (probe exit 0, `--version` medido)
- **Repo**: main @ 6eb8554f, limpo, 36 commits atrás absorvidos hoje (pull ff)

## Lentes ativas
chato · bruninha-agulha (via burrinha redirector) · critico-cetico · questionador · interrogador-documental · entrevista-me

## Rota viva vs legada
A definir no W0 (upstream router-for-me; branch dev existe no remote).

## W11 — Instalação + provider ZCode (2026-11-22, tar)
- **Instalado**: `cli-proxy-api.exe` (build exit 0) + `config.yaml` mínimo (127.0.0.1:8317, key <PROXY-KEY>, gitignored) + OAuth antigravity OK (`auths/antigravity-REDACTED.json`).
- **Server VIVO** em background (receipt `.agents/receipts/W11-server-run.txt`).
- **E2E provado**: gemini-3-flash (não-stream), gemini-3.8-flash-high e claude-sonnet-5-5-high (stream "pong") — nomes conferidos corretos contra o catálogo do proxy.
- **Provider ZCode cadastrado**: CLIProxyAPI (providerId 398edcea…), 12 modelos, backup `provider_config.json.backup-20261122-cliproxyapi`; validado contra doc oficial (api.type enum) + hot-reload (#pollOnce).
- **Ouro garimpado**: nota citável `zcode-provider-config-estrutura-v2` (emit exit 0) + memória tema zcode (COMMITTED 20/20) + memória project instalação (8/8 lote válido).
