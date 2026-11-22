# PENDENTES — CLIProxyAPI

<!-- PENDENTES:JSON:START -->
[
  {"id": "upstream-golden-drift", "status": "aberta", "nivel": "P1", "titulo": "Golden drift real: TestToolSearchDisabledMatchesDevGolden", "owner": "upstream router-for-me", "quando": "abrir item no tracker local via dex-gerar-issues-git", "evidencia": ".agents/receipts/W6-build-test.json"},
  {"id": "upstream-testes-windows", "status": "aberta", "nivel": "P2", "titulo": "8 falhas ambiente-Windows (file-lock/TUI-TTY/links POSIX)", "owner": "upstream router-for-me", "quando": "lote junto do golden drift", "evidencia": ".agents/receipts/W6-build-test.json"},
  {"id": "upstream-ci-sem-teste", "status": "aberta", "nivel": "P2", "titulo": "CI roda apenas build, sem go test", "owner": "upstream router-for-me", "quando": "item de tracker + proposta de job", "evidencia": ".agents/receipts/W1-inventario-go.txt"},
  {"id": "upstream-gitattributes-pin", "status": "aberta", "nivel": "P3", "titulo": ".gitattributes ausente (pin *.go text eol=lf)", "owner": "upstream router-for-me", "quando": "junto do lote", "evidencia": ".agents/receipts/W2-encoding-census.json"},
  {"id": "upstream-licencas-15", "status": "aberta", "nivel": "P3", "titulo": "15 deps sem LICENSE em nome padrao no module cache", "owner": "dono", "quando": "antes de qualquer redistribuicao", "evidencia": ".agents/receipts/W4-hidden.json"},
  {"id": "push-local", "status": "adiada", "nivel": "P2", "titulo": "Push dos commits locais de arqueologia", "owner": "dono", "quando": "aguarda ordem explicita", "evidencia": "git log 04671df9"}
]
<!-- PENDENTES:JSON:END -->

| # | Pendência | Owner | Quando | Evidência |
|---|---|---|---|---|
| 1 | Golden drift REAL: `TestToolSearchDisabledMatchesDevGolden` (claude_openai-responses_tool_search_disabled_test.go:90) — builder mudou +176 linhas no pull 6eb8554f e golden não acompanhou; atualizar golden ou reverter trecho | upstream router-for-me | abrir item no tracker local via `$dex-gerar-issues-git` (ISSUES-POR-REPO-DONO) | W6-build-test.json |
| 2 | Falhas ambiente-Windows (8: file-lock bolt/shadow ×4, TUI/TTY ×2, links POSIX ×2) — higiene de cleanup de handle + skip condicional de plataforma | upstream router-for-me | mesmo item de tracker (lote) | W6-build-test.json |
| 3 | CI sem `go test`: `pr-test-build.yml` só compila — regressões invisíveis (a golden drift teria sido pega) | upstream router-for-me | item de tracker + proposta de job de teste | W1 receipt + W6 |
| 4 | `.gitattributes` ausente — pin `*.go text eol=lf` evitaria contaminação de loja | upstream router-for-me | junto do lote 2 | W2 receipt |
| 5 | 15 deps sem LICENSE em nome padrão no module cache — confirmar licença upstream antes de redistribuir | dono/upstream | auditoria de release | W4-hidden.json |
| 6 | Push dos commits locais de arqueologia | **dono** | aguarda ordem | git log local |
