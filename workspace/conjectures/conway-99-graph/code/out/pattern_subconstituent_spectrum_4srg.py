"""Test whether 'eigenvalue 0 in the second subconstituent' is parameter-determined
(family-wide across mu) or mu=2-specific.  Second subconstituent H = induced graph on
non-neighbours of vertex 0.  Compute its spectrum for all four lambda=1 SRGs in lib.srg:
rook(3) srg(9,4,1,2) mu=2, doily srg(15,6,1,3) mu=3, GQ(2,4) srg(27,10,1,5) mu=5,
bvls srg(243,22,1,2) mu=2.
"""
import numpy as np
import sympy as sp
from lib.srg import rook, bvls_graph, doily, gq24_graph

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

specs = [("rook(3) (9,4,1,2) mu=2", rook(3), "4"),
         ("doily (15,6,1,3) mu=3", doily(), "6"),
         ("GQ(2,4) (27,10,1,5) mu=5", gq24_graph(), "10"),
         ("bvls (243,22,1,2) mu=2", bvls_graph(), "22")]

for name, A, k in specs:
    H, m = second_subconstituent(A)
    deg = int(H.sum(axis=1)[0])
    M = sp.Matrix(H.tolist())
    eig = M.eigenvals()
    # multiplicities
    mm = {int(k2): int(v) for k2, v in eig.items()}
    print(f"=== {name}: m={m}, H degree={deg} (k-lam)")
    print(f"    spectrum (eigenvalue: mult): {mm}")
    # check srg-ness
    from collections import Counter
    lamc, muc = Counter(), Counter()
    for i in range(m):
        for j in range(i+1, m):
            c = int((H[i] & H[j]).sum())
            if H[i, j]: lamc[c] += 1
            else: muc[c] += 1
    is_srg = (len(lamc)==1 and len(muc)==1)
    print(f"    lambda counts: {dict(lamc)}  mu counts: {dict(muc)}  -> srg: {is_srg}")
