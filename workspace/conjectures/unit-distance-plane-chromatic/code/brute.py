#!/usr/bin/env python3
"""
brute.py -- naive oracle for the Hadwiger-Nelson unit-distance graph problem.

This is the OBVIOUSLY-CORRECT exact-arithmetic oracle, deliberately not
optimised. It does two jobs, both in exact arithmetic over the algebraic
number field Q(sqrt(3), sqrt(11)) whose points the worked example lives in:

  1. unit_graph(points): certify, pair by pair, which pairs are at EXACTLY
     unit distance, i.e.  |x - y|^2 == 1 as an element of Q(sqrt3,sqrt11).
     No floating point anywhere: every squared distance is a field element
     and the equality test is exact tuple equality.

  2. coloring_test(graph, k): a complete (exhaustive, symmetry-broken)
     k-colourability test returning (True, witness) when a proper k-colouring
     exists and (False, None) otherwise. Used to decide the exact chromatic
     number of a small graph by trying k = 1, 2, 3, ...

It is calibrated against the 7-vertex worked example in problem.md: the
"spindle" built from two unit rhombi (each two equilateral triangles) sharing
a vertex, rotated so their far vertices are at unit distance. That graph must
report exactly 11 unit edges, chromatic number 4, and NOT 3.

Field arithmetic
----------------
An element of Q(sqrt3, sqrt11) is written c0 + c1*sqrt3 + c2*sqrt11 +
c3*sqrt33, stored as a 4-tuple of Fractions. The multiplication table:

    sqrt3 * sqrt3   = 3
    sqrt11 * sqrt11 = 11
    sqrt33 * sqrt33 = 33
    sqrt3  * sqrt11 = sqrt33
    sqrt3  * sqrt33 = 3 sqrt11
    sqrt11 * sqrt33 = 11 sqrt3

A point is a pair (re, im) of such field elements, so a complex number.
"""

from fractions import Fraction as F

# ---------------------------------------------------------------------------
# Exact field operations on Q(sqrt3, sqrt11), basis {1, sqrt3, sqrt11, sqrt33}
# ---------------------------------------------------------------------------

SQRT3 = (F(0), F(1), F(0), F(0))
SQRT11 = (F(0), F(0), F(1), F(0))

ZERO = (F(0), F(0), F(0), F(0))
ONE = (F(1), F(0), F(0), F(0))


def _from_Q(r):
    return (F(r), F(0), F(0), F(0))


def fadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def fmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    c0 = a0 * b0 + 3 * a1 * b1 + 11 * a2 * b2 + 33 * a3 * b3
    c1 = a0 * b1 + a1 * b0 + 11 * a2 * b3 + 11 * a3 * b2
    c2 = a0 * b2 + a2 * b0 + 3 * a1 * b3 + 3 * a3 * b1
    c3 = a0 * b3 + a3 * b0 + a1 * b2 + a2 * b1
    return (c0, c1, c2, c3)


