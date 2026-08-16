#!/usr/bin/env python3
"""
PE622 inclusion-exclusion closed-form certificate verification (exact integers).

We want the sum over divisors m of N = 2^60 - 1 with ord_m(2) = 60:

    S = sum of those m
    C = number of those m
    ANSWER = S + C      (each qualifying m contributes n = m + 1)

Inclusion-exclusion derivation
------------------------------
Since m | N, the order ord_m(2) divides 60.  Every proper divisor d of 60
divides at least one of {12, 20, 30} (check: 1,2,3,4,5,6,10,12,15,20,30 —
each divides 12, 20, or 30).  And m | 2^k - 1  <=>  ord_m(2) | k.  Hence

    ord_m(2) = 60
      <=>  m does not divide 2^12 - 1, 2^20 - 1, or 2^30 - 1.

So qualify = (divisors of N) \ (A_12 ∪ A_20 ∪ A_30) where A_k = {m | 2^k - 1}.
By inclusion-exclusion the sum over the qualifying set is

    S = sigma(N) - sigma(2^12-1) - sigma(2^20-1) - sigma(2^30-1)
        + sigma(gcd(2^12-1,2^20-1)) + sigma(gcd(2^12-1,2^30-1))
        + sigma(gcd(2^20-1,2^30-1)) - sigma(gcd(2^12-1,2^20-1,2^30-1))

using m | X and m | Y  <=>  m | gcd(X,Y), and
gcd(2^a - 1, 2^b - 1) = 2^gcd(a,b) - 1.  Concretely the pairwise intersections
are gcds 2^4-1=15, 2^6-1=63, 2^10-1=1023, triple 2^2-1=3:

    S = sigma(N) - sigma(4095) - sigma(1048575) - sigma(1073741823)
        + sigma(15) + sigma(63) + sigma(1023) - sigma(3)
    C = tau(N) - tau(4095) - tau(1048575) - tau(1073741823)
        + tau(15) + tau(63) + tau(1023) - tau(3)

Independent verification
------------------------
Brute-force direct enumeration over all divisors of N (sympy.divisors, exact):
classify m by whether it divides each of 2^12-1, 2^20-1, 2^30-1; keep those
dividing none; sum them (S) and count them (C).  Assert both routes agree,
and assert ANSWER == 3010983666182123972.
"""
import sympy
from sympy import divisor_sigma as sigma, divisor_count as tau

N = 2**60 - 1
bound12 = 2**12 - 1      # 4095
bound20 = 2**20 - 1      # 1048575
bound30 = 2**30 - 1      # 1073741823

# ------------------------------------------------------------------
# Route 1: inclusion-exclusion closed forms using sigma and tau.
# ------------------------------------------------------------------
sig_N    = sigma(N)
sig_12   = sigma(bound12)
sig_20   = sigma(bound20)
sig_30   = sigma(bound30)
sig_15   = sigma(15)
sig_63   = sigma(63)
sig_1023 = sigma(1023)
sig_3    = sigma(3)

tau_N    = tau(N)
tau_12   = tau(bound12)
tau_20   = tau(bound20)
tau_30   = tau(bound30)
tau_15   = tau(15)
tau_63   = tau(63)
tau_1023 = tau(1023)
tau_3    = tau(3)

S = (sig_N - sig_12 - sig_20 - sig_30
     + sig_15 + sig_63 + sig_1023 - sig_3)
C = (tau_N - tau_12 - tau_20 - tau_30
     + tau_15 + tau_63 + tau_1023 - tau_3)

print("N = 2^60 - 1 =", N)
print("factorisation of N:", sympy.factorint(N))
print()
print("Intermediates (sigma = sum of divisors):")
print("  sigma(N)          =", sig_N)
print("  sigma(2^12 - 1)   =", sig_12, " (2^12-1 =", bound12, ")")
print("  sigma(2^20 - 1)   =", sig_20, " (2^20-1 =", bound20, ")")
print("  sigma(2^30 - 1)   =", sig_30, " (2^30-1 =", bound30, ")")
print("  sigma(15)         =", sig_15)
print("  sigma(63)         =", sig_63)
print("  sigma(1023)       =", sig_1023)
print("  sigma(3)          =", sig_3)
print()
print("Intermediates (tau = number of divisors):")
print("  tau(N)          =", tau_N)
print("  tau(2^12 - 1)   =", tau_12)
print("  tau(2^20 - 1)   =", tau_20)
print("  tau(2^30 - 1)   =", tau_30)
print("  tau(15)         =", tau_15)
print("  tau(63)         =", tau_63)
print("  tau(1023)       =", tau_1023)
print("  tau(3)          =", tau_3)
print()
print("Closed form:  S =", S)
print("Closed form:  C =", C)
print("Closed form:  ANSWER = S + C =", S + C)
print()

# ------------------------------------------------------------------
# Route 2: direct enumeration over all divisors of N.
# ------------------------------------------------------------------
divisors = sympy.divisors(N)
print("number of divisors of N (sympy.divisors) =", len(divisors))
assert len(divisors) == 4608, len(divisors)

qualifying = []
for m in divisors:
    # m divides 2^k-1  <=>  (2^k-1) % m == 0  (2^k-1 is small)
    if (bound12 % m != 0) and (bound20 % m != 0) and (bound30 % m != 0):
        qualifying.append(m)

S_direct = sum(qualifying)
C_direct = len(qualifying)
print("direct-enumeration: C =", C_direct, " S =", S_direct)
print("direct-enumeration: ANSWER = S + C =", S_direct + C_direct)

assert S_direct == S, (S_direct, S)
assert C_direct == C, (C_direct, C)
print("\nBoth routes agree exactly (S and C).")

expected = 3010983666182123972
assert (S + C) == expected, (S + C, expected)
print("ANSWER == 3010983666182123972  -> asserted and confirmed.")
