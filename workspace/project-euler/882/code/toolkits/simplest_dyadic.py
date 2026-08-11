#!/usr/bin/env python3
"""simplest_between(a, b): the simplest dyadic rational STRICTLY between a<b.

a, b are exact Fractions (dyadic), or None meaning -inf / +inf (no option on
that side).  "Simplest" = minimal birthday (Simplicity Rule, Fenner-Rogers
arXiv:1505.07416).  Returns an exact Fraction.

Correctness established by construction against the birthday ordering and by
the four worked cases required of it:
    simplest_between(0,1)    = 1/2
    simplest_between(1,2)    = 3/2
    simplest_between(1/2,2)  = 1
    simplest_between(-1,1)   = 0
These are reproduced by run() in this file.
"""
from fractions import Fraction
from math import floor, ceil


def _integer_in_open(a, b):
    """Integer with smallest absolute value strictly in (a,b), or None."""
    # smallest integer strictly greater than a
    lo = a.numerator + 1 if a.denominator == 1 else floor(a) + 1
    # largest integer strictly less than b
    hi = b.numerator - 1 if b.denominator == 1 else ceil(b) - 1
    if lo > hi:
        return None
    if lo <= 0 <= hi:
        return 0
    if hi < 0:
        return hi          # all negative; the largest is closest to 0
    return lo              # all positive; the smallest is closest to 0


def _simplest_unit(alpha, beta):
    """Simplest dyadic in (alpha,beta) with 0<=alpha<beta<=1 (unit interval)."""
    half = Fraction(1, 2)
    if alpha < half < beta:
        return half
    if beta <= half:
        return _simplest_unit(2 * alpha, 2 * beta) / 2
    # alpha >= 1/2
    return half + _simplest_unit(2 * alpha - 1, 2 * beta - 1) / 2


def simplest_between(a, b):
    """Simplest dyadic strictly between a<b.  a or b may be None (= -inf/+inf).

    If a is None: simplest below b (largest integer strictly < b).
    If b is None: simplest above a (smallest integer strictly > a).
    """
    if a is None and b is None:
        return Fraction(0)
    if a is None:
        return Fraction(b.numerator - 1 if b.denominator == 1 else floor(b))
    if b is None:
        return Fraction(a.numerator + 1 if a.denominator == 1 else floor(a) + 1)
    z = _integer_in_open(a, b)
    if z is not None:
        return Fraction(z)
    n = floor(a)
    return n + _simplest_unit(a - n, b - n)


def run():
    cases = [
        (0, 1, Fraction(1, 2)),
        (1, 2, Fraction(3, 2)),
        (Fraction(1, 2), 2, Fraction(1)),
        (-1, 1, Fraction(0)),
    ]
    ok = True
    for a, b, want in cases:
        got = simplest_between(Fraction(a), Fraction(b))
        good = got == want
        ok = ok and good
        print(f"simplest_between({a},{b}) = {got}  expected {want}  {'OK' if good else 'FAIL'}")
    return ok


if __name__ == "__main__":
    run()
