#!/usr/bin/env python3
"""Extract exact per-level weight & boundary/transition structure for the PE763
transfer DP, purely from the existing data files (no BFS).

Reads data/level_N.txt (per-config lines "hist|M|dims") and
code/out/per_hist_mult_13_14.txt (distinct-hist,mult). For every distinct
histogram computes: a_1 (first nonzero level = a_1 since a_0=0 always) range,
M range, level-count value range, adjacent (a_k,a_{k+1}) transitions, and the
two equivalent weight-formula checks:
  branch form (as recorded): n6=0 -> 2^(2n4)*3^(n1+n2+n3-1),
                             n6>0 -> 10*2^(2n4)*3^(n1+n2+n3-2)
  unified product form:      C * prod_k w(a_k), C=1/3, w= {0:1,1:3,2:3,3:3,
                             4:4,5:1,6:10/3,7:1}
n_k counts levels with exactly k cells over ALL stored levels a_0..a_M
(a_0=0 contributes to no n_k; the top a_M=3 IS counted in n_3 -- verified
necessary: interior-only gives mult(0 2 3)=1 != 3).
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def hist_of_line(line):
    return line.split('|')[0].strip()

rows = []  # (N, vals_list_no_padding, mult)
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

print("total (hist,mult) rows:", len(rows), "  N range:", min(r[0] for r in rows), "..", max(r[0] for r in rows))

# ---- weight formula checks ----
def branch(vals):
    cnt = collections.Counter(vals)
    n1, n2, n3, n4, n6 = cnt[1], cnt[2], cnt[3], cnt[4], cnt[6]
    if n6:
        return 10 * 2**(2*n4) * 3**(n1+n2+n3-2)
    return 2**(2*n4) * 3**(n1+n2+n3-1)

W = {0:1, 1:3, 2:3, 3:3, 4:4, 5:1, 6:10.0/3.0, 7:1}
C = 1.0/3.0
def product(vals):
    p = 1.0
    for a in vals:
        p *= W[a]
    return C * p

bad_b = [r for r in rows if branch(r[1]) != r[2]]
bad_p = [r for r in rows if abs(product(r[1]) - r[2]) > 1e-9*max(1, r[2])]
print("branch-form mismatches:", len(bad_b), " product-form mismatches:", len(bad_p))

# ---- boundary rules ----
a1_vals, M_vals, top_vals, first_vals = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
lv_min, lv_max = {}, {}
for n, vals, m in rows:
    # stored hist may include trailing padding in level files? strip trailing zeros
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    M = len(v) - 1
    a0, a1 = v[0], v[1]
    first_vals[a0] += 1
    a1_vals[a1] += 1
    M_vals[M] += 1
    top_vals[v[-1]] += 1
    lo, hi = min(v), max(v)
    lv_min[n] = min(lv_min.get(n, 99), lo)
    lv_max[n] = max(lv_max.get(n, -1), hi)
    if sum(v) != 2*n+1:
        print("SUM VIOLATION", n, v, sum(v), "expected", 2*n+1)
print("a_0 (first stored level) distribution:", dict(sorted(first_vals.items())))
print("a_1 (first nonzero level) distribution:", dict(sorted(a1_vals.items())))
print("top level a_M distribution:", dict(sorted(top_vals.items())))
print("M distribution:", dict(sorted(M_vals.items())))
print("min level-count per N:", dict(sorted(lv_min.items())))
print("max level-count per N:", dict(sorted(lv_max.items())))

# ---- all occurring level-count values ----
occ = collections.Counter()
for n, vals, m in rows:
    for a in vals: occ[a] += 1
print("occurring level-count values (count of occurrences):", dict(sorted(occ.items())))

# ---- transition relation: adjacent pairs (a_k, a_{k+1}) ----
trans = collections.Counter()
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    for k in range(len(v)-1):
        trans[(v[k], v[k+1])] += 1
print("observed adjacent transitions (count):")
for (x, y), c in sorted(trans.items()):
    print(f"   {x} -> {y}  x{c}")
# check: is |a_{k+1}-a_k|<=3 always? max jump
maxjump = max(abs(b-a) for n, vals, m in rows
              for a, b in zip(vals, vals[1:]) if True)
print("max |a_{k+1}-a_k| over ALL stored adjacent pairs:", maxjump)

# ---- 6-level context: what precedes/follows a 6 ? ----
ctx6 = collections.Counter()
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    for k, a in enumerate(v):
        if a == 6:
            ctx6[(v[k-1] if k > 0 else None, v[k+1] if k+1 < len(v) else None)] += 1
print("contexts of a 6-level (prev,next) x count:", dict(sorted(ctx6.items(), key=lambda kv: (-kv[1], str(kv[0])))))

# ---- n6 per histogram ----
print("max #6-levels in a single histogram:", max(collections.Counter(v)[6] for n, v, m in rows))