#!/usr/bin/env python3
"""Extract the GENUINE (infinite-row) subsequences from blocks_depth1000.json
and dump them for the sequence tools + exact structural checks.

Kabs = first k where the leading {0,2} block covers the entire finite window
(W-k-1 entries); from k=Kabs on, b(k)=W-k-1 is a finite-width artifact and
tells us nothing about the infinite row. Only k=1..Kabs-1 are genuine.

Prints: b, s (0/2), bits s/2, intruder, diffs, erosion runs (start, length,
initial intruder y0, initial last-block-entry x0), regen events, and the
sliding-window XOR-track prediction of x during erosion runs (exact check).
"""
import json
from collections import Counter

with open("code/out/blocks_depth1000.json") as f:
    d = json.load(f)

W = d["num_primes"]
b = d["b"]
s = d["s"]
intr = d["intruder"]
D = d["D"]

# Kabs = first k with block covering full window: b(k) == W - k - 1
Kabs = None
for k in range(1, D + 1):
    if b[k - 1] == W - k - 1:
        Kabs = k
        break
print(f"W={W} D={D} Kabs={Kabs}  (genuine rows: k=1..{Kabs-1})")
assert Kabs is not None

bg = b[:Kabs - 1]
sg = s[:Kabs - 1]
ig = intr[:Kabs - 1]
bits = [x // 2 for x in sg]

print("genuine b(1..%d) = %s" % (len(bg), bg))
print("genuine s(1..%d) = %s" % (len(sg), sg))
print("genuine bits s/2 = %s" % bits)
print("genuine intruders = %s" % ig)

diffs = [bg[i + 1] - bg[i] for i in range(len(bg) - 1)]
print("diffs  b(k+1)-b(k) over genuine k: min=%d max=%d" % (min(diffs), max(diffs)))
print("erosion steps (diff==-1): %d of %d transitions" %
      (sum(1 for x in diffs if x == -1), len(diffs)))
print("regen events (diff>=0): %d of %d transitions" %
      (sum(1 for x in diffs if x >= 0), len(diffs)))
print("diff==0 events:", sum(1 for x in diffs if x == 0))

# erosion runs: maximal consecutive diff==-1, with start k, length, and the
# intruder+last-block-entry at the row BEFORE the run starts (row start-1)
runs = []
cur, start = 0, None
for i, x in enumerate(diffs):
    kk = i + 1  # transition kk -> kk+1
    if x == -1:
        if cur == 0:
            start = kk
        cur += 1
    else:
        if cur:
            # run covers transitions start..start+cur-1, i.e. rows
            # start-1 ... start+cur-1; initial row r0 = start-1
            r0 = start - 1
            y0 = ig[r0] if r0 < len(ig) and ig[r0] is not None else None
            x0 = None
            runs.append((r0, cur, y0, x0))
        cur = 0
if cur:
    r0 = start - 1
    y0 = ig[r0] if ig[r0] is not None else None
    runs.append((r0, cur, y0, None))
print("erosion runs (r0=initial row, L=length, y0=intruder at r0):")
for r in runs:
    print("   ", r)

# XOR-track check: during an erosion run starting at row r0 with block length
# b0 = b(r0), x at the end of step t (row r0+t, position b0-t) should equal the
# Pascal-mod-2 (XOR) combination of block bits A_{r0}(b0-t .. b0) = bits of row
# r0 at positions b0-t..b0. We don't have the full rows here (JSON only has
# b, s, intruder), so the full track check is done in a separate re-run that
# recomputes rows. Here we only report run geometry.
print("run length distribution:", Counter(r[1] for r in runs))
print("max genuine run length:", max(r[1] for r in runs))
print("min b over genuine k>=2:", min(bg[1:]), "at k=", bg[1:].index(min(bg[1:])) + 2)

# save for sequence tools
out = {
    "W": W, "Kabs": Kabs, "genuine_rows": Kabs - 1,
    "b": bg, "s": sg, "bits": bits, "intruder": ig,
    "diffs": diffs, "runs": runs,
}
with open("code/out/genuine_sequences.json", "w") as f:
    json.dump(out, f)
print("wrote code/out/genuine_sequences.json")