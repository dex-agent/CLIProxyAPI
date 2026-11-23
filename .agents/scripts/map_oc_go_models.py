# -*- coding: utf-8 -*-
"""Mapeia TODOS os modelos do OpenCode Go que funcionam via API direta."""
import json
import pathlib
import sqlite3
import urllib.error
import urllib.request
import uuid

DB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
BASE = "https://opencode.ai/inference/go/openai/v1/chat/completions"

cred = json.loads(
    sqlite3.connect(str(DB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()[0]
)
TOKEN = cred["access"]

# catalogo do opencode-go (43 modelos)
req_cat = urllib.request.Request(
    "https://models.opencode.ai/experimental/v2.0/api.json",
    headers={"User-Agent": "opencode/2.2.0"},
)
catalog = json.loads(urllib.request.urlopen(req_cat, timeout=30).read().decode())
go_models = catalog["opencode-go"]["models"]

# so os que usam chat-completions via /go/openai/v1
targets = []
for mid, meta in go_models.items():
    api = (meta.get("api") or {})
    cc = api.get("chat-completions")
    if cc and "go/openai/v1" in (cc.get("base_url") or ""):
        targets.append(mid)

print("modelos chat-completions do Go:", len(targets))


def probe(model):
    headers = {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "opencode/latest/2.2.0/desktop",
        "x-opencode-client": "desktop",
        "x-opencode-session": "ses_" + uuid.uuid4().hex[:24],
        "x-opencode-project": "prj_probe",
        "x-opencode-directory": "C:/tmp",
    }
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": "Responda apenas: pong"}],
        "max_tokens": 16,
    }).encode()
    req = urllib.request.Request(BASE, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8", "replace"))
            try:
                text = data["choices"][0]["message"]["content"]
            except (KeyError, IndexError):
                text = str(data)[:40]
            return "OK", (text or "")[:30]
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return str(exc.code), body[:90].replace("\n", " ")
    except Exception as exc:  # noqa: BLE001
        return "ERR", str(exc)[:60]


results = []
for model in targets:
    status, detail = probe(model)
    results.append({"model": model, "status": status, "detail": detail})
    print("%-5s %-30s %s" % (status, model, detail), flush=True)

out = pathlib.Path(".agents/receipts/oc-go-working.json")
out.write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
ok = [r for r in results if r["status"] == "OK"]
print("\nFUNCIONAM: %d/%d" % (len(ok), len(results)))
print("lista OK:", [r["model"] for r in ok])
