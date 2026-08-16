"""Exact canonical oracle for strong regularity, and the control graphs.

One canonical oracle for the whole run. Everything that decides "is this
srg(v,k,lambda,mu)" calls is_srg from here. No second implementation and no
script decides it inline. Exact integer common-neighbour counting off the
adjacency matrix (0/1, dtype int). Eigenvalues / spectra are used only to
*suggest*; they never decide.

VERIFIED: rook(3) is srg(9,4,1,2), bvls_graph() is srg(243,22,1,2) with 2673
edges, doily() is srg(15,6,1,3), gq24_graph() is srg(27,10,1,5),
random_regular_14_99 (a circulant conn {1..7} on 99) is 14-regular but NOT
srg(99,14,1,2), and is_srg rejects the Petersen graph (shape) and an
edge-switched rook(3) against (9,4,1,2). Negative controls *exercise the
lambda/mu counting path*: C9(1,2)=circulant(9,{1,2}) and circulant(99,{1..7})
both pass shape+degree and fail ONLY on the common-neighbour count, and the
rejection string names LAMBDA vs MU. All rechecked in
code/out/oracle-controls.captured.txt. The BvLS construction uses the
corrected _TERNARY_GOLAY_H (see the note there).

Exposed here, once verified:
  - rook(3)       -> 3x3 rook's graph, srg(9,4,1,2)  (positive control)
  - doily()       -> doily, srg(15,6,1,3) (GQ(2,2) collinearity graph = Kneser K(6,2))
  - gq24_graph()  -> GQ(2,4) collinearity graph, srg(27,10,1,5) (O^-(6,2) polar space)
  - bvls_graph()  -> 243-vertex BvLS graph, srg(243,22,1,2) (positive control)
  - random_regular_14_99() -> a random 14-regular graph on 99 vertices (negative control)
  - circulant(n, conn) -> circulant graph; used to build negatives that match
    shape+degree but fail the count path (C9(1,2), 99-graph above)
Any nonexistence argument in this workspace must be run against rook(3) and
bvls_graph() through this module; GOAL.md makes that an admissibility test.
"""
import itertools
import numpy as np


def is_srg(A, v, k, lam, mu):
    """Exact combinatorial check that the 0/1 integer matrix A is srg(v,k,lambda,mu).

    Uses only integer common-neighbour counts over the adjacency matrix
    (A @ A). No floating point. Returns (bool, detail_string).
    """
    A = np.asarray(A, dtype=np.int64)
    if A.shape != (v, v):
        return False, f"shape {A.shape} != ({v},{v})"
    if not np.array_equal(A, A.T):
        return False, "not symmetric"
    if np.any(np.diag(A) != 0):
        return False, "nonzero diagonal"
    if set(np.unique(A)) - {0, 1}:
        return False, "not a 0/1 matrix"

    # regularity: each row sums to k
    d = A.sum(axis=1)
    if not np.all(d == k):
        bad = int(np.sum(d != k))
        return False, f"{bad} rows have degree != {k}"

    A2 = A @ A  # exact integer: A2[i,j] = number of common neighbours of i,j
    I = np.eye(v, dtype=np.int64)
    adj = A.astype(bool)                # off-diagonal adjacent pairs
    off = ~I.astype(bool)               # off-diagonal mask (diag = degree, already checked)
    # Adjacent pairs must share exactly lam common neighbours; non-adjacent
    # distinct pairs exactly mu. Count each failure class separately so a
    # negative control proves WHICH counting path failed.
    la_err = int(np.count_nonzero((A2 != lam) & adj & off))
    mu_err = int(np.count_nonzero((A2 != mu) & (~adj) & off))
    if la_err == 0 and mu_err == 0:
        return True, "srg(v,k,lambda,mu) confirmed by exact common-neighbour counts"
    if la_err and mu_err:
        return False, (f"common-neighbour mismatch: LAMBDA wrong on {la_err} adjacent "
                       f"pairs (need {lam}), MU wrong on {mu_err} non-adjacent pairs (need {mu})")
    if la_err:
        return False, (f"LAMBDA mismatch: {la_err} adjacent pairs have "
                       f"common-neighbour count != {lam}")
    return False, (f"MU mismatch: {mu_err} non-adjacent pairs have "
                   f"common-neighbour count != {mu}")


# ---------------------------------------------------------------------------
# Control graphs

def circulant(n, conn):
    """Circulant graph on n vertices with connection offsets in ``conn``.

    Vertex i is adjacent to (i +/- s) mod n for each s in conn. Returns the
    adjacency matrix. Degree = 2*len(conn) (all offsets distinct and < n/2).
    Used for negative controls whose shape and degree match an srg but whose
    common-neighbour counts do not.
    """
    A = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for s in conn:
            A[i, (i + s) % n] = 1
            A[i, (i - s) % n] = 1
    np.fill_diagonal(A, 0)
    return A


def rook(n):
    """The n x n rook's graph (line graph of K_{n,n}). For n=3 it is srg(9,4,1,2)."""
    # vertices = cells (i,j) of an n x n grid; adjacent iff same row or same column.
    cells = list(itertools.product(range(n), range(n)))
    idx = {c: t for t, c in enumerate(cells)}
    A = np.zeros((n * n, n * n), dtype=np.int64)
    for (a, b), i in idx.items():
        for (c, d), j in idx.items():
            if (a == c) != (b == d):  # exactly one coordinate equal -> adjacent
                A[i, j] = 1
    return A


