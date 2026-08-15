#!/usr/bin/env python3
"""Is w(n) a positive-density sequence? w(n) = Hamming weight of mod-4 switch
bits hbits[2..n-1] (gap==2 mod4).  If w(n) stays above c*n for some c>0, then
the transfer nu2 >= w/2 gives nu2 >= (c/2)*n -- a genuine linear supply bound
for Route B (only needs nu2 > n^0.525, so any positive density suffices).

Report exact over the range:  min w(n)/n, the limiting density (last value),
the largest deficit dip of w relative to a linear line, and what constant c
holds as a lower bound on w(n)/n over n >= some threshold.
"""
from lib.gilbreath import primes_up_to

NMAX = 30000
P = primes_up_to(1_000_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,b in enumerate(hbits): pref[i+1]=pref[i]+b

def w(n): return pref[n]-pref[2]

# min ratio over various tails
for tail in (2, 17, 100, 1000, 4000, 10000):
    mn=(1e9,0)
    for n in range(tail, NMAX+1):
        r=w(n)/n
        if r<mn[0]: mn=(r,n)
    print("tail=%d: min w(n)/n = %.4f at n=%d" % (tail, mn[0], mn[1]))
print("w(NMAX)/NMAX = %.4f" % (w(NMAX)/NMAX))
# last-1000 average density
last = (w(NMAX)-w(NMAX-1000))/1000.0
print("marginal switch density in last 1000 = %.4f" % last)

# Does w(n) >= c*n for a positive c over n>=large? find largest such c (over n>=a tail)
# consecutive deficit of w - c*n for c=0.4,0.5,0.55
for c in (0.3,0.4,0.45,0.5):
    viol=[n for n in range(1000,NMAX+1) if w(n)<c*n]
    print("w(n)<%.2f*n over n>=1000: count=%d first=%s last=%s" % (c,len(viol),viol[:5],viol[-3:] if viol else []))
