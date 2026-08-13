#!/usr/bin/env python3
"""Exact binomial-coefficient multiplicity oracle for Singmaster's conjecture.

`multiplicity(a, n_max)` counts every (n,k) with 0<=k<=n<=n_max and C(n,k)=a,
in exact integer arithmetic, by inverting C(n,k)=a for each k (binary search in
n) rather than building the triangle.

Counting convention (matches code/out/witnesses.json):
    counts BOTH mirrored occurrences (C(n,k) and C(n,n-k) are two distinct
    pairs) and includes the trivial pair C(a,1)=C(a,a-1).

So an `a` with exactly one nontrivial canonical rep (n,k), 2<=k<=n/2, reports
N(a)=4, and the record 3003 reports 8.

Correctness: a canonical rep (n,k) with k>=2 satisfies a=C(n,k)>=C(2k,k)>=2^k,
so k<=log2(a); for fixed k, C(n,k) is strictly increasing in n (n>=k), so the
binary search finds the unique n with C(n,k)=a.  Each canonical rep (n,k) with
1<=k<=n/2 contributes 2 occurrences (mirror pair) unless k==n/2 (central, its
own mirror, contributes 1).  Cross-checked against the direct-O(n_max^2)
enumeration oracle in code/brute.py for every a in the witness set.
"""

from math import comb

CONVENTION = (
    "N(a) counts BOTH mirrored occurrences (C(n,k) and C(n,n-k) are two "
    "distinct pairs) and includes the trivial pair C(a,1) = C(a,a-1)."
)


def canonical_reps(a, n_max):
    """All (n,k), 1<=k<=n/2, n<=n_max with C(n,k)=a, via inversion.

    Each returned (n,k) stands for both itself and its mirror (n,n-k).  The
    trivial rep (a,1) is included when n_max >= a.
    """
    reps = set()
    # k <= log2(a): a = C(n,k) >= C(2k,k) >= 2^k forces k <= floor(log2 a).
    k_max = a.bit_length()
    for k in range(1, k_max + 1):
        if k > n_max:
            break
        if comb(n_max, k) < a:
            continue
        lo, hi = k, n_max
        while lo < hi:
            mid = (lo + hi) // 2
            if comb(mid, k) >= a:
                hi = mid
            else:
                lo = mid + 1
        n = lo
        if n <= n_max and comb(n, k) == a:
            kk = min(k, n - k)
            if 1 <= kk and 2 * kk <= n:
                reps.add((n, kk))
    return reps


def multiplicity(a, n_max):
    """N(a) over all 0<=k<=n<=n_max; both mirrors + trivial pair."""
    total = 0
    for (n, k) in canonical_reps(a, n_max):
        total += 1 if 2 * k == n else 2
    return total


def nontrivial_reps(a, n_max):
    """Canonical reps with 2<=k<=n/2 (trivial pair C(a,1) excluded)."""
    return sorted((n, k) for (n, k) in canonical_reps(a, n_max)
                  if not (n == a and k == 1))


if __name__ == "__main__":
    # Self-check against the witness set.
    assert multiplicity(3003, n_max=3003) == 8
    for v in (120, 210, 1540, 7140, 11628, 24310):
        assert multiplicity(v, n_max=v) == 6, v
    print("self-check PASS: 3003->8, and 120,210,1540,7140,11628,24310 all ->6")
