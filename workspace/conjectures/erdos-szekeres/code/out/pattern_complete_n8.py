#!/usr/bin/env python3
"""Completeness check at n=8: is the FULL-pattern set EXACTLY the six candidates?

For every block-count pattern of (n-1)-subsets of es_construct(8) that is NOT
one of the six FULL candidates, find ONE non-convex realization (sampling up to
L).  A found non-convex realization proves the pattern is NOT full.  If every
non-six pattern has a non-convex realization, the six are exactly the FULL set.
The six themselves were shown fully-convex exhaustively in pattern_factor_n8.py.
"""
from itertools import combinations, product, islice
from math import comb as C

from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def main():
    n = 8
    pts, blocks = es_set_blocks(n)
    sizes = [len(b) for b in blocks]
    nb = len(sizes)
    r = n - 1
    print(f"n={n} sizes={sizes}")

    # the six FULL candidates (from pattern_factor_n8.py)
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
    the_six = {pat_a(), pat_b(), pat_fulltrans(), pat_d(), pat_e(), pat_f()}
    for p in the_six: assert sum(p) == r, (p, sum(p), r)

    # enumerate all patterns (sum=r, pat[i]<=sizes[i])
    def gen_pats(i, rem, cur):
        if i == nb:
            if rem == 0:
                yield tuple(cur)
            return
        mx = min(sizes[i], rem)
        for v in range(mx + 1):
            cur.append(v)
            yield from gen_pats(i + 1, rem - v, cur)
            cur.pop()

    def realizations(sizes, pat):
        off = 0
        pos = []
        for s in sizes:
            pos.append(list(range(off, off + s)))
            off += s
        choice_lists = [combinations(pos[i], pat[i]) for i in range(nb)]
        for combo in product(*choice_lists):
            idxs = [x for g in combo for x in g]
            yield [pts[j] for j in idxs]

    non_full_found = 0
    could_not_prove = []
    npats = 0
    L = 4000
    for pat in gen_pats(0, r, []):
        npats += 1
        if pat in the_six:
            continue
        # try to find a non-convex realization
        found = False
        cnt = 0
        for sub in realizations(sizes, pat):
            cnt += 1
            if not in_convex_position(sub):
                found = True
                break
            if cnt >= L:
                break
        if found:
            non_full_found += 1
        else:
            could_not_prove.append((pat, cnt))
    print(f"patterns enumerated: {npats} (six FULL excluded)")
    print(f"non-six patterns with a found non-convex realization (proven non-full): {non_full_found}")
    print(f"non-six patterns where no non-convex found in <=L samples (NOT proven, maybe FULL): {len(could_not_prove)}")
    for p, c in could_not_prove[:50]:
        print("   unproven:", p, "samples", c)
    if not could_not_prove:
        print("COMPLETE: exactly the six patterns are FULL at n=8.")


if __name__ == "__main__":
    main()
