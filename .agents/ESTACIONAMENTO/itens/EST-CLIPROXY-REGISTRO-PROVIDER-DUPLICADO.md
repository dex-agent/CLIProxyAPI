---
schema: dex.frontmatter.envelope.v1
profile: dex.parking.item.v1
id: dex.parking.item:CLIPROXYREGDUP000001
localizador: EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO
name: Registro de provider no ZCode duplicado em seis scripts
aliases: []
summary: 'Cinco scripts (register_zcode_provider, register_xai_provider, register_opencode_go_zcode,
  register_oc_go_multi_protocol, add_free_models_zcode) e a rota register-zcode do
  free_aggregator repetem a mesma logica: backup do provider_config.json, append de
  providerRule, regra por modelo, revalidacao.'
tags:
- cliproxyapi/registro-provider
- zcode/duplicacao
hashtags:
- '#cliproxyapi/registro-provider'
- '#zcode/duplicacao'
type: debt
status: active
owner: sessao-do-projeto
scope: project
priority: null
origin:
  type: conversation
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
  flow_id: null
  phase: implementation
  actor: null
review:
  after: null
  triggers:
  - no proximo cadastro ou alteracao de provider no provider_config.json do ZCode
destination:
  type: monitor
  target: dex-frontmatter-finder-padrao
  owner: estacionamento
related: []
created_at: '2026-11-23T12:10:05-03:00'
updated_at: '2026-11-23T12:10:05-03:00'
lifecycle:
- at: '2026-11-23T12:10:05-03:00'
  event: created
  from: null
  to: active
  by: sessao-do-projeto
  reason: Lateral ao bloco do grupo de gratuitos; unificar agora ampliaria o escopo
    e tocaria scripts que ja rodaram.
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
closure: null
promoted_to: null
superseded_by: null
---

# Registro de provider no ZCode duplicado em seis scripts

^est-cliproxy-registro-provider-duplicado

## Resumo

Cinco scripts (register_zcode_provider, register_xai_provider, register_opencode_go_zcode, register_oc_go_multi_protocol, add_free_models_zcode) e a rota register-zcode do free_aggregator repetem a mesma logica: backup do provider_config.json, append de providerRule, regra por modelo, revalidacao.

## Motivo do estacionamento

Lateral ao bloco do grupo de gratuitos; unificar agora ampliaria o escopo e tocaria scripts que ja rodaram.

## Garimpo vinculado

Ponto cego de R6 (conhecimento unico): reuso.py nao enxerga .agents/scripts do repo, entao devolveu nenhum candidato.

## Dados para retomar

Extrair register_provider(name, api_type, base_url, key, headers, models, position) num modulo unico e fazer os scripts existentes importarem. Fonte: .agents/scripts/ no repo CLIProxyAPI.

## Proveniencia

- Origem: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
- Localizador: `EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO`
- ID: `dex.parking.item:CLIPROXYREGDUP000001`
- Índice: [[../INDEX#^est-cliproxy-registro-provider-duplicado|EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO]]
- Tags: #cliproxyapi/registro-provider #zcode/duplicacao
