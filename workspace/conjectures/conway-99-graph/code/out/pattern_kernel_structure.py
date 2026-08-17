"""Identify the explicit kernel structure of A2 (second subconstituent).

Hypothesis: for each matched edge {a,a'} of N(0)'s perfect matching (k/2 of them),
there is a kernel vector over GF(p).  Test candidates built from the matching.

For a matched pair {a,a'}, define x on R by x_u = [a in P_u] - [a' in P_u].
Test whether H x = 0 mod p.
Also test x_u = [a in P_u]+[a' in P_u] and other combos.
"""
import numpy as np
from lib.srg import rook, bvls_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [j for j in range(n) if j != 0 and A[0][j] == 1]
    R = [j for j in range(n) if j != 0 and A[0][j] == 0]
    H = np.array([[A[r1, r2] for r2 in R] for r1 in R], dtype=np.int64)
    return H, N, R, A

def matched_edges(A, N):
    # N(0) induces perfect matching
    edges = []
    rem = set(N)
    while rem:
        a = min(rem); rem.discard(a)
        b = [c for c in N if A[a][c]==1][0]
        rem.discard(b)
        edges.append((a,b))
    return edges

def pair_of(R, A, N):
    pr = {}
    for u in R:
        pr[u] = tuple(sorted(a for a in N if A[u][a]==1))
    return pr

for name, A, k in [("rook", rook(3), 4), ("bvls", bvls_graph(), 22)]:
    H, N, R, A = second_subconstituent(A)
    pr = pair_of(R, A, N)
    Rlist = list(R)
    idx = {u:i for i,u in enumerate(Rlist)}
    edges = matched_edges(A, N)
    print(f"=== {name}: k={k}, M={len(R)}, k/2={k//2} matched edges: {len(edges)}")
    # candidate kernel vectors: for matched {a,a'}, x_u = [a in P_u]-[a' in P_u]
    cand_ok = []
    for (a,ap) in edges:
        x = np.zeros(len(R), dtype=int)
        for u in R:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0) - (1 if ap in Pu else 0)
        Hx = H @ x
        cand_ok.append((a,ap, np.all(Hx==0)))
    print("   diff-of-matching candidates Hx=0:", cand_ok, " all:", all(c[2] for c in cand_ok))
    # sum candidate: x_u = [a in P_u]+[a' in P_u]
    candsum = []
    for (a,ap) in edges:
        x = np.zeros(len(R), dtype=int)
        for u in R:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0)+(1 if ap in Pu else 0)
        Hx = H @ x
        candsum.append((a,ap, np.all(Hx==0)))
    print("   sum-of-matching candidates Hx=0:", candsum, " all:", all(c[2] for c in candsum))
