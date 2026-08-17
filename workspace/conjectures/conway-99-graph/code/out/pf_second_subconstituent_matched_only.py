"""Is the kernel vector of the second subconstituent specifically a MATCHED-pair
phenomenon (uses lambda=1 -> N(0)=7K2 matching, mu=2 -> pair-labels), or do all
2-subsets give kernel vectors?

For a 2-subset S of N(0) define x^S_u = [a in P_u] - [b in P_u] for S={a,b}.
Test (H x^S)_w = 0 for every outer w:
  - matched pairs {a,a'} (a~a'), and
  - non-matched pairs {a,b} (a!~b).
Only matched pairs should vanish identically.  Exact integer arithmetic,
both mu=2 controls.
"""
import numpy as np
from lib.srg import rook, bvls_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
    m = len(outer)
    H = np.array([[A[outer[i], outer[j]] for j in range(m)] for i in range(m)], dtype=np.int64)
    return H, outer

def check(name, A, k):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N0 = [j for j in range(n) if j != 0 and A[0][j] == 1]
    H, outer = second_subconstituent(A)
    m = len(outer)
    idx = {u: i for i, u in enumerate(outer)}
    pr = {}
    for u in outer:
        pr[u] = frozenset(c for c in N0 if A[u][c] == 1)  # 2-set, mu=2
    # matched edges
    rem = set(N0); edges = []
    while rem:
        a = min(rem); rem.discard(a)
        b = [c for c in N0 if A[a][c] == 1][0]
        rem.discard(b); edges.append((a, b))
    matched = set(edges) | set(tuple(reversed(e)) for e in edges)
    def xvec(a, b):
        x = np.zeros(m, dtype=int)
        for u in outer:
            Pu = pr[u]
            x[idx[u]] = (1 if a in Pu else 0) - (1 if b in Pu else 0)
        return x
    npairs = 0; nmatchedzero = 0; nnonmatchedzero = 0; nnonmatched = 0
    bad = []
    for a in N0:
        for b in N0:
            if a >= b: continue
            npairs += 1
            x = xvec(a, b)
            hx = H @ x
            iszero = bool(np.all(hx == 0))
            if (min(a,b), max(a,b)) in matched:
                if iszero: nmatchedzero += 1
            else:
                nnonmatched += 1
                if iszero: nnonmatchedzero += 1
                else: bad.append((a,b))
    print(f"{name}: k={k}, matched pairs {len(matched)//2}, non-matched pairs {nnonmatched}")
    print(f"    matched pairs with Hx=0: {nmatchedzero}/{len(matched)//2}")
    print(f"    non-matched pairs with Hx=0: {nnonmatchedzero}/{nnonmatched}")
    print(f"    non-matched pairs that FAIL: {bad}")

check("rook(3)", rook(3), 4)
check("bvls", bvls_graph(), 22)
