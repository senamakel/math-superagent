#!/usr/bin/env python3
"""Push w*(n) to larger powers of two to resolve the drift direction:
does the per-doubling exponent keep falling toward 1/2, or settle?
Continued grouped-Krawtchouk exact computation.  Start scan where the
previous run left off (w* grows ~n^0.54, so w* at 2^19 ~ 1100).
"""
from fractions import Fraction
from math import comb, log2
import sys, time

def popcount_counts(n):
    c = {}
    for d in range(2, n):
        p = bin(d).count('1')
        c[p] = c.get(p, 0) + 1
    return c

def mean_frac(n, w, cnt):
    Cnw = comb(n, w)
    tot = Fraction(0)
    for p, cntp in cnt.items():
        if cntp == 0:
            continue
        m = 1 << p
        K = 0
        jlo = max(0, w - (n - m))
        jhi = min(w, m)
        for j in range(jlo, jhi + 1):
            term = comb(m, j) * comb(n - m, w - j)
            K += -term if (j & 1) else term
        tot += Fraction(cntp, 2) * (1 - Fraction(K, Cnw))
    return tot / n

prev_w = 738   # from n=262144
for k in range(19, 22):
    n = 1 << k
    t0 = time.time()
    cnt = popcount_counts(n)
    lo = max(1, int(prev_w * 1.4))   # w* increases sublinearly
    w = None
    for ww in range(max(1, lo - 20), n // 2):
        if mean_frac(n, ww, cnt) >= Fraction(2, 5):
            # scan downward to be safe about exact crossing boundary
            w = ww
            break
    # confirm by stepping back
    while w and w > 1 and mean_frac(n, w - 1, cnt) >= Fraction(2, 5):
        w -= 1
    me = float(mean_frac(n, w, cnt)) if w else None
    prev_w = w
    print("k=%2d  n=%8d  w*=%6d  theta=%.6f  mean=%.4f  [%.1fs]"
          % (k, n, w, w / n, me, time.time() - t0), flush=True)
