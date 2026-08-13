#!/usr/bin/env python3
"""Regeneration-event analysis from code/out/blocks_depth1000.json.

Only reads the JSON already on disk (b, s, intruder at depth 1000); no new
rows are generated. All row numbers are 1-based k (A_k). b(k) = length of the
leading {0,2} block of row k, s(k) = A_k(1) (second entry), intruder(k) =
A_k(b(k)+1) = first value past the block, None when the block reaches the end
of the row (b(k) = width(k) - 1).

Everything printed is computed exactly from the JSON.

Q1  regen events: transition k -> k+1 with b(k+1) >= b(k); jump = b(k+1)-b(k);
    intruder value at the source row k.
Q2  b(k) at regen rows vs at erosion rows (live regime k=1..161); jump-size
    distribution.
Q3  the longest pure-erosion run: its start, end, the b values in it, and what
    the intruder is doing (the run turns out to be the width-exhausted tail).
Q4  gaps between regeneration events; uniform/geometric/runs tests.
Q5  how low b gets, how often b sits at its running minimum.
"""
import json
from collections import Counter
import numpy as np

d = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = d["b"], d["s"], d["intruder"]
W, D = d["num_primes"], d["D"]
assert len(b) == len(s) == len(intr) == D == 1000

def bl(r): return b[r - 1]       # block length of row r
def ss(r): return s[r - 1]       # second entry of row r
def it(r): return intr[r - 1]    # intruder of row r (None if exhausted)

diff = {r: bl(r + 1) - bl(r) for r in range(1, D)}   # transition r -> r+1

print(f"D={D} primes={W}")
assert min(diff.values()) >= -1

# ---------- Q1: regeneration events ----------
regen = [r for r in range(1, D) if diff[r] >= 0]
print(f"\n=== Q1 ===\nn regen events (b(k+1)>=b(k)): {len(regen)} of {D-1} transitions")
print(f"regen k range: {min(regen)}..{max(regen)}")
print(f"all regen k <= 161: {max(regen) <= 161}")
print(f"n regen in live regime k=1..161: {sum(1 for r in regen if r <= 161)}")
print("intruder(k) at regen rows:", Counter(it(r) for r in regen).most_common())

print("\nregeneration events: k | b(k) -> b(k+1) | jump | intruder(k) | intruder(k+1)")
for r in sorted(regen):
    print(f"  {r:4d} | {bl(r):8d} -> {bl(r+1):8d} | {diff[r]:8d} | "
          f"{str(it(r)):>4s} | {str(it(r+1)):>5s}")

# rows with visible intruder == 4 that are NOT regen rows (these have x=0 at
# the block edge: y stays 4, erosion continues)
rows4 = [r for r in range(1, D + 1) if it(r) == 4]
regen_set = set(regen)
rows4_no = [r for r in rows4 if r not in regen_set]
print(f"\nrows with intruder==4: {len(rows4)}; of these regen rows: "
      f"{len(rows4) - len(rows4_no)}; non-regen (x=0) rows: {len(rows4_no)}")
print("non-regen intruder==4 rows:", rows4_no)

# do the non-regen 4-rows persist? next intruder after a non-regen 4-row
next4 = Counter()
for r in rows4_no:
    if r + 1 <= D and it(r + 1) is not None:
        next4[it(r + 1)] += 1
print("intruder(k+1) after non-regen intruder==4 rows:", sorted(next4.items()))
# after a regen row: new intruder distribution
nxt = Counter(it(r + 1) for r in regen if r + 1 <= D and it(r + 1) is not None)
print("intruder(k+1) after regen rows (visible only):", sorted(nxt.items()))

# consecutive regen: P(regen at k+1 | regen at k) vs marginal
marg = len(regen) / (D - 1)
tr = set(regen)
cond = sum(1 for k in regen if k + 1 in tr and k + 1 <= D - 1) / len(regen)
print(f"P(regen) marginal = {marg:.4f}; P(regen at k+1 | regen at k) = {cond:.4f} "
      f"(over all 999 transitions; tail dilutes both)")

