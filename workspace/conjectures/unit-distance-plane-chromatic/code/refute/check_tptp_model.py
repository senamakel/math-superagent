#!/usr/bin/env python3
"""Check the TPTP counterexample model against the ORIGINAL statement."""
import sys
sys.path.insert(0, "/workspace/code")
from census_kernel import check_kernel
from lib.satcolor import is_k_colorable
from lib.critoracle import chrom

# Edge relation decoded from the 8-vertex TPTP model (1-indexed -> 0-indexed).
adj = {0:{3,4,5,7}, 1:{2,5,6,7}, 2:{1,3,6,7}, 3:{0,2,4,7},
       4:{0,3,5,6}, 5:{0,1,4,6}, 6:{1,2,4,5}, 7:{0,1,2,3}}
n=8
edges=[]
for a in range(n):
    for b in adj[a]:
        if a<b: edges.append((a,b))

deg=[0]*n
for a,b in edges: deg[a]+=1;deg[b]+=1
print("degrees:",deg,"min:",min(deg))

ok, reason = check_kernel(n, edges)
print("run's check_kernel:", ok, reason)

# independent K4
A=[set(adj[v]) for v in range(n)]
def has_K4():
    for a in range(n):
        for b in A[a]:
            if b<=a: continue
            for c in A[a]&A[b]:
                if c<=b: continue
                for d in A[a]&A[b]&A[c]:
                    if d>c: return (a,b,c,d)
    return None
print("K4:",has_K4())

# independent K2,3
def has_K23():
    for a in range(n):
        for b in range(a+1,n):
            if len(A[a]&A[b])>=3: return (a,b,A[a]&A[b])
    return None
print("K2,3:",has_K23())

# neighbourhood max-degree
def nbhd_maxdeg():
    for v in range(n):
        nb=sorted(A[v])
        for x in nb:
            if sum(1 for y in nb if y in A[x])>2: return (v,x)
    return None
print("nbhd maxdeg>2:",nbhd_maxdeg())

sat,w=is_k_colorable(edges,4,n)
print("satcolor 4-colourable:",sat,w)
print("chrom:",chrom(n,edges))
sat3,w3=is_k_colorable(edges,3,n)
print("3-colourable:",sat3,w3)
