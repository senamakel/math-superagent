#!/usr/bin/env python3
"""Get whole cap at n=12,13 only (cheap-ish)."""
import time
from lib.es_construct import es_set
from lib.es_geom import longest_cap

for n in (12, 13):
    t0 = time.time()
    S = es_set(n)
    t1 = time.time()
    ca = longest_cap(S)
    t2 = time.time()
    print(f"n={n}: |S|={len(S)} whole-cap={ca} (==2? {ca==2}) "
          f"set_t={t1-t0:.1f}s cap_t={t2-t1:.1f}s", flush=True)
