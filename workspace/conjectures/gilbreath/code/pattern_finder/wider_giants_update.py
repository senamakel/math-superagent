#!/usr/bin/env python3
"""Pattern pass on the wider-width record (sieve 3e8, depth 300, verified by
two independent runs: wider_width_extend + wider_width_clean, oracle-matched
on rows 1..161, step-law failures 0).

What is new since the depth-1000 analysis:
  * the depth-1000 "capped" jump at the 161->162 transition is now EXACT
    (landing block 5,417,975 has flooring ~10.8e6 >> 0 at width 3e8);
  * two NEW genuine giants beyond row 161 in the live regime (rows 162, 175),
    plus a capped giant at row 239 (the new k*).

This program extracts the extended sequences and updates the growth-law
comparisons (geometric vs sublinear) with the new points.  All arithmetic
exact (int64 / Fraction / math.log only of exact integers for fits).
"""
import json, math
from fractions import Fraction

D1 = json.load(open('/workspace/code/out/blocks_depth1000.json'))
DW = json.load(open('/workspace/code/out/wider_width_b_clean.json'))

b1, bW = D1['b'], DW['b']
P1, PW = D1['num_primes'], DW['num_primes']
print(f"depth-1000: P={P1} D={len(b1)}  wider: P={PW} D={len(bW)}")
# agreement on rows 1..161 (0-based 0..160)
agree = all(b1[i] == bW[i] for i in range(161))
print(f"b agreement rows 1..161: {agree}")
print(f"row-161 b (0-based 160): depth1000={b1[160]} wider={bW[160]}")

# events in the wider record: transition k->k+1 (0-based k), 1-based row k+1
def events(b):
    ev = []
    for k in range(len(b) - 1):
        j = b[k + 1] - b[k]
        if j != 0:  # (2,4)-events include jump-0 stalls, skip those here
            ev.append((k + 1, b[k], b[k + 1], j))  # 1-based row, b_k, b_{k+1}, jump
    return ev

evW = events(bW)
print(f"wider events with jump>0: {len(evW)}")
giants = [(r, bk, bl, j) for (r, bk, bl, j) in evW if j > 1000]
print(f"giants (jump>1000): {len(giants)}")
kstar = None
for r in range(1, len(bW) + 1):
    if bW[r - 1] >= PW - r - 1:
        kstar = r
        break
print(f"k* (first row with no intruder): {kstar}")
live = [(r, bk, bl, j) for (r, bk, bl, j) in giants if r < kstar]
print(f"live giants (rows < k*): {len(live)}")

g_rows   = [r for (r, bk, bl, j) in live]
g_jumps  = [j for (r, bk, bl, j) in live]
g_land   = [bl for (r, bk, bl, j) in live]
g_bk     = [bk for (r, bk, bl, j) in live]
g_gaps   = [g_rows[i + 1] - g_rows[i] for i in range(len(g_rows) - 1)]

print("\ngiant rows (1-based):", g_rows)
print("gaps:", g_gaps, " max:", max(g_gaps))
print("jumps:", g_jumps)
print("landing blocks:", g_land)
print("b_k at event:", g_bk)

# flooring at landing rows for the two new giants (exactness check)
for (r, bk, bl, j) in live:
    if r >= 160:
        # landing row = r+1, flooring = (W - (r+1) - 1) - bl
        fl = (PW - (r + 1) - 1) - bl
        print(f"giant row {r}: jump {j} land {bl} flooring(landing row {r+1}) = {fl}")

# --- fits ---
def lsq(xs, ys):
    n = len(xs)
    mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    m = sxy / sxx if sxx else 0.0
    c = my - m * mx
    ss = sum((y - (m * x + c)) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1 - ss / sst if sst else 1.0
    return m, c, r2

n = len(g_land)
lx = list(range(n)); ly = [math.log(x) for x in g_land]
m, c, r2 = lsq(lx, ly)
print(f"\ngeometric fit log(land)=a+m*x over {n} live giants: m={m:.6f} factor/event={math.exp(m):.4f} R2={r2:.6f}")

# log-log: log(jump) vs log(b_k)
lx = [math.log(x) for x in g_bk]; ly = [math.log(x) for x in g_jumps]
m, c, r2 = lsq(lx, ly)
print(f"log-log fit log(jump)=a+alpha*log(b): alpha={m:.6f} R2={r2:.6f}")

# sublinear rho model: rho-1 = C * b^(alpha-1); log(rho-1) = log C + (alpha-1) log b
rhos = [g_land[i + 1] / g_land[i] for i in range(len(g_land) - 1)]
lx = [math.log(g_land[i]) for i in range(len(g_land) - 1)]
ly = [math.log(r - 1) for r in rhos]
m, c, r2 = lsq(lx, ly)
print(f"\nsublinear fit log(rho-1)=logC+(alpha-1)*log(b): alpha-1={m:.6f} (alpha={1+m:.6f}) logC={c:.4f} (C={math.exp(c):.3f}) R2={r2:.6f}")
print("ratios:", [round(r, 4) for r in rhos])
pred_old = [1 + 802.6 * (b ** -0.612) for b in g_land[:-1]]
print("old-directive25 prediction (1+802.6*b^-0.612) at each b:", [round(p, 3) for p in pred_old])
print("old-model deviation at the row-162 giant:", round(rhos[11] - pred_old[11], 3))

# max-gap threshold table at wider width, live regime rows 1..kstar-1
print("\nthreshold table T(J) (live regime):")
for J in [100, 300, 1000, 3000, 10000, 30000, 100000, 200000, 1000000]:
    rows = [r for (r, bk, bl, j) in live if j > J]
    gaps = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
    print(f"  J={J:>9}: count {len(rows):2d}  max-gap {max(gaps) if gaps else '-'}  rows {rows}")

# new all-time maxima among giants
print("\ngiants setting new all-time max (of b):")
mx = 0
for (r, bk, bl, j) in live:
    print(f"  row {r}: land {bl} newmax={bl > mx}")
    mx = max(mx, bl)

# ratio of the pair straddling the old cap
print("\nratio at old cap (1094273 -> 5417975):", round(5417975 / 1094273, 4))
