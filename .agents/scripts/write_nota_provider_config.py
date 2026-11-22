# -*- coding: utf-8 -*-
# Payload da nota citável zcode-provider-config-estrutura-v2 (canal dex-notas-citaveis)
import json, pathlib

corpo = "\n".join([
"# [notas-citaveis] zcode-provider-config-estrutura-v2",
"",
"Localizador: ZCODE-PROVIDER-CONFIG-ESTRUTURA-V2 | Data: 2026-11-22",
"",
"## O que e",
"O arquivo `%USERPROFILE%\\.zcode\\v2\\provider_config.json` (schemaVersion 1) tem na raiz apenas",
"`{config, schemaVersion}`. A chave `providers[]` existe vazia (ou nem existe) no arquivo moderno —",
"ela NAO e a morada dos providers. Um agente que le `providers[]`, ve `[]` e conclui que nao ha",
"providers cadastrados comete leitura cega (paga ao vivo: 3 leituras cegas na mesma janela,",
"incluindo 6 backups erroneamente descartados como vazios).",
"",
"## A regra",
"Estrutura REAL (confirmada na fonte viva 2026-11-22, 16 providers ativos):",
"- `config.providerOrder` — lista de strings (ordem dos providers)",
"- `config.providerConfigRules.providerRules[]` — 1 entrada por provider:",
"  `{providerId, providerName, config: {access (SEGREDO — nunca ecoar), api, group,",
"  modelOrder[], personalModelIds[]}}`",
"- `config.modelConfigRules.providerModelRules[]` — propriedades por par provider/model",
"  (contextWindow, supportsToolCall, optionSpecs...); no acervo da casa TODO modelo `:free`",
"  tem regra de contextWindow (142 regras vivas)",
"- `config.defaultModelSelection` — selecao padrao",
"",
"Protocolo de escrita da casa (sessao `sess_132e1d87-d9c6-4816-a07f-305656fe77da`, 2026-11-21,",
"skills `zcode-provider-manager-model` + `zcode-provider-manager-agents`): hash anterior ->",
"backup privado NO MESMO diretorio (`provider_config.json.backup-<data>`) -> menor delta",
"(modelOrder += IDs faltantes; regra providerModelRules por modelo novo; NUNCA remover ausente",
"por silencio) -> revalidacao (JSON valido, IDs unicos, 16 providers intactos).",
"Agents espelho moram em `%USERPROFILE%\\.zcode\\agents\\*.md` (molde canonico",
"`agent-gemma4-31b-free.md`); modelo de midia (output_modalities text+audio, ex lyria) fica no",
"provider e NUNCA vira agent de texto.",
"",
"Comando de leitura segura (sem vazar access):",
"`python -Ic \"import json; d=json.load(open(r'C:\\\\Users\\\\<USER>\\\\.zcode\\\\v2\\\\provider_config.json',encoding='utf-8')); rules=d['config']['providerConfigRules']['providerRules']; print([(r.get('providerName'), len(r['config'].get('personalModelIds',[]))) for r in rules])\"`",
"",
"## Prova de nascimento",
"- Fonte viva conferida 2026-11-22: 16 providerRules (openrouter 38/42, nvidia, nvidia-2, Kimi,",
"  DeepSeek, GROK, dex, cloudflare, agnes...) + 142 providerModelRules — saida do comando acima",
"  nesta janela (repo CLIProxyAPI).",
"- Sessao que pagou o sync completo: `sess_132e1d87-d9c6-4816-a07f-305656fe77da` (workspace",
"  ~/.agents/skills, 2026-11-21 21:40-22:32): openrouter 38->42 (+4 `:free` com tools),",
"  4 agents OR criados + 8 atualizados, NIM 15->18 nas 2 contas, +11 agents NIM, limpeza da",
"  regra orfa diffusiongemma (EOL 410 documentado).",
"- Backups da escrita: `provider_config.json.backup-20261121-214108`..`221200` (4 no mesmo diretorio).",
"",
"## Quando usar",
"Cadastrar/lapidar provider ou modelos no ZCode; ler inventario de providers da maquina;",
"diagnostico de 'provider sumiu'; sync free OpenRouter/NIM; qualquer janela fria tocando",
"provider_config.json.",
"",
"## Quando NAO usar",
"Nao e rota para credenciais (credentials.json e outra superficie, keys `oauth:*`); nao cobre o",
"legado `config.json` do cli/ (nao escrever em ambos); nota cita o CAMINHO, nunca o conteudo de access.",
"",
"## Prova reexecutavel",
"Comando: `python -Ic \"import json; d=json.load(open(r'C:\\\\Users\\\\<USER>\\\\.zcode\\\\v2\\\\provider_config.json',encoding='utf-8')); print(len(d['config']['providerConfigRules']['providerRules']))\"`",
"(saida 2026-11-22: 16)",
"",
])

payload = {
 "slug": "zcode-provider-config-estrutura-v2",
 "gatilhos": [
  "ZCODE-PROVIDER-CONFIG-ESTRUTURA-V2",
  "provider_config.json providers vazio",
  "cadastrar provider no zcode",
 ],
 "resumo": ("Providers e modelos do ZCode v2 NAO moram em providers[] do provider_config.json — "
            "moram em config.providerConfigRules.providerRules (selector providerId/providerName, "
            "config.personalModelIds + config.modelOrder) com propriedades em "
            "config.modelConfigRules.providerModelRules; ler providers[] e achar [] e concluir "
            "config vazio = leitura cega paga ao vivo em 2026-11-22."),
 "corpo": corpo,
 "hub_porque": ("Janela fria le providers[] vazio e conclui que nao ha providers — re-cadastro "
                "duplicado ou desistencia falsa; ja custou 3 leituras cegas pagas numa unica sessao."),
 "hub_como": ("Antes de ler/cadastrar provider no ZCode: ler "
              "config.providerConfigRules.providerRules (comando seguro na nota); escrita pelo "
              "protocolo backup-no-mesmo-diretorio + menor delta + revalidacao (skills "
              "zcode-provider-manager-model/-agents)."),
}
pathlib.Path(".agents/receipts/nota-provider-config.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
print("payload ok | gatilhos:", len(payload["gatilhos"]), "| corpo linhas:", len(corpo.splitlines()))
