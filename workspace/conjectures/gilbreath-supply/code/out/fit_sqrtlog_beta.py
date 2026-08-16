#!/usr/bin/env python3
"""Fit the structural model w*(n) = c * n^(1/2) * (log2 n)^beta against the
extended exact table (n = 2^4 .. 2^20), and compare to pure power n^E.
Structural reasoning: mean/n = 1/2 - (1/2n) sum_p cnt_p (1-2alpha)^{2^p},
a binomial-popcount CDF; only cells with 2^p ~ 1/(2alpha) stay active, and
the popcount distribution is concentrated at k/2 = (log2 n)/2, forcing
alpha ~ n^{-1/2} * (log n)^beta.  Test: does beta give a flat column?
"""
from math import log2, sqrt

data = [
    (16, 3), (32, 5), (64, 7), (128, 11), (256, 16), (512, 24),
    (1024, 35), (2048, 52), (4096, 77), (8192, 112), (16384, 164),
    (32768, 239), (65536, 349), (131072, 507), (262144, 738),
    (524288, 1072), (1048576, 1557),
]

def flatness(beta, lo=256):
    cols = []
    for n, w in data:
        if n < lo:
            continue
        cols.append(w / (sqrt(n) * (log2(n) ** beta)))
    rng = max(cols) - min(cols)
    spread = rng / min(cols)
    # trend with log2 n
    xs = [log2(n) for n, w in data if n >= lo]
    mx, my = sum(xs)/len(xs), sum(cols)/len(cols)
    trend = sum((x-mx)*(c-my) for x,c in zip(xs,cols)) / sum((x-mx)**2 for x in xs)
    return spread, trend, min(cols), max(cols)

print("Flatness of w*/(c·sqrt(n)·(log2 n)^beta) over extended table:")
for beta in [0.0, 0.25, 0.4, 0.5, 0.6, 0.8, 1.0]:
    s, t, mn, mx = flatness(beta)
    print("  beta=%4.2f  spread=%6.3f  trend(dcol/dlog2n)=%+.4f  range=[%.3f,%.3f]"
          % (beta, s, t, mn, mx))

# grid-search best beta (minimize spread)
best = None
for i in range(0, 201):
    b = i / 100.0
    s, t, mn, mx = flatness(b)
    if best is None or s < best[0]:
        best = (s, b, t)
print("\nBest beta by min-spread: %.2f (spread %.4f, trend %+.4f)" % (best[1], best[0], best[2]))

# Also: pure-power exponent via OLS over full tail
import statistics
def ols(points):
    xs = [log2(float(n)) for n,_ in points]
    ys = [log2(float(w)) for _,w in points]
    k = len(xs)
    mx, my = sum(xs)/k, sum(ys)/k
    sxx = sum((x-mx)**2 for x in xs)
    sxy = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    return sxy/sxx
for lo in [256, 1024, 65536]:
    pts = [(n,w) for n,w in data if n>=lo]
    print("pure-power OLS n>=%7d: E=%.4f" % (lo, ols(pts)))
