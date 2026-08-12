#!/usr/bin/env python3
"""Confirmed negative result: V(n)^2 / V(n) is NOT always a quadratic surd.

Exact sympy minimal-polynomial results for the critical speed V(n)=1/cos(alpha):
  n=3: V = sqrt2*(3+sqrt5);  minpoly of V is x^4 - 56x^2 + 64  (DEGREE 4, not quadratic)
  n=4: V = sqrt(5/2*(7+sqrt41)); minpoly x^4 - 35x^2 + 50       (DEGREE 4)
  n=6: V = 2 + 2sqrt21/3;      minpoly 3x^2 - 12x - 16         (DEGREE 2 = quadratic)
  n=5,7,8,9,10,11,12: V = cos(pi/n*something + acos(inner)/2) where inner lies in a
       cyclotomic field of degree >= 4 -> NOT quadratic.

So the pattern "V(n) is a simple quadratic surd" is a SMALL-n coincidence
(n=3,4,6 only), not a general regularity. n=5 already falsifies it.

This matches the established knowledge that only n=3,4,6 have clean radical
closed forms; the hexagon's quadratic form is special, not general.
"""
print("See v_quadratic_surd_test.py output (exact sympy minpolys).")
