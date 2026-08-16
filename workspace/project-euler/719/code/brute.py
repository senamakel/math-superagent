#!/usr/bin/env python3
"""
Brute-force oracle for Project Euler 719 (S-numbers).

Definition: n is an S-number iff n = m^2 for some integer m >= 2, and the
decimal digit string of n can be split into 2 or more non-empty contiguous
blocks whose values sum to m. T(N) = sum of all S-numbers n <= N.

This oracle, for each root m with m^2 <= N, considers every way of splitting
the digit string of m^2 into contiguous non-empty blocks (leading zeros within
a block are allowed -- each block is treated as its decimal value). If any
split has >= 2 blocks summing to m, then m^2 is an S-number.

It is intentionally naive and obviously correct: it enumerates every partition
of the digit string via all choices of cut positions, then checks each one.
Exact integer arithmetic throughout (Python ints). This is the oracle that the
efficient solver in solution.py is checked against.

Output is written to stdout and to code/out/brute.txt.
"""
import math
import sys
from itertools import combinations


def partitions(s):
    """Yield every split of digit string s into >=2 non-empty contiguous
    blocks, as a tuple of (value, block_string) pairs."""
    L = len(s)
    # a split into k blocks has k-1 cut positions chosen from 1..L-1
    for k in range(2, L + 1):
        for cuts in combinations(range(1, L), k - 1):
            parts = []
            prev = 0
            for c in cuts + (L,):
                parts.append(s[prev:c])
                prev = c
            yield tuple(parts)


def is_s_number(m):
    """m is the root; m^2 must split into >=2 contiguous blocks summing to m.
    Returns the list of (blocks, sum) satisfying splits, or empty list if not
    an S-number."""
    n = m * m
    s = str(n)
    hits = []
    for blocks in partitions(s):
        if sum(int(b) for b in blocks) == m:
            hits.append(blocks)
    return hits


def is_s_number_rec(m):
    """Independent, exact, exhaustive-over-splits route to the same test.
    Tries every split of the digit string of m^2 into contiguous blocks and
    checks whether any >1-block split sums to m. This is the same definition,
    reached by a different code path (recursion with memoization instead of
    enumerating cut combinations), and is used as the route that reaches
    T(10^12) within time budget while the full-enumeration oracle covers the
    small cases."""
    s = str(m * m)
    n = len(s)

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def expr(i):
        # set of all block-sums achievable by splitting suffix s[i:] into one
        # or more contiguous blocks
        res = set()
        val = 0
        for j in range(i, n):
            val = val * 10 + int(s[j])
            if j == n - 1:
                res.add(val)
            else:
                for sub in expr(j + 1):
                    res.add(val + sub)
        return res

    # require >=2 blocks: exclude the trivial single-block split of the whole
    # string. So consider every proper first block summing with the rest to m.
    val = 0
    for j in range(0, n - 1):
        val = val * 10 + int(s[j])
        if (m - val) in expr(j + 1):
            return True
    return False


def T(N):
    """Sum of all S-numbers n <= N, plus the list of (root, square, splits)."""
    total = 0
    found = []  # (m, m^2, list_of_splits)
    limit = int(math.isqrt(N))
    for m in range(2, limit + 1):
        hits = is_s_number(m)
        if hits:
            total += m * m
            found.append((m, m * m, hits))
    return total, found


def T_rec(N):
    """Sum of all S-numbers n <= N using the recursive route."""
    total = 0
    for m in range(2, int(math.isqrt(N)) + 1):
        if is_s_number_rec(m):
            total += m * m
    return total


def main():
    out = []

    def emit(*a):
        line = " ".join(str(x) for x in a)
        out.append(line)
        print(line)

    # ---- 1. reproduce the four worked examples ---------------------------
    emit("=== 1. Worked examples ===")
    for ex in (81, 6724, 8281, 9801):
        m = int(math.isqrt(ex))
        hits = is_s_number(m)
        assert m * m == ex
        emit(f"n={ex} root={m} is S-number? {bool(hits)}  splits={hits}")

    # ---- 2. T(10^4) must equal 41333 -------------------------------------
    emit("")
    emit("=== 2. T(10^4) ===")
    t4, found4 = T(10**4)
    emit(f"T({10**4}) = {t4}")
    emit(f"S-number set for N=10^4 (root, square, splits):")
    for m, sq, hits in found4:
        emit(f"  root={m}  square={sq}  splits={hits}")
    assert t4 == 41333, f"T(10^4) expected 41333, got {t4}"
    emit("CHECK: T(10^4) == 41333  ->  PASS")

    # ---- 3. T(10^6) and T(10^12) ----------------------------------------
    emit("")
    emit("=== 3. Larger reference values ===")
    t6, _ = T(10**6)
    emit(f"T({10**6}) = {t6}")
    t12, _ = T(10**12)
    emit(f"T({10**12}) = {t12}")

    # ---- write to out/brute.txt ------------------------------------------
    import os
    os.makedirs("code/out", exist_ok=True)
    with open("code/out/brute.txt", "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output written to code/out/brute.txt")


if __name__ == "__main__":
    main()
