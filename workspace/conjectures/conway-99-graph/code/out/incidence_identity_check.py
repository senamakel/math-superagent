"""Verify the exact incidence identity NN^T = (k/2)*I + A for the triangle
geometry of a lambda=1 srg(v,k,1,mu), and check rank consistency.

N[i,blk]=1 iff point i is on triangle blk.  For a partial STS whose blocks are
the triangles (3-cliques) of the graph:
  NN^T[i,i] = replication r = k/2   (triangles through point i)
  NN^T[i,j] (i~j)  = lam = 1         (triangles containing the edge ij: each
                                      common neighbour x gives {i,j,x}; i~j needed)
  NN^T[i,j] (i!~j) = 0               (non-adjacent points share no triangle)
so NN^T = r I + lam A = (k/2) I + A.   [at 99, r=7 => 7I+A; the note's special case]

Verify this exactly on all four controls, then compare rank_3(NN^T) <= rank_3(N)
(nuclear-norm-type bound) as an independent check of the rank computation.
"""
import numpy as np
from lib.srg import rook, bvls_graph, doily, gq24_graph
from incidence_p_rank import triangles_from, incidence, rank_modp

cases = [
    ("rook(3) (9,4,1,2)", rook(3), 4),
    ("doily (15,6,1,3)", doily(), 6),
    ("GQ(2,4) (27,10,1,5)", gq24_graph(), 10),
    ("BvLS (243,22,1,2)", bvls_graph(), 22),
]

for name, A, k in cases:
    n = A.shape[0]
    tris = triangles_from(A)
    N = incidence(A, tris)
    r = k // 2
    NNt = N @ N.T
    pred = r * np.eye(n, dtype=np.int64) + A
    ok = int(np.array_equal(NNt, pred))
    # rank_3 bound: rank_3(NN^T) <= rank_3(N)
    r3_N = rank_modp(N.copy(), 3)
    r3_NNt = rank_modp((NNt % 3).copy(), 3)
    r2_N = rank_modp(N.copy(), 2)
    print(f"{name}: NN^T == (k/2)I+A (k={k},r={r})? {bool(ok)}")
    print(f"   replication r = {r}  (block count {len(tris)}, row sum check "
          f"{int(np.array_equal(NNt@np.ones(n,dtype=np.int64), 3*(N@np.ones(N.shape[1],dtype=np.int64))))})")
    print(f"   rank_3(N)={r3_N}  rank_3(NN^T)={r3_NNt}  (need <= : {r3_NNt<=r3_N})")
    print(f"   rank_2(N)={r2_N}")
    print()
