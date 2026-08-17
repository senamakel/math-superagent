#!/usr/bin/env python3
"""n=9 middle-block goodness g_2(3), two-phase exact:
  Phase 1: for each 3-subset S of block T_2, try up to K random completions
           (1 point each from blocks 3..7); if one is convex (exact check) mark
           completable (EXACT positive verdict).  Reporting a found convex
           completion is exact; only 'not found in K' risks undercounting.
  Phase 2: exact exhaustive existence only on the unresolved subsets.
Parallel, 28 CPUs.
"""
import multiprocessing as mp
import random
from itertools import combinations, product
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position

K = 4000


def phase1(args):
    S_idx, S, other_points = args
    rng = random.Random(S_idx * 7919 + 12345)
    op = other_points
    for _ in range(K):
        combo = tuple(rng.choice(lst) for lst in op)
        ps = list(S) + list(combo)
        if in_convex_position(ps):
            return S_idx, 1, None  # completable (exact)
    return S_idx, 0, S  # unresolved in sampling


def phase2(args):
    S_idx, S, other_points = args
    for combo in product(*other_points):
        ps = list(S) + list(combo)
        if in_convex_position(ps):
            return S_idx, True
    return S_idx, False


def main():
    n = 9
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    print("n=9 block sizes:", sizes, flush=True)
    other_idxs = [3, 4, 5, 6, 7]
    other_points = [list(blocks[j]) for j in other_idxs]
    subsets = list(combinations(blocks[2], 3))
    total = len(subsets)
    print(f"subsets={total} combos_base={'*'.join(str(len(p)) for p in other_points)} "
          f"K={K}", flush=True)
    ncpu = mp.cpu_count()
    jobs = [(i, S, other_points) for i, S in enumerate(subsets)]
    # phase 1
    good = 0
    unresolved = []
    with mp.Pool(ncpu) as pool:
        for S_idx, ok, S in pool.imap_unordered(phase1, jobs, chunksize=16):
            if ok:
                good += 1
            else:
                unresolved.append((S_idx, S))
    print(f"PHASE1: completable(probabilistic exact-pos)={good}, "
          f"unresolved={len(unresolved)}", flush=True)
    # phase 2 exact on unresolved
    bad = []
    exact_good = good
    if unresolved:
        ujobs = [(i, S, other_points) for i, S in unresolved]
        with mp.Pool(ncpu) as pool:
            for S_idx, ok in pool.imap_unordered(phase2, ujobs, chunksize=4):
                if ok:
                    exact_good += 1
                    bad.append(S)  # was in unresolved, found in phase2
                else:
                    bad.append(None)
    # bad contains either a resolved-convex or None(truly not);
    # exact_good already counts the phase2 positives.
    print(f"EXACT g_2(3) n=9 = {exact_good}  prediction 371 -> "
          f"{'CONFIRMED' if exact_good==371 else 'DIFFERS: '+str(exact_good)}", flush=True)


if __name__ == "__main__":
    main()
