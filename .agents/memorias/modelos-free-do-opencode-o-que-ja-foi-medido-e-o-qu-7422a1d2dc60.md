---
implementation_version: v2
layer: L2
slug: modelos-free-do-opencode-o-que-ja-foi-medido-e-o-qu-7422a1d2dc60
tags:
  - "#cliproxyapi/opencode"
  - "#cliproxyapi/modelos-free"
---

# Modelos free do OpenCode: o que ja foi medido e o que falta

Medido em 2026-11-23 e 2026-11-24. Item aberto: opencode-free-fora-do-zcode no .agents/PENDENTES.md.

O que funciona e de onde vem:
- Plano free do OpenCode (sem Go), 9 modelos: beam-free, deepseek-v4.1-flash-free, flint-40b-free, iceman-free, nemotron-3.5-super-vl-free, nemotron-3.5-lightning-free, tidepool-alpha-free, hy4-flash-free, mimo-v2.6-flash-free. Todos deram OK pela suite que passa pelo cliente OpenCode (.agents/receipts/free-models-result.json; scripts test_free_models.py e test_free_parallel.py).
- Chamados direto pela API eles devolvem FreeUsageLimitError (recibos W25-beam-free.out e W25-hy4-free.out): so funcionam dentro do cliente OpenCode.
- So beam-free e hy4-flash-free tambem existem no plano Go, e por isso estao no ZCode: no provider OpenCode Go e no grupo Gratis (todos) pelos aliases free-oc-beam e free-oc-hy4-flash.

O que falta:
- Os outros 7 nao estao cadastrados no ZCode. O app-server do ZCode (CLI 0.18.0) expõe 206 modelos aos agents e nenhum deles e do plano free sem Go (.agents/receipts/W27-meta-zcode.json). O grupo Gratis (todos) nao os alcanca porque o grupo passa pela API do proxy.
- Lacuna aberta: o nome que o ZCode da ao provider do cliente OpenCode (o do seletor de modelo do Desktop). Sem esse par provider/model nao ha como criar agent. Agents de provider de plugin usam nome, nao UUID (ex.: moonshot-kimi/kimi-for-coding).
- hungerg-free: nao testado. iceman-contributor-free: bloqueado pela decisao de privacidade Training do dono (PENDENTES item 9).

Ferramentas da casa para este tema:
- Listar os modelos que o ZCode expõe: node meta-zcode.mjs --cwd <workspace> --out <recibo> (pacote zcode-orquestrador-multimodelo/scripts). Sem inferencia. Exige ZCODE_CLI_PATH apontando para %LOCALAPPDATA%/Programs/ZCode/resources/glm/zcode.cjs; sem ela devolve CLI version probe failed.
- list-zcode-models.mjs le o config antigo e nao ve provider de plugin. --help nao mostra ajuda: executa e grava um artefato.
- Criar agents: skill zcode-provider-manager-agents; editar modelos de um provider: zcode-provider-manager-model.
- Manter o grupo: free_aggregator.py (setup-proxy, reiniciar o proxy, register-zcode, test).

#cliproxyapi/opencode #cliproxyapi/modelos-free

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^modelos-free-do-opencode-o-que-ja-foi-medido-e-o-qu-7422a1d2dc60-content
