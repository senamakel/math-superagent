"""Exact U_d(a) = max over A subset E, |A|=a of |O_{<=d}(A)|, and d*(n).

d*(n) = max d such that U_d(a) <= 2^{n-1} - a for all a = 0..2^{n-1}. This is
the strongest d for which G1's contrapositive fires, so the best lower bound
this entire bipartite-threshold-shadow route can deliver is f(n) >= d*(n)+1.
If d*(n) is not omega(log n), G-threshold-analysis is refuted.

n <= 5: |E| = 2^{n-1} <= 16, exhaustive over all A subset E is small.
"""
from itertools import combinations


def popcount(x):
    return bin(x).count("1")


def is_edge(u, v):
    d = u ^ v
    return d & (d - 1) == 0


def O_leq_d(n, A, d):
    Aset = set(A)
    Oset = [v for v in range(1 << n) if popcount(v) & 1]
    return sum(1 for x in Oset
               if sum(1 for a in Aset if is_edge(x, a)) <= d)


def worst_gap(n, d):
    """max over a of U_d(a) - (half - a)."""
    half = 1 << (n - 1)
    E = [v for v in range(1 << n) if not (popcount(v) & 1)]
    worst, wa = -10**9, None
    for a in range(0, half + 1):
        U = max(O_leq_d(n, A, d) for A in combinations(E, a))
        gap = U - (half - a)
        if gap > worst:
            worst, wa = gap, a
    return worst, wa


def dstar(n):
    for d in range(0, n + 1):
        g, _ = worst_gap(n, d)
        if g > 0:
            return d - 1
    return n


if __name__ == "__main__":
    for n in range(1, 6):
        print(f"--- n={n} half={1<<(n-1)} ---")
        for d in range(0, n + 1):
            w, a = worst_gap(n, d)
            print(f"  d={d}: worst_gap={w:3d} at a={a:2d} hold={'YES' if w<=0 else 'no'}")
    dv = [dstar(n) for n in range(1, 6)]
    print("d*(n) n=1..5:", dv)
    print("best lower bound d*(n)+1:", [x + 1 for x in dv])
    import math
    print("log2(n) n=1..5:", [round(math.log2(x), 3) for x in range(1, 6)])
