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
| ZCODE-ANTIGRAVITY-FILTRO-SYSTEM-PROMPT | sessão que operar o provider CLIProxyAPI no ZCode | provider custom Antigravity falha no chat do ZCode mas curl minimo responde 200 | [Fonte viva](<config.yaml%20-%3E%20oauth.providers.antigravity.sensitive-patterns-replace%3B%20bodies%20reais%20em%20auths/logs/error-v1-%2A.log%3B%20start%20.agents/scripts/start-proxy.ps1>) · 429 RESOURCE_EXHAUSTED do Antigravity em chat do ZCode mesmo com quota cheia = filtro de CONTEUDO no system prompt do ZCode, nao quota |
| RECEIPTS-NAO-VERSIONADOS | sessao do repo que for commitar ou enviar | todo commit ou push deste repo, em especial depois de criar recibo de diagnostico | [Fonte viva](<.agents/receipts/%20%28local%29%20e%20.gitignore%20%28o%20upstream%20ja%20ignora%20.agents%29>) · .agents/receipts/ guarda corpo de requisicao, logs com e-mail e capturas de tela de contexto: nunca entra no git, porque o fork dex-agent/CLIProxyAPI e publico |
| OPENCODE-GO-CLIENTE-EXTERNO | sessao que for usar o plano OpenCode Go fora do cliente OpenCode (ZCode, proxy, curl) | cadastrar, renovar ou diagnosticar o acesso ao OpenCode Go | [Fonte viva](<scripts%20register_opencode_go_zcode.py,%20register_oc_go_multi_protocol.py%20e%20refresh_opencode_go_token.py%20em%20.agents/scripts/>) · o endpoint e https://opencode.ai/inference/go/openai/v1 (o /go/ e obrigatorio) com o token OAuth do opencode.db e os headers x-opencode-session, x-opencode-project, x-opencode-directory e x-opencode-client; o ZCode aceita isso direto em api.headers, sem proxy |
| GRATIS-TODOS-RESSYNC | sessao que mantem o grupo de modelos gratuitos | quando um alias free-* devolver 404, ou depois de cada sync dos free do OpenRouter | [Fonte viva](<.agents/scripts/free_aggregator.py>) · o provider Gratis (todos) do ZCode so tem os modelos que o proxy expoe com alias free-or-* (OpenRouter) e free-oc-* (OpenCode Go); ele nao se atualiza sozinho |
| PROXY-WMI-SEM-JANELA | sessao que precisar do CLIProxyAPI no ar | antes de usar os providers CLIProxyAPI, xAI (CLIProxyAPI) e Gratis (todos) do ZCode | [Fonte viva](<.agents/scripts/start-proxy.ps1>) · o proxy sobe por start-proxy.ps1, que cria o processo via WMI com ShowWindow=0: fora da job do ZCode e sem janela de console |
| FORK-REDE-APAGAR-NAO-PURGA | dono do fork e sessao do repo que for publicar ou reescrever historico | antes de prometer que um historico exposto sumiu, antes de apagar ou recriar um fork e antes de citar um SHA antigo em arquivo versionado | [Fonte viva](<recibo%20local%20.agents/receipts/W18-old-history-reach.txt,%20texto%20do%20pedido%20em%20.agents/receipts/W18-support-ticket.txt%20e%20pendencia%20fork-dados-pessoais%20em%20.agents/PENDENTES.md>) · Apagar um fork nao remove os objetos inalcancaveis: a rede de forks compartilha o armazem com o upstream e o commit antigo segue acessivel pelas duas namespaces (medido em 2026-11-23: API, pagina e raw responderam 200 sem login) |


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

