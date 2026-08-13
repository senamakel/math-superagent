#!/usr/bin/env python3
"""Extend the live (non-width-exhausted) regime with a wider sieve.

Question this run answers that the depth-1000 / sieve-20M record cannot:
does the (2,4)-event / giant-jump tail persist past row 161, when the row
width is 300M-sieve wide instead of 20M? Concretely:

  (i)   at what row k* does the block meet the finite width (intruder None)?
  (ii)  how many more regeneration events / giants (jump>1000) appear in
        rows 162..k*?
  (iii) empirical max gap between consecutive events with jump > J, in the
        extended live regime (the T(J) of the "gap between large jumps").
  (iv)  does every giant still land at a new all-time maximum of b?
  (v)   do the new giants continue the geometric growth of the landing
        blocks (compare with directive24's ×1.68/event)?

Exact integer arithmetic throughout (int64 numpy diffs of exact primes).
Oracle: first 161 block lengths must equal blocks_depth1000.json exactly.
Memory: sieve 300MB bytearray + ~4 x 15.4M int64 arrays ~= 1 GB peak.
Cost: ~30-60 s, 1 worker.
"""
import json
import time
from math import isqrt

import numpy as np

LIMIT = 300_000_000
DEPTH = 300

t0 = time.time()
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
r = isqrt(LIMIT)
for i in range(2, r + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
buf = np.frombuffer(sieve, dtype=np.uint8)
idx = np.nonzero(buf[2:])[0].astype(np.int64) + 2
del sieve, buf
P = int(len(idx))
print(f"sieve {LIMIT}: {P} primes in {time.time() - t0:.1f}s", flush=True)

cur = idx
b_list, s_list, intr = [], [], []
for k in range(1, DEPTH + 1):
    nxt = np.abs(np.diff(cur))
    n = len(nxt)
    arr = nxt[1:]
    mask = (arr == 0) | (arr == 2)
    bad = np.flatnonzero(~mask)
    bb = int(bad[0]) if bad.size else n - 1
    b_list.append(bb)
    s_list.append(int(nxt[1]))
    intr.append(int(nxt[bb + 1]) if bb + 1 <= n - 1 else None)
    cur = nxt
    if k % 40 == 0:
        print(f"row {k}: b={bb} intruder={intr[-1]} ({time.time() - t0:.0f}s)",
              flush=True)
print(f"rows done in {time.time() - t0:.1f}s", flush=True)

# ---- oracle: first 161 block lengths must match the depth-1000 record ----
rec = json.load(open("code/out/blocks_depth1000.json"))
mism = [(k + 1, b_list[k], rec["b"][k]) for k in range(161) if b_list[k] != rec["b"][k]]
print("oracle mismatches vs blocks_depth1000 (rows 1..161):", mism if mism else "none")

# ---- events and giants ----
events = []  # (row k, jump, b_{k-1})  for transitions k-1 -> k with b_k >= b_{k-1}
for k in range(2, DEPTH + 1):
    d = b_list[k - 1] - b_list[k - 2]
    if d >= 0:
        events.append((k, d, b_list[k - 2]))
genuine = [e for e in events if e[2] is not None or True]  # all rows have intruder? filter below
live = [e for e in events if intr[e[0] - 2] is not None]   # event row k must have intruder at row k-1
print(f"\nevents total: {len(events)}; events with intruder defined: {len(live)}")

k_star = next((k for k in range(1, DEPTH + 1) if b_list[k - 1] >= P - k - 1), None)
print(f"k* (first row with b_k >= P-k-1, no intruder): {k_star}")
print(f"genuine regime rows: 1..{k_star - 1 if k_star else DEPTH}")

live_events = [e for e in events if e[0] <= (k_star - 1 if k_star else DEPTH)]
giants = [e for e in live_events if e[1] > 1000]
print(f"\ngiants (jump>1000), live regime: {len(giants)}")
for (k, j, bk) in giants:
    print(f"  row {k:3d}: jump {j:8d}  b_k={bk:8d}  land={bk + j:8d}")

if len(giants) >= 2:
    gro = [g[0] for g in giants]
    gaps = [gro[i + 1] - gro[i] for i in range(len(gro) - 1)]
    print(f"  giant rows: {gro}")
    print(f"  gaps between giants: {gaps}  max = {max(gaps)}")

print("\n== threshold table T(J): max gap between live events with jump > J ==")
for J in (100, 300, 1000, 10000, 100000):
    rows = [e[0] for e in live_events if e[1] > J]
    if len(rows) < 2:
        print(f"J={J:>7}: rows {rows} count {len(rows)} max-gap n/a")
        continue
    gaps = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
    print(f"J={J:>7}: count {len(rows):2d}  max-gap {max(gaps)}  rows {rows}")

# ---- records ----
recmax = 0
recset, giant_no_rec = [], []
giant_rows = {g[0] for g in giants}
for (k, j, bk) in live_events:
    land = bk + j
    if land > recmax:
        recmax = land
        recset.append(k)
    elif k in giant_rows:
        giant_no_rec.append((k, land, recmax))
print(f"\nevents setting a new all-time max: {len(recset)} of {len(live_events)}")
print(f"giants NOT setting a record: {giant_no_rec or 'none'}")
print(f"new giants beyond row 161: {[g for g in giants if g[0] > 161]}")

# ---- geometric continuation: landing blocks of ALL giants ----
lands = [bk + j for (k, j, bk) in giants]
print("\nlanding blocks of giants (in order):", lands)
if len(lands) >= 3:
    import math
    xs = list(range(len(lands)))
    ln = [math.log(x) for x in lands]
    mx, my = sum(xs) / len(xs), sum(ln) / len(ln)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ln))
    slope = sxy / sxx
    ssr = sum((y - (my + slope * (x - mx))) ** 2 for x, y in zip(xs, ln))
    sst = sum((y - my) ** 2 for y in ln)
    r2 = 1 - ssr / sst
    print(f"geometric fit log(land) = a + m*x over {len(lands)} giants: "
          f"m={slope:.4f} R2={r2:.4f}  (per-event factor exp(m)={math.exp(slope):.3f})")

print("\nall s in {0,2}:", all(x in (0, 2) for x in s_list))
out = {"limit": LIMIT, "num_primes": P, "depth": DEPTH, "k_star": k_star,
       "b": b_list, "s": s_list, "intruder": intr}
with open("code/out/wider_width_b.json", "w") as f:
    json.dump(out, f)
print(f"\nwrote code/out/wider_width_b.json ({time.time() - t0:.1f}s total)")