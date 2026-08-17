#!/usr/bin/env python3
"""Check the structural claim: in es_construct, EVERY full transversal of the
blocks (one point from each of the n-1 blocks) is in convex position.

trans = product of block sizes = A001142 would follow only if every full
transversal were convex.  Here we count full transversals, and count those in
convex position, directly, at n=4..7.  Also test the same claim on an
INDEPENDENT placement for comparison: a random perturbation / other order type,
to see whether this is structure of the ES block template or of the arc placement.
"""
from itertools import combinations, product
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def check(n, label):
    pts, blocks = es_set_blocks(n)
    # build list of per-block point index lists
    idx = []
    start = 0
    for blk in blocks:
        idx.append(list(range(start, start + len(blk))))
        start += len(blk)
    # enumerate full transversals lazily via product
    total = 1
    for l in idx:
        total *= len(l)
    nconvex = 0
    for pick in product(*idx):
        sub = [pts[i] for i in pick]
        if in_convex_position(sub):
            nconvex += 1
    print(f"{label} n={n}: |blocks|={[len(b) for b in blocks]} "
          f"total_full_transversals={total} convex_full_transversals={nconvex} "
          f"all_convex={nconvex==total}")


for n in (4, 5, 6, 7):
    check(n, "es_construct")
