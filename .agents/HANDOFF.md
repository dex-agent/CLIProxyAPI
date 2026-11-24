# HANDOFF — CLIProxyAPI

Última atualização: 2026-11-24

## Estado
Arqueologia W-1..W10 executada (tier COMPLETO, 2405 fontes Go/143k linhas). O fork foi apagado pelo dono e recriado em 2026-11-23 com os commits da casa sobre o upstream `6eb8554f` (o upstream já avançou; não mesclado). Estado vivo atual: `ACTIVE.md`.

## Feito
- W-1..W5 fechados com receipts em `.agents/receipts/` (W1 inventário, W2 encoding 3 camadas, W3 grafo Tarjan, W4 hidden, W5 segredos).
- W6: build VERDE (exit 0 sem pipe); test VERMELHO honesto — 9 falhas classificadas (8 ambiente-Windows, 1 golden drift REAL) em `W6-build-test.json`.
- W7: CRG 2.4.0 build verde (tree-sitter-go nativo, SEM feeder) + graphify rico (36.327 nós) + grafo_gate **5/6 verde, exit 1 por 1 achado real** (span 1585L — pódio).
- W8: pódio completo com arquivo:linha (gocyclo 28.660 rotinas, cobertura 100%).
- W9/W10: INDEX.md + DEPENDENCIES.md raiz, GATILHOS-VIVOS/HANDOFF/PENDENTES/LIXEIRA, memórias V2 (dex-memoria scope=project), commits locais por bloco.

## Não feito / pendente (owner)
- Correção do golden drift e das falhas Windows → upstream router-for-me (PENDENTES.md com rota `dex-gerar-issues-git`).
- `.gitattributes` pin (proposta, decisão upstream).
- Histórico antigo: continua acessível no GitHub (rede de forks). O dono decidiu em 2026-11-23 não pedir a remoção ao suporte — ver W18 abaixo.

## Retomada
1. Ler GATILHOS-VIVOS → 2. `source .agents/scripts/go-env.sh` → 3. receipts em `.agents/receipts/` → 4. grafo fresco? `code-review-graph status`.

## W11 (2026-11-22 tarde) — instalação viva
- Proxy no ar: `./cli-proxy-api.exe --config config.yaml` (127.0.0.1:8317; key em config.yaml local). Reiniciar após reboot: mesmo comando (server não é serviço).
- Provider CLIProxyAPI no ZCode picker (12 modelos antigravity). Nomes com sufixo -high/-tiered/-xhigh são os IDs reais do catálogo.
- E2E: 3 classes testadas com resposta. Receipts W11-*.
- Rota B (decisão gemini-zcode 261122): este provider serve testes/uso pontual — NÃO propõe substituir elenco ZCode.

## W16 (2026-11-22 noite) — provider ZCode FUNCIONANDO
- Chat do ZCode responde via CLIProxyAPI/gemini-4-argon (E2E real, print do dono).
- Se o proxy parar: `powershell -File .agents/scripts/start-proxy.ps1` (detached; nao pode ser filho do shell do host).
- Se voltar Reconnecting: ler `auths/logs/error-v1-*.log` (body real) antes de qualquer teoria.
- Camadas ja aplicadas no config.yaml: model-alias(fork), cooldown disabled, sensitive-patterns-replace, request-log+logging-to-file. user_agent no auth JSON.
- Ressalva: o filtro do Google e por conteudo — mensagens sobre seguranca/CTF podem dar 429.

## W17 (2026-11-23) — OpenCode Go direto + grupo "Gratis (todos)"
- Subir o proxy: `powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1` (idempotente: responde JA_ATIVO se ja estiver no ar). Nao usar `./cli-proxy-api.exe` direto do shell do ZCode: morre no restart.
- `debug` e `request-log` do proxy estao DESLIGADOS de novo (gravavam corpo de cada request em disco). Para diagnosticar: ligar, reproduzir, ler `auths/logs/`, desligar.
- Provider "Gratis (todos)" no ZCode = 14 gratuitos via proxy. Ressincronizar (3 comandos, nesta ordem): `python -I -X utf8 .agents/scripts/free_aggregator.py setup-proxy` -> `stop-proxy.ps1` e depois `start-proxy.ps1` (o hot-reload nao remove modelo) -> `register-zcode`. O `setup-proxy` consulta o catalogo vivo do OpenRouter e deixa de fora os aposentados.
- OpenCode Go: token OAuth expira em 2026-12-23. Renovar: `python -I -X utf8 .agents/scripts/refresh_opencode_go_token.py` (atualiza os 3 providers do ZCode e o upstream do proxy; depois reiniciar os dois).
- Decisoes do dono no console do OpenCode (Settings > Privacy): Regions = Global libera DeepSeek e longcat; Training libera muse-spark e iceman-contributor. Ver PENDENTES 8 e 9.
- `.agents/receipts/` e local: tem corpo de requisicao e e-mail. Nunca versionar (ficha RECEIPTS-NAO-VERSIONADOS no hub).

