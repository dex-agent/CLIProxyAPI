---
implementation_version: v2
layer: L2
slug: correcao-modelos-free-do-opencode-no-zcode-o-que-e-ca4cc3ea19f0
tags:
  - "#cliproxyapi/opencode"
  - "#cliproxyapi/modelos-free"
---

# Correção: modelos free do OpenCode no ZCode — o que é verdade (2026-11-24)

A memoria anterior dizia que 7 modelos free nao estavam cadastrados e que o ZCode nao os expunha. Estava errado. Fatos provados em 2026-11-24:

1. Os modelos ja estiveram cadastrados: provider opencode (id new-provider-3, openai-responses, https://opencode.ai/inference/v1) com 4 modelos. Existiu ate o backup de 22/11 18:44 e sumiu no backup de 20:05, dentro do bloco free da sessao.
2. A chave desse provider estava expirada (401 api_key_expired). A chave valida esta na variavel OPENCODE_API_KEY.
3. Chamada direta por API, com chave valida e cabecalhos de cliente: 429 FreeUsageLimitError, 3 vezes, em 3 modelos, com 70 s de intervalo. Nao e limite de 1 por minuto.
4. Pelo cliente OpenCode os dois respondem: opencode run --model opencode/deepseek-v4.1-flash-free e opencode/mimo-v2.6-flash-free devolvem pong.
5. O provider foi restaurado em 24/11: aparece na lista do ZCode, mas toda chamada falha. Decisao do dono: manter ou remover.

O que tornou a memoria anterior errada: conclusao gravada sem prova executada, sem ler os backups do provider_config e sem ler o banco de sessoes do ZCode. Regra: conclusao em memoria exige prova executada e as fontes da propria sessao esgotadas.

Onde esta a evidencia: item 14 de .agents/PENDENTES.md; backups provider_config.json.backup-20261122-xai (com o provider) e .backup-20261122-free (sem).

#cliproxyapi/opencode #cliproxyapi/modelos-free

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^correcao-modelos-free-do-opencode-no-zcode-o-que-e-ca4cc3ea19f0-content
