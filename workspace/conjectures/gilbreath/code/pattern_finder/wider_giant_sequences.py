"""Extract and verify the 15-giant sequences from the wider-width (3e8) run.

Inputs:
  code/out/wider_width_b_clean.json  -- b[k-1] = leading {0,2} block length of
        row k (1-based), k = 1..300; W = 16,252,325 primes; step-law verified 0
        failures in the producing run (wider_width_clean.captured.txt).
  code/out/pattern_finder_outputs/b_genuine.txt -- depth-1000 b, rows 1..161.

Outputs (stdout, then JSON):
  - cross-check rows 1..161 of wider run vs depth-1000 run (must be identical)
  - giants (jump j = b[k]-b[k-1] > 1000) as (row, pre-jump b, jump, landing b)
  - landing floorings  (W - r - 1) - b[r-1]  for each giant row r
  - k* = first row with flooring < 1000
  - sequences: giant_rows, gaps, landing_blocks, giant_jumps
  - geometric vs linear least-squares fit over the 15 landing blocks
  - parity of giant rows (new convention k=1..300, old convention k=1..161)
  - serialized to code/out/pattern_finder_outputs/wider_giants.json
"""
import json, math

with open('code/out/wider_width_b_clean.json') as f:
    wide = json.load(f)
W = wide['num_primes']
bw = wide['b']                      # index r-1 = row r (1-based), r=1..300
depth = len(bw)
assertW = 16252325
assert W == assertW, (W, assertW)

with open('code/out/pattern_finder_outputs/b_genuine.txt') as f:
    old = [int(x) for x in f.read().split()]

# ---- cross-check rows 1..161 against the depth-1000 run ----
n_match = min(161, len(bw), len(old))
mismatches = [i + 1 for i in range(n_match) if bw[i] != old[i]]
print(f"cross-check rows 1..{n_match}: mismatches = {mismatches} "
      f"({'MATCH' if not mismatches else 'FAIL'})")

# ---- giants via step law: b increases (regeneration with jump > 0) ----
rows, pre, jumps, land = [], [], [], []
for k in range(1, depth):           # transitions row k -> k+1 (k = event row)
    j = bw[k] - bw[k - 1]
    if j > 1000:
        rows.append(k + 1)          # 1-based new-convention event row
        pre.append(bw[k - 1])
        jumps.append(j)
        land.append(bw[k])
gaps = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
print(f"giants (j>1000): {len(rows)}  rows={rows}")
print(f"gaps: {gaps}  max={max(gaps)}")
print(f"landing blocks: {land}")
print(f"jumps: {jumps}")

# ---- landing floorings and k* ----
floor = [(W - r - 1) - bw[r - 1] for r in range(1, depth + 1)]
kstar = next((r for r in range(1, depth + 1) if floor[r - 1] < 1000), None)
print(f"first row with flooring<1000: k* = {kstar}")
print(f"giant landing floorings (row, flooring): "
      f"{[(r, (W - r - 1) - bw[r - 1]) for r in rows]}")

# ---- exact fits: geometric (log b ~ a + m x) vs linear (b ~ a + m x) ----
n = len(land)
x = list(range(n))
logb = [math.log(v) for v in land]
def ls(xs, ys):
    m = len(xs); sx = sum(xs); sy = sum(ys); sxx = sum(v * v for v in xs)
    sxy = sum(a * b for a, b in zip(xs, ys))
    denom = m * sxx - sx * sx
    slope = (m * sxy - sx * sy) / denom
    inter = (sy - slope * sx) / m
    return slope, inter
def r2(xs, ys, slope, inter):
    ybar = sum(ys) / len(ys)
    ss_tot = sum((y - ybar) ** 2 for y in ys)
    ss_res = sum((y - slope * xx - inter) ** 2 for xx, y in zip(xs, ys))
    return 1 - ss_res / ss_tot
sg, ig = ls(x, logb)
sl, il = ls(x, land)
print(f"geometric: slope={sg:.6f} R2={r2(x, logb, sg, ig):.6f} "
      f"rate={math.exp(sg):.4f}/event")
print(f"linear   : slope={sl:.2f} R2={r2(x, land, sl, il):.6f}")
ratios = [land[i + 1] / land[i] for i in range(n - 1)]
print(f"consecutive landing ratios: {[f'{v:.3f}' for v in ratios]}")

# ---- parity profile ----
odd_new = [r for r in rows if r % 2 == 1]
print(f"new-convention giant rows parity: {len(odd_new)}/{len(rows)} odd, "
      f"even rows = {[r for r in rows if r % 2 == 0]}")
# old-convention giants (depth-1000): from b_genuine step law
old_rows = []
for k in range(1, len(old)):
    if old[k] - old[k - 1] > 1000:
        old_rows.append(k + 1)
odd_old = [r for r in old_rows if r % 2 == 1]
print(f"old-convention giant rows: {old_rows}; parity: "
      f"{len(odd_old)}/{len(old_rows)} odd; even rows = "
      f"{[r for r in old_rows if r % 2 == 0]}")

out = dict(W=W, depth=depth, kstar=kstar, giant_rows=rows, gaps=gaps,
           landing_blocks=land, giant_jumps=jumps,
           pre_jump_blocks=pre, landing_floorings=[(W - r - 1) - bw[r - 1]
                                                   for r in rows],
           ratios=[round(v, 6) for v in ratios])
with open('code/out/pattern_finder_outputs/wider_giants.json', 'w') as f:
    json.dump(out, f, indent=1)
print("wrote code/out/pattern_finder_outputs/wider_giants.json")