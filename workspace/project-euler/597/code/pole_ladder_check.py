#!/usr/bin/env python3
"""Verify the denominator-root (pole) ladder for the known exact closed forms.
Conjecture: p(n,L)=N(m)/D(m), m=L/40, has D with simple roots exactly at
   m = k/2  for  k = n-1, n, ..., 2n-3   (n-1 consecutive half-integers),
i.e. poles at L = 20(n-1), 20n, ..., 20(2n-3).
Check n=2,3,4 closed forms factor into these roots with nonzero numerators.
"""
from fractions import Fraction as F
from sympy import symbols, factor

m = symbols('m')
forms = {
  2: (m, 2*m-1),  # p2 = m/(2m-1)
  3: (7*m**2-17*m+12, 18*m**2-45*m+27),
  4: (19*m**3-119*m**2+244*m-162, 9*(m-2)*(2*m-5)*(2*m-3)),
}
for n,(num,den) in forms.items():
    D = factor(den)
    print(f"n={n}: D(m) = {D}")
    print(f"      expected pole set m = k/2, k={n-1}..{2*n-3} -> {[F(k,2) for k in range(n-1,2*n-2)]}")
    # roots of denominator polynomial
    from sympy import Poly, real_roots
    roots = real_roots(D, multiple=True)
    print(f"      actual real roots: {sorted(roots)}")
