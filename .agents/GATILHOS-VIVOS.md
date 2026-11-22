# GATILHOS-VIVOS — CLIProxyAPI

| Gatilho | Quem | Quando lembrar | Fonte viva / ação |
| --- | --- | --- | --- |
| GO-TOOLCHAIN-FORA-PATH | sessão do repo | qualquer build/teste Go no CLIProxyAPI | [Fonte viva](<.agents/scripts/go-env.sh%20%28repo%29%20+%20%USERPROFILE%/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.10.windows-amd64/bin/go.exe>) · Binário go NÃO está no PATH da máquina; toolchain 1.26.10 (exata do go.mod) vive no module cache |
| TESTE-VERMELHO-WINDOWS | sessão do repo | rodar go test ./... e ver 9 falhas / 6 pacotes | [Fonte viva](<.agents/receipts/W6-build-test.json%20+%20.agents/receipts/W6-pluginhost-retest.txt>) · 9 falhas conhecidas de go test ./... (HEAD 6eb8554f, 2026-11-22): 8 ambiente-Windows (file-lock TempDir em home/kvstore/pluginhost; TUI/TTY timeout 30s; links POSIX em internal/store) + 1 golden drift REAL (TestToolSearchDisabledMatchesDevGolden) |
| CI-SOMENTE-BUILD | sessão do repo | confiar em CI verde do CLIProxyAPI | [Fonte viva](<.github/workflows/pr-test-build.yml%20+%20.agents/receipts/W1-inventario-go.txt>) · pr-test-build.yml roda apenas go build + rm — NÃO roda go test |
| ENC-CRLF-LOJA-LF | sessão do repo | editar fonte ou investigar EOL no CLIProxyAPI | [Fonte viva](<.agents/receipts/W2-encoding-census.json>) · Working 100% CRLF, loja i/lf limpa, core.autocrlf=true (system), SEM .gitattributes; 125 UTF-8 válidos (mandarim em internal/tui/i18n.go) |
| CRG-GRAFO-LOCAL | sessão do repo | review estrutural ou análise de impacto no CLIProxyAPI | [Fonte viva](<.agents/CODE-REVIEW-GRAPH/%20+%20.agents/CODE-REVIEW-GRAPH-INDEX.md>) · Grafo CRG 2.4.0+dex.3 em .agents/CODE-REVIEW-GRAPH (2463 arquivos, 35497 nós, 646569 arestas, tree-sitter-go NATIVO, built 6eb8554f); doctor: já segura todo arquivo mudado desde então |
| HOTSPOT-GEMINI-RESPONSES | sessão do repo | refatorar translator gemini ou escolher alvo de refactor | [Fonte viva](<.agents/receipts/W8-gocyclo.txt%20%28p%C3%B3dio%20completo,%20gocyclo%2028660%20rotinas,%20cobertura%20100%%29>) · ConvertGeminiResponseToOpenAIResponses CC348/1585L (gemini_openai-responses_response.go:381-1966) = duplo coroa com gate de span; depois streamCodexDuplex CC325, MarkResult CC314; god file conductor_cooldown.go 4217L/150fn |
| PIPE-EXIT-FALSO | sessão do repo | medir qualquer exit/gate/contagem nesta janela | [Fonte viva](<disciplina%20de%20execu%C3%A7%C3%A3o%20+%20.agents/GATILHOS-VIVOS.md%20%28esta%20ficha%29>) · 3 falsos na mesma sessão (iconv 125/125, find de fóssil, diff de branch) todos por pipe engolindo erro/código de exit |
| MERGE-CHECK-HOOK-PRE-MERGE | Hook do repo (tools/hooks/pre-merge-commit, executado pelo git via core.hooksPath) | Todo git merge local; e merge remoto via PR (nesse caso o agente roda o merge-check completo ANTES do dono clicar em merge — hook local não cobre PR). | [Fonte viva](<tools/hooks/pre-merge-commit%20+%20tools/hooks/merge-check.conf%20%28SUITE%29%3B%20contracts/schemas%20do%20merge-check%20no%20fork%20code-review-graph%202.4.0+dex.3>) · Todo git merge passa pelo gate merge-check tres vias (texto + grafo + suíte) antes de gerar o commit de merge; escapes: MERGE_CHECK_SKIP=1 ou git merge --no-verify. |
| STALENESS-ARTEFATOS-DERIVADOS | sessão do repo (leitor/citador de qualquer artefato derivado) | ANTES de qualquer leitura/citação do artefato: janela fria, re-arqueologia, decisão que cita "o grafo diz X", fechamento que conta métricas de derivado. | [Fonte viva](<invent%C3%A1rio%20vivo%20desta%20ficha%20%28comandos%20abaixo%29%20+%20.agents/GATILHOS-VIVOS.md%20+%20receipts%20.agents/receipts/>) · Artefatos derivados (grafo CRG, grafo rico graphify, INDEX.md, receipts/mapas datados) fotografam a fonte num instante; antes de LER/CITAR qualquer número deles, medir staleness com 3 números. |


