#!/usr/bin/env python3
"""Verify the per-level product factorization of the per-histogram multiplicity:
   mult(h) = C * prod_k w(a_k)   over levels a_0..a_M
with candidate weights. Also enumerate which level-counts k actually occur and
their per-level weight, and check the boundary rules (a_0=0, a_1=1, a_M=3,
sum=2N+1, smooth-composition |a_{k+1}-a_k|<=1).

Data sources (read-only, no BFS):
  - data/level_N.txt : one line per CONFIG "hist|M|bbox", per-hist multiplicity
                       = #lines with same hist.
  - code/out/per_hist_mult_13_14.txt : distinct-hist with mult, N=13,14.
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def hist_of_line(line):
    return line.split('|')[0].strip()

# candidate per-level weight map (product weights)
W = {0:1, 1:3, 2:3, 3:3, 4:4, 5:1, 6:10.0/3.0, 7:1}
C = 1.0/3.0

def prod_weight(vals):
    # vals = full histogram list a_0..a_M (no trailing padding zeros)
    p = 1.0
    unknown = set()
    for a in vals:
        if a in W:
            p *= W[a]
        else:
            unknown.add(a)
    return C*p, unknown

def exact_mult(vals):
    """closed 2/3-smooth form from the established rule, counted over ALL
    levels a_0..a_M (leading 0 contributes nothing; top a_M=3 is a real 3)."""
    cnt = collections.Counter(vals)
    n1,n2,n3,n4 = cnt[1],cnt[2],cnt[3],cnt[4]
    if 6 in cnt:
        return 10 * 2**(2*n4) * 3**(n1+n2+n3-2)
    return 2**(2*n4) * 3**(n1+n2+n3-1)

rows = []  # (N, hist_vals, mult)
# in-sample
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    per = collections.Counter()
    for line in open(path):
        per[hist_of_line(line)] += 1
    for hist, m in per.items():
        rows.append((n, list(map(int, hist.split())), m))
# OOS
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); mi = line.index('mult=')
    hstr = line[h+5:mi].strip(); mval = int(line[mi+5:])
    vals = [int(x) for x in hstr.split()]
    while vals and vals[-1]==0: vals.pop()
    rows.append((n, vals, mval))

print(f"total (hist,mult) rows: {len(rows)}")

# 1) exact closed form vs recorded mult
bad = 0
for n,vals,m in rows:
    if exact_mult(vals) != m:
        bad += 1
        if bad <= 8: print("  CLOSED-FORM MISMATCH", n, vals, 'mult',m,'pred',exact_mult(vals))
print("closed-form(2/3-smooth) mismatches:", bad)

# 2) per-level product form vs recorded mult
badp = 0; unknown_all = set()
for n,vals,m in rows:
    p, unk = prod_weight(vals)
    unknown_all |= unk
    if abs(p - m) > 1e-9 * max(1,m):
        badp += 1
        if badp <= 8: print("  PRODUCT MISMATCH", n, vals, 'mult',m,'pred',p, 'unk',unk)
print("per-level-product mismatches:", badp, " unknown-level-counts seen:", sorted(unknown_all))

# 3) boundary rules & occurring level counts
occ = collections.Counter()
viol_first = viol_last = viol_sum = viol_smooth = 0
for n,vals,m in rows:
    for a in vals: occ[a] += 1
    nonpadded = [a for a in vals]  # already unpadded for OOS; data maybe has trailing? check
    # strip trailing zeros if any
    while nonpadded and nonpadded[-1]==0: nonpadded.pop()
    if nonpadded[0] != 0: viol_first += 1
    if len(nonpadded) >= 2 and nonpadded[1] != 1: 
        # first nonzero level a_1
        pass
    if nonpadded[-1] != 3: viol_last += 1
    if sum(nonpadded) != 2*n+1: viol_sum += 1
    # smooth composition check |a_{k+1}-a_k|<=1 over interior
    for k in range(1, len(nonpadded)):
        if abs(nonpadded[k]-nonpadded[k-1]) > 1:
            viol_smooth += 1
            break
print("occurring level-counts (a_k values):", sorted(occ.items()))
print("violations: first!=0:",viol_first, " last!=3:",viol_last,
      " sum!=2N+1:",viol_sum, " non-smooth:",viol_smooth)

# 4) does a_1 always =1 ? 
a1_bad = 0
for n,vals,m in rows:
    np_=[a for a in vals]
    while np_ and np_[-1]==0: np_.pop()
    if np_[1] != 1: a1_bad += 1
print("a_1 != 1 count:", a1_bad)

# 5) how many 6-levels can occur in one histogram? (product form predicts (10/3)^n6)
maxn6 = 0; two6 = 0
for n,vals,m in rows:
    c6 = collections.Counter(vals)[6]
    maxn6 = max(maxn6, c6)
    if c6 >= 2: two6 += 1
print("max #6-levels in any single histogram:", maxn6, "  histograms with >=2 six-levels:", two6)
