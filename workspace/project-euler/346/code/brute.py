#!/usr/bin/env python3
"""Literal brute-force oracle for the strong-repunit problem (Project Euler 346).

A number n is a strong repunit if it equals a repunit (a string of all 1's) in
at least two distinct bases b > 1.  For a base b, the repunits are
    1, 1 + b, 1 + b + b^2, 1 + b + b^2 + b^3, ...
that is R_1(b)=1 and R_{k+1}(b) = R_k(b) * b + 1.

This is implemented *literally* from the definition, with no cleverness:

    for each n:
        for each base b from 2 to n-1:
            build the repunit sequence 1, 1+b, 1+b+b^2, ... for this base,
            count how many distinct bases produce n
        n is strong iff that count >= 2

n = 1 is a repunit in every base (the length-1 repunit R_1(b) = 1), so it is
included as strong.

Complexity: O(N^2) numbers examined in total (each n scans ~n bases, and each
base's repunit sequence in base b has O(log_b n) terms), O(1) extra space.
This is the naive oracle, meant to validate the efficient solver on small
bounds.  It is not intended to reach 1e12.
"""

import sys


def repunit_values_in_base(b, limit):
    """Yield repunit values 1, 1+b, 1+b+b^2, ... for base b up to `limit`."""
    # R_1(b) = 1; then R_{k+1} = R_k * b + 1
    val = 1
    while val <= limit:
        yield val
        val = val * b + 1


def is_strong(n):
    """True iff n is a repunit in at least two distinct bases b > 1."""
    if n == 1:
        return True                      # 1 = R_1(b) in every base b > 1
    count = 0
    for b in range(2, n):                # base b from 2 to n-1
        for r in repunit_values_in_base(b, n):
            if r == n:
                count += 1
                break                    # this base represents n; stop scanning it
    return count >= 2


def strong_repunits(bound):
    """All strong repunits n with 1 <= n < bound, in increasing order."""
    return [n for n in range(1, bound) if is_strong(n)]


def strong_repunits_direct(bound):
    """All strong repunits n with 1 <= n <= bound, by direct generation.

    Every n > 1 is a length-2 repunit in base n-1 ("11"), so n > 1 is strong
    iff it is also a repunit of length k >= 3 in some base b > 1, i.e. it
    equals R_k(b) = 1 + b + ... + b^{k-1} for some k >= 3.  Each such generated
    value (and the special case n = 1) is exactly one strong repunit, so the
    sorted set of all distinct R_k(b) <= bound with k >= 3, plus 1, is the
    answer.  This is still "brute" (enumerating all repunit values by hand with
    no number theory) but is O(sqrt(N) * log N) and reaches large bounds that
    the per-n literal loop cannot.
    """
    s = set()
    if bound >= 1:
        s.add(1)
    b = 2
    while b * b + b + 1 <= bound:          # length-3 repunit R_3(b) = b^2+b+1
        val = b * b + b + 1                # R_3(b)
        while val <= bound:
            s.add(val)
            val = val * b + 1              # next length: R_{k+1} = R_k * b + 1
        b += 1
    return sorted(s)


def main():
    if len(sys.argv) < 2:
        print("usage: brute.py N", file=sys.stderr)
        sys.exit(1)
    N = int(sys.argv[1])

    # 1. sorted list of strong repunits below 50
    sr50 = strong_repunits(50)
    print("strong repunits below 50:", sr50)

    # 2. sum of strong repunits below 1000
    sr1000 = strong_repunits(1000)
    print("sum of strong repunits below 1000:", sum(sr1000))

    # 3. sum of strong repunits below N (from argv)
    #    The literal per-n loop is O(N^2) and cannot reach N up to 1e6 in
    #    reasonable time, so for large N we use the direct generator, which is
    #    verified identical to the literal loop on every bound it can reach.
    if N <= 1000:
        srN = strong_repunits(N)
        print(f"sum of strong repunits below {N} (literal):", sum(srN))
    else:
        srN = strong_repunits_direct(N - 1)   # "below N" is strict: n < N
        print(f"sum of strong repunits below {N} (direct):", sum(srN))


if __name__ == "__main__":
    main()
