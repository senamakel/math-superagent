#!/usr/bin/env python3
"""Giant-jump analysis at sieve 1e9, depth 400 — the larger-run settlement run.

Questions the run settles that the 6e8 record (W = 31,324,703 primes) cannot:

  1. Does the 16th genuine giant exist?  At 6e8 the event at 1-based row 248
     (0-based 247) landed at the finite-width edge (floor = 0, b_land =
     W-248-1 = 31,324,454 = n-1, no intruder; k* = 248), so its jump of
     8,161,172 was a lower bound and rows 249+ were width-truncated.  With
     W = 50,847,534 the same row-248 block can extend past column 31.3M, so
     the true jump and landing block are measured — if the {0,2} run ends
     before the 1e9 row edge the 16th giant is genuine; if it reaches the
     1e9 edge the whole triangle is {0,2}-valued from row 248 on (GC would
     hold there forever by closure) and the giant is capped again.
  2. Its gap from the previous genuine giant (1-based 239): is it > 64
     (trend) or <= 64 (noise; the 64-row gap 175->239 stays the max)?
  3. Do the ratio bound gap_i/(j_i+1) and the geometric (log-linear) fit of
     landing blocks survive at landing b ~ 40M+?

Method: exact int64 streaming row generator (identical to giants_6e8.py),
one row live at a time.  Proved step law: b_{k+1} >= b_k iff the boundary
pair (A_k[b_k], A_k[b_k+1]) == (2,4); else b_{k+1} = b_k - 1.  A regen event
is a row where b increases; a giant is an event with jump j > 1000.
Flooring = (W - k - 1) - b on row k = W - i0 - 2 - b_land at a giant;
floor > 0 means the landing block ends strictly inside the finite row
(genuine measurement), floor == 0 means the width cap truncated the jump.

Complexity: sieve O(N log log N) time / N bytes; rows O(D*W) int64
elementwise ops / O(W) memory (peak ~2.2 GiB: 1 GB sieve + 407 MB prime idx
+ two live 407 MB rows after the sieve is freed).  No exponential anything.

Oracle: rows 1..247 must match the 6e8 record exactly (the shared genuine
regime; the 6e8 row-248 value is the capped one, so the 1e9 value is
expected to be larger — that single divergence is the cap artifact, not an
error); rows 1..161 must match the 2e7 depth-1000 record.  The geometric fit
is computed twice — numpy polyfit and an exact closed-form OLS over
Fraction sums of the same log values — and the two must agree.

Usage: python3 giants_1e9.py [LIMIT] [DEPTH] [outpath]   (defaults: 1e9, 400,
code/out/pattern_finder_outputs/giants_1e9.json — run with no arguments).
"""
import json
import os
import sys
import time
from fractions import Fraction
from math import comb, exp, isqrt, log

import numpy as np

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000_000
DEPTH = int(sys.argv[2]) if len(sys.argv) > 2 else 400
GIANT = 1000
OUTDIR = "code/out/pattern_finder_outputs"
OUTNAME = sys.argv[3] if len(sys.argv) > 3 else "giants_1e9.json"
PI_1E9 = 50_847_534

t0 = time.time()
# --- prime sieve (bytearray over full 0..N; identical structure to 6e8) ---
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
if LIMIT == 1_000_000_000:
    print(f"sieve {LIMIT}: W = {W} primes, pi(1e9) = {PI_1E9}, diff = {W - PI_1E9:+d} "
          f"in {time.time() - t0:.1f}s", flush=True)
else:
    print(f"sieve {LIMIT}: W = {W} primes in {time.time() - t0:.1f}s (smoke)", flush=True)

