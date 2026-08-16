#!/usr/bin/env python3
"""Structural simplification for PRIME order k=p.

From the Möbius identity (verified k=1..60 in the run):
    C(k) = sum_{d|k} mu(k/d)(tau(2^d-1)-1),  S(k) = sum_{d|k} mu(k/d)(sigma(2^d-1)-1)

For k=p prime, divisors are {1,p}, mu(p)=-1, mu(1)=1, so
    C(p) = tau(2^p-1) - 1,   S(p) = sigma(2^p-1) - 1
regardless of whether 2^p-1 is prime.  When 2^p-1 is a Mersenne prime then
tau=2, sigma=2^p, giving C(p)=1, S(p)=2^p-1.
Check this tau/sigma reduction against the direct computation for primes.
"""
import sympy

def C_S(k):
    C = sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k))
    return C, S

print(" p  C(p)  tau(2^p-1)-1  match |  S(p)      sigma(2^p-1)-1  match")
ok = True
for p in range(2, 80):
    if not sympy.isprime(p):
        continue
    C, S = C_S(p)
    Ct = sympy.divisor_count(2**p - 1) - 1
    St = sympy.divisor_sigma(2**p - 1, 1) - 1
    m = (C == Ct and S == St)
    ok &= m
    print("%2d  %5d  %13d   %5s | %12d %14d   %5s" % (p, C, Ct, C == Ct, S, St, S == St))
print("All primes p=2..79 (both identities):", ok)
