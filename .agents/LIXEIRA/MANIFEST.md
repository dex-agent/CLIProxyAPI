# MANIFEST — LIXEIRA (nada apagado sem garimpo prévio)

| Resíduo | Origem | Descarte | Motivo | Valor resgatado antes |
|---|---|---|---|---|
| `test-output` (109.275.648 bytes, binário Windows) | W6 build (argv do dono, exit 0) | 2026-11-22 | artefato reconstruível em 1 comando (`CGO_ENABLED=0 go build -o test-output ./cmd/server`) | receipt `W6-build-test.json` com tamanho/exit/argv |
| bash.exe.stackdump | crash do Git Bash no loop iconv W2 | 2026-11-22 | crash dump reconstruível, zero valor | causa raiz documentada em W2 (paths com \r do python print) |
| bash.exe.stackdump | crash do Git Bash (comando longo cancelado) | 2026-11-22 | crash dump, zero valor | causa: timeouts de shell longo; nada resgatavel |
