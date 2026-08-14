"""Independent verification of Phi(1e8) via the Mobius inversion identity.

Phi(N) = sum_{k=1..N} phi(k) = sum_{k=1..N} mu(k) * T(floor(N/k)),
T(m) = m*(m+1)/2, from phi(n) = sum_{d|n} mu(d) * n/d summed over n.

This uses a different sieve (multiplicative definition of mu via prime
marking on an int8 array) and a different summation than the incremental
phi sieve in lib/totient.py; only the prime list is shared.  Its result
should agree exactly with Phi(1e8) from solution.py.
"""

import numpy as np
from lib.totient import sum_phi


def phi_sieve_primes(N):
    """Return the primes <= N as a 1-D numpy int64 array (Eratosthenes)."""
    isprime = np.ones(N + 1, dtype=bool)
    isprime[0:2] = False
    lim = int(np.sqrt(N))
    for p in range(2, lim + 1):
        if isprime[p]:
            isprime[p * p::p] = False
    return np.nonzero(isprime)[0]


def sum_phi_mobius(N):
    """Phi(N) by Mobius inversion, exact (Python int)."""
    mu = np.ones(N + 1, dtype=np.int8)
    mu[0] = 0
    primes = phi_sieve_primes(N)
    for p in primes.tolist():
        mu[p::p] *= -1
        mu[p * p::p] = 0
    k = np.arange(1, N + 1, dtype=np.int64)
    t = N // k
    term = (t * (t + 1) // 2) * mu[1:].astype(np.int64)
    return int(np.sum(term, dtype=np.int64))


if __name__ == "__main__":
    N = 10**8
    a = sum_phi(N)
    b = sum_phi_mobius(N)
    print(f"phi-sieve Phi(1e8) = {a}")
    print(f"mobius   Phi(1e8) = {b}")
    print("MATCH" if a == b else "MISMATCH")
    assert a == b