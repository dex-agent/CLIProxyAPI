---
implementation_version: v2
layer: L2
slug: achado-notavel-2026-11-24-provider-opencode-free-hi-2dcc4b2fa888
tags:
  - "#cliproxyapi/opencode"
  - "#cliproxyapi/modelos-free"
  - "#zcode/provider-config"
---

# Achado notável 2026-11-24: provider opencode free — história completa, receita de recuperação e o que ainda falta

HISTORIA PROVADA (2026-11-24):
1. O provider opencode (4 modelos free: glm-5.3-flash-free, flint-40b-free, mimo-v2.6-flash-free, deepseek-v4.1-flash-free) existia no ZCode, no schema e no lugar corretos, ate 22/11 18:44.
2. Sumiu as 20:05 de 22/11, no bloco free da propria sessao, SEM registro — o dono so descobriu porque pediu de novo. Apareceu de novo no seletor em 24/11 apos a restauracao (confirmado pelo dono: agora sim apareceu).
3. A chave do provider estava expirada (401 api_key_expired). A chave valida estava na variavel de ambiente OPENCODE_API_KEY. Trocada no provider (backups -20261124-restore-opencode-free e -20261124-opencode-free-key).
4. Chamada direta por API com chave valida: 429 FreeUsageLimitError, 3 vezes, 3 modelos, 70 s de intervalo. Pelo cliente OpenCode: opencode run --model opencode/deepseek-v4.1-flash-free responde pong. Caminho que funciona: cliente.
5. Restam: o dono escolher o modelo no seletor numa conversa nova (a escolha so grava no inicio da conversa) para capturar o providerId do provider OpenCode CLI; depois criar os agents (skill zcode-provider-manager-agents) e provar por subagente.

ONDE EU TIVE DIFICULDADE (reforcos):
D1. Reaprendi do zero o que a propria sessao ja tinha feito: nao li memorias/recibos antes de agir. Reforco: memoria perguntas-base-antes-de-agir (responder as 2 perguntas base por escrito).
D2. Gravei memoria ERRADA (7 modelos nao alcancaveis) sem prova executada. Reforco: memoria conclusao-em-memoria-exige-prova-executada; a errada esta supersedida por correcao-modelos-free-do-opencode-no-zcode.
D3. Procurei o nome do provider CLI do ZCode no escuro (rollout, app.asar, corpus do mentor) quando a resposta estava nos backups do provider_config.json e no banco de sessoes. Reforco: RECEITA abaixo.
D4. meta-zcode.mjs falhou sem ZCODE_CLI_PATH; list-zcode-models.mjs --help executa em vez de ajudar. Reforco: napkin W27.
D5. Confundi duas fontes: catalogo do agent (meta-zcode, 206 modelos) nao e a lista do seletor (modelProviderService do app). Doc do ZCode: model-provider-opencode-config.md.
D6. Sem os cabecalhos x-opencode-* e User-Agent opencode/..., a API devolve 403 Cloudflare 1010.
D7. Erro de sintaxe Python (next mal fechado) e closeout com updater da skill errada (garimpeiro no lugar do chato -> skill_mismatch). Reforco: cada skill tem updater proprio.

RECEITA DE RECUPERACAO (nao acessar session id de novo; so se o nome driftar):
- Um provider que sumiu: diff dos backups ~/.zcode/v2/provider_config.json.backup-* (ordenar por mtime; o ultimo com e o primeiro sem o providerId mostram a janela exata).
- Par provider/modelo que o ZCode usou: SELECT session_id, data FROM session_entry WHERE type='runtime/model_selection' ORDER BY time_created DESC (banco ~/.zcode/cli/db/db.sqlite, modo ro; o par vem aninhado em data.modelSelection.providerId/modelId). O indice do Desktop ~/.zcode/v2/tasks-index.sqlite, tabela tasks, colunas provider e model, guarda o par por tarefa.
- O arquivo rollout/model-io-<sessao>.jsonl so tem o pos-compactacao; o banco tem o historico inteiro.
- Modelos que o ZCode expõe aos agents: meta-zcode.mjs (pacote zcode-orquestrador-multimodelo) com ZCODE_CLI_PATH=%LOCALAPPDATA%/Programs/ZCode/resources/glm/zcode.cjs.

RESPOSTA PARA A PROXIMA VEZ (semana que vem): NAO precisa acessar o session id nem o banco: tudo que foi aprendido esta nesta memoria e no item 14 do PENDENTES. So volta a ser preciso (a) se o provider sumir de novo (receita acima resolve em 2 comandos) ou (b) na hora de criar agents ligados ao provider CLI do seletor, quando falta capturar 1 clique do dono.

EVIDENCIA: .agents/PENDENTES.md item 14; backups provider_config.json.backup-20261122-xai (com) e -free (sem); recibos W25/W27/W30; banco do ZCode session_entry e tasks.model.

#cliproxyapi/opencode #cliproxyapi/modelos-free #zcode/provider-config

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^achado-notavel-2026-11-24-provider-opencode-free-hi-2dcc4b2fa888-content
