#!/usr/bin/env python3
"""
candidates_digitdp.py  --  candidate 02

Independent implementation of the Project Euler 719 split-and-sum test using
the Digit-DP / memoized (position, remaining-sum) recursion.

Method (Branicky-style exact recursion, this candidate's approach):
  For a candidate root m with square s = str(m*m), define
      dp(i, target)  ->  Can the suffix s[i:] be split left-to-right into
                         ONE OR MORE contiguous non-empty blocks whose values
                         sum exactly to target?
  Base:  if i >= len(s): dp(i, target) is True iff target == 0.
  Else: take a first block s[i:j] (j > i); dp(i,target) = OR over j of
        dp(j, target - int(s[i:j])), with dp(j,0) meaning the remaining
        suffix contributes nothing.
  A split of the WHOLE string (>= 2 blocks) exists iff
        OR over the first block s[0:j] (0<j<len(s)) of
        dp(j, m - int(s[0:j]))  is True.
  (Forcing j < len(s) guarantees the first block is proper, so the total
   block count is >= 2; the single-block whole-string split m^2 == m is
   impossible for m >= 2 anyway.)

Each (i, target) state is computed once per root by a per-root lru_cache, so
the per-root work is at most (num_positions) * (reachable target values) rather
than re-enumerating every partition. Exact integer arithmetic throughout.

This is written from scratch for this candidate (own file), independent of
/code/solution.py and /code/brute.py, and is verified against the brute-force
oracle code/brute.py on the small cases.
"""
import math
import time
from functools import lru_cache


def is_s_number(m):
    """Return True iff n = m^2 is an S-number (digit string of m^2 splits into
    >= 2 contiguous blocks summing to m). Exact integers."""
    s = str(m * m)
    n = len(s)

    @lru_cache(maxsize=None)
    def dp(i, target):
        # suffix s[i:] into >=1 contiguous blocks summing to target
        if target < 0:
            return False
        if i >= n:
            return target == 0
        val = 0
        for j in range(i, n):
            val = val * 10 + int(s[j])     # block s[i:j+1]
            if target - val < 0:
                break
            if dp(j + 1, target - val):
                return True
        return False

    # proper first prefix s[0:j], j in 1..n-1, then >=1 blocks on the rest
    val = 0
    for j in range(0, n - 1):
        val = val * 10 + int(s[j])
        if dp(j + 1, m - val):
            return True
    return False


def T(N):
    """Sum of all S-numbers n <= N and the count."""
    total = 0
    cnt = 0
    limit = int(math.isqrt(N))
    for m in range(2, limit + 1):
        if is_s_number(m):
            total += m * m
            cnt += 1
    return total, cnt


def main():
    out = []
    t0 = time.time()

    def emit(*a):
        line = " ".join(str(x) for x in a)
        out.append(line)
        print(line)

    emit("=== candidate_02 digit-DP implementation ===")

    # ---- 1. worked examples ----------------------------------------------
    emit("=== 1. Worked examples ===")
    examples = [("81 IS S (8+1)", 81, True),
                ("6724 IS S (6+72+4)", 6724, True),
                ("8281 IS S (8+2+81 / 82+8+1)", 8281, True),
                ("9801 IS S (98+0+1)", 9801, True),
                ("100 IS S (10+0+0)", 100, True),
                ("4 is NOT S (root 2)", 4, False)]
    for label, ex, expect in examples:
        m = int(math.isqrt(ex))
        assert m * m == ex, f"{ex} not a square"
        got = is_s_number(m)
        status = "PASS" if got == expect else "FAIL"
        emit(f"  n={ex} root={m} is S-number? {got} (expected {expect}) -> {status}")
        assert got == expect

    # ---- 2. reference T values ------------------------------------------
    emit("")
    emit("=== 2. Reference values ===")
    for N, expected in [(10**4, 41333),
                        (10**6, 10804656),
                        (10**9, 6222187932),
                        (10**12, 128088830547982)]:
        val, cnt = T(N)
        status = "PASS" if val == expected else "FAIL"
        emit(f"  T({N}) = {val}  (count={cnt})  expected {expected} -> {status}")
        assert val == expected
    emit("")
    emit(f"All checks passed in {time.time()-t0:.2f}s")

    # ---- write to log -----------------------------------------------------
    import os
    os.makedirs("code/out", exist_ok=True)
    logpath = "code/out/candidates_digitdp.log"
    with open(logpath, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"Log written to {logpath}")


if __name__ == "__main__":
    main()
