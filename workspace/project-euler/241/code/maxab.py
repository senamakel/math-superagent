"""Upper bound on sigma(n)/n for n <= BOUND, via partition shapes.

Structural fact (derived here, verified against brute force below): for
p < q and exponents a <= b,

    sigma(p^a) sigma(q^b) / (p^a q^b)  <=  sigma(p^b) sigma(q^a) / (p^b q^a)

because log f(e, p) with f(e,p) = sigma(p^e)/p^e has e-increment
g_b(p) - g_a(p) = -sum_j (p^{-(a+1)j} - p^{-(b+1)j})/j, a positive function
decreasing in p (each summand decreases in p).  Hence bubble-sorting the
exponent multiset of any n into non-increasing order on the smallest primes
only increases sigma/n and only decreases n.  Therefore

    max{sigma(n)/n : n <= X} = max over shapes n = prod_i p_i^{e_i},
    e_1 >= e_2 >= ... >= e_k >= 1 (k = number of prime factors), n <= X.

The family of such shapes is tiny at X = 10^18 (thousands), so an exact DFS
over partitions with pruning (e_i <= previous exponent, product <= X) finds
the exact maximum in exact rational arithmetic.

Verified: for X in {10, 100, 10^3, 10^4, 10^5, 10^6} the shape-DSF maximum
equals the plain scan max over all n <= X (see verify_against_bruteforce).
"""

import sys
from fractions import Fraction

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67)


def factor_ratio(p, e):
    """sigma(p^e)/p^e = (p^(e+1)-1)/(p^e * (p-1)) as exact Fraction."""
    return Fraction(p ** (e + 1) - 1, (p ** e) * (p - 1))


def max_sigma_over_n(X):
    """(max_ratio, n, [(p,e),...]) maximizing sigma(n)/n over n <= X.

    DFS enumerated exactly the partition shapes of the Sorting Lemma.
    """
    best_frac = Fraction(0)
    best_n = 0
    best_shape = []

    def dfs(idx, max_exp, n, frac, shape):
        nonlocal best_frac, best_n, best_shape
        if frac > best_frac:
            best_frac, best_n, best_shape = frac, n, list(shape)
        p = PRIMES[idx]
        pk = p                       # p^e
        e = 1
        while e <= max_exp and pk <= X // n:
            shape.append((p, e))
            dfs(idx + 1, e, n * pk, frac * factor_ratio(p, e), shape)
            shape.pop()
            e += 1
            pk *= p

    # the DFS only recurses while the next prime index exists; give it a
    # safety margin by stopping when no prime is left (shape is then final).
    dfs(0, 64, 1, Fraction(1), [])
    return best_frac, best_n, best_shape


def verify_against_bruteforce(X):
    """Oracle: plain scan over all n <= X (exact rationals)."""
    best_frac = Fraction(0)
    best_n = 0
    for n in range(1, X + 1):
        m, s = n, 1
        p = 2
        while m > 1:
            if p * p > m:
                s *= m + 1
                break
            if m % p == 0:
                e, pk = 0, 1
                while m % p == 0:
                    m //= p
                    e += 1
                    pk *= p
                s *= (pk * p - 1) // (p - 1)
            p += 1
        f = Fraction(s, n)
        if f > best_frac:
            best_frac, best_n = f, n
    return best_frac, best_n


def main():
    bounds = [10**14, 10**18]
    if len(sys.argv) > 1:
        bounds = [int(sys.argv[1])]

    for X in (10, 100, 1000, 10**4, 10**5, 10**6):
        fast = max_sigma_over_n(X)
        slow = verify_against_bruteforce(X)
        ok = fast[0] == slow[0] and fast[1] == slow[1]
        print(f"check X={X}: shape DFS {float(fast[0])} at n={fast[1]} "
              f"== scan {float(slow[0])} at n={slow[1]} -> {ok}")
        if not ok:
            print("MISMATCH", fast, slow)
            return

    for X in bounds:
        frac, n, shape = max_sigma_over_n(X)
        print(f"BOUND = {X}")
        print(f"  max sigma(n)/n = {float(frac)}")
        print(f"  n = {n}")
        print(f"  shape = {shape}")
        diff = frac - Fraction(1, 2)
        kmax = int(diff.numerator // diff.denominator) if diff >= 0 else None
        print(f"  largest integer k with k+1/2 <= max: {kmax}")
        print()


if __name__ == "__main__":
    main()