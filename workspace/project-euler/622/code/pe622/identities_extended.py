#!/usr/bin/env python3
"""Fresh falsification coverage for the crux identities beyond the recorded k=80.

  sum_{d|k} C(d) == tau(2^k-1) - 1
  sum_{d|k} S(d) == sigma(2^k-1) - 1
Cached so each 2^d-1 is factored once.
"""
import sympy
from functools import lru_cache


@lru_cache(maxsize=None)
def tau_sigma(d):
    n = 2**d - 1
    fac = sympy.factorint(n)
    tau = 1
    sig = 1
    for p, e in fac.items():
        tau *= (e + 1)
        sig *= (p**(e + 1) - 1) // (p - 1)
    return tau, sig


@lru_cache(maxsize=None)
def C_S(k):
    C = sum(sympy.mobius(k // d) * (tau_sigma(d)[0] - 1) for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (tau_sigma(d)[1] - 1) for d in sympy.divisors(k))
    return C, S


badC, badS = [], []
for k in range(1, 161):
    C, S = C_S(k)
    Cs = sum(C_S(d)[0] for d in sympy.divisors(k))
    Ss = sum(C_S(d)[1] for d in sympy.divisors(k))
    if Cs != tau_sigma(k)[0] - 1:
        badC.append(k)
    if Ss != tau_sigma(k)[1] - 1:
        badS.append(k)

print("prefix-sum identity k=1..160:")
print("  C(ord-count): holds", not badC, " first violation:", badC[:3])
print("  S(ord-sum):   holds", not badS, " first violation:", badS[:3])

# independent direct route, small k only
def C_S_direct(k):
    N = 2**k - 1
    C = S = 0
    for m in sympy.divisors(N):
        if m > 1 and sympy.n_order(2, m) == k:
            C += 1
            S += m
    return C, S

ok = True
for k in range(1, 36):
    if C_S(k) != C_S_direct(k):
        ok = False
        print("  direct-vs-mobius MISMATCH at k =", k)
print("direct-vs-mobius match k=1..35:", ok)
C60, S60 = C_S(60)
print("C(60),S(60) =", C60, S60, "-> answer", S60 + C60)
