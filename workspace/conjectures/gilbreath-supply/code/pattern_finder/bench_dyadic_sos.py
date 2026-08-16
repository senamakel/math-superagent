#!/usr/bin/env python3
"""Benchmark: how long does the SOS fold (lib.supply_fold.s_sos) take at
dyadic n = 2^k, and does it reproduce the canonical JSON values at k <= 15?

The whole extension plan rests on this cost: one s_sos call per dyadic n,
O(n log n) exact integer arithmetic. Benchmark at k = 18, 20, 22 (each is 4x
the previous) against a fixed random h so the real prime h cost is comparable.
"""
import json
import sys
import time

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

d = json.load(open("/workspace/code/out/nu2_primes_xor_40000.json"))
assert d[53] == 18 and d[64] == 27 and d[4000] == 1975 and d[40000] == 20081
print("JSON guards pass; JSON d[i] = nu2(i)")

# reproduce dyadic values from JSON through s_sos with a random h of same
# length is not possible (h is the prime string) -- so instead verify s_sos
# against the JSON at a few non-dyadic n using the real prime h.
from lib.primes import h_string
h40000 = h_string(40002)
for n in (53, 64, 4000, 40000):
    _, ones = s_sos(n, h40000[:n])
    print(f"  s_sos nu2({n}) = {ones}  (json {d[n]})  match={ones == d[n]}")
    assert ones == d[n]

# benchmark on a fixed random ±1 pattern (same cost as h, h is bits)
import random
rng = random.Random(1234)
for k in (18, 20, 22):
    n = 1 << k
    h = [rng.randrange(2) for _ in range(n + 1)]
    t0 = time.time()
    S, ones = s_sos(n, h)
    dt = time.time() - t0
    print(f"k={k} n=2^{k}={n}: s_sos took {dt:.2f}s, S={S}, ones={ones}")