#!/usr/bin/env python3
"""Rigorous closed-form verification of cap = v*k*(k-2)/4.

cap_brute(n,k) = min over formulas f with n3-coefficient c<0 of base/(-c),
where base = f(n,k,0).

The claim: for k>=6 the min is attained at n1 = (1/12) n k (k-2) - n3/3,
giving cap = n k (k-2)/4. We verify by:
 (1) computing brute cap from ALL 62 formulas,
 (2) computing the n1-only value,
 (3) confirming equality for every integrality-feasible member EXCEPT k=4
     (where the n5 formula, with factor (k-4), binds and gives 0).
Also verify the closed form is an integer: v = 1+k^2/2; v*k*(k-2)/4 must be
an integer for each feasible k.
"""
import importlib.util, os
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

FAMILY = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]

print("Verification of cap closed form = v*k*(k-2)/4 for k>=6 members:\n")
print(f"{'k':>4} {'v':>8} {'brute_cap':>14} {'v*k(k-2)/4':>13} {'match':>6} {'integer?':>8}")
for (n,k) in FAMILY:
    brute = m.n3_upper_cap(n,k)[0]
    v = 1 + k*k//2
    ana_num = v*k*(k-2)
    ana = ana_num // 4
    is_int = (ana_num % 4 == 0)
    print(f"{k:>4} {v:>8} {brute:>14} {ana:>13} {str(brute==ana):>6} {str(is_int):>8}")

print()
print("Integer proof: v = (k^2+2)/2, so cap = (k^2+2)*k*(k-2)/8.")
print("k=u^2+u+2 is even? k mod 4 for u in {1,3,4,10,31}: ", end="")
for u in [1,3,4,10,31]:
    k = u*u+u+2
    print(f"{k%4}", end=" ")
print()
print("=> show k(k-2)(k^2+2)/8 integer for each feasible k:")
for u in [1,3,4,10,31]:
    k = u*u+u+2
    val = k*(k-2)*(k*k+2)//8
    print(f"  u={u:>2} k={k:>4}: cap={val}  divisibility (num%8={k*(k-2)*(k*k+2)%8})")
print()
print("The k=4 (u=1) member: cap closed form gives", 4*2*(16+2)//8, "but brute gives 0,")
print("because for k=4 the n5 formula (carries factor k-4) binds; n1 gives a finite")
print("value but n5's base (1/8)*n*k*(k-2)(k-4) = 0 requires n3 <= 0. So k=4 is the")
print("degenerate case; the closed form v*k(k-2)/4 governs all k>=6 members and the")
print("k=4 member separately pins n3 to 0 (which is the true rook value).")
