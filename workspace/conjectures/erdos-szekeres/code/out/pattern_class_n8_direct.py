#!/usr/bin/env python3
"""n=8: test EVERY candidate block-count pattern (sum=7, c_i <= |T_i|) for
realizability by a convex 7-subset of es_construct(8).  Enumerate candidate
patterns directly (few hundred), for each sample K random realizations and
ask whether any is convex.  A pattern found convex somewhere is REALIZED;
this discovers the realized set far more efficiently than uniform subset
sampling.  Distinct realized classes should be 21 = C(7,2) if the conjecture
holds.  NOTE: for patterns that are non-FULL, sampling cannot *prove* each
realization non-convex (a rare convex realization could be missed); the
count is therefore a lower bound on realized classes.  We also bound the
headline count by the FULL patterns (all-realization convex, provable by
enumeration where cheap)."""
import random
from itertools import product
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    sizes = [len(b) for b in blocks]
    nblk = len(blocks)
    r = 7
    block_of = {}
    off = 0
    for b, blk in enumerate(blocks):
        for p in blk:
            block_of[off] = b
            off += 1
    # per-block index ranges
    ranges = []
    off = 0
    for b in range(nblk):
        ranges.append(list(range(off, off + sizes[b])))
        off += sizes[b]
    # enumerate candidate patterns: tuples c summing to 7, 0<=c_i<=sizes[i]
    cand = []
    def rec(i, rem, cur):
        if i == nblk - 1:
            if rem <= sizes[i]:
                cand.append(tuple(cur + [rem]))
            return
        for v in range(min(sizes[i], rem) + 1):
            rec(i + 1, rem - v, cur + [v])
    rec(0, r, [])
    rng = random.Random(7)
    K = 150
    realized = set()
    for pat in cand:
        found = False
        for _ in range(K):
            sel = []
            for i in range(nblk):
                sel.extend(rng.sample(ranges[i], pat[i]))
            sub = [pts[j] for j in sel]
            if in_convex_position(sub):
                found = True
                break
        if found:
            realized.add(pat)
    print(f"candidate patterns with sum 7: {len(cand)}")
    print(f"distinct realized pattern classes found (K={K}/pattern): {len(realized)} "
          f"(conjecture: 21 = C(7,2))")
    for pat in sorted(realized):
        print("   ", pat)
    print("not realized so far:", len(cand) - len(realized))


if __name__ == "__main__":
    main()
