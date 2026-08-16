"""Shared helpers for es-nogon candidate modules.

Export two functions used by every candidate module:
  es_int(k)   -> the verified ES 2^{k-2}-point set as *integer* coords (no
                 convex k-gon, general position), i.e. harness's points(k).
  affine(pts, a,b,c,d,e,f) -> integer affine image
                 (x,y) -> (a*x+b*y+c, d*x+e*y+f).  An affine invertible map
                 is a bijection preserving collinearity and convexity exactly,
                 so an affine image of the ES set is STILL a no-convex-k-gon,
                 general-position integer set of the same size.

All arithmetic exact (Fractions -> integer LCM scaling), never floats.
"""

import math
from fractions import Fraction

from lib.es_construct import es_set


def to_ints(points):
    """Scale exact-Fraction points to integer coords (LCM of denominators)."""
    if not points:
        return []
    den = 1
    for (x, y) in points:
        den = math.lcm(den, Fraction(x).denominator)
        den = math.lcm(den, Fraction(y).denominator)
    return [(Fraction(x).numerator * (den // Fraction(x).denominator),
             Fraction(y).numerator * (den // Fraction(y).denominator))
            for (x, y) in points]


def es_int(k):
    """Integer-coordinate ES 2^{k-2}-point no-convex-k-gon set."""
    return to_ints(es_set(k))


def affine(pts, a, b, c, d, e, f):
    """Integer affine image (x,y) -> (a*x+b*y+c, d*x+e*y+f)."""
    return [(a * x + b * y + c, d * x + e * y + f) for (x, y) in pts]
