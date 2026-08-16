#!/usr/bin/env python3
"""Verify the structural mechanism prediction directly.
mean/n = 1/2 - (1/2n) sum_p cnt_p (1 - 2*alpha)^{2^p}  (alpha = w/n).
For a cell of popcount p to contribute non-negligibly (parity far from 1/2),
we need (1-2*alpha)^{2^p} NOT ~0, i.e. 2^p of order 1/(2*alpha) = n/(2w).
The popcounts p are distributed over d in [2,n-1] with mean (log2 n - 2)/2-ish
(binomial).  So the active cells are those at the LOW tail of the popcount
distribution, of width ~ sqrt(log2 n).  This forces w such that
   2^(p_mean - c sqrt(log2 n)) ~ n/(2w)
=>  n/(2^p_mean) ~ w * 2^{c sqrt(log2 n)}  and 2^p_mean ~ sqrt(n)/(log n)
so w ~ sqrt(n) (log n)^(1/2)-ish.  Check numerically: compute mean_n(w) at the
sqrt·log scaling and see it cross 0.40 at w ~ c sqrt(n)(log n)^0.5.
"""
from fractions import Fraction
from math import comb, log2
import math

def popcount_counts(n):
    c = {}
    for d in range(2, n):
        p = bin(d).count('1')
        c[p] = c.get(p, 0) + 1
    return c

def mean_ratio(n, w):
    cnt = popcount_counts(n)
    Cnw = comb(n, w)
    tot = Fraction(0)
    for p, cntp in cnt.items():
        if cntp == 0: continue
        m = 1 << p
        K = 0
        jlo = max(0, w - (n - m)); jhi = min(w, m)
        for j in range(jlo, jhi+1):
            t = comb(m,j)*comb(n-m,w-j)
            K += -t if (j&1) else t
        tot += Fraction(cntp,2)*(1-Fraction(K,Cnw))
    return float(tot)/n

# At various n, find w* / (sqrt(n) (log2 n)^0.5) -> should be ~constant.
print("w*/(sqrt(n) (log2 n)^0.5) :")
prev_w = None
for k in range(12, 19):
    n = 1 << k
    w = None
    # scan
    lo = 1
    if prev_w: lo = max(1, int(prev_w*1.3)-30)
    for ww in range(max(1,lo), n//2):
        if mean_ratio(n, ww) >= 0.40:
            w = ww; break
    prev_w = w
    col = w / (math.sqrt(n) * (log2(n))**0.5)
    print("  n=%-8d w*=%d  col=%.4f" % (n, w, col))
