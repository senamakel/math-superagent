#!/usr/bin/env python3
"""
Efficient solution for Project Euler 719 (S-numbers).

Method: n is an S-number iff n = m^2 and the digit string of n admits a
partition into k >= 2 contiguous blocks summing to m. Rather than scanning all
n <= N (N = 10^12 candidates), scan only the roots m in [2, sqrt(N)] = [2, 10^6]
and test m against the digits of m^2. Work is O(sqrt(N)) root trials, each at
most 13 digits => at most 2^12 = 4096 partitions.

The test is an exact-integer recursive digit-partition check (no floating
point, no enumeration of the answer space). This is the same recursion the
OEIS A038206/A104113 records use.

Result rests on: definitional reduction n = m^2, statement that the partition
must sum to the square root m. For m >= 2 the trivial single-block partition
never equals m (m^2 = m only for m in {0,1}), so any successful partition is
automatically 2+ blocks; we start at m=2 to exclude n=1.
"""
import math
import sys
from functools import lru_cache


def partition_matches(m, s):
    """Return True if digit string s can be split (left-to-right, one or more
    blocks) into blocks whose sum equals m. Used with a proper first prefix
    forced by the caller so the result is always >=2 blocks."""
    @lru_cache(maxsize=None)
    def expr(target, i):
        # can the suffix s[i:] be split (each block contiguous, one or more)
        # into blocks summing to target?
        if target < 0:
            return False
        rest = s[i:]
        if target == int(rest):
            return True          # whole remaining suffix as a single block
        # try first block of lengths 1..len(rest)-1
        for j in range(i + 1, len(s)):
            if expr(target - int(s[i:j]), j):
                return True
        return False

    # force first block to be a proper prefix so total block count >= 2
    for j in range(1, len(s)):
        if expr(m - int(s[:j]), j):
            return True
    return False


def T(N):
    limit = int(math.isqrt(N))
    total = 0
    for m in range(2, limit + 1):
        if partition_matches(m, str(m * m)):
            total += m * m
    return total


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**12
    print(f"T({N}) = {T(N)}")
