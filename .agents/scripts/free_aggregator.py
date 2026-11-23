# -*- coding: utf-8 -*-
"""Free-models group "Gratis (todos)" - every free model in one place.

ZCode groups models by provider, and one provider has a single base URL and key.
The free models live in two places (OpenRouter and OpenCode Go), so the proxy is
what joins them: it exposes `free-or-*` aliases (OpenRouter) and `free-oc-*` aliases
(OpenCode Go), and ZCode points a single provider at the proxy.

Routes:
  setup-proxy     rewrites the api-keys.openai-compatibility block of the proxy config.yaml
  register-zcode  creates/updates the "Gratis (todos)" provider in the ZCode provider_config.json
  test            tests each free-* alias through the proxy and writes status + verdict (for the watcher)
  status | verdict  print the files the watcher reads
"""
import datetime
import json
import pathlib
import re
import shutil
import sqlite3
import sys
import time
import urllib.error
import urllib.request
import uuid

REPO = pathlib.Path(r"C:\CodexProjetos\CLIProxyAPI")
PROXY_CFG = REPO / "config.yaml"
RECEIPTS = REPO / ".agents" / "receipts"
STATUS = RECEIPTS / "free-agg-status.txt"
VERDICT = RECEIPTS / "free-agg-verdict.txt"
RESULT = RECEIPTS / "free-aggregator-result.json"

ZCFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
OCDB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"

PROXY_BASE = "http://127.0.0.1:8317/v1"
ZCODE_PROVIDER = "Gratis (todos)"
OR_CATALOG = "https://openrouter.ai/api/v1/models"

START_MARK = "# INICIO gratis-todos (gerado por free_aggregator.py setup-proxy)"
END_MARK = "# FIM gratis-todos"
OLD_HEADER = "# Provedor OpenAI-compat custom"
TOKEN_MARK = "# opencode-go-token (renovado por refresh_opencode_go_token.py)"

# OpenCode Go free models that answered 200 during mapping
OC_FREE = [("hy4-flash-free", "free-oc-hy4-flash"), ("beam-free", "free-oc-beam")]

# suffixes the ZCode UI turns into effort levels (dropped from the model name)
EFFORT_SUFFIXES = ("-high", "-low", "-medium", "-max", "-xhigh", "-min", "-nothink")


def yaml_str(value):
    """String JSON e um escalar YAML valido entre aspas."""
    return json.dumps(value)


def proxy_key(config=PROXY_CFG):
    """First entry of access.api-keys in the proxy config; the value never lives in a script."""
    lines = config.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "access:":
            for item in lines[i + 1:]:
                found = re.match(r"""\s*-\s*["']?([^"'\s#]+)""", item)
                if found:
                    return found.group(1)
                if item[:1] not in ("", " ", "\t", "#"):
                    break
    raise SystemExit("access.api-keys nao encontrado em " + str(config))


PROXY_KEY = proxy_key()


def or_alias(model_id):
    base = model_id.split(":")[0].strip("/")
    slug = base.replace("/", "-").replace("_", "-").lower()
    if slug.endswith(EFFORT_SUFFIXES):
        slug += "-model"
    return "free-or-" + slug


def zcode_openrouter():
    """Chave e modelos :free do provider openrouter ja existente no ZCode."""
    data = json.loads(ZCFG.read_text(encoding="utf-8"))
    rules = [r for r in data["config"]["providerConfigRules"]["providerRules"]
             if r.get("providerName") == "openrouter"]
    if len(rules) != 1:
        raise SystemExit("esperava 1 provider 'openrouter' no ZCode, achei %d" % len(rules))
    cfg = rules[0]["config"]
    key = (cfg.get("access") or {}).get("apiKey")
    # ":free" = free model; "openrouter/free" = router of the free ones (no suffix)
    free = [m for m in cfg.get("personalModelIds", [])
            if m.endswith(":free") or m == "openrouter/free"]
    if not key:
        raise SystemExit("provider openrouter do ZCode sem apiKey")
    return key, free


