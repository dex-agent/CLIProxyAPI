# -*- coding: utf-8 -*-
"""Renova o token do OpenCode Go onde ele esta gravado.

O token OAuth do OpenCode expira em ~30 dias. O OpenCode renova sozinho quando a CLI roda;
este script le o access token atual do opencode.db e espelha nos dois lugares que guardam
uma copia: os providers "OpenCode Go*" do provider_config.json do ZCode e o upstream
opencode-go do config.yaml do proxy (o provider "Gratis (todos)" passa por ele).

Uso: python -I -X utf8 .agents/scripts/refresh_opencode_go_token.py
Depois: reinicie o ZCode e o proxy (.agents/scripts/start-proxy.ps1, idempotente).
"""
import json
import pathlib
import shutil
import sqlite3
import sys

ZCFG = pathlib.Path.home().joinpath(".zcode", "v2", "provider_config.json")
OCDB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
PROXY_CFG = pathlib.Path(r"C:\CodexProjetos\CLIProxyAPI\config.yaml")
ZCODE_PROVIDERS = ("OpenCode Go", "OpenCode Go (Anthropic)", "OpenCode Go (Responses)")

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from free_aggregator import TOKEN_MARK  # noqa: E402  (uma fonte so para o marcador)


def current_token():
    row = sqlite3.connect(str(OCDB)).execute(
        "SELECT value FROM credential WHERE integration_id='opencode'"
    ).fetchone()
    if not row:
        raise SystemExit("credencial 'opencode' ausente: opencode auth login opencode --method device")
    cred = json.loads(row[0])
    if not cred.get("access"):
        raise SystemExit("sem access token na credencial")
    return cred["access"], cred.get("expires"), (cred.get("metadata") or {}).get("orgID")


def refresh_zcode(token, org):
    """Atualiza os providers OpenCode Go* do ZCode. Devolve (n_alterados, n_encontrados)."""
    data = json.loads(ZCFG.read_text(encoding="utf-8"))
    changed, found = 0, 0
    for rule in data["config"]["providerConfigRules"]["providerRules"]:
        if rule.get("providerName") not in ZCODE_PROVIDERS:
            continue
        found += 1
        cfg = rule["config"]
        differs = (cfg.get("access") or {}).get("apiKey") != token
        if org and (cfg.get("api", {}).get("headers") or {}).get("x-opencode-project") != org:
            differs = True
        if differs:
            cfg.setdefault("access", {})["apiKey"] = token
            if org:
                cfg.setdefault("api", {}).setdefault("headers", {})["x-opencode-project"] = org
            changed += 1
    if changed:
        backup = ZCFG.with_name("provider_config.json.backup-token-refresh")
        shutil.copy2(ZCFG, backup)
        ZCFG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed, found


def refresh_proxy(token):
    """Atualiza o api-key do upstream opencode-go no config.yaml do proxy. Devolve se alterou."""
    if not PROXY_CFG.exists():
        print("proxy: config.yaml ausente, pulado")
        return False
    lines = PROXY_CFG.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.strip() == TOKEN_MARK and i + 1 < len(lines) and "- api-key:" in lines[i + 1]:
            target = lines[i + 1]
            if json.dumps(token) in target:
                return False
            indent = target[: len(target) - len(target.lstrip())]
            lines[i + 1] = indent + "- api-key: " + json.dumps(token)
            shutil.copy2(PROXY_CFG, PROXY_CFG.with_name("config.yaml.bak-token-refresh"))
            PROXY_CFG.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True
    print("proxy: bloco opencode-go nao encontrado (rode free_aggregator.py setup-proxy)")
    return False


def main():
    token, expires, org = current_token()
    z_changed, z_found = refresh_zcode(token, org)
    p_changed = refresh_proxy(token)
    if not z_changed and not p_changed:
        print("NO-OP: token ja esta igual em todos os lugares | expira: %s" % expires)
        return
    print("token atualizado | expira: %s" % expires)
    print("ZCode: %d de %d providers OpenCode Go alterados" % (z_changed, z_found))
    print("proxy: %s" % ("upstream opencode-go alterado" if p_changed else "sem alteracao"))
    print("reinicie o proxy (start-proxy.ps1) e o ZCode para recarregar.")


if __name__ == "__main__":
    main()
