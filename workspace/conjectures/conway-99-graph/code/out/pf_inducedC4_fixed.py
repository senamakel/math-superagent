"""Exact induced-C4 count on all four lambda=1 members, O(n^2 * mu^2)
using the anchored method (each induced C4 counted once per nonedge then /2).
"""
from lib.srg import rook, doily, gq24_graph, bvls_graph, is_srg

def compute(A):
    n = len(A)
    N = [set(j for j in range(n) if A[i][j]) for i in range(n)]
    nonedges = 0
    ic4 = 0   # sum over nonedges of C(mu,2)  (later /2)
    for u in range(n):
        for v in range(u+1, n):
            if A[u][v]:
                continue
            nonedges += 1
            cn = N[u] & N[v]
            mu = len(cn)
            # among common neighbours, no two are adjacent (c7) => all pairs C(mu,2)
            ic4 += mu*(mu-1)//2
    return nonedges, ic4//2

for name, A, (v,k,l,m) in [
        ("rook", rook(3), (9,4,1,2)), ("doily", doily(), (15,6,1,3)),
        ("GQ24", gq24_graph(), (27,10,1,5)), ("BvLS", bvls_graph(), (243,22,1,2)),
]:
    assert is_srg(A, v, k, l, m), name
    ne, ic4 = compute(A)
    halfpred = m*(m-1)//2 * ne // 2
    print(f"{name:>6}: v={v:>4} k={k:>3} mu={m} nonedges={ne:>8} inducedC4={ic4:>9}  (1/2)C(mu,2)*ne={halfpred:>9}  match={ic4==halfpred}")
