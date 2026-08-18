"""Naive exact Goldbach oracle — the reference every other program checks against.

Statement it bears on (problem.md / GOAL.md, formalised in
code/lean/Lib/Statement.lean): every even integer n > 2 is a sum of two
primes, n = p + q, with p, q prime.  The ordered count below takes p <= q;
p and q need not be distinct (4 = 2 + 2 is a valid representation).  1 is not
prime, so n = 2 has no representation and is excluded by hypothesis, not a
counterexample.

Deliberately naive: trial division for primality, exhaustive search over
p in [2, n//2].  Exact integer arithmetic throughout.  This module is the
ORACLE: a fast method is checked against it on small cases, and it is never
pointed at the literature's verification bound (~4e18) — that bound is chosen
to defeat exactly this method.  Only ever run for n <= 200 here.

Complexity: O(n * sqrt(n)) time (n/2 trial divisions, each O(sqrt n)),
O(#partitions) space per query.

Verified (see code/out/oracle-brute-worked-examples.md):
  * reproduces every worked example in problem.md (4 = 2 + 2 valid; n = 2 has
    no representation and is excluded by hypothesis; 1 is not prime);
  * reproduces the hand-counted partition table HAND_COUNTS_4_50;
  * an independent sympy.isprime enumeration agrees for every even n <= 198.
"""

from math import isqrt

# Hand-counted number of ordered (p <= q) prime partitions p + q = n, for
# even n in [4, 50].  Counted by hand above the code; the oracle must
# reproduce every entry, and code/lean/Lib/GoldbachOracle.lean pins one
# witness per n in the kernel.
HAND_COUNTS_4_50 = {4: 1, 6: 1, 8: 1, 10: 2, 12: 1, 14: 2, 16: 2, 18: 2,
                    20: 2, 22: 3, 24: 3, 26: 3, 28: 2, 30: 3, 32: 2, 34: 4,
                    36: 4, 38: 2, 40: 3, 42: 4, 44: 3, 46: 4, 48: 5, 50: 4}


def is_prime(k: int) -> bool:
    """True iff k is prime.  1 is not prime; 2 is prime."""
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    d = 3
    while d <= isqrt(k):
        if k % d == 0:
            return False
        d += 2
    return True


def goldbach_partitions(n: int) -> list:
    """All (p, q) with p <= q, both prime, p + q == n.  [] for n < 4."""
    if n < 4:
        return []
    out = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if p <= q and is_prime(p) and is_prime(q):
            out.append((p, q))
    return out


def satisfies_goldbach(n: int) -> bool:
    """The conjecture's predicate on its domain: n even, n > 2, and n is a
    sum of two primes.  n outside the domain reports False (excluded by
    hypothesis, not a counterexample)."""
    if n <= 2 or n % 2 != 0:
        return False
    return len(goldbach_partitions(n)) > 0


def verify_partitions(n: int, expected: int) -> bool:
    """Second-route self-check of goldbach_partitions(n): every returned pair
    really is a prime-sum pair with p <= q, the list matches an independent
    recount, and the count equals the expected hand count `expected`."""
    got = goldbach_partitions(n)
    for p, q in got:
        assert p <= q and is_prime(p) and is_prime(q) and p + q == n, \
            f"invalid partition {p}+{q} for n={n}"
    recount = [(p, n - p) for p in range(2, n // 2 + 1)
               if is_prime(p) and is_prime(n - p) and p <= n - p]
    assert got == recount, f"self-inconsistency for n={n}"
    assert len(got) == expected, \
        f"n={n}: got {len(got)} partitions {got}, hand count {expected}"
    return True
