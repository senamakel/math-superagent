#!/usr/bin/env python3
"""Measure the DP's state growth to confirm N=10000 feasibility, and check
D(20) / D(100)-last-nine against the statement's own examples (out-of-sample
for this run, which only reached N=14).

Use modular arithmetic (mod 10^9) for speed when checking last-nine-digits.
"""
from fractions import Fraction
import time

MOD = 10**9

def D_from_dseq(N, mod=None):
    dp = {(1, 1): (1 if mod is None else 1)}
    total = 0
    maxstates = 0
    for _ in range(N):
        ndp = {}
        for (last, s), wt in dp.items():
            for nxt in range(max(1, 3*last-7), 3*last):
                a = 3*last - nxt
                ns = s + nxt
                if ns > N: continue
                w = wt * (3 if a in (1,2,3) else 4 if a==4 else 1 if a==5 or a==7 else 10 if a==6 else 0)
                key = (nxt, ns)
                if mod is None:
                    ndp[key] = ndp.get(key, 0) + w
                else:
                    ndp[key] = (ndp.get(key, 0) + w) % mod
        dp = ndp
        maxstates = max(maxstates, len(dp))
        total += dp.get((1, N), 0)
        if mod is not None: total %= mod
    return total, maxstates

# exact reproduction through 14 (already done), then scaling probes
for N in [20, 30, 40, 50, 60, 80, 100, 200, 400]:
    t0 = time.time()
    val, ms = D_from_dseq(N, mod=MOD)
    dt = time.time()-t0
    print(f"N={N:>4}: D mod 1e9 = {val:>9}   maxstates={ms:>7}   {dt:.3f}s")

print("\nStatement checks:")
val20, _ = D_from_dseq(20)
print("D(20) exact =", val20, " expected 9204559704 ->", val20 == 9204559704)
val100, _ = D_from_dseq(100)
print("D(100) last 9 =", val100 % MOD, " expected 780166455 ->", val100 % MOD == 780166455)
