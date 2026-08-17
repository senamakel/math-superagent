#!/usr/bin/env python3
"""Pattern-finder: exact structural regularities of the ES construction's
maximal (n-1)-convex subsets.

For the verified es_construct (blocks T_0..T_{n-2}, |T_i|=C(n-2,i)):
  * enumerate every (n-1)-convex subset, record its block-index pattern
    (count of points taken from each block);
  * check REVERSAL SYMMETRY: the multiset of pattern counts is invariant
    under i -> (n-2)-i (a reflection of the order-type-preserving kind);
  * check the FULL-TRANSVERSAL diagonal (1,1,..,1) count == prod C(n-2,i)
    == A001142(n-2) (all transversals convex -- established in memory).

Everything exact (lib.es_geom.in_convex_position on Fraction coords).
"""
from itertools import combinations
from collections import defaultdict
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position
from math import comb, prod


def build_block_of(blocks):
    block_of = []
    for i, blk in enumerate(blocks):
        block_of.extend([i] * len(blk))
    return block_of


def pattern_table(n):
    pts, blocks = es_set_blocks(n)
    block_of = build_block_of(blocks)
    nblocks = len(blocks)
    counts = defaultdict(int)
    for comb_ in combinations(range(len(pts)), n - 1):
        sub = [pts[i] for i in comb_]
        if in_convex_position(sub):
            pat = [0] * nblocks
            for i in comb_:
                pat[block_of[i]] += 1
            counts[tuple(pat)] += 1
    return dict(counts)


def check_reversal(counts, nblocks):
    """Each pattern and its reversal (reverse tuple) must have equal count."""
    ok = True
    bad = []
    seen = set()
    for pat, c in counts.items():
        if pat in seen:
            continue
        rev = tuple(reversed(pat))
        seen.add(pat); seen.add(rev)
        if counts.get(rev) != c:
            ok = False
            bad.append((pat, c, rev, counts.get(rev)))
    return ok, bad


for n in (5, 6):
    counts = pattern_table(n)
    nblocks = n - 1
    # full-transversal diagonal
    full = tuple([1] * nblocks)
    ft_count = counts.get(full, 0)
    expect = prod(comb(n - 2, i) for i in range(nblocks))
    # reversal symmetry
    ok, bad = check_reversal(counts, nblocks)
    print(f"n={n}: blocks={[comb(n-2,i) for i in range(nblocks)]} "
          f"num patterns={len(counts)}")
    print(f"   full-transversal (1,...,1) count={ft_count}  "
          f"expect prod C(n-2,i)={expect}  A001142({n-2})  match={ft_count==expect}")
    print(f"   reversal symmetry (all paired counts equal): {'PASS' if ok else 'FAIL'}")
    if bad:
        for b in bad[:5]:
            print(f"      MISMATCH {b}")
    # print the full table
    print("   pattern -> count (sorted):")
    for pat in sorted(counts):
        print(f"      {pat} -> {counts[pat]}")
    print()
