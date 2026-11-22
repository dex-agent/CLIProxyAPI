---
implementation_version: v2
layer: L2
slug: hotspots-de-toxicidade-do-cliproxyapi-podio-w8-106be41e7603
tags:
  - "#arqueologia/hotspot"
  - "#metricas/go"
---

# Hotspots de toxicidade do CLIProxyAPI (podio W8)

Podio CC (gocyclo, 28660 rotinas, cobertura 100%): 1) ConvertGeminiResponseToOpenAIResponses CC348/1585L internal/translator/gemini/openai/responses/gemini_openai-responses_response.go:381 (duplo coroa com gate de span); 2) streamCodexDuplex CC325 codex_websockets_duplex.go:39; 3) (*Manager).MarkResult CC314 conductor_cooldown.go:1636. God files por LOC de funcoes: conductor_cooldown.go 4217L/150fn, conductor_execution.go 3958L/117fn. Hubs fan-in: internal/util 67, config/registry 39. 137 pacotes internos, 761 arestas, 0 ciclos.

#arqueologia/hotspot #metricas/go

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^hotspots-de-toxicidade-do-cliproxyapi-podio-w8-106be41e7603-content
