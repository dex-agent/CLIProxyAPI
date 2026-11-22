# CODE-REVIEW-GRAPH-INDEX — CLIProxyAPI

**LOCALIZADOR**: `CRG-LOCAL-STRUCTURAL-GRAPH` · tags: `#code-review-graph` `#crg` `#grafo-estrutural`

| Campo | Valor |
|---|---|
| repo | `C:\CodexProjetos\CLIProxyAPI` |
| branch / SHA | main / `6eb8554f0ede` |
| data dir | `.agents/CODE-REVIEW-GRAPH/` (banco `graph.db`) |
| build | 2026-11-22 — full build + update pós-ignore; parser **tree-sitter-go nativo** (sem feeder) |
| escala | 2463 arquivos · 35497 nós (17.833 Function, 11.042 Test, 3.112 Class) · 646569 arestas · FTS 35497 rows |
| linguagens | bash, c, go, json, powershell, python, rust, yaml |
| ignore | `.code-review-graphignore`: .agents/, .code-review-graph/, __backups/, LIXEIRA/, test-output* |
| grafo rico | `graphify-out/graph.json` (36327 nós / 485008 arestas / 1276 comunidades) — `graphify update .` |
| gate | `grafo_gate.py --data-dir .agents/CODE-REVIEW-GRAPH --min-functions 16000 --max-functions 19000 --max-span 1500` → **5/6 ✅, exit 1 por 1 achado real** (span 1585L: ConvertGeminiResponseToOpenAIResponses — pódio W8, não é lixo de infra) |
| refresh | `code-review-graph update --data-dir .agents/CODE-REVIEW-GRAPH` (usa `.code-review-graphignore`) |
| limites | sem embeddings (não habilitado); flows/communities sumários sem LLM backend |

Regra: consultar ANTES de review estrutural; grafo é pista — achado só vira fato na fonte viva (arquivo/teste/doc).
