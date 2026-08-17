#!/usr/bin/env python3
"""DEFINITIVE check of the block-pattern count factorization.

Claim (NEW, exact n=4..7): #(n-1)-convex subsets of es_construct(n) realizing
block-count pattern c == prod_i g_i(c_i), where g_i(c) is a per-block intrinsic
count depending only on (block size |T_i|, count c), identical for the two
reversal-symmetric middle blocks, with g(0)=1 and g(1)=|T_i|.

Recovery: for each pattern the bumps (blocks with c>=2) are exactly positions L
and R of the unordered block pair (the bijection).  Single-bump patterns give
g directly; double-bump patterns verify consistency.  We then check that the
two symmetric blocks agree and that prod g == exact count for EVERY pattern.
"""
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def exact_counts(n):
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    owned = []
    for bi, b in enumerate(blocks):
        owned.extend([bi] * len(b))
    B = len(blocks)
    cnt = Counter()
    for comb in combinations(range(len(pts)), n - 1):
        if in_convex_position([pts[i] for i in comb]):
            c = [0] * B
            for i in comb:
                c[owned[i]] += 1
            cnt[tuple(c)] += 1
    return cnt, sizes


def pair_of_pattern(pat):
    """Invert the bijection: find the {L,R} pair (positions of the two bumps
    in reverse-symmetric sense).  Actually L=first index with non-small value,
    R=last.  We just return positions where value is not (0 or 1)."""
    B = len(pat)
    Lv = [i for i in range(B) if pat[i] not in (0, 1)]
    return Lv


for n in (4, 5, 6, 7):
    cnt, sizes = exact_counts(n)
    B = len(sizes)
    # recover g
    g = {i: {0: 1, 1: sizes[i]} for i in range(B)}
    # iterate: patterns whose bumps are all solved give new g values
    for _ in range(6):
        for pat in sorted(cnt, key=sum):
            bumps = pair_of_pattern(pat)
            if not bumps:
                continue
            # single bump: direct
            unsolved = [i for i in bumps if pat[i] not in g[i]]
            if len(unsolved) == 0:
                continue  # already in g
            if len(bumps) == 1:
                i = bumps[0]
                if pat[i] in g[i]:
                    continue
                others = 1
                for j in range(B):
                    if j == i:
                        continue
                    if pat[j] not in g[j]:
                        break
                    others *= g[j][pat[j]]
                else:
                    g[i][pat[i]] = cnt[pat] // others
                    if cnt[pat] % others != 0:
                        print(f"  !! nondiv {pat} {cnt[pat]} / {others}")
    # verify every pattern
    ok = True
    total_model = 0
    for pat in sorted(cnt):
        model = 1
        for i in range(B):
            if pat[i] not in g[i]:
                ok = False
                model = None
                break
            model *= g[i][pat[i]]
        if model is not None:
            total_model += model
        if model != cnt[pat]:
            ok = False
            print(f"  MISMATCH {pat}: true={cnt[pat]} model={model}")
    sym_ok = True
    # check two middle blocks agree on shared c
    if B >= 4:
        mid = B // 2
        # blocks mid-1 and mid (or for even B the two central)
        a, b2 = mid - 1, B - mid
        for c in set(g[a]) & set(g[b2]):
            if g[a][c] != g[b2][c]:
                sym_ok = False
    print(f"\n===== n={n} sizes={sizes} =====")
    print(f"  recovered per-block g (by block size):")
    shown = {}
    for i in range(B):
        key = sizes[i]
        shown.setdefault(key, (i, g[i]))
    for siz, (i, gi) in sorted(shown.items()):
        print(f"    size {siz} (block {i}): {dict(sorted(gi.items()))}")
    print(f"  all patterns factorize exactly: {ok}   total_model={total_model} "
          f"total_exact={sum(cnt.values())}   middle-block symmetry: {sym_ok}")
