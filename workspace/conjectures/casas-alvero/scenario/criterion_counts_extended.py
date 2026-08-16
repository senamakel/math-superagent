"""Counts of primes p such that p divides (d choose i) - 1 for some 1<=i<=d-1
(Schaub-Spivakovsky sufficient bad-prime criterion, arXiv:2307.05997 Cor 8).
Each such prime is a BAD prime for degree d (CA_{d,p} false).  The count of
distinct such primes, as a function of d, is a fresh integer sequence.

Compute it exactly for d=2..N.  Only needs binomials and factorization of
integers (d choose i) - 1, which is small for moderate d.
"""
from sympy import binomial, factorint


def criterion_primes(d):
    bad = set()
    for i in range(1, d):
        v = binomial(d, i) - 1
        for p in factorint(v):
            bad.add(p)
    return bad


if __name__ == "__main__":
    N = 40
    print("d | count | criterion primes")
    counts = []
    for d in range(2, N + 1):
        P = criterion_primes(d)
        counts.append(len(P))
        print(f"{d:2d} | {len(P):3d} | {sorted(P)}")
    print("\ncounts:", counts)