# ---------- Q2: b at regen vs erosion (live regime) ----------
live = list(range(1, 162))          # transitions k=1..161 (intruder visible)
er_l = [r for r in live if diff[r] == -1]
rg_l = [r for r in live if diff[r] >= 0]
print(f"\n=== Q2 ===\nlive regime transitions k=1..161: 161; regen {len(rg_l)}, erosion {len(er_l)}")

bj_reg = [bl(r) for r in rg_l]
bj_er = [bl(r) for r in er_l]
print(f"b(k) at regen rows : n={len(bj_reg)} min={min(bj_reg)} max={max(bj_reg)} "
      f"mean={np.mean(bj_reg):.1f} median={np.median(bj_reg):.0f}")
print(f"b(k) at erosion rows: n={len(bj_er)} min={min(bj_er)} max={max(bj_er)} "
      f"mean={np.mean(bj_er):.1f} median={np.median(bj_er):.0f}")

# regen rate by b-bucket over the live regime
bounds = [0, 10, 100, 1000, 10000, 100000, 1000000, 10**9]
print("regen rate by b(k) bucket (live regime):")
for lo, hi in zip(bounds[:-1], bounds[1:]):
    rs = [r for r in live if lo <= bl(r) < hi]
    if rs:
        nr = sum(1 for r in rs if diff[r] >= 0)
        print(f"  b in [{lo},{hi}): transitions {len(rs):4d}, regen {nr:3d}, "
              f"rate {nr/len(rs):.3f}")

# jump size distribution
jumps = sorted(diff[r] for r in regen)
print("\njump sizes at regen: min", min(jumps), "max", max(jumps),
      "median", np.median(jumps), "mean", f"{np.mean(jumps):.1f}")
hist = Counter()
for j in jumps:
    if j == 0: hist["0"] += 1
    elif j < 10: hist["1-9"] += 1
    elif j < 100: hist["10-99"] += 1
    elif j < 1000: hist["100-999"] += 1
    elif j < 10000: hist["1000-9999"] += 1
    elif j < 100000: hist["10000-99999"] += 1
    else: hist[">=100000"] += 1
print("jump-size histogram:", sorted(hist.items()))
bjrk = np.array(bj_reg); jrk = np.array(jumps)
print(f"corr(jump, b at regen row): pearson={np.corrcoef(bjrk, jrk)[0,1]:.3f}")

# ---------- Q3: longest pure-erosion run ----------
runs = []          # (start_row, length)
c_start, c_len = None, 0
for r in range(1, D):
    if diff[r] == -1:
        if c_len == 0: c_start = r
        c_len += 1
    else:
        if c_len: runs.append((c_start, c_len))
        c_len = 0
if c_len: runs.append((c_start, c_len))
runs.sort(key=lambda t: -t[1])
print(f"\n=== Q3 ===\nerosion runs (start, length), top 8: {runs[:8]}")
top_start, top_len = runs[0]
print(f"longest: starts at k={top_start}, ends at k={top_start+top_len-1}, "
      f"length {top_len}")
top_end = top_start + top_len - 1
print(f"record boundary: D-1 = {D-1}; start + length - 1 = {top_end}")
print(f"run ends at the last transition of the record: {top_end == D-1}")
print(f"b(161)={bl(161)} b(162)={bl(162)} b(163)={bl(163)}")
print(f"intruder(161)={it(161)} intruder(162)={it(162)}")
print(f"width(162) = W-162 = {W-162}; b(162) = {bl(162)} = width-1: "
      f"{bl(162) == W-162-1}")
print(f"tail check: b(k) == W-k-1 and diff==-1 for all k=162..1000: "
      f"{all(bl(k) == W-k-1 and diff[k] == -1 for k in range(162, D))}")
print(f"intruder null from k=162: {all(it(k) is None for k in range(162, D+1))}")
print(f"b month by month near run start:")
for k in range(158, 172):
    print(f"  k={k:4d} b={bl(k):8d} diff={diff[k] if k < D else None} intruder={it(k)}")
print(f"b at run end (k=995..1000):")
for k in range(995, D + 1):
    print(f"  k={k:4d} b={bl(k):8d}")
live_runs = [t for t in runs if t[0] + t[1] - 1 <= 161]
print(f"longest erosion run fully inside live regime k<=161: {max(live_runs, key=lambda t: t[1])}")
print("live-regime erosion run lengths:", sorted([t[1] for t in live_runs]))

