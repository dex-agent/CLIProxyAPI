# DEPENDENCIES — CLIProxyAPI

## Grafo interno (fechamento real via `go list -deps`, 2026-11-22, HEAD 6eb8554f)

- **137 pacotes internos · 761 arestas · 0 ciclos** (compilador Go proíbe ciclo de import — confirmado por SCC/Tarjan)
- **808 pacotes no fechamento total** (inclui stdlib + 3rd-party)
- hubs de fan-in: `internal/util` (67) · `internal/config` (39) · `internal/registry` (39) · `internal/interfaces` (34) · `internal/thinking` (32) · `internal/constant` (32)
- fan-out: `internal/runtime/executor/helps` (41) · `internal/api` (36) · `internal/runtime/executor` (34) · `sdk/cliproxy` (34)

```text
cmd/server ──▶ internal/api ──▶ sdk/api/handlers/* ──▶ internal/runtime/executor/* ──▶ internal/translator/* ──▶ common/util
     │               │                                        │
     └─▶ sdk/cliproxy ──▶ auth (conductor_*: selection/cooldown/refresh/execution)   └─▶ registry (model registry + updater)
```

Estrutura canônica do AGENTS.md vale: thinking = "representação canônica → tradução por provider" (`internal/thinking`).

## 3ª-parceria (2 colunas)

Todas as dependências Go são **estáticas** (entram no binário). Nenhuma vendorizada (`vendor/` ausente na raiz). Fonte completa: `.agents/receipts/W4-hidden.json` (111 requires no go.mod).

| entra no binário | presente no repo | licença |
|---|---|---|
| TODAS via link estático | go.mod/go.sum somente | verificado no module cache: 96/111 com LICENSE em nome padrão; **15 sem licença nos nomes padrão** (moego, flock, sonic/bytedance ×4, go-json, base64x/iasm, go-internal, go-winio, go-crypto, xxHash, golang-asm, x/arch) — confirmar licença no upstream antes de redistribuir |

## Toolchain

| Ferramenta | Versão | Nota |
|---|---|---|
| Go | 1.26.10 | **não está no PATH**; vive em `%USERPROFILE%\go\pkg\mod\golang.org\toolchain@v0.0.1-go1.26.10.windows-amd64\bin\go.exe` (ver `.agents/scripts/go-env.sh`) |
| code-review-graph | 2.4.0+dex.3 | grafo estrutural em `.agents/CODE-REVIEW-GRAPH` (tree-sitter nativo) |
| gocyclo | go/bin | métricas CC, cobertura 100% (28.660 rotinas) |
| graphify | 0.9.105 | grafo rico 36.327 nós/485k arestas em `graphify-out/` |

## Status de build (2026-11-22)

- build `./cmd/server`: **VERDE** (exit 0, binário 109MB CGO_ENABLED=0)
- `go test ./...`: **VERMELHO** (9 falhas/6 pacotes; 8 ambiente-Windows, 1 drift de golden REAL — ver `.agents/receipts/W6-build-test.json`)
- CI upstream roda **apenas build** (`pr-test-build.yml` sem `go test`)
