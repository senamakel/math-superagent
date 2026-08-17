#!/usr/bin/env python3
"""Scholar check of Reimbayev arXiv:2409.10620, arXiv:2508.03377.

Verify from the primary full text that:
  (A) the c6 (coefficient of x^(n-6) in char poly), expressed in closed form
      c6 = -(1/576) n k (k-2) (3k^5 + 6k^4 - 84k^3 + 116k^2 + 124k - 240),
      reproduces his Table-3 numerics for the five family members.
  (B) the hexagon identity  n12 = (1/12)n k (k-2)(2k^2 - 21k + 53) + n3  holds
      at least symbolically given his relations, i.e. the base term equals
      F(n,k) for n3=0, and lands at 209286 for (99,14).
  (C) the pentagon count p5 = (1/5)n k (k-2)(k-4) (Theorem 1).
All exact integer arithmetic.
"""
from fractions import Fraction

members = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]

def c6(n,k):
    return -(Fraction(1,576)*n*k*(k-2)*(3*k**5+6*k**4-84*k**3+116*k**2+124*k-240))

def n12_base(n,k):
    return Fraction(1,12)*n*k*(k-2)*(2*k**2-21*k+53)

def p5(n,k):
    return Fraction(1,5)*n*k*(k-2)*(k-4)

print("(A) c6 closed form vs Reimbayev Table 3:")
reimbayev_c6 = {9:-168,99:-47288703,243:-2975686065,6273:-7204770339625320,494019:-2466795174682153663896408}
for (n,k) in members:
    v = c6(n,k)
    print(f"  n={n:7d} k={k:4d}  c6={v}   matches paper={v==reimbayev_c6[n]}   (paper said {reimbayev_c6[n]})")

print()
print("(B) hexagon base term F(n,k) [=n12 when n3=0]:")
for (n,k) in members:
    b = n12_base(n,k)
    print(f"  n={n:7d} k={k:4d}  (1/12)nk(k-2)(2k^2-21k+53) = {b}   integral={b.denominator==1}")
print("  => at (99,14) base = 209286 (with n3=0); at (243,22):")
print("     base =", n12_base(243,22))

print()
print("(C) pentagon count p5=(1/5)nk(k-2)(k-4) (Theorem 1):")
for (n,k) in members:
    print(f"  n={n:7d} k={k:4d}  p5 = {p5(n,k)}  integral={p5(n,k).denominator==1}")
