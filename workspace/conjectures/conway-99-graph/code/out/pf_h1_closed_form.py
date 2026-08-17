"""Pattern-finder: is H1 of the clique complex parameter-determined?

New computation (homology_controls.py, directive-39 gate):
  dim H1(Cl(rook(3)))  =  4
  dim H1(Cl(bvls(243)))= 1540

Both are NONZERO, which is the refutation-on-arrival of any Cioaba-Mim
homology separator.  But there is a candidate CLOSED FORM worth testing:

  H1(Cl(G)) = (cycle space dim) - rank(triangle boundaries)
            = (E - V + 1) - rank(delta_2)

EVERYTHING is determined by the parameters EXCEPT
  rho := rank(delta_2) / #triangles   (does the map have full rank?).

If rho = 1 (triangle boundaries independent in edge space), then
  H1 = (vk/2 - v + 1) - vk/6 = vk/3 - v + 1.

Verify: (9,4): 9*4/3-9+1 = 4  |  (243,22): 243*22/3-243+1 = 1540.
Both match.  So the ONLY graph-content is independence of triangle boundaries.

We verify (a) the closed form predicts exactly the direct values, (b) rho=1 on
both controls (rank == T), and (c) what the closed form forces at 99 (still
nonzero => no homology obstruction, and identical to a parameter value so no
separation bootstrap).

Exact integer arithmetic.
"""
from lib.srg import rook, bvls_graph
import numpy as np
from itertools import combinations


def triangle_boundary_rank(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i, j]]
    eidx = {e: t for t, e in enumerate(edges)}
    tris = [(a, b, c) for a in range(n) for b in range(a + 1, n)
            for c in range(b + 1, n) if A[a, b] and A[a, c] and A[b, c]]
    # Gaussian elimination over Q via exact fractions on rows=edges, cols=tris
    M = [[0] * len(tris) for _ in range(len(edges))]
    for c, (a, b, d) in enumerate(tris):
        M[eidx[(a, b)]][c] = 1
        M[eidx[(b, d)]][c] = 1
        M[eidx[(a, d)]][c] = 1
    # bare fraction rank
    from fractions import Fraction
    rows = [[Fraction(x) for x in row] for row in M]
    R = len(rows); C = len(tris); rank = 0; piv_col = [0] * R
    r = 0
    for c in range(C):
        piv = None
        for i in range(r, R):
            if rows[i][c] != 0:
                piv = i; break
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(R):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r, len(edges), len(tris)


def report(name, A, v, k):
    A = np.asarray(A, dtype=np.int64)
    E = int(A.sum()) // 2
    rank, E_, T = triangle_boundary_rank(A)
    h1 = (E - v + 1) - rank
    closed = v * k // 3 - v + 1
    rho = rank / T if T else None
    print(f"=== {name} (v={v}, k={k})")
    print(f"    |E|={E}  cycle-dim={E-v+1}  T={T}  rank(delta2)={rank}  rho={rho}")
    print(f"    dim H1 (direct)        = {h1}")
    print(f"    closed form vk/3-v+1   = {closed}   MATCH: {h1==closed}")
    return h1, closed, rho


report("rook(3)", rook(3), 9, 4)
report("bvls(243)", bvls_graph(), 243, 22)

# prediction at 99 (under the closed form / independence conjecture)
v, k = 99, 14
h1_99 = v * k // 3 - v + 1
print(f"\npredicted dim H1(Cl(99)) under vk/3-v+1 (if triangle boundaries independent): {h1_99}")
print(f"  (= vk/3-v+1 = 99*14/3-99+1).  Nonzero => {h1_99} != 0,"
      f" so Cioaba's H1=0 criterion is vacuous at 99 too.")
print(f"  chi(99) = v - E + T = 99-693+231 = {99-693+231}; "
      f" beta2-beta1 = chi-1 = {99-693+231-1} -> beta1 - beta2 = {-(99-693+231-1)}")
print(f"  (if beta2=0 then beta1 = {v*k//3-v+1}, matching the closed form.)")
