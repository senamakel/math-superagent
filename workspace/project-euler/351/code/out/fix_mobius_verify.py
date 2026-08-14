"""Corrected Mobius-inversion verification of Phi(1e8) for PE 351.

The earlier verify_mobius.py used  mu[p*p::p] = 0, which zeroes every
multiple of p from p^2 on -- including squarefree numbers like 6, 10, 14, 15
(6 is p=2 step 2 from 4: 4,6,8,10,...).  The step must be p*p so only numbers
divisible by p^2 are zeroed.  That bug made the old Möbius route disagree with
the totient sieve at N=10 (32 vs 30) and at 1e8.

Identity:  Phi(N) = sum_{k=1..N} phi(k) = sum_{k=1..N} mu(k) * T(floor(N/k)),
T(m) = m*(m+1)//2, from phi(n) = sum_{d|n} mu(d)*(n/d).
Exact integer arithmetic; the mu table is int8 but the sum is exact Python int.
"""
import sys
import numpy as np
from lib.totient import sum_phi


def mu_sieve_correct(N):
    """Mobius function mu[0..N], exact, vectorized prime marking."""
    mu = np.ones(N + 1, dtype=np.int8)
    mu[0] = 0
    isprime = np.ones(N + 1, dtype=bool)
    isprime[0:2] = False
    for p in range(2, int(N ** 0.5) + 1):
        if isprime[p]:
            isprime[p * p::p] = False
    for p in np.nonzero(isprime)[0].tolist():
        mu[p::p] *= -1            # every multiple of p flips sign
        mu[p * p::p * p] = 0      # numbers divisible by p^2 -> 0 (STEP p*p!)
    return mu


def sum_phi_mobius(N, mu=None):
    if mu is None:
        mu = mu_sieve_correct(N)
    k = np.arange(1, N + 1, dtype=np.int64)
    t = N // k
    term = (t * (t + 1) // 2) * mu[1:].astype(np.int64)
    return int(np.sum(term, dtype=np.int64))


def check_small():
    for N in (2, 3, 5, 10, 20, 100, 1000, 100_000):
        a = sum_phi(N)
        b = sum_phi_mobius(N)
        ok = a == b
        print(f"N={N:6d}  phi-sieve={a:9d}  mobius={b:9d}  MATCH={ok}")
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    check_small()
    N = 10 ** 8
    a = sum_phi(N)
    b = sum_phi_mobius(N)
    print(f"N={N}  phi-sieve={a}  mobius={b}  MATCH={a == b}")
    assert a == b
