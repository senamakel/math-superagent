#!/usr/bin/env python3
"""Factorize the (n-1)-convex-subset counts of es_construct.

Conjecture (new): the number of (n-1)-convex subsets of X_n realizing block
pattern c = (c_0..c_{B-1}) equals prod_i g_i(c_i), where g_i(c) is a
per-block "good subset" count, INDEPENDENT of the other blocks, defined as:
  g_i(0)=1, g_i(1)=|T_i|, and for c>=2, g_i(c)=# c-subsets S of block i such
  that S union {one fixed representative from each other block} is convex.

We compute g_i(c) EXACTLY by fixing a representative per other block (the
convexity of the completion must be independent of reps if factorization is
exact).  Then model count = prod g, compared (n=8) against sampled full
counts; and validated exactly at n=6,7 against the full enumeration.

Returns per-block g arrays and, at n=8, sampled verification.
"""
import random
from itertools import combinations
from math import comb
from collections import Counter
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position

random.seed(7)


def block_of_and_sizes(blocks):
    B = len(blocks)
    sizes = [len(b) for b in blocks]
    # global list of (blockidx, pt)
    pts = []
    owned = []
    for bi, b in enumerate(blocks):
        for p in b:
            pts.append(p)
            owned.append(bi)
    return pts, owned, sizes


def goodness(n, blocks, fix_lowest=True):
    """Compute g_i(c) for each block, c=0..sizes[i].
    Reps: pick the FIRST point of each other block."""
    pts, owned, sizes = block_of_and_sizes(blocks)
    B = len(blocks)
    reps = [blocks[bi][0] for bi in range(B)]  # first point of each block
    g = []
    for bi in range(B):
        sizes_i = sizes[bi]
        gi = [0] * (sizes_i + 1)
        gi[0] = 1
        gi[1] = sizes_i
        for c in range(2, sizes_i + 1):
            base = [reps[bi2] for bi2 in range(B) if bi2 != bi]  # one rep/other block
            cnt = 0
            for comb in combinations(blocks[bi], c):
                if in_convex_position(list(comb) + base):
                    cnt += 1
            gi[c] = cnt
        g.append(gi)
    return g


def exact_counts(n):
    pts, blocks = es_set_blocks(n)
    _, owned, sizes = block_of_and_sizes(blocks)
    N = len(pts)
    B = len(blocks)
    cnt = Counter()
    for comb in combinations(range(N), n - 1):
        if in_convex_position([pts[i] for i in comb]):
            c = [0] * B
            for i in comb:
                c[owned[i]] += 1
            cnt[tuple(c)] += 1
    return cnt, sizes


def sampled_counts(n, reps_each=8000):
    """Sample subsets per pattern at n=8 (too big to enumerate)."""
    pts, blocks = es_set_blocks(n)
    _, owned, sizes = block_of_and_sizes(blocks)
    B = len(blocks)
    # candidate patterns
    res = {}
    from itertools import product
    def gen(i, rem, cur):
        if i == B - 1:
            if rem <= sizes[i]:
                yield tuple(cur + [rem])
            return
        for v in range(min(rem, sizes[i]) + 1):
            yield from gen(i + 1, rem - v, cur + [v])
    for pat in gen(0, n - 1, []):
        Cc = S = 0
        tries = 0
        while S < reps_each and tries < 400000:
            sel = []
            for bi in range(B):
                sel += random.sample(blocks[bi], pat[bi])
            tries += 1
            S += 1
            if in_convex_position([pts[i] for i in sel]):
                Cc += 1
        # estimate fraction; convex count ~ fraction * prod C
        res[pat] = (Cc, S)
    return res, sizes


# ---- exact validation at n=6,7 ----
for n in (6, 7):
    cnt, sizes = exact_counts(n)
    blocks = es_set_blocks(n)[1]
    g = goodness(n, blocks)
    print(f"\n===== n={n} sizes={sizes} exact: model(prod g) vs true count =====")
    total_model = 0
    for pat, true in sorted(cnt.items()):
        model = 1
        for i in range(len(pat)):
            model *= g[i][pat[i]]
        total_model += model
        mark = "OK" if model == true else "MISMATCH"
        print(f"  {pat} true={true} model={model} {mark}")
    print(f"  total true={sum(cnt.values())} total model={total_model}")

# ---- n=8: compute g exactly, sample to compare ----
print("\n===== n=8: per-block goodness + sampled totals =====")
blocks8 = es_set_blocks(8)[1]
sizes8 = [len(b) for b in blocks8]
print("  n=8 block sizes:", sizes8)
g8 = goodness(8, blocks8)
for bi in range(len(blocks8)):
    print(f"  g_{bi} (c=0..{sizes8[bi]}): {g8[bi]}   [C(s,c) for ref: "
          f"{[comb(sizes8[bi],c) for c in range(sizes8[bi]+1)]}]")
sample, _ = sampled_counts(8)
print("\n  sample vs prod(g) for each pattern:")
for pat in sorted(sample.keys()):
    Cc, S = sample[pat]
    model = 1
    for i in range(len(pat)):
        model *= g8[i][pat[i]]
    # sampled estimate of true count = frac * prod(C)
    prodC = 1
    for i in range(len(pat)):
        prodC *= comb(sizes8[i], pat[i])
    est = (Cc / S) * prodC if S else 0
    rel = model / est if est else None
    print(f"  {list(pat)} sample convex {Cc}/{S} prodC={prodC} "
          f"model={model} est={est:.0f} rel={rel if rel is None else round(rel,3)}")
