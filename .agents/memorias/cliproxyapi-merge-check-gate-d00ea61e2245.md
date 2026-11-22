---
implementation_version: v2
layer: L2
slug: cliproxyapi-merge-check-gate-d00ea61e2245
tags:
  - "#cliproxyapi/merge-gate"
  - "#git/hooks"
---

# CLIProxyAPI merge-check gate

Hook pre-merge-commit instalado em 2026-11-22 (padrao da casa: hook commitado + core.hooksPath). core.hooksPath=tools/hooks; arquivos tools/hooks/pre-merge-commit + tools/hooks/merge-check.conf (SUITE="" — a suite nativa go test ./... esta vermelha no Windows com 9 falhas conhecidas, entao o gate avisa e nao bloqueia ate alguem declarar a suite minima). Rotas do hook: nao-merge exit 0 silencioso; MERGE_CHECK_SKIP=1 ou --no-verify passam com 1 linha; sem resolucao manual roda code-review-graph merge-check (exit 0 passa, 1 bloqueia conflito texto/semantico, 2 execution_error nao bloqueia); MERGE_MSG com '# Conflicts:' roda a suite direto no worktree resolvido. Ficha MERGE-CHECK-HOOK-PRE-MERGE no .agents/GATILHOS-VIVOS.md. Pendencia estacionada: declarar SUITE minima (os 102 pacotes verdes do W6).

#cliproxyapi/merge-gate #git/hooks

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^cliproxyapi-merge-check-gate-d00ea61e2245-content
