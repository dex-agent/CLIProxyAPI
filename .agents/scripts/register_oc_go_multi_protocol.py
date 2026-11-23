# -*- coding: utf-8 -*-
"""Registra OpenCode Go (Anthropic) e (Responses) no ZCode — protocolos alternativos.

ZCode aceita um api.type por provider, entao cada protocolo vira um provider.
"""
import json
import pathlib
import shutil
import sqlite3
import sys
import uuid

ZCFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
OCDB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"

PROVIDERS = [
    {
        "name": "OpenCode Go (Anthropic)",
        "type": "anthropic-messages",
        "base": "https://opencode.ai/inference/go/anthropic/v1",
        "models": ["minimax-m3", "qwen4-max", "qwen3.8-flash", "qwen3.8-max", "claude-haiku-5-5"],
    },
    {
        "name": "OpenCode Go (Responses)",
        "type": "openai-responses",
        "base": "https://opencode.ai/inference/go/openai/v1",
        "models": ["gpt-6-luna", "gpt-5.6-luna", "grok-4.7"],
    },
]

cred = json.loads(
    sqlite3.connect(str(OCDB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()[0]
)
TOKEN = cred["access"]
ORG = (cred.get("metadata") or {}).get("orgID") or "prj_default"

d = json.loads(ZCFG.read_text(encoding="utf-8"))
rules = d["config"]["providerConfigRules"]["providerRules"]
pmr = d["config"]["modelConfigRules"]["providerModelRules"]
added = []

for spec in PROVIDERS:
    if any(r.get("providerName") == spec["name"] for r in rules):
        print("JA_EXISTE:", spec["name"])
        continue
    pid = str(uuid.uuid4())
    headers = {
        "User-Agent": "opencode/latest/2.2.0/desktop",
        "x-opencode-client": "desktop",
        "x-opencode-session": "ses_zcode_" + uuid.uuid4().hex[:20],
        "x-opencode-project": ORG,
        "x-opencode-directory": "C:/CodexProjetos/CLIProxyAPI",
    }
    if spec["type"] == "anthropic-messages":
        headers["anthropic-version"] = "2023-06-01"
    rules.append({
        "providerId": pid,
        "providerName": spec["name"],
        "config": {
            "access": {"type": "api-key", "apiKey": TOKEN},
            "api": {"type": spec["type"], "baseUrl": spec["base"], "headers": headers},
            "group": "standard-personal",
            "modelOrder": list(spec["models"]),
            "personalModelIds": list(spec["models"]),
        },
    })
    d["config"]["providerOrder"].append(pid)
    pmr.extend(
        {"providerId": pid, "modelId": m, "config": {"enabled": True}}
        for m in spec["models"]
    )
    added.append((spec["name"], pid, len(spec["models"])))

if not added:
    sys.exit(0)

backup = ZCFG.with_name("provider_config.json.backup-20261123-oc-multi-proto")
shutil.copy2(ZCFG, backup)
ZCFG.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

d2 = json.loads(ZCFG.read_text(encoding="utf-8"))
rules2 = d2["config"]["providerConfigRules"]["providerRules"]
for name, pid, n in added:
    r = [x for x in rules2 if x.get("providerName") == name][0]
    assert len(r["config"]["personalModelIds"]) == n
    assert pid in d2["config"]["providerOrder"]
    print("OK:", name, "|", n, "modelos | id:", pid[:8])
print("total providers:", len(rules2))
print("backup:", backup.name)
print("\nREINICIE O ZCODE para carregar.")
