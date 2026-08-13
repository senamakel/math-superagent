#!/usr/bin/env python3
"""Last facts for the regeneration note (on-disk JSON only)."""
import json
from collections import Counter

d = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = d["b"], d["s"], d["intruder"]
D = 1000
bl = lambda r: b[r - 1]
it = lambda r: intr[r - 1]
diff = {r: bl(r + 1) - bl(r) for r in range(1, D)}
regen = sorted(r for r in range(1, D) if diff[r] >= 0)
rgset = set(regen)
LIVE = 161

# A. Every row with intruder==4 that ends a run: is it a regen row?
runs4 = []
cur = []
for k in range(1, LIVE + 1):
    if it(k) == 4:
        cur.append(k)
    else:
        if cur:
            runs4.append(cur)
        cur = []
if cur:
    runs4.append(cur)
print("Every 4-run's last row is a regen row:", all(r[-1] in rgset for r in runs4))

# B. Distinct run-interior values: within a 4-run, are b's and s's arbitrary?
for r in runs4:
    if len(r) >= 4:
        print(f"  4-run k={r[0]}..{r[-1]} len {len(r)}: interior b values "
              f"{[bl(k) for k in r[1:-1]]} s {[None]}")
        # s at these rows
        print(f"    s interior: {[None]}")

# C. every erosion run: how often does the intruder at run start == 4?
eruns = []
c_start, c_len = None, 0
for k in range(1, D):
    if diff[k] == -1:
        if c_len == 0:
            c_start = k
        c_len += 1
    else:
        if c_len:
            eruns.append((c_start, c_len))
        c_len = 0
if c_len:
    eruns.append((c_start, c_len))
live_er = [t for t in eruns if t[0] + t[1] - 1 <= LIVE]
starts = Counter(it(t[0]) for t in live_er)
print("intruder at start of live erosion runs:", sorted(starts.items()))

# D. the three long tall cycles: rows where y in {10,12,14}
print("\nrows with tall intruder y>=10:")
for k in range(1, LIVE + 1):
    if it(k) is not None and it(k) >= 10:
        print(f"  k={k:3d} y={it(k):2d} b={bl(k):9d} regen={'k' in [str(r) for r in regen] and k in rgset}")

# E. the y-drain staircase: are the drops exactly -2 each erosion step?
drops = Counter()
for k in range(1, LIVE):
    if diff[k] == -1 and it(k) is not None and it(k + 1) is not None:
        drops[it(k) - it(k + 1)] += 1
print("erosion-step y drops (y(k)-y(k+1)):", sorted(drops.items()))

# F. does b ever go below 7 after k>=2? and near-misses: min b(k) for k>=3
print("min b over k>=3:", min(bl(k) for k in range(3, D + 1)),
      "at k =", [k for k in range(3, D + 1) if bl(k) == min(bl(x) for x in range(3, D + 1))][:10])
print("min b over k>=10:", min(bl(k) for k in range(10, D + 1)))
print("min b over k>=40:", min(bl(k) for k in range(40, D + 1)))
print("min b over k>=100:", min(bl(k) for k in range(100, D + 1)))
print("min b over k>=150:", min(bl(k) for k in range(150, D + 1)))

# G. confirm s at the 4-run interiors (regen rows with jump 0)
print("\nstall rows s values:", [(k, s[k - 1]) for k in regen if diff[k] == 0])