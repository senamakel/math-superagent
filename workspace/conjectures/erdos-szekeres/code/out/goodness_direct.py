#!/usr/bin/env python3
"""Direct confirmation of the goodness value: is g_i(c) the number of c-subsets
of block T_i that are 'convex-compatible' with a transversal representative of
the other blocks?  And is this independent of the representative choice?

We compute for n=6 (size-6 middle block, c=3 -> expect 10 of C(6,3)=20) and
n=7 (size-10 block, c=3 -> 46; c=4 -> 41).  Convex-compatible = the c-subset
plus one point from each other block (a transversal of the rest) is in convex
position.  We vary the representative to test independence.
"""
from itertools import combinations
from math import comb
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def good_direct(nbi, ci, block, other_blocks, reps=None):
    """count c_i-subsets S of `block` such that S + reps-of-others is convex."""
    others_pts = []
    for b in other_blocks:
        if reps is not None and b is not block:
            others_pts.append(b[reps[id(b)]]) if False else None
    # simpler: caller passes the fixed transversal of other blocks
    cnt = 0
    total = comb(len(block), ci)
    for S in combinations(block, ci):
        if in_convex_position(list(S) + others_pts):
            cnt += 1
    return cnt, total


def run(n, blk_idx, ci):
    pts, blocks = es_set_blocks(n)
    B = len(blocks)
    block = blocks[blk_idx]
    others = [blocks[j] for j in range(B) if j != blk_idx]
    # try several transversals of the others (0th element each, 1st, etc.)
    results = {}
    for repinfo in [(0,) * (B - 1), (1,) * (B - 1), (2,) * (B - 1)]:
        others_pts = []
        for k, b in enumerate(others):
            idx = min(repinfo[k], len(b) - 1)
            others_pts.append(b[idx])
        cnt = sum(1 for S in combinations(block, ci)
                  if in_convex_position(list(S) + others_pts))
        results[repinfo] = cnt
    return results, comb(len(block), ci)


print("n=6, middle size-6 block:")
r, tot = run(6, 2, 3)
print("  c=3: direct goodness by transversal =", r, " C(6,3)=", tot)
print("n=7, middle size-10 block:")
r, tot = run(7, 2, 3)
print("  c=3: direct goodness by transversal =", r, " C(10,3)=", tot)
r, tot = run(7, 2, 4)
print("  c=4: direct goodness by transversal =", r, " C(10,4)=", tot)
r2, _ = run(7, 3, 3)
print("  block3 c=3 (mirror):", r2)
r2, _ = run(7, 3, 4)
print("  block3 c=4 (mirror):", r2)
