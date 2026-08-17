#!/usr/bin/env python3
"""Test the 'six FULL block patterns' conjecture at n=8 (out-of-sample).

Hypothesis from n=5,6,7: among (n-1)-subsets of es_construct(n), exactly six
block-count patterns are FULL (EVERY realizing subset is convex). They are
reversal-symmetric and of the form (block sizes C(n-2,0..n-2)):

  (0^{n-3}, |T_{n-3}|, 1)        all of block n-3 + one of block n-2
  (1, |T_1|, 0^{n-3})            one of block 0 + all of block 1
  (1,1,...,1)                    full transversal
  (0, 2, 1,...,1)                two of block 1, one of rest
  (1,...,1, 2, 0)                reversal above
  (0,2,1,...,1,2,0)              symmetric: 2 of block1, 2 of block n-3, 1 rest

At n=8 blocks are [1,6,15,20,15,6,1] (7 blocks). For each candidate FULL pattern
we enumerate ALL realizations and require every one convex.  For control
NON-full patterns we require at least one NON-convex realization.  Exact
arithmetic via lib.es_geom.
"""
from math import comb as C
from itertools import combinations
from time import time

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def build_block_map(blocks):
    mapping, idx = [], 0
    for bi, blk in enumerate(blocks):
        for _ in blk:
            mapping.append(bi)
            idx += 1
    return mapping


def all_realizations(sizes, pat, pts):
    """Yield every (n-1)-subset (as point lists) with given block pattern."""
    nb = len(sizes)
    # positions in each block
    pos = []
    off = 0
    for s in sizes:
        pos.append(list(range(off, off + s)))
        off += s
    # pick pat[i] of the size[i] points in block i, chains
    import itertools as it
    choice_lists = [list(it.combinations(pos[i], pat[i])) for i in range(nb)]
    for combo in it.product(*choice_lists):
        idxs = [x for grp in combo for x in grp]
        yield [pts[i] for i in idxs]


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    nb = len(sizes)
    nb_ = nb
    r = n - 1
    print(f"n={n}  N={len(pts)}  blocks={nb_}  sizes={sizes}")
    assert sum(sizes) == 2 ** (n - 2)

    # candidate FULL patterns
    full_candidates = []
    # 1: all of block n-3 (T_{n-3}, size C(n-2,n-3)=n-2) + 1 of block n-2
    p = [0] * nb_
    p[nb_ - 2] = sizes[nb_ - 2]; p[nb_ - 1] = 1
    full_candidates.append(tuple(p))
    # 2: 1 of block 0 + all of block 1
    p = [0] * nb_
    p[0] = 1; p[1] = sizes[1]
    full_candidates.append(tuple(p))
    # 3: full transversal
    full_candidates.append((1,) * nb_)
    # 4: (0,2,1,1,...,1)
    p = [1] * nb_; p[0] = 0; p[1] = 2
    full_candidates.append(tuple(p))
    # 5: reversal of 4
    p = [1] * nb_; p[nb_ - 1] = 0; p[nb_ - 2] = 2
    full_candidates.append(tuple(p))
    # 6: (0,2,1,...,1,2,0)
    p = [1] * nb_; p[0] = 0; p[nb_ - 1] = 0; p[1] = 2; p[nb_ - 2] = 2
    full_candidates.append(tuple(p))

    t0 = time()
    for pat in full_candidates:
        total = 1
        for i in range(nb_):
            total *= C(sizes[i], pat[i])
        nonconv = 0
        checked = 0
        break_flag = False
        for sub in all_realizations(sizes, pat, pts):
            checked += 1
            if not in_convex_position(sub):
                nonconv += 1
                break_flag = True
                break
        print(f"FULL-cand {pat} total={total} checked={checked} "
              f"non_convex_seen={nonconv} -> {'PASS all convex' if not break_flag else 'FAIL'}")
    print(f"time for FULL candidates: {time()-t0:.1f}s")

    # control NON-full patterns: find a non-convex realization (sample up to N)
    controls = [
        (0, 0, 4, 1, 1, 1, 1),   # 4 from block 2
        (0, 0, 0, 4, 1, 1, 1),   # 4 from block 3
        (1, 1, 1, 4, 1, 0, 0),   # 4 from block 3, skip ends
        (0, 1, 2, 1, 1, 1, 1),   # 2 from block 2
        (0, 0, 0, 2, 2, 1, 1),   # two middle blocks double
    ]
    for pat in controls:
        from itertools import islice
        found_nonconv = False
        cnt = 0
        for sub in all_realizations(sizes, pat, pts):
            cnt += 1
            if not in_convex_position(sub):
                found_nonconv = True
                break
            if cnt >= 3000:
                break
        print(f"CONTROL {pat} checked={cnt} has_non_convex={found_nonconv}")


if __name__ == "__main__":
    main()
