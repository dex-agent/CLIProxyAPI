"""Count published blobs that carry a credential from the local runtime. Prints counts only, never a value.

Usage: python -I -B -X utf8 W18-credential-membership.py <repo> <export_dir>
Exit 0 when no local credential appears in the export, 1 when at least one does.
shortcut: covers the proxy access key, the upstream api-keys of config.yaml, the OpenCode OAuth
token and the GitHub login token; extend the source list when a new credential enters the runtime.
"""
import json
import pathlib
import re
import sqlite3
import subprocess
import sys


def local_secrets(repo):
    secrets = {}
    in_access = False
    for line in (repo / "config.yaml").read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^access:\s*$", line):
            in_access = True
            continue
        if re.match(r"^\S", line):
            in_access = False
        found = re.match(r'^\s*-\s*["\']?([A-Za-z0-9_\-\.]{8,})["\']?\s*$', line) if in_access else None
        if found:
            secrets[f"proxy-access-key#{len(secrets) + 1}"] = found.group(1)
        found = re.match(r"^\s*api-key:\s*[\"']?([^\"'\s#]+)[\"']?\s*$", line)
        if found:
            secrets[f"upstream-api-key#{len(secrets) + 1}"] = found.group(1)

    db = pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"
    try:
        con = sqlite3.connect(str(db))
        for i, (value,) in enumerate(con.execute("select value from credential where integration_id='opencode'")):
            secrets[f"opencode-oauth-access#{i + 1}"] = json.loads(value)["access"]
        con.close()
    except Exception as exc:  # noqa: BLE001
        print("opencode_token_read=FAILED", type(exc).__name__)

    token = subprocess.run(["gh", "auth", "token"], capture_output=True).stdout.strip().decode("utf-8", "replace")
    if token:
        secrets["github-token"] = token
    return secrets


def main():
    repo, export = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    files = [p for p in export.iterdir() if p.is_file()]
    print(f"export={export.name} files={len(files)}")
    worst = 0
    for label, value in sorted(local_secrets(repo).items()):
        if len(value) < 8:
            continue
        hits = [p.name for p in files if value.encode() in p.read_bytes()]
        worst = max(worst, len(hits))
        print(f"{label}: len={len(value)} published_blobs={len(hits)} {hits[:3]}")
    print("credential_gate=", "RED" if worst else "GREEN", f"(max blobs per secret={worst})")
    sys.exit(1 if worst else 0)


if __name__ == "__main__":
    main()
