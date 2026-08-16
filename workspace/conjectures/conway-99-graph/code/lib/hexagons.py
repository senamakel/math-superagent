"""Exact counting of induced 6-cycles (induced hexagons) in a graph.

count_induced_C6(A) counts the induced C6 subgraphs of a 0/1 integer adjacency
matrix A exactly, using only boolean/integer arithmetic (no floating point).

Method (clean-room, polynomial time, not a search of the answer space):

An induced hexagon is a 6-cycle with no chords.  Each induced hexagon has 6
rotations and 2 directions, so 12 oriented representations (v1,v2,v3,v4,v5,v6)
with edges only between consecutive vertices.  We anchor each oriented
representation at its first four vertices (v1,v2,v3,v4), which must be an
*oriented induced P4* (a path v1-v2-v3-v4 with no chord among those four:
v1.v3, v1.v4, v2.v4 all non-adjacent).

For a fixed oriented induced P4 the hexagon is completed by (v5,v6) with
  v5 in N(v4), v5 not adjacent to v1,v2,v3,   (and v5 distinct from v1..v4)
  v6 in N(v5) cap N(v1), v6 not adjacent to v2,v3,v4.
The constraints above, together with the induced-P4 condition, are exactly the
9 non-consecutive non-edges of a C6, so a completion is precisely an induced
hexagon extending this P4, and each oriented hexagon has a unique (v1..v4)
anchor -- no double counting.  The total oriented count is divided by 12.

The completion count for one P4 is done with a matrix-vector trick so that no
inner loop over (v5,v6) pairs is needed:
    mask5 = N4 & ~N1 & ~N2 & ~N3            (candidate v5)
    A     = N1 & ~N2 & ~N3 & ~N4            (candidate-v6 frame: adj v1, not v2,v3,v4)
    S     = mask5 @ N                       S[w] = number of v5 in mask5 adjacent to w
    completions = sum_{w in A} S[w].
A contains no vertex of {v1..v5} (shown in the module docstring's sibling note),
so no correction terms are needed.

Verified against brute force: rook(3)=srg(9,4,1,2) gives 6, a bare C6 gives 1.
The BvLS srg(243,22,1,2) result is in code/out/hexagon_count_bvls.py's capture.
"""
import numpy as np
from multiprocessing import Pool


def _completions(N, Nint, v1, v2, v3, v4):
    """Number of induced-P4 completions (v5,v6) closing an induced hexagon."""
    N1, N2, N3, N4 = N[v1], N[v2], N[v3], N[v4]
    mask5 = N4 & ~N1 & ~N2 & ~N3
    A = N1 & ~N2 & ~N3 & ~N4
    if not mask5.any():
        return 0
    S = mask5.astype(np.int64) @ Nint
    return int((S * A).sum())


def _root_oriented(v1, Aint):
    """Oriented induced-hexagon count anchored with first vertex v1."""
    n = Aint.shape[0]
    N = Aint.astype(bool)
    Nint = Aint
    oriented = 0
    N1 = N[v1]
    for v2 in np.flatnonzero(N1):
        N2 = N[v2]
        cand3 = N2 & ~N1
        cand3[v1] = False
        for v3 in np.flatnonzero(cand3):
            N3 = N[v3]
            cand4 = N3 & ~N1 & ~N2
            cand4[v1] = cand4[v2] = False
            for v4 in np.flatnonzero(cand4):
                oriented += _completions(N, Nint, v1, v2, v3, v4)
    return oriented


def count_induced_C6(A, workers=1):
    """Exact induced-C6 count. A is a 0/1 integer matrix. workers>1 splits
    over the root vertex (which is exact because each oriented hexagon has a
    unique root and the sum is over disjoint roots)."""
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    if workers <= 1:
        oriented = sum(_root_oriented(v, A) for v in range(n))
    else:
        with Pool(workers) as p:
            per = p.starmap(_root_oriented, [(v, A) for v in range(n)])
        oriented = sum(per)
    assert oriented % 12 == 0, f"oriented {oriented} not divisible by 12"
    return oriented // 12


def hexagon_formula(n, k):
    """Reimbayev-style conjectured closed form for the induced-hexagon count:
    (1/12) n k (k-2) (2k^2 - 21k + 53)."""
    return n * k * (k - 2) * (2 * k * k - 21 * k + 53) // 12
