#!/usr/bin/env python3
"""Final consolidated flatness report for the corrected sqrt·log model,
including the largest exact w* values (n up to 2^20).
"""
from math import log2, sqrt

data = [
    (16,3),(32,5),(64,7),(128,11),(256,16),(512,24),(1024,35),(2048,52),
    (4096,77),(8192,112),(16384,164),(32768,239),(65536,349),(131072,507),
    (262144,738),(524288,1072),(1048576,1557),
]

def report(beta, lo=256):
    cols = [(n, w/(sqrt(n)*(log2(n)**beta))) for n,w in data if n>=lo]
    cs = [c for _,c in cols]
    spread = (max(cs)-min(cs))/min(cs)
    xs = [log2(n) for n,_ in cols]
    mx,my = sum(xs)/len(xs), sum(cs)/len(cs)
    trend = sum((x-mx)*(c-my) for x,c in zip(xs,cs))/sum((x-mx)**2 for x in xs)
    return spread, trend, min(cs), max(cs)

print("Residual flatness of w*/(sqrt(n)*(log2 n)^beta), extended n=2^8..2^20:")
for b in [0.0, 0.45, 0.5]:
    s,t,mn,mx = report(b)
    print("  beta=%.2f  spread=%.4f (%4.1f%%)  trend=%+.4f  range=[%.4f,%.4f]"
          % (b, s, 100*s, t, mn, mx))

print("\nExact w*/(sqrt(n)*(log2 n)^0.5) column (the clean candidate, beta=1/2):")
for n,w in data:
    if n>=256:
        print("  n=%-8d  col=%.4f" % (n, w/(sqrt(n)*(log2(n)**0.5))))
