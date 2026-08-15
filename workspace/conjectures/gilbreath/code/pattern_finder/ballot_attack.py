#!/usr/bin/env python3
"""Pattern-finder: the mod-4 switch-majority ballot e(n)>=0, verified fresh,
and attacked.

h[j] = 1 iff prime gap g_j = p_{j+1}-p_j is ≡ 2 (mod 4)  (a 'switch':
p_{j+1} not≡ p_j mod 4).  w(n) = sum_{j} h[j],  e(n) = 2*w(n) - (n-2).

We recompute from scratch over a fresh sieve and record:
  - the running minimum of e(n) (the ballot asks it stay >= 0),
  - the number of n where e(n) == 0 ('ties'),
  - the lag-1 autocorrelation of h (the anti-clustering fact),
  - w(n)/n density (Mazur's question direction: majority of gaps ≡2 mod 4).
Attacks: is the ballot merely a concentration artifact? We also test the same
ballot statistic on synthetic 2-then-odds sequences with *independent uniform
switch bits* to see whether e(n)>=0 is a special prime fact or a generic walk
fact (it should NOT be generic: an unbiased ±1 walk hits negative values).
"""
import sys, math

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
LIM = NMAX + 2_000_000   # slack to get > NMAX gaps

# sieve
sieve = bytearray(b'\x01') * (LIM + 1)
sieve[0:2] = b'\x00\x00'
for i in range(2, int(math.isqrt(LIM)) + 1):
    if sieve[i]:
        sieve[i*i::i] = b'\x00' * (((LIM - i*i) // i) + 1)
primes = [i for i in range(2, LIM + 1) if sieve[i]]

h = []
gaps = []
for i in range(len(primes) - 1):
    g = primes[i+1] - primes[i]
    gaps.append(g)
    h.append(1 if (g % 4) == 2 else 0)

n_gaps = len(h)
# prefix sums
pref = [0]*(n_gaps+1)
for i,b in enumerate(h): pref[i+1] = pref[i] + b

# ballot: min over prefixes of 2*w(n)-(n-2)
emin = None; emin_at = []
for n in range(2, n_gaps+1):
    e = 2*pref[n] - (n-2)
    if emin is None or e < emin:
        emin = e; emin_at = [n]
    elif e == emin:
        emin_at.append(n)
    elif e == 0:
        pass
ties = [n for n in range(2, n_gaps+1) if 2*pref[n]-(n-2) == 0]

print(f"NMAX(gaps)={n_gaps}  sieve_limit={LIM}")
print(f"density w/n = {pref[n_gaps]/n_gaps:.5f}  (#switches {pref[n_gaps]})")
print(f"ballot e(n)>=0 over all prefixes n=2..{n_gaps}: min e = {emin} at n={emin_at[:10]}")
print(f"#prefixes with e==0 (ties): {len(ties)}  first few: {ties[:12]}")
print(f"final e = {2*pref[n_gaps]-(n_gaps-2)}")

# lag-1 autocorrelation of centered h
m = pref[n_gaps]/n_gaps
r1 = sum((h[i]-m)*(h[i+1]-m) for i in range(n_gaps-1)) / (n_gaps-1)
var = sum((x-m)**2 for x in h)/n_gaps
print(f"lag-1 autocorr r1 = {r1/var:.5f}   (E[h]={m:.5f})")

# joint
import itertools
from collections import Counter
c = Counter()
for i in range(n_gaps-1): c[(h[i],h[i+1])] += 1
print("joint (h_i,h_{i+1}):", dict(c), f"  P(1,1)={c[(1,1)]/(n_gaps-1):.5f} vs E^2={m*m:.5f}")

# ---- control: independent uniform switch bits (50/50), same length ----
# an unbiased ±1 walk WILL dip below 0; count how often
import random
random.seed(1)
under = 0
for trial in range(200):
    w = 0
    dipped = False
    for n in range(2, n_gaps+1):
        bit = 1 if random.random()<0.5 else 0
        w += bit
        e = 2*w-(n-2)
        if e < 0: dipped = True; break
    if dipped: under += 1
print(f"control (iid fair switch bits): {under}/200 trials dip below 0")

# ---- control: biased toward switch-majority p=0.56, to mimic density ----
under2 = 0
already_needed = pref[n_gaps]  # keep same total switch count
# use a biased coin p=0.56
random.seed(2)
p=0.56
for trial in range(200):
    w=0; dipped=False
    for n in range(2, n_gaps+1):
        bit = 1 if random.random()<p else 0
        w+=bit
        if 2*w-(n-2)<0: dipped=True; break
    if dipped: under2+=1
print(f"control (iid biased p=0.56): {under2}/200 trials dip below 0 at some prefix")
