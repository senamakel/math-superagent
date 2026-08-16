#!/usr/bin/env python3
"""
Candidate 01 -- Project Euler 719, DFS over digit-block boundaries with pruning.

Definition: n is an S-number iff n = m^2 (m >= 2 integer) and the decimal
digit string of n can be split left-to-right into k >= 2 non-empty contiguous
blocks whose values sum to m. T(N) = sum of all S-numbers n <= N.

Method (this candidate's approach):
  Scan only the roots m in [2, isqrt(N)]  (isqrt(10^12)=10^6 of them).
  For each m, walk the digit string s = str(m*m) left to right with a
  recursive DFS branching on how many digits the NEXT block occupies,
  carrying a running sum of block-values placed so far.  Prune when the
  running sum already exceeds m (block-values are non-negative, so the sum
  never decreases).  Force >=2 blocks by requiring the first block to be a
  proper prefix.  Exact integer arithmetic throughout.

  Two extra exact accelerations, both provable:
   (1) mod-9 filter: for an S-number every block-value == its digit-sum
       (mod 9) since 10^k==1 (mod 9); block-sum == m == m^2 (mod 9), so
       m(m-1)==0 (mod 9), i.e. m == 0 or 1 (mod 9).  Skips 7/9 of roots,
       exactly.
  Work is O(isqrt(N)) root trials, each on a string of up to 13 digits
  (at most 2^12 = 4096 partitions) with pruning.
"""
import math
import time


def is_s_number(m):
    """Return True iff m^2 is an S-number (>=2 blocks summing to m)."""
    s = str(m * m)
    L = len(s)
    if L < 2:
        return False

    def dfs(pos, running, blocks):
        # blocks = number of blocks placed so far.
        if running > m:
            return False          # prune: sums only grow
        rem = s[pos:]
        # option: current new block is the LAST (consume whole remainder);
        # valid only if we end with >=2 blocks total.
        if blocks >= 1:
            if running + int(rem) == m:
                return True
        # otherwise take a proper prefix as the next block and recurse.
        for end in range(pos + 1, L):
            nxt = running + int(s[pos:end])
            if nxt > m:
                break             # prefix sums increase with length: prune
            if dfs(end, nxt, blocks + 1):
                return True
        return False

    # first block is a proper prefix so total block count >= 2.
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
    # mod-9 filter: m == 0 or 1 (mod 9) for S-roots.
    for m in range(2, lim + 1):
        if m % 9 not in (0, 1):
            continue
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

    emit("=== 1. Individual S-status ===")
    examples = {  # root: (square, expected_is_S)
        2: (4, False),
        9: (81, True),
        10: (100, True),
        82: (6724, True),
        91: (8281, True),
        99: (9801, True),
    }
    for m, (sq, exp) in examples.items():
        got = is_s_number(m)
        ok = "OK" if got == exp else "*** MISMATCH ***"
        emit(f"root={m} square={sq} is_S={got} expected={exp}  {ok}")

    emit("")
    emit("=== 2. Reference totals ===")
    refs = {10**4: 41333, 10**6: 10804656, 10**9: 6222187932}
    for N, expect in refs.items():
        tot, cnt, dt = T(N)
        ok = "PASS" if tot == expect else "FAIL"
        emit(f"T({N}) = {tot}  (expected {expect})  [{cnt} S-numbers, {dt:.2f}s]  {ok}")
        assert tot == expect

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
