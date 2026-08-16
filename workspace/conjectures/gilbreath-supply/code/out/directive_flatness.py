#!/usr/bin/env python3
"""Directive's requested comparison: residual flatness of w*(n)/n^E for
candidate exponents E.
   E = log2(3)-1 = 0.58496   (the natural Pascal-mod-2 constant)
   E = 0.5568               (fitted, pass 3)
   E = 0.543                (largest-tail OLS from extended run)
Report residual range (max/min) and any monotone trend in log2(n).
Exact w* extended to n=262144 (grouped Krawtchouk).
"""
from math import log2, log

data = [
    (16, 3), (32, 5), (64, 7), (128, 11), (256, 16), (512, 24),
    (1024, 35), (2048, 52), (4096, 77), (8192, 112), (16384, 164),
    (32768, 239), (65536, 349), (131072, 507), (262144, 738),
]

def col(n, w, E):
    return w / (n ** E)

for name, E in [("log2(3)-1=0.58496", log(3)/log(2)-1),
                ("0.5568 (pass-3 fit)", 0.5568),
                ("0.543 (large-tail fit)", 0.543)]:
    vals = [(n, col(n, w, E)) for n, w in data if n >= 256]
    xs = [v[0] for v in vals]
    cs = [v[1] for v in vals]
    rng = max(cs) - min(cs)
    spread = (max(cs) - min(cs)) / min(cs)
    # trend: correlation of col with log2(n)
    import statistics
    ys = [log2(x) for x in xs]
    mx, my = statistics.mean(ys), statistics.mean(cs)
    sxy = sum((y-mx)*(c-my) for y,c in zip(ys,cs))
    sxx = sum((y-mx)**2 for y in ys)
    trend = sxy/sxx
    print("%-24s spread=%6.3f  range=[%.4f,%.4f]  dcol/dlog2n=%.5f"
          % (name, spread, min(cs), max(cs), trend))
    print("   residuals: " + " ".join("%.3f" % c for c in cs))
