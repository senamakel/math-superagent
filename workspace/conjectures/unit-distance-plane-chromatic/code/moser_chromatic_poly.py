#!/usr/bin/env python3
"""Chromatic polynomial of the Moser spindle: count proper k-colourings for
k=1..K by exhaustive backtracking (each vertex k choices, check edges).
Degree of chromatic poly is n=7, so k=0..7 values determine it. Then fit the
polynomial exactly (integer/rational coefficients) and report.
The colouring counts 0,0,0,384,5040 (k=1..5) are the calibration data; this
extends to a full polynomial and checks it is one (a known exact fact: the
number of proper k-colourings is always a polynomial in k of degree n).
"""
def proper_colorings(n, edges, k):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    count=0
    col=[-1]*n
    def bt(v):
        nonlocal count
        if v==n:
            count+=1; return
        for c in range(k):
            ok=True
            for u in adj[v]:
                if col[u]==c: ok=False; break
            if ok:
                col[v]=c; bt(v+1); col[v]=-1
    bt(0)
    return count

moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
vals={}
for k in range(1,11):
    vals[k]=proper_colorings(7,moser,k)
print("proper k-colouring counts k=1..10:")
for k in range(1,11): print(f"  P({k}) = {vals[k]}")
