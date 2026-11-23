---
implementation_version: v2
layer: L2
slug: grupo-gratis-todos-os-14-modelos-gratuitos-num-prov-d1682ea28e59
tags:
  - "#cliproxyapi/gratis-todos"
  - "#openrouter/free"
  - "#zcode/provider-config"
---

# Grupo Gratis (todos): os 14 modelos gratuitos num provider so do ZCode, agregados pelo proxy

O ZCode agrupa modelos por provider e um provider tem uma base URL e uma chave só, então os gratuitos de origens diferentes só ficam juntos por meio do proxy. O provider Gratis (todos) aponta para o proxy local e o proxy agrega dois upstreams em api-keys.openai-compatibility: openrouter-free (os modelos com sufixo free do provider openrouter do ZCode, mais o roteador openrouter/free) com alias free-or-nome, e opencode-go (hy4-flash-free e beam-free) com alias free-oc-nome. O script free_aggregator.py tem as rotas setup-proxy, register-zcode e test; o setup-proxy consulta o catalogo público do OpenRouter e deixa fora os aposentados, porque a lista do ZCode guarda modelos que o OpenRouter já retirou (cinco em 2026-11-23: cohere/north-mini-code, liquid/lfm-2.5-2.6b, poolside/laguna-xs-2.1, thinkingmachines/inkling-small e xingchen-agi/xing4.0-29b-a4b, todos com 404 no longer available). Suíte medida em 2026-11-23: 11 de 14 responderam; gemma-4-26b-a4b-it, gemma-4-31b-it e particle-1 deram 429 com provider_error_code 429 e limit_source upstream_provider_shared_pool, que é lotação do fornecedor e não cota da conta. O hot-reload do proxy adiciona modelo mas não remove, então depois de mudar a lista é preciso reiniciar pelo start-proxy.ps1. Ressincronizar na ordem: setup-proxy, reiniciar o proxy, register-zcode e test. O alias não pode terminar em sufixo de esforço do ZCode (high, low, medium, max, xhigh), porque a interface do ZCode tira esse sufixo do nome e o proxy passa a não conhecer o modelo.

#cliproxyapi/gratis-todos #openrouter/free #zcode/provider-config

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^grupo-gratis-todos-os-14-modelos-gratuitos-num-prov-d1682ea28e59-content
