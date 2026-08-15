#!/usr/bin/env python3
"""Does the ballot e(n)>=0 survive if we only keep the *nearest-neighbour*
structure of the prime switch bit, i.e. a Markov chain with the SAME
one-step transition probabilities as the primes? If yes, the ballot is carried
by the two-point (lag-1 anti-clustering + drift) structure, not by longer-range
correlations. If it fails, we need longer-range structure.

We fit the empirical transition matrix from the real primes and iterate a
Markov chain, then count how often the ballot dips below 0.

Also: an *independent* exact recompute of the ballot over a fresh sieve to a
larger scale than 2e6, recording min e.
"""
import math, sys
from collections import Counter

# ---------- fresh sieve, larger ----------
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20_000_000
LIM  = NMAX + 1_000_000
sieve = bytearray(b'\x01')*(LIM+1)
sieve[0:2]=b'\x00\x00'
for i in range(2, int(math.isqrt(LIM))+1):
    if sieve[i]:
        sieve[i*i::i]=b'\x00'*(((LIM-i*i)//i)+1)
primes=[i for i in range(2,LIM+1) if sieve[i]]
h=[]
for i in range(len(primes)-1):
    g=primes[i+1]-primes[i]
    h.append(1 if g%4==2 else 0)
n=len(h)
pref=[0]*(n+1)
for i,b in enumerate(h): pref[i+1]=pref[i]+b
emin=None; emin_at=[]
for k in range(2,n+1):
    e=2*pref[k]-(k-2)
    if emin is None or e<emin:
        emin=e; emin_at=[k]
    elif e==emin: emin_at.append(k)
print(f"PRIMES fresh: n_gaps={n}  density={pref[n]/n:.5f}  ballot min e={emin} at {emin_at[:8]}  final e={2*pref[n]-(n-2)}")

# empirical transition matrix  P[prev][nxt]
tr=Counter()
for i in range(n-1): tr[(h[i],h[i+1])]+=1
counts={prev:{0:0,1:0} for prev in (0,1)}
for (a,b),c in tr.items(): counts[a][b]+=c
P={pr:{0:counts[pr][0]/(counts[pr][0]+counts[pr][1]),
        1:counts[pr][1]/(counts[pr][0]+counts[pr][1])} for pr in (0,1)}
print("transition matrix (empirical):", {pr:{k:round(v,4) for k,v in P[pr].items()} for pr in (0,1)})
stat0 = counts[0][0]+counts[0][1]; stat1=counts[1][0]+counts[1][1]
# stationary: solve pi*P=pi
pi1 = P[0][1]/(P[1][0]+P[0][1])
print(f"stationary P(1) = {pi1:.5f}  (stationary drift 2pi1-1={2*pi1-1:.5f})")

# ---------- Markov control with same transition matrix ----------
import random
random.seed(7)
dips=0
dip_at_first=[]
for trial in range(2000):
    state = 1 if random.random()<pi1 else 0
    w = state
    dipped=False
    min_e=None
    for k in range(3, n+1):
        r=random.random()
        state=0 if r<P[state][0] else 1
        w+=state
        e=2*w-(k-2)
        if min_e is None or e<min_e: min_e=e
        if e<0 and not dipped:
            dipped=True
            dip_at_first.append(k); break
    if dipped: dips+=1
print(f"MARKOV control (same transition matrix): {dips}/2000 trials dip below 0")
if dip_at_first:
    print("  first dip index (smallest):", min(dip_at_first))

# ---------- iid control with same marginal density ----------
random.seed(8)
p=pref[n]/n
dips2=0
for trial in range(2000):
    w=0;dipped=False
    for k in range(2,n+1):
        bit=1 if random.random()<p else 0
        w+=bit
        if 2*w-(k-2)<0: dipped=True; break
    if dipped: dips2+=1
print(f"IID control (marginal p={p:.5f}): {dips2}/2000 trials dip below 0")
