"""Exact p-rank / SNF of the triangle-incidence matrix N (points x triangles)
for the lambda=1 controls, to test whether the incidence-code invariant is
parameter-determined (ranks equal across controls) or live (differ).

N[i,blk] = 1 iff point i is on triangle blk.  Built from the same triangle
enumeration used by the oracle (code/lib.triangles._triangles).

Ranks over GF(2) and GF(3) via exact Gaussian elimination on integer arrays.
SNF over Z via sympy (small cases only; 243x891 is deferred/fractional note).

Over GF(3): column weight 3 == 0 so every column lies in even-weight subspace,
rank <= v-1 = 98 at 99, 242 at 243.  We report rank and rank-deficiency.
"""
import numpy as np
from fractions import Fraction


def triangles_from(A):
    """Return list of frozenset triangles (3-cliques) exactly from 0/1 int adj."""
    n = A.shape[0]
    tris = []
    for a in range(n):
        adj_a = np.flatnonzero(A[a])
        for i in range(len(adj_a)):
            b = adj_a[i]
            if b <= a:
                continue
            nbs = np.flatnonzero(A[b])
            cvals = np.intersect1d(adj_a[i:], nbs)
            for c in cvals:
                if A[b, c] and A[a, c]:
                    tris.append(frozenset((int(a), int(b), int(c))))
    return tris


def incidence(A, tris):
    n = A.shape[0]
    N = np.zeros((n, len(tris)), dtype=np.int64)
    for j, tr in enumerate(tris):
        for p in tr:
            N[p, j] = 1
    return N


def rank_modp(M, p):
    """Exact rank over GF(p) by Gaussian elimination, integer arithmetic only."""
    M = M % p
    H, W = M.shape
    r = 0
    for col in range(W):
        piv = -1
        for row in range(r, H):
            if M[row, col] % p != 0:
                piv = row
                break
        if piv == -1:
            continue
        M[[r, piv]] = M[[piv, r]]
        pivrow = M[r].astype(object).copy()
        inv = pow(int(pivrow[col] % p), p - 2, p)  # Fermat inverse in GF(p)
        pivrow = (pivrow * inv) % p
        M[r] = pivrow
        for row in range(H):
            if row != r and M[row, col] % p != 0:
                fac = M[row, col] % p
                M[row] = (M[row] - fac * pivrow) % p
        r += 1
    return r


def run(A, name):
    tris = triangles_from(A)
    N = incidence(A, tris)
    n, b = N.shape
    r2 = rank_modp(N.copy(), 2)
    r3 = rank_modp(N.copy(), 3)
    rQ = np.linalg.matrix_rank(N.astype(float))  # rational/generic rank
    print(f"{name}: n={n} blocks={b}")
    print(f"  rank_2(N) = {r2}   (rank deficiency vs n: {n - r2})")
    print(f"  rank_3(N) = {r3}   (rank deficiency vs n-1: {(n-1) - r3})")
    print(f"  rational rank = {rQ} (should equal rank over Q of 0/1 matrix)")
    # column-weight check over GF(3): each column weight 3 => 0 mod 3
    return r2, r3, n, b


from lib.srg import rook, bvls_graph
from lib.srg import doily, gq24_graph

print("=== rook(3) = srg(9,4,1,2) ===")
A9 = rook(3)
run(A9, "rook(3)")

print()
print("=== doily = srg(15,6,1,3) ===")
A15 = doily()
run(A15, "doily")

print()
print("=== GQ(2,4) = srg(27,10,1,5) ===")
A27 = gq24_graph()
run(A27, "GQ(2,4)")

print()
print("=== BvLS = srg(243,22,1,2) ===")
A243 = bvls_graph()
run(A243, "BvLS")
