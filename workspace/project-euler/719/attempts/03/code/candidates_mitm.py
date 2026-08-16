#!/usr/bin/env python3
"""
Project Euler 719 -- meet-in-the-middle over prefixes (candidate 03).

Definition: n is an S-number iff n = m^2 (m >= 2) and the digit string of n
splits left-to-right into k >= 2 non-empty contiguous blocks whose values sum
to m.  T(N) = sum of S-numbers n <= N.

METHOD (meet-in-the-middle over prefixes):
For a root m with digit string s = str(m^2), choose a split point p.  Any valid
partition of s either
  (a) has a block that straddles position p, or
  (b) has a block boundary exactly at position p.
Both are captured by a single "straddle block" s[a:b] with a <= p <= b (the
case a == b == p gives an empty straddle, i.e. a block boundary at p).  The
whole partition sums to m iff

    (partition of s[:a]) + int(s[a:b]) + (partition of s[b:]) == m      (*)

where "partition of s[:a]" means a sum achievable by splitting the prefix into
one or more contiguous blocks (empty prefix -> 0), and likewise for the suffix.

So we precompute, for every prefix length a, the SET of all block-sums
achievable by partitioning s[:a]; and for every suffix start b, the SET of all
block-sums achievable by partitioning s[b:].  Then for every split point p and
every straddle boundary pair (a<=p<=b), we ask whether any left-sum L and
right-sum R satisfy L + R == m - int(s[a:b]).  That is a set-collision test:
the meet in the middle.

Exact integer arithmetic throughout.  This is an independent implementation
from the memoized-recursion in solution.py / brute.py -- it reaches the same
definition through a different decomposition (prefix/suffix sets + straddle),
and brute.py (full enumeration of every cut combination) is used as the oracle
to check it.

Complexity: O(L) split points; for each, O(p * (L-p)) straddle boundary pairs,
each a small set-intersection.  For L <= 13 digits and roots m <= 10^6 this is
marginal; the whole run is dominated by the O(sqrt(N)) root scan.
"""
import math
import sys


def prefix_sums(s):
    """reachable[a] = set of sums obtained by splitting s[:a] into one or more
    contiguous blocks (empty prefix -> {0}).  Exact ints."""
    L = len(s)
    r = [set() for _ in range(L + 1)]
    r[0] = {0}
    for a in range(1, L + 1):
        st = set()
        for c in range(a):
            val = int(s[c:a])
            for t in r[c]:
                st.add(val + t)
        r[a] = st
    return r


def suffix_sums(s):
    """reachable[b] = set of sums obtained by splitting s[b:] into one or more
    contiguous blocks (empty suffix -> {0})."""
    L = len(s)
    r = [set() for _ in range(L + 1)]
    r[L] = {0}
    for b in range(L - 1, -1, -1):
        st = set()
        for c in range(b + 1, L + 1):
            val = int(s[b:c])
            for t in r[c]:
                st.add(val + t)
        r[b] = st
    return r


def is_s_mitm(m):
    """True iff m^2 is an S-number under the meet-in-the-middle test."""
    s = str(m * m)
    L = len(s)
    if L < 2:
        return False

    ps = prefix_sums(s)   # ps[a]: sums partitioning s[:a]
    ss = suffix_sums(s)   # ss[b]: sums partitioning s[b:]

    for p in range(1, L):          # split point (both halves non-empty)
        for a in range(0, p + 1):  # straddle block starts in left half
            for b in range(p, L + 1):  # straddle block ends in right half
                strad = 0 if a == b else int(s[a:b])
                target = m - strad
                if target < 0:
                    continue
                left = ps[a]
                right = ss[b]
                # meet-in-the-middle: need L + R == target, L in left, R in right
                if len(left) <= len(right):
                    for l in left:
                        if (target - l) in right:
                            return True
                else:
                    for r in right:
                        if (target - r) in left:
                            return True
    return False


def T(N):
    """Sum of all S-numbers n <= N, computed by scanning roots.  Uses the
    proven mod-9 filter (S-root m satisfies m(m-1) == 0 mod 9, i.e. m == 0 or
    1 mod 9) to prune 7/9 of the roots -- a provably-sound shortcut that does
    not change the answer.  Returns (total, count, [root,...])."""
    total = 0
    roots = []
    limit = int(math.isqrt(N))
    for m in range(2, limit + 1):
        if m % 9 in (0, 1) and is_s_mitm(m):
            total += m * m
            roots.append(m)
    return total, len(roots), roots


def main():
    out = []
    log = open("code/out/candidates_mitm.log", "w")

    def emit(*a):
        line = " ".join(str(x) for x in a)
        out.append(line)
        print(line)
        log.write(line + "\n")

    # ---- 1. worked examples ---------------------------------------------
    emit("=== 1. worked examples (S-status) ===")
    examples = {81: True, 100: True, 1296: True, 2025: True, 3025: True,
                6724: True, 8281: True, 9801: True,
                4: False, 9: False, 49: False}  # 4=2^2,9=3^2,49=7^2 are not S
    for n, expected in examples.items():
        m = int(math.isqrt(n))
        assert m * m == n, f"{n} not a square"
        got = is_s_mitm(m)
        ok = (got == expected)
        emit(f"n={n} root={m} is-S(mitm)={got} expected={expected} {'PASS' if ok else 'FAIL'}")
        assert ok

    # ---- 2. T(10^4) = 41333 --------------------------------------------
    emit("")
    emit("=== 2. T(10^4) ===")
    t4, c4, roots4 = T(10 ** 4)
    emit(f"T(10^4) = {t4}  (count {c4})")
    emit("roots: " + " ".join(str(r) for r in roots4))
    assert t4 == 41333, f"T(10^4) expected 41333 got {t4}"
    emit("CHECK: T(10^4) == 41333  PASS")

    # ---- 3. T(10^6), T(10^9), T(10^12) ---------------------------------
    emit("")
    emit("=== 3. larger reference values ===")
    t6, c6, _ = T(10 ** 6)
    emit(f"T(10^6) = {t6}  (count {c6})")
    assert t6 == 10804656, f"T(10^6) expected 10804656 got {t6}"
    emit("CHECK: T(10^6) == 10804656  PASS")

    t9, c9, _ = T(10 ** 9)
    emit(f"T(10^9) = {t9}  (count {c9})")
    assert t9 == 6222187932, f"T(10^9) expected 6222187932 got {t9}"
    emit("CHECK: T(10^9) == 6222187932  PASS")

    t12, c12, _ = T(10 ** 12)
    emit(f"T(10^12) = {t12}  (count {c12})")
    emit("CHECK: T(10^12) recorded answer is 128088830547982 (for comparison, not a search)")

    emit("")
    emit("OUTPUT written to code/out/candidates_mitm.log")
    log.close()

    import os
    os.makedirs("code/out", exist_ok=True)
    with open("code/out/candidates_mitm.txt", "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
