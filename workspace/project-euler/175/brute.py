#!/usr/bin/env python3
"""
brute.py  -- naive, obviously-correct computation for Project Euler 175.

f(0) = 1.
For n >= 1, f(n) = number of ways to write n as a sum of powers of 2 where
no power of 2 occurs more than twice (each 2^k used 0, 1, or 2 times).

Method: bounded-multiplicity coin DP over coin values 2^k (each usable 0..2
times).  dp[j] = number of multisets summing to j.

Complexity: O(N log N) time, O(N) space, with N the largest target.
"""


def f_table(max_n):
    """Return list f[0..max_n] of the counts."""
    dp = [0] * (max_n + 1)
    dp[0] = 1
    k = 0
    c = 1  # 2^k
    while c <= max_n:
        # Add 1 and 2 copies of coin value c (each used 0,1,2 times total).
        for copies in (1, 2):
            step = copies * c
            for j in range(max_n, step - 1, -1):
                dp[j] += dp[j - step]
        k += 1
        c *= 2
    return dp


def shortened_binary_expansion(n):
    """Runs of equal bits, most-significant first, as a list of run lengths."""
    bits = bin(n)[2:]          # e.g. '11110001'
    runs = []
    cur = bits[0]
    length = 1
    for b in bits[1:]:
        if b == cur:
            length += 1
        else:
            runs.append(length)
            cur = b
            length = 1
    runs.append(length)
    return bits, runs


def main():
    print("=" * 60)
    print("Project Euler 175 -- naive brute.py")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 1 & 2. Sanity table f(0..20) and check f(10) == 5
    # ------------------------------------------------------------------
    N = 10000  # big enough for all needed checks
    f = f_table(N)

    print("\n[1] f(0)..f(20):")
    for n in range(21):
        print(f"    f({n:2d}) = {f[n]}")

    print("\n[2] Sanity check: f(10) == 5 ->", f[10] == 5, "(f(10) = %d)" % f[10])
    assert f[10] == 5, "f(10) should be 5"

    # ------------------------------------------------------------------
    # 3. Worked example: n = 241, ratio f(241)/f(240) == 13/17
    # ------------------------------------------------------------------
    from fractions import Fraction
    ratio = Fraction(f[241], f[240])
    print("\n[3] Worked example n=241:")
    print(f"    f(240) = {f[240]}")
    print(f"    f(241) = {f[241]}")
    print(f"    f(241)/f(240) = {ratio}  (as Fraction)")
    print(f"    equals 13/17? ->", ratio == Fraction(13, 17))

    # Verify smallest n with ratio 13/17 by scanning 1..245.
    target = Fraction(13, 17)
    first_n = None
    for n in range(1, 246):
        if Fraction(f[n], f[n - 1]) == target:
            first_n = n
            break
    print(f"    first n in 1..245 with f(n)/f(n-1)==13/17 -> {first_n}")
    print(f"    first_n == 241 ? ->", first_n == 241)

    # ------------------------------------------------------------------
    # 4. Empirically derive recurrences: compare odd/even around doubles.
    # ------------------------------------------------------------------
    print("\n[4] Recurrence exploration (n in 1..40):")
    print("     n | f(2n-1) f(2n) f(2n+1) | f(n-1) f(n) f(n+1)")
    for n in range(1, 41):
        print(f"   {n:3d} | {f[2*n-1]:6d} {f[2*n]:6d} {f[2*n+1]:6d}"
              f" | {f[n-1]:6d} {f[n]:6d} {f[n+1]:6d}")

    # ------------------------------------------------------------------
    # 5. Binary expansion and SBE of 241
    # ------------------------------------------------------------------
    bits, runs = shortened_binary_expansion(241)
    print("\n[5] n = 241:")
    print(f"    binary expansion = {bits}")
    print(f"    SBE (MSB first) = {runs}")
    print(f"    matches 4,3,1 ? ->", runs == [4, 3, 1])


if __name__ == "__main__":
    main()
