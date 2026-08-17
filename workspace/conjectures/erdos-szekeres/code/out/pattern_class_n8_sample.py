#!/usr/bin/env python3
"""n=8 partial test: sample random 7-subsets of es_construct(8), collect
distinct realized block-index pattern classes.  If the C(n-1,2) conjecture
holds, n=8 should have exactly 21 = C(7,2) classes.  C(64,7) is too large to
enumerate, so this is a *sampled* (supportive, not exhaustive) check —
sampling cannot prove there are no further classes.
N=64, blocks 0..6 sizes [1,6,15,20,15,6,1], r=7."""
import random
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    block_of = {}
    off = 0
    for b, blk in enumerate(blocks):
        for p in blk:
            block_of[off] = b
            off += 1
    r = 7
    classes = {}
    rng = random.Random(2024)
    S = 400000
    convex_hits = 0
    for _ in range(S):
        comb = rng.sample(range(N), r)
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            convex_hits += 1
            cnt = [0] * len(blocks)
            for i in comb:
                cnt[block_of[i]] += 1
            classes[tuple(cnt)] = classes.get(tuple(cnt), 0) + 1
    print(f"sampled {S} random 7-subsets; convex {convex_hits}")
    print(f"distinct realized pattern classes found = {len(classes)} (conjecture: 21 = C(7,2))")
    for pat in sorted(classes):
        print("   ", pat, classes[pat])


if __name__ == "__main__":
    main()
