# -*- coding: utf-8 -*-
# Memória tema zcode: estrutura real do provider_config.json v2 (GO dono 2026-11-22)
import json, pathlib

payload = {
 "scope": "theme",
 "theme": "zcode",
 "title": "Estrutura real do provider_config.json v2: providers moram em providerRules, nao no array providers",
 "trigger": "ler, editar ou cadastrar provider/modelos no ZCode; diagnostico de provider sumido; provider_config.json aparentando vazio; sync openrouter/nvidia; configurar CLIProxyAPI ou proxy local como provider do ZCode",
 "body": (
  "O arquivo %USERPROFILE%/.zcode/v2/provider_config.json (schemaVersion 1) tem na raiz apenas "
  "{config, schemaVersion}; o array providers existe VAZIO ou ausente e NAO e a morada dos "
  "providers — ler providers e achar vazio e concluir que nao ha nada e LEITURA CEGA (paga ao "
  "vivo 2026-11-22: 3 leituras erradas + 6 backups descartados como vazios que nao estavam). "
  "ESTRUTURA REAL (fonte viva 2026-11-22, 16 providers): config.providerOrder (lista de strings); "
  "config.providerConfigRules.providerRules[] com {providerId, providerName, config:{access "
  "(SEGREDO, nunca ecoar), api, group, modelOrder, personalModelIds}}; "
  "config.modelConfigRules.providerModelRules[] com propriedades por par provider/model "
  "(contextWindow, supportsToolCall, optionSpecs; todo :free da casa tem regra de contextWindow "
  "— 142 regras vivas); config.defaultModelSelection. "
  "PROTOCOLO DE ESCRITA da casa (sessao sess_132e1d87-d9c6-4816-a07f-305656fe77da, 2026-11-21, "
  "skills zcode-provider-manager-model + zcode-provider-manager-agents): hash anterior, backup "
  "privado NO MESMO diretorio, menor delta (modelOrder += IDs novos + regra providerModelRules "
  "por modelo novo; nunca remover ausente por silencio), revalidar JSON/IDs/providers intactos. "
  "Agents espelho: %USERPROFILE%/.zcode/agents/*.md (molde agent-gemma4-31b-free.md); modelo de "
  "midia (output_modalities text+audio, ex lyria) fica no provider e nunca vira agent de texto. "
  "Credenciais moram em credentials.json (superficie separada). Comando seguro de leitura na "
  "nota citavel zcode-provider-config-estrutura-v2 do acervo notas-citaveis."
 ),
 "tags": ["#zcode/provider-config", "#zcode/sync-modelos", "#config/estrutura-v2"],
}
pathlib.Path(".agents/receipts/mem/m-tema-zcode.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
print("payload tema zcode ok")
