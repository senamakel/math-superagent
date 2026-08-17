#!/usr/bin/env python3
"""Decisive (a) vs (b) test for transversal-convexity.

es_construct places identical tiny clusters (blocks) on a strictly convex
downward arc.  Transversal-convexity (one point per block => convex) could be:
  (a) a structural consequence of the arc placement (scale separation), or
  (b) an intrinsic property of the block decomposition alone.

Experiment: keep the EXACT SAME blocks and their internal coordinates, but
replace the convex-arc centers by SCRAMBLED / NON-CONVEX placements.  Check at
n=6 (16 pts, blocks sizes [1,4,6,4,1]):
  (i)  are all 96 full transversals still convex?
  (ii) is the resulting set still n-avoiding (no convex 6-gon)?
If transversal-convexity breaks when the arc is broken, the property is an
artifact of the arc (design), confirming (a) and showing it does NOT
characterise n-avoiding sets in general.  Exact arithmetic throughout.
"""
from itertools import product
from fractions import Fraction
from random import Random
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position, has_convex_k_subset, in_general_position


def scramble_centers(n, rng, mode):
    """Rebuild es_set blocks with centers replaced by `mode` placement.
    Blocks identical; only center arrangement changes."""
    from lib.es_construct import _convex_arc_centers, es_block
    scale = Fraction(1, 10 ** 6)
    m = n - 1
    blocks_orig = [es_block(n, i) for i in range(m)]  # same blocks
    # centers: perturb or scramble
    if mode == "convex":
        centers = _convex_arc_centers(n)
    elif mode == "scramble_y":
        # keep x = i*1000, shuffle y values among the arc's y's => non-convex
        arc = _convex_arc_centers(n)
        ys = [c[1] for c in arc]
        ys2 = ys[:]
        rng.shuffle(ys2)
        centers = [(Fraction(i * 1000), ys2[i]) for i in range(m)]
    elif mode == "random":
        centers = [(Fraction(i * 1000), Fraction(rng.randrange(-20000, 20000)))
                   for i in range(m)]
    pts = []
    blocks = []
    for i in range(m):
        cx, cy = centers[i]
        blk = [(cx + scale * p[0], cy + scale * p[1]) for p in blocks_orig[i]]
        pts.extend(blk)
        blocks.append(blk)
    return pts, blocks


def check(n, rng, mode):
    pts, blocks = scramble_centers(n, rng, mode)
    N = len(pts)
    gp = in_general_position(pts)
    # (i) all transversals convex?
    sizes = [len(b) for b in blocks]
    trans_total = 1
    for s in sizes:
        trans_total *= s
    bad = 0
    for choice in product(*[range(s) for s in sizes]):
        sub = [blocks[k][choice[k]] for k in range(len(blocks))]
        if not in_convex_position(sub):
            bad += 1
    # (ii) n-avoiding? largest convex subset <= n-1
    hasn, _ = has_convex_k_subset(pts, n)
    # largest convex for reference
    return dict(mode=mode, N=N, gp=gp, transversals=trans_total,
                nonconvex_trans=bad, all_trans_convex=(bad == 0),
                has_convex_n=hasn)


def main():
    rng = Random(12345)
    for mode in ("convex", "scramble_y", "random"):
        r = check(6, rng, mode)
        print(f"n=6 mode={mode:10s} gp={r['gp']} "
              f"transversals={r['transversals']} nonconvex={r['nonconvex_trans']} "
              f"ALL_CONVEX={r['all_trans_convex']} has_convex_6gon={r['has_convex_n']}")


if __name__ == "__main__":
    main()
