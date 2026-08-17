#!/usr/bin/env python3
"""Test the count-factorization model exactly at n=6,7 and by sampling at n=8.

Model (conjectured): #(n-1)-convex subsets realizing block pattern {L,R} =
  product over blocks i of g_i(c_i),
where g_i(c) = C(|T_i|, c) EXCEPT for large-middle-block 'bumps', where
g_i(c) is a smaller per-block count (independent of the other blocks).
Verified exactly: n=6 -> bump size3 in size-6 block has g=10 (of 20);
  n=7 -> bump size3 in size-10 block g=46 (of 120), bump size4 g=41 (of 210).
So a pattern's count = prod g factors = exact product of independent
per-block compatibilities.  (2,3) at n=7 = 46*46 = 2116 = 46^2 confirms
independence, not coincidence.

Below we re-derive g at n=6,7 exactly for every pattern and test n=8 by
random sampling of subsets matching each of the C(7,2)=21 patterns.
"""
import random
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position

random.seed(12345)


def counts_per_pattern(n, limit_n8=40000):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    blk_of = {}
    off = 0
    sizes = []
    for b, blk in enumerate(blocks):
        sizes.append(len(blk))
        for p in blk:
            blk_of[off] = b
            off += 1
    B = len(blocks)
    r = n - 1
    cnt = Counter()
    if N <= 33:
        for comb in combinations(range(N), r):
            sub = [pts[i] for i in comb]
            if in_convex_position(sub):
                c = [0] * B
                for i in comb:
                    c[blk_of[i]] += 1
                cnt[tuple(c)] += 1
    else:  # n=8: sample
        # candidate patterns: all tuples c with sum=r, c_i<=sizes[i]
        from itertools import product
        def gen_pats(i, rem, cur):
            if i == B - 1:
                if rem <= sizes[i]:
                    yield tuple(cur + [rem])
                return
            for v in range(min(rem, sizes[i]) + 1):
                yield from gen_pats(i + 1, rem - v, cur + [v])
        pats = list(gen_pats(0, r, []))
        # for each pattern, sample subsets matching it, count convex fraction
        frac = {}
        for p in pats:
            S = 0
            Cc = 0
            rounds = 0
            while S < limit_n8:
                sel = []
                for b in range(B):
                    sel += random.sample(blocks[b], p[b])
                S += 1
                if in_convex_position([pts[i] for i in sel]):
                    Cc += 1
                rounds += 1
                if rounds > 200000:
                    break
            frac[p] = (Cc, S)
        cnt = frac
    return cnt, sizes


for n in (6, 7):
    cnt, sizes = counts_per_pattern(n)
    B = len(sizes)
    print(f"\n===== n={n} B={B} sizes={sizes} exact =====")
    for pat in sorted(cnt.keys()):
        c0 = list(pat)
        if cnt[tuple(c0)] == 0:
            continue
        prod = 1
        for i in range(B):
            prod *= comb(sizes[i], c0[i])
        print(f"  {c0} count={cnt[tuple(c0)]:6d} prod={prod:6d} "
              f"ratio={cnt[tuple(c0)]/prod:.4f}")

# n=8 sampling
cnt8, sizes8 = counts_per_pattern(8)
B8 = len(sizes8)
print(f"\n===== n=8 B={B8} sizes={sizes8} SAMPLED =====")
print("  Only sampling; counts below are convex-fraction estimates, not exact.")
for pat in sorted(cnt8.keys()):
    c0, tot = cnt8[pat]
    if tot == 0:
        continue
    prod = 1
    for i in range(B8):
        prod *= comb(sizes8[i], pat[i])
    print(f"  {list(pat)} sample convex {c0:6d}/{tot:6d} "
          f"frac={c0/tot:.4f} prod={prod}")
