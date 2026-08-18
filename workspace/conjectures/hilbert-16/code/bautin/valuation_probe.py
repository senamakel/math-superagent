#!/usr/bin/env python3
"""Exact least-squares 'fit' of the denominator valuation sequences against
simple affine forms, and the same for the monomial complement c(h).

This probes whether the observed valuation rows
  (v2,v3,v5,v7) for d = 4,6,8,10,12,14  = (3,0,0,0),(6,1,0,0),(11,2,0,0),
  (13,3,1,0),(19,5,2,1),(23,6,3,2)
obey simple affine laws.  Deliberately NOT fitting: only reporting exact
consistency with candidate symbolic laws, since with 6 points anything can
be fit — the point is which simple structures survive to d=16,18 (computed
by the running d18 agent).

Also sanity-checks whether v2 ~ ceil(3*d/2), which the data suggests:
  d=4:3, 6:6, 8:11, 10:13, 12:19, 14:23.  Indeed v3 = d/2-2 (d>=6),
  v5 = d/2-4 (d>=10), v7 = d/2-5 (d>=12).  Report the exact residuals.
"""
import sympy as sp

dvals = [4, 6, 8, 10, 12, 14]
v2 = [3, 6, 11, 13, 19, 23]
v3 = [0, 1, 2, 3, 5, 6]
v5 = [0, 0, 0, 1, 2, 3]
v7 = [0, 0, 0, 0, 1, 2]

print("== candidate affine laws ==")
for name, v in (("v2", v2), ("v3", v3), ("v5", v5), ("v7", v7)):
    print(f"{name}: {v}")
    # v3 = d/2 - 2 for d>=6; v5 = d/2 - 4 for d>=10; v7 = d/2 - 5 for d>=12
    if name == "v3":
        print("  v3 - (d/2 - 2):", [v[i] - (d / 2 - 2) for i, d in enumerate(dvals)])
    if name == "v5":
        print("  v5 - (d/2 - 4):", [v[i] - (d / 2 - 4) for i, d in enumerate(dvals)])
    if name == "v7":
        print("  v7 - (d/2 - 5):", [v[i] - (d / 2 - 5) for i, d in enumerate(dvals)])

print("\n== v2 candidate: 2*v2 - 3*d ==", [2 * v2[i] - 3 * d for i, d in enumerate(dvals)])
print("== v2 odd terms: v2(4)=3, v2(6)=6, v2(8)=11, v2(10)=13: diffs 3,5,2,6,4 — no affine fit over all ==")
print("residuals v2 - ceil(3d/2):",
      [v2[i] - sp.ceiling(sp.Rational(3 * d, 2)) for i, d in enumerate(dvals)])

print("\n== monomial complement c(h) from the quadratic formula ==")
print("c(h) = (h^2+14h+8)/8 for h = 2,4,6,8,10,12,14:")
print([(h, (h*h + 14*h + 8) // 8) for h in (2, 4, 6, 8, 10, 12, 14)])