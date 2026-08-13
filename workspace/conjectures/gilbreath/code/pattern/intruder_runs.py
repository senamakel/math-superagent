#!/usr/bin/env python3
"""Intruder-run and drain-stair statistics, from blocks_depth1000.json on disk."""
import json
from collections import Counter

d = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = d["b"], d["s"], d["intruder"]
D = 1000
bl = lambda r: b[r - 1]
it = lambda r: intr[r - 1]
diff = {r: bl(r + 1) - bl(r) for r in range(1, D)}
regen = set(r for r in range(1, D) if diff[r] >= 0)
LIVE = 161

# --- maximal runs of rows with intruder == 4 in live regime ---
rows = list(range(1, LIVE + 1))
runs4 = []
cur = []
for k in rows:
    if it(k) == 4:
        cur.append(k)
    else:
        if cur:
            runs4.append(cur)
        cur = []
if cur:
    runs4.append(cur)

print(f"intruder==4 runs in k=1..{LIVE}: n={len(runs4)}, lengths=",
      sorted(Counter(len(r) for r in runs4).items()))
bad_end = [r for r in runs4 if r[-1] not in regen]
print(f"runs whose last row is NOT a regen row: n={len(bad_end)}")
for r in runs4:
    last = r[-1]
    after = it(last + 1) if last + 1 <= D else None
    print(f"  run k={r[0]}..{r[-1]} len={len(r)} "
          f"(rows: {[bl(x) for x in r]}) ends regen={last in regen} "
          f"jump={diff[last] if last in regen else '-'} "
          f"after-intruder={after}")

# inside a 4-run, every non-final row is non-regen?
inside_nonregen = sum(1 for r in runs4 for k in r[:-1] if k not in regen)
inside_total = sum(len(r) - 1 for r in runs4)
print(f"non-final rows of 4-runs that are regen rows: "
      f"{inside_total - inside_nonregen} of {inside_total}")

# --- y-drain steps: among live erosion steps, how often does y change? ---
# y(k+1) = |x-y| with x in {0,2}: y drops by 2 iff x==2; else y unchanged.
drain = Counter()
for k in range(1, LIVE):
    if diff[k] == -1 and it(k) is not None:
        y0, y1 = it(k), it(k + 1)
        drain[(y0, y1)] += 1
print("\nlive erosion steps by (y_in, y_out):", sorted(drain.items()))
# dwell per intruder value
dwell = Counter()
for k in range(1, LIVE + 1):
    y = it(k)
    if y is not None:
        dwell[y] += 1
print("rows per intruder value (live):", sorted(dwell.items()))
steps = Counter()
for k in range(1, LIVE):
    if diff[k] == -1 and it(k) is not None:
        steps[it(k)] += 1
print("erosion steps originating at intruder y:", sorted(steps.items()))

# --- after-regen intruder vs jump size ---
print("\nafter-regen intruder by jump size class:")
for lo, hi, name in [(0, 1, "0"), (1, 10, "1-9"), (10, 1000, "10-999"),
                     (1000, 1 << 60, ">=1000")]:
    c = Counter(v for k in regen if lo <= diff[k] < hi and k + 1 <= D
                for v in [it(k + 1)] if v is not None)
    print(f"  jump {name:>6s}: {sorted(c.items())} n={sum(c.values())}")

# --- b at the end of each 4-run (regen base) vs jump ---
print("\nregen base b(k) vs jump:")
print("  base values:", [bl(r[-1]) for r in runs4])
print("  jumps:", [diff[r[-1]] for r in runs4])

# --- smallest distinct b values ever ---
small = sorted({bl(k) for k in range(1, D + 1) if bl(k) < 2000})
print("\ndistinct b values < 2000:", small)
print(f"b < 2000 for rows: n={sum(1 for k in range(1, D+1) if bl(k) < 2000)}")