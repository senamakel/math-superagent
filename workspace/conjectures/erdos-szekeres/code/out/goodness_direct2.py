#!/usr/bin/env python3
"""Direct (non-circular) verification of the per-block goodness g_i(c):

g_i(c) := # of c-subsets S of block T_i such that there EXISTS a completion to
a convex (n-1)-gon respecting a SPECIFIC pattern p (with the other blocks'
counts per p).  The factorization claim is that this value is independent of
which pattern p involving (i,c) we use.  We:
  - compute g_p(i,c) directly for every pattern p containing block i with c_i=c
  - check it's the same for all such p (pattern independence),
  - check it equals the recovered g from the exact enumeration,
at n=6 and n=7.
"""
from itertools import combinations, product
from math import comb
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def pattern_completions(blocks, pattern, blk_ignore=None):
    """Return a list of 'choice-lists': for each block j, the combinations
    (subsets) of size pattern[j] to try as the completion (excluding the block
    we're testing, blk_ignore, which provides S)."""
    B = len(blocks)
    lists = []
    for j in range(B):
        if j == blk_ignore:
            continue
        lists.append(list(combinations(blocks[j], pattern[j])))
    return lists


def g_direct(n, i, c, pattern):
    """# c-subsets S of block i that complete to convex with the OTHER blocks
    per `pattern` (pattern[i] must == c)."""
    pts, blocks = es_set_blocks(n)
    lists = pattern_completions(blocks, pattern, blk_ignore=i)
    cnt = 0
    for S in combinations(blocks[i], c):
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


def realized_patterns(n):
    """Return the block-count patterns that are realized (from exact counts)."""
    from collections import Counter
    pts, blocks = es_set_blocks(n)
    owned = []
    for bi, b in enumerate(blocks):
        owned.extend([bi] * len(b))
    B = len(blocks)
    pats = set()
    for cmb in combinations(range(len(pts)), n - 1):
        if in_convex_position([pts[i] for i in cmb]):
            c = [0] * B
            for x in cmb:
                c[owned[x]] += 1
            pats.add(tuple(c))
    return pats, [len(b) for b in blocks]


for n, g_expected in ((6, {3: 10}),
                      (7, {3: 46, 4: 41})):
    pats, sizes = realized_patterns(n)
    B = len(sizes)
    # middle block i with non-trivial g: n=6 -> block2 (size6), n=7 -> block2 (size10)
    i = 2
    print(f"\n===== n={n}  middle block i={i} size={sizes[i]} =====")
    # group patterns by c = pat[i]
    byc = {}
    for p in pats:
        c = p[i]
        if c >= 2:
            byc.setdefault(c, []).append(p)
    for c in sorted(byc):
        vals = set()
        for p in byc[c]:
            v = g_direct(n, i, c, p)
            vals.add(v)
            print(f"  c={c} pattern {p}: direct g={v}")
        exp = g_expected.get(c)
        print(f"    -> patterns with c={c}: distinct direct values {vals} "
              f"(pattern-independence: {len(vals)==1}); expected g={exp}")
