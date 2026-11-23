# -*- coding: utf-8 -*-
"""Testa os modelos do OpenCode Go que usam protocolos anthropic-messages e openai-responses."""
import json
import pathlib
import sqlite3
import urllib.error
import urllib.request
import uuid

DB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
cred = json.loads(
    sqlite3.connect(str(DB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()[0]
)
TOKEN = cred["access"]
meta = cred.get("metadata") or {}
ORG = meta.get("orgID") or "prj_default"


def base_headers():
    return {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "opencode/latest/2.2.0/desktop",
        "x-opencode-client": "desktop",
        "x-opencode-session": "ses_" + uuid.uuid4().hex[:24],
        "x-opencode-project": ORG,
        "x-opencode-directory": "C:/tmp",
    }


def probe_anthropic(model):
    url = "https://opencode.ai/inference/go/anthropic/v1/messages"
    h = base_headers()
    h["anthropic-version"] = "2023-06-01"
    body = json.dumps({
        "model": model,
        "max_tokens": 32,
        "messages": [{"role": "user", "content": "Responda apenas: pong"}],
    }).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h), timeout=45) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
            parts = d.get("content") or []
            txt = " ".join(p.get("text", "") for p in parts if isinstance(p, dict))
            return "OK", (txt or str(d)[:40])[:40]
    except urllib.error.HTTPError as e:
        return str(e.code), e.read().decode("utf-8", "replace")[:100].replace("\n", " ")
    except Exception as e:  # noqa: BLE001
        return "ERR", str(e)[:60]


def probe_responses(model):
    url = "https://opencode.ai/inference/go/openai/v1/responses"
    h = base_headers()
    body = json.dumps({"model": model, "input": "Responda apenas: pong", "max_output_tokens": 32}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h), timeout=45) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
            return "OK", str(d.get("output") or d.get("status") or "")[:40]
    except urllib.error.HTTPError as e:
        return str(e.code), e.read().decode("utf-8", "replace")[:100].replace("\n", " ")
    except Exception as e:  # noqa: BLE001
        return "ERR", str(e)[:60]


ANTHROPIC_MODELS = ["minimax-m3", "minimax-m2.7", "qwen4-max", "qwen3.8-flash", "qwen3.8-max",
                    "claude-haiku-5-5", "claude-sonnet-5-5"]
RESPONSES_MODELS = ["gpt-6-luna", "gpt-5.6-luna", "crouton-alpha-free",
                    "muse-spark-1.2-contributor", "grok-4.7", "muse-spark-1.3-contributor"]

print("=== anthropic-messages ===")
ok_a = []
for m in ANTHROPIC_MODELS:
    st, det = probe_anthropic(m)
    print("%-5s %-26s %s" % (st, m, det), flush=True)
    if st == "OK":
        ok_a.append(m)

print("\n=== openai-responses ===")
ok_r = []
for m in RESPONSES_MODELS:
    st, det = probe_responses(m)
    print("%-5s %-26s %s" % (st, m, det), flush=True)
    if st == "OK":
        ok_r.append(m)

out = pathlib.Path(".agents/receipts/oc-go-other-protocols.json")
out.write_text(json.dumps({"anthropic": ok_a, "responses": ok_r}, indent=1), encoding="utf-8")
print("\nOK anthropic:", ok_a)
print("OK responses:", ok_r)