def opencode_token():
    row = sqlite3.connect(str(OCDB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()
    if not row:
        raise SystemExit("credencial opencode ausente: opencode auth login opencode --method device")
    cred = json.loads(row[0])
    org = (cred.get("metadata") or {}).get("orgID") or "prj_default"
    return cred["access"], org


def proxy_models():
    req = urllib.request.Request(
        PROXY_BASE + "/models", headers={"Authorization": "Bearer " + PROXY_KEY}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8", "replace"))
    return sorted(m.get("id") for m in data.get("data", []))


def openrouter_live(model_ids):
    """Divide os ids entre os que ainda estao no catalogo publico do OpenRouter e os aposentados."""
    req = urllib.request.Request(OR_CATALOG, headers={"User-Agent": "cliproxyapi-free-aggregator"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8", "replace"))
    live = {m.get("id") for m in data.get("data", [])}
    return [m for m in model_ids if m in live], [m for m in model_ids if m not in live]


def build_block(or_key, or_free, oc_token, oc_org):
    lines = [
        START_MARK,
        "# Todos os modelos gratuitos num lugar so. O ZCode aponta para o proxy (provider",
        "# 'Gratis (todos)') e o proxy roteia por alias: free-or-* = OpenRouter, free-oc-* = OpenCode Go.",
        "api-keys:",
        "  openai-compatibility:",
        "    - name: \"openrouter-free\"",
        "      base-url: \"https://openrouter.ai/api/v1\"",
        "      request-retry: 0",
        "      disable-cooling: true",
        "      keys:",
        "        - api-key: " + yaml_str(or_key),
        "      models:",
    ]
    for model in or_free:
        lines += ["        - name: " + yaml_str(model), "          alias: " + yaml_str(or_alias(model))]
    lines += [
        "    - name: \"opencode-go\"",
        "      base-url: \"https://opencode.ai/inference/go/openai/v1\"",
        "      request-retry: 0",
        "      disable-cooling: true",
        "      headers:",
        "        User-Agent: \"opencode/latest/2.2.0/desktop\"",
        "        x-opencode-client: \"desktop\"",
        "        x-opencode-session: \"ses_cliproxyapi_gratis\"",
        "        x-opencode-project: " + yaml_str(oc_org),
        "        x-opencode-directory: \"C:/CodexProjetos/CLIProxyAPI\"",
        "      keys:",
        "        " + TOKEN_MARK,
        "        - api-key: " + yaml_str(oc_token),
        "      models:",
    ]
    for name, alias in OC_FREE:
        lines += ["        - name: " + yaml_str(name), "          alias: " + yaml_str(alias)]
    lines.append(END_MARK)
    return "\n".join(lines) + "\n"


def setup_proxy():
    or_key, or_free = zcode_openrouter()
    oc_token, oc_org = opencode_token()
    # the ZCode list keeps models OpenRouter already retired; only live ones get in
    try:
        or_free, retired = openrouter_live(or_free)
    except Exception as exc:  # noqa: BLE001
        raise SystemExit("nao consegui consultar o catalogo do OpenRouter (%s: %s); nada foi escrito"
                         % (type(exc).__name__, exc))

    lines = PROXY_CFG.read_text(encoding="utf-8").splitlines()
    # block from an earlier run of this session: from the old header to the end of the file
    for i, line in enumerate(lines):
        if line.startswith(OLD_HEADER):
            lines = lines[:i]
            break
    text = "\n".join(lines).rstrip("\n")
    if START_MARK in text and END_MARK in text:
        a = text.index(START_MARK)
        b = text.index(END_MARK) + len(END_MARK)
        text = (text[:a] + text[b:]).rstrip("\n")

    backup = PROXY_CFG.with_name("config.yaml.bak-" + datetime.date.today().strftime("%Y%m%d"))
    shutil.copy2(PROXY_CFG, backup)
    PROXY_CFG.write_text(text + "\n\n" + build_block(or_key, or_free, oc_token, oc_org), encoding="utf-8")

    aliases = [or_alias(m) for m in or_free] + [a for _, a in OC_FREE]
    print("config.yaml: bloco gratis-todos escrito | backup:", backup.name)
    print("openrouter-free: %d modelos | opencode-go: %d modelos | aliases: %d"
          % (len(or_free), len(OC_FREE), len(aliases)))
    if retired:
        print("aposentados no OpenRouter, fora do grupo: %d" % len(retired))
        for model in retired:
            print("   ", model)
    print("reinicie o proxy para carregar")


def register_zcode():
    free = [m for m in proxy_models() if m.startswith("free-")]
    if not free:
        raise SystemExit("o proxy nao expoe nenhum alias free-* (rode setup-proxy e reinicie o proxy)")

    data = json.loads(ZCFG.read_text(encoding="utf-8"))
    rules = data["config"]["providerConfigRules"]["providerRules"]
    pmr = data["config"]["modelConfigRules"]["providerModelRules"]
    existing = [r for r in rules if r.get("providerName") == ZCODE_PROVIDER]

    if existing:
        rule = existing[0]
        pid = rule["providerId"]
        before = len(rule["config"].get("personalModelIds", []))
        rule["config"]["personalModelIds"] = free
        rule["config"]["modelOrder"] = free
        action = "atualizado (%d -> %d modelos)" % (before, len(free))
    else:
        pid = str(uuid.uuid4())
        rules.append({
            "providerId": pid,
            "providerName": ZCODE_PROVIDER,
            "config": {
                "access": {"type": "api-key", "apiKey": PROXY_KEY},
                "api": {"type": "openai-responses", "baseUrl": PROXY_BASE},
                "group": "standard-personal",
                "modelOrder": list(free),
                "personalModelIds": list(free),
            },
        })
        d_order = data["config"]["providerOrder"]
        if pid not in d_order:
            d_order.insert(0, pid)
        action = "criado (%d modelos)" % len(free)

    have = {x.get("modelId") for x in pmr if x.get("providerId") == pid}
    pmr.extend({"providerId": pid, "modelId": m, "config": {"enabled": True}}
               for m in free if m not in have)

    backup = ZCFG.with_name("provider_config.json.backup-" + datetime.date.today().strftime("%Y%m%d") + "-gratis")
    shutil.copy2(ZCFG, backup)
    ZCFG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    check = json.loads(ZCFG.read_text(encoding="utf-8"))
    rule = [r for r in check["config"]["providerConfigRules"]["providerRules"]
            if r.get("providerName") == ZCODE_PROVIDER][0]
    assert rule["config"]["personalModelIds"] == free
    assert len(free) == len(set(free)), "aliases duplicados"
    assert check["config"]["providerOrder"][0] == pid
    print("ZCode provider '%s' %s | id: %s" % (ZCODE_PROVIDER, action, pid))
    print("total providers:", len(check["config"]["providerConfigRules"]["providerRules"]),
          "| backup:", backup.name)
    for m in free:
        print("  ", m)


def probe(model):
    body = json.dumps({"model": model, "input": "Responda apenas: pong", "max_output_tokens": 32}).encode("utf-8")
    req = urllib.request.Request(
        PROXY_BASE + "/responses", data=body,
        headers={"Authorization": "Bearer " + PROXY_KEY, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            resp.read()
            return "OK"
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        if exc.code == 429:
            return "429"
        if exc.code == 404 or "model_not_found" in raw:
            return "not-found"
        return "http" + str(exc.code)
    except Exception as exc:  # noqa: BLE001
        name = type(exc).__name__
        return "timeout" if "timeout" in name.lower() else "erro-" + name


def run_test():
    models = [m for m in proxy_models() if m.startswith("free-")]
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    STATUS.write_text("running", encoding="utf-8")
    VERDICT.write_text("em andamento", encoding="utf-8")
    results = []
    try:
        for model in models:
            t0 = time.time()
            status = probe(model)
            results.append({"model": model, "status": status, "dur": round(time.time() - t0, 1)})
            print("%-14s %-52s %ss" % (status, model, results[-1]["dur"]), flush=True)
        ok = sum(1 for r in results if r["status"] == "OK")
        verdict = "%d/%d OK" % (ok, len(results))
        fails = ["%s=%s" % (r["model"], r["status"]) for r in results if r["status"] != "OK"]
        if fails:
            verdict += " | falhas: " + ", ".join(fails)
    except Exception as exc:  # noqa: BLE001
        verdict = "ERRO na suite: %s: %s" % (type(exc).__name__, exc)
        print(verdict, flush=True)
    finally:
        RESULT.write_text(json.dumps(results, indent=1), encoding="utf-8")
        VERDICT.write_text(verdict, encoding="utf-8")
        STATUS.write_text("done", encoding="utf-8")
        print("\nVEREDITO: " + verdict, flush=True)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "setup-proxy":
        setup_proxy()
    elif cmd == "register-zcode":
        register_zcode()
    elif cmd == "test":
        run_test()
    elif cmd in ("status", "verdict"):
        path = STATUS if cmd == "status" else VERDICT
        print(path.read_text(encoding="utf-8").strip() if path.exists() else "ausente")
    else:
        print(__doc__)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
