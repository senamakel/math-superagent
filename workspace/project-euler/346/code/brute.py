"""Naive oracle for Project Euler 346 (strong repunits).

A repunit in base b is a number whose base-b representation is a string of
all 1's, i.e. R_k(b) = 1 + b + b^2 + ... + b^(k-1) = (b^k - 1)/(b - 1) for
k >= 1.  The length-1 repunit equals 1, whatever the base, so the number 1 is
a repunit in every base.

A strong repunit is a positive integer that is a repunit in at least two
distinct bases b > 1.

This file implements the definition directly, without any cleverness: for
each n it counts, over every base 2 <= b <= n, how many bases represent n as
a repunit, and reports n as strong when the count is at least 2.  It is the
oracle the efficient solver is checked against.
"""


def is_repunit(n, b):
    """True iff n is a repunit (string of all 1's) in base b, b > 1."""
    if n == 1:
        return True          # R_1(b) = 1 in every base
    if b < 2:
        return False
    # build repunits R_k(b) = (b^k-1)/(b-1) for k = 2, 3, ... while <= n
    val = 1 + b              # R_2(b)
    while val <= n:
        if val == n:
            return True
        val = val * b + 1    # next length: R_{k+1} = R_k * b + 1
        if val < 0:          # guard against runaway growth (unused here)
            break
    return False


def base_count(n):
    """Number of bases b in [2, n] in which n is a repunit."""
    if n == 1:
        # R_1(b) = 1 for every base b > 1, so 1 is a repunit in all bases
        # and hence a strong repunit.
        return 2
    return sum(1 for b in range(2, n + 1) if is_repunit(n, b))


def strong_repunits(bound):
    """All strong repunits n with 1 <= n < bound, in increasing order."""
    return [n for n in range(1, bound) if base_count(n) >= 2]


if __name__ == "__main__":
    for bound in (50, 1000):
        s = strong_repunits(bound)
        print(f"below {bound}: {s}")
        print(f"  count = {len(s)}, sum = {sum(s)}")
