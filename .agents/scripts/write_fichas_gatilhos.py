# -*- coding: utf-8 -*-
# Gera records dex.gatilho-vivo.v1 para os 7 gatilhos legados do hub (migração 2026-11-22)
import json, pathlib

out = pathlib.Path(".agents/receipts/mem")
S = "dex.gatilho-vivo.v1"

records = [
 {"gatilho": "GO-TOOLCHAIN-FORA-PATH", "quem": "sessão do repo",
  "o_que": "Binário go NÃO está no PATH da máquina; toolchain 1.26.10 (exata do go.mod) vive no module cache",
  "por_que": "build/teste falha com go: command not found e alguém re-instala Go desnecessariamente",
  "onde": ".agents/scripts/go-env.sh (repo) + C:/Users/<USER>/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.10.windows-amd64/bin/go.exe",
  "quando": "qualquer build/teste Go no CLIProxyAPI",
  "como": "source .agents/scripts/go-env.sh e usar $GO com CGO_ENABLED=0. Re-localizar via AppData/Roaming/go/telemetry se o cache mudar.",
  "quanto": "0s (source de script)",
  "e_se": [{"pergunta": "E se?? o module cache for limpo (go clean -modcache)?", "resposta": "toolchain some: baixar Go 1.26.x oficial para C:/tools e atualizar go-env.sh"}]},
 {"gatilho": "TESTE-VERMELHO-WINDOWS", "quem": "sessão do repo",
  "o_que": "9 falhas conhecidas de go test ./... (HEAD 6eb8554f, 2026-11-22): 8 ambiente-Windows (file-lock TempDir em home/kvstore/pluginhost; TUI/TTY timeout 30s; links POSIX em internal/store) + 1 golden drift REAL (TestToolSearchDisabledMatchesDevGolden)",
  "por_que": "re-abrir investigação já classificada ou tratar falha de ambiente como regressão de código",
  "onde": ".agents/receipts/W6-build-test.json + .agents/receipts/W6-pluginhost-retest.txt",
  "quando": "rodar go test ./... e ver 9 falhas / 6 pacotes",
  "como": "Ler o receipt ANTES de agir; build VERDE (exit 0); pendências com owner em .agents/PENDENTES.md.",
  "quanto": "leitura de 1 receipt (segundos)",
  "e_se": [{"pergunta": "E se?? uma das 9 falhas mudar de classe após update?", "resposta": "re-classificar pelo receipt novo: rótulo vale enquanto a fonte viva confere"}]},
 {"gatilho": "CI-SOMENTE-BUILD", "quem": "sessão do repo",
  "o_que": "pr-test-build.yml roda apenas go build + rm — NÃO roda go test",
  "por_que": "confiar que CI verde prova testes quando não prova (regressão de golden passou invisível no upstream)",
  "onde": ".github/workflows/pr-test-build.yml + .agents/receipts/W1-inventario-go.txt",
  "quando": "confiar em CI verde do CLIProxyAPI",
  "como": "CI verde = prova de build somente; teste só local (go test ./...).",
  "quanto": "0 (fato de contrato)",
  "e_se": [{"pergunta": "E se?? o upstream adicionar job de teste?", "resposta": "re-medir o workflow e atualizar esta ficha na mesma sessão que descobrir"}]},
 {"gatilho": "ENC-CRLF-LOJA-LF", "quem": "sessão do repo",
  "o_que": "Working 100% CRLF, loja i/lf limpa, core.autocrlf=true (system), SEM .gitattributes; 125 UTF-8 válidos (mandarim em internal/tui/i18n.go)",
  "por_que": "commitar com autocrlf=false colapsa a loja para CRLF (contaminação de 2.5k arquivos)",
  "onde": ".agents/receipts/W2-encoding-census.json",
  "quando": "editar fonte ou investigar EOL no CLIProxyAPI",
  "como": "Nunca commitar com autocrlf=false nesta máquina; pin *.go text eol=lf é proposta pendente no upstream.",
  "quanto": "0 (fato de contrato)",
  "e_se": [{"pergunta": "E se?? um .gitattributes aparecer num pull futuro?", "resposta": "re-medir o census W2 e atualizar a ficha"}]},
 {"gatilho": "CRG-GRAFO-LOCAL", "quem": "sessão do repo",
  "o_que": "Grafo CRG 2.4.0+dex.3 em .agents/CODE-REVIEW-GRAPH (2463 arquivos, 35497 nós, 646569 arestas, tree-sitter-go NATIVO, built 6eb8554f); doctor: já segura todo arquivo mudado desde então",
  "por_que": "review estrutural sem grafo re-analisa do zero, ou cita número de mapa velho (falso verde)",
  "onde": ".agents/CODE-REVIEW-GRAPH/ + .agents/CODE-REVIEW-GRAPH-INDEX.md",
  "quando": "review estrutural ou análise de impacto no CLIProxyAPI",
  "como": "Consultar ANTES de review estrutural; refresh: code-review-graph update --data-dir .agents/CODE-REVIEW-GRAPH; staleness pela ficha STALENESS-ARTEFATOS-DERIVADOS.",
  "quanto": "update incremental ~minuto",
  "e_se": [{"pergunta": "E se?? o doctor acusar cópia divergente na máquina?", "resposta": "hook e shell resolvem pelo PATH (dex.3, fork da casa); cópia uv dex.1 é ressalva de máquina, não do repo"}]},
 {"gatilho": "HOTSPOT-GEMINI-RESPONSES", "quem": "sessão do repo",
  "o_que": "ConvertGeminiResponseToOpenAIResponses CC348/1585L (gemini_openai-responses_response.go:381-1966) = duplo coroa com gate de span; depois streamCodexDuplex CC325, MarkResult CC314; god file conductor_cooldown.go 4217L/150fn",
  "por_que": "escolher alvo de refactor sem os números ou re-medir o pódio inteiro a cada decisão",
  "onde": ".agents/receipts/W8-gocyclo.txt (pódio completo, gocyclo 28660 rotinas, cobertura 100%)",
  "quando": "refatorar translator gemini ou escolher alvo de refactor",
  "como": "Usar o pódio medido; staleness da métrica segue STALENESS-ARTEFATOS-DERIVADOS.",
  "quanto": "0 (pódio já medido)",
  "e_se": [{"pergunta": "E se?? a função-monstro for dividida no upstream?", "resposta": "re-medir gocyclo e atualizar o pódio na mesma sessão que tocar o arquivo"}]},
 {"gatilho": "PIPE-EXIT-FALSO", "quem": "sessão do repo",
  "o_que": "3 falsos na mesma sessão (iconv 125/125, find de fóssil, diff de branch) todos por pipe engolindo erro/código de exit",
  "por_que": "declarar resultado de pipeline quebrado como fato (falso verde ou falso vermelho)",
  "onde": "disciplina de execução + .agents/GATILHOS-VIVOS.md (esta ficha)",
  "quando": "medir qualquer exit/gate/contagem nesta janela",
  "como": "Exit SEMPRE medido sem pipe: comando > arquivo 2>&1; echo exit=$?. Contagem idem (wc -l no arquivo).",
  "quanto": "0 (disciplina de execução)",
  "e_se": [{"pergunta": "E se?? o comando só existir em pipeline?", "resposta": "redirecionar a SAÍDA para arquivo e medir exit/contagem do arquivo, nunca confiar no código do pipe"}]},
]

for i, r in enumerate(records):
    r["schema"] = S
    (out / f"ficha-legacy-{i}.json").write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
print("records:", len(records))
