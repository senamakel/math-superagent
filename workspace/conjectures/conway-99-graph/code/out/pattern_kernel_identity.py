"""Derive the kernel identity symbolically: for a matched edge {a,a'} of N(0),
x_u = [a in P_u] - [a' in P_u] satisfies (A2 x)_u = 0 identically under the
pair-adjacency rules of the mu=2 lambda=1 SRG family.

We express (A2 x)_u = sum_{w in R} A2[u,w] x_w.  Group by w.

We verify the SUM identity numerically per u on both controls: (A2 x)_u == 0.
That's the computation-backed check; the symbolic derivation is in the notes.
"""
import numpy as np
from lib.srg import rook, bvls_graph

def setup(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [j for j in range(n) if j != 0 and A[0][j] == 1]
    R = [j for j in range(n) if j != 0 and A[0][j] == 0]
    H = np.array([[A[r1, r2] for r2 in R] for r1 in R], dtype=np.int64)
    edges = []
    rem = set(N)
    while rem:
        a = min(rem); rem.discard(a)
        b = [c for c in N if A[a][c]==1][0]
        rem.discard(b)
        edges.append((a,b))
    pr = {}
    for u in R:
        pr[u] = tuple(sorted(c for c in N if A[u][c]==1))
    return H, N, R, edges, pr, A

for name, A, k in [("rook", rook(3), 4), ("bvls", bvls_graph(), 22)]:
    H, N, R, edges, pr, A = setup(A)
    idx = {u:i for i,u in enumerate(R)}
    # check per-u that (A2 x)_u = 0 for each candidate kernel vector
    all_ok = True
    for (a,ap) in edges:
        x = np.zeros(len(R), dtype=int)
        for u in R:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0)-(1 if ap in Pu else 0)
        Hx = H @ x
        if not np.all(Hx==0):
            all_ok = False
            print(f"  FAIL a={a},a'={ap}: nonzero Hx coords: {np.nonzero(Hx)[0]}")
    print(f"{name}: all {len(edges)} kernel vectors satisfy A2 x = 0 exactly: {all_ok}")