## W18 (2026-11-23) — fork recriado limpo; histórico antigo ainda acessível
- Proxy: ligar `start-proxy.ps1`, desligar `stop-proxy.ps1`, reiniciar = os dois nessa ordem. A chave de acesso é lida do `config.yaml`; nenhum script fixa o valor.
- O gate antes do push virou hook em 2026-11-24 (ficha `RECEIPTS-NAO-VERSIONADOS`): `tools/hooks/pre-push` chama o shim `.agents/scripts/push_gate.py`, que roda a ferramenta da casa `range_gate.py` (skill dex-sanitizar-dados-pessoais) sobre os blobs novos. Os dois scripts antigos do gate saíram do repo.
- Para reescrever só os commits da casa: `git filter-repo --force --refs 6eb8554f..main --replace-text <arquivo>`. O modo parcial preserva a ancestridade com o upstream; o modo integral reescreve tudo e rompe o parentesco.
- Histórico antigo (com e-mail e corpos de requisição) continua acessível no GitHub pelas duas namespaces. Apagar fork não purga rede de forks. O dono decidiu em 2026-11-23 não pedir a remoção ao suporte (resíduo aceito depois do inventário `W18-exposed-inventory.txt`: nenhuma credencial de serviço externo); o texto do pedido continua em `.agents/receipts/W18-support-ticket.txt` (local) caso reabra. Medição em `W18-old-history-reach.txt`.
- Nunca citar, em arquivo versionado, o SHA de um commit do histórico antigo.

## W19 (2026-11-23 noite) — gate de pré-push com indicação de reuso aberta
- Indicação de reuso do gate aberta no tracker do registry de skills (`~/.agents/skills/.agents/TRACKER`, `ISSUE-LOCAL-0066`, P2).
- Rerun do gate em 2026-11-24 00:06 UTC sobre `6eb8554f..HEAD`: exportação completa e nenhuma credencial local nos blobs (recibo local `W19-push-gate-rerun.txt`).
- Indicação de reuso aberta no tracker do registry de skills (`~/.agents/skills/.agents/TRACKER`, `ISSUE-LOCAL-0066`). O dono deu GO PADRAO na mesma noite; a execução está em W20.

## W20 (2026-11-24) — gate de pré-push é ferramenta da casa e virou hook
- O gate virou ferramenta da casa: `range_gate.py` na skill `dex-sanitizar-dados-pessoais` (núcleo genérico, 24 testes). Este repo guarda só o shim `.agents/scripts/push_gate.py`, com as fontes de segredo desta máquina: chave e api-keys do `config.yaml`, token do OpenCode e token do `gh`.
- Hook `tools/hooks/pre-push` (`core.hooksPath` já aponta para lá): bloqueia o push quando um valor secreto declarado aparece nos blobs novos e falha fechado se o gate não rodar. Ele roda também no `git push --dry-run`. Escape declarado: `PUSH_GATE_SKIP=1`.
- Triagem de dado pessoal antes de um push arriscado: `python -I -B -X utf8 .agents/scripts/push_gate.py . 6eb8554f..HEAD --triage`. A saída é mascarada; o julgamento é da sessão.
- Teste do hook: `git push --dry-run fork main` (verde). `PUSH_GATE_EXTRA_ENV=PG_TEST PG_TEST=ISSUE-LOCAL-0066 git push --dry-run fork main` (vermelho; nada é enviado). O valor do controle precisa estar nos commits novos, não no que o remoto já tem.

## W21 (2026-11-24) — primeira release do fork e recorte do `.agents`
- **Release `v8.1.1-dex.1` publicada** (https://github.com/dex-agent/CLIProxyAPI/releases/tag/v8.1.1-dex.1): 9 pacotes + `checksums.txt`, nota curta de 29 linhas. O fork não altera nenhum arquivo Go sobre a v8.1.1: o binário é o do upstream. **`darwin-arm64` não foi gerado**: o runner `macos-15` ficou 15 minutos na fila e foi cancelado, 2 vezes. Trilho: `.agents/PLAN-TASKS/2026-11-24-publicar-release-do-fork.md`.
- **Tags no fork**: `v8.1.1-dex.1` (alvo `ec7670aa0`) e a tag de base `upstream-v8.1.1` (alvo `6eb8554f0`). A tag de base existe para o workflow achar uma tag anterior: sem ela o changelog tem 4969 entradas e a criação da release cai com HTTP 422 (`body is too long`). **Não apagar.**
- **O primeiro push de uma tag pode não disparar o Actions no fork** (medido 1 vez; causa não identificada). Antes de concluir que o workflow quebrou, conferir `gh run list --repo dex-agent/CLIProxyAPI`. Se não houver run, a saída usada foi reaplicar a permissão de Actions e reenviar a tag, com aprovação do dono.
- **`.gitignore`**: completado com as entradas padrão (`.env.*`, `*.log`, `*.tmp` etc.) e recortado com a `dex-ignore`. A regra nua `.agents` foi removida; `.agents/*` segue como padrão e só o estado vivo é re-incluído. Arquivo novo em `PLAN-TASKS`, `memorias`, `.dex-memoria`, `ESTACIONAMENTO` e `LIXEIRA` agora aparece no `git status`. `scripts/`, `receipts/`, `TEMP/` e os grafos seguem ignorados; script novo entra com `git add -f` e conferência de dado pessoal.
- **Instalação em outra máquina**: baixar o pacote da release e conferir com `checksums.txt`. Mac Apple Silicon: compilar do clone (Go 1.26+) até o pacote existir.
- **Runs vermelhos esperados no fork**: `docker-image` em toda tag `v*` (sem segredos do Docker Hub) e o run da própria tag de base.
