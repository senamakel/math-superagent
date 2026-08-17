#!/usr/bin/env python3
"""Test the closed-form conjecture for the T_1-block goodness g_1(c).

Observed (exact captures, n=4..7): for the block T_1 of es_construct(n),
size m = |T_1| = C(n-2,1) = n-2,
    g_1(c) = C(m, c)  for c in {0,1,2,m},   g_1(c)=0 for 3<=c<=m-1.
i.e. the goodness is full binomial on the allowed values {0,1,2,m},
and the disallowed interior values 3..m-1 are zero (no completion).

n=4: m=2 g={0:1,1:2,2:1}  (2=m, empty interior)   OK
n=5: m=3 g={0:1,1:3,2:3,3:1}                       OK
n=6: m=4 g={0:1,1:4,2:6,4:1}  interior {3} zero     OK
n=7: m=5 g={0:1,1:5,2:10,5:1} interior {3,4} zero  OK

TARGETED n=8 test (no full C(64,7) enumeration):
  T_1 has size m=6.  Test g_1(2) == C(6,2) == 15:
    for each 2-subset S of block 1, does there EXIST one point each from
    blocks 2..6 such that the 7 chosen points (pattern D=(0,2,1,1,1,1,1))
    lie in convex position?  If exactly 15 are completable, conjecture survives.
  Also test g_1(1): trivially all 6 singletons complete (transversal).
Cost: 15 * (15*20*15*6*1) convexity checks, exact Fraction arithmetic.
"""
from itertools import combinations
from math import comb
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    # 1) Verify the closed form compiles on the exact n=4..7 recovery
    print("=== Closed-form check on recovered g_1 (n=4..7) ===")
    known = {  # (n, m) -> g_1 dict from goodness_recovered.captured.txt
        4: (2, {0: 1, 1: 2, 2: 1}),
        5: (3, {0: 1, 1: 3, 2: 3, 3: 1}),
        6: (4, {0: 1, 1: 4, 2: 6, 4: 1}),
        7: (5, {0: 1, 1: 5, 2: 10, 5: 1}),
    }
    allok = True
    for n in sorted(known):
        m, g = known[n]
        model = {}
        for c in range(0, m + 1):
            if c in (0, 1, 2, m):
                model[c] = comb(m, c)
            else:
                model[c] = 0
        # compare only on g's recorded keys (recovered) + interior zeros
        ok = True
        for c, v in model.items():
            rec = g.get(c, 0)
            if rec != v:
                ok = False
        # also confirm no extra keys in recovered g
        for c in g:
            if model.get(c, 0) != g[c]:
                ok = False
            if c not in (0, 1, 2, m):
                ok = False  # interior value present -> breaks conjecture
        allok &= ok
        print(f"  n={n} m={m}: recovered {g} model(C(m,c) on {{0,1,2,m}}) -> "
              f"{'OK' if ok else 'MISMATCH'}")
    print(f"  all n=4..7 match closed form: {allok}")

    # 2) Targeted n=8 computation of g_1(2)
    print("\n=== Targeted n=8: g_1(2) == C(6,2)=15 ===")
    pts, blocks = es_set_blocks(8)
    sizes = [len(b) for b in blocks]
    print(f"  n=8 block sizes: {sizes}")
    assert sizes[1] == 6, sizes
    good = 0
    good_sets = []
    for S in combinations(blocks[1], 2):
        found = False
        # pattern D=(1:2 from block1, and 1 each from blocks 2..6, 0 from block 0)
        # completions: choose 1 from each of blocks 2,3,4,5,6
        lists = [list(blocks[j]) for j in (2, 3, 4, 5, 6)]
        from itertools import product
        for combo in product(*lists):
            pts_s = list(S) + list(combo)
            if in_convex_position(pts_s):
                found = True
                break
        if found:
            good += 1
            good_sets.append(S)
    print(f"  g_1(2) exact = {good}, expected C(6,2) = {comb(6,2)}  "
          f"-> {'SURVIVES' if good == comb(6,2) else 'REFUTED'}")
    if good != comb(6, 2):
        print("  non-completable 2-subsets:", [s for s in combinations(blocks[1], 2)
                                               if s not in set(good_sets)])


if __name__ == "__main__":
    main()
