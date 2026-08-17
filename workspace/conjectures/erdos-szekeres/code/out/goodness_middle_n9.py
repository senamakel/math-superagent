#!/usr/bin/env python3
"""Exact g_2(3) at n=9: # 3-subsets S of middle block T_2 (size 21) that
complete to a convex 8-gon with 1 point each from blocks 3,4,5,6,7
(pattern {2,7}: (0,0,3,1,1,1,1,1), sum 8).

Parallelized over the C(21,3)=1330 subsets across CPUs; existence search with
early exit.  Exact Fraction convexity via lib.es_geom.

Closed-form conjecture to test: g(m)=cumulative-sum of T_k^2 predicts 371.
"""
import multiprocessing as mp
from itertools import combinations, product
from math import comb
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def worker(args):
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
    print(f"building jobs: {total} subsets, combos per = "
          f"{'*'.join(str(len(p)) for p in other_points)} "
          f"= {len(other_points[0])*len(other_points[1])*len(other_points[2])*len(other_points[3])*len(other_points[4])}",
          flush=True)
    jobs = [(i, S, other_points) for i, S in enumerate(subsets)]
    ncpu = mp.cpu_count()
    print(f"using {ncpu} workers", flush=True)
    good = 0
    done = 0
    with mp.Pool(ncpu) as pool:
        for S_idx, ok in pool.imap_unordered(worker, jobs, chunksize=10):
            done += 1
            if ok:
                good += 1
            if done % 200 == 0:
                print(f"  done {done}/{total}  completable so far {good}", flush=True)
    print(f"EXACT g_2(3) at n=9 = {good}  (C(21,3)={comb(21,3)})  "
          f"closed-form prediction 371 -> {'CONFIRMED' if good==371 else 'REFUTED'}", flush=True)


if __name__ == "__main__":
    main()
