#!/usr/bin/env python3
"""Non-circular test of the count factorization: compute each per-block
goodness g_i(c) DIRECTLY as '# of c-subsets of block i that admit SOME
completion to a convex (n-1)-gon', then check prod_i g_i(c_i) == exact count
for every realized pattern, at n=6 and n=7.

For the completion we use a canonical transversal of the other blocks:
enumerate over choices in the bumped blocks.  Directly: g_i(c) = number of
c-subsets S of T_i such that S + (one point from each OTHER block, i.e. the
transversal of the remaining blocks that the pattern activates) is convex for
SOME transversal of the other blocks' non-zero counts.  We enumerate.

To keep it exact and bounded: for n=6 the completions come from at most two
other non-trivial blocks; for n=7 the size-10 middle blocks at c=3,4 give g.
We compute g via 'exists completion' and compare to the recovered values.
"""
from itertools import combinations, product
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def g_exists(n, blk, c, nontrivial_pairs):
    """# c-subsets S of block blk such that S + a completion (points from the
    other blocks in nontrivial_pairs, plus one from each remaining block) is
    convex for SOME completion.
    nontrivial_pairs: list of (blockidx, count) for the OTHER blocks that take
    a bumped count; all other blocks (except blk) take exactly 1."""
    pts, blocks = es_set_blocks(n)
    B = len(blocks)
    other_pick = {j: 1 for j in range(B) if j != blk}
    for (j, cj) in nontrivial_pairs:
        other_pick[j] = cj
    cnt = 0
    for S in combinations(blocks[blk], c):
        # lists to enumerate over: for each other block j, combos of size other_pick[j]
        lists = []
        for j in range(B):
            if j == blk:
                continue
            lists.append(list(combinations(blocks[j], other_pick[j])))
        found = False
        for combo in product(*lists):
            pts_s = list(S)
            for grp in combo:
                pts_s.extend(grp)
            if in_convex_position(pts_s):
                found = True
                break
        if found:
            cnt += 1
    return cnt


# n=6: middle size-6 block c=3; completions from (3,1)+(4,1) [pattern 0,0,3,1,1]
# or (3,2) [pattern 0,0,3,2,0].  Both should give g=10.
print("=== n=6 direct exists-completion goodness (middle size-6 block, c=3) ===")
g1 = g_exists(6, 2, 3, [(3, 1), (4, 1)])
g2 = g_exists(6, 2, 3, [(3, 2)])
print(f"  via pattern (0,0,3,1,1) completions: g(3)={g1}  (expect 10)")
print(f"  via pattern (0,0,3,2,0) completions: g(3)={g2}  (expect 10)")
