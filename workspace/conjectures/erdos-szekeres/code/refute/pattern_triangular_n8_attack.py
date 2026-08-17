#!/usr/bin/env python3
"""REFUTER attack on es-construct-realized-pattern-classes-triangular at n=8.

Claim attacked (a run-owned finding, flagged most-likely-false because the n=8
evidence is SAMPLED):
    "In the verified es_construct ES construction X_8 (N=64 points, blocks
     T_0..T_6, |T_i| = C(6,i), no convex 7-gon), the number of distinct
     block-count patterns realized by 7-convex subsets equals C(7,2)=21."

Sampling can only under-count realized classes, so a convex 7-subset of
es_construct(8) whose block-count pattern is NOT among the claimed 21 refutes
'exactly 21 at n=8'.  The previous n=8 evidence was K=150 realizations per
candidate pattern (pattern_class_n8_direct.py) — too thin to rule out a rare
22nd class.

Method (exact integer arithmetic, lib.es_geom.in_convex_position, never float):
  Phase 0  sanity: every formula pattern (the claimed 21) realizes.
  Phase 1  reproduce: moderate sample over ALL candidate patterns (sum 7,
           c_i <= |T_i|) to re-derive the 21.
  Phase 2  heavy hunt: for every candidate pattern NOT yet realized, sample
           far more realizations, parallel over 28 cores, looking for any
           convex 7-subset outside the 21.
           A hit prints REFUTED with the witness pattern.

Declared cost class: exponential in the subset size being tested is avoided;
cost is polynomial in (#candidate patterns * K * hull work).  #candidate
patterns = 874, so this is ~874 * K convexity tests of 7-point sets.

A 'no hit' result is honest evidence for 'exactly 21 at n=8' but NOT a proof —
it says which sizes were covered.  Run under the safe capture idiom:
cd /workspace && { echo "$ python code/refute/pattern_triangular_n8_attack.py";
timeout 550 python code/refute/pattern_triangular_n8_attack.py;
echo "EXIT: $?"; } > code/out/pattern_triangular_n8_attack.captured.txt 2>&1
"""
import random
from multiprocessing import Pool
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def build(n):
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    ranges = []
    off = 0
    for b in range(len(blocks)):
        ranges.append(list(range(off, off + sizes[b])))
        off += sizes[b]
    return pts, blocks, sizes, ranges


def formula_patterns(B):
    """The claimed 21: c_L=L+1, c_R=B-R, c_i=1 between, from block pair {L,R}."""
    pats = set()
    for L in range(B):
        for R in range(L + 1, B):
            c = [0] * B
            c[L] = L + 1
            c[R] = B - R
            for i in range(L + 1, R):
                c[i] = 1
            pats.add(tuple(c))
    return pats


def enumerate_candidates(nblk, sizes, r):
    cand = []
    def rec(i, rem, cur):
        if i == nblk - 1:
            if rem <= sizes[i]:
                cand.append(tuple(cur + [rem]))
            return
        for v in range(min(sizes[i], rem) + 1):
            rec(i + 1, rem - v, cur + [v])
    rec(0, r, [])
    return cand


def sample_pattern(args):
    pat, n, K, seed = args
    pts, blocks, sizes, ranges = build(n)
    rng = random.Random(seed)
    nblk = len(blocks)
    for _ in range(K):
        sel = []
        for i in range(nblk):
            sel.extend(rng.sample(ranges[i], pat[i]))
        sub = [pts[j] for j in sel]
        if in_convex_position(sub):
            return pat
    return None


def main():
    import sys
    K_phase1 = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    K_heavy = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
    n = 8
    pts, blocks, sizes, ranges = build(n)
    nblk = len(blocks)
    r = 7
    cand = enumerate_candidates(nblk, sizes, r)
    formula = formula_patterns(nblk)
    print(f"n={n}: blocks={nblk}, candidate block patterns sum {r}: {len(cand)}")
    print(f"     claimed formula patterns (21): {len(formula)}")

    # Phase 0: every formula pattern realizes (directional support for the 21)
    jobs = [(pat, n, 300, 7 + i) for i, pat in enumerate(sorted(formula))]
    with Pool(28) as p:
        res = p.map(sample_pattern, jobs)
    realized_formula = [pat for pat, got in zip(sorted(formula), res) if got is not None]
    print(f"\nPhase0: formula patterns realized in sample: {len(realized_formula)}/{len(formula)}")
    for pat in sorted(formula - set(realized_formula)):
        print("   NOT realized in sample:", pat)

    # Phase 1: reproduce the 21 realized classes by moderate sampling
    jobs = [(pat, n, K_phase1, 12345 + i) for i, pat in enumerate(cand)]
    with Pool(28) as p:
        res = p.map(sample_pattern, jobs)
    realized = [pat for pat, got in zip(cand, res) if got is not None]
    print(f"\nPhase1: realized classes with K={K_phase1}: {len(realized)}")
    for pat in sorted(realized):
        print("   ", pat)
    print(f"   realized == formula? {set(realized) == formula}")

    # Phase 2: heavy hunt for a 22nd class
    not_yet = [pat for pat in cand if pat not in set(realized)]
    print(f"\nPhase2: heavy hunt over {len(not_yet)} not-yet-realized patterns x K={K_heavy}")
    jobs = [(pat, n, K_heavy, 999 * i + 1) for i, pat in enumerate(not_yet)]
    with Pool(28) as p:
        res = p.map(sample_pattern, jobs)
    new = [pat for pat, got in zip(not_yet, res) if got is not None]
    if new:
        print(f"!! REFUTED at n=8: found {len(new)} realized class(es) outside the 21:")
        for pat in sorted(new):
            print("   ", pat)
    else:
        print(f"no convex realization among {len(not_yet)} non-realized patterns "
              f"x K={K_heavy} each. Supports 'exactly 21 at n=8' over these sizes; "
              f"still not a proof.")
    print("done")


if __name__ == "__main__":
    main()