Hub quente de retomada: gatilhos promovidos com validação (formato canônico 5W2H pelo helper `dex-5w2h-gatilhos-vivo`; mantém fonte viva; NÃO substitui L1/L2, Trilho, ACTIVE/HANDOFF).

## 🔥 GO-TOOLCHAIN-FORA-PATH

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: Binário go NÃO está no PATH da máquina; toolchain 1.26.10 (exata do go.mod) vive no module cache
- **Por que**: build/teste falha com go: command not found e alguém re-instala Go desnecessariamente
- **Onde**: [Fonte viva](<.agents/scripts/go-env.sh%20%28repo%29%20+%20%USERPROFILE%/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.10.windows-amd64/bin/go.exe>)
- **Quando**: qualquer build/teste Go no CLIProxyAPI
- **Como**: source .agents/scripts/go-env.sh e usar $GO com CGO_ENABLED=0. Re-localizar via AppData/Roaming/go/telemetry se o cache mudar.
- **Quanto**: 0s (source de script)
- **E se??**: E se?? o module cache for limpo (go clean -modcache)? → toolchain some: baixar Go 1.26.x oficial para C:/tools e atualizar go-env.sh

## 🔥 TESTE-VERMELHO-WINDOWS

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: 9 falhas conhecidas de go test ./... (HEAD 6eb8554f, 2026-11-22): 8 ambiente-Windows (file-lock TempDir em home/kvstore/pluginhost; TUI/TTY timeout 30s; links POSIX em internal/store) + 1 golden drift REAL (TestToolSearchDisabledMatchesDevGolden)
- **Por que**: re-abrir investigação já classificada ou tratar falha de ambiente como regressão de código
- **Onde**: [Fonte viva](<.agents/receipts/W6-build-test.json%20+%20.agents/receipts/W6-pluginhost-retest.txt>)
- **Quando**: rodar go test ./... e ver 9 falhas / 6 pacotes
- **Como**: Ler o receipt ANTES de agir; build VERDE (exit 0); pendências com owner em .agents/PENDENTES.md.
- **Quanto**: leitura de 1 receipt (segundos)
- **E se??**: E se?? uma das 9 falhas mudar de classe após update? → re-classificar pelo receipt novo: rótulo vale enquanto a fonte viva confere

## 🔥 CI-SOMENTE-BUILD

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: pr-test-build.yml roda apenas go build + rm — NÃO roda go test
- **Por que**: confiar que CI verde prova testes quando não prova (regressão de golden passou invisível no upstream)
- **Onde**: [Fonte viva](<.github/workflows/pr-test-build.yml%20+%20.agents/receipts/W1-inventario-go.txt>)
- **Quando**: confiar em CI verde do CLIProxyAPI
- **Como**: CI verde = prova de build somente; teste só local (go test ./...).
- **Quanto**: 0 (fato de contrato)
- **E se??**: E se?? o upstream adicionar job de teste? → re-medir o workflow e atualizar esta ficha na mesma sessão que descobrir

## 🔥 ENC-CRLF-LOJA-LF

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: Working 100% CRLF, loja i/lf limpa, core.autocrlf=true (system), SEM .gitattributes; 125 UTF-8 válidos (mandarim em internal/tui/i18n.go)
- **Por que**: commitar com autocrlf=false colapsa a loja para CRLF (contaminação de 2.5k arquivos)
- **Onde**: [Fonte viva](<.agents/receipts/W2-encoding-census.json>)
- **Quando**: editar fonte ou investigar EOL no CLIProxyAPI
- **Como**: Nunca commitar com autocrlf=false nesta máquina; pin *.go text eol=lf é proposta pendente no upstream.
- **Quanto**: 0 (fato de contrato)
- **E se??**: E se?? um .gitattributes aparecer num pull futuro? → re-medir o census W2 e atualizar a ficha

