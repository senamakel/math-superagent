#!/usr/bin/env python3
"""Fresh independent re-derivation of the per-histogram multiplicity as a
per-level product (the transfer-kernel form needed for a DP).

Weight(v) over INTERIOR levels (exclude a_0=0 and a_M=3):
  v(1)=v(2)=v(3)=3, v(4)=4, v(5)=1, v(6)=10/3, v(a>=7)=1.
Check mult(h) == prod_k v(a_k) exactly on all in-sample (N=2..12) and
out-of-sample (N=13,14) histograms.
"""
import glob, collections
from fractions import Fraction

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def v(a):
    if a in (1,2,3): return Fraction(3)
    if a == 4: return Fraction(4)
    if a == 5: return Fraction(1)
    if a == 6: return Fraction(10,3)
    return Fraction(1)  # a>=7   (a==7 top-level 3 excluded by interior loop)

def product_weight(hist):
    w = Fraction(1)
    for k in range(1, len(hist)-1):   # interior levels
        w *= v(hist[k])
    return w

bad = 0; tot = 0
# in-sample
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    per = collections.Counter()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        per[hist.strip()] += 1
    for hist, m in per.items():
        tot += 1
        vals = tuple(map(int, hist.split()))
        pw = product_weight(vals)
        if pw != m:
            bad += 1
            if bad <= 10:
                print(f"MISMATCH in-sample N={n} hist={vals} count={m} product={pw}")
# out-of-sample
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); m_i = line.index('mult=')
    hist_str = line[h+5:m_i].strip(); mval = int(line[m_i+5:])
    vals = [int(x) for x in hist_str.split()]
    while vals and vals[-1] == 0: vals.pop()
    vals = tuple(vals)
    tot += 1
    pw = product_weight(vals)
    if pw != mval:
        bad += 1
        if bad <= 10:
            print(f"MISMATCH OOS N={n} hist={vals} count={mval} product={pw}")

print(f"Total histograms checked (in-sample N=2..12 + OOS N=13,14): {tot}")
print(f"Exceptions to per-level product rule: {bad}")
print("VERDICT:", "PRODUCT FORM EXACT" if bad == 0 else "PRODUCT FORM FAILS")
