---
schema: dex.frontmatter.envelope.v1
profile: dex.parking.item.v1
id: dex.parking.item:CLIPROXYSUITE0000005
localizador: EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK
name: 'Gate de merge com SUITE vazia: avisa e nao bloqueia'
aliases: []
summary: 'tools/hooks/merge-check.conf esta com SUITE vazia, entao o hook pre-merge-commit
  nao bloqueia merge nenhum. A suite nativa go test ./... esta vermelha no Windows
  (9 falhas em 6 pacotes: 8 de ambiente e 1 golden drift).'
tags:
- cliproxyapi/merge-gate
hashtags:
- '#cliproxyapi/merge-gate'
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
  - quando o dono quiser o gate de merge bloqueando de verdade
destination:
  type: monitor
  target: dex-frontmatter-finder-padrao
  owner: estacionamento
related: []
created_at: '2026-11-23T12:19:13-03:00'
updated_at: '2026-11-23T12:19:13-03:00'
lifecycle:
- at: '2026-11-23T12:19:13-03:00'
  event: created
  from: null
  to: active
  by: sessao-do-projeto
  reason: Declarar a suite minima exige escolher os pacotes verdes e decidir o que
    fazer com as falhas de ambiente; e decisao de dono.
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
closure: null
promoted_to: null
superseded_by: null
---

# Gate de merge com SUITE vazia: avisa e nao bloqueia

^est-cliproxy-suite-minima-merge-check

## Resumo

tools/hooks/merge-check.conf esta com SUITE vazia, entao o hook pre-merge-commit nao bloqueia merge nenhum. A suite nativa go test ./... esta vermelha no Windows (9 falhas em 6 pacotes: 8 de ambiente e 1 golden drift).

## Motivo do estacionamento

Declarar a suite minima exige escolher os pacotes verdes e decidir o que fazer com as falhas de ambiente; e decisao de dono.

## Garimpo vinculado

Era o unico item de .agents/ESTACIONAMENTO.md (superficie improvisada no primeiro dia). Migrado para o diretorio canonico; o arquivo antigo foi para a LIXEIRA com manifesto.

## Dados para retomar

Preencher SUITE em tools/hooks/merge-check.conf com go test dos pacotes verdes (102 pacotes ok em .agents/receipts/W6-test-out.txt), usando o go de .agents/scripts/go-env.sh, e provar com um merge real.

## Proveniencia

- Origem: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
- Localizador: `EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK`
- ID: `dex.parking.item:CLIPROXYSUITE0000005`
- Índice: [[../INDEX#^est-cliproxy-suite-minima-merge-check|EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK]]
- Tags: #cliproxyapi/merge-gate
