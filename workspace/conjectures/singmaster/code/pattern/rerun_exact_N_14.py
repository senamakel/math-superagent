#!/usr/bin/env python3
"""Re-verify the exact-N(a_i) claim for the infinite family with the SAME
per-column binary-inversion oracle path used in the i=4/i=5 captures, on
i=1..4 (fast; i=5 at 9688 digits takes ~330s and its complete capture is
code/out/extend_exact_N_family_i5.captured.txt).

Purpose: mechanically confirm that the captures N(3003)=8, N(a_2)=N(a_3)=N(a_4)=6
reproduce under this fresh run (the captures are the evidence; a re-run shows
the oracle path itself gives these numbers today).

Convention: N(a) counts BOTH mirrors and the trivial pair C(a,1)=C(a,a-1).
Exact integer arithmetic; no triangle; k bound C(2k,k)>=2^k => k <= floor(log2 a).
"""
import math
import gmpy2


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def comb(n, k):
    return math.comb(int(n), int(k))


def invert_column(a, k):
    """n in [k, inf) with C(n,k)=a, or None.  Binary search, C(n,k) strictly
    increasing in n for fixed k.  Requires C(2k,k) <= a."""
    if comb(2 * k, k) > a:
        return None
    lo, hi = k, k
    while comb(hi, k) < a:
        hi <<= 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if comb(mid, k) <= a:
            lo = mid
        else:
            hi = mid
    return lo if comb(lo, k) == a else None


def exact_half_reps(a):
    """All (n,k), 2<=k<=n/2, with C(n,k)=a, by scanning every live column."""
    reps = []
    kmax = a.bit_length()          # C(2k,k) >= 2^k bound (over-estimate)
    seen_cols = 0
    for k in range(2, kmax + 1):
        if comb(2 * k, k) > a:
            break                  # bigger k only bigger, monotone -> done
        seen_cols += 1
        n = invert_column(a, k)
        if n is not None and 2 * k <= n:
            reps.append((int(n), k))
    return reps, seen_cols


def N_both_mirrors_plus_trivial(reps):
    """Each (n,k) with 2k<n stands for its mirror pair (2); 2k==n (impossible
    for k>=2) would be self-mirror (1).  Plus trivial pair C(a,1),C(a,a-1) = 2."""
    return 2 + sum(1 if 2 * k == n else 2 for (n, k) in reps)


def main():
    print("Convention: N(a) counts BOTH mirrors + trivial pair C(a,1)=C(a,a-1).")
    print("Fresh per-column exact scan (binary inversion, no triangle, k<=bit_length(a)).")
    for i in range(1, 5):
        n = fib(2 * i + 2) * fib(2 * i + 3) - 1
        k = fib(2 * i) * fib(2 * i + 3) - 1
        a = comb(n + 1, k + 1)
        assert comb(n, k + 2) == a
        reps, cols = exact_half_reps(a)
        N = N_both_mirrors_plus_trivial(reps)
        print("i=%d  a digits=%d  live columns=%d  half-reps=%s  N(a)=%d"
              % (i, len(str(a)), cols, reps, N))
    # oracle self-check on a small known value
    reps, cols = exact_half_reps(120)
    print("self-check N(120)=%d (expect 6), reps=%s" % (N_both_mirrors_plus_trivial(reps), reps))
    reps, cols = exact_half_reps(3003)
    print("self-check N(3003)=%d (expect 8), reps=%s" % (N_both_mirrors_plus_trivial(reps), reps))
    print("DONE")


if __name__ == "__main__":
    main()