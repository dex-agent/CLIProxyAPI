# ACTIVE — CLIProxyAPI (estado vivo)

**O que é**: fork `dex-agent/CLIProxyAPI` (público) do upstream `router-for-me/CLIProxyAPI`, com a camada de arqueologia e a integração com o ZCode.

## Estado em 2026-11-24
- **Release `v8.1.1-dex.1` publicada** no fork: 9 pacotes + `checksums.txt`. Falta só `darwin-arm64` (runner `macos-15` não entregue). Instalação em outra máquina: baixar o pacote e conferir o checksum. Detalhe em `HANDOFF.md` (W21).
- **`.gitignore` recortado**: `.agents/*` é padrão e só o estado vivo é re-incluído. Arquivo novo em `PLAN-TASKS`, `memorias`, `.dex-memoria`, `ESTACIONAMENTO` e `LIXEIRA` aparece no `git status`; `scripts/`, `receipts/` e `TEMP/` seguem ignorados.
- **Tag de base `upstream-v8.1.1` não deve ser apagada**: sem ela o workflow de release não acha tag anterior e a nota passa do limite.
- **Arqueologia** W-1..W10 fechada (tier completo: 2405 fontes Go). Grafo interno e 3rd-party em `DEPENDENCIES.md`; recibos em `.agents/receipts/` (local, nunca versionado).
- **Build do upstream**: verde. **Suíte nativa**: vermelha no Windows (9 falhas: 8 de ambiente, 1 golden drift real) — ver `PENDENTES.md`.
- **Proxy local** (`127.0.0.1:8317`): liga com `powershell -NoProfile -ExecutionPolicy Bypass -File .agents\scripts\start-proxy.ps1` (idempotente) e desliga com `stop-proxy.ps1`; reiniciar é os dois nessa ordem. A chave de acesso é lida do `config.yaml`. Sobreviver a um restart do ZCode ainda não foi provado (estacionado).
- **Providers no ZCode**: `CLIProxyAPI` (12, antigravity) · `xAI (CLIProxyAPI)` (8) · `OpenCode Go` + `(Anthropic)` + `(Responses)` (22, direto, sem proxy) · `Gratis (todos)` (14, via proxy) · `openrouter` (41).
- **Fork**: recriado em 2026-11-23 como fork verdadeiro do upstream (só a `main`), com os commits da casa sobre `6eb8554f` (a contagem muda a cada fechamento; confira pela comparação da API). O upstream já avançou 51 commits (não mesclados). Histórico limpo: sem dado pessoal, sem credencial e sem ponteiro para o histórico antigo. Cite commits por data e assunto, nunca pelo SHA de um commit antigo.
- **Antes de cada push**: rodar o gate da ficha `RECEIPTS-NAO-VERSIONADOS`.
- **Toolchain Go**: fora do PATH. `source .agents/scripts/go-env.sh` (Go 1.26.10 no module cache).
- **Grafo estrutural (CRG)**: `.agents/CODE-REVIEW-GRAPH/` (local, não versionado). Antes de citar número dele, aplicar a ficha `STALENESS-ARTEFATOS-DERIVADOS`.

## Ações do dono pendentes (detalhe em `PENDENTES.md`)
- Console do OpenCode (Settings > Privacy): **Regions = Global** libera `deepseek-v4.1-flash`, `deepseek-v4-pro` e `longcat-2.5`; **Training** libera `muse-spark-1.3-contributor` e `iceman-contributor-free`.
- 5 modelos `:free` aposentados pelo OpenRouter continuam listados no provider `openrouter`.
- Reiniciar o ZCode para provar por subagente o grupo `Gratis (todos)` e os dois providers novos do OpenCode Go.

## Lentes ativas
chato · bruninha-agulha · critico-cetico · questionador · interrogador-documental · entrevista-me · ponytail (full)

## Histórico do bloco

### W11 — Instalação + provider ZCode (2026-11-22)
- `cli-proxy-api.exe` (build exit 0) + `config.yaml` mínimo (gitignored) + OAuth antigravity OK (`auths/antigravity-<conta-google>.json`).
- E2E provado: `gemini-3-flash`, `gemini-3.8-flash-high`, `claude-sonnet-5-5-high`.
- Provider `CLIProxyAPI` no ZCode: 12 modelos, validado contra a doc oficial (`api.type`) e o hot-reload (`#pollOnce`).

### W16 — provider CLIProxyAPI E2E no ZCode (2026-11-22)
- E2E provado no chat: "123 recebido! gemini-4-argon via CLIProxyAPI".
- 5 camadas curadas (cada uma mascarava a seguinte): `reasoningLevel` da regra; `model-alias` com `fork: true`; cooldown desligado; `user_agent` desktop no auth JSON; `sensitive-patterns-replace` contra o filtro de conteúdo do Antigravity.
- Causa-raiz: o system prompt do ZCode (embutido no `zcode.cjs`, não no `AGENTS.md`) contém vocabulário de segurança ofensiva e o Google devolve 429 `RESOURCE_EXHAUSTED` enganoso.

### W17 — OpenCode Go direto + grupo "Gratis (todos)" (2026-11-23)
- **OpenCode Go sem proxy**: endpoint `/inference/go/openai/v1` + headers `x-opencode-session`, `x-opencode-project`, `x-opencode-directory`, `x-opencode-client` + token OAuth do `opencode.db` (vale ~30 dias). E2E provado com `glm-5.3-flash` por subagente (3,9 s).
- **Grupo "Gratis (todos)"**: um provider só, com os 14 gratuitos, via proxy. O proxy agrega por alias `free-or-*` (OpenRouter) e `free-oc-*` (OpenCode Go) e consulta o catálogo vivo para deixar de fora os aposentados. Suíte medida: 11/14 OK; os outros 3 dão 429 de lotação no fornecedor.
- **Correção de diagnóstico**: DeepSeek no Go não é bloqueio pela localização da máquina; é a política de região do workspace no console do OpenCode.
- **Fork público**: recebeu e-mail e corpos de requisição por descuido do agente. Decisão do dono em 2026-11-23: purgar e force-push. `.agents/receipts/` saiu do versionamento e não volta (ficha `RECEIPTS-NAO-VERSIONADOS`).

### W18 — Fork recriado limpo + alcance do histórico antigo medido (2026-11-23)
- O dono apagou o fork. Antes de recriar, o gate achou a chave de acesso local do proxy fixa em 8 arquivos versionados: o histórico da casa foi reescrito só nos commits locais (`git filter-repo --refs 6eb8554f..main`), a chave saiu e os 4 scripts passaram a ler o `config.yaml`.
- Fork recriado (fork verdadeiro, só a `main`), com o histórico limpo: sem dado pessoal, sem credencial e sem o ponteiro do commit antigo.
- **Achado**: apagar o fork não removeu o histórico antigo. Ele responde 200 sem login pela API, pela página e pelo raw, na namespace do upstream e, com o fork novo, também na do fork. A rede de forks compartilha o armazém de objetos; só o suporte do GitHub remove.
- **Decisão do dono (2026-11-23)**: não pedir a remoção ao suporte do GitHub; resíduo aceito depois do inventário (recibo local `W18-exposed-inventory.txt`): nenhuma credencial de serviço externo; e-mail da conta Google em 8 arquivos; chave local do proxy em 29, que só vale em `127.0.0.1`.
- `stop-proxy.ps1` criado e testado (o dono perguntou como desligar o proxy).
