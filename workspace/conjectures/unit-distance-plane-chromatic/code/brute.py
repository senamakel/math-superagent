#!/usr/bin/env python3
"""
Naive oracle for the unit-distance plane-colouring problem.

Objects: a finite set of points, each coordinate an exact algebraic number in
the field Q(sqrt(3), sqrt(11)).  A pair of vertices is an edge iff the squared
distance between them is *exactly* 1 (exact rational arithmetic -- no floats).

The oracle decides two things, both obviously correctly:
  1. unit_graph(points): which pairs are at unit distance, and how many.
  2. chromatic_number / is_k_colorable: a complete backtracking k-colouring
     test with a witness colouring.

Everything is exact arithmetic.  Coordinates are given in the 4-dimensional
Q-basis {1, sqrt(3), sqrt(11), sqrt(33)} as tuples of 4 Fractions.

Relies on: the worked example in problem.md, the 7-vertex graph built from two
unit quadris (lozenges = pairs of unit equilateral triangles) sharing one
vertex, rotated so their far vertices are exactly distance 1 apart.  That graph
must certify exactly 11 edges and chromatic number 4 (colour: yes, 3-colour: no).
"""

from fractions import Fraction
from itertools import combinations

# ---- exact field Q(sqrt3, sqrt11), basis {1, r3, r11, r33} ----

# multiplication table: (coef, basis_index)
TABLE = {}
for i in range(4):
    TABLE[(i, 0)] = (Fraction(1), i)
    TABLE[(0, i)] = (Fraction(1), i)
TABLE[(1, 1)] = (Fraction(3), 0)
TABLE[(1, 2)] = (Fraction(1), 3)   # sqrt3 * sqrt11 = sqrt33
TABLE[(1, 3)] = (Fraction(3), 2)   # sqrt3 * sqrt33 = 3 sqrt11
TABLE[(2, 2)] = (Fraction(11), 0)
TABLE[(2, 3)] = (Fraction(11), 1)  # sqrt11 * sqrt33 = 11 sqrt3
TABLE[(3, 3)] = (Fraction(33), 0)
# symmetric mates
TABLE[(2, 1)] = (Fraction(1), 3)    # sqrt11 * sqrt3 = sqrt33
TABLE[(3, 1)] = (Fraction(3), 2)    # sqrt33 * sqrt3 = 3 sqrt11
TABLE[(3, 2)] = (Fraction(11), 1)   # sqrt33 * sqrt11 = 11 sqrt3


def mul(x, y):
    """Multiply two 4-tuples of rationals in the field, exact."""
    out = [Fraction(0)] * 4
    for i in range(4):
        if x[i] == 0:
            continue
        for j in range(4):
            if y[j] == 0:
                continue
            c, b = TABLE[(i, j)]
            out[b] += x[i] * y[j] * c
    return tuple(out)


def sub(x, y):
    return tuple(x[i] - y[i] for i in range(4))


def add(x, y):
    return tuple(x[i] + y[i] for i in range(4))


def sq_dist(p, q):
    """Exact squared distance between points p, q (each a pair of 4-tuples)."""
    dx = sub(p[0], q[0])
    dy = sub(p[1], q[1])
    return add(mul(dx, dx), mul(dy, dy))


ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


# ---- edge certifier ----

def unit_graph(points):
    """Return (edges, n) where edges is the list of unit-distance pairs.

    Edges are pairs of indices where the exact squared distance equals 1.
    """
    edges = []
    n = len(points)
    for i, j in combinations(range(n), 2):
        if sq_dist(points[i], points[j]) == ONE:
            edges.append((i, j))
    return edges, len(edges)


# ---- complete k-colouring test ----

def is_k_colorable(adj, k):
    """Backtracking k-colouring.  Returns (True, colouring) or (False, None).

    adj[i] = set of neighbour indices.  Complete: returns a colouring when one
    exists, so UNSAT here is a real theorem for that graph.  Symmetry break:
    vertex 0 is forced to colour 0.
    """
    n = len(adj)
    colour = [-1] * n
    colour[0] = 0
    nodes = list(range(n))

    def ok(v, c):
        for u in adj[v]:
            if colour[u] == c:
                return False
        return True

    def bt(idx):
        if idx == n:
            return True
        v = nodes[idx]
        if v == 0:
            return bt(idx + 1)
        for c in range(k):
            if ok(v, c):
                colour[v] = c
                if bt(idx + 1):
                    return True
                colour[v] = -1
        return False

    if bt(1):
        return True, colour
    return False, None


def chromatic_number(adj):
    """Smallest k for which the graph is k-colourable (backtracking)."""
    for k in range(1, len(adj) + 1):
        ok, _ = is_k_colorable(adj, k)
        if ok:
            return k
    raise AssertionError("unreachable")


# ---- the calibrated 7-vertex example ----

def moser_spindle_points():
    """The 7 points of the two-lozenges graph.

    Lozenge A: O(0,0), a1(1,0), a2(1/2, sqrt3/2), a3(3/2, sqrt3/2).
    Lozenge B: O rotated by phi with cos phi = 5/6, sin phi = sqrt11/6,
    giving far vertices exactly distance 1 apart.
    """
    O = ((0, 0, 0, 0), (0, 0, 0, 0))
    a1 = ((1, 0, 0, 0), (0, 0, 0, 0))
    a2 = ((Fraction(1, 2), 0, 0, 0), (0, Fraction(1, 2), 0, 0))
    a3 = ((Fraction(3, 2), 0, 0, 0), (0, Fraction(1, 2), 0, 0))
    b1 = ((Fraction(5, 6), 0, 0, 0), (0, 0, Fraction(1, 6), 0))
    b2 = ((Fraction(5, 12), 0, 0, Fraction(-1, 12)),
          (0, Fraction(5, 12), Fraction(1, 12), 0))
    b3 = (add(b1[0], b2[0]), add(b1[1], b2[1]))
    return [O, a1, a2, a3, b1, b2, b3]


def main():
    pts = moser_spindle_points()
    print("distinct points:", len(pts))
    edges, m = unit_graph(pts)
    n = len(pts)
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    print("number of unit-distance edges:", m)
    print("edges:", edges)

    # confirm every declared edge really has squared distance exactly 1
    for i, j in edges:
        assert sq_dist(pts[i], pts[j]) == ONE, (i, j)
    print("all edges certified exactly |x-y|^2 = 1")

    # confirm no NON-edge is at unit distance (nothing missed)
    for i, j in combinations(range(n), 2):
        if (i, j) not in edges and (j, i) not in edges:
            assert sq_dist(pts[i], pts[j]) != ONE, "missed edge %s" % (i, j)
    print("no spurious or missed edges")

    chi = chromatic_number(adj)
    print("chromatic number:", chi)
    ok4, col4 = is_k_colorable(adj, 4)
    ok3, _ = is_k_colorable(adj, 3)
    print("4-colourable:", ok4, "colouring:", col4)
    print("3-colourable:", ok3)
    assert chi == 4 and ok4 and not ok3
    assert m == 11
    print("CALIBRATION PASSED: 11 edges, chi=4, not 3-colourable")


if __name__ == "__main__":
    main()
