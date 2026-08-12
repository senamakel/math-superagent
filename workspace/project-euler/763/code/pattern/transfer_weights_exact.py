#!/usr/bin/env python3
"""Exact-rational confirmation that the per-level product
   mult(h) = (1/3) * prod_k w(a_k),  w = {0:1, 1:3, 2:3, 3:3, 4:4, 5:1,
                                          6:10/3, 7:1}
reproduces every recorded multiplicity EXACTLY (no float), and that the only
non-constant weight is w(6) = 10/3.  Also reports the branch-form equivalence
and the observed transition/boundary structure in exact integers."""
from fractions import Fraction
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def hist_of_line(line):
    return line.split('|')[0].strip()

rows = []
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    per = collections.Counter()
    for line in open(path):
        per[hist_of_line(line)] += 1
    for hist, m in per.items():
        rows.append((n, list(map(int, hist.split())), m))
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); mi = line.index('mult=')
    hstr = line[h+5:mi].strip(); mval = int(line[mi+5:])
    vals = [int(x) for x in hstr.split()]
    while vals and vals[-1] == 0: vals.pop()
    rows.append((n, vals, mval))

W = {0: Fraction(1), 1: Fraction(3), 2: Fraction(3), 3: Fraction(3),
     4: Fraction(4), 5: Fraction(1), 6: Fraction(10, 3), 7: Fraction(1)}
C = Fraction(1, 3)

bad = []
nonint_contrib = set()
for n, vals, m in rows:
    prod = Fraction(1)
    for a in vals:
        prod *= W[a]
        if W[a].denominator != 1:
            nonint_contrib.add(a)
    pred = C * prod
    if pred != m:
        bad.append((n, vals, m, pred))
print(f"rows={len(rows)}  exact-product mismatches={len(bad)}  non-integer weights used={sorted(nonint_contrib)}")
for b in bad[:8]:
    print("   ", b)

# branch equivalence in exact form
print("\nbranch-form equivalence (exact):")
print("  no 6-level : mult = 2^(2 n4) * 3^(n1+n2+n3-1)")
print("  has 6-level: mult = 10 * 2^(2 n4) * 3^(n1+n2+n3-2)")
print("  product-form  : mult = (1/3) * 3^(n1+n2+n3) * 4^(n4) * (10/3)^[has 6]")
print("  (identical: (1/3)*3^a*4^b = 3^(a-1)*4^b; with a 6: (1/3)*(10/3)=10/9 -> 10*3^(a-2))")

# boundary rules exact
print("\nboundary/transition structure (exact, from recorded data):")
a1 = collections.Counter(); top = collections.Counter(); sm = True
trans = collections.Counter()
ctx6 = collections.Counter(); n6max = 0; vals_seen = set()
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    a1[v[1]] += 1; top[v[-1]] += 1
    if sum(v) != 2*n+1: sm = False
    for k in range(len(v)-1): trans[(v[k], v[k+1])] += 1
    vals_seen.update(v)
    n6 = sum(1 for a in v if a == 6)
    n6max = max(n6max, n6)
    for k, a in enumerate(v):
        if a == 6: ctx6[(v[k-1] if k else None, v[k+1] if k+1 < len(v) else None)] += 1
print(f"  a_1 (first nonzero level) distribution: {dict(sorted(a1.items()))}")
print(f"  top level a_M distribution: {dict(sorted(top.items()))}")
print(f"  sum a_k = 2N+1 always: {sm}")
print(f"  all level-count values occurring: {sorted(vals_seen)}")
print(f"  transitions: {dict(sorted(trans.items()))}")
print(f"  6-level context (prev,next)x cnt: {dict(sorted(ctx6.items(), key=lambda kv: (-kv[1], str(kv[0]))))}  max #6 per hist: {n6max}")
mxj = max(abs(b-a) for n, v, m in rows for a, b in zip(v, v[1:]))
print(f"  max |a_{k+1}-a_k| jump: {mxj}")