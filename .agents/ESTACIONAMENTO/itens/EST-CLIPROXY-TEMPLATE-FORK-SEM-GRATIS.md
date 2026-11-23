---
schema: dex.frontmatter.envelope.v1
profile: dex.parking.item.v1
id: dex.parking.item:CLIPROXYTMPLGRATIS04
localizador: EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS
name: config.example.fork.yaml nao descreve o bloco gratis-todos
aliases: []
summary: O template versionado do fork traz as curas do antigravity mas nao o bloco
  api-keys.openai-compatibility com os upstreams openrouter-free e opencode-go.
tags:
- cliproxyapi/fork
- cliproxyapi/gratis-todos
hashtags:
- '#cliproxyapi/fork'
- '#cliproxyapi/gratis-todos'
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
  - quando o fork publico for limpo ou recriado
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
  reason: So faz sentido versionar depois de a sorte do fork publico ser decidida.
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
closure: null
promoted_to: null
superseded_by: null
---

# config.example.fork.yaml nao descreve o bloco gratis-todos

^est-cliproxy-template-fork-sem-gratis

## Resumo

O template versionado do fork traz as curas do antigravity mas nao o bloco api-keys.openai-compatibility com os upstreams openrouter-free e opencode-go.

## Motivo do estacionamento

So faz sentido versionar depois de a sorte do fork publico ser decidida.

## Garimpo vinculado

Nenhuma informacao perdida: o gerador e free_aggregator.py setup-proxy, que le as chaves do ambiente e nunca as escreve em texto.

## Dados para retomar

Acrescentar ao config.example.fork.yaml um bloco comentado, com CHANGE_ME no lugar de api-key, copiando a forma de build_block() em .agents/scripts/free_aggregator.py.

## Proveniencia

- Origem: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
- Localizador: `EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS`
- ID: `dex.parking.item:CLIPROXYTMPLGRATIS04`
- Índice: [[../INDEX#^est-cliproxy-template-fork-sem-gratis|EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS]]
- Tags: #cliproxyapi/fork #cliproxyapi/gratis-todos
