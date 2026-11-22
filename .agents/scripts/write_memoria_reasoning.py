# -*- coding: utf-8 -*-
# Memória tema zcode: contrato de reasoningLevel para providers customizados (GO dono 2026-11-22)
import json, pathlib

payload = {
 "scope": "theme",
 "theme": "zcode",
 "title": "Agent claude-* em provider custom exige reasoningLevel declarado; gemini/gpt caem no toggle on/off",
 "trigger": "criar agent ou model rule de provider customizado com modelId claude-*/gpt-*/glm-*; erro reasoning-level-missing ou reasoning-level-not-supported no dispatch de agent; cadastrar modelos de thinking no ZCode",
 "body": (
  "Contrato do host ZCode (corpus mentor-documental-zcode r3, tabela oficial de niveis): o host classifica o modelId "
  "por SERIE para exigir nivel de raciocinio no dispatch de agent — Claude series: low/medium/high/xhigh (default "
  "medium), NIVEL OBRIGATORIO; GPT series: low/medium/high/xhigh (default medium); GLM-5.3 low/high/max; GLM-5.2 "
  "nothink/high/max; Kimi K3 low/high/max; DeepSeek V4 high/max; OUTROS modelos custom: toggle on/off ou nenhum "
  "nivel, 'Defined by the model configuration'. "
  "SINTOMAS MEDIOS ao vivo (2026-11-22, provider CLIProxyAPI): agent com model claude-* e thoughtLevel 'enabled' → "
  "reasoning-level-NOT-SUPPORTED ('enabled' fora do vocabulario claude); sem thoughtLevel → reasoning-level-MISSING "
  "(serie claude exige); com 'high' MAS regra do modelo sem optionSpecs → AINDA missing (o registry valida contra o "
  "que a MODEL RULE declara, nao contra o vocabulario da serie). Agents gemini-* passaram com 'enabled' (caem em "
  "Other custom = toggle). "
  "FIX (precedente Flint do contrato zcode-models.md da casa): declarar na providerModelRule do modelo "
  "config.optionSpecs.reasoningLevel = {'values': ['high']} — values ordenado do menor ao maior; chamadas "
  "auxiliares de conectividade pegam values[0]; agent mantem thoughtLevel: high. Aplicado e PROVADO: dispatch do "
  "agent claude-sonnet-5-5-high passou a validar (backup provider_config.json.backup-20261122-reasoning-fix). "
  "Nao copiar thoughtLevel entre modelos (regra da skill zcode-sync); nivel e por par provider/model. "
  "Escape existente no codigo: allowMissingReasoning (opcao interna do resolveRegistryOwnedModelSelection)."
 ),
 "tags": ["#zcode/reasoning-level", "#zcode/provider-config", "#agents/criacao"],
}
pathlib.Path(".agents/receipts/mem/m-reasoning.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
print("payload reasoning ok")
