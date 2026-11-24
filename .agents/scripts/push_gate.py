"""Pre-push gate of this repository: the house range gate plus this machine's secret sources.

The generic core lives in the dex-sanitizar-dados-pessoais skill (range_gate.py);
this file only declares where the local secrets are. The core loads this file
through --values-from and calls secret_values().

Usage: python -I -B -X utf8 push_gate.py <repo> <base>..<head> [--triage]
Default mode checks secret values only (fast; this is what the pre-push hook
runs). --triage also lists the personal-data findings of the range, masked.
Exit codes are the core's: 0 clean, 1 secret value found, 2 export invalid,
3 scanner failed, 5 no secret source, 64 usage. A secret value is never printed.
"""
import argparse
import json
import os
import pathlib
import re
import sqlite3
import subprocess
import sys

CORE = pathlib.Path.home() / ".agents" / "skills" / "dex-sanitizar-dados-pessoais" / "scripts" / "range_gate.py"
REPO = pathlib.Path(__file__).resolve().parents[2]
OPENCODE_DB = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"


def proxy_secrets(text):
    """Access keys and upstream api-keys of the proxy config, in block or list-item form."""
    secrets = {}
    in_access = False
    for line in text.splitlines():
        if re.match(r"^access:\s*$", line):
            in_access = True
            continue
        if re.match(r"^\S", line):
            in_access = False
        found = re.match(r'^\s*-\s*["\']?([A-Za-z0-9_\-\.]{8,})["\']?\s*$', line) if in_access else None
        if found:
            secrets[f"proxy-access-key#{len(secrets) + 1}"] = found.group(1)
        # Upstream keys arrive as list items ("- api-key: ...") under keys:
        found = re.match(r"^\s*(?:-\s*)?api-key:\s*[\"']?([^\"'\s#]+)[\"']?\s*$", line)
        if found:
            secrets[f"upstream-api-key#{len(secrets) + 1}"] = found.group(1)
    return secrets


def opencode_token():
    """OAuth access token the OpenCode CLI stores locally; empty when the store does not exist."""
    if not OPENCODE_DB.is_file():
        return ""
    # Read-only URI: a live OpenCode must not see this gate as a writer.
    con = sqlite3.connect(OPENCODE_DB.as_uri() + "?mode=ro", uri=True)
    try:
        rows = con.execute("select value from credential where integration_id='opencode'").fetchall()
    finally:
        con.close()
    for (value,) in rows:
        access = json.loads(value).get("access")
        if access:
            return access
    return ""


def secret_values():
    """Secret values of this machine's runtime, read at call time; nothing is hard-coded here."""
    # A clone without the local proxy config has no proxy key to check.
    config = REPO / "config.yaml"
    values = proxy_secrets(config.read_text(encoding="utf-8", errors="replace")) if config.is_file() else {}
    values["opencode-oauth-access"] = opencode_token()
    return values


def main():
    parser = argparse.ArgumentParser(description="Pre-push gate of this repository (house range gate + local secret sources)")
    parser.add_argument("repo")
    parser.add_argument("range")
    parser.add_argument("--triage", action="store_true",
                        help="also list the personal-data findings of the range (masked)")
    args = parser.parse_args()
    if not CORE.is_file():
        print("push gate: core range_gate.py not found in the dex-sanitizar-dados-pessoais skill", file=sys.stderr)
        return 3
    cmd = [sys.executable, "-I", "-B", "-X", "utf8", str(CORE), args.repo, args.range,
           "--values-from", str(pathlib.Path(__file__).resolve()), "--gh-token"]
    # Extra values for tests and one-off checks: comma-separated environment variable names.
    for name in os.environ.get("PUSH_GATE_EXTRA_ENV", "").split(","):
        if name.strip():
            cmd += ["--env", name.strip()]
    if not args.triage:
        cmd.append("--secrets-only")
    return subprocess.run(cmd).returncode


if __name__ == "__main__":
    sys.exit(main())