## 🔥 CRG-GRAFO-LOCAL

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: Grafo CRG 2.4.0+dex.3 em .agents/CODE-REVIEW-GRAPH (2463 arquivos, 35497 nós, 646569 arestas, tree-sitter-go NATIVO, built 6eb8554f); doctor: já segura todo arquivo mudado desde então
- **Por que**: review estrutural sem grafo re-analisa do zero, ou cita número de mapa velho (falso verde)
- **Onde**: [Fonte viva](<.agents/CODE-REVIEW-GRAPH/%20+%20.agents/CODE-REVIEW-GRAPH-INDEX.md>)
- **Quando**: review estrutural ou análise de impacto no CLIProxyAPI
- **Como**: Consultar ANTES de review estrutural; refresh: code-review-graph update --data-dir .agents/CODE-REVIEW-GRAPH; staleness pela ficha STALENESS-ARTEFATOS-DERIVADOS.
- **Quanto**: update incremental ~minuto
- **E se??**: E se?? o doctor acusar cópia divergente na máquina? → hook e shell resolvem pelo PATH (dex.3, fork da casa); cópia uv dex.1 é ressalva de máquina, não do repo

## 🔥 HOTSPOT-GEMINI-RESPONSES

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: ConvertGeminiResponseToOpenAIResponses CC348/1585L (gemini_openai-responses_response.go:381-1966) = duplo coroa com gate de span; depois streamCodexDuplex CC325, MarkResult CC314; god file conductor_cooldown.go 4217L/150fn
- **Por que**: escolher alvo de refactor sem os números ou re-medir o pódio inteiro a cada decisão
- **Onde**: [Fonte viva](<.agents/receipts/W8-gocyclo.txt%20%28p%C3%B3dio%20completo,%20gocyclo%2028660%20rotinas,%20cobertura%20100%%29>)
- **Quando**: refatorar translator gemini ou escolher alvo de refactor
- **Como**: Usar o pódio medido; staleness da métrica segue STALENESS-ARTEFATOS-DERIVADOS.
- **Quanto**: 0 (pódio já medido)
- **E se??**: E se?? a função-monstro for dividida no upstream? → re-medir gocyclo e atualizar o pódio na mesma sessão que tocar o arquivo

## 🔥 PIPE-EXIT-FALSO

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo
- **O quê**: 3 falsos na mesma sessão (iconv 125/125, find de fóssil, diff de branch) todos por pipe engolindo erro/código de exit
- **Por que**: declarar resultado de pipeline quebrado como fato (falso verde ou falso vermelho)
- **Onde**: [Fonte viva](<disciplina%20de%20execu%C3%A7%C3%A3o%20+%20.agents/GATILHOS-VIVOS.md%20%28esta%20ficha%29>)
- **Quando**: medir qualquer exit/gate/contagem nesta janela
- **Como**: Exit SEMPRE medido sem pipe: comando > arquivo 2>&1; echo exit=$?. Contagem idem (wc -l no arquivo).
- **Quanto**: 0 (disciplina de execução)
- **E se??**: E se?? o comando só existir em pipeline? → redirecionar a SAÍDA para arquivo e medir exit/contagem do arquivo, nunca confiar no código do pipe

