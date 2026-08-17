#!/usr/bin/env python3
"""Verify a NEW exact regularity connecting the two recorded es_construct
findings: the six FULL (all-convex) block patterns are exactly the realized
patterns whose bijection-pair {L,R} has BOTH endpoints in the corner block set
CO = {0, 1, n-3, n-2}.

Exploit: pattern_factor (already computed) gives FULL set; the bijection pairs
every realized pattern to {L,R}. We recompute FULL patterns exhaustively here
(exact oracle) and check the corner-pair characterization for n=5,6,7.
"""
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def pair_of_pattern(c):
    """Invert realized-pattern <-> {L,R} bijection (c_L=L+1, c_R=B-R, 1 between)."""
    B = len(c)
    for L in range(B):
        for R in range(L + 1, B):
            ok = True
            for i in range(B):
                exp = 0
                if i < L or i > R:
                    exp = 0
                elif i == L:
                    exp = L + 1
                elif i == R:
                    exp = B - R
                else:
                    exp = 1
                if c[i] != exp:
                    ok = False
                    break
            if ok:
                return (L, R)
    return None


def full_patterns(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    nb = len(blocks)
    blk_of = {}
    off = 0
    sizes = []
    for b, blk in enumerate(blocks):
        sizes.append(len(blk))
        for _ in blk:
            blk_of[off] = b
            off += 1
    total = Counter()
    convex = Counter()
    for cmb in combinations(range(N), n - 1):
        sub = [pts[i] for i in cmb]
        c = [0] * nb
        for i in cmb:
            c[blk_of[i]] += 1
        total[tuple(c)] += 1
        if in_convex_position(sub):
            convex[tuple(c)] += 1
    full = {p for p in total if convex[p] == total[p]}
    realized = set(convex)
    return full, realized, nb, sizes


for n in (5, 6, 7):
    full, realized, nb, sizes = full_patterns(n)
    CO = {0, 1, n - 3, n - 2}
    ok = True
    full_pairs = []
    for p in sorted(full):
        pr = pair_of_pattern(p)
        full_pairs.append(pr)
        if not (pr[0] in CO and pr[1] in CO):
            ok = False
            print(f"  n={n} FULL pattern {p} pair={pr} NOT both in CO={CO}")
    # any corner-pair realized pattern that is NOT full?
    corner_realized = []
    for p in realized:
        pr = pair_of_pattern(p)
        if pr and pr[0] in CO and pr[1] in CO:
            corner_realized.append(p)
    notfull_corner = [p for p in corner_realized if p not in full]
    print(f"n={n}: CO={set(sorted(CO))}  #FULL={len(full)} "
          f"full_pairs={sorted(full_pairs)} "
          f"realized={len(realized)} corner_realized={len(corner_realized)} "
          f"-> corner-not-full={notfull_corner}  "
          f"FULL==corner-pairs: {ok and not notfull_corner}")
print("EXIT: 0")
