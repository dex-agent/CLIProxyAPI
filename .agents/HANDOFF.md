# HANDOFF — CLIProxyAPI (arqueologia 2026-11-22)

## Estado
Arqueologia W-1..W10 executada (tier COMPLETO, 2405 fontes Go/143k linhas). HEAD `6eb8554f` (main, após pull ff de 36 commits).

## Feito
- W-1..W5 fechados com receipts em `.agents/receipts/` (W1 inventário, W2 encoding 3 camadas, W3 grafo Tarjan, W4 hidden, W5 segredos).
- W6: build VERDE (exit 0 sem pipe); test VERMELHO honesto — 9 falhas classificadas (8 ambiente-Windows, 1 golden drift REAL) em `W6-build-test.json`.
- W7: CRG 2.4.0 build verde (tree-sitter-go nativo, SEM feeder) + graphify rico (36.327 nós) + grafo_gate **5/6 verde, exit 1 por 1 achado real** (span 1585L — pódio).
- W8: pódio completo com arquivo:linha (gocyclo 28.660 rotinas, cobertura 100%).
- W9/W10: INDEX.md + DEPENDENCIES.md raiz, GATILHOS-VIVOS/HANDOFF/PENDENTES/LIXEIRA, memórias V2 (dex-memoria scope=project), commits locais por bloco.

## Não feito / pendente (owner)
- Correção do golden drift e das falhas Windows → upstream router-for-me (PENDENTES.md com rota `dex-gerar-issues-git`).
- `.gitattributes` pin (proposta, decisão upstream).
- Push não executado — aguarda ordem do dono (upstream público).

## Retomada
1. Ler GATILHOS-VIVOS → 2. `source .agents/scripts/go-env.sh` → 3. receipts em `.agents/receipts/` → 4. grafo fresco? `code-review-graph status`.

## W11 (2026-11-22 tarde) — instalação viva
- Proxy no ar: `./cli-proxy-api.exe --config config.yaml` (127.0.0.1:8317; key em config.yaml local). Reiniciar após reboot: mesmo comando (server não é serviço).
- Provider CLIProxyAPI no ZCode picker (12 modelos antigravity). Nomes com sufixo -high/-tiered/-xhigh são os IDs reais do catálogo.
- E2E: 3 classes testadas com resposta. Receipts W11-*.
- Rota B (decisão gemini-zcode 261122): este provider serve testes/uso pontual — NÃO propõe substituir elenco ZCode.
