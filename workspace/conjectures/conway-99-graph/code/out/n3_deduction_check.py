"""Pin the n3 structural invariant on both control graphs exactly.

For an srg(v,k,1,2) with lambda=1, mu=2: every edge lies in a unique triangle,
and two distinct triangles share at most one vertex (an edge in exactly one
triangle).  "Joined by e edges" = number of edges of the graph joining a vertex
of triangle T1 to a distinct vertex of triangle T2.

n3 = number of unordered pairs of triangles joined by exactly 2 edges.

This script ONLY COMPUTES the triangle-pair join-edge histograms on both
control graphs (rook(3) and BvLS) in exact integer arithmetic over the
adjacency matrices, confirms n3 = 0 on both, and confirms the total-pair
bookkeeping sums to C(T,2) so the two-parameter histogram is complete.  It
draws NO conclusion about v=99: the value of n3 on the control graphs is a
computed fact about THOSE graphs, not about a putative (99,14,1,2).  Any claim
that "a (99,14,1,2) is forced to have n3 >= 1" is a separate, sourced step
(Makhnev 1988 Thm 2) and is deliberately NOT asserted here.
"""
import numpy as np
from lib.srg import rook, bvls_graph
from itertools import combinations


def triangles(A):
    """Return list of triangles (sets of 3 vertices) via brute force over triples."""
    n = A.shape[0]
    tris = []
    for i, j, l in combinations(range(n), 3):
        if A[i, j] and A[i, l] and A[j, l]:
            tris.append(frozenset((i, j, l)))
    return tris


def join_hist(A, tris):
    """Histogram: number of triangle pairs joined by exactly e edges."""
    n = A.shape[0]
    A = np.asarray(A)
    from collections import Counter
    hist = Counter()
    for a, b in combinations(tris, 2):
        e = 0
        for x in a:
            for y in b:
                if A[x, y]:
                    e += 1
        hist[e] += 1
    return hist


for name, A in [("rook(3) srg(9,4,1,2)", rook(3)),
                ("bvls   srg(243,22,1,2)", bvls_graph())]:
    A = np.asarray(A)
    tris = triangles(A)
    T = len(tris)
    hist = join_hist(A, tris)
    n3 = hist.get(2, 0)
    total = sum(hist.values())
    print(f"{name}:")
    print(f"  triangles T = {T}  (expect vk/6)")
    print(f"  join-edge histogram {dict(sorted(hist.items()))}")
    print(f"  sum(hist) = {total}   C(T,2) = {T*(T-1)//2}   complete: {total == T*(T-1)//2}")
    print(f"  n3 (pairs joined by exactly 2 edges) = {n3}")
    print()
