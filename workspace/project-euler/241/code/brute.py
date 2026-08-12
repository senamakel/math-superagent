"""Naive oracle for Project Euler 241.

A positive integer n has perfection quotient p(n)=sigma(n)/n, where sigma(n)
is the sum of all divisors of n.  We want n with p(n) = k + 1/2 for an integer
k, i.e. 2*sigma(n)/n is an ODD integer.

Equivalently:  n | 2*sigma(n)  and  (2*sigma(n)//n) is odd.

This file is the obviously-correct brute force.  It factors nothing cleverly:
it sums divisors by direct trial division up to sqrt(n).  It is only ever run
at the sizes of the worked examples / small sanity checks, never at 1e18.

Verification target from the statement: sigma(6) = 12.
"""

import math
from bisect import insort


def sigma(n):
    """Sum of all positive divisors of n, by direct trial division."""
    if n < 1:
        raise ValueError("n must be positive")
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d
            other = n // d
            if other != d:
                total += other
        d += 1
    return total


def is_half_integer_quotient(n):
    """True iff p(n)=sigma(n)/n is k+1/2 for some integer k."""
    s = sigma(n)
    num = 2 * s
    if num % n != 0:
        return False
    return (num // n) % 2 == 1


def qualifying_up_to(N):
    """Sorted list of n in [1, N] with p(n) = k + 1/2."""
    res = []
    for n in range(1, N + 1):
        if is_half_integer_quotient(n):
            res.append(n)
    return res


if __name__ == "__main__":
    # --- worked examples from the statement -------------------------------
    print("sigma(6) =", sigma(6), "(statement says 12)")

    # --- small sanity sweep -----------------------------------------------
    N = 2000
    qual = qualifying_up_to(N)
    print(f"qualifying n <= {N}: {qual}")
    print("count:", len(qual), " sum:", sum(qual))
    for n in qual:
        x = 2 * sigma(n) // n
        print(f"  n={n}: sigma={sigma(n)} p(n)={sigma(n)}/{n}, 2p={x} (odd? {x % 2 == 1})")
