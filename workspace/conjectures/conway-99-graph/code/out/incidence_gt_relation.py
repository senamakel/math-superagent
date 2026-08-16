"""Compare rank_3(N) (incidence of triangle geometry) with rank_3(I+A) (the
graph co-adjacency mod 3), using the identity N N^T = 7I + A over GF(3) where
7 == 1 mod 3, so N N^T == I + A mod 3.

We also record rank_2(I+A) mod 2 (NN^T = 7I+A = I+A mod 2 too).
This tells whether the p-rank of the incidence code is pinned by the graph
spectrum/A, which decides whether the incidence-p-rank invariant is
parameter-determined (dead) or carries independent information (live).
"""
import numpy as np
from lib.srg import rook, bvls_graph, doily, gq24_graph
from incidence_p_rank import triangles_from, incidence, rank_modp


def rank_sym_gt3(A):
    M = (np.eye(A.shape[0], dtype=np.int64) + A) % 3
    return rank_modp(M, 3)


def rank_sym_gt2(A):
    M = (np.eye(A.shape[0], dtype=np.int64) + A) % 2
    return rank_modp(M, 2)


for name, A in [("rook(3) (9,4)", rook(3)),
                ("doily (15,6,1,3)", doily()),
                ("GQ(2,4) (27,10,1,5)", gq24_graph()),
                ("BvLS (243,22)", bvls_graph())]:
    n = A.shape[0]
    tris = triangles_from(A)
    N = incidence(A, tris)
    r3_N = rank_modp(N.copy(), 3)
    r3_IpA = rank_sym_gt3(A)
    r2_N = rank_modp(N.copy(), 2)
    r2_IpA = rank_sym_gt2(A)
    rQ = np.linalg.matrix_rank(N.astype(float))
    print(f"{name}: n={n}")
    print(f"   rank_3(N)={r3_N}  rank_3(I+A)={r3_IpA}  (v-1={n-1})")
    print(f"   rank_2(N)={r2_N}  rank_2(I+A)={r2_IpA}  (v-1={n-1})")
    print(f"   rank_Q(N)={rQ}")
    print()
