#!/usr/bin/env python3
"""Verify longest_cup/longest_cap on es_construct with a CORRECT brute force.

Since a cap/cup is a SUBSET (points can be skipped), the DP must carry the
best-so-far forward.  The lib DP does not, so it may undercount.  Here we
brute-force all subsets for small n (N<=16) and compare with lib values.
Also tests whether whole-cap=2 is real (it should be >=3 if largest convex = n-1
but the whole set is not a single convex chain).
"""
from itertools import combinations
from lib.es_construct import es_set
from lib.es_geom import longest_cup, longest_cap, largest_convex_subset
from fractions import Fraction


def slope(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])  # Fraction


def brute_longest_cup(S):
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    best = 1 if m >= 1 else 0
    # iterate over all subsets in x-order, check strictly increasing slopes
    for r in range(m, 1, -1):
        for comb in combinations(range(m), r):
            ok = True
            for t in range(1, r - 1):
                if not (slope(pts[comb[t-1]], pts[comb[t]]) < slope(pts[comb[t]], pts[comb[t+1]])):
                    ok = False
                    break
            if ok:
                return r
    return 1 if m >= 1 else 0


def brute_longest_cap(S):
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    for r in range(m, 1, -1):
        for comb in combinations(range(m), r):
            ok = True
            for t in range(1, r - 1):
                if not (slope(pts[comb[t-1]], pts[comb[t]]) > slope(pts[comb[t]], pts[comb[t+1]])):
                    ok = False
                    break
            if ok:
                return r
    return 1 if m >= 1 else 0


for n in (4, 5, 6):
    S = es_set(n)
    m = len(S)
    lib_cu = longest_cup(S)
    lib_ca = longest_cap(S)
    b_cu = brute_longest_cup(S)
    b_ca = brute_longest_cap(S)
    k, _ = largest_convex_subset(S)
    print(f"n={n}: |S|={m} largest_convex={k}")
    print(f"   cup  lib={lib_cu} brute={b_cu} {'SAME' if lib_cu==b_cu else '*** LIB UNDERSHOOTS ***'}")
    print(f"   cap  lib={lib_ca} brute={b_ca} {'SAME' if lib_ca==b_ca else '*** LIB UNDERSHOOTS ***'}")
