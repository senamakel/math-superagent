#!/usr/bin/env python3
"""Verify the naive oracle and the ES lower-bound construction.

Checks, all exact arithmetic (fractions.Fraction):

 (1) Convex-position predicate on hand-computable cases:
       - 4 points in convex position  -> largest convex subset == 4
       - triangle + 1 interior point  -> largest convex subset == 3
 (2) ES lower-bound construction at n=3..6:
       - set has 2^(n-2) points and is in general position
       - largest convex subset is n-1  (so NO convex n-gon)
     This is the construction of Thm 2.6 (Erdos-Szekeres 1961), and n=4,5,6
     correspond to the known 5/9/17 thresholds:
       - at n=4 : 4 points, no convex quad  (ES(4)=5)
       - at n=5 : 8 points, no convex pentagon (ES(5)=9)
       - at n=6 : 16 points, no convex hexagon (ES(6)=17)
 (3) The ES theorem's exact values are reproduced only in the sense that the
     oracle *reports* convex subsets; the full ES(N)=2^(N-2)+1 statement is
     a verification-bound exercise for another agent.  We only check the
     construction side (no convex n-gon at 2^(n-2) points), which the oracle
     can certify exactly.
"""
from fractions import Fraction
from brute import (general_position, convex_position, largest_convex_subset,
                   is_cup, is_cap, cup_cap_spectrum)
from lib.esz import es_set_exact

print("=" * 70)
print("CHECK 1: convex-position predicate on hand-computable cases")
print("=" * 70)

# 4 points in convex position (no 3 collinear)
sq = [(Fraction(0), Fraction(0)),
      (Fraction(2), Fraction(1)),
      (Fraction(4), Fraction(4)),
      (Fraction(1), Fraction(3))]
res = largest_convex_subset(sq)[0]
print(f"  4 points in convex position: largest convex subset = {res} (expect 4)")
assert res == 4, "FAIL: square should have 4 in convex position"

# triangle + one interior point -> no 4 in convex position
tri = [(Fraction(0), Fraction(0)),
       (Fraction(4), Fraction(0)),
       (Fraction(0), Fraction(4)),
       (Fraction(1), Fraction(1))]
res = largest_convex_subset(tri)[0]
print(f"  triangle + interior point: largest convex subset = {res} (expect 3)")
assert res == 3, "FAIL: triangle+interior should max at 3"

# Klein's 5-point theorem: ANY 5 general-position points contain a convex quad.
# This is the formulated ES(4)=5 lower... we check on our construction at n=5
# (8 points, 5 has a quad trivially).  We instead rely on the oracle's exact
# subset check for the construction below.

print()
print("=" * 70)
print("CHECK 2: ES lower-bound construction, no convex n-gon at 2^(n-2) points")
print("=" * 70)
for n in (3, 4, 5, 6):
    S = es_set_exact(n)
    expected_size = 2 ** (n - 2)
    k, ex = largest_convex_subset(S)
    print(f"  n={n}: |S|={len(S)} (expect {expected_size}) "
          f"general={general_position(S)} "
          f"largest convex subset={k} (expect {n - 1})  ->  "
          f"{'PASS' if (len(S)==expected_size and general_position(S) and k==n-1) else 'FAIL'}")
    assert len(S) == expected_size
    assert general_position(S), f"n={n} not in general position"
    assert k == n - 1, f"n={n}: construction contains a convex {k}-gon, expected max {n-1}"

print()
print("ALL ORACLE CHECKS PASSED")
