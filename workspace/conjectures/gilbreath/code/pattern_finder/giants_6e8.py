#!/usr/bin/env python3
"""Giant-jump parity test at a wide sieve: primes to 6e8, rows to depth 400.

Question the run answers that the 2e7 depth-1000 and 3e8 depth-300 records
cannot: with the finite-width cap pushed out (W ~= 31.1M primes instead of
1.27M / 16.25M), do rows 239..400 contain a giant jump (j > 1000) whose
pre-jump row has ODD 0-based index other than 161?  At 2e7 the 13 giants sat
at 0-based rows 34,56,64,68,94,96,110,112,126,130,134,146,161 — the only odd
one was i=161, the capped width artifact; at 3e8 rows 162(ii) and 175 became
genuine giants at even 0-based rows and row 239 (even 0-based) was added, so
the regularity "giant pre-jump rows are even (0-based) except the cap
artifact" survived; this run tests it on fresh rows.

Mathematics: the conjecture is equivalent to A_k(1) in {0,2} for all k, i.e.
the leading {0,2} block (cols 1..b_k of row A_k) never vanishes.  Proved step
law: b_{k+1} >= b_k iff the boundary pair (A_k[b_k], A_k[b_k+1]) == (2,4);
else b_{k+1} = b_k - 1.  A regen event is such a (2,4)-event; a giant is an
event with jump j = b_{k+1} - b_k > 1000.  This program records only b_k per
row (one row live at a time), extracts events/giants, and reports k* = first
row whose block reaches the row's right edge (intruder None, b_k = W-k-1).

Exact integer arithmetic throughout (numpy int64 holds all values exactly;
entries are differences of primes <= 6e8).  No triangle is stored.

Complexity (state before running):
  time:  sieve O(N log log N) + rows O(D * W) elementwise int64 ops;
  space: sieve bytearray N bytes + ONE row (W int64) + masks; peak ~2 GB.
  No exponential time or space anywhere; it is a streaming row generator.

Oracle: b values of rows 1..161 must equal blocks_depth1000.json exactly and
rows 1..300 must equal wider_width_b_clean.json exactly (primes of the 2e7 /
3e8 sieves are the same columns of the 6e8 sieve, and those rows never reach
the 2e7/3e8 right edge in the shared regime).
"""
import json
import sys
import time
from math import isqrt

import numpy as np

LIMIT = 600_000_000
DEPTH = 400
GIANT = 1000

