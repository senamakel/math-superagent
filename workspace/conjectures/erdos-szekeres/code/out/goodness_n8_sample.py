#!/usr/bin/env python3
"""n=8 consistency test of the per-pattern count factorization, by sampling.

If count(pattern) = prod_i g_i(c_i) with g pattern-independent, then for a
single-bump pattern, the convex fraction equals g_bump(c)/C(s_bump,c).
So the estimated g for all single-bump patterns on the same (bumped block, c)
must agree.  We sample and check agreement (n=8 is too big to enumerate).
"""
import random
from itertools import combinations
from math import comb
from collections import defaultdict
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position

random.seed(99)


def sample_single_bump(n, per_pattern=800):
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    B = len(blocks)
    r = n - 1
    out = []
    for bi in range(B):
        for c in range(2, sizes[bi] + 1):
            rem = r - c
            if rem < 0:
                continue
            others = [j for j in range(B) if j != bi]
            for pick in combinations(others, rem):
                pat = [0] * B
                pat[bi] = c
                for j in pick:
                    pat[j] = 1
                Cc = S = 0
                tries = 0
                while S < per_pattern and tries < 300000:
                    sel = []
                    for bj in range(B):
                        if pat[bj]:
                            sel += random.sample(blocks[bj], pat[bj])
                    tries += 1
                    S += 1
                    if in_convex_position(sel):
                        Cc += 1
                frac = Cc / S if S else 0
                g_est = frac * comb(sizes[bi], c)
                out.append((bi, c, pat, Cc, S, frac, g_est))
    return out, sizes


res, sizes = sample_single_bump(8)
print("n=8 block sizes:", sizes)
bykey = defaultdict(list)
for (bi, c, pat, Cc, S, frac, g) in res:
    bykey[(bi, c)].append((pat, Cc, S, frac, g))
print("\nEstimated g_bump(c) per (bumped block, c); factorization => same value:")
for (bi, c) in sorted(bykey):
    vals = bykey[(bi, c)]
    gs = [v[4] for v in vals]
    mean = sum(gs) / len(gs)
    spread = max(gs) - min(gs)
    npat = len(vals)
    print(f"  block {bi} (size {sizes[bi]}) c={c}: {npat} patterns, "
          f"g mean={mean:.1f}, min={min(gs):.1f}, max={max(gs):.1f}, spread={spread:.1f}")
