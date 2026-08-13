#!/usr/bin/env python3
"""Follow-up detail on regeneration events from blocks_depth1000.json (on-disk).

Adds: gap histogram, s(k) at regen rows, intruder trace during the three
longest live erosion runs, multiplicative ratios of the huge jumps, and the
'1.5-2x expansion' structure of major regenerations.
"""
import json
from collections import Counter

d = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = d["b"], d["s"], d["intruder"]
D = 1000

bl = lambda r: b[r - 1]
ss = lambda r: s[r - 1]
it = lambda r: intr[r - 1]
diff = {r: bl(r + 1) - bl(r) for r in range(1, D)}

regen = [r for r in range(1, D) if diff[r] >= 0]          # all in 1..161
rgset = set(regen)

# --- s at regen rows ---
print("s(k) at the 60 regen rows:", Counter(ss(r) for r in regen))
print("s(k) at 101 erosion rows (live):", Counter(ss(r) for r in range(1, 162) if diff[r] == -1))
# does regen coincide with s-run starts?
sch = [r for r in range(2, D + 1) if ss(r) != ss(r - 1)]   # k where s changes between k-1,k
print("s-change rows k (s(k)!=s(k-1)):", len(sch), sch[:30], "...")
print("regen rows that are also s-change rows:", sorted(set(regen) & set(sch)))

# --- gap histogram ---
gaps = [regen[i + 1] - regen[i] for i in range(len(regen) - 1)]
gc = Counter(gaps)
print("\ngap histogram (gaps between consecutive regen rows):", sorted(gc.items()),
      "n =", len(gaps))

# --- big jumps: ratios ---
big = [(r, diff[r], bl(r), bl(r + 1)) for r in regen if diff[r] >= 1000]
print("\nregenerations with jump >= 1000: k | jump | b(k) -> b(k+1) | ratio b(k+1)/b(k)")
for r, j, b0, b1 in big:
    print(f"  {r:4d} | {j:8d} | {b0:9d} -> {b1:9d} | {b1/b0:.3f}")
jumps = [diff[r] for r in regen]
over3 = [b1 / b0 for r, j, b0, b1 in big if b0 > 0]
print("...all >=1000 jumps have ratio > 1.5:", all(tr > 1.5 for tr in over3),
      "; ratios:", [f"{t:.2f}" for t in over3])

# --- intruder trace across the three longest live runs ---
runs = []
c_start, c_len = None, 0
for r in range(1, D):
    if diff[r] == -1:
        if c_len == 0:
            c_start = r
        c_len += 1
    else:
        if c_len:
            runs.append((c_start, c_len))
        c_len = 0
if c_len:
    runs.append((c_start, c_len))
live_runs = sorted([t for t in runs if t[0] + t[1] - 1 <= 161], key=lambda t: -t[1])
print("\nthree longest live erosion runs (start, len):", live_runs[:3])
for start, ln in live_runs[:3]:
    end = start + ln - 1
    print(f"\nrun k={start}..{end} (transitions {start}->...->{end+1}):")
    print("  k | b(k) | intruder(k)")
    for k in range(max(1, start - 1), min(162, end + 3)):
        print(f"  {k:4d} | {bl(k):9d} | {str(it(k)):>5s}")
    regen_k = min([r for r in range(1, 162) if r >= end + 1])
    print(f"  regeneration that ends it: k={regen_k}, jump {diff[regen_k]}")

# --- after a big jump, where does the new intruder come from ---
print("\nafter huge regenerations (jump>=1000), intruder(k+1):",
      sorted(Counter(v for r, j, _, _ in big if r + 1 <= D
                     for v in [it(r + 1)] if v is not None).items()))
print("after small regenerations (jump<1000), intruder(k+1):",
      sorted(Counter(v for r in regen if diff[r] < 1000
                     for v in [it(r + 1)] if v is not None).items()))

# --- rows where intruder == 6,8,... : does a regen EVER happen there? ---
for v in (4, 6, 8, 10, 12, 14):
    rows = [r for r in range(1, 162) if it(r) == v]
    nreg = sum(1 for r in rows if r in rgset)
    print(f"intruder={v:2d}: {len(rows):3d} rows, regen at {nreg:3d} of them")