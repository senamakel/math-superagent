#!/usr/bin/env python3
"""Extend the middle-block goodness sequence to n=8, exact, TARGETED.

Goodness g_i(c) = # c-subsets S of block T_i completable to a convex (n-1)-gon
in a canonical single-bump pattern with 1 point from each of the other blocks.
Factorization (pattern-independence) verified at n=6,7; we use the cleanest
single-bump completion and cross-check nothing beyond existence.

Recorded so far (exact captures):
    n=6 block2 size6: g(3)=10
    n=7 block2/3 size10: g(3)=46, g(4)=41      -> middle-goodness c=3 seq: [10,46]
n=8 (B=7 blocks, sizes [1,6,15,20,15,6,1]):
    g_2(3): pattern {2,6} -> (0,0,3,1,1,1,1): 1 from blocks 3,4,5,6
    g_3(4): pattern {3,6} -> (0,0,0,4,1,1,1): 1 from blocks 4,5,6
Exact Fraction convexity via lib.es_geom.
"""
from itertools import combinations, product
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def g_single_bump(n, mid_idx, c, other_idxs):
    """# c-subsets of block mid_idx with a convex completion taking 1 from each
    of other_idxs (the 'between/beyond' blocks of the {L,R} single-bump pattern)."""
    pts, blocks = es_set_blocks(n)
    cnt = 0
    lists = [list(blocks[j]) for j in other_idxs]
    for S in combinations(blocks[mid_idx], c):
        found = False
        for combo in product(*lists):
            ps = list(S) + list(combo)
            if in_convex_position(ps):
                found = True
                break
        if found:
            cnt += 1
    return cnt


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    print("n=8 block sizes:", sizes, flush=True)
    g23 = g_single_bump(n, 2, 3, [3, 4, 5, 6])   # T_2 size 15, c=3
    print("g_2(3) [T2 size15] =", g23, flush=True)
    g34 = g_single_bump(n, 3, 4, [4, 5, 6])      # T_3 size 20, c=4
    print("g_3(4) [T3 size20] =", g34, flush=True)
    # middle-goodness (c=3) by middle-block size:
    print("middle-goodness c=3 by block size m: n=6(m6)=10, n=7(m10)=46, "
          f"n=8(m15, T2)={g23}, n=8(m20,T3): (c=4) {g34}", flush=True)


if __name__ == "__main__":
    main()