# --- row iteration, one row live at a time ---
# b_list[k-1] = b_k = leading {0,2} block length of row A_k (1-based row k).
# Row A_k has n = W - k columns (0-based 0..n-1); no intruder iff b == n-1.
b_list = []
intruder_list = []
floor_list = []
k_star = None          # first 1-based row k with no intruder
k_near = None          # first k with flooring < 1000 (width-degradation caveat)
cur = idx
for k in range(1, DEPTH + 1):
    nxt = np.abs(np.diff(cur))
    n = int(len(nxt))
    arr = nxt[1:]
    mask = (arr == 0) | (arr == 2)
    bad = np.flatnonzero(~mask)
    bb = int(bad[0]) if bad.size else n - 1
    b_list.append(bb)
    floor = n - 1 - bb                      # columns past the block on this row
    floor_list.append(floor)
    if bb == n - 1:
        intruder_list.append(None)
        if k_star is None:
            k_star = k
            print(f"row {k}: NO INTRUDER (block reaches right edge, b={bb}, floor={floor})",
                  flush=True)
    else:
        intruder_list.append(int(nxt[bb + 1]))
        if k_near is None and floor < 1000:
            k_near = k
            print(f"row {k}: flooring < 1000 (b={bb}, floor={floor})", flush=True)
    cur = nxt
    tm = f"  [{time.time() - t0:.0f}s]" if k % 50 == 0 else ""
    print(f"row {k}: b={bb} floor={floor} intruder={intruder_list[-1]}{tm}", flush=True)
print(f"rows done in {time.time() - t0:.1f}s", flush=True)
del cur

# --- oracle cross-checks against prior records ---
if os.path.exists("code/out/pattern_finder_outputs/giants_6e8.json"):
    b6 = json.load(open("code/out/pattern_finder_outputs/giants_6e8.json"))["b"]
    m_shared = [i for i in range(min(247, len(b6), len(b_list))) if b_list[i] != b6[i]]
    print(f"cross-check rows 1..247 (shared genuine regime) vs 6e8 record: "
          f"mismatches = {m_shared}", flush=True)
    m_strict = [i for i in range(min(248, len(b6), len(b_list))) if b_list[i] != b6[i]]
    b6r = b6[247] if len(b6) > 247 else None
    b1r = b_list[247] if len(b_list) > 247 else None
    print(f"cross-check rows 1..248 strict vs 6e8 record: mismatches = {m_strict} "
          f"(row 248: 6e8={b6r} [capped, = n-1 at 6e8 width], 1e9={b1r} — 1e9 "
          f"expected to exceed it iff the {0,2} block extends past the 6e8 edge)",
          flush=True)
else:
    print("cross-check vs 6e8 record: file missing", flush=True)
if os.path.exists("code/out/blocks_depth1000.json"):
    b10 = json.load(open("code/out/blocks_depth1000.json"))["b"]
    m1 = [i for i in range(min(161, len(b10), len(b_list))) if b_list[i] != b10[i]]
    print(f"cross-check rows 1..161 vs 2e7 depth-1000 record: mismatches = {m1}",
          flush=True)

# --- events and giants (conventions as in giants_6e8.py) ---
events = [r for r in range(2, DEPTH + 1) if b_list[r - 1] > b_list[r - 2]]
giants = [(r, b_list[r - 1] - b_list[r - 2], b_list[r - 2], b_list[r - 1])
          for r in events if b_list[r - 1] - b_list[r - 2] > GIANT]
g_rows1 = [r for (r, _, _, _) in giants]
g_rows0 = [r - 1 for (r, _, _, _) in giants]
g_jumps = [j for (_, j, _, _) in giants]
g_pre = [bp for (_, _, bp, _) in giants]
g_land = [bl for (_, _, _, bl) in giants]
g_floor = [W - r - 1 - bl for (r, _, _, bl) in giants]      # W - i0 - 2 - b_land
genuine = [fl > 0 for fl in g_floor]
g_gaps = [g_rows1[t + 1] - g_rows1[t] for t in range(len(g_rows1) - 1)]
n_g = len(giants)

print(f"\nevents (any regen): {len(events)}   giants (j>{GIANT}): {n_g}   "
      f"genuine (floor > 0): {sum(genuine)}")
print(f"k* (first no-intruder row): {k_star}   first row with flooring < 1000: {k_near}")
print("\nfull giant table (i = giant ordinal; row0 = 0-based pre-jump row; "
      "row1 = 1-based; gap_i = rows since previous giant):")
print(f"{'i':>3} {'row0':>4} {'row1':>4} {'jump':>11} {'b_pre':>11} {'b_land':>11} "
      f"{'floor':>11} {'gen':>4} {'gap_i':>6} {'gap/(j_i+1)':>12} {'gap/(j_prev+1)':>14}")
for t, (r, j, bp, bl) in enumerate(giants):
    gap = g_gaps[t - 1] if t >= 1 else None
    s_gap = f"{gap:>6}" if gap is not None else "     -"
    s_own = f"{gap / (j + 1):.4e}"