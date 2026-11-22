# W2 encoding census - read-only evidence (arqueologia-warmup-base)
# Per-file: BOM, high-bytes (>=0x80), CRLF/LF profile. Output: JSON receipt.
import json, sys, pathlib

root = pathlib.Path(".")
out = {"schema": "arq.w2.encoding-census.v1", "files": [], "summary": {}}
bom = high = crlf_only = lf_only = mixed = empty = 0
high_files = []
for p in root.rglob("*.go"):
    if ".git" in p.parts:
        continue
    data = p.read_bytes()
    rec = {"path": str(p).replace("\\", "/"), "size": len(data)}
    rec["bom"] = data[:3] == b"\xef\xbb\xbf"
    rec["high_bytes"] = any(b > 127 for b in data)
    crlf_n = data.count(b"\r\n")
    lf_n = data.count(b"\n") - crlf_n
    rec["crlf"] = crlf_n
    rec["lf"] = lf_n
    if len(data) == 0:
        rec["class"] = "empty"; empty += 1
    elif rec["bom"]:
        rec["class"] = "utf8-bom"; bom += 1
    elif rec["high_bytes"]:
        rec["class"] = "utf8-nonascii"; high += 1
        high_files.append(rec["path"])
    else:
        rec["class"] = "ascii"; rec.pop("high_bytes")
    if crlf_n and lf_n:
        rec["eol"] = "MIXED"
    elif crlf_n:
        rec["eol"] = "CRLF"; crlf_only += 1
    elif lf_n:
        rec["eol"] = "LF"; lf_only += 1
    else:
        rec["eol"] = "none"
    out["files"].append(rec)

out["summary"] = {"total_files": len(out["files"]), "utf8_bom": bom,
    "utf8_nonascii": high, "ascii": len(out["files"]) - bom - high - empty,
    "empty": empty, "eol_crlf": crlf_only, "eol_lf": lf_only, "eol_mixed": len([f for f in out["files"] if f.get("eol") == "MIXED"])}
out["high_bytes_paths"] = sorted(set(high_files))
pathlib.Path(".agents/receipts").mkdir(exist_ok=True)
pathlib.Path(".agents/receipts/W2-encoding-census.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out["summary"], indent=1))
print("HIGH-BYTES FILES:", out["high_bytes_paths"][:20])
