"""Exact cup/cap predicates and the cup-cap convex-position characterization.

Cups and caps are defined on a set with distinct x-coordinates, after sorting
by x.  A *k-cup* is k points whose consecutive slopes (segment slopes between
x-adjacent points of the subset) are strictly increasing; a *k-cap* is k points
whose consecutive slopes are strictly decreasing.  All comparisons are exact
(no floats): slopes are compared by cross-multiplication of reduced (dy, dx)
pairs, so Fraction/int coordinate rings are both supported.

The classical claim (G-cupcap, Erdos-Szekeres 1935) is that a plane point set
X in general position with distinct x contains n points in convex position iff
there is k in {2..n} and a k-cup C plus an (n+2-k)-cap D in X that share their
leftmost and rightmost points (by x) and whose union is n points in convex
position.  The functions here build that predicate exactly; the oracle check
that tests both directions for every small set lives in code/cupcap/verify.py.

Standard shape used throughout: a k-cup is the strictly-convex lower chain
(concave-up, increasing slopes) between its two x-extreme points, and a k-cap
is the strictly-concave upper chain (decreasing slopes).  A convex n-gon is the
union of one cup and one cap sharing its leftmost and rightmost vertices.
"""

from fractions import Fraction
from itertools import combinations
from lib.es_geom import in_convex_position

# ---------------------------------------------------------------------------
# exact slope comparison
# ---------------------------------------------------------------------------

def _slope_pair(a, b):
    """Exact reduced (dy, dx) with dx>0; requires dx != 0 (distinct x)."""
    ax, ay = a
    bx, by = b
    dx = Fraction(bx) - Fraction(ax)
    dy = Fraction(by) - Fraction(ay)
    if dx == 0:
        raise ValueError("distinct x-coordinates required for cup/cap slope")
    return dy / dx


def _sorted_by_x(sub):
    return sorted(sub, key=lambda p: Fraction(p[0]))


def is_cup(sub):
    """True iff `sub` (>=2 points, distinct x) is a k-cup: strictly increasing
    consecutive slopes after sorting by x.  Exact rational comparison."""
    pts = _sorted_by_x(sub)
    if len(pts) < 3:
        return len(pts) >= 2
    slopes = [_slope_pair(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    return all(slopes[i] < slopes[i + 1] for i in range(len(slopes) - 1))


def is_cap(sub):
    """True iff `sub` (>=2 points, distinct x) is a k-cap: strictly decreasing
    consecutive slopes after sorting by x.  Exact rational comparison."""
    pts = _sorted_by_x(sub)
    if len(pts) < 3:
        return len(pts) >= 2
    slopes = [_slope_pair(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    return all(slopes[i] > slopes[i + 1] for i in range(len(slopes) - 1))


# ---------------------------------------------------------------------------
# the G-cupcap predicate
# ---------------------------------------------------------------------------

def _extreme_x_indices(pts, sub_idxs):
    """(min index, max index) by x over the given index subset."""
    xs = [Fraction(pts[i][0]) for i in sub_idxs]
    lo = sub_idxs[xs.index(min(xs))]
    hi = sub_idxs[xs.index(max(xs))]
    return lo, hi


def exists_cupcap(X, n):
    """True iff there is k in {2..n} and a k-cup C plus an (n+2-k)-cap D in X
    sharing their leftmost and rightmost points by x, whose union is exactly n
    points in convex position.  Matches the G-cupcap claim exactly.

    Brute force over all subsets (fine for the small sizes here)."""
    pts = list(X)
    m = len(pts)
    by_x = sorted(range(m), key=lambda i: Fraction(pts[i][0]))
    # collect all cup subsets and cap subsets (as frozensets of indices)
    cups = {}   # frozenset -> True (a cup)
    caps = {}   # frozenset -> True (a cap)
    for k in range(2, n + 1):
        for combo in combinations(range(m), k):
            sub = [pts[i] for i in combo]
            fs = frozenset(combo)
            if is_cup(sub):
                cups[fs] = True
            if is_cap(sub):
                caps[fs] = True
    for k in range(2, n + 1):
        dl = n + 2 - k                    # required size of the cap
        for C in cups:
            if len(C) != k:
                continue
            for D in caps:
                if len(D) != dl:
                    continue
                loC, hiC = _extreme_x_indices(pts, list(C))
                loD, hiD = _extreme_x_indices(pts, list(D))
                if loC == loD and hiC == hiD:
                    # sizes + shared extremes force |C u D| == n exactly
                    union = C | D
                    if len(union) == n:
                        union_pts = [pts[i] for i in sorted(union, key=lambda i: Fraction(pts[i][0]))]
                        if in_convex_position(union_pts):
                            return True
    return False


def convex_by_cupcap(X):
    """Returns the largest n in {3..|X|} for which exists_cupcap(X, n) is true
    (so 0 if none).  Compare against largest_convex_subset(X)."""
    m = len(X)
    for n in range(m, 2, -1):
        if exists_cupcap(X, n):
            return n
    return 0


def shared_extreme_nonconvex_pairs(X, n):
    """Diagnostic: count of (cup C size k, cap D size n+2-k) pairs sharing
    leftmost and rightmost indices whose union is exactly n points but is NOT
    in convex position.  A nonzero count means 'sharing extremes' alone does
    not force convexity and the explicit convex check matters (as the claim
    states)."""
    pts = list(X)
    m = len(pts)
    bad = 0
    total = 0
    cups = {}
    caps = {}
    for k in range(2, n + 1):
        for combo in combinations(range(m), k):
            sub = [pts[i] for i in combo]
            fs = frozenset(combo)
            if is_cup(sub):
                cups.setdefault(k, []).append(fs)
            if is_cap(sub):
                caps.setdefault(k, []).append(fs)
    for k in range(2, n + 1):
        dl = n + 2 - k
        for C in cups.get(k, []):
            for D in caps.get(dl, []):
                loC, hiC = _extreme_x_indices(pts, list(C))
                loD, hiD = _extreme_x_indices(pts, list(D))
                if loC == loD and hiC == hiD:
                    union = C | D
                    if len(union) == n:
                        total += 1
                        union_pts = [pts[i] for i in sorted(union, key=lambda i: Fraction(pts[i][0]))]
                        if not in_convex_position(union_pts):
                            bad += 1
    return bad, total
