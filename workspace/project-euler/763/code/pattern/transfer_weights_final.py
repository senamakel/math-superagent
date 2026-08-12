#!/usr/bin/env python3
"""AUTHORITATIVE table for the PE763 transfer-DP weights, verified against the
694 recorded (histogram, multiplicity) pairs (in-sample N=2..12 dumps +
out-of-sample N=13,14 bitmask run).  Read-only; no BFS.

Output: per-level weight table, boundary rules, transition table, and the
exact statement of which weights are constant.
"""
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

assert len(rows) == 694, len(rows)

# --- the two weight rules, spelled over ALL stored levels a_0..a_M ----
def branch(vals):
    cnt = collections.Counter(vals)   # NOTE: includes a_0=0 (no-op) AND the top a_M=3
    n1, n2, n3, n4, n6 = cnt[1], cnt[2], cnt[3], cnt[4], cnt[6]
    if n6:
        return 10 * 2**(2*n4) * 3**(n1+n2+n3-2)
    return 2**(2*n4) * 3**(n1+n2+n3-1)

W = {0:1, 1:3, 2:3, 3:3, 4:4, 5:1, 6:10, 7:1}   # integer weights; C = 1/3
C = (1, 3)  # C = 1/3 as fraction
def product(vals):
    num, den = 1, 1
    for a in vals:
        num *= W[a]
    return (num, den*3)

bad_b = bad_p = 0
for n, vals, m in rows:
    if branch(vals) != m: bad_b += 1
    num, den = product(vals)
    if num != m * den: bad_p += 1
print(f"rows={len(rows)}  branch-form mismatches={bad_b}  product-form(C=1/3) mismatches={bad_p}")

# --- per-level weight table with occurrence counts, min/max number of that
# --- level per histogram, max simultaneous occurrences
occ = collections.Counter()
mxm = {}
for n, vals, m in rows:
    c = collections.Counter(vals)
    for k, v in c.items():
        occ[k] += v
        mxm[k] = max(mxm.get(k, 0), v)
print("\nper-level weight table (mult = 1/3 * prod_k w(a_k) over stored levels a_0..a_M):")
for k in sorted(occ):
    print(f"  w({k}) = {W[k]}   occurrences={occ[k]:5d}   max #such levels per histogram={mxm[k]}")

# --- boundary rules ----
print("\nboundary rules:")
a1, tops, sumsOK = collections.Counter(), collections.Counter(), True
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    a1[v[1]] += 1
    tops[v[-1]] += 1
    if sum(v) != 2*n+1: sumsOK = False
print(f"  a_0 (stored origin level): always 0 (seen {rows[0][1][0]}); checked all 694")
print(f"  first nonzero level a_1 distribution: {dict(sorted(a1.items()))}")
print(f"  top level a_M distribution: {dict(sorted(tops.items()))}")
print(f"  sum a_k = 2N+1 held for all rows: {sumsOK}")

# --- transition relation (adjacent stored levels) and 6-context ----
trans = collections.Counter()
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    for k in range(len(v)-1):
        trans[(v[k], v[k+1])] += 1
print("\ntransitions (a_k -> a_{k+1}) observed, count:", len(trans))
print("  " + ", ".join(f"{a}->{b}(x{c})" for (a, b), c in sorted(trans.items())))
mxj = max(abs(b-a) for n, v, m in rows for a, b in zip(v, v[1:]))
print(f"  max |jump| = {mxj}")

ctx6 = collections.Counter()
n6max = 0
for n, vals, m in rows:
    v = [a for a in vals]
    while v and v[-1] == 0: v.pop()
    c6 = sum(1 for a in v if a == 6)
    n6max = max(n6max, c6)
    for k, a in enumerate(v):
        if a == 6:
            ctx6[(v[k-1] if k > 0 else None, v[k+1] if k+1 < len(v) else None)] += 1
print(f"\n6-level context (prev,next) x count: {dict(sorted(ctx6.items(), key=lambda kv:(-kv[1], str(kv[0]))))}")
print(f"max #6-levels in one histogram: {n6max}")