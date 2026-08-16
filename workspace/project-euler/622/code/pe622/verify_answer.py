#!/usr/bin/env python3
"""Independent check: answer by Möbius inversion under the divisor-count identity,
versus the direct structural enumeration. Also verify the core 'iff' that makes
the inversion exact: ord_m(2)|k  <=>  m | 2^k - 1  for odd m."""
import sympy


def answer_mobius(k):
    C = int(sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
                for d in sympy.divisors(k)))
    S = int(sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
                for d in sympy.divisors(k)))
    return C, S, S + C


def answer_direct(k):
    N = 2**k - 1
    good = [m for m in sympy.divisors(N) if m > 1 and sympy.n_order(2, m) == k]
    S = sum(good)
    return len(good), S, S + len(good)


# 1. Verify the core iff on many k and many odd m.
ok_iff = True
for k in range(1, 30):
    for m in sympy.divisors(2**k - 1):
        lhs = (2**k - 1) % m == 0
        rhs = ord_m_divides = (sympy.n_order(2, m) % k == 0) if m > 1 else True
        if m > 1:
            ordm = sympy.n_order(2, m)
            ok_iff &= ((2**k - 1) % m == 0) == (ordm % k == 0)
print("iff ord_m(2)|k <=> m|2^k-1 holds for all tested (k, m|2^k-1):", ok_iff)

# 2. Two independent routes, full k up to 24, and target 60.
print("\n  k  C_mob C_dir  S_mob==S_dir   answer agreement")
agree = True
for k in list(range(1, 25)) + [60]:
    Cm, Sm, Am = answer_mobius(k)
    Cd, Sd, Ad = answer_direct(k)
    ok = (Cm == Cd and Sm == Sd and Am == Ad)
    agree &= ok
    print("%3d %5d %5d  %s   %s" % (k, Cm, Cd, Sm == Sd, "OK" if ok else "FAIL"))
print("\nAll routes agree:", agree)
print("ANSWER =", answer_mobius(60)[2])
