#!/usr/bin/env python3
"""Re-check the es-construct-block-tightness claim with a CORRECT brute-force
longest_cap/longest_cup.  The claim says every interior block T_i of X_n has
longest_cup(T_i)=n-i-1 and longest_cap(T_i)=i+1 (so cup+cap=n).  The es_geom
longest_cap was found buggy (undershoots); check what the true values are.
"""
from itertools import combinations
from lib.es_construct import es_set_blocks
from math import comb


def slope(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])


def brute_longest_cup(S):
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    if m == 0:
        return 0
    for r in range(m, 1, -1):
        for comb_ in combinations(range(m), r):
            ok = True
            for t in range(1, r - 1):
                if not (slope(pts[comb_[t-1]], pts[comb_[t]]) < slope(pts[comb_[t]], pts[comb_[t+1]])):
                    ok = False
                    break
            if ok:
                return r
    return 1


def brute_longest_cap(S):
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    if m == 0:
        return 0
    for r in range(m, 1, -1):
        for comb_ in combinations(range(m), r):
            ok = True
            for t in range(1, r - 1):
                if not (slope(pts[comb_[t-1]], pts[comb_[t]]) > slope(pts[comb_[t]], pts[comb_[t+1]])):
                    ok = False
                    break
            if ok:
                return r
    return 1


for n in (4, 5, 6, 7):
    allp, blocks = es_set_blocks(n)
    rows = []
    for i, blk in enumerate(blocks):
        b_cu = brute_longest_cup(blk)
        b_ca = brute_longest_cap(blk)
        exp_cu = n - i - 1 if (1 <= i <= n - 3) else 1
        exp_ca = i + 1 if (1 <= i <= n - 3) else 1
        rows.append((i, len(blk), b_cu, exp_cu, b_ca, exp_ca))
    print(f"n={n}: |T_i| row = {[len(b) for b in blocks]}")
    for i, sz, cu, ecu, ca, eca in rows:
        cuok = cu == ecu
        caok = ca == eca
        print(f"   i={i}: |T|={sz} brute_cup={cu} (exp {ecu}, {'ok' if cuok else '***'}) "
              f"brute_cap={ca} (exp {eca}, {'ok' if caok else '***'}) "
              f"cup+cap={cu+ca} (exp {ecu+eca})")
