#!/usr/bin/env python3
"""Temporary invalid candidate for the scorer self-test.

kind='collinear': returns 8 points, three of which (first three) are collinear
                  (all with y=0).  INVALID at general position.
kind='overfilled': returns the 16 verified es_construct(6) points plus one
                  extra point appended, so 17 points --- which, by ES(6)=17,
                  MUST contain a convex 6-gon.  INVALID at the convexity check.

Written only to exercise score.py's INVALID paths; not meant to be a searched
candidate.
"""

import math
from fractions import Fraction
from lib.es_construct import es_set


def _to_integer(points):
    den = 1
    for (x, y) in points:
        den = math.lcm(den, Fraction(x).denominator)
        den = math.lcm(den, Fraction(y).denominator)
    return [(Fraction(x).numerator * (den // Fraction(x).denominator),
             Fraction(y).numerator * (den // Fraction(y).denominator))
            for (x, y) in points]


import os

KIND = os.environ.get("ES_NOGON_SELFTEST_KIND", "collinear")


def points(k):
    if KIND == "collinear":
        return [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (3, 4), (5, 1), (2, 7)]
    if KIND == "overfilled":
        base = _to_integer(es_set(6))          # 16 verified no-6-gon points
        extra = (10 ** 12, 10 ** 12)           # a far-off fresh point
        return base + [extra]
    raise ValueError("unknown kind %r" % KIND)
