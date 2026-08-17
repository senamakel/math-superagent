#!/usr/bin/env python3
"""Randomized strong test of the six-FULL-pattern family at n=9 (out-of-sample).

At n=5,6,7,8 all six candidate block-count patterns are FULL (every realizing
(n-1)-subset is convex); controls are not.  Full enumeration at n=9 is
infeasible (full transversal barely is 26M, and the (0,2,1,...) ones are ~1e8),
so test randomly: for each candidate FULL pattern sample up to K random
realizations; if even ONE is non-convex the pattern is refuted at n=9.  If none
in K samples, that is supportive (not proof) for that pattern.
"""
from math import comb as C
from itertools import combinations
from random import Random

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def random_realization(sizes, pat, pts, rng):
    """Pick pat[i] points uniformly from block i."""
    off = 0
    sel = []
    for i, s in enumerate(sizes):
        idxs = list(range(off, off + s))
        chosen = rng.sample(idxs, pat[i])
        sel.extend(chosen)
        off += s
    return [pts[j] for j in sel]


def main():
    n = 9
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    nb = len(sizes)
    r = n - 1
    assert sum(sizes) == 2 ** (n - 2) == 128
    print(f"n={n}  N={len(pts)}  blocks={nb}  sizes={sizes}")

    def mk(*vals):
        # vals as dict of (index->value), rest 0
        p = [0] * nb
        for i, v in vals:
            p[i] = v
        return tuple(p)

    # the six candidate FULL patterns (confirmed FULL at n=5..8)
    full_candidates = [
        mk((nb - 2, sizes[nb - 2]), (nb - 1, 1)),          # all of block n-3 + 1 of n-2
        mk((0, 1), (1, sizes[1])),                          # 1 of block0 + all of block1
        tuple([1] * nb),                                    # full transversal
        mk((0, 0), (1, 2)) + tuple([1] * (nb - 2)),        # (0,2,1,...,1)
        tuple([1] * (nb - 2)) + mk((nb - 1, 0), (nb - 2, 2)),  # (1,...,1,2,0)
        mk((0, 0), (1, 2)) + tuple([1] * (nb - 4)) + mk((nb - 2, 2), (nb - 1, 0)),  # (0,2,1..1,2,0)
    ]
    # fix: build cleanly
    def pc(core, nbfull):
        return tuple(core) if len(tuple(core)) == nbfull else None

    # rebuild unambiguously
    def pat_fulltrans():
        return tuple([1] * nb)
    def pat_a():
        p = [0]*nb; p[nb-2]=sizes[nb-2]; p[nb-1]=1; return tuple(p)
    def pat_b():
        p = [0]*nb; p[0]=1; p[1]=sizes[1]; return tuple(p)
    def pat_d():
        p = [1]*nb; p[0]=0; p[1]=2; return tuple(p)
    def pat_e():
        p = [1]*nb; p[nb-1]=0; p[nb-2]=2; return tuple(p)
    def pat_f():
        p = [1]*nb; p[0]=0; p[nb-1]=0; p[1]=2; p[nb-2]=2; return tuple(p)
    full_candidates = [pat_a(), pat_b(), pat_fulltrans(), pat_d(), pat_e(), pat_f()]

    rng = Random(12345)
    for pat in full_candidates:
        # sanity: sum
        assert sum(pat) == r, pat
        K = 60000
        bad = 0
        for _ in range(K):
            sub = random_realization(sizes, pat, pts, rng)
            if not in_convex_position(sub):
                bad += 1
                break
        print(f"FULL-cand {pat} sampled={K} non_convex_in_sample={bad} "
              f"-> {'PASS (no fail in sample)' if bad==0 else 'REFUTED at n=9'}")
        if bad:
            break


if __name__ == "__main__":
    main()
