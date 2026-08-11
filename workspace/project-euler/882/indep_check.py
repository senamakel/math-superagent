#!/usr/bin/env python3
"""Independent verification of Project Euler 882 answer.

Deliberately DIFFERENT method from solution.py / verify_dyadic.py:

  * g(k) is computed by DIRECT RECURSIVE surreal-value evaluation:
        g(0) = 0
        g(k) = simplest_dyadic_between( max{ g(j) : j a 1-deletion of k },
                                        min{ g(j) : j a 0-deletion of k } )
    with memoization on k (children are always < k, so recursion terminates).
    solution.py / verify_dyadic.py instead use a forward ascending sweep.

  * simplest_dyadic_between(a, b) is written here FROM SCRATCH as a pure
    birthday scan: for each denominator 1, 2, 4, ..., 2^25 it enumerates the
    integers m with a < m/2^d < b, scores each dyadic by its CGT birthday
    (minimal birthday = "simplest", the Simplicity Rule), and returns the
    candidate of globally minimal birthday.  solution.py imports the
    toolkits.simplest_dyadic structural routine instead.

  * The sum G(N) = sum_{k=1..N} k*g(k) is accumulated in exact Fraction
    arithmetic and reported as numerator/denominator with a
    numerator-divisible-by-denominator (integer) check and S = ceil(G(N)).

Birthday of a dyadic (as used in toolkits/test_simplest_dyadic.py): integer n
has birthday |n|; a non-integer dyadic x with |x|=n+f (0<f<1, f=m/2^d reduced,
m odd) has birthday n + d + 1.

Complexity: each g(k) does a birthday scan to 2^25 in the worst case, but the
simplest dyadic always has small denominator, so the scan exits early in
practice; recursion + memoization makes the whole sweep O(N * log N).
"""
import sys
from fractions import Fraction
from math import ceil


def one_deletions(x):
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '1':
            t = s[:i] + s[i + 1:]
            out.add(0 if t == '' else int(t, 2))
    return out


def zero_deletions(x):
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '0':
            t = s[:i] + s[i + 1:]
            out.add(0 if t == '' else int(t, 2))
    return out


def birthday(x):
    """CGT birthday of a dyadic Fraction (see module docstring)."""
    x = abs(x)
    if x == 0:
        return 0
    n = x.numerator // x.denominator        # floor(abs)
    f = x - n
    if f == 0:
        return n
    d = 0
    while f.denominator > 1:
        f *= 2
        d += 1
    return n + d + 1


def _dyadics_of_birthday(b):
    """Generator of all dyadics whose CGT birthday is exactly b (|.| bounded).

    Dyadic |x| = n + m/2^d with m odd has birthday n+d+1; integer n has
    birthday |n|.  Yields both x and -x.  Bound n by b so all are finite.
    """
    # integers with birthday b
    if b > 0:
        yield Fraction(b)
        yield Fraction(-b)
    # non-integers
    for n in range(0, b):            # n+d+1 = b  =>  d = b-n-1
        d = b - n - 1
        if d < 1:
            continue
        for m in range(1, (1 << d), 2):   # m odd in [1, 2^d - 1]
            f = Fraction(m, (1 << d))
            yield Fraction(n) + f
            yield -(Fraction(n) + f)


def simplest_dyadic_between(a, b):
    """Simplest dyadic strictly between a<b, by birthday-ordered scan.

    a, b are exact Fractions (dyadic), or None meaning -inf/+inf.  Enumerates
    dyadics in increasing CGT birthday and returns the first lying strictly in
    the open interval.  Independent from-scratch routine distinct from
    toolkits.simplest_dyadic.
    """
    BDAY_CAP = 60
    for bday in range(0, BDAY_CAP + 1):
        for v in _dyadics_of_birthday(bday):
            if a is not None and not (a < v):
                continue
            if b is not None and not (v < b):
                continue
            return v
    raise RuntimeError(f"no dyadic found in ({a},{b}) up to birthday {BDAY_CAP}")


_g_memo = {0: Fraction(0)}


def g(k):
    """Surreal value of single-number game k, recursive + memoized."""
    if k in _g_memo:
        return _g_memo[k]
    L = [g(j) for j in one_deletions(k)]
    R = [g(j) for j in zero_deletions(k)]
    lo = max(L) if L else None
    hi = min(R) if R else None
    val = simplest_dyadic_between(lo, hi)
    _g_memo[k] = val
    return val


def main():
    N = int(sys.argv[1])
    G = Fraction(0)
    for k in range(1, N + 1):
        G += k * g(k)
    num, den = G.numerator, G.denominator
    integer = (num % den == 0)
    S = ceil(G)
    print(f"N = {N}")
    print(f"G(N) = {num} / {den}")
    print(f"numerator % denominator == 0 (G integer): {integer}")
    print(f"G(N) float = {float(G):.4f}")
    print(f"S(N) = ceil(G(N)) = {S}")


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 7)
    main()
