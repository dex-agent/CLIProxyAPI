# -*- coding: utf-8 -*-
# Registra provider xAI no provider_config.json do ZCode v2 (mesmo protocolo da casa)
import json, pathlib, uuid, shutil, sys

CFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
KEY = "<PROXY-KEY>"
BASE = "http://127.0.0.1:8317/v1"
NAME = "xAI (CLIProxyAPI)"
# somente modelos de texto que responderam 200 no proxy
MODELS = ["grok-4.7", "grok-4.6", "grok-4.5", "grok-4.20-0309-reasoning",
          "grok-4.20-0309-non-reasoning", "grok-4.20-multi-agent-0309",
          "grok-3-mini", "grok-3-mini-fast"]

raw = CFG.read_text(encoding="utf-8")
d = json.loads(raw)
rules = d["config"]["providerConfigRules"]["providerRules"]
if any(r.get("providerName") == NAME for r in rules):
    print("JA_EXISTE"); sys.exit(0)

pid = str(uuid.uuid4())
rules.append({
    "providerId": pid, "providerName": NAME,
    "config": {
        "access": {"type": "api-key", "apiKey": KEY},
        "api": {"type": "openai-responses", "baseUrl": BASE},
        "group": "standard-personal",
        "modelOrder": list(MODELS),
        "personalModelIds": list(MODELS),
    },
})
d["config"]["providerOrder"].append(pid)
pmr = d["config"]["modelConfigRules"]["providerModelRules"]
# grok = GPT-like: series exige nivel -> declarar high
pmr.extend({"providerId": pid, "modelId": m,
            "config": {"enabled": True, "optionSpecs": {"reasoningLevel": {"values": ["high"]}}}}
           for m in MODELS)

backup = CFG.with_name("provider_config.json.backup-20261122-xai")
shutil.copy2(CFG, backup)
CFG.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

d2 = json.loads(CFG.read_text(encoding="utf-8"))
r2 = [x for x in d2["config"]["providerConfigRules"]["providerRules"] if x.get("providerName") == NAME]
assert len(r2) == 1
mine = r2[0]
assert mine["config"]["personalModelIds"] == MODELS and mine["config"]["modelOrder"] == MODELS
assert pid in d2["config"]["providerOrder"]
assert sum(1 for x in d2["config"]["modelConfigRules"]["providerModelRules"] if x["providerId"] == pid) == len(MODELS)
print("OK provider:", NAME, "| providerId:", pid, "| models:", len(MODELS))
print("total providers:", len(d2["config"]["providerConfigRules"]["providerRules"]))
print("backup:", backup.name)
