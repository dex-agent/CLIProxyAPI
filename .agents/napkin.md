# Napkin — CLIProxyAPI

Ideias/táticas brutas desta sessão (promoção → GATILHOS-VIVOS quando validadas).

- (W-1) Go não no PATH do Windows — toolchain vivendo no module cache `go/pkg/mod/golang.org/toolchain@...`; acha-se por telemetria `AppData/Roaming/go/telemetry`.
- (W19) `rg` com o glob negativo `!**/.agents/**` zera qualquer busca enraizada em `~/.agents/...` (skills, workflow, memórias): o glob casa com o caminho da própria raiz. Medido por A/B em 2026-11-23; o mesmo glob numa raiz fora do `.agents` funciona. Para excluir uma subpasta, use glob relativo à raiz (ex.: `!**/TRACKER/**`) e confira a lista com um controle positivo.
- (W19) `sanitizar-scan.py --file` resolve o caminho pelo diretório corrente, não pelo `--root`: caminho relativo vira `erro-leitura`. Passar caminho absoluto.
- (W20) No Windows, `bash` chamado de dentro do Python cai no lançador do WSL (`System32\bash.exe`), que sai com 1 sem rodar nada. Um "esperado 1" passa sozinho. Chamar pelo caminho do Git (`$EXEPATH/bin/bash.exe`) e ler a saída antes de acreditar.
- (W20) O valor de controle de um gate de push precisa estar nos commits que o remoto ainda não tem. Valor de commit já publicado não acende o hook.
