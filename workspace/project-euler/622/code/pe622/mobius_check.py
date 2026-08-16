#!/usr/bin/env python3
"""Test the Möbius-inversion structure for ord-counts and ord-sums.

Classic identities:
  sum_{d|k} C(d) = #{m>1 : ord_m(2) | k} = tau(2^k - 1) - 1
  sum_{d|k} S(d) = sum_{m>1, m | 2^k-1} m = sigma(2^k - 1) - 1
so  C(k) = sum_{d|k} mu(k/d) (tau(2^d - 1) - 1)
    S(k) = sum_{d|k} mu(k/d) (sigma(2^d - 1) - 1)
"""
import sympy


def C_direct(k):
    N = 2**k - 1
    return sum(1 for m in sympy.divisors(N) if m > 1 and sympy.n_order(2, m) == k)


def S_direct(k):
    N = 2**k - 1
    return sum(m for m in sympy.divisors(N) if m > 1 and sympy.n_order(2, m) == k)


print(" k  C_dir C_mob S_dir S_mob  (mobius inversion)")
ok = True
for k in range(1, 25):
    Cdir = C_direct(k)
    Cmob = int(sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
                   for d in sympy.divisors(k)))
    Sdir = S_direct(k)
    Smob = int(sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
                   for d in sympy.divisors(k)))
    match = (Cdir == Cmob and Sdir == Smob)
    ok &= match
    print("%2d %5d %5d %12d %12d  %s" % (k, Cdir, Cmob, Sdir, Smob,
                                         'OK' if match else 'MISMATCH'))
print("All match:", ok)


k = 60
C = int(sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k)))
S = int(sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k)))
print("C(60) =", C)
print("S(60) =", S)
print("ANSWER sum of n = S(60) + C(60) =", S + C)
