#!/usr/bin/env python3
import sys
sys.path.insert(0, "/workspace/code")
from count_signatures import count_signatures
from collections import Counter

for L in (10**6, 10**10, 10**14, 10**18):
    c, _ = count_signatures(L)
    print(f"LIMIT {L}: {c} feasible exponent signatures", flush=True)

c, sl = count_signatures(10**18)
dist = Counter(len(s) for s in sl)
print("signature count by number of distinct primes r (at 1e18):")
for r in sorted(dist):
    print(f"  r={r}: {dist[r]}", flush=True)
print("total:", c)
print("max r:", max(len(s) for s in sl))