## 🔥 ZCODE-ANTIGRAVITY-FILTRO-SYSTEM-PROMPT

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessão que operar o provider CLIProxyAPI no ZCode
- **O quê**: 429 RESOURCE_EXHAUSTED do Antigravity em chat do ZCode mesmo com quota cheia = filtro de CONTEUDO no system prompt do ZCode, nao quota
- **Por que**: A mensagem do Google e enganosa (diz quota); a causa real e o paragrafo IMPORTANT: Assist with authorized security testing, CTF challenges hardcoded em AppData/Local/Programs/ZCode/resources/glm/zcode.cjs (NAO esta no AGENTS.md, esta no binario do app)
- **Onde**: [Fonte viva](<config.yaml%20-%3E%20oauth.providers.antigravity.sensitive-patterns-replace%3B%20bodies%20reais%20em%20auths/logs/error-v1-%2A.log%3B%20start%20.agents/scripts/start-proxy.ps1>)
- **Quando**: provider custom Antigravity falha no chat do ZCode mas curl minimo responde 200
- **Como**: (1) ligar observability.logs.request-log e logging-to-file; (2) ler o body real em auths/logs/error-v1-*.log (=== REQUEST BODY ===); (3) reproduzir com o body real via curl variando UM campo; (4) aplicar o pattern de remocao no proxy
- **Quanto**: ~5 min com o log; horas sem ele (pago: 4h nesta sessao)
- **E se??**: E se?? aparecer 400 model_not_found? → e a camada 2: oauth.model-alias sem fork:true substitui o ID original — adicionar fork:true
- **E se??**: E se?? o cooldown persistir apos um 429? → camada 3: routing.cooldown.disable-cooling: true (com save-cooldown-status:false o restart tambem zera)
- **E se??**: E se?? o usuario falar de seguranca/CTF na propria mensagem? → o filtro e por conteudo: mensagens do usuario tambem podem disparar 429 — diagnosticar pelo body em auths/logs, nao presumir quota

## 🔥 RECEIPTS-NAO-VERSIONADOS

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessao do repo que for commitar ou enviar
- **O quê**: .agents/receipts/ guarda corpo de requisicao, logs com e-mail e capturas de tela de contexto: nunca entra no git, porque o fork dex-agent/CLIProxyAPI e publico
- **Por que**: Em 2026-11-22 um git add -f .agents/ no atacado publicou o e-mail do dono em 8 arquivos e 23 corpos de requisicao com conversa e o AGENTS.md global; o push foi feito sem olhar o conteudo
- **Onde**: [Fonte viva](<.agents/receipts/%20%28local%29%20e%20.gitignore%20%28o%20upstream%20ja%20ignora%20.agents%29>)
- **Quando**: todo commit ou push deste repo, em especial depois de criar recibo de diagnostico
- **Como**: adicionar por caminho explicito, nunca -f no diretorio; o hook pre-push (tools/hooks/pre-push) roda sozinho o gate de valor secreto pelo shim .agents/scripts/push_gate.py, que chama a ferramenta da casa range_gate.py (skill dex-sanitizar-dados-pessoais); para a triagem de dado pessoal antes de um push arriscado: python -I -B -X utf8 .agents/scripts/push_gate.py . 6eb8554f..HEAD --triage; nunca citar o SHA de um commit do historico antigo
- **Quanto**: o hook e automatico; 1 comando de triagem por push arriscado
- **E se??**: E se?? precisar versionar um recibo? → copiar so a parte saneada para um doc em .agents/ e deixar o original local · E se?? o hook bloquear o push? → ler o rotulo, o tamanho e a contagem impressos (nunca o valor); remover o valor do commit ou trocar o segredo; nao empurrar com PUSH_GATE_SKIP=1 sem conferir a faixa a mao

## 🔥 OPENCODE-GO-CLIENTE-EXTERNO

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessao que for usar o plano OpenCode Go fora do cliente OpenCode (ZCode, proxy, curl)
- **O quê**: o endpoint e https://opencode.ai/inference/go/openai/v1 (o /go/ e obrigatorio) com o token OAuth do opencode.db e os headers x-opencode-session, x-opencode-project, x-opencode-directory e x-opencode-client; o ZCode aceita isso direto em api.headers, sem proxy
- **Por que**: sem o /go/ e sem x-opencode-session a resposta e 429 FreeUsageLimitError ou 400 MissingSessionID; os modelos -free do provider sem Go so funcionam dentro do cliente OpenCode
- **Onde**: [Fonte viva](<scripts%20register_opencode_go_zcode.py,%20register_oc_go_multi_protocol.py%20e%20refresh_opencode_go_token.py%20em%20.agents/scripts/>)
- **Quando**: cadastrar, renovar ou diagnosticar o acesso ao OpenCode Go
- **Como**: para modelo bloqueado com 400, ler a mensagem inteira: ela traz o link da configuracao do workspace (regiao Global ou permitir endpoints que treinam) e nao tem a ver com a localizacao da maquina
- **Quanto**: o token vale cerca de 30 dias
- **E se??**: E se?? um modelo do Go devolver 400 hosted outside Europe? → e a politica Regions do workspace no console: decidir la, e escolha de privacidade do dono

