# W3 internal dependency graph - Tarjan SCC + fan-in hubs (read-only)
import json, pathlib, collections

MOD = "github.com/router-for-me/CLIProxyAPI/v8"
adj = {}
for line in pathlib.Path(".agents/receipts/W3-imports-adj.txt").read_text(encoding="utf-8").splitlines():
    parts = line.split("\t")
    if not parts or not parts[0] or " " not in parts[0]:
        continue
    pkg, first_import = parts[0].split(" ", 1)
    imports = [first_import] + parts[1:]
    imports = [i for i in imports if i and i.startswith(MOD)]
    adj[pkg] = imports  # raw; filter after all names known

names = set(adj)
adj = {p: [i for i in imports if i in names]
       for p, imports in adj.items()}
short = lambda p: p.replace(MOD, "")

names = set(adj)
# Tarjan SCC (iterative)
index, low, on_stack, stack, sccs, counter = {}, {}, set(), [], [], [0]
for start in names:
    if start in index: continue
    work = [(start, iter(adj[start]))]
    index[start] = low[start] = counter[0]; counter[0] += 1
    stack.append(start); on_stack.add(start)
    while work:
        node, it = work[-1]
        advanced = False
        for nxt in it:
            if nxt not in index:
                index[nxt] = low[nxt] = counter[0]; counter[0] += 1
                stack.append(nxt); on_stack.add(nxt)
                work.append((nxt, iter(adj[nxt])))
                advanced = True
                break
            elif nxt in on_stack:
                low[node] = min(low[node], index[nxt])
        if advanced: continue
        work.pop()
        if work:
            low[work[-1][0]] = min(low[work[-1][0]], low[node])
        if low[node] == index[node]:
            scc = []
            while True:
                w = stack.pop(); on_stack.discard(w); scc.append(w)
                if w == node: break
            if len(scc) > 1: sccs.append(sorted(scc))

fan_in = collections.Counter()
fan_out = {p: len(v) for p, v in adj.items()}
for p, imports in adj.items():
    for i in imports: fan_in[i] += 1

edge_count = sum(len(v) for v in adj.values())
receipt = {
    "schema": "arq.w3.internal-graph.v1",
    "module": MOD,
    "packages_internal": len(names),
    "edges_internal": edge_count,
    "cycles_scc_gt1": [sorted(s) for s in sccs],
    "fan_in_top10": fan_in.most_common(10),
    "fan_out_top10": sorted(fan_out.items(), key=lambda x: -x[1])[:10],
}
pathlib.Path(".agents/receipts/W3-graph.json").write_text(json.dumps(receipt, indent=1))
print("pkgs_internos:", len(names), "| arestas:", edge_count, "| ciclos(SCC>1):", len(sccs))
for s in sccs: print("  ciclo:", s)
print("TOP-10 FAN-IN (quem mais é importado):")
for p, n in fan_in.most_common(10): print(f"  {n:3d} <- {p}")
print("TOP-10 FAN-OUT (quem mais importa):")
for p, n in sorted(fan_out.items(), key=lambda x: -x[1])[:10]: print(f"  {n:3d} -> {p}")
