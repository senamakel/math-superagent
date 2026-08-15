#!/usr/bin/env python3
"""
Check whether the graph returned by find_counterexample on kernel_4color.p is
a GENUINE counterexample (a 5-chromatic kernel member) or a broken-encoding
artifact.

The .p file returned a 8-vertex model.  I reconstruct that graph's edge list
from the predicate_edge table in code/out/refute/code_refute_kernel_4color.p.json
and test it two independent ways:
  (1) is it genuinely a kernel member (min-deg>=4, K4-free, K2,3-free,
      nbhd-maxdeg<=2)?
  (2) is it genuinely non-4-colourable (complete SAT oracle)?

If it IS 4-colourable and a kernel member, the "refuted" verdict from
find_counterexample is a vacuous encoding artifact (has_colour is unconstrained
by the axioms, so the solver just set it all-false to break the colouring
conjunct), NOT a real counterexample.
"""
from lib.satcolor import is_k_colorable
from lib.coloring import chromatic_colorable as backtrack_colorable

# Reconstructed from predicate_edge in the model (vertices fmb_1..fmb_8 -> 0..7)
edges = []
edge_pairs = [
    (0,3),(0,4),(0,5),(0,7),
    (1,2),(1,5),(1,6),(1,7),
    (2,1),(2,3),(2,6),(2,7),
    (3,0),(3,2),(3,4),(3,7),
    (4,0),(4,3),(4,5),(4,6),
    (5,0),(5,1),(5,4),(5,6),
    (6,1),(6,2),(6,4),(6,5),
    (7,0),(7,1),(7,2),(7,3),
]
# dedupe (i,j) i<j
ed = set()
for (a,b) in edge_pairs:
    i,j = (a,b) if a<b else (b,a)
    ed.add((i,j))
edges = sorted(ed)
n = 8
print("vertex count:", n)
print("edge count:", len(edges))
print("edges:", edges)

# Kernel checks
adj = [set() for _ in range(n)]
for (i,j) in edges:
    adj[i].add(j); adj[j].add(i)

print("\n== kernel conditions ==")
mindeg_ok = all(len(adj[v])>=4 for v in range(n))
print("min-deg>=4 :", mindeg_ok, [len(adj[v]) for v in range(n)])

# K4-free
k4 = False
for a in range(n):
    for b in range(a+1,n):
        if b not in adj[a]: continue
        inter = adj[a]&adj[b]
        for c in inter:
            for d in inter:
                if c<d and d in adj[c]:
                    k4=True
print("K4-free    :", not k4)

# K2,3-free
k23 = False
for a in range(n):
    for b in range(a+1,n):
        common = len(adj[a]&adj[b])
        if common>=3: k23=True
print("K2,3-free  :", not k23)

# nbhd maxdeg<=2
nbd = True
for v in range(n):
    nb = sorted(adj[v]); pos={u:i for i,u in enumerate(nb)}
    dg=[0]*len(nb)
    for i,x in enumerate(nb):
        for j,y in enumerate(nb):
            if i<j and y in adj[x]:
                dg[i]+=1; dg[j]+=1
    if any(d>2 for d in dg): nbd=False
print("nbhd-maxdeg<=2:", nbd)

# 4-colourability: two independent complete oracles
sat, wit = is_k_colorable(edges, 4, n)
print("\nSAT oracle 4-colourable:", sat, "witness:", wit)
ok, w2 = backtrack_colorable(n, edges, 4)
print("backtrack 4-colourable:", ok, "witness:", w2)
if sat:
    bad = [e for e in edges if wit[e[0]]==wit[e[1]]]
    print("verify SAT witness proper:", not bad)
