# W4 hidden surface: 3rd-party licenses, URL fragments, commented dead code (read-only)
import json, pathlib, re, collections

root = pathlib.Path(".")
# --- 3rd-party: direct requires from go.mod + license in module cache ---
gomodcache = pathlib.Path.home() / "go" / "pkg" / "mod"
requires = []
in_block = False
for line in (root / "go.mod").read_text(encoding="utf-8").splitlines():
    s = line.strip()
    if s == "require (": in_block = True; continue
    if in_block and s == ")": in_block = False; continue
    if in_block or (not in_block and s.startswith("require ")):
        parts = s.replace("require ", "").split()
        if len(parts) >= 2 and not parts[0] == "//":
            requires.append((parts[0], parts[1]))

def find_license(modpath):
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "LICENSE-MIT", "LICENSE-APACHE"):
        if (modpath / name).exists(): return name
    return None

tp = []
for mod, ver in requires:
    # module cache path: lowercase domain -> path replacement
    lp = mod.lower()
    mp = gomodcache / lp.replace("github.com/", "github.com/")
    mp = gomodcache / f"{lp}@{ver}"
    lic = None
    if mp.exists():
        lic = find_license(mp)
        if not lic:
            for sub in mp.iterdir():
                if sub.is_file() and "licen" in sub.name.lower():
                    lic = sub.name; break
    tp.append({"mod": mod, "ver": ver, "licenca": lic, "entra_no_binario": "SIM (link estatico)",
               "presente_no_repo": "go.mod/go.sum (sem vendor/)"})

# --- URL fragments (never whole domain as anchor) ---
url_re = re.compile(rb"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]{4,120}")
frag = collections.Counter()
go_files = [p for p in root.rglob("*.go") if ".git" not in p.parts]
for p in go_files:
    for m in url_re.findall(p.read_bytes()):
        s = m.decode("utf-8", "replace")
        frag[s] += 1

# --- commented-out dead code heuristic ---
dead_re = re.compile(r"^\s*//\s*(if |for |func |return |\w+ :=|\w+\.\w+\(|import |\})")
dead = collections.Counter()
for p in go_files:
    try: text = p.read_text(encoding="utf-8")
    except Exception: continue
    n = sum(1 for l in text.splitlines() if dead_re.match(l))
    if n >= 5: dead[str(p)] = n

receipt = {
    "schema": "arq.w4.hidden.v1",
    "third_party_direct": tp,
    "url_fragments_top": frag.most_common(40),
    "url_unique": len(frag),
    "dead_code_files": dead.most_common(20),
}
pathlib.Path(".agents/receipts/W4-hidden.json").write_text(json.dumps(receipt, indent=1, ensure_ascii=False))
print("deps_diretas:", len(tp), "| licenca_ausente:", len([t for t in tp if not t['licenca']]))
for t in tp:
    if not t["licenca"]: print("  SEM LICENCA:", t["mod"], t["ver"])
print("url_unicas:", len(frag), "| top6:", [u[0][:60] for u in frag.most_common(6)])
print("dead_code>=5lin:", len(dead))
for p, n in dead.most_common(8): print(f"  {n:3d} | {p}")
