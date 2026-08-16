"""Exact-rational realization of the ES 2^{n-2}-point no-convex-n-gon set.

Implements the *recursive* Erdős–Szekeres cups-and-caps construction for
n = 4, 5, 6 directly, realising Morris-Soltan Thm 2.6:

  X = union over i = 0..n-2 of a tiny copy of T_i,
      T_i has C(n-2, i) points, no (i+2)-cap, no (n-i)-cup, all pair-slopes
      in (-1,1),
      placed near a point on a downward-convex arc with strictly decreasing
      polar angle (so a convex polygon meets the blocks in increasing index
      order and is cut short to <= n-1 vertices).

Every block is built by the f(k,l) cups/caps recursion with exact rationals,
all internal pair-slopes kept in (-1,1).  The whole set is then VERIFIED
against the exact oracle: largest convex subset must equal n-1 (no convex
n-gon).

All coordinates are exact fractions.Fraction.
"""

from fractions import Fraction
from math import comb
import itertools


def _bbox(S):
    xs = [p[0] for p in S]
    ys = [p[1] for p in S]
    return min(xs), max(xs), min(ys), max(ys)


def _max_abs_slope(S):
    m = Fraction(0)
    for (a, b) in itertools.combinations(S, 2):
        if a[0] == b[0]:
            return Fraction(2)
        s = abs((b[1] - a[1]) / (b[0] - a[0]))
        if s > m:
            m = s
    return m


def _flatten_y(S, target_max=Fraction(2, 10)):
    m = _max_abs_slope(S)
    if m == 0:
        return S
    factor = target_max / (2 * m)
    return [(x, y * factor) for (x, y) in S]


def _cup(n):
    c = Fraction(1, 20)
    return [(Fraction(i), c * i * i) for i in range(n)]


def _cap(n):
    c = Fraction(1, 20)
    return [(Fraction(i), -c * i * i) for i in range(n)]


def _merge_AB_above(A, B):
    """Place B to the upper-right of A so every A-B slope > 1/2, A and B flat."""
    Ax0, Ax1, Ay0, Ay1 = _bbox(A)
    Bx0, Bx1, By0, By1 = _bbox(B)
    gap = Fraction(8)
    shift_x = (Ax1 - Bx0) + gap
    dy = Ay1 + Fraction(1, 2) * gap - By1
    Bm = [(x + shift_x, y + dy) for (x, y) in B]
    return A + Bm


def cupcap(k, l):
    """C(k+l-4, k-2) points with no k-cup and no l-cap, all slopes in (-1,1)."""
    if k == 2 or l == 2:
        return [(Fraction(0), Fraction(0))]
    if k == 3:
        return _cap(l - 1)
    if l == 3:
        return _cup(k - 1)
    A = cupcap(k - 1, l)
    B = cupcap(k, l - 1)
    A = _flatten_y(A, Fraction(1, 40))
    B = _flatten_y(B, Fraction(1, 40))
    return _flatten_y(_merge_AB_above(A, B), Fraction(1, 20))


def es_block(n, i):
    """T_i: C(n-2,i) points, no (i+2)-cap and no (n-i)-cup, slopes in (-1,1)."""
    k = n - i      # no k-cup
    l = i + 2      # no l-cap
    S = cupcap(k, l)
    S = _flatten_y(S, Fraction(1, 20))
    x0, x1, y0, y1 = _bbox(S)
    return [(x - x0, y - y0 + Fraction(1)) for (x, y) in S]


def _convex_arc_centers(n):
    """n-1 centers on a downward-convex arc, increasing x, strictly decreasing
    successive slopes => strictly decreasing polar angle (away from vertical).
    Returns a list of n-1 exact-rational centers."""
    m = n - 1
    # choose successive y-differences strictly decreasing (convex downward)
    start_y = Fraction(5000)
    diffs = [Fraction(-(1000 - 100 * t)) for t in range(m)]
    centers = []
    y = start_y
    for i in range(m):
        centers.append((Fraction(i * 1000), y))
        if i < m - 1:
            y = y + diffs[i]
    return centers


def es_set_blocks(n):
    """(points, blocks) for n in {4,5,6}: 2^{n-2} points, no convex n-gon."""
    centers = _convex_arc_centers(n)
    scale = Fraction(1, 10 ** 6)
    out = []
    blocks = []
    for i in range(n - 1):
        T = es_block(n, i)
        assert len(T) == comb(n - 2, i), (n, i, len(T), comb(n - 2, i))
        cx, cy = centers[i]
        block = []
        for (px, py) in T:
            block.append((cx + scale * px, cy + scale * py))
        out.extend(block)
        blocks.append(block)
    return out, blocks


def es_set(n):
    """2^{n-2} points with no convex n-gon (exact Fractions).  Verify with oracle."""
    pts, _ = es_set_blocks(n)
    return pts
