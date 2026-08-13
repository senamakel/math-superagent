"""Corrected 14-genuine-giant analysis (3e8 run), rows 35..175.

Fixes my earlier 15-term extraction: row 239 is the k* width-capped event
(flooring = 1, intruder None) — its jump is a lower bound and its gap
arithmetic is excluded. Genuine giants at 3e8 (per producing run and by
flooring check): rows 35,57,65,69,95,97,111,113,127,131,135,147,162,175.

Checks:
 1. landing floorings all > 1000 (genuine, none width-truncated)
 2. geometric vs linear LS fit over the 14 landing blocks
 3. parity of the event index i = row - 1 (old convention): 34,56,64,68,
    94,96,110,112,126,130,134,146,161,174
 4. mod-4 classes of the event indices
 5. inter-giant gaps (genuine only)
 6. recharge identity surplus at depth 300
Exact integer arithmetic throughout; floats only in the fits (doubles).
"""
import json, math

with open('code/out/pattern_finder_outputs/wider_giants.json') as f:
    w = json.load(f)

W = w['W']
rows = w['giant_rows']
genuine = [r for r in rows if r != 239]          # 239 = capped k* event
land = [w['landing_blocks'][i] for i, r in enumerate(rows) if r != 239]
jumps = [w['giant_jumps'][i] for i, r in enumerate(rows) if r != 239]
floors = w['landing_floorings']
gfloors = [floors[i] for i, r in enumerate(rows) if r != 239]

print(f"W = {W}, genuine giants = {len(genuine)}: rows={genuine}")
print(f"landing floorings (all must be >1000): {gfloors}")
print(f"genuine landing blocks: {land}")
print(f"genuine jumps: {jumps}")
print(f"genuine inter-giant gaps: {[genuine[i+1]-genuine[i] for i in range(len(genuine)-1)]}")

# ---- event indices (old convention i = row - 1) and parity ----
ev = [r - 1 for r in genuine]
print(f"event indices: {ev}")
par = [i % 2 for i in ev]
print(f"event-index parity: {par}  -> {par.count(0)}/14 even; "
      f"odd = {[e for e in ev if e % 2 == 1]}")
print(f"event-index mod 4: {[e % 4 for e in ev]}")
print(f"event-index mod 8: {[e % 8 for e in ev]}")

# also depth-1000 giants (2e7): rows 35..147 -> event indices 34..146, plus
# the old capped event at row 162 (i=161)
old = [35, 57, 65, 69, 95, 97, 111, 113, 127, 131, 135, 147, 162]
old_ev = [r - 1 for r in old]
print(f"depth-1000 event indices: {old_ev}, parity {[e % 2 for e in old_ev]}")

# ---- fits over the 14 genuine landings ----
n = len(land)
x = list(range(n))
logb = [math.log(v) for v in land]
def ls(xs, ys):
    m = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(v * v for v in xs); sxy = sum(a * b for a, b in zip(xs, ys))
    d = m * sxx - sx * sx
    return (m * sxy - sx * sy) / d, (sy - (m * sxy - sx * sy) / d * sx) / m
def r2(xs, ys, slope, inter):
    ybar = sum(ys) / len(ys)
    ss_tot = sum((y - ybar) ** 2 for y in ys)
    ss_res = sum((y - slope * xx - inter) ** 2 for xx, y in zip(xs, ys))
    return 1 - ss_res / ss_tot
sg, ig = ls(x, logb)
sl, il = ls(x, land)
print(f"GEOMETRIC: slope m={sg:.6f}, intercept={ig:.6f}, R2={r2(x, logb, sg, ig):.6f}, "
      f"factor/event = exp(m) = {math.exp(sg):.4f}")
print(f"LINEAR   : slope m={sl:.2f}, intercept={il:.2f}, R2={r2(x, land, sl, il):.6f}")
ratios = [land[i + 1] / land[i] for i in range(n - 1)]
print(f"ratios: {[f'{v:.3f}' for v in ratios]}, mean={sum(ratios)/len(ratios):.3f}")

# ---- recharge surplus at depth 300 ----
b300 = w['landing_blocks'][-1] if False else None
with open('code/out/wider_width_b_clean.json') as f:
    bw = json.load(f)['b']
k = 300
surplus = bw[k - 1] - 2 + (k - 1)          # b_k = b_1 + sum(j+1) - (k-1)
print(f"b_300 = {bw[299]}, surplus sum(j+1) over events = {surplus}, "
      f"slack vs required (k-1-b_1 = {k-1-2}) = {bw[299]}")

# ---- record the depth-1000 geniune gap set for comparison ----
print("depth-1000 genuine gaps (rows 35..147):",
      [old[i + 1] - old[i] for i in range(len(old) - 1)])