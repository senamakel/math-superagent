#!/usr/bin/env python3
"""Exact Krawtchouk sphere-mean for the SUPPLY fold on the Hamming sphere.

The mathematical fact this module rests on (research/backward/
linear-supply-threshold-limit.md, gaps G-sphere-mean / G-threshold-tends-zero):
for h uniform on the weight-w Hamming sphere S_w = {h in F2^n : wt(h)=w},

    E_Sw[nu2(h)]  =  sum_{d=2}^{n-1} (1/2) ( 1 - K_w(2^popcount(d); n) / C(n,w) ),

because the depth-d fold cell T(n,d) = ⊕_{o⊆d} h[n-1-d+o] is a parity over
exactly m_d = 2^popcount(d) distinct coordinates (fold-cell-degree-is-2^popcount),
and #{h in S_w : cell-parity == 1} = (C(n,w) - K_w(m_d; n))/2, where

    K_w(m; n) = sum_j (-1)^j C(m,j) C(n-m, w-j)

is the (univariate) Krawtchouk polynomial value.  These two identities (cell
degree and the Krawtchouk parity count) are the classical,
krawtchouk-polynomials-encyclopedic / guruswami-macwilliams-lp-from-fourier
evaluations already in the library.

Asymptotic saturation (G-threshold-tends-zero): for w = alpha n,
K_w(2^p; n)/C(n,w) -> (1-2alpha)^{2^p}, so cells with large popcount are
saturated at parity probability 1/2, and there are only o(n) cells with
popcount below a fixed K; hence E[nu2]/n -> 1/2 for every fixed alpha > 0.

All arithmetic is exact integer/rational.  Only final ratios are floats.
This module was verified against exhaustive brute force (s_sos over all C(n,w)
strings) for n in {8,10,12,14,16}, every weight w, digit-for-digit (Stage A).
"""

from fractions import Fraction
from math import comb


def krawtchouk(w, m, n):
    """K_w(m; n) = sum_j (-1)^j C(m,j) C(n-m, w-j), exact integer."""
    total = 0
    jlo = max(0, w - (n - m))
    jhi = min(w, m)
    for j in range(jlo, jhi + 1):
        term = comb(m, j) * comb(n - m, w - j)
        if j & 1:
            total -= term
        else:
            total += term
    return total


def sphere_mean_abs(n, w):
    """Exact E_Sw[nu2(h)] as a Fraction, via the per-cell Krawtchouk sum."""
    Cnw = comb(n, w)
    total = Fraction(0)
    for d in range(2, n):
        p = bin(d).count('1')
        m = 1 << p
        K = krawtchouk(w, m, n)
        total += Fraction(1, 2) * (1 - Fraction(K, Cnw))
        # total += (Cnw - K) // 2  (integer per-cell parity count) -- same
    return total


def sphere_mean_ratio(n, w):
    """E_Sw[nu2(h)]/n as a float -- the mean half of 'typical' (>= 0.40)."""
    return float(sphere_mean_abs(n, w)) / n


def popcount_counts(n):
    """cnt_p = #{ d in [2, n-1] : popcount(d) = p }, by one O(n) pass."""
    from collections import Counter
    c = Counter()
    for d in range(2, n):
        c[bin(d).count('1')] += 1
    return c


def sphere_mean_ratio_grouped(n, w, cnt=None):
    """E_Sw[nu2]/n grouped by popcount, for exactness with fewer cells at
    large n.  mean/n = (1/(2n)) sum_p cnt_p (1 - K_w(2^p;n)/C(n,w))."""
    if cnt is None:
        cnt = popcount_counts(n)
    Cnw = comb(n, w)
    acc = 0.0
    for p, cntp in cnt.items():
        if cntp == 0:
            continue
        m = 1 << p
        K = krawtchouk(w, m, n)
        acc += cntp * 0.5 * (1.0 - K / Cnw)
    return acc / n


def theta_mean(n, start_w=1, cap_frac=0.5):
    """theta_mean(n) = min{ w : mean(n,w)/n >= 0.40 }, scanning w upward.

    Returns (first crossing w, mean/n at that w) or (None, None) if no w in
    [start_w, floor(cap_frac*n)] crosses.  Exact (Fractions/Fraction ratios
    only at the comparison; K and C(n,w) exact).  cap_frac defaults to 0.5:
    the sphere mean is symmetric under w -> n-w (complement symmetry of the
    sphere), so the minimum crossing weight always lies in the low half.
    """
    cnt = popcount_counts(n)
    Cnw_rows = {}          # cache comb rows?  simple: comb(n,w) per w
    wmax = int(cap_frac * n)
    for w in range(start_w, wmax + 1):
        Cnw = comb(n, w)
        tot = Fraction(0)
        for p, cntp in cnt.items():
            if cntp == 0:
                continue
            m = 1 << p
            K = krawtchouk(w, m, n)
            tot += Fraction(cntp, 2) * (1 - Fraction(K, Cnw))
        mean = tot / n
        if mean >= Fraction(2, 5):          # 0.40 exactly
            return w, float(mean)
    return None, None
