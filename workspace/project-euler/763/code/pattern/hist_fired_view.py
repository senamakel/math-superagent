#!/usr/bin/env python3
"""Study per-histogram counts: display fired vector, look for tensor / transfer structure."""
import os
from collections import defaultdict
from fractions import Fraction

def fired_from_hist(hist):
    f = [1]
    for l in range(1, len(hist)):
        f.append(3*f[l-1] - hist[l])
    return f

def factor_powers_of_3(n):
    """Return (3^a * rest)."""
    a = 0
    while n % 3 == 0:
        n //= 3
        a += 1
    return a, n

print("N=4..12: histogram (h) | fired vector (f) | count, factorized")
for N in range(4, 13):
    path = f"data/level_{N}.txt"
    if not os.path.exists(path):
        continue
    hcount = defaultdict(int)
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            hist = tuple(int(x) for x in line.split('|')[0].split())
            hcount[hist] += 1
    print(f"\n===== N={N} (total D={sum(hcount.values())}) =====")
    for hist in sorted(hcount):
        f = fired_from_hist(hist)
        c = hcount[hist]
        a, rest = factor_powers_of_3(c)
        print(f"  h={' '.join(map(str,hist))}  f={' '.join(map(str,f))}  "
              f"count={c} = 3^{a} * {rest}")
