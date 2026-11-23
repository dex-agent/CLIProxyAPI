# -*- coding: utf-8 -*-
"""Configura OpenCode Go DIRETO no ZCode (sem proxy) usando o token OAuth + headers.

ZCode suporta api.headers no providerConfigRules, entao o mesmo contrato que provou
200 no curl funciona nativamente.
"""
import json
import pathlib
import shutil
import sqlite3
import sys
import uuid

ZCFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
OCDB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
NAME = "OpenCode Go"

# modelos que responderam 200 no mapeamento
MODELS = [
    "hy4-preview", "glm-5.3-flash", "hy4-flash-free", "kimi-k3",
    "minimax-m3.1-flash", "mimo-v2.6-flash", "step-5-preview", "hy3",
    "glm-5.3", "kimi-k2.7-code", "hy4", "beam-free",
    "mimo-v2.6-pro", "kimi-k3.1-pro",
]

cred = json.loads(
    sqlite3.connect(str(OCDB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()[0]
)
token = cred["access"]
meta = cred.get("metadata") or {}
project = meta.get("orgID") or "prj_default"

d = json.loads(ZCFG.read_text(encoding="utf-8"))
rules = d["config"]["providerConfigRules"]["providerRules"]

existing = [r for r in rules if r.get("providerName") == NAME]
if existing:
    print("JA_EXISTE:", existing[0].get("providerId"))
    sys.exit(0)

pid = str(uuid.uuid4())
rules.append({
    "providerId": pid,
    "providerName": NAME,
    "config": {
        "access": {"type": "api-key", "apiKey": token},
        "api": {
            "type": "openai-chat-completions",
            "baseUrl": "https://opencode.ai/inference/go/openai/v1",
            "headers": {
                "User-Agent": "opencode/latest/2.2.0/desktop",
                "x-opencode-client": "desktop",
                "x-opencode-session": "ses_zcode_" + uuid.uuid4().hex[:20],
                "x-opencode-project": project,
                "x-opencode-directory": "C:/CodexProjetos/CLIProxyAPI",
            },
        },
        "group": "standard-personal",
        "modelOrder": list(MODELS),
        "personalModelIds": list(MODELS),
    },
})
d["config"]["providerOrder"].append(pid)

pmr = d["config"]["modelConfigRules"]["providerModelRules"]
pmr.extend(
    {"providerId": pid, "modelId": m, "config": {"enabled": True}}
    for m in MODELS
)

backup = ZCFG.with_name("provider_config.json.backup-20261123-opencode-go")
shutil.copy2(ZCFG, backup)
ZCFG.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# revalidacao
d2 = json.loads(ZCFG.read_text(encoding="utf-8"))
r2 = [x for x in d2["config"]["providerConfigRules"]["providerRules"] if x.get("providerName") == NAME]
assert len(r2) == 1
mine = r2[0]
assert mine["config"]["personalModelIds"] == MODELS
assert pid in d2["config"]["providerOrder"]
assert sum(1 for x in d2["config"]["modelConfigRules"]["providerModelRules"]
           if x["providerId"] == pid) == len(MODELS)
print("OK provider:", NAME, "| providerId:", pid, "| models:", len(MODELS))
print("total providers:", len(d2["config"]["providerConfigRules"]["providerRules"]))
print("backup:", backup.name)
