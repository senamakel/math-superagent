#!/usr/bin/env python3
"""Pattern pass on the wider-width record (sieve 3e8, depth 300).

Data: code/out/wider_width_b.json (run A, k*=239) and
      code/out/wider_width_b_clean.json (run B).  Rows 1..238 identical in
      both; the row-239 giant is width-capped (landing within 1 column of the
      row edge) and the two runs differ by 1 there.  Live regime = rows 1..238
      (flooring >= 1000); rows >= 239 are lower bounds.

New since depth-1000: the previously capped jump at row 161->162 is now exact
(4,323,712), and two new genuine giants exist at rows 162, 175.
"""
import json, math

A = json.load(open('/workspace/code/out/wider_width_b.json'))
B = json.load(open('/workspace/code/out/wider_width_b_clean.json'))
b = A['b']; W = A['num_primes']
assert all(b[i] == B['b'][i] for i in range(238)), "rows 1..238 must agree"
print(f"P={W}, D={len(b)}, rows 1..238 agree between the two runs")

# live regime: rows 1..238 (row 239 = capped giant, landing at flooring<=1)
kstar = 239
live_rows = list(range(1, kstar))

def events(b, rows):
    ev = []
    for k in range(len(b) - 1):
        r = k + 1
        if r not in rows:
            continue
        j = b[k + 1] - b[k]
        ev.append((r, b[k], b[k + 1], j))
    return ev

ev = events(b, live_rows)
giants = [(r, bk, bl, j) for (r, bk, bl, j) in ev if j > 1000]
g_rows  = [r for (r, bk, bl, j) in giants]
g_bk    = [bk for (r, bk, bl, j) in giants]
g_land  = [bl for (r, bk, bl, j) in giants]
g_jump  = [j for (r, bk, bl, j) in giants]
g_gaps  = [g_rows[i+1] - g_rows[i] for i in range(len(g_rows)-1)]

print(f"live giants (jump>1000, rows<239): {len(giants)}")
print("rows:", g_rows)
print("gaps:", g_gaps, "max", max(g_gaps))
print("landing blocks:", g_land)
print("jumps:", g_jump)

# flooring at each giant's landing row (must be > 1000 for genuine)
for (r, bk, bl, j) in giants:
    fl = (W - (r + 1) - 1) - bl
    assert fl > 1000, f"giant row {r} not genuine: flooring {fl}"
print("all 14 giants have landing-flooring > 1000 (genuine): True")

# the capped row-239 event (both runs)
for name, d in [("A", A), ("B", B)]:
    bb = d['b']
    print(f"capped row-239 {name}: b238={bb[237]} -> b239={bb[238]} jump {bb[238]-bb[237]}")

# every giant sets a new all-time max of b
mx = 0; n_rec = 0
for (r, bk, bl, j) in giants:
    if bl > mx:
        n_rec += 1
    mx = max(mx, bl)
print(f"giants setting a new all-time max: {n_rec}/{len(giants)}")

# ---- fits ----
def lsq(xs, ys):
    n = len(xs)
    mx = sum(xs)/n; my = sum(ys)/n
    sxx = sum((x-mx)**2 for x in xs); sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    m = sxy/sxx if sxx else 0.0; c = my - m*mx
    ss = sum((y-(m*x+c))**2 for x, y in zip(xs, ys))
    sst = sum((y-my)**2 for y in ys)
    return m, c, (1 - ss/sst if sst else 1.0)

n = len(g_land)
m, c, r2 = lsq(range(n), [math.log(x) for x in g_land])
print(f"\ngeometric fit over {n} live giants: slope {m:.6f} factor {math.exp(m):.4f}/event R2 {r2:.6f}")

m, c, r2 = lsq([math.log(x) for x in g_bk], [math.log(x) for x in g_jump])
print(f"log-log jump vs b: alpha {m:.6f} R2 {r2:.6f}")

rhos = [g_land[i+1]/g_land[i] for i in range(len(g_land)-1)]
print("\nratios rho_k = land_{k+1}/land_k:")
print([round(r, 4) for r in rhos])
print("min ratio:", min(rhos), " max ratio:", max(rhos))

# sublinear model (directive25): rho = 1 + C*b^(alpha-1), C=802.6 alpha=0.388
C, alpha = 802.6, 0.388
print("\nsublinear-model predictions rho = 1 + 802.6*b^-0.612 vs actual:")
for i in range(len(g_land)-1):
    pred = 1 + C * (g_land[i] ** -0.612)
    print(f"  b={g_land[i]:>10} pred {pred:7.3f}  actual {rhos[i]:7.3f}  {'OK' if abs(pred-rhos[i])<0.15 else 'MISS'}")

# threshold table in live regime
print("\nthreshold table T(J), live regime rows 1..238:")
for J in [100, 300, 1000, 3000, 10000, 30000, 100000, 200000, 1000000]:
    rows = [r for (r, bk, bl, j) in giants if j > J]
    gaps = [rows[i+1]-rows[i] for i in range(len(rows)-1)]
    print(f"  J={J:>9}: count {len(rows):2d}  max-gap {max(gaps) if gaps else '-':>4}  rows {rows}")

# jumps as multiples of current block (jump/b_k)
print("\njump/b_k at each giant:", [round(j/bk, 3) for (r, bk, bl, j) in giants])

# erosion-before-giant: rows since previous event (any event incl. stalls)
ev_rows = [r for (r, bk, bl, j) in events(b, live_rows)]
print("\nall event rows (incl. jump-0 stalls) in live regime:", len(ev_rows))
gi = set(g_rows)
prev_ev = {}
last = None
for r in ev_rows:
    if r in gi:
        prev_ev[r] = last
    last = r
print("gap to previous event (any) before each giant:")
print([(r, (r - prev_ev[r]) if prev_ev[r] else None) for r in g_rows])
