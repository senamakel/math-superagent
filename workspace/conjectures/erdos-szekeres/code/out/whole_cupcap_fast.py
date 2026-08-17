#!/usr/bin/env python3
"""Fast independent whole-set cap/cup check for es_construct at larger n.

A cap = subset with strictly decreasing consecutive slopes (in x order);
longest cap >= 3 iff there exist x_a < x_b < x_c with slope(a,b) > slope(b,c).
A cup = subset with strictly increasing consecutive slopes; longest cup >= k
iff some k points with x increasing form a strictly-concave chain.

We want: does the WHOLE set contain a cap of length >=3? (cap answer should
be 2 for all n.) And what is the longest cup? (should be n-1.)

Slopes computed with exact Fraction reducer via self-reduction; O(m^2).
"""
from fractions import Fraction
from lib.es_construct import es_set


def cross(a, b, c):
    """sign of orient(a,b,c): >0 is counterclockwise."""
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def has_cap3(S):
    """True if some 3 points in x-order form a descending convex chain (a cap).
    Uses: p_a < p_b < p_c in x is a cap-3 iff orient(a,b,c) < 0 with x_a<x_b<x_c
    where orient(a,b,c) = (b-a)x(c-a).  Check: slopes s_ab > s_bc  <=>
    (yb-ya)/(xb-xa) > (yc-yb)/(xc-xb)  <=> orientation negative."""
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    for b in range(1, m - 1):
        B = pts[b]
        for a in range(b):
            A = pts[a]
            for c in range(b + 1, m):
                if cross(A, B, pts[c]) < 0:
                    return True
    return False


def longest_cup(S):
    """Longest strictly-increasing-slope chain in x order (cup)."""
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    from math import gcd
    def slope(i, j):
        dx = pts[j][0] - pts[i][0]
        dy = pts[j][1] - pts[i][1]
        g = gcd(abs(dx.numerator * dx.denominator), abs(dy.numerator * dy.denominator))
        return (dy / dx) if dx != 0 else None  # Fraction exact
    best = [1] * m
    last = [None] * m
    for i in range(m):
        for j in range(i):
            s = slope(j, i)
            if s is None:
                continue
            if last[j] is None or s > last[j]:
                cand = best[j] + 1
                if cand > best[i] or (cand == best[i] and last[i] is None) or (cand == best[i] and last[i] is not None and s > last[i]):
                    if cand > best[i] or last[i] is None or s > last[i]:
                        best[i] = cand
                        last[i] = s
    return max(best)


for n in (11, 12, 13):
    S = es_set(n)
    m = len(S)
    c3 = has_cap3(S)
    cu = longest_cup(S)
    print(f"n={n}: |S|={m} cap3? {c3}  (cap constant 2 => expect False) "
          f"longest_cup={cu} (expect n-1={n-1}) -> {'OK' if (not c3 and cu==n-1) else 'DIFF'}")
