"""Exact unit-distance graph construction.

The foundation of the whole oracle pair. `unit_graph` takes a list of points
with exact algebraic coordinates and returns the list of vertex pairs at
Euclidean distance exactly 1, with that equality certified symbolically — no
tolerance.

Coordinates are supplied as length-2 sequences of sympy expressions (rationals,
QQbar, sqrt combinations). Points must be exact; floats are rejected.
"""
import sympy as sp


def _exact_pair(p):
    """Validate/coerce one point into a length-2 sympy exact sequence."""
    if len(p) != 2:
        raise ValueError(f"point must have 2 coordinates, got {p!r}")
    out = []
    for c in p:
        x = sp.sympify(c)
        if x.has(sp.Float):
            raise ValueError(f"float coordinate not allowed (must be exact): {c!r}")
        out.append(x)
    return tuple(out)


def unit_graph(points):
    """Return the list of edges [(i, j), ...] of the unit-distance graph on
    `points`: all pairs (i, j), i < j, with |p_i - p_j|^2 == 1 exactly.

    The check is symbolic: it simplifies |a-b|^2 - 1 and requires the result
    to equal the integer 0 by exact sympy equality. No tolerance is used.

    Returns (n, edges). `edges` is a list of (i, j) tuples with i < j.
    """
    pts = [_exact_pair(p) for p in points]
    n = len(pts)
    edges = []
    for i in range(n):
        xi, yi = pts[i]
        for j in range(i + 1, n):
            xj, yj = pts[j]
            d2 = sp.simplify((xi - xj) ** 2 + (yi - yj) ** 2)
            if d2 == 1:
                edges.append((i, j))
    return n, edges


def moser_spindle():
    """Return the 7-vertex Moser spindle as a list of exact coordinate pairs.

    Two unit rhombi (each a pair of unit equilateral triangles on a shared
    edge) share the vertex O and are rotated by the angle gamma so that their
    two far tips Q and Q' are at distance exactly 1.

    A rhombus is two equilateral triangles on a shared unit edge from O:
      O -- P1 -- Q -- P2 -- O, all unit edges, with Q at distance sqrt(3) from
      O. Rotating this by gamma about O and reusing the same O and the same
      P1, P2 unit directions is equivalent to starting the second rhombus at
      the rotated P1', P2'. We need 2*sqrt(3)*sin(gamma/2) = 1, so
      sin(gamma/2) = 1/(2*sqrt(3)), whose half-angle gives
      cos(gamma/2) = sqrt(11/12).

      Base rhombus vertices (unit triangles on edge O--P1 with third point P2):
        O   = (0, 0)
        P1  = (1, 0)
        P2  = (1/2, sqrt(3)/2)
        Q   = P1 + P2 = (3/2, sqrt(3)/2),   |Q - O| = sqrt(3)
      Rotated (primed) rhombus obtained by rotating (P1, P2, Q) by gamma about
      O.   Coordinates land in Q(sqrt(3), sqrt(33), sqrt(11)).
    """
    s3 = sp.sqrt(3)
    O = (0, 0)
    P1 = (1, 0)
    P2 = (sp.Rational(1, 2), s3 / 2)
    Q = (sp.Rational(3, 2), s3 / 2)

    # half-angle: sin(gamma/2) = 1/(2 sqrt3), cos(gamma/2) = sqrt(11/12)
    sh = sp.Rational(1, 2) / s3          # sin(gamma/2)
    ch = sp.sqrt(sp.Rational(11, 12))     # cos(gamma/2)
    cg = 1 - 2 * sh * sh                  # cos(gamma) = 1 - 2 sin^2(gamma/2)
    sg = 2 * sh * ch                      # sin(gamma)

    def rot(x, y):
        return (sp.simplify(cg * x - sg * y), sp.simplify(sg * x + cg * y))

    P1p = rot(*P1)
    P2p = rot(*P2)
    Qp = rot(*Q)

    return [O, P1, P2, Q, P1p, P2p, Qp]
