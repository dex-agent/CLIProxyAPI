# -*- coding: utf-8 -*-
"""Le a mensagem de erro INTEIRA dos modelos do OpenCode Go que falharam,
e levanta o custo de cada modelo no catalogo (para saber o que e gratuito)."""
import json
import pathlib
import sqlite3
import urllib.error
import urllib.request
import uuid

DB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
BASE_GO = "https://opencode.ai/inference/go/openai/v1/chat/completions"
CATALOG = "https://models.opencode.ai/experimental/v2.0/api.json"

cred = json.loads(
    sqlite3.connect(str(DB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()[0]
)
TOKEN = cred["access"]
ORG = (cred.get("metadata") or {}).get("orgID") or "prj_default"

HEADERS = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "opencode/latest/2.2.0/desktop",
    "x-opencode-client": "desktop",
    "x-opencode-session": "ses_" + uuid.uuid4().hex[:24],
    "x-opencode-project": ORG,
    "x-opencode-directory": "C:/tmp",
}

BLOCKED = [
    "deepseek-v4.1-flash", "deepseek-v4-pro", "longcat-2.5",
    "iceman-contributor-free", "muse-spark-1.3-contributor", "space-bunny",
    "deepseek-v4.1-flash-free",
]

print("=== MENSAGENS INTEIRAS ===", flush=True)
for model in BLOCKED:
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": "pong"}],
        "max_tokens": 8,
    }).encode("utf-8")
    req = urllib.request.Request(BASE_GO, data=body, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            print("%-30s 200 OK" % model, flush=True)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            msg = json.loads(raw)
            err = msg.get("error", msg)
            text = err.get("message", "") if isinstance(err, dict) else str(err)
            etype = err.get("type", "") if isinstance(err, dict) else ""
        except Exception:  # noqa: BLE001
            text, etype = raw, ""
        print("%-30s %s %s" % (model, exc.code, etype), flush=True)
        print("    " + text, flush=True)
    except Exception as exc:  # noqa: BLE001
        print("%-30s ERR %s" % (model, str(exc)[:80]), flush=True)

print("\n=== CUSTO NO CATALOGO ===", flush=True)
req_cat = urllib.request.Request(CATALOG, headers={"User-Agent": "opencode/2.2.0"})
catalog = json.loads(urllib.request.urlopen(req_cat, timeout=30).read().decode())

for provider in ("opencode-go", "opencode"):
    models = catalog[provider]["models"]
    free, paid, unknown = [], [], []
    for mid, meta in models.items():
        costs = meta.get("cost") or {}
        vals = [v for v in costs.values() if isinstance(v, (int, float))]
        if not vals:
            unknown.append(mid)
        elif max(vals) == 0:
            free.append(mid)
        else:
            paid.append(mid)
    print("[%s] total=%d | custo zero=%d | pago=%d | sem custo declarado=%d"
          % (provider, len(models), len(free), len(paid), len(unknown)), flush=True)
    print("   custo zero:", free, flush=True)
    print("   sem custo declarado:", unknown[:20], flush=True)
    if provider == "opencode-go":
        print("   pago:", paid, flush=True)
