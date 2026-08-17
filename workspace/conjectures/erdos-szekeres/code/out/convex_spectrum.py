#!/usr/bin/env python3
"""Full convex-subset spectrum of the verified es_construct(n): the number of
k-subsets in convex position for each k=3..n-1.  Exact exact-arithmetic via
lib/es_geom.in_convex_position.  n=7 is C(32,3)+C(32,4)+C(32,5)+C(32,6) ~ 1.1M
subsets, feasible and exact; we do NOT enumerate 2^32 subsets, only sizes <= n-1
(the largest convex subset is n-1)."""
from itertools import combinations
from collections import Counter
from time import time
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def spectrum(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    rmax = n - 1  # largest convex subset size
    spec = Counter()
    t0 = time()
    for k in range(3, rmax + 1):
        nconv = 0
        for comb in combinations(range(N), k):
            if in_convex_position([pts[i] for i in comb]):
                nconv += 1
        spec[k] = nconv
        print(f"  n={n} k={k}: convex k-subsets = {nconv}")
    print(f"  n={n}: wall {time()-t0:.2f}s")
    return [spec[k] for k in range(3, rmax + 1)]


def main():
    for n in (5, 6, 7):
        print(f"=== es_construct(n={n}) N={2**(n-2)} ===")
        s = spectrum(n)
        print(f"  SPECTRUM k=3..n-1: {s}")


if __name__ == "__main__":
    main()
