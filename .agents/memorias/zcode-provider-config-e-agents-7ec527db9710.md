---
implementation_version: v2
layer: L2
slug: zcode-provider-config-e-agents-7ec527db9710
tags:
  - "#zcode/provider-config"
  - "#agents/criacao"
---

# ZCode provider config e agents

provider_config.json v2 do ZCode: providers moram em config.providerConfigRules.providerRules (NAO no array providers, que existe vazio) com {providerId, providerName, config:{access, api, group, modelOrder, personalModelIds}}; propriedades por modelo em config.modelConfigRules.providerModelRules. Agent de claude-* exige optionSpecs.reasoningLevel.values na regra do modelo (serie Claude exige nivel; gemini cai em toggle on/off). Frontmatter de agent usa model: "<providerId>/<modelId>" e thoughtLevel nao se copia entre modelos. A UI normaliza o ID tirando o sufixo de esforco (-high vira Effort), entao o proxy precisa de model-alias com fork:true para aceitar os dois nomes. Molde canonico de agent: agent-gemma4-31b-free.md em ~/.zcode/agents.

#zcode/provider-config #agents/criacao

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^zcode-provider-config-e-agents-7ec527db9710-content
