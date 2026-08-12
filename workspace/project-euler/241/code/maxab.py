"""Greedy upper bound on sigma(n)/n for n <= 10**18.

Claim we inspect: maximizing sigma(n)/n is a "greedy" colonial problem -
sigma(n)/n is multiplicative, sigma(p^e)/p^e = (p^(e+1)-1)/(p^e (p-1)),
and this factor is largest for the smallest primes and decays as e grows and
as p grows.  A DFS over primes in increasing order with all exponents, pruning
when the running n times the next prime would exceed the bound, hunts the top
of the space.

This is NOT the answer to the Project Euler 241 question (that, by theory, is
effectively a small set of explicit candidates), just an expensive-but-correct
upper bound: any n has sigma(n)/n at most the best this walk finds among
"minimal" shapes.  Because sigma/n is multiplicative and increasing in each
exponent, the true maximiser is always among combinations of the smallest
primes, so DFS with pruning reaches it.

Exact integer arithmetic throughout (rationals compared exactly via
Fraction).  Time is bounded by the number of prime-power combinations with
product <= 10^18, which is small (thousands); space O(depth).
"""

import sys
from fractions import Fraction

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67]


def sigma_over_n_factor(p, e):
    """sigma(p^e)/p^e = (p^(e+1)-1)/(p^e * (p-1)) as an exact Fraction."""
    return Fraction(p ** (e + 1) - 1, (p ** e) * (p - 1))


def max_sigma_over_n(BOUND):
    """Best (frac, n, factors) with n <= BOUND over greedy prime-power DFS."""
    best_frac = Fraction(0)
    best_n = 0
    best_factors = []

    def dfs(start_idx, n, frac, factors):
        nonlocal best_frac, best_n, best_factors
        if frac > best_frac:
            best_frac, best_n, best_factors = frac, n, list(factors)
        for i in range(start_idx, len(PRIMES)):
            p = PRIMES[i]
            if n * p > BOUND:
                break
            pk = p
            e = 1
            while pk <= BOUND // n:
                factors.append((p, e))
                dfs(i + 1, n * pk, frac * sigma_over_n_factor(p, e), factors)
                factors.pop()
                e += 1
                pk *= p

    dfs(0, 1, Fraction(1), [])
    return best_frac, best_n, best_factors


def main():
    bounds = [10**14, 10**18]
    if len(sys.argv) > 1:
        bounds = [int(sys.argv[1])]
    for B in bounds:
        frac, n, factors = max_sigma_over_n(B)
        print(f"BOUND = {B}")
        print(f"  max sigma(n)/n = {float(frac)}")
        print(f"  n = {n}")
        print(f"  factorisation = {factors}")
        # largest integer k with k + 1/2 <= frac  =>  k <= frac - 1/2
        diff = frac - Fraction(1, 2)
        kmax = int(diff.numerator // diff.denominator) if diff >= 0 else None
        print(f"  largest integer k (any n<=BOUND could at most reach): {kmax}")
        print()


if __name__ == "__main__":
    import sys
    main()
