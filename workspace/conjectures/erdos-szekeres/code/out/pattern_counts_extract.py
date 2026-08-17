#!/usr/bin/env python3
"""Extract per-pattern COUNTS of (n-1)-convex subsets of es_construct(n) and
test candidate closed forms: does count == prod_i C(|T_i|, c_i) with a simple
correction?  Exact via lib.es_geom.  n=4..7 exhaustive (n=7 ~2min)."""
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def counts_per_pattern(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    blk_of = {}
    off = 0
    sizes = []
    for b, blk in enumerate(blocks):
        sizes.append(len(blk))
        for p in blk:
            blk_of[off] = b
            off += 1
    B = len(blocks)
    cnt = Counter()
    r = n - 1
    for comb in combinations(range(N), r):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            c = [0] * B
            for i in comb:
                c[blk_of[i]] += 1
            cnt[tuple(c)] += 1
    return cnt, sizes


def pattern_pair(c, B):
    """Invert the bijection: find {L,R} giving this profile, if any."""
    # profile: c_L=L+1, c_R=B-R, c_i=1 between, 0 outside
    for L in range(B):
        for R in range(L + 1, B):
            ok = True
            for i in range(B):
                exp = 0
                if i < L or i > R:
                    exp = 0
                elif i == L:
                    exp = L + 1
                elif i == R:
                    exp = B - R
                else:
                    exp = 1
                if c[i] != exp:
                    ok = False
                    break
            if ok:
                return (L, R)
    return None


for n in (4, 5, 6, 7):
    cnt, sizes = counts_per_pattern(n)
    B = len(sizes)  # n-1
    total = sum(cnt.values())
    print(f"\n===== n={n}  B={B}  blocks sizes={sizes}  total convex (n-1)-subsets={total} =====")
    print(f"  C(B,2)={comb(B,2)}  distinct patterns={len(cnt)}")
    for pat in sorted(cnt.keys()):
        c0 = list(pat)
        pr = 1
        for i in range(B):
            pr *= comb(sizes[i], c0[i])
        pair = pattern_pair(c0, B)
        ratio = (cnt[tuple(c0)] / pr) if pr else None
        print(f"  pattern {c0} pair={pair} count={cnt[tuple(c0)]:8d} prod={pr:8d} "
              f"ratio={ratio if ratio is None else round(ratio,4)}")
