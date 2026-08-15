#!/usr/bin/env python3
import sys
sys.path.insert(0, "/workspace/code")
from lib.unitfield import moser_spindle_points, minkowski_sum, unit_graph

M=moser_spindle_points()
S=minkowski_sum(M,M)
edges,n=unit_graph(S)
pts_n=len(S)
adj=[set() for _ in range(pts_n)]
for a,b in edges: adj[a].add(b); adj[b].add(a)
print("Moser+Moser points=",pts_n,"edges=",n)

import sys
sys.setrecursionlimit(100000)
best=[0]
def rec(cand, size):
    if size>best[0]: best[0]=size
    if not cand: return
    v=max(cand, key=lambda x: len(adj[x]))
    rec(cand - adj[v] - {v}, size+1)
    rec(cand - {v}, size)
rec(set(range(pts_n)),0)
print("alpha =",best[0])
print("n/alpha =", float(pts_n/best[0]), "(lower bound on chi_f; must be <=4)")
print("=> needed alpha >= ceil(n/4) =", (pts_n+3)//4)
