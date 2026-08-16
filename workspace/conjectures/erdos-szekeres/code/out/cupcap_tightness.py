#!/usr/bin/env python3
"""Tightness of cupcap(k,l); small range with progress flush."""
import sys
from lib.es_construct import cupcap
from lib.es_geom import longest_cup, longest_cap
from math import comb

bad = []
count = 0
for k in range(3, 7):
    for l in range(3, 7):
        T = cupcap(k, l)
        count += 1
        cu = longest_cup(T)
        ca = longest_cap(T)
        print(f"k={k} l={l} |T|={len(T)} (C={comb(k+l-4,k-2)}) cup={cu}(want {k-1}) cap={ca}(want {l-1})", flush=True)
        if not (cu == k - 1 and ca == l - 1):
            bad.append((k, l, len(T), cu, ca))
print(f"checked {count} blocks, violations:", bad if bad else "NONE")