## 🔥 MERGE-CHECK-HOOK-PRE-MERGE

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: Hook do repo (tools/hooks/pre-merge-commit, executado pelo git via core.hooksPath)
- **O quê**: Todo git merge passa pelo gate merge-check tres vias (texto + grafo + suíte) antes de gerar o commit de merge; escapes: MERGE_CHECK_SKIP=1 ou git merge --no-verify.
- **Por que**: Sem gate, merge que quebra nasce: conflito semântico (grafo/risco) e regressão de suíte entram na main invisíveis — o CI deste repo roda apenas build, sem go test.
- **Onde**: [Fonte viva](<tools/hooks/pre-merge-commit%20+%20tools/hooks/merge-check.conf%20%28SUITE%29%3B%20contracts/schemas%20do%20merge-check%20no%20fork%20code-review-graph%202.4.0+dex.3>)
- **Quando**: Todo git merge local; e merge remoto via PR (nesse caso o agente roda o merge-check completo ANTES do dono clicar em merge — hook local não cobre PR).
- **Como**: hook: não-merge exit 0 silencioso; SUITE vazia -> avisa e NÃO bloqueia (nunca bloqueia por falta de suíte usável); sem resolução manual -> code-review-graph merge-check --repo . --base BASE --ours HEAD --theirs MERGE_HEAD --test-failure-exit 1 -- $SUITE (exit 0 passa; 1 bloqueia: conflito texto/semântico; 2 não bloqueia: suíte doente não é veredito de integração); MERGE_MSG com # Conflicts -> camada comportamental direta ($SUITE no worktree resolvido) porque a textual refaria o merge sem a resolução humana.
- **Quanto**: Custo: 1 execução do merge-check por merge (laboratório descritível em minutos no tamanho atual); economiza o merge-que-nasce-quebrado e o re-trabalho de revert.
- **E se??**: E se?? o merge vier de PR (GitHub), fora do hook local? → hook local não cobre: o agente roda o merge-check completo ANTES do clique de merge e cola o receipt no PR
- **E se??**: E se?? o índice CRG estiver stale? → não invalida o gate: merge-check constrói laboratório próprio em temp (merge-tree + checkouts); staleness vigia o que se CITA, não o que se gata — ver STALENESS-ARTEFATOS-DERIVADOS
- **E se??**: E se?? a SUITE ficar vazia por muito tempo? → gate fica inerte (avisa e passa): pendência de suíte mínima está em PENDENTES/ESTACIONAMENTO com owner/quando — um o-que sem um-quando é nunca
- **E se??**: E se?? duas cópias do code-review-graph divergirem na máquina? → hook resolve pelo PATH (2.4.0+dex.3, fork da casa); doctor 261122 mediu cópia uv 2.4.0+dex.1 divergente — ressalva de máquina, não do repo

## 🔥 STALENESS-ARTEFATOS-DERIVADOS

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão do repo (leitor/citador de qualquer artefato derivado)
- **O quê**: Artefatos derivados (grafo CRG, grafo rico graphify, INDEX.md, receipts/mapas datados) fotografam a fonte num instante; antes de LER/CITAR qualquer número deles, medir staleness com 3 números.
- **Por que**: Fonte mudou sem regen = leitura confiante em mapa antigo (falso verde); foto velha vira ruído confiável e decisão errada nasce de timestamp desatualizado.
- **Onde**: [Fonte viva](<invent%C3%A1rio%20vivo%20desta%20ficha%20%28comandos%20abaixo%29%20+%20.agents/GATILHOS-VIVOS.md%20+%20receipts%20.agents/receipts/>)
- **Quando**: ANTES de qualquer leitura/citação do artefato: janela fria, re-arqueologia, decisão que cita "o grafo diz X", fechamento que conta métricas de derivado.
- **Como**: comparar SEMPRE 3 números: (a) quando a FONTE mudou: git log -1 --format=%cI -- <escopo-indexado> (ou stat); (b) quando o ARTEFATO nasceu: doctor/timestamp interno (CRG: code-review-graph doctor; graphify: built_at_commit do graph.json; INDEX: commit que o tocou); (c) fonte > artefato => STALE => regenerar e SÓ ENTÃO citar. Inventário medido 261122: CRG .agents/CODE-REVIEW-GRAPH (doctor, regen: code-review-graph update --data-dir .agents/CODE-REVIEW-GRAPH), graphify-out/graph.json (built_at_commit, regen: graphify update .), INDEX.md raiz+.agents (fiscal dex-fechamento-projeto-atualizado superficie 4), receipts .agents/receipts (data no nome), MAPAS inexistente, PLAYBOOK inexistente (n-a).
- **Quanto**: Custo: 3 comandos read-only (~segundos) por citação material; economiza falso verde de decisão com mapa antigo.
- **E se??**: E se?? o repo não tiver git (stat/mtime como única origem)? → usar mtime das fontes vs timestamp interno do artefato; sem fonte comparável, declarar artefato não-consultável e nunca citar número dele
- **E se??**: E se?? o regenerador não estiver instalado? → declarar o artefato NÃO CONSULTÁVEL (nunca citar número dele) e estacionar a instalação com owner/quando — não regenerar por improviso
- **E se??**: E se?? check verde mas o conteúdo parecer errado? → verde de staleness não é prova de semântica: abrir a FONTE (fonte viva sempre vence memória) e conferir o número citado no código real
- **E se??**: E se?? o commit mais recente só tocou arquivos fora do escopo indexado? → medido 261122: 8a3f9dd tocou só .agents (ignorado) — doctor CRG declarou "holds every file changed since"; staleness é por ESCOPO, não por HEAD bruto
