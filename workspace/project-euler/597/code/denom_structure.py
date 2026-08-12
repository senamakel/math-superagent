#!/usr/bin/env python3
"""Analyse the number-theoretic structure of the EXACT reduced rational
p(n,L) across the L grid: factor reduced numerators & denominators of the
closed forms p(3,L)=(7m^2-17m+12)/(18m^2-45m+27) and
p(4,L)=(19m^3-119m^2+244m-162)/(9(m-2)(2m-5)(2m-3)).
Goal: detect a pattern in denominators (e.g. vanishing factors at half-integers,
shared factors, prime structure) that might extend to n=5,6,... """
from fractions import Fraction as F
import sys

def sympy(expr=None):
    pass

def factor_int(x):
    """small factor of integer (trial division)."""
    x = abs(int(x))
    if x < 2:
        return []
    facs = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            c = 0
            while x % d == 0:
                x //= d
                c += 1
            facs.append((d, c))
        d += 1 if d == 2 else 2
    if x > 1:
        facs.append((x, 1))
    return facs

def p3(m):
    m = F(m)
    return (7*m*m - 17*m + 12) / (18*m*m - 45*m + 27)

def p4(m):
    m = F(m)
    num = 19*m**3 - 119*m**2 + 244*m - 162
    den = 9*(m-2)*(2*m-5)*(2*m-3)
    return num/den

print("=== p(3,L) reduced denominators over m = L/40 ===")
for m in range(4, 25):
    v = p3(m)
    d = v.denominator
    print(f"  m={m:2d}  denom={d} = {'*'.join(f'{p}^{e}' if e>1 else str(p) for p,e in factor_int(d))}")

print("\n=== p(4,L) reduced denominators over m = L/40 ===")
for m in range(4, 25):
    v = p4(m)
    d = v.denominator
    print(f"  m={m:2d}  denom={d} = {'*'.join(f'{p}^{e}' if e>1 else str(p) for p,e in factor_int(d))}")
