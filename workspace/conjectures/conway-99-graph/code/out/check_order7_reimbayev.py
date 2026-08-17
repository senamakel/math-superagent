"""Verify Reimbayev order-7 (arXiv 2511.06572) arithmetic at the five family members.

Claims checked (exact integer arithmetic):
  p7 <=  (1/14) n k (k-2)(k-4)(2k^2 - 30k + 133)   [upper bound, parameter-determined]
  h0  =  (1/14) n k (k-2)(k-4)(2k^2 - 30k + 133) - 10*n3 - h11
  and every other h_i expressed in (n,k) terms + n3, h11 coefficients.

Purpose: does any order-7 identity force n3 or pin h11 into a range the
controls (n3=0) or the family cannot realize?  Expected (falsifies the
counting-route closure): the p7 bound is parameter-determined, so it gives
zero separating power between 99 and the n3=0 controls (9,243); and the
presence of the SECOND free variable h11 (with 2*n3 <= h11 <= 4*n3) means the
order-7 counts still do not force n3 >= 1.

Runs on the exact integer formulas from the paper's full text in the library.
"""
from fractions import Fraction as F

def p7_bound(n, k):
    # (1/14) n k (k-2)(k-4)(2k^2 - 30k + 133)
    return F(n) * k * (k-2) * (k-4) * (2*k*k - 30*k + 133) / 14

def h0_expr(n, k, n3, h11):
    base = F(n) * k * (k-2) * (k-4) * (2*k*k - 30*k + 133) / 14
    return base - 10*n3 - h11

# five-member family (v,k): integral bound check
family = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]

from math import prod
for (n,k) in family:
    pb = p7_bound(n,k)
    # integrality of the bound's numerator
    num = n*k*(k-2)*(k-4)*(2*k*k-30*k+133)
    print(f"n={n:6d} k={k:3d} | p7 bound = {pb} | integer? {pb.denominator==1} "
          f"| numerator mod14 = {num%14}")

print("\n-- at the target (99,14,1,2), h_i as functions of n3, h11 --")
n,k = 99,14
C = F(n)*k*(k-2)*(k-4)          # nk(k-2)(k-4)
C2 = F(n)*k*(k-2)*(2*k*k-25*k+68)
print("nk(k-2)(k-4) =", C, "  nk(k-2)(2k^2-25k+68) =", C2)
# h11 range from paper: 2*n3 <= h11 <= 4*n3 (from h16>=0, h18>=0)
# with n3 in [0, 4158] (order-6 residue class, exact)
print("h11 free with 2*n3 <= h11 <= 4*n3 (h16=h11-2n3>=0, h18=n3-h11/4>=0)")
print("p7 bound at (99,14,1,2):", p7_bound(99,14), "= heptagon upper bound (parameter-determined)")

# n3 in the order-6 residue class: n3≡0 mod 3, n3 in [0,4158]
# for n3=0 and any valid h11 (0), what is h0? (n3=0 forces h11=0)
print("\n-- n3=0 / h11=0 case (the Makhnev-conditional branch, both controls) --")
for (n,k) in [(9,4),(243,22),(99,14)]:
    h0 = h0_expr(n,k,0,0)
    print(f"n={n:5d} k={k:2d} | h0(n3=0,h11=0) = {h0} | integer? {h0.denominator==1}")
