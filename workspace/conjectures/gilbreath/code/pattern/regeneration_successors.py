#!/usr/bin/env python3
"""Final verification of regeneration successor patterns (on-disk JSON only)."""
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

# 1. jump-0 stalls: is row k+1 always a regen row?
j0 = [r for r in regen if diff[r] == 0]
succ_ok = all(r + 1 in rgset for r in j0)
print(f"jump-0 stalls: {len(j0)}; k+1 also regen: {succ_ok}")
print("  stall rows:", j0)

# 2. after-regen successor by intruder(k+1):
#    if intruder(k+1)==4 then next event is regen; if >=6 it is erosion
c = Counter()
for k in regen:
    y1 = it(k + 1)
    if k + 1 >= D:
        continue
    ev = "regen" if (k + 1) in rgset else "erosion"
    c[(str(y1), ev)] += 1
print("after-regen (intruder(k+1), event at k+1):", sorted(c.items()))

# 3. max consecutive non-regen rows inside intruder==4 regions (x=0 runs)
best = cur = 0
for k in range(1, LIVE + 1):
    if it(k) == 4 and k not in rgset:
        cur += 1
        best = max(best, cur)
    else:
        cur = 0
print(f"max consecutive non-regen rows with intruder=4 (x=0 runs): {best}")

# 4. after regen rows with intruder(k+1) >= 6: how long until next 4?
for k in regen:
    y1 = it(k + 1)
    if y1 is not None and y1 >= 6:
        # rows until intruder is 4 again (or regen)
        j = k + 1
        while j <= LIVE and it(j) not in (4,):
            j += 1
        print(f"  regen at k={k:4d} -> y(k+1)={y1}, next y=4 at k={j} "
              f"(after {j-(k+1)} rows), drain: "
              f"{[it(x) for x in range(k+1, min(j+1, LIVE+1))]}")

# 5. global invariants double-check
print("b>=2 for all k:", min(b) >= 2, "| b==2 exactly at k=1:",
      [k + 1 for k in range(D) if b[k] == 2])
print("all regen k <= 161:", all(k <= 161 for k in regen))
print("all y(k) for k<=161 in {4,6,8,10,12,14}:",
      set(it(k) for k in range(1, LIVE + 1)))
print("y monotone non-increasing over live erosion stretches: check every pair")
mono = all(it(k + 1) <= it(k)
           for k in range(1, LIVE)
           if diff[k] == -1 and it(k) is not None and it(k + 1) is not None)
print("  monotone:", mono)

# 6. ASCII histogram of jumps and gaps for the note
jumps = [diff[r] for r in regen]
import math
def hist(vals, buckets):
    out = []
    for lo, hi, name in buckets:
        n = sum(1 for v in vals if lo <= v < hi)
        out.append(f"{name:>11s}: {'#' * n} ({n})")
    return "\n".join(out)
print("\njump histogram (60 events):")
print(hist(jumps, [(0, 1, "0"), (1, 2, "1"), (2, 10, "2-9"),
                   (10, 100, "10-99"), (100, 1000, "100-999"),
                   (1000, 10000, "1000-9999"), (10000, 100000, "10^4-10^5"),
                   (100000, 1 << 60, ">=10^5")]))
gaps = [regen[i + 1] - regen[i] for i in range(len(regen) - 1)]
print("gap histogram (59 gaps):")
print(hist(gaps, [(1, 2, "1"), (2, 3, "2"), (3, 4, "3"), (4, 5, "4"),
                  (5, 6, "5"), (6, 10, "6-9"), (10, 15, "10-14")]))

# 7. regen at k AND k+1 both regen: how many pairs of consecutive regen rows
pairs = sum(1 for k in regen if k + 1 in rgset)
print(f"\nconsecutive regen pairs (k, k+1 both regen): {pairs} of {len(regen)} events "
      f"(={pairs}/{len(regen)-1} of event adjacencies)")