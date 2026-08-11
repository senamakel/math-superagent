"""Test the scaling symmetry: if d1 = m^2 * d2 then |I_{d1}(n)| = |I_{d2}(n)|?
And if so, b_{d1} = m * b_{d2}? Check from results_full.txt (n=1e13) and the
n=1e4 scan (compute_I-derived data).
Also sum grouped |I| values and compare S.
"""
import math, re

# parse results_full
res = {}
for line in open('/workspace/results_full.txt'):
    parts = line.split()
    if parts and parts[0].isdigit():
        d = int(parts[0]); b = int(parts[1]); a = int(parts[2]); absa = int(parts[3])
        res[d] = (b, a, absa)

# find pairs d1 = m^2 d2 with both non-square in [2,99]
pairs = []
non_sq = sorted(d for d in range(2,100) if math.isqrt(d)**2 != d)
for d2 in non_sq:
    for m in range(2, 10):
        d1 = m*m*d2
        if d1 in res and d1 != d2 and math.isqrt(d1)**2 != d1:
            pairs.append((d1, d2, m, res[d1][2], res[d2][2], res[d1][0], res[d2][0]))

print("d1=m^2*d2 pairs (|I|_d1, |I|_d2, b_d1, b_d2):")
ok_all = True
for (d1,d2,m,a1,a2,b1,b2) in pairs:
    ok_abs = (a1 == a2)
    ok_b = (b1 == m*b2) if True else None
    if not ok_abs: ok_all = False
    print(f"  {d1} = {m}^2*{d2}: |I| {a1} vs {a2} same={ok_abs}  b {b1} vs {m}*{b2}={m*b2} bmatch={ok_b}")

print("ALL |I| match:", ok_all)
# count distinct |I| values
absvals = [res[d][2] for d in sorted(res)]
print("distinct |I|:", len(set(absvals)), "out of", len(absvals))
S = sum(absvals)
print("S from file:", S)
print("S via pairs check: still", S)
# Histogram of repeats
from collections import Counter
c = Counter(absvals)
print("repeated |I|:", {k: v for k,v in c.items() if v>1})