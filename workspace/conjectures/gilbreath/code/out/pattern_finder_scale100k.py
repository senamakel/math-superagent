#!/usr/bin/env python3
"""Extend the two legs of the linear supply bound to n=100000.
Leg (b) [w density] computed densely to 1e5.  Leg (a) [nu2>=w/2] checked at
the 28 sampled nu2 points from nu2_incremental_1e5.txt (up to n=100000).
"""
from lib.gilbreath import primes_up_to
NMAX=100000
SIEVE=1_500_000
P=primes_up_to(SIEVE)
if len(P)<NMAX+2: raise SystemExit("not enough primes %d" % len(P))
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,b in enumerate(hbits): pref[i+1]=pref[i]+b
def w(n): return pref[n]-pref[2]

print("=== leg (b): w(n) density to 1e5 ===")
for tail in (2,17,31,100,1000,10000,40000,100000):
    mn=(1e9,0)
    for n in range(tail,NMAX+1):
        r=w(n)/n
        if r<mn[0]: mn=(r,n)
    print("tail=%d: min w(n)/n=%.4f at n=%d ; w(NMAX)/NMAX=%.4f" % (tail,mn[0],mn[1],w(NMAX)/NMAX))

print("=== leg (a): nu2>=w/2 at the 28 sampled points ===")
import re
samples=[]
with open("code/out/nu2_incremental_1e5.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==7 and p[0].isdigit():
            samples.append((int(p[0]), int(p[1])))
viol=[]
for n,nu in samples:
    if n>=2 and nu < 0.5*w(n)-1e-9:
        viol.append((n,nu,w(n)))
print("sampled points:", [s[0] for s in samples])
print("violations nu2<w/2 at samples: %d %s" % (len(viol), viol))
# also check nu2>=0.4*w etc at samples and nu2/n
for n,nu in samples:
    print("  n=%6d nu2=%6d w=%6d nu2/w=%.3f nu2/n=%.4f" % (n,nu,w(n),nu/w(n),nu/n))
