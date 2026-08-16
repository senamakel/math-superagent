#!/usr/bin/env python3
"""Naive exact-arithmetic oracle for the Erdos-Szekeres convex-position problem.

Deliberately obvious, not fast.  Works over any exact coordinate ring that
supports +,-,* and comparison (int, Fraction, or exactly-representable
rationals).  Every predicate is the sign of a 3x3 determinant computed
exactly, so there is no floating-point rounding.

What this module decides / reports:
  general_position(pts)            -> True iff no three points are collinear.
  convex_position(sub)             -> True iff the given points are exactly the
                                      vertices of their own convex hull.
  largest_convex_subset(pts)       -> size of the largest subset in convex
                                      position (naive: checks every subset).
  cup_cap_spectrum(pts)            -> (largest cup size, largest cap size).
  largest_convex_points(pts)       -> an actual largest convex subset.

The oracle exists to pin down the definitions exactly, and to be the ground
truth that every faster method is checked against.  Exact verification only;
no search over order types is attempted here.
"""

from itertools import combinations
from fractions import Fraction


def orient(a, b, c):
    """Sign of the z-component of (b-a) x (c-a).

    Returns +1 (ccw), -1 (cw), or 0 (collinear).  Exact.
    """
    d = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if d > 0:
        return 1
    if d < 0:
        return -1
    return 0


def general_position(pts):
    """True iff no three points of pts are collinear (exact)."""
    n = len(pts)
    for i, j, k in combinations(range(n), 3):
        if orient(pts[i], pts[j], pts[k]) == 0:
            return False
    return True


def convex_hull(points):
    """Indices->sorted points; returns the strictly convex hull vertices in
    ccw order using Andrew's monotone chain with exact orientation.
    Collinear points are dropped (harmless under general position)."""
    pts = sorted(points)
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex_position(subpoints):
    """True iff subpoints are exactly the vertex set of their convex hull,
    i.e. form a (strictly) convex polygon."""
    return len(convex_hull(subpoints)) == len(subpoints)


def largest_convex_subset(pts):
    """Largest subset of pts in convex position.  Naive: try every subset.
    Returns (size, one exemplar subset of point-coordinates)."""
    n = len(pts)
    best = 0
    bestset = None
    # search from large k down for speed; result is exact regardless of order
    for k in range(n, 0, -1):
        for combo in combinations(range(n), k):
            sub = [pts[i] for i in combo]
            if convex_position(sub):
                return k, sub
    return 0, []


def _sorted_slopes(subpoints):
    """Slopes of consecutive segments after sorting by x-coordinate.
    Requires distinct x-coordinates (holds for all general-position sets we
    feed, and is the standard cup/cap setting)."""
    pts = sorted(subpoints)
    out = []
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        assert dx != 0, "cup/cap routine requires distinct x-coordinates"
        out.append(dy / dx)
    return out


def is_cup(subpoints):
    """True iff subpoints, sorted by x, have strictly increasing slopes
    (the classic 'cup': vertices of an upper convex chain)."""
    sl = _sorted_slopes(subpoints)
    return all(sl[i] < sl[i + 1] for i in range(len(sl) - 1)) if len(sl) >= 2 else True


def is_cap(subpoints):
    """True iff subpoints, sorted by x, have strictly decreasing slopes
    (the classic 'cap')."""
    sl = _sorted_slopes(subpoints)
    return all(sl[i] > sl[i + 1] for i in range(len(sl) - 1)) if len(sl) >= 2 else True


def cup_cap_spectrum(pts):
    """(largest-cup-size, largest-cap-size) over subsets of pts, exact."""
    n = len(pts)
    best_cup = 0
    best_cap = 0
    for k in range(n, 0, -1):
        for combo in combinations(range(n), k):
            sub = [pts[i] for i in combo]
            if is_cup(sub):
                best_cup = max(best_cup, k)
            if is_cap(sub):
                best_cap = max(best_cap, k)
        if best_cup >= k and best_cap >= k:
            # both can only grow with smaller k-subsets checked below; but a
            # k-cup can still be found for a smaller k only if not already,
            # so short-circuit only when both reach potential max; harmless.
            pass
    return best_cup, best_cap


if __name__ == "__main__":
    from lib.esz import es_set_exact as es_set

    def show(name, pts):
        print(f"--- {name} ---")
        print(f"  points      : {len(pts)}")
        print(f"  general pos : {general_position(pts)}")
        kcx, ex = largest_convex_subset(pts)
        print(f"  largest convex subset : {kcx}")
        print(f"    (exemplar)          : {ex[:20]}{' ...' if len(ex) > 20 else ''}")
        print(f"  cup/cap spectrum      : {cup_cap_spectrum(pts)}")

    # moral equivalents of the hand examples (all exact)
    convex_4 = [(Fraction(0), Fraction(0)),
                (Fraction(2), Fraction(1)),
                (Fraction(4), Fraction(4)),
                (Fraction(1), Fraction(3))]
    quad_with_inside = [(Fraction(0), Fraction(0)),
                        (Fraction(4), Fraction(0)),
                        (Fraction(0), Fraction(4)),
                        (Fraction(1), Fraction(1))]

    print("== oracle self-checks on hand-computable cases ==")
    show("4 vertices of a square (in convex position)", convex_4)
    show("triangle + one interior point (NOT 4 in convex position)", quad_with_inside)

    print()
    print("== Erdos-Szekeres lower-bound construction (no convex n-gon at 2^(n-2) points) ==")
    for n in (3, 4, 5, 6):
        S = es_set(n)
        show(f"ES construction n={n} (expect maxConvex == {n - 1})", S)
