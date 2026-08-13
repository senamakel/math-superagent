#!/usr/bin/env python3
"""Verify the run's computed genus closed forms against the LITERATURE formula
for superelliptic curves y^m = f(x) with f squarefree of degree d:

    g = ((d-2)(m-1) + m - gcd(m,d)) / 2

(Sutherland, "Counting points on superelliptic curves in average polynomial
time", Open Book Series 4 (2020), eq. (1); Wikipedia "Superelliptic curve",
Ramification/Genus section, general form g = 1/2 ( m(|B|-2) - sum_alpha
(m,r_alpha) ) + 1.)

Claim: for the curves C(x,k1) = C(y,k2) the small-column rows are
    k2=2 (pairs {2,n}): y(y-1) = 2 C(x,n)          ->  g = floor((n-1)/2)
    k2=3 (pairs {3,n}): Y^3 - Y = 6 C(x,n)         ->  g = n-1 (3 ∤ n), n-2 (3|n)
    k2=4 (pairs {4,n}): 2:1 cover of w^2=1+24C(x,n)->  g = floor(3(n-1)/2) variant

This checker immediately checks: (i) the literature formula evaluates to integer
matching the recorded {3,n} closed form for all n in the computed range, and
(ii) {2,n} hyperelliptic row matches the same formula. The {4,n} row is a 2:1
cover of a hyperelliptic curve, so the plain superelliptic formula does not
apply directly to it — the cover genus must be recomputed separately; this run
only checks {2,n} and {3,n}, and reports {4,n} as needing a cover computation.

Also verifies the literature formula against the RECORDED table values
genus(3,k1) and genus(2,k1) for k1 = 4..24 (k2=3 row) and k1 = 3..12 (k2=2 row)
from code/genus/full_grid.sing / genus_table.py.

The relevant curve: C(x,k1) = C(y,k2) is a superelliptic curve in the variable
x when the other variable is solved for... specifically, for {3,n}: viewing the
affine model C(x,3) = C(y,n) as a curve; the recorded closed form came from
Singular. This script ONLY verifies the claimed closed forms and the literature
genus formula on the small-column {2,n} and {3,n} families.
"""

import math

def genus_superelliptic(m, d):
    """g = ((d-2)(m-1) + m - gcd(m,d)) / 2 for y^m = f(x), deg f = d squarefree."""
    return ((d - 2) * (m - 1) + m - math.gcd(m, d)) // 2

def closed_genus_3n(n):
    """Claimed closed form for the {3,n} family: g = n-1 if 3 ∤ n else n-2."""
    return n - 1 if n % 3 else n - 2

def closed_genus_2n(n):
    """Claimed closed form for the {2,n} family: g = floor((n-1)/2)."""
    return (n - 1) // 2

# The {3,n} family: C(x,3) = C(y,n). Affine model in the variable whose column
# is 3. For a cyclic-trigonal curve Y^3 - Y = 6 C(x,n), the polynomial on the
# right has degree n in x, so m=3, d = n. That is a superelliptic curve
# (trigonal = m=3), so the literature formula should give the genus if the
# right-hand polynomial is squarefree.
print("== {3,n} family: trigonal y^3 = f_n(x), f_n = 6 C(x,n), deg f_n = n ==")
mismatches = 0
for n in range(4, 25):
    lit = genus_superelliptic(3, n)
    claim = closed_genus_3n(n)
    status = "OK " if lit == claim else "MISMATCH"
    if lit != claim:
        mismatches += 1
        print(f"  n={n:2d}: literature g={lit:2d}  claimed g={claim:2d}   {status}")
print(f"  n=4..24: {mismatches} mismatches")

print()
print("== {2,n} family: hyperelliptic y^2 = 2 C(x,n) (y(y-1)=2C(x,n)), deg = n ==")
mismatches2 = 0
for n in range(3, 13):
    lit = genus_superelliptic(2, n)
    claim = closed_genus_2n(n)
    status = "OK " if lit == claim else "MISMATCH"
    if lit != claim:
        mismatches2 += 1
        print(f"  n={n:2d}: literature g={lit:2d}  claimed g={claim:2d}   {status}")
print(f"  n=3..12: {mismatches2} mismatches")

# Now check the full recorded grid rows against the literature formula where
# the row IS a pure superelliptic cover:
#   k2=2 row: pairs {2,n}, g = floor((n-1)/2)  -- direct hyperelliptic formula
#   k2=3 row: pairs {3,n}, g = n-1 or n-2      -- direct trigonal formula
# Recorded data (from code/out/genus_table.captured.txt):
recorded_2n = {3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:4, 10:4, 11:5, 12:5}
recorded_3n = {4:3, 5:4, 6:4, 7:6, 8:7, 9:7, 10:9, 11:10, 12:10,
               13:12, 14:13, 15:13, 16:15, 17:16, 18:16, 19:18, 20:19,
               21:19, 22:21, 23:22, 24:22}
print()
print("== Recorded grid rows vs literature formula ==")
m3 = sum(1 for n in recorded_3n if genus_superelliptic(3, n) != recorded_3n[n])
m2 = sum(1 for n in recorded_2n if genus_superelliptic(2, n) != recorded_2n[n])
print(f"  k2=3 row ({len(recorded_3n)} values): {m3} mismatches "
      f"({', '.join(str(n) for n in recorded_3n if genus_superelliptic(3,n)!=recorded_3n[n]) or 'none'})")
print(f"  k2=2 row ({len(recorded_2n)} values): {m2} mismatches "
      f"({', '.join(str(n) for n in recorded_2n if genus_superelliptic(2,n)!=recorded_2n[n]) or 'none'})")

# The {4,n} row is a 2:1 cover of a hyperelliptic curve; per the claim it is
# NOT a direct superelliptic cover, and the plain literature formula does not
# apply. Report expected behavior: the formula gives the genus of the
# hyperelliptic base w^2 = 1+24C(x,n), whose genus is floor((deg-1)/2)-type.
print()
print("== {4,n} row: expected NOT to match direct formula (2:1 cover) ==")
print("  base hyperelliptic w^2 = 1+24C(x,n): superelliptic(2, n) = g_base")
for n in range(5, 13):
    gbase = genus_superelliptic(2, n)
    grec  = recorded_4n[n] if (recorded_4n := {5:6,6:7,7:9,8:9,9:12,10:13,11:15,12:15}).get(n) else None
    print(f"  n={n:2d}: base genus (lit)={gbase:2d}, recorded {4,n} genus={grec}")
print("  Note: recorded {4,n} genus > 2*g_base in general, consistent with a")
print("  2:1 cover of the hyperelliptic base (Riemann-Hurwitz adds ramification).")

# Summary
ok = (mismatches == 0 and mismatches2 == 0 and m3 == 0 and m2 == 0)
print()
print("RESULT:", "ALL LITERATURE-FORMULA CROSS-CHECKS PASS" if ok
      else "SOME MISMATCHES — see above")