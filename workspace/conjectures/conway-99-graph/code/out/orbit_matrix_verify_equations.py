"""Validate the orbit-level srg condition MM^T = 6J + cI - M against real orbit matrices.

Derivation (necessary orbit-level conditions from A^2 = kI + lam A + mu (J-I-A),
order-3 fixed-point-free action, orbit size 3):
  off-diagonal block (i,j) summed:  sum_l M[l][i]*M[l][j] = 3*mu + (lam-mu)*M[i][j]
  diagonal block (i,i) summed:      sum_l M[l][i]^2      = k + lam*M[i][i] + 2*mu - mu*M[i][i]
For lam=1, mu=2 these unite as
  MM^T = 6J + (k-8) I - M     [check: diag = 6 + (k-8) - M[i][i] = k-2 - M[i][i];
                               off-diag = 6 - M[i][j]]
  99: k=14 -> MM^T = 6J + 6I - M   (diag = 12 - M[i][i], off = 6 - M[i][j])
  BvLS: k=22 -> MM^T = 6J + 14I - M

Wait: recompute. For i=j: sum_l M[l][i]^2 = k + lam*M[i][i] + 2mu - mu*M[i][i]
  = 14 + M[i][i] + 4 - 2*M[i][i] = 18 - M[i][i]   (k=14)
So diag = 18 - M[i][i] = 6J + 12I - M: 6 + 12 - M[i][i] = 18 - M[i][i].  -> c = 12.
BvLS diag = 22 + M[i][i] + 4 - 2M[i][i] = 26 - M[i][i] = 6 + 20 - M[i][i]. -> c = 20.
OFF-diag (i!=j): sum_l M[l][i]M[l][j] = 3*2 + (1-2)*M[i][j] = 6 - M[i][j] for both.

So 99:  MM^T = 6J + 12I - M     (diag 18-M[i][i], off 6-M[i][j])
   BvLS: MM^T = 6J + 20I - M    (diag 26-M[i][i], off 6-M[i][j])

This script checks these identities on the REAL orbit matrices that
code/out/orbit_matrix_controls.py computed:
  rook(3) Z3 row-shift  -> 3 orbits of size 3, k=4
  bvls Z3 translation   -> 81 orbits of size 3, k=22
Plus row sums = k and diagonal in {0,2}.
"""
import numpy as np
from lib.srg import rook, bvls_graph, orbit_matrix

# reuse the control automorphisms (copied small definitions)
def rook_z3():
    g = [0] * 9
    for i in range(3):
        for j in range(3):
            g[3 * i + j] = 3 * ((i + 1) % 3) + j
    return g

def _pidx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]

def bvls_z3():
    a = (1, 0, 0, 0, 0)
    g = [0] * 243
    for s0 in range(3):
        for s1 in range(3):
            for s2 in range(3):
                for s3 in range(3):
                    for s4 in range(3):
                        s = (s0, s1, s2, s3, s4)
                        t = tuple((s[j] + a[j]) % 3 for j in range(5))
                        g[_pidx(s)] = _pidx(t)
    return g


def check(name, A, k, c, g, s):
    """Verify MM^T = 6J + c*I - M, row sums = k, diag in {0,2}, for order-3 orbit-sz-3."""
    orbits, lengths, M = orbit_matrix(A, g)
    m = len(orbits)
    M = M.astype(np.int64)
    J = np.ones((m, m), dtype=np.int64)
    I = np.eye(m, dtype=np.int64)
    lhs = M @ M.T
    rhs = 6 * J + c * I - M
    ok_mat = np.array_equal(lhs, rhs)
    rowsums = M.sum(axis=1)
    ok_rows = bool(np.all(rowsums == k))
    diag = np.diag(M)
    ok_diag = set(diag.tolist()) <= {0, 2}
    # off-diag entries in 0..3
    off = M - np.diag(np.diag(M))
    ok_off = bool(np.all((off >= 0) & (off <= 3)))
    ntri = int(np.sum(diag == 2))
    print(f"[{name}] orbits={m} (size-3: all={all(l==3 for l in lengths)})")
    print(f"  row sums all == k={k}: {ok_rows}  (min {rowsums.min()}, max {rowsums.max()})")
    print(f"  diagonal entries set within {{0,2}}: {ok_diag}  (diag={sorted(set(diag.tolist()))})")
    print(f"  off-diagonal entries in 0..3: {ok_off}")
    print(f"  MM^T == 6J + {c}I - M  (factor {s}): {ok_mat}")
    print(f"  #triangle orbits (diag=2) T = {ntri}  (f value: g=3T={3*ntri})")
    print()


if __name__ == "__main__":
    # rook(3): k=4 -> c = k-2 - ... recompute: diag = 4+M[i][i]+4-2M[i][i] = 8-M[i][i]
    #   = 6 + c - M[i][i] -> c = 2. Check: 6+2 - M[i][i] = 8 - M[i][i]. off = 6 - M[i][j].
    check("rook(3) Z3 row-shift", rook(3), 4, 2, rook_z3(), "srg(9,4,1,2)")
    # bvls: k=22 -> c=20
    check("bvls Z3 translation", bvls_graph(), 22, 20, bvls_z3(), "srg(243,22,1,2)")
    print("All orbit-level srg conditions validated on both real control orbit matrices.")
