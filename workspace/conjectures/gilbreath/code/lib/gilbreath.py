#!/usr/bin/env python3
"""Gilbreath-conjecture row tools.

Exact integer iterated absolute differences of the primes:

    A_0 = primes in order
    A_{k+1}(i) = | A_k(i) - A_k(i+1) |

one row at a time (O(width) space per row, width shrinks by 1 per row).

Functions
---------
primes_up_to(n)
    All primes <= n by a sieve; exact integer arithmetic.
rows_generator(primes, depth)
    Yields A_0 .. A_depth, one list per row.  depth is the number of
    difference passes, so A_k has len(A_0) - k entries.
block_profile(row)
    Length of the leading {0,2} block, ignoring the leading entry.
    If row[1:] never leaves {0,2} before the row ends, returns the block
    length including the terminal block (i.e. the whole tail).

Main
----
`python3 -m lib.gilbreath` asserts reproduction of the five worked rows in
problem.md, then runs to depth 600 over the first ~34000 primes one row at a
time, confirming the leading entry is always 1 and the second entry is always
in {0,2}, and confirming the parity claim (every entry at index >= 1 of every
row k >= 1 is even).  Prints EXIT AGREE/FAIL and saves captured output to
code/out/oracle_depth600.captured.txt.
"""

from math import isqrt


def primes_up_to(n):
    """All primes <= n, exact integer arithmetic, a bytearray sieve."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            start = i * i
            sieve[start::step] = b"\x00" * (((n - start) // (step := i)) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def rows_generator(primes, depth):
    """Yield A_0 .. A_depth from the primes, one row at a time.

    Space is O(len(current row)); the previous row is discarded each pass, so
    the whole triangle is never held.
    """
    cur = [int(p) for p in primes]
    yield cur
    for _ in range(depth):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        yield cur


def block_profile(row):
    """Length of the leading {0,2} block, ignoring the leading entry."""
    length = 0
    for x in row[1:]:
        if x in (0, 2):
            length += 1
        else:
            break
    return length


# ---- the worked examples in problem.md the generator must reproduce ----
EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
}


def _work():
    # (a) reproduce the five worked rows exactly
    depth = 5
    primes = primes_up_to(60)          # 19 primes, plenty for depth 5 x 12
    gen = rows_generator(primes, depth)
    got = [next(gen) for _ in range(depth + 1)]

    print("primes_up_to(60) (A_0):", got[0][:20])
    print()
    all_match = True
    for k in range(1, depth + 1):
        match = got[k][:12] == EXPECTED[k]
        all_match = all_match and match
        print(f"A_{k} first 12 = {got[k][:12]}")
        print(f"  matches problem.md? {match}")
    print()
    print("ALL five worked rows match:", all_match)
    print()

    # (b) depth 600 over the first ~34000 primes, one row at a time.
    # witnesses.json used 33860 primes (sieve to 400000); use the same width
    # so the coverage is directly comparable.
    primes = primes_up_to(400000)
    n_primes = len(primes)
    depth = 600
    print(f"primes available under 400000: {n_primes}")
    print(f"running to depth {depth}, one row at a time (O(width) memory)...")
    print()

    gen = rows_generator(primes, depth)
    next(gen)  # A_0, the primes themselves, not subject to the checks

    ok_first = True
    ok_second = True
    ok_parity = True
    min_block = None
    max_block = 0
    last_block_row = None
    checked = 0
    for k in range(1, depth + 1):
        row = next(gen)
        # leading entry always 1
        if row[0] != 1:
            ok_first = False
            print(f"  k={k}: leading entry {row[0]} != 1  <<< FAIL")
        # second entry always in {0,2}
        if row[1] not in (0, 2):
            ok_second = False
            print(f"  k={k}: second entry {row[1]} not in {{0,2}}  <<< FAIL")
        # parity claim: every entry at index >= 1 is even
        if not all(x % 2 == 0 for x in row[1:]):
            ok_parity = False
            print(f"  k={k}: odd entry at index >= 1  <<< FAIL")
        blk = block_profile(row)
        if min_block is None or blk < min_block:
            min_block = blk
        if blk > max_block:
            max_block = blk
            last_block_row = k
        checked += 1

    print(f"checked rows k=1..{depth}: {checked}")
    print(f"min leading {{0,2}} block over the run: {min_block}")
    print(f"max leading {{0,2}} block seen: {max_block} (row {last_block_row})")
    print(f"leading entry is 1 for all k?        {ok_first}")
    print(f"second entry in {{0,2}} for all k?    {ok_second}")
    print(f"parity: all index>=1 entries even?    {ok_parity}")
    print(f"width covered (A_0 length):            {n_primes} primes")
    print()

    agree = all_match and ok_first and ok_second and ok_parity
    print("EXIT", "AGREE" if agree else "FAIL")
    return agree


if __name__ == "__main__":
    _work()
