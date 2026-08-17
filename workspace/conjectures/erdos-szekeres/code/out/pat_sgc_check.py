#!/usr/bin/env python3
"""Cross-check the split-gon spectrum's cup/cap numbers against the validated
es_geom oracle, and against chains_by_rightmost, to catch a cap/cup-label bug."""
import time
from collections import Counter
from fractions import Fraction
from lib.es_construct import es_set
from lib.es_geom import longest_cup, longest_cap
from lib.chainenum import chains_by_rightmost, chain_totals

for n in (5, 6, 7):
    pts = es_set(n)
    g_cup = longest_cup(pts)
    g_cap = longest_cap(pts)
    cups, caps = chains_by_rightmost(pts, 9)
    ct = chain_totals(cups, caps)
    print(f"n={n}: es_geom longest_cup={g_cup} longest_cap={g_cap}")
    print(f"     chains: cups by size={dict(ct[0])}  caps by size={dict(ct[1])}")
    cmax = max((len(fs) for lst in caps.values() for fs in lst), default=0)
    umax = max((len(fs) for lst in cups.values() for fs in lst), default=0)
    print(f"     chain max cap size={cmax}  max cup size={umax}")
print("EXIT: 0")
