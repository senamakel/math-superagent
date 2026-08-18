#!/usr/bin/env python3
"""Exact factorization of the Bautin focal-value clearing denominators.

D_d = gcd-clearing denominator of L_d (chart family, 5 params), d = 4..14:
  [8, 192, 18432, 1105920, 22295347200, 37456183296000]
Report prime factorizations and look for a closed multiplicative form.
Exact integer arithmetic only.
"""
import sympy as sp

Ds = [8, 192, 18432, 1105920, 22295347200, 37456183296000]
ds = [4, 6, 8, 10, 12, 14]

print("d     D_d                     factorization")
for d, D in zip(ds, Ds):
    fac = sp.factorint(D)
    s = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(fac.items()))
    print(f"{d:2d}  {D:16d}   {s}")

# ratios
print("\nratios D_{d+2}/D_d:")
prev = None
for D in Ds:
    if prev is not None:
        r = D // prev
        print(f"  {r}  = {sp.factorint(r)}")
    prev = D

# even/odd split of the indices: D depends on d, look at consecutive ratios only
print("\nvaluation vectors (v2, v3, v5, v7):")
for d, D in zip(ds, Ds):
    fac = sp.factorint(D)
    v = tuple(fac.get(p, 0) for p in (2, 3, 5, 7))
    print(f"  d={d:2d}: {v}")