# ---------- Q4: position/gap structure of regen events ----------
rg_sorted = sorted(rg_l)   # regen rows inside live regime
gaps = [rg_sorted[i+1] - rg_sorted[i] for i in range(len(rg_sorted)-1)]
print(f"\n=== Q4 ===\nregen rows in live regime (k=1..161): {rg_sorted}")
print(f"internal gaps between consecutive regen rows: {gaps}")
print(f"gap stats: n={len(gaps)} min={min(gaps)} max={max(gaps)} "
      f"mean={np.mean(gaps):.2f} median={np.median(gaps):.0f}")
print(f"stdev={np.std(gaps):.2f} (mean of geometric p={len(rg_sorted)/161:.3f} is "
      f"{1/(len(rg_sorted)/161):.2f} for iid Bernoulli)")

# uniformity chi-square over 7 buckets of 23 rows in k=1..161
nb = 7
obs = [sum(1 for r in rg_sorted if lo <= r <= hi) for lo, hi in
       [(1 + i*23, 23 + i*23) for i in range(nb)]]
exp = len(rg_sorted) / nb
chi2 = sum((o - exp) ** 2 / exp for o in obs)
print(f"uniformity k=1..161 in 7 buckets of 23: obs={obs} exp={exp:.2f} "
      f"chi2={chi2:.2f} (df=6, 95% crit 12.59)")

# runs test on the binary string (1=regen) inside live regime
binstr = [1 if diff[r] >= 0 else 0 for r in live]
n1, n0 = sum(binstr), len(binstr) - sum(binstr)
nruns = 1 + sum(1 for i in range(1, len(binstr)) if binstr[i] != binstr[i-1])
mu = 2*n1*n0/(n1+n0) + 1
var = 2*n1*n0*(2*n1*n0 - n1 - n0) / ((n1+n0)**2 * (n1+n0-1))
print(f"runs test (live): n1={n1} n0={n0} runs={nruns} expected={mu:.2f} "
      f"sd={var**0.5:.2f} z={(nruns-mu)/var**0.5:+.2f}")

# ---------- Q5: minimum block lengths ----------
print("\n=== Q5 ===")
print(f"global min b = {min(bl(r) for r in range(1, D+1))} at k = "
      f"{[r for r in range(1, D+1) if bl(r) == min(bl(x) for x in range(1, D+1))]}")
b2min = min(bl(r) for r in range(2, D + 1))
k2min = [r for r in range(2, D + 1) if bl(r) == b2min]
print(f"min b over k=2..1000 = {b2min} at k = {k2min}")
print(f"count of rows with b == 2: {sum(1 for r in range(1, D+1) if bl(r) == 2)}")
runmin = 10**9; atmin = 0; tot_atmin = 0
for r in range(1, D + 1):
    if bl(r) < runmin:
        runmin = bl(r); atmin = 1
    elif bl(r) == runmin:
        atmin += 1; tot_atmin += 1
print(f"running min stays 2 forever (first row is global min): {runmin == 2}")
print(f"rows after k=1 at running min: {tot_atmin}")

# local minima and their dwell times
lmin = []
for r in range(2, D):
    if bl(r) <= bl(r-1) and bl(r) <= bl(r+1):
        lmin.append((r, bl(r)))
print(f"local minima of b (k, value), n={len(lmin)}:")
for r, v in lmin:
    # dwell: consecutive rows from r with b == v (running at the floor)
    j = r
    while j < D and bl(j+1) == v:
        j += 1
    print(f"  k={r:4d} b={v:8d} (dwell {j-r+1} rows)")
print("distinct small b values with counts (whole record):",
      sorted(Counter(bl(r) for r in range(1, D+1)).most_common(12)))

# s structure
sr = Counter(ss(r) for r in range(1, D + 1))
print(f"\ns: {sr[0]} zeros, {sr[2]} twos")
scur, slen = ss(1), 1
srun = []
for r in range(2, D + 1):
    if ss(r) == scur: slen += 1
    else: srun.append((scur, slen)); scur, slen = ss(r), 1
srun.append((scur, slen))
print("longest s runs:", sorted(srun, key=lambda t: -t[1])[:8])