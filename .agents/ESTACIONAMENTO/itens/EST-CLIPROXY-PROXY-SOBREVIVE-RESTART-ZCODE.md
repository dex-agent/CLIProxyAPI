---
schema: dex.frontmatter.envelope.v1
profile: dex.parking.item.v1
id: dex.parking.item:CLIPROXYSURVIVE00003
localizador: EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE
name: Proxy via WMI ainda nao provado contra restart do ZCode
aliases: []
summary: O proxy morria com o ZCode quando subia por Start-Process (herda a job do
  host) e morreu de novo quando subiu por WMI com janela de console visivel. A versao
  atual usa WMI com ShowWindow=0 e sobreviveu a trocas de chamada e ao fim de tarefas
  em background, mas nenhum restart do ZCode aconteceu desde entao.
tags:
- cliproxyapi/proxy
- windows/processo-desacoplado
hashtags:
- '#cliproxyapi/proxy'
- '#windows/processo-desacoplado'
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
  - no primeiro uso depois do proximo restart do ZCode
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
  reason: So da para provar depois de um restart real do ZCode, que e acao do dono.
  reference: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
closure: null
promoted_to: null
superseded_by: null
---

# Proxy via WMI ainda nao provado contra restart do ZCode

^est-cliproxy-proxy-sobrevive-restart-zcode

## Resumo

O proxy morria com o ZCode quando subia por Start-Process (herda a job do host) e morreu de novo quando subiu por WMI com janela de console visivel. A versao atual usa WMI com ShowWindow=0 e sobreviveu a trocas de chamada e ao fim de tarefas em background, mas nenhum restart do ZCode aconteceu desde entao.

## Motivo do estacionamento

So da para provar depois de um restart real do ZCode, que e acao do dono.

## Garimpo vinculado

O conhecimento job-object-kill-on-close da casa confirma o mecanismo (Job Object) mas nao tem receita de como um servico sai dele. A janela fechada e causa provavel, nao provada.

## Dados para retomar

Conferir: powershell -NoProfile -ExecutionPolicy Bypass -File .agents/scripts/start-proxy.ps1. Se responder JA_ATIVO, a sobrevivencia esta provada. Se subir do zero (INICIADO), o proxy morreu no restart: proxima hipotese e tarefa agendada do Windows, que exige decisao do dono.

## Proveniencia

- Origem: zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb
- Localizador: `EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE`
- ID: `dex.parking.item:CLIPROXYSURVIVE00003`
- Índice: [[../INDEX#^est-cliproxy-proxy-sobrevive-restart-zcode|EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE]]
- Tags: #cliproxyapi/proxy #windows/processo-desacoplado
