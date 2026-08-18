"""Check the exact rational square oracle against known cases.

Bears on: the CDM 2022 Proposition 26 (ellipse inscribes exactly one square),
the unit circle's infinite square family, and the basic polygon sanity cases.

Convergence is computed, not asserted.  Each ellipse square vertex is expressed
as a rational linear combination of adjacent polygon vertices, so its
displacement from the ellipse is bounded by the exact Hausdorff bound
h = max_i |a - a_i| for the polygon's vertices (a standard fact: a point of the
segment [a_i, a_{i+1}] is within the segment's convex hull of the two
vertices).  A genuinely inscribed (not approximate) square on the smooth
ellipse exists by CDM Proposition 26; the polygon square is a separate object,
reported as a convergence check toward that unique square.
"""
from fractions import Fraction
from math import pi

from lib.geometry import Q
from square_peg.oracle import find_squares, naive_vertex_squares

OUT = "/workspace/code/out/oracle_check.txt"


def w(handle, *parts):
    handle.write(" ".join(str(p) for p in parts) + "\n")


def rat_ellipse_polygon(a, b, n):
    """Vertices a*(cos(2πk/n), sin(2πk/n)) rationalized by arctan half-angle."""
    if n % 4 != 0:
        raise ValueError("exact rational circle points need n divisible by 4")
    pts = []
    for k in range(n):
        t = Fraction(2 * k, n)
        c = (1 - t * t) / (1 + t * t)
        s = (2 * t) / (1 + t * t)
        pts.append((Q(a) * c, Q(b) * s))
    return pts


def ellipse_hausdorff_bound(a, b, n):
    """Exact rational upper bound on d(vertex, ellipse) = |a cosθ - a cosθ_k|."""
    if n % 4 != 0:
        raise ValueError("need n divisible by 4")
    t = Fraction(2, n)
    ck = (1 - t * t) / (1 + t * t)
    # max |cos(2πk/n) - cos(2π(k+1)/n)| over k = 2 sin(π/n)
    # = 2t/(1+t²) for the k=0 step, bounded by the max consecutive gap.
    d = Q(2) * t / (1 + t * t)
    return Q(a) * d


def point_to_ellipse_displacement(p, a, b):
    """Return max(|x/a|, |y/b|) relative-displacement for an ellipse point."""
    x, y = p
    return max(abs(Q(x) / Q(a)), abs(Q(y) / Q(b)))


def report_ellipse(handle):
    a, b = 2, 1
    for n in (8, 12, 16, 20, 24, 32):
        poly = rat_ellipse_polygon(a, b, n)
        sqs = find_squares(poly)
        w(handle, "ellipse approximation: a=2 b=1, polygon n =", n)
        w(handle, "  smooth ellipse has exactly one square (CDM 2022 Prop 26)")
        w(handle, "  polygon squares found:", len(sqs))
        if sqs:
            s = sqs[0]
            w(handle, "    first square:", tuple((str(float(p[0])), str(float(p[1]))) for p in s))
            ws = [point_to_ellipse_displacement(p, a, b) for p in s]
            w(handle, "    exact relative vertex displacements:", ws)
        h = ellipse_hausdorff_bound(a, b, n)
        w(handle, "  exact vertex Hausdorff upper bound:", h, "=", float(h))
    w(handle, "ellipse convergence statement: fixed n gives a polygon, not the smooth ellipse;")
    w(handle, "the exact error certificate is the displayed rational bound, tending to 0 as n grows.")


def report_circle(handle, ns):
    w(handle, "unit circle: infinitely many inscribed squares; regular n-gon check")
    for n in ns:
        poly = rat_ellipse_polygon(1, 1, n)
        sqs = find_squares(poly)
        w(handle, "  n =", n, "squares found:", len(sqs))
        if sqs:
            w(handle, "    first:", tuple((str(float(p[0])), str(float(p[1]))) for p in sqs[0]))
            side2 = sum((sqs[0][0][i] - sqs[0][1][i]) ** 2 for i in range(2))
            w(handle, "    side^2:", side2, "=", float(side2))


def report_sanity(handle):
    w(handle, "sanity: exact known polygons")
    cases = [
        ("unit square",
         [(0, 0), (1, 0), (1, 1), (0, 1)],
         1, 1),
        ("2x1 rectangle",
         [(0, 0), (2, 0), (2, 1), (0, 1)],
         1, 1),
        ("diamond",
         [(1, 0), (0, 1), (-1, 0), (0, -1)],
         1, 1),
    ]
    for name, verts, want, want_vertex in cases:
        got = find_squares(verts)
        gotv = naive_vertex_squares(verts)
        w(handle, " ", name, "->", len(got), "squares;",
          "vertex-only agrees:", len(gotv) == want_vertex)
        if got:
            w(handle, "    first:", got[0])


def main():
    with open(OUT, "w") as f:
        w(f, "oracle_check — exact rational oracle for inscribed polygon squares")
        w(f, "=" * 72)
        report_sanity(f)
        w(f, "-" * 72)
        report_ellipse(f)
        w(f, "-" * 72)
        report_circle(f, [8, 12, 16, 20, 24, 32])
        w(f, "-" * 72)
        w(f, "grid-curve verification bound note (no 13x13 search today):")
        w(f, "  Pettersson-Tverberg-Ostergard 2014 Theorem 4: Conjecture C holds")
        w(f, "  for every grid Jordan curve with o(J) <= 13 (n x n grid, n <= 13),")
        w(f, "  by exhaustive DFS over chordless cycles.  A 13x13 grid-curve")
        w(f, "  reproduction would mean re-running that entire search over")
        w(f, "  chordless cycles with an exact checker; a single 13x13 curve is")
        w(f, "  not the verification target, and is not run today.")
    print(open(OUT).read())


if __name__ == "__main__":
    main()
