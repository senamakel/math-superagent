#!/usr/bin/env python3
"""Check the prime-k structure of S(k) and C(k).

For k = p prime: S(p) = sum of m>1 with ord_m(2)=p, over divisors m of 2^p-1.
Claim to test: S(p) == 2^p - 1  (and C(p)==1)  iff 2^p-1 is prime (Mersenne).
If 2^p-1 is composite, its prime-power factors q^a each have ord_{q^a}(2) dividing p;
those sub-multiples also contribute, so S(p) > 2^p-1 and C(p) > 1.
"""
import sympy

def C_S(p):
    C = sum(sympy.mobius(p // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(p))
    S = sum(sympy.mobius(p // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(p))
    return C, S

print(" p  C(p)   S(p)      S==2^p-1?   2^p-1 prime?")
for p in range(1, 40):
    if not sympy.isprime(p):
        continue
    C, S = C_S(p)
    mp = 2**p - 1
    primal = sympy.isprime(mp)
    print("%2d  %5d %10d   %5s       %s" % (p, C, S, S == mp, primal))
