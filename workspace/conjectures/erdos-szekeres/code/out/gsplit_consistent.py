#!/usr/bin/env python3
"""Test G-split-consistent on the CORRECT es_construct construction.

Claim: the ES construction X_n splits into two halves each of size 2^{n-3},
each (n-1)-avoiding, witnessing the recursion X_n = X_{n-1} u X_{n-1}.

The class-ES construction uses blocks T_0..T_{n-2} with |T_i| = C(n-2,i).
Classical split: even-indexed blocks (i even) form one (n-1)-avoiding set,
odd-indexed the other, each of size sum_{i even} C(n-2,i) = 2^{n-3}.
A radial placement puts consecutive-index blocks at increasing polar angle,
so a line through the centre separates lower-index from higher-index blocks;
we verify the actual even/odd block groups are each (n-1)-avoiding.
"""
from math import comb
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position, has_convex_k_subset
from itertools import combinations


def largest_convex_from_has(pts, cmax):
    for k in range(cmax, 2, -1):
        if has_convex_k_subset(pts, k)[0]:
            return k
    return 0


for n in (5, 6, 7):
    _all, blocks = es_set_blocks(n)
    nblocks = len(blocks)
    even = []
    odd = []
    for i, blk in enumerate(blocks):
        (even if i % 2 == 0 else odd).extend(blk)
    print(f"n={n}: blocks={[len(b) for b in blocks]}")
    print(f"   even-blocks: {len(even)} pts (want 2^{n-3}={2**(n-3)}) "
          f"no-convex-{n-1}? {not has_convex_k_subset(even, n-1)[0]}")
    print(f"   odd -blocks: {len(odd)} pts (want 2^{n-3}={2**(n-3)}) "
          f"no-convex-{n-1}? {not has_convex_k_subset(odd, n-1)[0]}")
    # binomial row check
    row = [comb(n-2, i) for i in range(n-1)]
    print(f"   binomial row C(n-2,·)= {row}, even-sum={sum(row[::2])} "
          f"odd-sum={sum(row[1::2])}")
