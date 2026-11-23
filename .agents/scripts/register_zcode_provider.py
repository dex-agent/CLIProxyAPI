# -*- coding: utf-8 -*-
# Registers the CLIProxyAPI provider (antigravity via the local proxy) in the ZCode v2 provider_config.json
# House protocol (note zcode-provider-config-estrutura-v2 + session 132e1d87):
# fresh-read -> backup in the same dir -> smallest delta -> revalidation. Never echo the key.
import json, pathlib, uuid, shutil, sys, hashlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from free_aggregator import proxy_key  # noqa: E402  (single source for the proxy access key)

CFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
KEY = proxy_key()
BASE = "http://127.0.0.1:8317/v1"
NAME = "CLIProxyAPI"
MODELS = [
    "gemini-4-argon-high", "gemini-3.8-flash-high", "gemini-3.8-flash-tiered",
    "gemini-3.1-flash-image", "gemini-3.1-flash-lite", "gemini-3.5-flash-lite",
    "gemini-4-hydrogen-xhigh", "gemini-4-neon-xhigh", "gemini-3-flash",
    "gpt-oss-120b-medium", "claude-opus-5-5-high", "claude-sonnet-5-5-high",
]

raw = CFG.read_text(encoding="utf-8")
d = json.loads(raw)
rules = d["config"]["providerConfigRules"]["providerRules"]

if any(r.get("providerName") == NAME for r in rules):
    print("JA_EXISTE"); sys.exit(0)

pid = str(uuid.uuid4())
rule = {
    "providerId": pid,
    "providerName": NAME,
    "config": {
        "access": {"type": "api-key", "apiKey": KEY},
        "api": {"type": "openai-chat-completions", "baseUrl": BASE},
        "group": "standard-personal",
        "modelOrder": list(MODELS),
        "personalModelIds": list(MODELS),
    },
}
rules.append(rule)
d["config"]["providerOrder"].append(pid)
pmr = d["config"]["modelConfigRules"]["providerModelRules"]
pmr.extend({"providerId": pid, "modelId": m, "config": {"enabled": True}} for m in MODELS)

backup = CFG.with_name("provider_config.json.backup-20261122-cliproxyapi")
shutil.copy2(CFG, backup)
CFG.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# revalidation
d2 = json.loads(CFG.read_text(encoding="utf-8"))
r2 = d2["config"]["providerConfigRules"]["providerRules"]
assert len(r2) == len(rules) and any(x.get("providerName") == NAME for x in r2)
mine = [x for x in r2 if x.get("providerName") == NAME][0]
assert mine["config"]["modelOrder"] == MODELS and mine["config"]["personalModelIds"] == MODELS
assert pid in d2["config"]["providerOrder"]
assert sum(1 for x in d2["config"]["modelConfigRules"]["providerModelRules"] if x["providerId"] == pid) == 12
ids = [x.get("providerName") for x in r2]
assert len(ids) == len(set(ids)), "nomes duplicados"
print("OK provider:", NAME, "| providerId:", pid)
print("providers:", len(r2), "| providerOrder:", len(d2["config"]["providerOrder"]), "| pmr novas: 12")
print("backup:", backup.name)
