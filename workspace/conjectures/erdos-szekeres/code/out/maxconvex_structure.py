"""Maximal-convex-subset structure of the VERIFIED ES construction.

For n in {5,6,7}, es_construct has N = 2^(n-2) points in blocks
T_0..T_{n-2} of sizes C(n-2,0..n-2), and its largest convex subset is n-1.
The largest (and hence every) (n-1)-convex subset is maximal.

We fully enumerate every (n-1)-subset that lies in convex position (exact
integer/Fraction arithmetic via lib/es_geom.in_convex_position) and report:

  (a) how many distinct (n-1)-convex subsets exist;
  (b) the block-index patterns: for each convex (n-1)-subset, how many points
      it takes from each block T_0..T_{n-2}; the distribution of patterns;
  (c) the precise conjecture verdict: 'every maximal (n-1)-convex subset takes
      exactly one point from each of the n-1 blocks' (i.e. is a full
      transversal), PASS/FAIL with counterexample witnesses.

Complexity: enumerating all C(N, n-1) subsets; C(32,6)=906192 at n=7, each
checked by an exact convex-hull test (O(m log m) per subset).  Exact and
feasible.
"""

from fractions import Fraction
from itertools import combinations
from collections import Counter
from time import time

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def build_block_map(blocks):
    """Returns (pt, block_index) list over all points in concatenated order."""
    mapping = []
    for i, blk in enumerate(blocks):
        for p in blk:
            mapping.append((p, i))
    return mapping


def analyze(n):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    nblocks = len(blocks)          # = n-1
    mapping = build_block_map(blocks)
    # point identity -> block index
    block_of = {}
    for idx, (p, b) in enumerate(mapping):
        block_of[idx] = b

    r = n - 1                      # we count all (n-1)-subsets
    total = 0
    convex = 0
    pattern_counter = Counter()
    counterexamples = []           # witnesses to the transversal conjecture

    t0 = time()
    for comb in combinations(range(N), r):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            convex += 1
            # block pattern
            pat = tuple(block_of[i] for i in comb)
            # pattern as counts per block index (ordered by block index)
            counts = [0] * nblocks
            for i in comb:
                counts[block_of[i]] += 1
            counts = tuple(counts)
            pattern_counter[counts] += 1
            if counts != (1,) * nblocks:
                if len(counterexamples) < 5:
                    counterexamples.append(comb)
        total += 1
    dt = time() - t0

    # verdict on the transversal conjecture
    non_trans = sum(c for pat, c in pattern_counter.items() if pat != (1,) * nblocks)
    verdict = "PASS" if non_trans == 0 else "FAIL"

    print(f"=== n={n}: N={N}, r={r}, blocks={nblocks}, block sizes={[len(b) for b in blocks]} ===")
    print(f"total (n-1)-subsets checked: {total}")
    print(f"distinct (n-1)-convex subsets: {convex}")
    print(f"wall clock: {dt:.2f} s")
    print(f"\n(b) distribution of block-index patterns (counts per block T_0..T_{nblocks-1}):")
    for pat, c in sorted(pattern_counter.items()):
        print(f"   pattern {pat}: {c}")
    print(f"\n(c) transversal conjecture (every maximal (n-1)-convex subset is a full "
          f"transversal taking exactly one point from each of the {nblocks} blocks):")
    print(f"   VERDICT: {verdict}")
    if non_trans > 0:
        print(f"   non-transversal convex (n-1)-subsets: {non_trans}")
        for i, w in enumerate(counterexamples):
            counts = tuple(block_of[ii] for ii in w)
            idxs = tuple(sorted(counts))
            print(f"     witness {i+1}: point-indices {w}, "
                  f"block-points-taken {tuple(counts.count(b) for b in range(nblocks))}")
    print()
    return {"n": n, "convex": convex, "patterns": dict(pattern_counter),
            "verdict": verdict, "wall": dt}


def main():
    for n in (5, 6, 7):
        analyze(n)


if __name__ == "__main__":
    main()