## 🔥 GRATIS-TODOS-RESSYNC

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessao que mantem o grupo de modelos gratuitos
- **O quê**: o provider Gratis (todos) do ZCode so tem os modelos que o proxy expoe com alias free-or-* (OpenRouter) e free-oc-* (OpenCode Go); ele nao se atualiza sozinho
- **Por que**: a lista de :free do OpenRouter muda: em 2026-11-23 cinco ja estavam aposentados (404 no longer available)
- **Onde**: [Fonte viva](<.agents/scripts/free_aggregator.py>)
- **Quando**: quando um alias free-* devolver 404, ou depois de cada sync dos free do OpenRouter
- **Como**: em ordem: free_aggregator.py setup-proxy (consulta o catalogo vivo), stop-proxy.ps1 e start-proxy.ps1 (o hot-reload nao remove modelo), free_aggregator.py register-zcode, free_aggregator.py test para o numero medido
- **Quanto**: a suite dos 14 levou cerca de 15 segundos
- **E se??**: E se?? a falha for 429 e nao 404? → 429 e lotacao do fornecedor (upstream_provider_shared_pool): o modelo e valido, tentar depois

## 🔥 PROXY-WMI-SEM-JANELA

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: sessao que precisar do CLIProxyAPI no ar
- **O quê**: o proxy sobe por start-proxy.ps1, que cria o processo via WMI com ShowWindow=0: fora da job do ZCode e sem janela de console
- **Por que**: por Start-Process ele morria no restart do ZCode (herda a job do host); por WMI com janela visivel morreu junto com o wrapper cmd minutos depois
- **Onde**: [Fonte viva](<.agents/scripts/start-proxy.ps1>)
- **Quando**: antes de usar os providers CLIProxyAPI, xAI (CLIProxyAPI) e Gratis (todos) do ZCode
- **Como**: powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1 responde JA_ATIVO (ja esta no ar) ou INICIADO com o pid do proxy; stop-proxy.ps1 responde PARADO ou JA_PARADO; reiniciar e stop seguido de start; a chave de acesso e lida do config.yaml
- **Quanto**: menos de 15 segundos
- **E se??**: E se?? depois de um restart do ZCode responder INICIADO em vez de JA_ATIVO? → o proxy morreu no restart: a hipotese seguinte e tarefa agendada do Windows, que exige decisao do dono

## 🔥 FORK-REDE-APAGAR-NAO-PURGA

<!-- dex.gatilho-vivo.v1 -->
- **Quem**: dono do fork e sessao do repo que for publicar ou reescrever historico
- **O quê**: Apagar um fork nao remove os objetos inalcancaveis: a rede de forks compartilha o armazem com o upstream e o commit antigo segue acessivel pelas duas namespaces (medido em 2026-11-23: API, pagina e raw responderam 200 sem login)
- **Por que**: Em 2026-11-23 o dono apagou o fork para remover o historico com dado pessoal e o commit continuou abrindo pelo namespace do upstream; o fork recriado voltou a servi-lo pela propria namespace. A afirmacao anterior de que apagar seria a remocao completa estava errada.
- **Onde**: [Fonte viva](<recibo%20local%20.agents/receipts/W18-old-history-reach.txt,%20texto%20do%20pedido%20em%20.agents/receipts/W18-support-ticket.txt%20e%20pendencia%20fork-dados-pessoais%20em%20.agents/PENDENTES.md>)
- **Quando**: antes de prometer que um historico exposto sumiu, antes de apagar ou recriar um fork e antes de citar um SHA antigo em arquivo versionado
- **Como**: medir antes de afirmar (API anonima, pagina e raw, com controle positivo); nunca citar o SHA do commit exposto em arquivo publicado; reescrever so os commits da casa com git filter-repo --refs <base>..main, que preserva a ancestridade; pedir a remocao ao suporte do GitHub
- **Quanto**: 4 pedidos HTTP para a medida; o pedido ao suporte e do dono
- **E se??**: o dono quiser o endereco do proprio fork morto antes de o suporte responder? → um repositorio avulso (fora da rede de forks) devolve 404 na namespace do fork, mas a namespace do upstream segue servindo ate o suporte remover
- **E se??**: o commit exposto ja tiver sido clonado por alguem? → o dado exposto e e-mail e texto de conversa, sem credencial; depois do pedido ao suporte, avaliar com o dono se algo precisa ser trocado
