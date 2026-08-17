#!/usr/bin/env python3
"""Block-count-pattern convexity structure of the VERIFIED es_construct.

For each block-count pattern p arising among (n-1)-subsets of es_construct(n):
  total(p) = prod_i C(|T_i|, p_i)   (all subsets with that block pattern)
  convex(p)= how many of those are in convex position (exact oracle)
  ratio(p) = convex(p)/total(p)

Reports the FULL patterns (ratio==1: every realizing subset is convex) and the
characterization of that set. Exact integer/Fraction arithmetic via es_geom.
"""
from fractions import Fraction
from math import comb as math_comb
from itertools import combinations
from collections import Counter

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    for n in (5, 6, 7):
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        sizes = [len(b) for b in blocks]
        nb = len(blocks)
        r = n - 1
        # point index -> block index
        block_of = {}
        idx = 0
        for bi, blk in enumerate(blocks):
            for _ in blk:
                block_of[idx] = bi
                idx += 1
        convex = Counter()   # pattern -> convex count
        for combo in combinations(range(N), r):
            sub = [pts[i] for i in combo]
            counts = [0] * nb
            for i in combo:
                counts[block_of[i]] += 1
            pat = tuple(counts)
            if in_convex_position(sub):
                convex[pat] += 1
        # total per pattern = prod C(size_i, p_i)
        allpats = sorted(convex.keys())
        totals = {}
        for pat in allpats:
            t = 1
            for i in range(nb):
                t *= math_comb(sizes[i], pat[i])
            totals[pat] = t
        print(f"=== n={n}  N={N}  block sizes={sizes} ===")
        full = []
        for pat in allpats:
            t = totals[pat]; c = convex[pat]
            ratio = Fraction(c, t)
            tag = "FULL " if ratio == 1 else ("half" if ratio == Fraction(1,2) else "frac")
            if ratio == 1:
                full.append(pat)
            print(f"   {tag} pat={pat} convex={c} total={t} ratio={float(ratio)}")
        # characterize FULL set: support + value structure
        print(f"   FULL patterns ({len(full)}):")
        for pat in full:
            support = [i for i in range(nb) if pat[i] > 0]
            print(f"      {pat}  support={support}  values={[pat[i] for i in support]}")
        print()
        # also test: is FULL exactly those patterns whose support is a contiguous
        # band?? print non-FULL supports for comparison
        nonfull = [p for p in allpats if convex[p] != totals[p]]
        print(f"   NON-FULL patterns ({len(nonfull)}): supports=")
        for p in nonfull:
            print(f"      {p}  support={[i for i in range(nb) if p[i]>0]}")
        print("="*70)


if __name__ == "__main__":
    main()
