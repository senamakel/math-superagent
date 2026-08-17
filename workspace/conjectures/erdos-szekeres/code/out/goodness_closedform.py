#!/usr/bin/env python3
"""Two checks on the per-block goodness factorization:

(A) Closed form for the TOTAL number of (n-1)-convex subsets:
    T_n = sum over block pairs {L,R} (0<=L<R<=B-1, B=n-1) of
          g_L(L+1) * g_R(B-R) * prod_{L<i<R} |T_i|
    where g(0)=1, g(1)=|T_i|, and non-trivial g values are taken as observed.
    Verify T_n matches the exact total at n=4..7.

(B) Geometric meaning test: is g_i(c) = the number of c-subsets S of block i
    for which there EXISTS a completion (choices of the other blocks' points
    per a supporting pattern) making S + completion convex?  Test at n=6
    (size-6 middle block, c=3, patterns (0,0,3,1,1) and (0,0,3,2,0)).
"""
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


# recovered per-block g from the exact count factorization (verified prior)
G = {
    4: {1: {0: 1, 1: 1}, 2: {0: 1, 1: 2, 2: 1}},
    5: {1: {0: 1, 1: 1}, 3: {0: 1, 1: 3, 2: 3, 3: 1}},
    6: {1: {0: 1, 1: 1}, 4: {0: 1, 1: 4, 2: 6, 4: 1}, 6: {0: 1, 1: 6, 3: 10}},
    7: {1: {0: 1, 1: 1}, 5: {0: 1, 1: 5, 2: 10, 5: 1},
        10:{0: 1, 1: 10, 3: 46, 4: 41}},
}

def closed_form_total(n):
    pts, blocks = es_set_blocks(n)
    B = len(blocks)
    sizes = [len(b) for b in blocks]
    gmap = {i: G[n].get(sizes[i], {0: 1, 1: sizes[i]}) for i in range(B)}
    # fill trivial g(1) and g(0) into any missing
    for i in range(B):
        g = gmap[i]
        g.setdefault(0, 1)
        g.setdefault(1, sizes[i])
    total = 0
    for L in range(B):
        for R in range(L + 1, B):
            term = gmap[L].get(L + 1, 1) * gmap[R].get(B - R, 1)
            for i in range(L + 1, R):
                term *= gmap[i].get(1, 1)
            total += term
    return total, sizes


def exact_total(n):
    pts, blocks = es_set_blocks(n)
    owned = []
    for bi, b in enumerate(blocks):
        owned.extend([bi] * len(b))
    t = 0
    for cmb in combinations(range(len(pts)), n - 1):
        if in_convex_position([pts[i] for i in cmb]):
            t += 1
    return t


print("(A) closed-form total vs exact total:")
for n in (4, 5, 6, 7):
    cf, sizes = closed_form_total(n)
    ex = exact_total(n)
    print(f"  n={n} sizes={sizes}: closed_form={cf} exact={ex} match={cf==ex}")

# (B) geometric meaning at n=6
print("\n(B) 'exists a completion' interpretation at n=6 (middle size-6 block):")
pts6, blocks6 = es_set_blocks(6)
sizes = [len(b) for b in blocks6]
print("  sizes:", sizes)
blk = 2
c = 3
# pattern (0,0,3,1,1): completion = pick 1 from block3 and 1 from block4
others_small = [(3, 1), (4, 1)]   # (blockidx, count)
# pattern (0,0,3,2,0): completion = pick 2 from block3
others_big = [(3, 2)]

def count_exists(blk, c, other_choices):
    # other_choices: list of (blockidx, count)
    ok = 0
    for S in combinations(blocks6[blk], c):
        # enumerate completions
        lists = []
        for (bi, cnt) in other_choices:
            lists.append(list(combinations(blocks6[bi], cnt)))
        found = False
        for combo in __import__('itertools').product(*lists):
            pts = list(S)
            for grp in combo:
                pts.extend(grp)
            if in_convex_position(pts):
                found = True
                break
        if found:
            ok += 1
    return ok

r_small = count_exists(blk, c, others_small)
print(f"  c=3 with pattern (0,0,3,1,1): 'exists-completion' count = {r_small} (g should be 10)")
r_big = count_exists(blk, c, others_big)
print(f"  c=3 with pattern (0,0,3,2,0): 'exists-completion' count = {r_big} (g should be 10)")
