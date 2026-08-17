#!/usr/bin/env python3
"""DECIDING TEST for the per-block goodness factorization claim (v2).

Question (steer): the es_construct block-pattern count factorization
  #(n-1)-convex subsets with block pattern c == prod_i g_i(c_i)
is a property of the es_construct ARC placement.  Does it survive on sets
that are NOT this construction?

We keep the SAME blocks (exact-rational cups/caps blocks, sizes C(n-2,i),
extracted via es_construct.es_set_blocks / es_block) and change only the
PLACEMENT of the block centres, at n=6 (16 points, C(16,5)=4368 subsets —
cheap exact enumeration).  For each placement:
  (1) enumerate all (n-1)-subsets, record block-count patterns + convex counts;
  (2) recover per-block goodness g_i(c) from single-bump patterns and check
      prod_i g_i(c_i) == exact count for EVERY pattern (factorization test);
  (3) report whether the two symmetric middle blocks still share g.

Placements (all exact rational/integer, all in general position):
  arc       : es_construct's own convex-arc placement  (control, should pass)
  scrambled : y-centres off the arc (convexity corridor broken)
  staircase : x=+i, y=-i (all cross-slopes negative steep) -- ES-style
"""
from itertools import combinations
from math import comb
from fractions import Fraction
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position, in_general_position


def place_blocks(blocks, centres, scale):
    out = []
    for (cx, cy), T in zip(centres, blocks):
        for (px, py) in T:
            out.append((cx + scale * px, cy + scale * py))
    return out


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


def check_factorization(cnt, sizes, label):
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
    unresolved = 0
    prod_sum = 0
    mismatch = []
    for pat in sorted(cnt):
        model = 1
        good = True
        for i in range(B):
            if pat[i] not in g[i]:
                good = False
                break
            model *= g[i][pat[i]]
        if good:
            prod_sum += model
            if model != cnt[pat]:
                ok = False
                mismatch.append((pat, cnt[pat], model))
        else:
            unresolved += 1
    sym = None
    if B % 2 == 0:
        a, b = B // 2 - 1, B // 2
        sym = all(g[a].get(c) == g[b].get(c)
                  for c in set(g[a]) | set(g[b]))
    print(f"  [{label}] total_convex={sum(cnt.values())} "
          f"distinct_patterns={len(cnt)} factorization={ok} "
          f"unresolved={unresolved} mid_sym={sym}")
    if mismatch:
        for (p, cc, mm) in mismatch[:5]:
            print(f"      MISMATCH pat={p} exact={cc} model={mm}")
    for i in range(B):
        print(f"      g_{i}: {dict(sorted(g[i].items()))}")
    return ok


def main():
    n = 6
    # REUSE the verified es_construct blocks (exact-rational), fetch once
    pts_orig, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    print(f"n={n} block sizes={sizes} sum={sum(sizes)} (expect 16)")

    # ---- 1. ARC: es_construct's own placement (control, should factorize)
    print("\n=== ARC (control, es_construct's own placement) ===")
    cnt, sz = pattern_counts(pts_orig, blocks)
    check_factorization(cnt, sz, "arc")

    # ---- 2. SCRAMBLED: y-centres off the convex arc
    scale2 = Fraction(1, 10 ** 5)
    y_vals = [0, 30, 1, 200, 5]
    centres_scram = [(Fraction(i) * 1000, Fraction(y_vals[i]))
                     for i in range(n - 1)]
    pts2 = place_blocks(blocks, centres_scram, scale2)
    print("\n=== SCRAMBLED y (off the arc) ===")
    print("  gp:", in_general_position(pts2))
    cnt2, sz2 = pattern_counts(pts2, blocks)
    check_factorization(cnt2, sz2, "scrambled")

    # ---- 3. STAIRCASE: x=+i, y=-(some)*i  (cross-slopes negative steep)
    scale3 = Fraction(1, 10 ** 3)
    centres_stair = [(Fraction(i) * 20, -Fraction(i) * 40)
                     for i in range(n - 1)]
    pts3 = place_blocks(blocks, centres_stair, scale3)
    print("\n=== STAIRCASE (x=+i, y=-i) ===")
    print("  gp:", in_general_position(pts3))
    cnt3, sz3 = pattern_counts(pts3, blocks)
    check_factorization(cnt3, sz3, "staircase")


if __name__ == "__main__":
    main()
