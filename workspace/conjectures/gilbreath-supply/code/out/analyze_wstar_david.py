#!/usr/bin/env python3
"""Decision columns for the w* exponent:
(a) per-doubling exponent log2(w*(2n)/w*(n));
(b) w*/sqrt(n) — rising => NOT pure 1/2; flattening => 1/2;
(c) w*/(sqrt(n) log2(n)) — for the sqrt·log model.
Extended w* values computed exactly (grouped Krawtchouk) out to n=262144.
"""
from math import log2, sqrt

# (n, w*) exact, from the exact-mean threshold (powers of two)
data = [
    (16, 3), (32, 5), (64, 7), (128, 11), (256, 16), (512, 24),
    (1024, 35), (2048, 52), (4096, 77), (8192, 112), (16384, 164),
    (32768, 239), (65536, 349), (131072, 507), (262144, 738),
]

print("per-doubling exponent  log2(w*(2n)/w*(n)):")
prev = None
for n, w in data:
    if prev is not None:
        n0, w0 = prev
        if w0 > 0:
            print("  %7d -> %7d : w %4d -> %4d   exp=%.4f"
                  % (n0, n, w0, w, log2(w / w0)))
    prev = (n, w)

print("\nw*/sqrt(n)   (flat => pure 1/2, rising => not 1/2):")
for n, w in data:
    if n >= 128:
        print("  n=%7d  w*/sqrt=%.4f" % (n, w / sqrt(n)))

print("\nw*/(sqrt(n)*log2(n))  (flat => sqrt·log):")
for n, w in data:
    if n >= 128:
        print("  n=%7d  col=%.4f" % (n, w / (sqrt(n) * log2(n))))

# OLS: log2 w = a + E log2 n over tail
import statistics
def ols(points):
    xs = [log2(float(n)) for n, _ in points]
    ys = [log2(float(w)) for _, w in points]
    k = len(xs)
    mx, my = sum(xs)/k, sum(ys)/k
    sxx = sum((x-mx)**2 for x in xs)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    E = sxy/sxx
    a = my - E*mx
    res = [y - (a + E*x) for x, y in zip(xs, ys)]
    se = (sum(r*r for r in res)/(sxx*(k-2)))**0.5 if k>2 else float('nan')
    return E, se

for lo in [256, 1024, 4096, 16384]:
    pts = [(n,w) for n,w in data if n>=lo]
    E, se = ols(pts)
    print("OLS n>=%6d : E=%.4f +/- %.4f" % (lo, E, se))
