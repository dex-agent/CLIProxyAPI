# -*- coding: utf-8 -*-
# Interrogatorio: como o OpenBot fala com Antigravity (endpoint, headers, body)
import re, sys, pathlib

FT = pathlib.Path(r"C:\CodexProjetos\AprendizadoConsultado\temas\openbot\mentor-documental\fulltext.txt")
text = FT.read_text(encoding="utf-8", errors="replace")
lines = text.splitlines()

pats = [
    r"cloudcode", r"v1internal", r"daily-", r"antigravity.*baseUrl", r"baseUrl.*antigravity",
    r"X-Goog", r"antigravity.*headers", r"generateContent", r"streamGenerateContent",
]
seen = set()
hits = []
for i, ln in enumerate(lines, 1):
    low = ln.lower()
    if "antigravity" not in low and not any(p.lower() in low for p in ("cloudcode", "v1internal")):
        continue
    for p in pats:
        if re.search(p, ln, re.I):
            key = ln.strip()[:150]
            if key in seen:
                break
            seen.add(key)
            hits.append((i, ln.strip()[:190]))
            break

print(f"TOTAL HITS: {len(hits)}")
for i, ln in hits[:35]:
    print(f"{i}: {ln}")
