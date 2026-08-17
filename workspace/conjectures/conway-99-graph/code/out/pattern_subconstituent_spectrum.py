"""Spectrum of the second subconstituent H = induced graph on non-neighbours of 0
for both controls, computed exactly.

For an srg(99,14,1,2), fixing vertex 0, the 84 non-neighbours form the second
subconstituent H (12-regular by lambda=1: each outer vertex has k-2 = 12
neighbours outside N(0)).  Prior rounds never tooled H's spectrum.  We compute
it exactly for rook(3) (k=4, M=4) and bvls (k=22, M=220) to see whether the
subconstituent spectrum is forced / integral, and to find a pattern to test for
99.
"""
import numpy as np
import sympy as sp
from lib.srg import rook, bvls_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
    m = len(outer)
    H = np.zeros((m, m), dtype=np.int64)
    for i in range(m):
        for j in range(m):
            H[i, j] = A[outer[i], outer[j]]
    return H, m

for name, A in [("rook", rook(3)), ("bvls", bvls_graph())]:
    H, m = second_subconstituent(A)
    k_outer = int(H.sum(axis=1)[0])
    print(f"=== {name}: H srg? m={m} H degree={k_outer}")
    # characteristic polynomial
    M = sp.Matrix(H.tolist())
    cp = M.charpoly().as_expr()
    # eigenvalues as exact algebraic numbers
    polys = sp.factor(M.charpoly().as_poly())
    print("  charpoly factor:", polys)
    # integer eigenvalues
    eig = M.eigenvals()
    print("  eigenvalues (eigenvals dict):", {k2: v for k2, v in eig.items()})
    # check if H is an srg
    from collections import Counter
    lamc, muc = Counter(), Counter()
    ok_diag = True
    for i in range(m):
        for j in range(i+1, m):
            c = int((H[i] & H[j]).sum())
            if H[i, j]: lamc[c] += 1
            else: muc[c] += 1
    print("  H lambda cnt:", dict(lamc), " mu cnt:", dict(muc))
