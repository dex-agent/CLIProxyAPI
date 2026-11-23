# ESTACIONAMENTO — CLIProxyAPI

| Item | Owner | Quando | Nota |
|---|---|---|---|
| (vazio) | — | — | nada estacionado |

| Item | Owner | Quando | Nota |
|---|---|---|---|
| Declarar SUITE mínima no `tools/hooks/merge-check.conf` | dono | próximo bloco de trabalho | proposta: os pacotes verdes do W6 menos os 6 vermelhos — ex. `go test ./internal/translator/... ./internal/thinking/... ./internal/registry/... ./internal/usage/... ./sdk/translator/...` (102 pacotes ok em W6); até lá o gate avisa e NÃO bloqueia (SUITE="") |
