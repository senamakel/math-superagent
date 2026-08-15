"""Exact integer perfect-power detection: q-th roots, q-th-power tests, and
the consecutive-perfect-power oracle.  Exact integer arithmetic only, no
floats anywhere.

Every function is callable without reading this source: explicit arguments,
one job, no reliance on globals or on a file written earlier in the run.
"""
from math import isqrt


def iroot(n, k):
    """Floor integer k-th root of n >= 0, k >= 1, by integer Newton iteration.

    Returns the largest integer r with r**k <= n.  Exact integers throughout.
    """
    if n < 0:
        raise ValueError("iroot of a negative integer")
    if n == 0:
        return 0
    if k == 1:
        return n
    x = 1 << ((n.bit_length() + k - 1) // k)  # initial guess above the root
    while True:
        y = ((k - 1) * x + n // (x ** (k - 1))) // k
        if y >= x:
            break
        x = y
    return x


def is_perfect_power_k(n, k):
    """True iff n >= 0 is an exact k-th power.  Exact integer arithmetic."""
    r = iroot(n, k)
    return r ** k == n


def perfect_qth_power(n, q):
    """If n is an exact q-th power return its (nonneg) q-th root else None."""
    if n < 0:
        return None
    r = iroot(n, q)
    return r if r ** q == n else None


def is_square(n):
    """Exact integer square test."""
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_prime(n):
    """Trial division for small n (adequate for every use in this workspace)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
