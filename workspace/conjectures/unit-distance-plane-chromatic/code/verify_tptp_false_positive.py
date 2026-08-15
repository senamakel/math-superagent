"""Independent re-verification of the kernel-4color TPTP false-positive claim.

The note claims: the 8-vertex model graph decoded from the TPTP model is a
member of C_8 (min-deg 4, K4-free, K2,3-free, every neighbourhood max-deg<=2)
AND is 4-colourable with witness [0=C,1=D,2=A,3=D,4=A,5=B,6=C,7=B].

Edges (from the note):
0-3,0-4,0-5,0-7, 1-2,1-5,1-6,1-7, 2-3,2-6,2-7, 3-4,3-7, 4-5,4-6, 5-6
"""
import itertools
from collections import defaultdict

n = 8
edges = [(0,3),(0,4),(0,5),(0,7),(1,2),(1,5),(1,6),(1,7),(2,3),(2,6),(2,7),
         (3,4),(3,7),(4,5),(4,6),(5,6)]

adj = defaultdict(set)
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)

# (a) min degree
deg = [len(adj[i]) for i in range(n)]
print("degrees:", deg, "min:", min(deg), "all==4:", all(d == 4 for d in deg))

# (b) K4-free: no 4-clique. Use brute over combos (n small).
k4 = any(all((a,b) in set(map(tuple,edges)) or (b,a) in map(tuple,edges) for a,b in itertools.combinations(c,2)) for c in itertools.combinations(range(n),4))
# simpler: build clean adjacency
adjset = set()
for u,v in edges:
    adjset.add((u,v)); adjset.add((v,u))
k4 = any(all((a,b) in adjset for a,b in itertools.combinations(c,2)) for c in itertools.combinations(range(n),4))
print("has K4:", k4)

# (c) K2,3-free: every pair of vertices has <=2 common neighbours
maxcommon = 0
bad = []
for a,b in itertools.combinations(range(n),2):
    c = len(adj[a]&adj[b])
    maxcommon = max(maxcommon, c)
    if c >= 3: bad.append((a,b,c))
print("max common neighbours:", maxcommon, "pairs w/ >=3:", bad)

# (d) every neighbourhood induces max degree <= 2
maxnbdeg = 0
for v in range(n):
    nb = list(adj[v])
    inner = 0
    for i in range(len(nb)):
        for j in range(i+1,len(nb)):
            if (nb[i],nb[j]) in adjset: inner += 1
    maxnbdeg = max(maxnbdeg, inner)
print("max inner-degree over all neighbourhoods:", maxnbdeg)

# 4-colourability: exhaustive over 4^8 colourings (65536) with the witness check.
witness = {'C':0,'D':1,'A':2,'B':3}
wcol = [witness['C'],witness['D'],witness['A'],witness['D'],witness['A'],witness['B'],witness['C'],witness['B']]
proper = all(wcol[u]!=wcol[v] for u,v in edges)
print("witness proper 4-colouring:", proper, wcol)
# count all proper 4-colourings
from itertools import product
cnt = 0
first = None
for c in product(range(4), repeat=n):
    if all(c[u]!=c[v] for u,v in edges):
        cnt += 1
        if first is None: first = c
print("total proper 4-colourings:", cnt, "first:", first)
# 3-colourability
cnt3 = 0
for c in product(range(3), repeat=n):
    if all(c[u]!=c[v] for u,v in edges):
        cnt3 += 1
print("proper 3-colourings:", cnt3)
