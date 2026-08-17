"""Exact cross-check of the triangle-boundary ranks used in the homology gate.

numpy.linalg.matrix_rank uses SVD with a floating tolerance, so the ranks that
feed dim H1 (cycle_dim - rank_boundary) deserve a second, tolerance-free route.
For an integer matrix, rank over Q equals rank over R (both are the rank of the
same rational matrix), and equals rank over GF(p) whenever the GF(p) rank is
full (it can never exceed the column count). So: if the GF(p) rank equals the
number of triangles T, the Q-rank of the C2->C1 boundary map is exactly T.

This script recomputes the boundary ranks for rook(3)=L2(3) and BvLS srg(243,22,1,2)
over GF(p), p a large prime, by exact modular Gaussian elimination, and prints a
VERDICT for the gate. Statement it bears on: the homology gate capture's dim H1
values (rook 4, BvLS 1540), require rank_boundary = T = 6 and 891 respectively.
"""
import numpy as np
from lib.srg import rook, bvls_graph

P = 1000003  # large prime field for exact modular rank


def triangle_boundary(A):
    """Return (edges, triangles, sparse entries) of the C2->C1 boundary map."""
    n = len(A)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i, j]]
    edge_idx = {e: t for t, e in enumerate(edges)}
    triangles = []
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                if A[i, j] and A[i, l] and A[j, l]:
                    triangles.append((i, j, l))
    # columns = triangles, rows = edges
    M = np.zeros((len(triangles), len(edges)), dtype=np.int64)
    for c, (a, b, d) in enumerate(triangles):
        M[c, edge_idx[tuple(sorted((a, b)))]] = 1
        M[c, edge_idx[tuple(sorted((b, d)))]] = 1
        M[c, edge_idx[tuple(sorted((a, d)))]] = 1
    return M, len(edges), len(triangles)


def rank_gf(M, p):
    """Exact rank over GF(p) by modular Gaussian elimination (rows=triangles)."""
    M = M.astype(np.int64) % p
    rows, cols = M.shape
    rank = 0
    for col in range(cols):
        # find pivot at or below current rank
        piv = -1
        for r in range(rank, rows):
            if M[r, col] % p != 0:
                piv = r
                break
        if piv == -1:
            continue
        # swap pivot row into position
        if piv != rank:
            M[[rank, piv]] = M[[piv, rank]]
        inv = pow(int(M[rank, col]) % p, p - 2, p)
        # eliminate below
        below = M[rank + 1:, col].copy()
        nz = np.nonzero(below)[0]
        for rr in nz:
            rr_abs = rank + 1 + rr
            factor = int(below[rr]) * inv % p
            M[rr_abs] = (M[rr_abs] - factor * M[rank]) % p
            M[rr_abs, col] = 0  # exact zero
        rank += 1
        if rank == rows:
            break
    return rank


ok = True
for name, A in [("rook(3) = lattice L2(3)", rook(3)),
                ("BvLS srg(243,22,1,2)", bvls_graph())]:
    M, E, T = triangle_boundary(A)
    r = rank_gf(M, P)
    full = (r == T)
    ok = ok and full
    print(f"{name}: edges={E}  triangles={T}  "
          f"GF({P})-rank(boundary)={r}  full-column-rank={full}")
print()
print("RESULT:", "PASS — GF(p) rank equals #triangles on BOTH controls, so the "
      "Q-rank of the triangle-boundary map is exact (T each), and the homology-"
      "gate dim H1 values (rook 4, BvLS 1540) rest on exact integer ranks."
      if ok else "FAIL — modular rank dropped below T; investigate before use.")
