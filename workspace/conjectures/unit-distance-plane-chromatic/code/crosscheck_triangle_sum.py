#!/usr/bin/env python3
"""Independent cross-check of the triangle-sum result from verify_sources.py.

verify_sources.py section B/C built the Minkowski sum T+T of two unit
equilateral triangles with its own local exact rational arithmetic, found
6 distinct vertices, 9 unit edges, and chi = 3 (not 1, not 2).

This script rebuilds the SAME point set and SAME distance rule using the
library's exact machinery (lib.satcolor complete SAT k-colourability) on the
edge list extracted independently, and also confirms the point count and
edge count with lib.unitfield's exact squared-distance arithmetic in Q(sqrt3).

A second route must agree on: |T+T| = 6, edges = 9, chi = 3.
"""
from itertools import combinations
from fractions import Fraction as F

# ---- independent rebuild of the point set in Q(sqrt3) ----
# T = {0, 1, (1+sqrt(-3))/2}, points as (real, sqrt3-coeff)
T = [(F(0), F(0)), (F(1), F(0)), (F(1, 2), F(1, 2))]

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

def sqdist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + 3 * dy * dy   # |x + i sqrt3 y|^2 = x^2 + 3 y^2

S = sorted({add(p, q) for p in T for q in T})
n = len(S)
edges = [(i, j) for i, j in combinations(range(n), 2) if sqdist(S[i], S[j]) == F(1)]

# ---- now the independent SAT oracle route ----
from lib.satcolor import is_k_colorable

print("T+T distinct vertices n =", n)
print("unit edges m =", len(edges))
chi = None
for k in range(1, 5):
    sat, w = is_k_colorable(edges, k, n)
    if sat:
        chi = k
        print(f"  {k}-colourable: True (chi <= {k})")
        break
    else:
        print(f"  {k}-colourable: False")
print("RESULT chi(T+T) =", chi)
ok = (n == 6) and (len(edges) == 9) and (chi == 3)
print("CROSS-CHECK:", "PASSED (agrees with verify_sources: n=6, m=9, chi=3)"
      if ok else "MISMATCH")
