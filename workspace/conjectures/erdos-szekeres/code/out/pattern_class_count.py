#!/usr/bin/env python3
"""Count distinct realized block-index pattern classes among (n-1)-convex
subsets of es_construct(n), for n=4..7.  Exact via lib.es_geom.
A pattern class = tuple of counts per block (the block-count pattern).
n=7 enumerates all C(32,6)=906192 (about 2 minutes)."""
from itertools import combinations
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def pattern_classes(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    nblk = len(blocks)
    block_of = {}
    off = 0
    for b, blk in enumerate(blocks):
        for p in blk:
            block_of[off] = b
            off += 1
    classes = set()
    r = n - 1
    for comb in combinations(range(N), r):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            cnt = [0] * nblk
            for i in comb:
                cnt[block_of[i]] += 1
            classes.add(tuple(cnt))
    return len(classes), classes


seq = []
for n in (4, 5, 6, 7):
    k, cls = pattern_classes(n)
    seq.append(k)
    print(f"n={n}: distinct realized pattern classes = {k}")
    if n <= 6:
        print("   ", sorted(cls))
print("SEQ distinct pattern classes n=4..7:", seq)
