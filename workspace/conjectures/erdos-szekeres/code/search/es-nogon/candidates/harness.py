#!/usr/bin/env python3
"""Template candidate module for the es-nogon scored search.

Exposes `points(k) -> list[(int, int)]`. A search program imports this module
(or any module shaped like it) and its scorer calls `points(k)`.

This template wraps the verified Erdős–Szekeres construction from
lib.es_construct.es_set(n), which produces 2^{n-2} points in *exact rational*
coordinates with no convex n-gon (verified: largest convex subset == n-1).
Because the scorer requires *integer* coordinates, we scale the rationals to
integers by multiplying every coordinate by the LCM of all denominators — this
is an (x,y) -> (Cx, Cy) scaling, which preserves collinearity and convexity
exactly, so `points(6)` still has no convex 6-gon and `points(7)` no convex
7-gon. The scorer's general-position and no-convex-k checks are then exact on
the integers.

A candidate that beats the record would return MORE than 2^{k-2} points (or
break the no-convex-k bound) and would be reported SCORE by the scorer — which
would be a real finding. This harness just provides the verified baseline.
"""

import math
from fractions import Fraction

from lib.es_construct import es_set


def _to_integer(points):
    """Scale exact-Fraction rational points to integer coords (LCM scaling).

    (x, y) -> (C*x, C*y) with C = lcm of all denominators.  An invertible
    linear scaling, so it is a bijection on the point set respecting
    collinearity and convexity exactly."""
    if not points:
        return []
    den = 1
    for (x, y) in points:
        den = math.lcm(den, Fraction(x).denominator)
        den = math.lcm(den, Fraction(y).denominator)
    return [(Fraction(x).numerator * (den // Fraction(x).denominator),
             Fraction(y).numerator * (den // Fraction(y).denominator))
            for (x, y) in points]


def points(k):
    """2^{k-2} integer points with no convex k-gon (verified baseline)."""
    # es_set supports k up to 7 (verified no 7-gon at k=7, 32 points).
    return _to_integer(es_set(k))


if __name__ == "__main__":
    import sys
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    pts = points(k)
    print("points(%d) -> %d integer points" % (k, len(pts)))
    print("sample:", pts[:3])
