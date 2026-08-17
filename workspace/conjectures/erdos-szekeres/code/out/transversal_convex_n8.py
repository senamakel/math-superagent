#!/usr/bin/env python3
"""Out-of-sample test of the transversal-convexity conjecture at n=8.

Claim under test (established at n=4..7 by exact oracle): every full
transversal of the es_construct ES construction -- choosing exactly one
point from each block T_0..T_{n-2} -- lies in convex position.

At n=8 the full-subset enumeration (C(128,7) ~ 1e12) is infeasible, but the
number of full transversals is prod C(6,k) = 162000, each a 7-point convexity
test.  If any transversal is NOT convex, the conjecture fails here.

Exact arithmetic throughout (lib.es_geom.in_convex_position, exact hull).
"""
from itertools import product
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position
from math import comb, prod


def build_transversal_points(blocks, choice):
    """choice[k] = index of point taken from block k."""
    return [blocks[k][choice[k]] for k in range(len(blocks))]


def test(n):
    pts, blocks = es_set_blocks(n)
    nblocks = len(blocks)          # n-1
    sizes = [len(b) for b in blocks]
    total = prod(sizes)
    print(f"n={n}: N={len(pts)} blocks={nblocks} block sizes={sizes} "
          f"total transversals={total}")
    bad = 0
    first_bad = None
    checked = 0
    for choice in product(*[range(s) for s in sizes]):
        sub = build_transversal_points(blocks, choice)
        if not in_convex_position(sub):
            bad += 1
            if first_bad is None:
                first_bad = choice
        checked += 1
    print(f"  checked={checked} non-convex transversals={bad}")
    if first_bad is not None:
        print(f"  FIRST non-convex transversal (choice per block): {first_bad}")
    else:
        print("  ALL transversals convex: PASS")
    return bad


for n in (9,):
    bad = test(n)
    print(f"RESULT n={n}: all-transversals-convex =", bad == 0)
