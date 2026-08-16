#!/usr/bin/env python3
"""Extend the threshold-weight exponent check to larger n.

mean_n(w) = (1/n) sum_{d=2}^{n-1} P_d(w), and P_d(w) depends on d only
through k = 2^popcount(d).  Group depths by popcount so each mean is a sum
over <= log2(n) distinct k values, making the scan over w cheap.

Reports: first weight w with mean_n(w) >= 0.40, plus per-doubling
log2(w)/log2(n) slope, to see whether the ~0.565 exponent drifts.
"""
from math import comb
from fractions import Fraction
from collections import Counter


def parity_prob_coeff(n, w, k):
    """P_d(w) = ( C(n,w) - c_w ) / ( 2 C(n,w) ), c_w=[z^w](1-z)^k(1+z)^{n-k}."""
    lo = max(0, w - (n - k))
    hi = min(k, w)
    c = 0
    for j in range(lo, hi + 1):
        c += (-1) ** j * comb(k, j) * comb(n - k, w - j)
    C = comb(n, w)
    from fractions import Fraction
    return float(Fraction(C - c, 2 * C))


def popcount_distribution(n):
    c = Counter()
    for d in range(2, n):
        c[d.bit_count()] += 1
    return c


def mean_over_weight(n, w, pc_dist):
    # mean of nu2/n over all weight-w strings = (1/n) sum_d P_d(w)
    # group by popcount: k = 2^pc
    total = 0.0
    for pc, cnt in pc_dist.items():
        k = 1 << pc
        total += cnt * parity_prob_coeff(n, w, k)
    return total / n


# validate grouping formula against the schema's exhaustive numbers
from lib.supply_fold import s_sos
from itertools import combinations
from fractions import Fraction as Fr

def brute_mean(n, w):
    tot = Fr(0); cnt = 0
    for ones in combinations(range(n), w):
        h = [0]*n
        for j in ones: h[j]=1
        _, c1 = s_sos(n, h)
        tot += c1; cnt += 1
    return tot/cnt/n

import sys
for (n,w) in [(6,1),(6,2),(8,1),(8,3),(10,2)]:
    m = mean_over_weight(n, w, popcount_distribution(n))
    b = float(brute_mean(n,w))
    print(f"n={n} w={w} group={m:.4f} brute={b:.4f} {'OK' if abs(m-b)<1e-9 else 'MISMATCH'}")

print("\nE X T E N D E D   T A B L E")
print(f"{'n':>7} {'first w':>8} {'w/n':>9} {'per-doubling slope':>20}")
prev = None
ns = [8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
ws = []
for n in ns:
    pc = popcount_distribution(n)
    first = None
    for w in range(1, n):
        if mean_over_weight(n, w, pc) >= 0.40:
            first = w
            break
    ws.append(first)
    import math
    slope = ""
    if prev is not None and abs(n/prev[0]-2) < 1e-9:
        sl = (math.log2(first)-math.log2(prev[1]))/math.log2(n/prev[0])
        slope = f"{sl:.4f}"
    print(f"{n:>7} {first:>8} {first/n:>9.4f} {slope:>20}")
    prev = (n, first)

print("\nws =", ws)
