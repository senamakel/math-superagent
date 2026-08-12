"""Naive but obviously-correct brute force for Project Euler 241.

For a positive integer n, p(n) = sigma(n)/n where sigma(n) is the sum of all
divisors of n.  We want every n <= N with p(n) = k + 1/2 for an integer k,
i.e. 2*sigma(n)/n is an ODD integer:

    n | 2*sigma(n)   and   (2*sigma(n)//n) is odd.

Method: sieve the smallest prime factor (spf) of every integer up to N, then
recover sigma(n) from the canonical prime-power factorisation given by spf
(multiplicative formula  sigma = prod (p^(e+1)-1)/(p-1) ).  All arithmetic is
exact integer.

Complexity: O(N log log N) time to sieve spf, plus O(N * (number of prime
factors per n)) to form sigma — about O(N log N) overall; O(N) space.

Verification target from the statement: sigma(6) = 12.
"""

import sys
from math import gcd


def spf_sieve(N):
    """spf[i] = smallest prime factor of i for i in [2, N]; spf[1] = 1."""
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    i = 2
    while i * i <= N:
        if spf[i] == i:                     # i is prime
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def sigma_from_spf(n, spf):
    """Sum of divisors of n using the spf factorisation.

    factorise n into prime powers via repeated spf, then
    sigma(n) = prod_p (p^(e+1) - 1) // (p - 1).
    """
    total = 1
    m = n
    while m > 1:
        p = spf[m]
        e = 0
        pk = 1                       # p^e
        while m % p == 0:
            m //= p
            e += 1
            pk *= p
        # sum 1 + p + ... + p^e = (p^(e+1)-1)/(p-1)
        geom = (pk * p - 1) // (p - 1)
        total *= geom
    return total


def reduced_p(n, s):
    """p(n) = s/n as a reduced fraction (num, den)."""
    g = gcd(s, n)
    return s // g, n // g


def main():
    N = 10**6
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    # (a) confirm sigma(6) = 12
    s6 = sum(d for d in range(1, 7) if 6 % d == 0)
    print(f"sigma(6) = {s6}  (statement says 12)")

    # (b) sieve spf and compute sigma for all n up to N
    spf = spf_sieve(N)
    count = 0
    total_sum = 0
    for n in range(1, N + 1):
        s = sigma_from_spf(n, spf)
        two_s = 2 * s
        if two_s % n != 0:
            continue
        two_p = two_s // n
        if two_p % 2 == 0:
            continue
        k = (two_p - 1) // 2            # p(n) = k + 1/2
        num, den = reduced_p(n, s)
        print(f"n={n}: sigma={s}  p(n)={num}/{den}  k={k}  (2p={two_p})")
        count += 1
        total_sum += n

    print(f"count of qualifying n <= {N}: {count}")
    print(f"sum of qualifying n <= {N}: {total_sum}")


if __name__ == "__main__":
    main()
