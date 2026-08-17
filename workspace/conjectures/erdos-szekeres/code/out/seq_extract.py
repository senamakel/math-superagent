#!/usr/bin/env python3
"""Extract integer sequences from the verified es_construct ES construction.

For each n in 4..7, on X_n = es_set(n) (2^{n-2} points, no convex n-gon):
  (a) number of distinct (n-1)-subsets that lie in convex position
      (same as maxconvex_structure's 'convex' count, but including n=4);
  (b) among those, the number that are FULL TRANSVERSALS (one point from
      each of the n-1 blocks T_0..T_{n-2});
  (c) the gsplit valid-split count (rotating-line enumerator) for n=4..7.
All exact; convexity via lib.es_geom.in_convex_position (exact hull).
"""
from itertools import combinations
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position, orient, has_convex_k_subset


def build_block_of(blocks):
    block_of = []
    for i, blk in enumerate(blocks):
        for _ in blk:
            block_of.append(i)
    return block_of


def distinct_convex_and_transversal(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    nblocks = len(blocks)
    block_of = build_block_of(blocks)
    convex = 0
    trans = 0
    for comb in combinations(range(N), n - 1):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            convex += 1
            counts = [0] * nblocks
            for i in comb:
                counts[block_of[i]] += 1
            if tuple(counts) == (1,) * nblocks:
                trans += 1
    return convex, trans


def ordered_pair_sides(points):
    N = len(points)
    res = set()
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            strict = frozenset(x for x in range(N)
                               if orient(points[a], points[b], points[x]) > 0)
            for extra in (frozenset(), frozenset([a]), frozenset([b]),
                          frozenset([a, b])):
                side = strict | extra
                if 0 < len(side) < N:
                    res.add(side)
    return res


def gsplit_count(n):
    allp, _ = es_set_blocks(n)
    N = len(allp)
    op = ordered_pair_sides(allp)
    target = 2 ** (n - 3)
    valid = 0
    for side in op:
        if len(side) != target:
            continue
        comp = frozenset(range(N)) - side
        if len(comp) != target:
            continue
        L_av = not has_convex_k_subset([allp[i] for i in side], n - 1)[0]
        R_av = not has_convex_k_subset([allp[i] for i in comp], n - 1)[0]
        if L_av and R_av:
            valid += 1
    return valid


print("distinct (n-1)-convex subsets and full transv ersals:")
conv_seq, trans_seq = [], []
for n in (4, 5, 6, 7):
    c, t = distinct_convex_and_transversal(n)
    conv_seq.append(c)
    trans_seq.append(t)
    print(f"  n={n}: N={2**(n-2)} distinct (n-1)-convex-subset count={c}  full-transversal count={t}")
print("SEQ distinct (n-1)-convex n=4..7:", conv_seq)
print("SEQ full-transversal        n=4..7:", trans_seq)

print()
print("gsplit valid-split counts (rotating-line, exact):")
gs = [gsplit_count(n) for n in (4, 5, 6, 7)]
print("SEQ gsplit n=4..7:", gs)
