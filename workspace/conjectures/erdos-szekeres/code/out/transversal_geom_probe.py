#!/usr/bin/env python3
"""Probe the geometric basis of transversal-convexity.

Conjecture: any full transversal of es_construct X_n is convex because each
block T_i is a TINY cluster near center c_i on a strictly (downward-)convex
arc, so one point per cluster keeps the n-1 points strictly convex.

We report the block cluster scale vs the inter-center convexity scale, to see
whether a general "sufficiently tiny clusters on a strictly convex curve keep
every transversal convex" lemma could hold.  All exact (Fraction), reporting
width/height of each block bbox relative to the chord gaps.
"""
from fractions import Fraction
from lib.es_construct import es_set_blocks, _convex_arc_centers


def bbox_dims(blk):
    xs = [p[0] for p in blk]
    ys = [p[1] for p in blk]
    return max(xs) - min(xs), max(ys) - min(ys)


for n in (5, 6, 7, 8, 9):
    pts, blocks = es_set_blocks(n)
    centers = _convex_arc_centers(n)
    print(f"n={n}: centers={[(float(c[0]), float(c[1])) for c in centers[:3]]} ...")
    for i, blk in enumerate(blocks):
        w, h = bbox_dims(blk)
        # chord gap from center i to center i+1 (Euclidean), and convexity: 
        # distance of center i+1 from the chord through neighbors.
        cx, cy = centers[i]
        print(f"   block {i}: size={len(blk)} bbox_w={float(w):.3g} "
              f"bbox_h={float(h):.3g}")
    print()
