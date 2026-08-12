"""PE346 independent solver, route 3: LENGTH-major enumeration.

Structural fact (established and oracle-checked in this run): n>1 is a strong
repunit (repunit in >=2 bases b>1) iff it is a repunit of length k>=3 in some
base b>1, because the length-2 repunit "11" in base n-1 is always the second
base.  The number 1 is strong on its own.  So the set of strong repunits below
N is {1} union { (b^k-1)/(b-1) : b>=2, k>=3, value <= N }.

Loop structure (transposed from every other solver in this folder, which is
base-major: outer over b, inner over k):
    for k in 3,4,... while 2^k - 1 <= N:      # smallest base is b=2
        for b in 2,3,... while (b^k-1)/(b-1) <= N:
            add (b^k-1)/(b-1) to the set

Exact integer arithmetic only: each r is computed directly as
(pow(b, k) - 1)//(b - 1) -- Python's pow is exact integer arithmetic, and //
is exact floor division.  No floats anywhere.

Complexity: for fixed k the base loop runs while b^(k-1) < N, i.e. ~N^(1/(k-1))
bases; the k-loop runs while 2^k-1 <= N, i.e. k <= log2(N+1).  Total
~ sum_{k=3}^{log2 N} N^(1/(k-1)) = O(sqrt(N)) pair visits (the k=3 term
~sqrt(N) dominates; every later term is o(sqrt(N)) and the sum converges).
Time O(sqrt(N)), space O(sqrt(N)) for the value set.  This scales with the
count of (b,k) pairs, not with N, so N=10^12 is fine (~10^6 visits).
"""
import sys


def strong_repunits(N):
    """Return the set of strong repunits <= N, length-major enumeration."""
    s = set()
    if N >= 1:
        s.add(1)
    k = 3
    while (1 << k) - 1 <= N:          # b=2 gives the smallest length-k repunit
        b = 2
        while True:
            r = (pow(b, k) - 1)//(b - 1)   # exact, direct repunit value
            if r > N:
                break
            s.add(r)
            b += 1
        k += 1
    return s


def route3(N):
    """Return (sum, count) of strong repunits <= N, printing a per-k base
    distribution (sanity check: bases per k must shrink as k grows)."""
    s = set()
    if N >= 1:
        s.add(1)
    k = 3
    print("k  bases")
    while (1 << k) - 1 <= N:
        b = 2
        cnt = 0
        while True:
            r = (pow(b, k) - 1)//(b - 1)
            if r > N:
                break
            s.add(r)
            cnt += 1
            b += 1
        print(f"{k:2d} {cnt:9d}")
        k += 1
    return sum(s), len(s)


if __name__ == "__main__":
    # Worked-example assertions from the statement (PE346 gives: below 50 the
    # strong repunits are the 8 numbers {1,7,13,15,21,31,40,43} summing to
    # 171; below 1000 there are 47 summing to 15864).
    w50 = strong_repunits(50)
    assert sorted(w50) == [1, 7, 13, 15, 21, 31, 40, 43], sorted(w50)
    assert sum(w50) == 171, sum(w50)
    w1000 = strong_repunits(1000)
    assert len(w1000) == 47, len(w1000)
    assert sum(w1000) == 15864, sum(w1000)
    print("PASS: below 50  -> count 8, sum 171")
    print("PASS: below 1000 -> count 47, sum 15864")

    N = 10**12
    print("N =", N)
    total, count = route3(N)
    print("sum   =", total)
    print("count =", count)