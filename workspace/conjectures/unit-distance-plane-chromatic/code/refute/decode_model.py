#!/usr/bin/env python3
import sys
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable
from lib.critoracle import chrom

# Independent re-decode of the TPTP model edge relation (from the model dump):
#   v1:{4,5,6,8} v2:{3,6,7,8} v3:{2,4,7,8} v4:{1,3,5,8}
#   v5:{1,4,6,7} v6:{1,2,5,7} v7:{2,3,5,6} v8:{1,2,3,4}
adj = {0:{3,4,5,7}, 1:{2,5,6,7}, 2:{1,3,6,7}, 3:{0,2,4,7},
       4:{0,3,5,6}, 5:{0,1,4,6}, 6:{1,2,4,5}, 7:{0,1,2,3}}
n=8
edges=[]
for a in range(n):
    for b in adj[a]:
        if a<b: edges.append((a,b))
deg=[0]*n
for a,b in edges: deg[a]+=1;deg[b]+=1
print("degrees:",deg)
assert all(d==4 for d in deg), "min degree must be 4"

# K4 check
def has_K4():
    A=[set() for _ in range(n)]
    for a,b in edges: A[a].add(b);A[b].add(a)
    for a in range(n):
        for b in A[a]:
            if b<=a:continue
            for c in A[a]&A[b]:
                if c<=b:continue
                for d in (A[a]&A[b]&A[c]):
                    if d>c: return (a,b,c,d)
    return None
print("K4:",has_K4())

# K2,3 check
def has_K23():
    A=[set() for _ in range(n)]
    for a,b in edges: A[a].add(b);A[b].add(a)
    for a in range(n):
        for b in range(a+1,n):
            c=len(A[a]&A[b])
            if c>=3: return (a,b,(A[a]&A[b]))
    return None
print("K2,3:",has_K23())

# neighbourhood max degree check
def nbhd_maxdeg():
    A=[set() for _ in range(n)]
    for a,b in edges: A[a].add(b);A[b].add(a)
    for v in range(n):
        nb=sorted(A[v])
        for x in nb:
            cnt=sum(1 for y in nb if y in A[x])
            if cnt>2: return (v,x,cnt)
    return None
print("nbhd maxdeg>2:",nbhd_maxdeg())

print("edges:",edges)
sat,w=is_k_colorable(edges,4,n)
print("satcolor 4-colourable:",sat,w)
print("chrom (critoracle):",chrom(n,edges))
sat3,w3=is_k_colorable(edges,3,n)
print("3-colourable:",sat3,w3)
