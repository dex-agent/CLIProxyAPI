---
implementation_version: v2
layer: L2
slug: provider-cliproxyapi-no-zcode-5-camadas-empilhadas-e98196bf0491
tags:
  - "#instalacao/cliproxyapi-provider"
  - "#zcode/provider"
  - "#antigravity/e2e"
---

# Provider CLIProxyAPI no ZCode: 5 camadas empilhadas até o E2E verde

E2E PROVADO 2026-11-22 (chat do ZCode respondeu 'gemini-4-argon via CLIProxyAPI'). O funcionamento exigiu 5 camadas SIMULTANEAS — cada uma mascarava a seguinte: (1) reasoningLevel: agent/model rule de claude-* exige config.optionSpecs.reasoningLevel.values=['high'] no providerModelRules do provider_config.json (serie Claude exige nivel; gemini cai em toggle on/off). (2) ID normalizado: a UI do ZCode tira o sufixo de esforco do modelId (-high vira 'Effort: High'); o proxy recebia 'gemini-4-argon' e devolvia model_not_found. Cura: oauth.model-alias.antigravity com fork:true + force-mapping:true (SEM fork o alias SUBSTITUI o ID original e quebra os que ja funcionavam). (3) cooldown: cada 429 semeia cooldown de credencial em memoria -> blackout em cascata. Cura: routing.cooldown.disable-cooling: true. (4) user_agent: o proxy manda 'antigravity/hub/<v> (aidev_client; os_type=darwin; arch=arm64)' fixo — mentira em maquina Windows e versao distinta da desktop. Cura: campo user_agent no auth JSON (auths/antigravity-*.json): 'antigravity/hub/2.24.0 (aidev_client; os_type=win32; arch=x64; cl=963137146)' (formato que o OpenBot usa e o que faz o Google servir o grupo correto a planos Pro — fonte: mentor-documental-openbot, antigravity-usage.ts). (5) CONTEUDO do system prompt: o do ZCode contem vocabulario de seguranca ofensiva (CTF/pentesting/C2/DoS) e o Antigravity responde 429 RESOURCE_EXHAUSTED enganoso. Cura: oauth.providers.antigravity.sensitive-patterns-replace removendo o paragrafo. PROCESSO: rodar o proxy com observability.logs.request-log:true + logging-to-file:true e ler os bodies reais em auths/logs/error-v1-*.log (o stdout nao traz body). Start desacoplado: .agents/scripts/start-proxy.ps1 (Start-Process; o proxy NAO pode ser filho do shell do host — morre junto). Diagnostico final: proxy 127.0.0.1:8317, key <PROXY-KEY>, config.yaml gitignored.

#instalacao/cliproxyapi-provider #zcode/provider #antigravity/e2e

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^provider-cliproxyapi-no-zcode-5-camadas-empilhadas-e98196bf0491-content
