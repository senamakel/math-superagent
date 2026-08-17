#!/usr/bin/env python3
"""Heavy test of the one unproven non-six pattern at n=8: (0,0,3,1,1,2,0).

Total realizations = C(15,3)*C(20,1)*C(15,1)*C(6,2) = 455*20*15*15 = 2047500.
Sample R random realizations; if any is non-convex the pattern is not FULL.
Exact convexity via lib.es_geom.
"""
import random
from math import comb as C
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    pat = (0, 0, 3, 1, 1, 2, 0)
    assert sum(pat) == 7
    total = C(sizes[2], 3) * sizes[3] * sizes[4] * C(sizes[5], 2)
    print(f"total realizations={total}")
    off = 0
    pos = []
    for s in sizes:
        pos.append(list(range(off, off + s))); off += s
    rng = random.Random(999)
    R = 200000
    bad = 0
    for _ in range(R):
        sel = []
        for i in range(len(sizes)):
            sel.extend(rng.sample(pos[i], pat[i]))
        sub = [pts[j] for j in sel]
        if not in_convex_position(sub):
            bad += 1
            print("NON-CONVEX WITNESS at sample:", sel)
            break
    print(f"sampled={R} non_convex={bad} -> pattern {'REFUTED as FULL' if bad else 'no non-convex in sample'}")


if __name__ == "__main__":
    main()
