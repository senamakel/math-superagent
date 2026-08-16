"""Exact count of (non-induced) 6-cycles in a graph given as 0/1 adjacency matrix.

Method: for every directed 3-path (a,b,c,d) with distinct vertices, count the
pairs (e,f) with e in N(d), f in N(a), e != f, e,f avoiding {a,b,c,d}, and
e-f an edge.  The complementary arc (d,e,f,a) closes a 6-cycle.

Multiplicity: a given undirected 6-cycle is cut at each of its 6 edges and read
in each of 2 directions, giving 12 directed (path, arc) pairs. So
  directed_total = 12 * (#undirected 6-cycles).
"""
import numpy as np
from collections import defaultdict


def count_C6(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    # adjacency lists
    N = [set(np.flatnonzero(A[i])) for i in range(n)]
    directed = 0
    for a in range(n):
        Na = N[a]
        for b in Na:
            for c in N[b] - {a}:
                for d in N[c] - {a, b}:
                    # path a-b-c-d distinct. count e in N(d), f in N(a)
                    Nd = N[d]
                    for e in Nd:
                        if e in (a, b, c):
                            continue
                        # f in N(a) \ {b,c,d}, f-e edge
                        for f in Na:
                            if f in (b, c, d) or f == e:
                                continue
                            if f in N[e]:
                                directed += 1
    assert directed % 12 == 0, f"directed {directed} not divisible by 12"
    return directed // 12


def hexagon_formula(n, k):
    return n * k * (k - 2) * (2 * k * k - 21 * k + 53) // 12


if __name__ == "__main__":
    from lib.srg import rook, bvls_graph

    # Rook's graph (9,4,1,2): formula = (1/12)*9*4*2*(32-84+53) = 72/12 = 6
    R = rook(3)
    c = count_C6(R)
    print("rook(3) C6 count:", c)
    print("formula(9,4):", hexagon_formula(9, 4), "match:", c == hexagon_formula(9, 4))
