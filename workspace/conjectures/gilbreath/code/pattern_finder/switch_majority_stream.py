#!/usr/bin/env python3
"""Streaming mod-4 switch-majority check to N primes (sieve LIMIT).

e(n) = 2*w(n) - (n-2), where w(n) = # of gaps g_3..g_n that are 2 mod 4
(equivalently: # of consecutive-prime pairs switching residue class mod 4
among the first n-2 pairs starting from p_2 -> p_3).

The increment of e is +1 on a switch, -1 on a stay, so e is a +/-1 walk.
The conjecture: e(n) >= 0 for every n (the walk never dips below 0).

Streaming: no primes list, no hbits list, no prefix array.  Memory is just
the sieve bytearray.  Also records the first-dip location if any, the global
min of e, and the tail min over [N/2, N] and [N/4, N].
"""
import sys, time
from math import isqrt

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000_000
N = int(sys.argv[2]) if len(sys.argv) > 2 else 10_000_000

t0 = time.time()
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
print("sieve to %d built (%.1fs)" % (LIMIT, time.time() - t0))

# stream primes, tracking the mod-4 residue of the previous prime.
# n counts primes in the window: we need gaps g_3..g_N (n from 2 to N).
# w(n) accumulates over gaps g_3..g_n, i.e. pairs (p_{i}, p_{i+1}) for i=2..n-1
# (0-indexed hbits[i] = bit of gap g_{i+1} = p_{i+1}-p_i; hbits[2..n-1] covers
#  gaps g_3..g_n => pairs (p_2,p_3) .. (p_{n-1}, p_n)).
# So: prime counter idx (1-based prime index).  The pair (p_{idx}, p_{idx+1})
# contributes to w(n) for n = idx+1.

prev_res = None   # residue mod 4 of the previous prime
idx = 0           # 1-based index of the current prime
w = 0             # running switch count
e_min_global = 10**18
e_min_global_n = 0
first_dip = None
dips = 0
# tail minima
tail_half = None; tail_quarter = None
tail_half_min = 10**18; tail_quarter_min = 10**18
count = 0

for p in range(2, LIMIT + 1):
    if not sieve[p]:
        continue
    idx += 1
    res = p & 3
    if idx >= 2:
        # pair (p_{idx-1}, p_{idx}) finished: it is gap g_{idx}, hbits[idx-1]
        # this gap contributes to w(n) for all n >= idx+1, i.e. as soon as
        # the running n reaches idx+1.  We update w now and e for n=idx+1.
        switch = 0 if res == prev_res else 1
        w += switch
        n = idx + 1          # e(n) at this n
        e = 2 * w - (n - 2)
        if n >= 2 and n <= N:
            count += 1
            if e < e_min_global:
                e_min_global = e; e_min_global_n = n
            if e < 0:
                dips += 1
                if first_dip is None:
                    first_dip = n
            if n >= N // 2 and e < tail_half_min:
                tail_half_min = e
            if n >= N // 4 and e < tail_quarter_min:
                tail_quarter_min = e
    prev_res = res
    if idx >= N + 1:
        break

print("processed %d primes, window n up to %d" % (idx, min(N, idx - 1)))
print("e(n) >= 0 for all n in [2,%d]: %s (dips %d, first dip at %s)"
      % (N, "YES" if first_dip is None else "NO", dips, first_dip))
print("global min e = %d at n=%d" % (e_min_global, e_min_global_n))
print("min e over [%d,%d] = %d ; over [%d,%d] = %d"
      % (N // 2, N, tail_half_min, N // 4, N, tail_quarter_min))
print("time %.1fs" % (time.time() - t0))
