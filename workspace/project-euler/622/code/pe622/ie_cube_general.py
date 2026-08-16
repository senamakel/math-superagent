#!/usr/bin/env python3
"""Verify, for GENERAL k, that the maximal-proper-divisor inclusion-exclusion
cube equals the Möbius-inversion ord-count C(k) and ord-sum S(k).

General structural lemma (this is the fact the run used at k=60 with the
three maximal proper divisors {12,20,30} = {60/5, 60/3, 60/2}):

  The maximal proper divisors of k are { k/p : p prime | k }  (omega(k) of them).
  Every proper divisor d | k, d<k, divides one of them (pick p | k/d, then
  d | k/p).
  And d | M  ==>  2^d-1 | 2^M-1  ==>  A_d = {m : m|2^d-1} subseteq A_M.
  Hence order-k set = divisors(2^k-1) \ union_{p|k} A_{k/p}.
  Intersections: m in intersection over p in T  iff  m | 2^{k/pi(T)} - 1
  (since m|2^a-1 and m|2^b-1 iff m|2^{gcd(a,b)}-1).

So  C(k) = sum_{T subseteq primes(k)} (-1)^{|T|} ( tau(2^{k/pi(T)}-1) - 1 )
    S(k) = sum_{T subseteq primes(k)} (-1)^{|T|} ( sigma(2^{k/pi(T)}-1) - 1 )
where pi(T) = product of the primes in T.

We check these against the Möbius-inversion forms over k = 1..N.
"""
import sympy
from functools import lru_cache


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
    C = sum(sympy.mobius(k // d) * (tau_sigma(d)[0] - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (tau_sigma(d)[1] - 1)
            for d in sympy.divisors(k))
    return C, S


def C_S_cube(k):
    """Inclusion-exclusion over maximal proper divisors k/p, p prime | k."""
    primes = sympy.factorint(k).keys()
    primes = list(primes)
    C = S = 0
    # empty subset: A_k itself = divisors of 2^k-1 (the full set)
    from itertools import combinations
    # iterate all subsets via bitmask
    for mask in range(1 << len(primes)):
        sign = 1 if bin(mask).count('1') % 2 == 0 else -1
        d = k
        for i, p in enumerate(primes):
            if mask & (1 << i):
                d //= p
        if d == k:
            continue  # empty intersection, A_k already included as the base
        t, s = tau_sigma(d)
        C += sign * t
        S += sign * s
    # base term: full divisor set (mask=all zero) counts τ(2^k-1), σ(2^k-1);
    # m=1 is cancelled automatically by inclusion-exclusion (it lies in every A_{k/p}).
    t, s = tau_sigma(k)
    C = t + C
    S = s + S
    return C, S


badC, badS = [], []
for k in range(1, 161):
    Cm, Sm = C_S_mobius(k)
    Cc, Sc = C_S_cube(k)
    if Cm != Cc:
        badC.append((k, Cm, Cc))
    if Sm != Sc:
        badS.append((k, Sm, Sc))

print("cube-vs-mobius C  k=1..160  mismatch:", badC[:5], "count", len(badC))
print("cube-vs-mobius S  k=1..160  mismatch:", badS[:5], "count", len(badS))
# sample a few values, incl 60
for k in [12, 20, 30, 60, 96, 120]:
    print("k=%3d  C=%8d  S=%24d" % (k, C_S_mobius(k)[0], C_S_mobius(k)[1]))
C60, S60 = C_S_mobius(60)
print("ANSWER =", S60 + C60)
