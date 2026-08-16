#!/usr/bin/env python3
"""Verify the Möbius-inversion structure for C(k), S(k) rigorously, and search
for a counterexample.

Claim (the exploitable structure):
    sum_{d|k} C(d) = tau(2^k - 1) - 1            (C = #{m>1 : ord_m(2)=k})
    sum_{d|k} S(d) = sigma(2^k - 1) - 1          (S = sum of such m)
    =>  C(k) = sum_{d|k} mu(k/d) (tau(2^d-1) - 1)
        S(k) = sum_{d|k} mu(k/d) (sigma(2^d-1) - 1)

Reason it is true: ord_m(2) | k  <=>  m | 2^k - 1 (for odd m, gcd(2,m)=1),
and 2^k-1 is odd so every divisor is odd.  Möbius inversion then recovers the
exact-order counts/sums.

Direct route (ground truth): enumerate divisors of 2^k-1 and compute ord_m(2)
by power iteration, count and sum those with ord==k.
"""
import sympy


def C_S_direct(k):
    N = 2**k - 1
    C = 0
    S = 0
    for m in sympy.divisors(N):
        if m > 1 and sympy.n_order(2, m) == k:
            C += 1
            S += m
    return C, S


def C_S_mobius(k):
    C = sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k))
    return C, S


# Full-range agreement check k = 1..60 (AT the target order).
print(" k   C_dir   C_mob   |   S_dir        S_mob       match")
bad = []
for k in range(1, 61):
    Cd, Sd = C_S_direct(k)
    Cm, Sm = C_S_mobius(k)
    match = (Cd == Cm and Sd == Sm)
    if not match:
        bad.append(k)
    print("%2d  %6d %6d  | %14d %14d   %s" % (k, Cd, Cm, Sd, Sm,
                                              'OK' if match else 'MISMATCH'))
print()
print("All k=1..60 match:", not bad)
if bad:
    print("FIRST counterexample k =", bad[0])

# The target answer at k=60.
C60, S60 = C_S_mobius(60)
print("C(60) =", C60)
print("S(60) =", S60)
print("ANSWER = sum of n = S(60) + C(60) =", S60 + C60)
