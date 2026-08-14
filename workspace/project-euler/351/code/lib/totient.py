"""Euler totient summatory function, exact integer arithmetic.

Everything here is a direct computation of Phi(N) = sum_{k=1..N} phi(k).
Memory-efficient enough for N = 1e8 (an int32 array of length N+1).
"""

import numpy as np


def sum_phi(N, primes=None):
    """Return Phi(N) = sum_{k=1..N} phi(k) exactly (a Python int).

    Uses the incremental totient sieve: phi[i] starts as i; for each prime p,
    every multiple m of p gets phi[m] -= phi[m]//p.  Correct because each
    prime factor contributes the (p-1)/p factor exactly once, and the order
    of factors does not matter for the product formula.  Verified against a
    naive gcd-based phi on N <= 1000 in solution.py's parity check.

    A numpy int32 array of length N+1 holds the phi values (phi(m) <= m <= N
    < 2^31 for N = 1e8).  The final sum is accumulated in int64.

    If `primes` is given it must be a 1-D numpy array of the primes <= N; it
    is used instead of re-sieving.
    """
    if N < 0:
        raise ValueError("N must be >= 0")
    Np1 = N + 1
    phi = np.arange(Np1, dtype=np.int32)
    if primes is None:
        isprime = np.ones(Np1, dtype=bool)
        isprime[0:2] = False
        lim = int(np.sqrt(N))
        for p in range(2, lim + 1):
            if isprime[p]:
                isprime[p * p::p] = False
        primes = np.nonzero(isprime)[0]
    for p in primes.tolist():
        window = phi[p::p]
        phi[p::p] = window - window // p
    return int(np.sum(phi, dtype=np.int64))


def H_hexagon(n, sum_phi_n):
    """H(n) = number of hidden points in a hexagon of order n.

    Hidden points = 3n^2 + 3n - 6*Phi(n).  This is the given identity
    (verified at n = 5, 10, 1000 against brute force).
    """
    return 3 * n * n + 3 * n - 6 * sum_phi_n
