"""Verify the conjecture: for srg(v,k,1,2), the second subconstituent A2
(induced on non-neighbours of vertex 0) has eigenvalue 0 with multiplicity k/2.

Direct numerical verification of nullity(A2) = k/2, and extraction of a basis
of the kernel to expose the mechanism.
"""
import numpy as np
import sympy as sp
from lib.srg import rook, bvls_graph, doily, gq24_graph

def second_subconstituent(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    outer = [j for j in range(n) if j != 0 and A[0][j] == 0]
    H = np.array([[A[outer[i], outer[j]] for j in range(len(outer))] for i in range(len(outer))], dtype=np.int64)
    return H, outer

for name, A, k in [("rook(3) 9,4,1,2 mu=2", rook(3), 4),
                   ("bvls 243,22,1,2 mu=2", bvls_graph(), 22),
                   ("doily 15,6,1,3 mu=3", doily(), 6),
                   ("GQ(2,4) 27,10,1,5 mu=5", gq24_graph(), 10)]:
    H, outer = second_subconstituent(A)
    m = len(outer)
    M = sp.Matrix(H.tolist())
    nullity = M.nullspace()
    print(f"{name}: m={m}, nullity(A2) = {len(nullity)}   k/2={k/2}  match={len(nullity)==k//2}")
    if len(nullity) <= 3:
        print("   kernel basis vecs (sparse, first 12 coords):")
        for v in nullity[:3]:
            print("   ", [int(x) for x in v])
