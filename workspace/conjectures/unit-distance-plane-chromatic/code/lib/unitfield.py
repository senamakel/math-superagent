#!/usr/bin/env python3
"""
Exact arithmetic in the field Q(sqrt(3), sqrt(11)) for the Moser-spindle
plane-colouring work.  Every coordinate of every point is a pair of 4-tuples
(x, y) of rationals in the Q-basis {1, sqrt(3), sqrt(11), sqrt(33)}.

Provided:
  add, sub, mul, sq_dist(p, q)      -- exact field arithmetic
  unit_graph(points)                -- (edges, m): pairs at squared distance 1
  moser_spindle_points()            -- the calibrated 7 points
  all_sqdist(points)                -- dict (i,j)-> exact sqdist for i<j

All arithmetic is exact (Fraction-based); nothing here is a float.
Verified against code/brute.py: moser_spindle_points() certifies exactly 11
unit edges, chi=4, not 3-colourable.
"""

from fractions import Fraction
from itertools import combinations

# ---- exact field Q(sqrt3, sqrt11), basis {1, r3, r11, r33} ----

# multiplication table: (coef, basis_index)
TABLE = {
    (0, 0): (Fraction(1), 0),
    (0, 1): (Fraction(1), 1),
    (0, 2): (Fraction(1), 2),
    (0, 3): (Fraction(1), 3),
    (1, 0): (Fraction(1), 1),
    (1, 1): (Fraction(3), 0),
    (1, 2): (Fraction(1), 3),   # sqrt3 * sqrt11 = sqrt33
    (1, 3): (Fraction(3), 2),   # sqrt3 * sqrt33 = 3 sqrt11
    (2, 0): (Fraction(1), 2),
    (2, 1): (Fraction(1), 3),   # sqrt11 * sqrt3 = sqrt33
    (2, 2): (Fraction(11), 0),
    (2, 3): (Fraction(11), 1),  # sqrt11 * sqrt33 = 11 sqrt3
    (3, 0): (Fraction(1), 3),
    (3, 1): (Fraction(3), 2),   # sqrt33 * sqrt3 = 3 sqrt11
    (3, 2): (Fraction(11), 1),  # sqrt33 * sqrt11 = 11 sqrt3
    (3, 3): (Fraction(33), 0),
}


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


ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


def sq_dist(p, q):
    """Exact squared distance between points p, q (each a pair of 4-tuples)."""
    dx = sub(p[0], q[0])
    dy = sub(p[1], q[1])
    return add(mul(dx, dx), mul(dy, dy))


def cmp_sqdist(a, b):
    """Compare two exact field elements by converting to float.

    Used only to *select* candidate pairs for the >= 1/4 test; the actual
    unit-distance certification and all colouring work is exact.  sqdist
    values here live in a 4D Q-vector space and are all reached from
    coordinates whose magnitudes are bounded, so a double is exact enough to
    only ever be the gate, never the verdict.
    """
    return float(a[0] + a[1] * 3 ** 0.5 + a[2] * 11 ** 0.5 + a[3] * 33 ** 0.5)


def pt(x, y):
    """Point(x, y) with rational or 4-tuple components -> (4-tuple, 4-tuple)."""
    def fz(v):
        if isinstance(v, tuple):
            return v
        return (Fraction(v), Fraction(0), Fraction(0), Fraction(0))
    return (fz(x), fz(y))


def unit_graph(points):
    """Return (edges, m): list of (i,j) pairs at exact squared distance 1."""
    edges = []
    n = len(points)
    for i, j in combinations(range(n), 2):
        if sq_dist(points[i], points[j]) == ONE:
            edges.append((i, j))
    return edges, len(edges)


def all_sqdist(points):
    """Return dict mapping (i,j) with i<j -> exact squared distance."""
    n = len(points)
    return {(i, j): sq_dist(points[i], points[j])
            for i, j in combinations(range(n), 2)}


def moser_spindle_points():
    """The calibrated 7 points of the two-lozenges Moser spindle.

    Rhombus A: O(0,0), a1(1,0), a2(1/2, sqrt3/2), a3(3/2, sqrt3/2).
    Rhombus B: O rotated by phi, cos phi = 5/6, sin phi = sqrt11/6, so the
    far vertices a3 and b3 are exactly distance 1 apart (the spindle chord).
    Matches brute.py exactly; index 0 = O.
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


def diamond_points():
    """The 4-vertex diamond: two unit equilateral triangles on common edge AB.

    A=(0,0), B=(1,0), C=(1/2, sqrt3/2), D=(1/2, -sqrt3/2).  Edges: AB, AC, BC,
    AD, BD.  |C-D| = sqrt(3) (squared distance 3), tips not joined.  In every
    3-colouring the two triangles force C and D to share the third colour.
    """
    A = pt(0, 0)
    B = pt(1, 0)
    # sqrt3/2 in field basis {1,sqrt3,sqrt11,sqrt33} is (0, 1/2, 0, 0)
    half_sqrt3 = (Fraction(0), Fraction(1, 2), Fraction(0), Fraction(0))
    C = pt((Fraction(1, 2), 0, 0, 0), half_sqrt3)
    D = pt((Fraction(1, 2), 0, 0, 0), (Fraction(0), Fraction(-1, 2),
                                       Fraction(0), Fraction(0)))
    return [A, B, C, D]


def minkowski_sum(A, B):
    """Exact Minkowski sum A + B = { a + b : a in A, b in B }, kept distinct."""
    pts = []
    seen = set()
    for a in A:
        for b in B:
            p = (add(a[0], b[0]), add(a[1], b[1]))
            if p not in seen:
                seen.add(p)
                pts.append(p)
    return pts
