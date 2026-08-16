#!/usr/bin/env python3
"""Per-block cup/cap achieved by the es_construct ES construction, across n.

For block i of X_n: claimed no (n-i)-cup (so cup <= n-i) and no (i+2)-cap
(cap <= i+2).  Report the ACHIEVED longest cup and cap per block so a
tightness regularity (if any) can be seen across n.
"""
from lib.es_construct import es_block
from lib.es_geom import longest_cup, longest_cap
from math import comb

for n in range(3, 8):
    print(f"n={n}:  blocks C(n-2,i)={[comb(n-2,i) for i in range(n-1)]}")
    # header
    cuprow = []
    caprow = []
    sizerow = []
    for i in range(n - 1):
        T = es_block(n, i)
        sizerow.append(len(T))
        cuprow.append(longest_cup(T))
        caprow.append(longest_cap(T))
    print(f"   size : {sizerow}")
    print(f"   cup  : {cuprow}   (bound no-(n-i)-cup: {[n-i for i in range(n-1)]})")
    print(f"   cap  : {caprow}   (bound no-(i+2)-cap: {[i+2 for i in range(n-1)]})")
    # cup + cap and cup - i, cap - i
    print(f"   cup_i + i : {[cuprow[i]+i for i in range(n-1)]}")
    print(f"   cap_i - i : {[caprow[i]-i for i in range(n-1)]}")
    print()
