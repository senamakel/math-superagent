#!/usr/bin/env python3
"""Time es_set + longest_cup/cap separately at n=11,12."""
import time
from lib.es_construct import es_set
from lib.es_geom import longest_cup, longest_cap

for n in (11, 12):
    t0 = time.time()
    S = es_set(n)
    t1 = time.time()
    print(f"n={n}: |S|={len(S)} es_set t={t1-t0:.1f}s", flush=True)
    t0 = time.time()
    cu = longest_cup(S)
    t1 = time.time()
    ca = longest_cap(S)
    t2 = time.time()
    print(f"   cup={cu} (n-1={n-1}) cap={ca} (==2? {ca==2}) "
          f"cup_t={t1-t0:.1f}s cap_t={t2-t1:.1f}s", flush=True)