t0 = time.time()
# --- prime sieve (bytearray, one byte per odd-inclusive range: full 0..N) ---
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
r = isqrt(LIMIT)
for i in range(2, r + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
buf = np.frombuffer(sieve, dtype=np.uint8)
idx = np.nonzero(buf[2:])[0].astype(np.int64) + 2
del sieve, buf
W = int(len(idx))
print(f"sieve {LIMIT}: W = {W} primes in {time.time() - t0:.1f}s", flush=True)

# --- row iteration, one row live at a time ---
# b_list[k-1] = b_k = leading {0,2} block length of row A_k (1-based row k).
# Block occupies cols 1..b_k; row A_k has W - k columns (0-based 0..W-k-1);
# no intruder (block at right edge) iff b_k == (W-k) - 1.
b_list = []
intruder_list = []
k_star = None          # first 1-based row k with no intruder
k_near = None          # first k with flooring < 1000 (width-degradation caveat)
cur = idx
for k in range(1, DEPTH + 1):
    nxt = np.abs(np.diff(cur))
    n = int(len(nxt))
    # leading entry A_k(0) = |cur[0]-cur[1]|; block is cols 1..b
    arr = nxt[1:]
    mask = (arr == 0) | (arr == 2)
    bad = np.flatnonzero(~mask)
    bb = int(bad[0]) if bad.size else n - 1
    b_list.append(bb)
    # intruder = A_k[b_k+1] exists iff block does not reach the right edge
    if bb == n - 1:
        intruder_list.append(None)
        if k_star is None:
            k_star = k
            print(f"row {k}: NO INTRUDER (block reaches right edge, b={bb})",
                  flush=True)
    else:
        intruder_list.append(int(nxt[bb + 1]))
    floor = (W - k) - 1 - bb          # columns past the block on this row
    if k_near is None and bb != n - 1 and floor < 1000:
        k_near = k
        print(f"row {k}: flooring < 1000 (b={bb}, floor={floor})", flush=True)
    cur = nxt
    if k % 50 == 0:
        print(f"row {k}: b={bb} intruder={intruder_list[-1]} "
              f"({time.time() - t0:.0f}s)", flush=True)
print(f"rows done in {time.time() - t0:.1f}s", flush=True)
del cur

# --- oracle cross-checks against prior records ---
b10 = json.load(open("code/out/blocks_depth1000.json"))["b"]
bw = json.load(open("code/out/wider_width_b_clean.json"))["b"]
m1 = [i for i in range(min(161, len(b10))) if b_list[i] != b10[i]]
m2 = [i for i in range(min(300, len(bw))) if b_list[i] != bw[i]]
print(f"cross-check rows 1..161 vs 2e7 record: mismatches = {m1}", flush=True)
print(f"cross-check rows 1..300 vs 3e8 record: mismatches = {m2}", flush=True)

# --- events and giants (conventions as in giant_parity_significance.py) ---
# b[k-1] is row k (1-based).  Event at pre-jump row r (1-based): b[r] > b[r-1]
# (list index r), i.e. b_list[r-1] > b_list[r-2].  Jump j = difference.
events = [r for r in range(2, DEPTH + 1) if b_list[r - 1] > b_list[r - 2]]
giants = [(r, b_list[r - 1] - b_list[r - 2], b_list[r - 2], b_list[r - 1])
          for r in events if b_list[r - 1] - b_list[r - 2] > GIANT]
# r is 1-based; i0 = r - 1 is the table's 0-based index (matches bigjump table)
g_rows0 = [r - 1 for (r, _, _, _) in giants]
g_rows1 = [r for (r, _, _, _) in giants]
g_jumps = [j for (_, j, _, _) in giants]
g_pre = [bp for (_, _, bp, _) in giants]
g_land = [bl for (_, _, _, bl) in giants]
g_floor = [(W - (r - 1) - 2) - bl for (r, _, _, bl) in giants]  # 0-based i0
g_gaps = [g_rows1[t + 1] - g_rows1[t] for t in range(len(g_rows1) - 1)]

print(f"\nevents (any regen): {len(events)}   giants (j>{GIANT}): {len(giants)}")
print(f"k* (first no-intruder row): {k_star}")
print(f"first row with flooring < 1000: {k_near}")
print(f"giant pre-jump rows (1-based): {g_rows1}")
print(f"giant pre-jump rows (0-based): {g_rows0}")
print(f"giant pre-jump rows parity (0-based even/odd): "
      f"{['even' if r % 2 == 0 else 'ODD' for r in g_rows0]}")
odd0 = [r for r in g_rows0 if r % 2 == 1]
print(f"odd 0-based pre-jump rows among giants: {odd0}")
print(f"  -> odd 0-based giant row other than 161: "
      f"{[r for r in odd0 if r != 161] or 'NONE'}")
odd1 = [r for r in g_rows1 if r % 2 == 1]
print(f"odd 1-based pre-jump rows among giants: {odd1}")
print(f"  -> odd 1-based giant row other than 162: "
      f"{[r for r in odd1 if r != 162] or 'NONE'}")
print(f"inter-giant gaps (1-based rows, consecutive pre-jump rows): {g_gaps}")
print(f"landing blocks b_land: {g_land}")
print(f"jumps: {g_jumps}")
print(f"landing floorings (W-i0-2 - b_land): {g_floor}")
print(f"max jump this run: {max(g_jumps) if g_jumps else 0} at 1-based row "
      f"{g_rows1[g_jumps.index(max(g_jumps))] if g_jumps else '-'}")

# --- durable artifact for the run's records ---
out = {
    "limit": LIMIT, "num_primes": W, "depth": DEPTH,
    "k_star_no_intruder": k_star, "k_near_floor1000": k_near,
    "giants_1based_rows": g_rows1, "giants_0based_rows": g_rows0,
    "jumps": g_jumps, "landing_blocks": g_land, "landing_floors": g_floor,
    "inter_giant_gaps": g_gaps,
    "odd_0based_other_than_161": [r for r in odd0 if r != 161],
    "b": b_list,
}
with open("code/out/pattern_finder_outputs/giants_6e8.json", "w") as f:
    json.dump(out, f)
print(f"wrote code/out/pattern_finder_outputs/giants_6e8.json", flush=True)
print(f"total wall {time.time() - t0:.1f}s", flush=True)
sys.exit(0)