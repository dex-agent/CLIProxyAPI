# -*- coding: utf-8 -*-
# Espelha 3 auto-memorias do host no dex-memoria (scope project), slugs casando por prefixo
import json, pathlib

out = pathlib.Path(".agents/receipts/mem")
mems = [
 {"scope": "project",
  "title": "CLIProxyAPI merge-check gate",
  "trigger": "fazer merge de branches no CLIProxyAPI",
  "body": ("Hook pre-merge-commit instalado em 2026-11-22 (padrao da casa: hook commitado + core.hooksPath). "
           "core.hooksPath=tools/hooks; arquivos tools/hooks/pre-merge-commit + tools/hooks/merge-check.conf "
           "(SUITE=\"\" — a suite nativa go test ./... esta vermelha no Windows com 9 falhas conhecidas, entao o gate "
           "avisa e nao bloqueia ate alguem declarar a suite minima). Rotas do hook: nao-merge exit 0 silencioso; "
           "MERGE_CHECK_SKIP=1 ou --no-verify passam com 1 linha; sem resolucao manual roda code-review-graph "
           "merge-check (exit 0 passa, 1 bloqueia conflito texto/semantico, 2 execution_error nao bloqueia); MERGE_MSG "
           "com '# Conflicts:' roda a suite direto no worktree resolvido. Ficha MERGE-CHECK-HOOK-PRE-MERGE no "
           ".agents/GATILHOS-VIVOS.md. Pendencia estacionada: declarar SUITE minima (os 102 pacotes verdes do W6)."),
  "tags": ["#cliproxyapi/merge-gate", "#git/hooks"]},
 {"scope": "project",
  "title": "CLIProxyAPI staleness derivados",
  "trigger": "citar numero de artefato derivado (grafo CRG, graphify, INDEX) no CLIProxyAPI",
  "body": ("Antes de LER/CITAR qualquer artefato derivado, comparar 3 numeros: quando a FONTE mudou "
           "(git log -1 --format=%cI -- <escopo>), quando o ARTEFATO nasceu (CRG: code-review-graph doctor; "
           "graphify: built_at_commit em graphify-out/graph.json), e fonte>artefato => STALE => regenerar antes de citar. "
           "Inventario 2026-11-22: CRG .agents/CODE-REVIEW-GRAPH (regen: code-review-graph update --data-dir "
           ".agents/CODE-REVIEW-GRAPH); graphify-out/graph.json (regen: graphify update .); INDEX.md raiz e .agents "
           "(fiscal dex-fechamento-projeto-atualizado superficie 4); receipts datados no nome; PLAYBOOK/MAPAS "
           "inexistentes (n-a). Ficha STALENESS-ARTEFATOS-DERIVADOS no GATILHOS-VIVOS. Regenerador ausente => "
           "artefato NAO CONSULTAVEL, nunca citar numero dele."),
  "tags": ["#cliproxyapi/staleness", "#artefatos/derivados"]},
 {"scope": "project",
  "title": "ZCode provider config e agents",
  "trigger": "criar ou editar provider/modelos/agents do ZCode para o CLIProxyAPI",
  "body": ("provider_config.json v2 do ZCode: providers moram em config.providerConfigRules.providerRules (NAO no "
           "array providers, que existe vazio) com {providerId, providerName, config:{access, api, group, modelOrder, "
           "personalModelIds}}; propriedades por modelo em config.modelConfigRules.providerModelRules. Agent de "
           "claude-* exige optionSpecs.reasoningLevel.values na regra do modelo (serie Claude exige nivel; gemini cai "
           "em toggle on/off). Frontmatter de agent usa model: \"<providerId>/<modelId>\" e thoughtLevel nao se copia "
           "entre modelos. A UI normaliza o ID tirando o sufixo de esforco (-high vira Effort), entao o proxy precisa "
           "de model-alias com fork:true para aceitar os dois nomes. Molde canonico de agent: "
           "agent-gemma4-31b-free.md em ~/.zcode/agents."),
  "tags": ["#zcode/provider-config", "#agents/criacao"]},
]
for i, m in enumerate(mems):
    (out / f"mirror-{i}.json").write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")
print("payloads:", len(mems))
