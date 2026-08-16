#!/usr/bin/env python3
"""Confirm the general cube-vs-Mobius identity on a bounded fresh run to k=130,
reporting the first mismatching k and a worst-case runtime guard."""
import sympy
from functools import lru_cache
import time

start = time.time()
LIMIT = 130  # 2^130-1 factorization is well within reach


@lru_cache(maxsize=None)
def tau_sigma(d):
    fac = sympy.factorint(2**d - 1)
    tau = 1
    sig = 1
    for p, e in fac.items():
        tau *= (e + 1)
        sig *= (p**(e + 1) - 1) // (p - 1)
    return tau, sig


def C_S_mobius(k):
    C = sum(sympy.mobius(k // d) * (tau_sigma(d)[0] - 1) for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (tau_sigma(d)[1] - 1) for d in sympy.divisors(k))
    return C, S


def C_S_cube(k):
    primes = list(sympy.factorint(k).keys())
    C = S = 0
    for mask in range(1 << len(primes)):
        sign = 1 if bin(mask).count('1') % 2 == 0 else -1
        d = k
        for i, p in enumerate(primes):
            if mask & (1 << i):
                d //= p
        if d == k:
            continue
        t, s = tau_sigma(d)
        C += sign * t
        S += sign * s
    t, s = tau_sigma(k)
    C = t + C
    S = s + S
    return C, S


badC, badS = [], []
for k in range(1, LIMIT + 1):
    Cm, Sm = C_S_mobius(k)
    Cc, Sc = C_S_cube(k)
    if Cm != Cc:
        badC.append((k, Cm, Cc))
    if Sm != Sc:
        badS.append((k, Sm, Sc))
    if k % 25 == 0:
        print("  ..k=%d  (%.1fs)" % (k, time.time() - start), flush=True)

print("first k where C mismatches:", badC)
print("first k where S mismatches:", badS)
C60, S60 = C_S_mobius(60)
print("ANSWER check C60,S60,answer =", C60, S60, S60 + C60)
print("elapsed %.1fs" % (time.time() - start))
