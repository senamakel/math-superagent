#!/usr/bin/env python3
"""Precise significance of the ballot survival, and confirmation of the
transfer composition.

Question: the prime switch-ballot e(n)>=0 survived to 1.33M gaps. My controls
show that neither iid-with-marginal-density nor lag-1 Markov (matching the
fitted transition matrix) force survival: both dip below 0 in ~60% of trials
and typical first-dip index is tiny.  Here we measure *how* long the Markov
control survives when it does survive, and how often it dips late (after
n=100), to bound what structure the primes' never-dip excludes.
"""
import math, random
from collections import Counter

# fitted transition matrix from the 20M run (near-stationary primes)
# P[prev][nxt]
P = {0:{0:0.4172,1:0.5828}, 1:{0:0.4546,1:0.5454}}
pi1 = P[0][1]/(P[1][0]+P[0][1])
print("stationary P(1)=", round(pi1,5), " drift 2pi1-1=", round(2*pi1-1,5))

N = int(input_default if False else 2000000)  # ballot length in the control
N = 2_000_000
random.seed(11)
surv=0
dip_before_100=0
dip_before_1000=0
dip_after_100k=0
total_dip=0
first_dips=[]
for trial in range(3000):
    state = 1 if random.random()<pi1 else 0
    w=state
    dipped=False
    dip_at=None
    for k in range(3,N+1):
        r=random.random()
        state = 0 if r<P[state][0] else 1
        w+=state
        if 2*w-(k-2)<0 and not dipped:
            dipped=True; dip_at=k; break
    if not dipped:
        surv+=1
    else:
        total_dip+=1
        first_dips.append(dip_at)
        if dip_at<100: dip_before_100+=1
        if dip_at<1000: dip_before_1000+=1
        if dip_at>100_000: dip_after_100k+=1
print(f"Markov control N=2e6: survived {surv}/3000 ({surv/3000:.4f})")
print(f"  of the dips: before n=100: {dip_before_100}  before n=1000: {dip_before_1000}  after n=100k: {dip_after_100k}")
print(f"  first dip index: min={min(first_dips) if first_dips else None} median={sorted(first_dips)[len(first_dips)//2] if first_dips else None}")
print(f"  P(dip before n=100 | dip) = {dip_before_100/max(1,total_dip):.4f}")

# The PRIMES at same scale never dip. Chance a single Markov sample survives
# N steps to 2e6 is ~ surv/3000 ≈ measured. One observed survival is then not
# surprising; the real content is that the SAME Markov model that matches
# lag-1 structure still dips ~60% of the time, so lag-1 alone is not the
# ballot's cause.
