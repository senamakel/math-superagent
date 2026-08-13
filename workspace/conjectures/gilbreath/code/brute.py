#!/usr/bin/env python3
"""Naive oracle for Gilbreath's conjecture.

Generates the iterated absolute-difference rows A_0..A_D of the primes by the
literal definition:

    A_0 = primes in order
    A_{k+1}(i) = | A_k(i) - A_k(i+1) |

exact integer arithmetic, one row at a time.  This is the obviously-correct
checker the whole investigation is measured against.  It is NOT fast and NOT
meant to be: the point is to pin down what the statement means and to reproduce
the worked examples in problem.md exactly.

Checks performed against the problem statement's given rows:

    A_1 = 1,2,2,4,2,4,2,4,6,2,6,4
    A_2 = 1,0,2,2,2,2,2,2,4,4,2,2
    A_3 = 1,2,0,0,0,0,0,2,0,2,0,0
    A_4 = 1,2,0,0,0,0,2,2,2,2,0,0
    A_5 = 1,2,0,0,0,2,0,0,0,2,0,2
"""

from math import isqrt


def primes_up_to(n):
    """Primes <= n by a sieve; exact integer arithmetic."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start::step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def rows(primes, depth):
    """Yield A_0 .. A_depth, one list per row, from the primes.

    depth is the number of difference passes.  Width shrinks by exactly 1 per
    row: A_k has len(A_0) - k entries.
    """
    cur = list(primes)
    yield cur
    for _ in range(depth):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        yield cur


def block_profile(row):
    """Length of the leading {0,2} block, ignoring the leading 1."""
    length = 0
    for x in row[1:]:
        if x in (0, 2):
            length += 1
        else:
            break
    return length


# ---- the worked examples the oracle must reproduce exactly ----
EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
}


def main():
    # How many primes do we need?  A_k has len(A_0) - k entries at its
    # original-width coordinates, though after slicing it keeps shrinking.
    # To get 12 entries of A_5 we need len(A_0) - 5 >= 12, i.e. >= 17 primes.
    depth = 5
    primes = primes_up_to(60)  # plenty (19 primes up to 60) for depth 5 x 12
    gen = rows(primes, depth)
    got = [next(gen) for _ in range(depth + 1)]

    print("primes (A_0):", got[0][:20])
    print()
    all_match = True
    for k in range(1, depth + 1):
        match = got[k][:12] == EXPECTED[k]
        all_match = all_match and match
        print(f"A_{k} first 12 = {got[k][:12]}")
        print(f"  matches problem.md? {match}")
    print()
    print("ALL worked examples match:", all_match)

    # Extra self-consistency checks the conjecture is about.
    print()
    print("shape / parity checks per row:")
    for k in range(1, depth + 1):
        row = got[k]
        first_one = row[0] == 1
        # entries after the first must all be even (the (odd, even, even,...) shape)
        all_even = all(x % 2 == 0 for x in row[1:])
        second_02 = row[1] in (0, 2)
        block = block_profile(row)
        print(f"  k={k}: first=1? {first_one}  rest even? {all_even}  "
              f"second in {{0,2}}? {second_02}  leading_02_block={block}")


if __name__ == "__main__":
    main()