def feq(a, b):
    return all(x == y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Complex numbers over the field
# ---------------------------------------------------------------------------

def cmul(p, q):
    " (a+bi)(c+di) = (ac-bd) + (ad+bc)i "
    a, b = p
    c, d = q
    return (fsub(fmul(a, c), fmul(b, d)),
            fadd(fmul(a, d), fmul(b, c)))


def cadd(p, q):
    return (fadd(p[0], q[0]), fadd(p[1], q[1]))


def sq_dist(p, q):
    " |p - q|^2 as an exact field element "
    dx = fsub(p[0], q[0])
    dy = fsub(p[1], q[1])
    return fadd(fmul(dx, dx), fmul(dy, dy))


def is_unit(p, q):
    " Exact test: is |p - q|^2 == 1 in Q(sqrt3,sqrt11)? "
    return feq(sq_dist(p, q), ONE)


# ---------------------------------------------------------------------------
# The 7-vertex worked example (Moser spindle construction)
# ---------------------------------------------------------------------------

def moser_spindle_points():
    """ The 7 points of problem.md's construction.

    Rhombus R1 (two equilateral triangles sharing the short diagonal):
      vertices {0, 1, u, 1+u},  u = exp(i pi/3) = 1/2 + i sqrt3/2.
    Rotate R1 about the shared vertex 0 by theta with
        sin(theta/2) = 1/(2 sqrt3)   i.e.  |(1+u) - e^{i theta}(1+u)| = 1,
    giving the far vertex e^{i theta}(1+u) at unit distance from (1+u).
        e^{i theta} = 5/6 + i sqrt11/6  (cos=5/6, sin=sqrt11/6).
    """
    half = _from_Q(F(1, 2))

    # u = exp(i pi/3)
    u = (half, (F(0), F(1, 2), F(0), F(0)))          # 1/2 + i sqrt3/2

    # e^{i theta} = 5/6 + i sqrt11/6
    et = (_from_Q(F(5, 6)), (F(0), F(0), F(1, 6), F(0)))

    one = (_from_Q(1), ZERO)
    zero = (ZERO, ZERO)

    one_plus_u = cadd(one, u)                          # 3/2 + i sqrt3/2
    u_et = cmul(u, et)                                 # u * e^{i theta}
    opu_et = cmul(one_plus_u, et)                      # (1+u) * e^{i theta}

    return [zero, one, u, one_plus_u, et, u_et, opu_et]


# ---------------------------------------------------------------------------
# Unit-distance graph certification
# ---------------------------------------------------------------------------

def unit_graph(points):
    """ Return (vertices, edges) where edges = sorted list of vertex-index
        pairs at exactly unit distance. Certifies every edge symbolically. """
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if is_unit(points[i], points[j]):
                edges.append((i, j))
    return list(range(n)), sorted(edges)


# ---------------------------------------------------------------------------
# Complete k-colourability
# ---------------------------------------------------------------------------

def coloring_test(n, edges, k):
    """ Complete k-colourability test.

    n      : number of vertices 0..n-1
    edges  : list of (i, j) pairs
    k      : number of colours

    Returns (True, assignment) if a proper k-colouring exists (assignment is
    a list of length n, each entry in 0..k-1), else (False, None). Exhaustive
    backtracking with symmetry breaking: vertex 0 is forced to colour 0.
    """
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    color = [-1] * n

    def backtrack(v):
        if v == n:
            return True
        # Try colours 0..k-1; prune by neighbour check.
        for c in range(k):
            if v == 0 and c != 0:
                break                     # symmetry break: fix vertex 0
            ok = True
            for nb in adj[v]:
                if nb < v and color[nb] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = -1
        return False

    found = backtrack(0)
    return (True, list(color)) if found else (False, None)


def chromatic_number(n, edges, maxk=5):
    """ Smallest k in 1..maxk for which a proper k-colouring exists. """
    for k in range(1, maxk + 1):
        ok, _ = coloring_test(n, edges, k)
        if ok:
            return k
    return None


# ---------------------------------------------------------------------------
# Self-check of the field arithmetic, then the worked example
# ---------------------------------------------------------------------------

def _selfcheck_field():
    # sqrt3*sqrt3 = 3, sqrt11*sqrt11 = 11, sqrt33*sqrt33 = 33
    assert feq(fmul(SQRT3, SQRT3), (F(3), F(0), F(0), F(0)))
    assert feq(fmul(SQRT11, SQRT11), (F(11), F(0), F(0), F(0)))
    r33 = fmul(SQRT3, SQRT11)
    assert feq(fmul(r33, r33), (F(33), F(0), F(0), F(0)))
    # sqrt3 * sqrt33 = 3 sqrt11 ;  sqrt11 * sqrt33 = 11 sqrt3
    assert feq(fmul(SQRT3, r33), (F(0), F(0), F(3), F(0)))
    assert feq(fmul(SQRT11, r33), (F(0), F(11), F(0), F(0)))
    # distributivity sanity: (sqrt3+sqrt11)^2 = 14 + 2 sqrt33
    s = fadd(SQRT3, SQRT11)
    assert feq(fmul(s, s), (F(14), F(0), F(0), F(2)))
    print("field self-check: OK")


def main():
    _selfcheck_field()

    pts = moser_spindle_points()
    n = len(pts)
    # Confirm all 7 points are distinct.
    distinct = len({(tuple(re), tuple(im)) for re, im in pts})
    print(f"number of points: {n}  (distinct: {distinct})")

    verts, edges = unit_graph(pts)
    print(f"unit-distance edges certified: {len(edges)}")
    for e in edges:
        i, j = e
        print(f"  edge {i}-{j}:  |p{i} - p{j}|^2 == 1  exactly")

    ch = chromatic_number(n, edges)
    print(f"chromatic number: {ch}")

    for k in (3, 4):
        ok, witness = coloring_test(n, edges, k)
        print(f"{k}-colourable? {ok}"
              + (f"  witness: {witness}" if ok else ""))

    # Calibration assertions.
    assert distinct == 7, "expected 7 distinct points"
    assert len(edges) == 11, f"expected 11 unit edges, got {len(edges)}"
    assert ch == 4, f"expected chromatic number 4, got {ch}"
    ok3, _ = coloring_test(n, edges, 3)
    assert not ok3, "graph must NOT be 3-colourable"
    ok4, _ = coloring_test(n, edges, 4)
    assert ok4, "graph must be 4-colourable"
    print("CALIBRATION PASSED: 7 points, 11 certified unit edges, "
          "chi = 4 and not 3.")


if __name__ == "__main__":
    main()
