#!/usr/bin/env python3
"""Confirm the goodness-factorization survival extends to n=7: staircase
placement vs arc placement, same blocks, exact enumeration of all C(32,6)
(n-1)-subsets. Verify (a) factorization holds on the staircase placement too,
(b) the recovered g values are IDENTICAL to the arc/recorded ones — in
particular the distinctive n=7 middle-block g_2=g_3={0:1,1:10,3:46,4:41} and
g_1=g_4={0:1,1:5,2:10,5:1}."""
from itertools import combinations
from fractions import Fraction
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position, in_general_position


def pattern_counts(pts, blocks):
    N = len(pts)
    nb = len(blocks)
    block_of = {}
    off = 0
    sizes = []
    for bi, blk in enumerate(blocks):
        sizes.append(len(blk))
        for _ in blk:
            block_of[off] = bi
            off += 1
    cnt = Counter()
    for comb in combinations(range(N), nb):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            c = [0] * nb
            for i in comb:
                c[block_of[i]] += 1
            cnt[tuple(c)] += 1
    return cnt, sizes


def recover_g_and_check(cnt, sizes):
    B = len(sizes)
    g = {i: {0: 1, 1: sizes[i]} for i in range(B)}
    changed = True
    while changed:
        changed = False
        for pat in sorted(cnt):
            bumps = [i for i in range(B) if pat[i] >= 2]
            if len(bumps) != 1:
                continue
            i = bumps[0]
            if pat[i] in g[i]:
                continue
            if all(pat[j] in g[j] for j in range(B) if j != i):
                others = 1
                for j in range(B):
                    if j != i:
                        others *= g[j][pat[j]]
                if others > 0 and cnt[pat] % others == 0:
                    g[i][pat[i]] = cnt[pat] // others
                    changed = True
    ok = True
    for pat in sorted(cnt):
        model = 1
        for i in range(B):
            if pat[i] not in g[i]:
                ok = False
                break
            model *= g[i][pat[i]]
        if model != cnt[pat]:
            ok = False
    return g, ok


def main():
    n = 7
    pts_arc, blocks = es_set_blocks(n)   # arc placement (reference)
    sizes = [len(b) for b in blocks]
    print(f"n={n} sizes={sizes} sum={sum(sizes)} (expect 32)")

    # staircase placement of the SAME blocks
    scale = Fraction(1, 10 ** 3)
    centres = [(Fraction(i) * 20, -Fraction(i) * 40) for i in range(n - 1)]
    stair = []
    for (cx, cy), T in zip(centres, blocks):
        for (px, py) in T:
            stair.append((cx + scale * px, cy + scale * py))
    print("  staircase gp:", in_general_position(stair))

    cnt_a, _ = pattern_counts(pts_arc, blocks)
    cnt_s, _ = pattern_counts(stair, blocks)
    ga, oka = recover_g_and_check(cnt_a, sizes)
    gs, oks = recover_g_and_check(cnt_s, sizes)
    print(f"  ARC      : total={sum(cnt_a.values())} patterns={len(cnt_a)} "
          f"factorization={oka}")
    print(f"  STAIRCASE: total={sum(cnt_s.values())} patterns={len(cnt_s)} "
          f"factorization={oks}")
    same = True
    for i in range(n - 1):
        if dict(sorted(ga[i].items())) != dict(sorted(gs[i].items())):
            same = False
    print(f"  g values identical arc vs staircase: {same}")
    print("  recorded g (arc):")
    for i in range(n - 1):
        print(f"    g_{i}: {dict(sorted(ga[i].items()))}")


if __name__ == "__main__":
    main()
