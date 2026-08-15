#!/usr/bin/env python3
"""Extend the Moser chromatic-polynomial out-of-sample check to k=11..14.
Polynomial from interpolation: P(k)=k(k-1)(k-2)^2(k-3)(k^2-3k+4).
Count proper k-colourings exhaustively. Matches = strong verification that the
fitted degree-7 polynomial is the true chromatic polynomial.
"""
def proper_colorings(n, edges, k):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b); adj[b].append(a)
    count=0
    col=[-1]*n
    def bt(v):
        nonlocal count
        if v==n: count+=1; return
        for c in range(k):
            ok=True
            for u in adj[v]:
                if col[u]==c: ok=False; break
            if ok:
                col[v]=c; bt(v+1); col[v]=-1
    bt(0)
    return count

def poly(k):
    return k*(k-1)*(k-2)**2*(k-3)*(k*k - 3*k + 4)

moser=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
allok=True
for k in range(4,15):
    exact=proper_colorings(7,moser,k)
    pred=poly(k)
    ok=(exact==pred)
    allok=allok and ok
    print(f"k={k:2d} exact={exact:9d} poly={pred:9d} match={ok}")
print("ALL MATCH:", allok)
