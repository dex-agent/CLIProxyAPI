"""Export every blob introduced by a commit range and run the house personal-data scanner on it.

Read-only on the repository. The report is masked; the gate decision belongs to the session.
Usage: python -I -X utf8 W18-export-new-blobs-scan.py <repo> <base>..<head> [<backup_dir>]
shortcut: triage is printed, not decided; upgrade to a push gate only if it must block a push.
"""
import collections
import json
import os
import pathlib
import re
import subprocess
import sys
import time

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
LONG = re.compile(r"[A-Za-z0-9_\-]{24,}")
IV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PLUS = re.compile(r"\+\d{8,15}\b")
SCAN = pathlib.Path.home() / ".agents/skills/dex-sanitizar-dados-pessoais/scripts/sanitizar-scan.py"


def git(repo, *args, data=None):
    return subprocess.run(["git", "-C", repo, *args], input=data, capture_output=True, check=True).stdout


def kind(value):
    return "module-path" if re.search(r"@v\d|\.json$|\.windows-amd64$", value) else "mail-like"


def masked(value):
    local, domain = value.rsplit("@", 1)
    return f"{local[:1]}***@***.{domain.rsplit('.', 1)[-1]}(len={len(value)})"


def mask_line(line):
    return LONG.sub("<LONG>", EMAIL.sub("<EMAILLIKE>", line.strip()))[:150]


def main():
    repo, rng = sys.argv[1], sys.argv[2]
    backup = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else None
    base, head = rng.split("..")
    out_dir = pathlib.Path(os.environ["TEMP"]) / ("pub-scan-" + time.strftime("%H%M%S"))
    out_dir.mkdir()

    lines = git(repo, "rev-list", "--objects", rng).splitlines()
    ids = [line.split(b" ", 1)[0] for line in lines]
    names = {i.decode(): line.split(b" ", 1)[1].decode("utf-8", "replace")
             for i, line in ((line.split(b" ", 1)[0], line) for line in lines if b" " in line)}
    feed = b"\n".join(ids) + b"\n"
    types = git(repo, "cat-file", "--batch-check=%(objecttype)", data=feed).split()
    raw = git(repo, "cat-file", "--batch", data=feed)
    pos = 0
    blobs = {}
    for oid, typ in zip(ids, types):
        nl = raw.index(b"\n", pos)
        parts = raw[pos:nl].split()
        pos = nl + 1
        if len(parts) != 3:
            continue  # "<sha> missing": no content follows
        size = int(parts[2])
        if typ == b"blob":
            blobs[oid.decode()] = raw[pos:pos + size]
        pos += size + 1  # every typed object is followed by its content and one newline

    head_blob = {}
    for entry in git(repo, "ls-tree", "-r", "-z", head).split(b"\0"):
        if entry:
            meta, path = entry.split(b"\t", 1)
            head_blob[path.decode("utf-8", "replace")] = meta.split()[2].decode()
    changed = [p.decode("utf-8", "replace")
               for p in git(repo, "diff", "--name-only", "--diff-filter=ACMR", "-z", rng).split(b"\0") if p]
    uncovered = [p for p in changed if head_blob.get(p) not in blobs]

    print(f"objects={len(ids)} blobs_expected={types.count(b'blob')} blobs_read={len(blobs)} "
          f"distinct_paths={len(set(names[o] for o in blobs))}")
    print(f"head_changed_files={len(changed)} head_files_not_covered={len(uncovered)} {uncovered[:5]}")
    if types.count(b"blob") != len(blobs) or uncovered or pos != len(raw):
        print("INVALID: export is incomplete or misaligned; the scan below must not be trusted")
        sys.exit(2)

    files = []
    for i, (oid, content) in enumerate(sorted(blobs.items(), key=lambda kv: names[kv[0]])):
        name = f"{i:03d}__" + os.path.basename(names[oid])
        (out_dir / name).write_bytes(content)
        files.append((str(out_dir / name), names[oid]))

    res = subprocess.run([sys.executable, "-I", "-X", "utf8", str(SCAN), "--root", str(out_dir), "--all", "--json"],
                         capture_output=True)
    if res.returncode not in (0, 1) or not res.stdout:
        print("INVALID: scanner did not produce a report:", res.stderr.decode("utf-8", "replace")[:600])
        sys.exit(3)
    findings = json.loads(res.stdout.decode("utf-8"))["findings"]
    path_of = dict(files)
    text = {full: pathlib.Path(full).read_text(encoding="utf-8", errors="replace").split("\n") for full, _ in files}
    joined = {full: "\n".join(txt) for full, txt in text.items()}

    print(f"scan_exit={res.returncode} findings={len(findings)} by_category="
          f"{dict(collections.Counter(f['categoria'] for f in findings))}")

    mail_like = set()
    print("--- email values (masked) x repo paths")
    seen = set()
    for f in findings:
        if f["categoria"] != "email":
            continue
        for value in EMAIL.findall(text[f["arquivo"]][f["linha"] - 1]):
            key = (kind(value), masked(value))
            if key not in seen:
                seen.add(key)
                print(key, sorted({path_of[full] for full in joined if value in joined[full]})[:4])
            if key[0] == "mail-like":
                mail_like.add(value)
    print(f"mail_like_count={len(mail_like)}")

    if backup:
        bk_files = [p for p in backup.rglob("*") if p.is_file()]
        candidates = collections.defaultdict(set)
        for p in bk_files:
            try:
                data = p.read_bytes()
            except OSError:
                continue
            for value in {m.group(0) for m in EMAIL.finditer(data.decode("utf-8", "replace"))}:
                if kind(value) == "mail-like":
                    candidates[value].add(p.name)
        print(f"--- mail-like values in the old receipts backup: {len(candidates)}")
        for value, names_ in sorted(candidates.items(), key=lambda kv: -len(kv[1])):
            published = sorted({path_of[full] for full in joined if value in joined[full]})
            print(masked(value), "backup_files=", len(names_), "published_paths=", published[:4])
            for p in bk_files:
                if p.name in names_:
                    for line in p.read_text(encoding="utf-8", errors="replace").split("\n"):
                        if value in line:
                            print("   ctx:", mask_line(line.replace(value, "<EMAIL>")))
                            break
                    break

    print("--- credencial / path / url / mojibake / read-error lines")
    shown = 0
    for f in findings:
        if f["categoria"] in ("credencial", "path-pessoal", "userprofile-hardcode", "url-pessoal", "mojibake", "erro-leitura"):
            print(f"[{f['categoria']}] {path_of[f['arquivo']]}:{f['linha']} | {mask_line(text[f['arquivo']][f['linha'] - 1])}")
            shown += 1
            if shown >= 60:
                print("   ... capped")
                break

    print("--- pii-estruturado: distinct values x count")
    values = collections.Counter()
    for f in findings:
        if f["categoria"] == "pii-estruturado":
            line = text[f["arquivo"]][f["linha"] - 1]
            for m in list(IV4.finditer(line)) + list(PLUS.finditer(line)):
                values[m.group(0)] += 1
    print(f"distinct={len(values)} top={values.most_common(12)}")
    print("export_dir=", out_dir)


if __name__ == "__main__":
    main()
