#!/usr/bin/env python3
"""Extend the whole-set cup/cap of es_construct to larger n, exact oracle."""
from lib.es_construct import es_set
from lib.es_geom import longest_cup, longest_cap
import time

for n in range(4, 14):
    t0 = time.time()
    S = es_set(n)
    cu = longest_cup(S)
    ca = longest_cap(S)
    dt = time.time() - t0
    print(f"n={n}: |S|={len(S)} whole-cup={cu} (n-1={n-1} match={cu==n-1}) "
          f"whole-cap={ca} (==2? {ca==2})  t={dt:.1f}s")
