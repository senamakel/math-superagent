"""Exact planar geometry oracle for the Erdos-Szekeres problem.

All coordinates are exact integers (or rationals given as integer pairs), so
every orientation and convexity test is exact arithmetic -- never floating
point.  This is the module every construction must be checked against.

Functions
---------
orient(a, b, c)
    Exact sign of the oriented area (cross product) of points a,b,c.
    Returns +1/-1/0.  Points are (x, y) tuples.
collinear(a, b, c)
    True iff a,b,c are collinear (exact).
in_general_position(points)
    True iff no three of the given points are collinear.
convex_hull(points)
    The vertex list of the convex hull (Andrew monotone chain), CCW.
    Exact integer arithmetic throughout.
in_convex_position(subset)
    True iff the points (>=3, in general position) are exactly the vertices
    of a convex polygon (all of them hull-vertices of the subset).
largest_convex_subset(points)
    Exact largest k such that some k of the points lie in convex position.
    Brute force over 2**N subsets (fine for N <= ~20).  Returns (k, witness).
has_convex_k_subset(points, k)
    Returns (True, witness) if some k points lie in convex position, else
    (False, None).  Enumerates C(N,k) subsets -- the right tool for
    N = 32 (n = 7) where 2**N is impossible.
side_of_line(line, p)
    Which open half-plane p is in, under the line given as (a, b) or as an
    implicit line described by the point pair defining it.
count_by_side(line, points)
    counts on each open side of the line (and how many are exactly on it).

The convexity facts used (classical, in research/CLAIMS.md):
  * n points are in convex position iff every 4 of them form a convex
    quadrilateral (es35-four-criterion);
  * a subset is in convex position iff all its points are hull-vertices.
A direct hull test of each candidate subset is exact and independent of the
4-criterion, so it doubles as a check on that criterion.
"""

from itertools import combinations


def orient(a, b, c):
    """Sign of the oriented area of triangle (a,b,c): +1 CCW, -1 CW, 0 flat."""
    ax, ay = a
    bx, by = b
    cx, cy = c
    v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0


def collinear(a, b, c):
    return orient(a, b, c) == 0


def in_general_position(points):
    for i, j, k in combinations(range(len(points)), 3):
        if collinear(points[i], points[j], points[k]):
            return False
    return True


def convex_hull(points):
    """Andrew monotone chain; returns hull vertices CCW, integer exact."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def in_convex_position(subset):
    """True iff subset (general position assumed by caller) is a convex polygon."""
    n = len(subset)
    if n < 3:
        # Degenerate: 1 or 2 points do not form a polygon.  Caller decides
        # whether it counts as 'convex position'.
        return False
    # All points must be extreme vertices of their own hull.
    return len(convex_hull(subset)) == n


def largest_convex_subset(points):
    """Exact largest convex subset via brute force over subsets, largest first.

    Starts at the biggest candidate size and returns the first convex subset
    found, so it is exact.  Fine for N <= ~20 (2**N subsets).  A subset of size
    3 that is not in convex position cannot happen in general position, so the
    answer is always >= 3 for N >= 3 general-position input.  Returns
    (k, witness_subset)."""
    pts = list(points)
    N = len(pts)
    for r in range(N, 2, -1):
        for comb in combinations(range(N), r):
            sub = [pts[i] for i in comb]
            if in_convex_position(sub):
                return (r, sub)
    return (0, None)


def has_convex_k_subset(points, k):
    """True + witness if some k points are in convex position. Brute C(N,k)."""
    pts = list(points)
    if k < 3:
        return (True, [] if k == 1 else (pts[:2] if len(pts) >= 2 else None))
    for comb in combinations(range(len(pts)), k):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            return (True, sub)
    return (False, None)


def _slope(a, b):
    """Exact reduced slope (dy, dx) with dx>0; None if dx==0 (vertical)."""
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    if dx == 0:
        return None
    if dx < 0:
        dx, dy = -dx, -dy
    g = _gcd(abs(dx), abs(dy))
    return (dy // g, dx // g)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def longest_cup(points):
    """Length of the longest cup (strictly increasing consecutive slopes),
    points taken in increasing x-order.  Exact rational slope comparison."""
    pts = sorted(points, key=lambda p: p[0])
    m = len(pts)
    if m == 0:
        return 0
    # best[i] = (max_len, min_last_slope) for cup ending at i (in x-order)
    NEG = None
    best = [(1, NEG)] * m
    for i in range(m):
        best_i = (1, NEG)
        for j in range(i):
            s = _slope(pts[j], pts[i])
            if s is None:
                continue
            lj, last = best[j]
            ok = True
            if last is not None:
                # need s > last (exact)
                ok = s[0] * last[1] > last[0] * s[1]
            if ok:
                cand = (lj + 1, s)
                if cand[0] > best_i[0] or (cand[0] == best_i[0] and
                                           (best_i[1] is None or cand[1][0] * best_i[1][1] < best_i[1][0] * cand[1][1])):
                    best_i = cand
        best[i] = best_i
        # also carry forward: a cup can skip index i
    return max(l for l, _ in best)


def longest_cap(points):
    """Length of the longest cap (strictly decreasing consecutive slopes)."""
    pts = sorted(points, key=lambda p: p[0])
    m = len(pts)
    if m == 0:
        return 0
    NEG = None
    best = [(1, NEG)] * m
    for i in range(m):
        best_i = (1, NEG)
        for j in range(i):
            s = _slope(pts[j], pts[i])
            if s is None:
                continue
            lj, last = best[j]
            ok = True
            if last is not None:
                ok = s[0] * last[1] < last[0] * s[1]   # s < last
            if ok:
                cand = (lj + 1, s)
                if cand[0] > best_i[0] or (cand[0] == best_i[0] and
                                           (best_i[1] is None or cand[1][0] * best_i[1][1] > best_i[1][0] * cand[1][1])):
                    best_i = cand
        best[i] = best_i
    return max(l for l, _ in best)


def side_of_line(pair, p):
    """Sign of p relative to the oriented line through pair[0], pair[1]."""
    a, b = pair
    return orient(a, b, p)


def count_by_side(line, points):
    """Count points strictly to each open side of the line, and on it.

    line is a pair of points defining the line (the two points need not be in
    `points`); the count is independent of which direction 'left'/'right' is.
    Returns (L, R, on) with L+R+on == len(points)."""
    a, b = line
    L = R = on = 0
    for p in points:
        if collinear(a, b, p):
            on += 1
        elif orient(a, b, p) > 0:
            L += 1
        else:
            R += 1
    return L, R, on


# ---------------------------------------------------------------------------
# API aliases matching the tool-request names
# ---------------------------------------------------------------------------

def general_position(points):
    """Alias for in_general_position: True iff no three points are collinear."""
    return in_general_position(points)


def cups_caps(points):
    """(longest cup, longest cap) over the x-sorted point set, exact.

    A cup is a subsequence (in x-order) with strictly increasing consecutive
    slopes; a cap one with strictly decreasing consecutive slopes.  Uses the
    exact rational-slope DP in longest_cup / longest_cap."""
    return longest_cup(points), longest_cap(points)
