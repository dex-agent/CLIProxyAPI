---
schema: dex.frontmatter.envelope.v1
profile: dex.parking.item.v1
id: dex.parking.item:CLIPROXYRESYNC000002
localizador: EST-CLIPROXY-RESSYNC-GRATIS-TODOS
name: Grupo Gratis (todos) nao se ressincroniza sozinho
aliases: []
summary: 'O grupo depende de tres passos manuais: free_aggregator.py setup-proxy,
  reiniciar o proxy, free_aggregator.py register-zcode. Se o OpenRouter aposentar
  um modelo ou a lista de free do ZCode mudar, o grupo fica desatualizado ate alguem
  rodar de novo.'
tags:
- cliproxyapi/gratis-todos
- openrouter/free
hashtags:
- '#cliproxyapi/gratis-todos'
- '#openrouter/free'
type: risk
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
  - quando um alias free-or-* ou free-oc-* devolver 404
  - depois de cada sync dos free do OpenRouter
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
  reason: Nao ha gatilho automatico; colocar um exigiria decidir onde (hook, tarefa
    agendada ou rotina de sync), o que e decisao de dono.
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
closure: null
promoted_to: null
superseded_by: null
---

# Grupo Gratis (todos) nao se ressincroniza sozinho

^est-cliproxy-ressync-gratis-todos

## Resumo

O grupo depende de tres passos manuais: free_aggregator.py setup-proxy, reiniciar o proxy, free_aggregator.py register-zcode. Se o OpenRouter aposentar um modelo ou a lista de free do ZCode mudar, o grupo fica desatualizado ate alguem rodar de novo.

## Motivo do estacionamento

Nao ha gatilho automatico; colocar um exigiria decidir onde (hook, tarefa agendada ou rotina de sync), o que e decisao de dono.

## Garimpo vinculado

Medido em 2026-11-23: 5 modelos :free da lista do ZCode ja estavam aposentados no OpenRouter (404 no longer available) e 3 davam 429 de lotacao do fornecedor.

## Dados para retomar

Rodar em ordem: python -I -X utf8 .agents/scripts/free_aggregator.py setup-proxy; powershell -File .agents/scripts/start-proxy.ps1 (idempotente); python -I -X utf8 .agents/scripts/free_aggregator.py register-zcode; e a rota test para o numero medido.

## Proveniencia

- Origem: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
- Localizador: `EST-CLIPROXY-RESSYNC-GRATIS-TODOS`
- ID: `dex.parking.item:CLIPROXYRESYNC000002`
- Índice: [[../INDEX#^est-cliproxy-ressync-gratis-todos|EST-CLIPROXY-RESSYNC-GRATIS-TODOS]]
- Tags: #cliproxyapi/gratis-todos #openrouter/free