def doily():
    """The doily, srg(15,6,1,3): the unique (15,6,1,3) strongly regular graph.

    = the GQ(2,2) collinearity graph = the Kneser graph K(6,2). Vertices are
    the C(6,2)=15 two-subsets of {1..6}; two are adjacent iff they are
    disjoint. Verified by the exact oracle: is_srg(...,15,6,1,3) == True
    (45 edges). Degree 6; adjacent disjoint pairs share exactly one common
    neighbour (lambda=1), non-adjacent pairs exactly 3 (mu=3).
    """
    subs = list(itertools.combinations(range(6), 2))
    s = {tuple(sorted(c)): i for i, c in enumerate(subs)}
    A = np.zeros((15, 15), dtype=np.int64)
    for c, i in s.items():
        cs = set(c)
        for d, j in s.items():
            if not (set(d) & cs):
                A[i, j] = 1
    np.fill_diagonal(A, 0)
    return A


def gq24_graph():
    """The GQ(2,4) collinearity graph, srg(27,10,1,5).

    = the complement of the Schlaefli graph = the O^-(6,2) polar space: the
    27 nonzero points v of GF(2)^6 with q(v)=0 under the minus-type quadratic
    form q(x)=x1x2+x3x4+x5+x5x6+x6; two are adjacent iff their polar
    bilinear forms vanish (orthogonal). Verified by the exact oracle:
    is_srg(...,27,10,1,5) == True (135 edges). Degree 10.
    """
    def Q(v):
        x1, x2, x3, x4, x5, x6 = v
        return (x1 * x2 + x3 * x4 + x5 + x5 * x6 + x6) & 1

    def B(u, v):
        # polar/symplectic form of q: q(u+v) + q(u) + q(v)
        w = tuple((u[i] + v[i]) & 1 for i in range(6))
        return (Q(w) ^ Q(u) ^ Q(v)) & 1

    pts = [v for v in itertools.product([0, 1], repeat=6) if Q(v) == 0 and any(v)]
    A = np.zeros((27, 27), dtype=np.int64)
    for i in range(27):
        for j in range(27):
            if i != j and B(pts[i], pts[j]) == 0:
                A[i, j] = 1
    return A


# Correct 5x11 parity-check matrix of the perfect ternary [11,6,5] Golay code,
# derived from the cyclic generator polynomial g0 = x^5 - x^3 + x^2 - x - 1
# (x^11 - 1 = (x-1) g0 h in GF(3)); the 11 columns are pairwise
# non-proportional (verified: 11 unique, no column a scalar multiple of
# another). This is what makes the coset-graph construction 22-regular and
# srg(243,22,1,2). The previous H here had two identical columns, which made
# the graph under-count edges (2430 != 2673) and fail all degree checks.
_TERNARY_GOLAY_H = [
    [1, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [2, 1, 0, 2, 1, 2, 0, 0, 1, 0, 0],
    [1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1],
]


def bvls_graph():
    """Berlekamp-van Lint-Seidel graph on 243 vertices, srg(243,22,1,2).

    Coset graph of the perfect ternary Golay code: vertices are the 3^5 = 243
    syndromes (= cosets of the code in F3^11); two vertices are adjacent iff
    their syndromes differ by +- one column of the parity-check matrix H.
    """
    H = np.array(_TERNARY_GOLAY_H, dtype=np.int64) % 3
    cols = [tuple(int(x) for x in H[:, j]) for j in range(11)]
    verts = list(itertools.product([0, 1, 2], repeat=5))  # 3^5 syndromes
    idx = {v: t for t, v in enumerate(verts)}
    n = 243
    A = np.zeros((n, n), dtype=np.int64)
    for s, i in idx.items():
        for c in cols:
            for coeff in (1, 2):
                t = tuple((s[j] + coeff * c[j]) % 3 for j in range(5))
                if t in idx:
                    A[i, idx[t]] = 1
    np.fill_diagonal(A, 0)
    return A


def random_regular_14_99(seed=0):
    """A deterministic 14-regular graph on 99 vertices (negative control).

    NOT intended to be a faithful random sampler (the config-model rejection
    sampler for this size can loop essentially forever, which is what made the
    first self-check run time out at 600s). Instead: circulant graph with
    connection set {1,2,...,7} mod 99 -- each vertex joins the 7 nearest on
    each side, giving degree 14 and a definite DEPENDENT structure that is
    certainly not srg(99,14,1,2). It terminates instantly and serves precisely
    as the negative control the oracle must reject.
    """
    return circulant(99, list(range(1, 8)))  # connection {1..7} -> degree 14


if __name__ == "__main__":
    # Self-check. tool_builder/coder MUST run this and record the output.
    print("rook(3) is_srg(9,4,1,2):", is_srg(rook(3), 9, 4, 1, 2))
    print("rook(4) is_srg(9,4,1,2):", is_srg(rook(4), 9, 4, 1, 2))

    B = bvls_graph()
    print("bvls shape:", B.shape)
    print("bvls edges:", int(B.sum() // 2))
    if B.shape == (243, 243):
        print("bvls is_srg(243,22,1,2):", is_srg(B, 243, 22, 1, 2))

    R = random_regular_14_99(seed=1)
    print("random 14-regular on 99 vertices is_srg(99,14,1,2):",
          is_srg(R, 99, 14, 1, 2))
