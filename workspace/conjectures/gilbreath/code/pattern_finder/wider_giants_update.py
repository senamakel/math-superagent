#!/usr/bin/env python3
"""Pattern pass on the wider-width record (sieve 3e8, depth 300). Final.

Conventions: event at source row r (1-based) means b[r-1] -> b[r],
jump j = b[r]-b[r-1] > 0.  Landing row = r+1.  The captured files
(wider_width_extend/clean) print landing rows; source = landing-1.
Rows 1..238 identical in both runs; the source-238 giant (landing 239)
is width-capped (landing flooring 0) -> exclude from "genuine".

Genuine giants: source rows 34,56,64,68,94,96,110,112,126,130,134,146,161,174.
Two of these (161, 174) are NEW beyond the depth-1000 live regime (1..161).
"""
import json, math

A = json.load(open('/workspace/code/out/wider_width_b.json'))
B = json.load(open('/workspace/code/out/wider_width_b_clean.json'))
b = A['b']; W = A['num_primes']
assert all(b[i] == B['b'][i] for i in range(238))
print(f"P={W}, D={len(b)}, rows 1..238 agree between the two runs")

def events(b, rmax):
    return [(k+1, b[k], b[k+1], b[k+1]-b[k]) for k in range(min(rmax, len(b)-1))]

giants = [(r, bk, bl, j) for (r, bk, bl, j) in events(b, 237) if j > 1000]  # source rows <= 237 = landing <= 238, all genuine
g_rows = [r for (r, bk, bl, j) in giants]
g_bk   = [bk for (r, bk, bl, j) in giants]
g_land = [bl for (r, bk, bl, j) in giants]
g_jump = [j for (r, bk, bl, j) in giants]
g_gaps = [g_rows[i+1]-g_rows[i] for i in range(len(g_rows)-1)]

print(f"\ngenume genuine giants (source rows 1..237): {len(giants)}")
print("source rows:", g_rows)
print("gaps (source rows):", g_gaps, "max", max(g_gaps))
print("landing blocks:", g_land)
print("jumps:", g_jump)

for (r, bk, bl, j) in giants:
    fl = (W - (r+1) - 1) - bl
    print(f"  src {r:3d} -> land {r+1:3d}: b {bk:>10} -> {bl:>10}  jump {j:>9}  flooring(land) {fl:>10}")

# capped row-238 event (landing 239)
for name, d in [("A", A), ("B", B)]:
    bb = d['b']
    print(f"capped src238 {name}: b238={bb[237]} -> b239={bb[238]} jump {bb[238]-bb[237]}")

# record maxima
mx = 0; n_rec = 0
for (r, bk, bl, j) in giants:
    n_rec += (bl > mx); mx = max(mx, bl)
print(f"genuine giants setting new all-time max: {n_rec}/{len(giants)}")

# running minima of b in the new regime (rows 162..238)
bseg = b[161:238]
runmin = min(bseg)
print(f"\nmin b over rows 162..238: {runmin} at rows {[162+i for i,v in enumerate(bseg) if v==runmin]}")
print(f"new minima below 1094263 in rows 162..238: {[v for v in bseg if v < 1094263]}")

# fits on 14 genuine giants
def lsq(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    sxx = sum((x-mx)**2 for x in xs); sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    m = sxy/sxx; c = my - m*mx
    ss = sum((y-(m*x+c))**2 for x, y in zip(xs, ys)); sst = sum((y-my)**2 for y in ys)
    return m, c, 1 - ss/sst

n = len(g_land)
m, c, r2 = lsq(range(n), [math.log(x) for x in g_land])
print(f"\nGEOMETRIC fit log(land)=a+m*idx over {n}: m={m:.6f} factor={math.exp(m):.4f}/event R2={r2:.6f}")
m2, c2, r22 = lsq(range(n), g_land)
print(f"LINEAR   fit land=a+m*idx: m={m2:.1f} R2={r22:.6f}")
m3, c3, r23 = lsq([math.log(x) for x in g_bk], [math.log(x) for x in g_jump])
print(f"log-log jump vs b: alpha={m3:.6f} R2={r23:.6f}")

rhos = [g_land[i+1]/g_land[i] for i in range(n-1)]
print("\nratios rho_k:", [round(r,4) for r in rhos])
print("min/max ratio:", min(rhos), max(rhos))

# directive25 sublinear model predictions (C=802.6, alpha=0.388)
print("\nold directive25 sublinear model rho=1+802.6*b^-0.612 vs actual:")
for i in range(n-1):
    pred = 1 + 802.6 * (g_land[i] ** -0.612)
    flag = "OK" if abs(pred-rhos[i]) < 0.15 else "MISS"
    print(f"  b={g_land[i]:>10} pred {pred:7.3f} actual {rhos[i]:7.3f} {flag}")

# jump-to-block ratios
print("\njump/b_k:", [round(j/bk,3) for (r,bk,bl,j) in giants])

# threshold table live regime (source rows <= 237)
print("\nthreshold T(J) max-gap over live regime rows 1..237:")
for J in [100, 300, 1000, 3000, 10000, 30000, 100000, 200000, 1000000]:
    rows = [r for (r,bk,bl,j) in giants if j > J]
    gaps = [rows[i+1]-rows[i] for i in range(len(rows)-1)]
    print(f"  J={J:>9}: count {len(rows):2d} max-gap {max(gaps) if gaps else '-':>4} rows {rows}")

# first-row-past-each-giant with flooring < 1000 (cap proximity): all giants have floor >> 1000
print("\nmin flooring over genuine giants' landing rows:",
      min((W-(r+1)-1)-bl for (r,bk,bl,j) in giants))
