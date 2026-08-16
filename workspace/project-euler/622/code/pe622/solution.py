#!/usr/bin/env python3
"""
Project Euler 622 - solution.

Problem: s(n) = number of consecutive out-faro (perfect riffle) shuffles needed
to restore an even deck of size n.  By Diaconis-Graham-Kantor / Packard,
s(n) = ord_{n-1}(2), the multiplicative order of 2 mod n-1 (verified against a
brute list-rotation oracle in oracle_check.py).

We want the sum of all even n with s(n) = 60.

Structural fact that defeats scanning n (the intended method):
    ord_m(2) = 60  <=>  2^60 == 1 (mod m)  and  2^(60/p) != 1 (mod m)
                        for every prime p | 60.
The first condition means m | 2^60 - 1 =: N.  So m ranges over the DIVISORS of
N, not over all integers.  Enumerating divisors of N is polynomial in the
description of N (a 60-bit number), not a sweep up to any stated bound.

    ANSWER = sum over m with ord_m(2)=60 of (m+1)
           = (sum of those m) + (count of those m).

Worked example check first (requirement 1), then the structural count (2),
then independent direct cross-check over m up to the largest divisor candidate
(3).
"""
from math import gcd
import sympy


# ---------------- shared ord helper ---------------------------------------
def ord_mod(a, m):
    """Smallest r>0 with a^r == 1 (mod m); None if gcd(a,m)!=1."""
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r


def out_shuffle(deck):
    n = len(deck)
    half = n // 2
    top, bot = deck[:half], deck[half:]
    out = []
    for i in range(half):
        out.append(top[i])
        out.append(bot[i])
    return out


def s_oracle(n):
    """Brute-force out-shuffle count to restore deck of even size n."""
    deck = list(range(n))
    d = deck[:]
    count = 0
    while True:
        d = out_shuffle(d)
        count += 1
        if d == deck:
            return count


# =========================================================================
# 1. Reproduce the statement's worked examples.
# =========================================================================
print("=" * 70)
print("Step 1: reproduce the statement's worked examples (brute force)")
print("=" * 70)
assert s_oracle(52) == 8, s_oracle(52)
assert s_oracle(86) == 8, s_oracle(86)
print("s(52) =", s_oracle(52), " (brute force)")
print("s(86) =", s_oracle(86), " (brute force)")

vals8, total8 = [], 0
for n in range(2, 500, 2):
    if s_oracle(n) == 8:
        vals8.append(n)
        total8 += n
print("even n with s(n)=8 (brute force):", vals8)
print("sum of even n with s(n)=8 =", total8)
assert total8 == 412, total8
print("Worked example sum == 412  -> reproduced.\n")


# =========================================================================
# 2. Structural count: enumerate m | N = 2^60 - 1 with ord_m(2)=60.
# =========================================================================
print("=" * 70)
print("Step 2: structural enumeration over divisors of 2^60 - 1")
print("=" * 70)
N = 2**60 - 1
print("N = 2^60 - 1 =", N)
fac = sympy.factorint(N)
print("factorisation:", fac)

primes60 = [p for p in sympy.primefactors(60)]
print("prime divisors of 60:", primes60)


def has_order_60(m):
    """True iff ord_m(2) == 60, using divisibility of N and 60's prime divisors."""
    if m <= 1:
        return False
    if N % m != 0:          # first condition: must divide 2^60-1
        return False
    # 2^60 == 1 (mod m) already follows from m | 2^60 - 1
    for p in primes60:
        if pow(2, 60 // p, m) == 1:   # proper divisor d=60/p would give order <60
            return False
    return True


good = []
for m in sympy.divisors(N):
    if has_order_60(m):
        good.append(m)

S = sum(good)
C = len(good)
print("number of divisors of N:", sympy.divisor_count(N))
print("m with ord_m(2)=60 (count C =", C, "):")
print(good)
print("S = sum of m =", S)
print("ANSWER = S + C =", S + C)
print()


# =========================================================================
# 3. Independent cross-check: direct ord over every divisor of N.
#
# The largest divisor candidate is N itself (ord_N(2)=60), so a full integer
# scan up to it would be the prohibited exhaustive sweep over the stated bound
# (~1.15e18 steps) AND is unnecessary: ord_m(2)=60 forces m | 2^60-1, so only
# divisors of N can qualify.  The feasible independent route is therefore to
# enumerate the divisor set directly and compute ord_m(2) by straight power
# iteration — a different algorithm than the structural 60/prime-divisor test —
# and require the identical set, C, and S from both routes.
# =========================================================================
print("=" * 70)
print("Step 3: independent direct-ord cross-check over every divisor of N")
print("=" * 70)
print("largest divisor candidate m =", max(good))
print("note: that is N itself, so a full integer sweep to it (~%.0e steps)"
      % float(N), "is the prohibited exhaustive scan and is unnecessary,")
print("since ord_m(2)=60 forces m | 2^60-1.")
direct_good = []
for m in sympy.divisors(N):           # same finite candidate set, different alg
    if m > 1 and ord_mod(2, m) == 60:
        direct_good.append(m)
direct_S = sum(direct_good)
direct_C = len(direct_good)
print("direct-ord same set as structural:", sorted(direct_good) == sorted(good))
print("direct C =", direct_C, " direct S =", direct_S)
print("direct ANSWER =", direct_S + direct_C)
assert sorted(direct_good) == sorted(good)
assert direct_C == C and direct_S == S
print("Cross-check passed: structural and direct-ord routes agree exactly.")
print()
print("FINAL RESULT")
print("  C      =", C)
print("  S      =", S)
print("  ANSWER =", S + C)
