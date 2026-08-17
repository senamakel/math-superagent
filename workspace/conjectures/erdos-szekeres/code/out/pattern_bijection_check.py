#!/usr/bin/env python3
"""Test the explicit bijection conjectured for the triangular realized-pattern-
class count (report4 / es-construct-realized-pattern-classes-triangular):
   realized (n-1)-convex block patterns of es_construct(n)  <->  unordered pairs
   {L,R} of blocks, 0 <= L < R <= n-2,  given by the closed-form profile

       c_i = 0            for i < L  or  i > R
       c_L = L + 1
       c_R = B - R          (B = n-1 total blocks)
       c_i = 1            for L < i < R

   sum c_i = (L+1)+ (R-L-1)*1 + (B-R) = B = n-1, so every candidate has the
   right total size.  Claim: a pattern p is REALIZED (some (n-1)-subset with
   that block pattern is in convex position)  iff  p equals the formula pattern
   for some pair {L,R}.  Equivalently, #realized = C(B,2) triangular.

For n=4..7 the check is EXHAUSTIVE (all C(N,n-1) subsets, exact es_geom oracle).
At n=8 C(64,7)=621M is too large to enumerate; instead for every formula pattern
we sample and confirm at least one convex realization (existence), which is the
directional content that matters for the bijection.
"""
from itertools import combinations
from math import comb as C
from random import Random
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def formula_patterns(B):
    """All C(B,2) patterns from unordered block pairs (L,R), 0<=L<R<=B-1."""
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


def exact_realized_classes(n, pts, blocks):
    """Exhaustive: every (n-1)-subset, convex?, record its block pattern."""
    N = len(pts)
    nb = len(blocks)
    block_of = {}
    off = 0
    for b, blk in enumerate(blocks):
        for _ in blk:
            block_of[off] = b
            off += 1
    realized = set()
    for comb in combinations(range(N), n - 1):
        sub = [pts[i] for i in comb]
        if in_convex_position(sub):
            cnt = [0] * nb
            for i in comb:
                cnt[block_of[i]] += 1
            realized.add(tuple(cnt))
    return realized


def main():
    print("=== Bijection check: realized patterns == formula C(B,2) patterns ===\n")
    for n in (4, 5, 6, 7):
        pts, blocks = es_set_blocks(n)
        B = n - 1
        realized = exact_realized_classes(n, pts, blocks)
        formula = formula_patterns(B)
        missing = formula - realized   # formula patterns with no convex realization
        spurious = realized - formula  # realized patterns not in formula
        ok = (not missing) and (not spurious)
        print(f"n={n}: B={B} |realized|={len(realized)} C({B},2)={C(B,2)} "
              f"formula={len(formula)} missing={len(missing)} "
              f"spurious={len(spurious)} -> {'BIJECTION PASS' if ok else 'FAIL'}")
        if missing:
            print("   missing formula patterns:", sorted(missing))
        if spurious:
            print("   spurious realized patterns:", sorted(spurious))

    # n=8: existence of each formula pattern (sampled, exact convexity)
    n = 8
    pts, blocks = es_set_blocks(n)
    B = n - 1
    sizes = [len(b) for b in blocks]
    ranges = []
    off = 0
    for b in range(B):
        ranges.append(list(range(off, off + sizes[b])))
        off += sizes[b]
    formula = formula_patterns(B)
    print(f"\nn={n}: B={B}, formula patterns to test for realizability: {len(formula)} "
          f"(C({B},2)={C(B,2)}) — sampling, not exhaustive")
    rng = Random(11)
    K = 300
    realized = set()
    for pat in formula:
        found = False
        for _ in range(K):
            sel = []
            for i in range(B):
                sel.extend(rng.sample(ranges[i], pat[i]))
            sub = [pts[j] for j in sel]
            if in_convex_position(sub):
                found = True
                break
        if found:
            realized.add(pat)
    print(f"   formula patterns realized in sample: {len(realized)}/{len(formula)}")
    missing = [p for p in sorted(formula) if p not in realized]
    if missing:
        print("   NOT found in sample (could be rare/convex-missed):", missing)
    else:
        print("   every formula pattern has a convex realization (sample) -> supportive")


if __name__ == "__main__":
    main()
