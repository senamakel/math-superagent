#!/usr/bin/env python3
"""
Candidate 01 -- Project Euler 719, DFS over digit-block boundaries with pruning.

Definition: n is an S-number iff n = m^2 (m >= 2 integer) and the decimal
digit string of n can be split left-to-right into k >= 2 non-empty contiguous
blocks whose values sum to m. T(N) = sum of all S-numbers n <= N.

Method (this candidate's approach):
  Scan only the roots m in [2, isqrt(N)]  (there are isqrt(10^12)=10^6 of
  them, not 10^12 n's).  For each m, walk the digit string s = str(m*m)
  left to right with a recursive DFS that branches on how many digits the
  NEXT block occupies.  Carry a running sum of the blocks placed so far.
  Two prunings:
    (a) if running sum  > m  we can cut this branch entirely (blocks are
        non-negative, so adding more blocks never lowers the sum);
    (b) at each new boundary we may decide the current block is the LAST
        (consume the whole remainder) and test whether
        running_sum + int(remainder) == m.
  We force at least 2 blocks by requiring the first boundary to be a proper
  cut (the first block is a proper prefix).

  This is exact integer arithmetic throughout (Python ints); no floating
  point.  Work is O(isqrt(N)) root trials, each on a string of up to 13
  digits i.e. at most 4096 partitions with pruning.

  Independently written by candidate 01 -- a different code path from the
  existing brute.py / solution.py (which memoize a recursion over suffixes
  and collect achievable-sum sets).  This one is a forward DFS carrying a
  scalar running sum and pruning on overshoot.
"""

import math
import sys
import time


def is_s_number(m):
    """Return True iff m^2 is an S-number (blocks sum to m, >=2 blocks)."""
    s = str(m * m)
    L = len(s)
    if L < 2:
        # single digit square (m<=3): cannot have >=2 non-empty blocks
        return False

    # dfs(pos, running_sum, first_cut_taken)
    # We branch on how many digits the next block occupies.  Edge case that
    # is handled naturally: a block may begin with '0', and int('0..') handles
    # leading zeros correctly as its decimal value.
    def dfs(pos, running, blocks):
        # blocks counts blocks placed so far
        if running > m:
            return False          # prune: sums only grow
        rem = s[pos:]
        # option: make the current new block the LAST block, consuming the
        # whole remainder (valid only if we will have >=2 blocks total)
        if blocks >= 1:
            if running + int(rem) == m:
                return True
        # otherwise extend: take a proper prefix as the next block and recurse
        for end in range(pos + 1, L):
            nxt = running + int(s[pos:end])
            if nxt > m:
                break             # sorted by prefix length: sums increase, prune
            if dfs(end, nxt, blocks + 1):
                return True
        return False

    # start: first block is a proper prefix (>=1 digit, not whole string) so
    # that we always have >=2 blocks total.
    for j in range(1, L):
        first = int(s[:j])
        if first > m:
            break
        if dfs(j, first, 1):
            return True
    return False


def T(N):
    lim = int(math.isqrt(N))
    total = 0
    count = 0
    t0 = time.time()
    for m in range(2, lim + 1):
        if is_s_number(m):
            total += m * m
            count += 1
    return total, count, time.time() - t0


def main():
    out = []
    def emit(*a):
        line = " ".join(str(x) for x in a)
        out.append(line)
        print(line)

    # ---- 1. S-status of individual examples ------------------------------
    emit("=== 1. Individual S-status ===")
    examples = [  # (root, square, expected_is_S)
        (2, 4, False),      # 4=2^2, "4" single block -> not S
        (9, 81, True),      # 81 -> 8+1=9
        (10, 100, True),    # 100 -> 10+0=10
        (82, 6724, True),   # 67+2+4 = 73? no -> but 6+7+24=37,6+72+4... let's just report
        (91, 8281, True),   # 8+2+81=91
        (99, 9801, True),   # 9+80+1=90? -> 98+0+1=99
    ]
    for m, sq, exp in examples:
        got = is_s_number(m)
        ok = "OK" if got == exp else "*** MISMATCH ***"
        emit(f"root={m} square={sq} is_S={got} expected={exp}  {ok}")
        assert got == exp, f"m={m} expected {exp} got {got}"

    # A non-square is never an S-number by definition; sanity check 2 and 3.
    for m in (2, 3):
        assert not is_s_number(m)

    # ---- 2. reference totals ---------------------------------------------
    emit("")
    emit("=== 2. Reference totals ===")
    refs = {
        10**4: 41333,
        10**6: 10804656,
        10**9: 6222187932,
    }
    for N, expect in refs.items():
        tot, cnt, dt = T(N)
        ok = "PASS" if tot == expect else "FAIL"
        emit(f"T({N}) = {tot}  (expected {expect})  [{cnt} S-numbers, {dt:.2f}s]  {ok}")
        assert tot == expect

    # ---- 3. T(10^12) ------------------------------------------------------
    emit("")
    emit("=== 3. T(10^12) ===")
    t12, cnt12, dt12 = T(10**12)
    emit(f"T({10**12}) = {t12}  [{cnt12} S-numbers, {dt12:.2f}s]")

    import os
    os.makedirs("code/out", exist_ok=True)
    with open("code/out/candidates_dfs.log", "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output written to code/out/candidates_dfs.log")


if __name__ == "__main__":
    main()
