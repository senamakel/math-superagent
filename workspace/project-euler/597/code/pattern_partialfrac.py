#!/usr/bin/env python3
"""Examine the closed forms p(n,L) for n=2,3,4 as rational functions in m=L/40.
Expresses them in normalized form and computes partial-fraction decomposition
in terms of (2m-k) to look for a cross-n residue pattern."""
from sympy import symbols, apart, factor, simplify, Rational

m = symbols('m')

forms = {
    2: (m, 2*m - 1),
    3: (Rational(7)*m**2 - 17*m + 12, 9*(m-1)*(2*m-3)),
    4: (19*m**3 - 119*m**2 + 244*m - 162, 9*(m-2)*(2*m-5)*(2*m-3)),
}

print("Partial fraction decompositions (in m):")
for n,(num,den) in forms.items():
    r = num/den
    print(f"\nn={n}:  p(n,m) = {factor(r)}")
    print(f"   apart = {apart(r)}")

# Express roots in the "k/2" ladder form: factor as product over k of (2m-k)
print("\n\nDenominator factorizations in (2m-k) form:")
for n,(num,den) in forms.items():
    print(f"  n={n}: den = {factor(den)}")

# Compare resize: partial fractions grouped by k in denominator (2m-k)
print("\n\nPartial fractions with denominators (2m - k):")
for n,(num,den) in forms.items():
    r = num/den
    # clear denominators to (2m-k) products
    # n=3 roots k=2,3; n=4 roots k=3,4,5
    print(f"  n={n}: p = {apart(r)}")
