#!/usr/bin/env python3
"""Whole-set cup/cap of es_construct (exact DP), n=4..10."""
from lib.es_construct import es_set
from lib.es_geom import longest_cup, longest_cap

for n in range(4, 11):
    S = es_set(n)
    cu = longest_cup(S)
    ca = longest_cap(S)
    print(f"n={n}: |S|={len(S)} whole-cup={cu} whole-cap={ca}")
