#!/usr/bin/env python3
"""n=8: convex 4-subset count of es_construct(8) (N=64 points). C(64,4)=635k
subsets, exact oracle.  k=3 is trivially C(64,3)=41664 (general position)."""
from itertools import combinations
from time import time
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    k = 4
    nconv = 0
    t0 = time()
    for comb in combinations(range(N), k):
        if in_convex_position([pts[i] for i in comb]):
            nconv += 1
    print(f"n={n} N={N} k={k}: convex {k}-subsets = {nconv}  (C({N},{k})={__import__('math').comb(N,k)})")
    print(f"wall {time()-t0:.2f}s")


if __name__ == "__main__":
    main()
