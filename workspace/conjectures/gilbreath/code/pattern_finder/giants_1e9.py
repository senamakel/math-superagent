#!/usr/bin/env python3
"""Giant-jump analysis at sieve 1e9, depth 400 — the larger-run settlement run.

Questions the run settles that the 6e8 record (W = 31,324,703 primes) cannot:

  1. Does the 16th genuine giant exist?  At 6e8 the event at 1-based row 248
     (0-based 247) landed at the finite-width edge (floor = 0, b_land =
     W-248-1, no intruder; k* = 248), so its jump of 8,161,172 was a lower
     bound and rows 249+ were width-truncated.  With W = 50,847,534 the same
     row-248 block can extend past column 31.3M, so the true jump and landing
     block are measured — if the {0,2} run ends before the 1e9 row edge the
     16th giant is genuine; if it reaches the 1e9 edge the whole row is
     {0,2}-valued from 248 on (GC would hold there forever by closure) and
     the giant is capped again.
  2. Its gap from the previous genuine giant (1-based 239): is it > 64
     (trend) or <= 64 (noise; the 64-row gap 175->239 stays the max)?
  3. Do the ratio bound gap_i/(j_i+1) and the geometric (log-linear) fit of
     landing blocks survive at landing b ~ 40M+?

Method: exact int64 streaming row generator (identical to giants_6e8.py), one
row live at a time.  Proved step law: b_{k+1} >= b_k iff the boundary pair
(A_k[b_k], A_k[b_k+1]) == (2,4); else b_{k+1} = b_k - 1.  A regen event is a
row where b increases; a giant is an event with jump j > 1000.  Flooring =
(W - k - 1) - b on row k = W - i0 - 2 - b_land at a giant; floor > 0 means the
landing block ends strictly inside the finite row (genuine measurement),
floor == 0 means the width cap truncated the jump.

Complexity: sieve O(N log log N) time / N bytes; rows O(D*W) int64 elementwise
ops / O(W) memory (peak ~2.2 GiB: 1 GB sieve + 407 MB prime idx + one live
407 MB row; sieve and idx freed before the row loop).  No exponential
anything.

Oracle: rows 1..247 must match the 6e8 record exactly (the shared genuine
regime; the 6e8 row-248 value is the capped one, so the 1e9 row-248 is
expected to be larger — that single divergence is the cap artifact, not an
error); rows 1..161 must match the 2e7 depth-1000 record.  The geometric fit
is computed twice — numpy polyfit and an exact closed-form OLS over Fraction
sums of the same log values — and the two must agree.

Usage: python3 giants_1e9.py [LIMIT] [DEPTH] [outname]
Defaults: LIMIT=1000000000 DEPTH=400 OUT=giants_1e9.json (written to
code/out/pattern_finder_outputs/).  Smoke test: python3 giants_1e9.py 300 20
(no oracle cross-checks run at smoke size if the records' rows differ).
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
print(f"sieve {LIMIT}: W = {W} primes " +
      (f"(pi(1e9) = {PI_1E9}, diff {W - PI_1E9:+d})" if LIMIT == 1_000_000_000
       else "(smoke size)") + f" in {time.time() - t0:.1f}s", flush=True)

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
            print(f"row {k}: NO INTRUDER (block reaches right edge, b={bb}, "
                  f"floor={floor})", flush=True)
    else:
        intruder_list.append(int(nxt[bb + 1]))
        if k_near is None and floor < 1000:
            k_near = k
            print(f"row {k}: flooring < 1000 (b={bb}, floor={floor})", flush=True)
    cur = nxt
    tm = f"  [{time.time() - t0:.0f}s]" if k % 50 == 0 else ""
    print(f"row {k}: b={bb} floor={floor} intruder={intruder_list[-1]}{tm}",
          flush=True)
print(f"rows done in {time.time() - t0:.1f}s", flush=True)
del cur

# --- oracle cross-checks against prior records ---
print("\n--- oracle cross-checks ---", flush=True)
if os.path.exists(f"{OUTDIR}/giants_6e8.json"):
    b6 = json.load(open(f"{OUTDIR}/giants_6e8.json"))["b"]
    lo = min(247, len(b6), len(b_list))
    m_shared = [i + 1 for i in range(lo) if b_list[i] != b6[i]]
    print(f"rows 1..247 vs 6e8 record: mismatches = {m_shared} (must be [])",
          flush=True)
    if len(b_list) > 247 and len(b6) > 247:
        print(f"row 248 vs 6e8: 6e8={b6[247]} (capped), 1e9={b_list[247]}",
              flush=True)
else:
    print("6e8 record missing; cross-check skipped", flush=True)
if os.path.exists("code/out/blocks_depth1000.json"):
    b10 = json.load(open("code/out/blocks_depth1000.json"))["b"]
    lo = min(161, len(b10), len(b_list))
    m1 = [i + 1 for i in range(lo) if b_list[i] != b10[i]]
    print(f"rows 1..161 vs 2e7 depth-1000 record: mismatches = {m1} (must be [])",
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
g_floor = [W - r - 1 - bl for (r, _, _, bl) in giants]   # W - i0 - 2 - b_land
genuine = [fl > 0 for fl in g_floor]
g_gaps = [g_rows1[t + 1] - g_rows1[t] for t in range(len(g_rows1) - 1)]
n_g = len(giants)

print(f"\n--- summary ---")
print(f"events (any regen): {len(events)}   giants (j>{GIANT}): {n_g}   "
      f"genuine (floor > 0): {sum(genuine)}")
print(f"k* (first no-intruder row): {k_star}   "
      f"first row with flooring < 1000: {k_near}")
print(f"W = {W}; note floor uses W - row1 - 1 - b (0-based i0 = row1 - 1)")

print("\n--- full giant table ---")
print(f"{'i':>3} {'row0':>4} {'row1':>4} {'jump':>11} {'b_pre':>11} "
      f"{'b_land':>11} {'floor':>11} {'gen':>4} {'gap_i':>6} "
      f"{'gap/(j_i+1)':>12} {'gap/(j_prev+1)':>14}")
for t, (r, j, bp, bl) in enumerate(giants):
    gap = g_gaps[t - 1] if t >= 1 else None
    s_gap = f"{gap:>6}" if gap is not None else "     -"
    s_own = f"{gap / (j + 1):.4e}" if gap is not None else "         -"
    s_prev = (f"{gap / (g_jumps[t - 1] + 1):.4e}" if t >= 1 and gap is not None
              else "             -")
    print(f"{t:>3} {r - 1:>4} {r:>4} {j:>11} {bp:>11} {bl:>11} "
          f"{g_floor[t]:>11} {'Y' if genuine[t] else 'N':>4} {s_gap} "
          f"{s_own} {s_prev}")

# --- things the run is asked to settle, in one place ---
print("\n--- settlements ---")
if n_g:
    print(f"16th giant (i=15): row0={g_rows0[-1]} row1={g_rows1[-1]} "
          f"jump={g_jumps[-1]} b_land={g_land[-1]} floor={g_floor[-1]} "
          f"genuine={genuine[-1]}")
    if len(g_gaps) >= 1:
        print(f"gap from previous giant (row1 {g_rows1[-2]} -> {g_rows1[-1]}): "
              f"{g_gaps[-1]}  -> {'TREND (> 64)' if g_gaps[-1] > 64 else 'NOISE (<= 64)'}")
    print(f"max gap over all giants: {max(g_gaps)} at gap index "
          f"{g_gaps.index(max(g_gaps))} (between giants {g_gaps.index(max(g_gaps))} "
          f"and {g_gaps.index(max(g_gaps)) + 1}, rows1 {g_rows1[g_gaps.index(max(g_gaps)) - 1]}"
          f"..{g_rows1[g_gaps.index(max(g_gaps))]})")
    print(f"max ratio gap_i/(j_i+1): {max(g/(j + 1) for g, j in zip(g_gaps, g_jumps[1:])):.4e}")
    print(f"min ratio gap_i/(j_i+1): {min(g/(j + 1) for g, j in zip(g_gaps, g_jumps[1:])):.4e}")
    print(f"ratio > 0.1 rows: "
          f"{[t + 1 for t, (g, j) in enumerate(zip(g_gaps, g_jumps[1:])) if g/(j+1) > 0.1]}")

# parity of 0-based pre-jump rows, with exact binomial arithmetic
odd0 = [r for r in g_rows0 if r % 2 == 1]
n_odd = len(odd0)
print(f"\n--- parity of 0-based pre-jump rows ---")
print(f"0-based rows: {g_rows0}")
print(f"odd 0-based among {n_g} giants (j > 1000): {odd0}")
print(f"other than 161/capped: {[r for r in odd0 if r not in (161,)] or 'NONE'}")
# H0: each giant's pre-jump 0-based row is uniform over 0..DEPTH-1 (parity
# exactly 1/2 since DEPTH = 400 is even), independent across giants.  The
# task's specified tail is P(<= 1 odd row) = (C(n,1)+C(n,0)) / 2^n.
p_le1 = Fraction(comb(n_g, 1) + comb(n_g, 0), 2 ** n_g)
print(f"p(<=1 odd 0-based row | {n_g} giants, uniform parity H0) "
      f"= (C({n_g},1)+C({n_g},0))/2^{n_g} = {p_le1} = {float(p_le1):.4g}")

# --- geometric vs linear fits on landing blocks of GENUINE giants ---
print(f"\n--- fits on landing blocks, genuine giants only "
      f"({sum(genuine)} points of {n_g}) ---")
rows_g = [r - 1 for r, _, _, _ in giants]
grow_g = [r for t, (r, _, _, _) in enumerate(giants) if genuine[t]]
land_g = [bl for t, bl in enumerate(g_land) if genuine[t]]
if sum(genuine) >= 2:
    y = np.log2(np.array(land_g, dtype=np.float64))
    xg = np.array(grow_g, dtype=np.float64)
    slope, intercept = np.polyfit(xg, y, 1)      # numpy OLS, deg 1
    resid = y - (slope * xg + intercept)
    r2 = 1.0 - float(np.sum(resid * resid) / np.sum((y - y.mean()) ** 2))
    print(f"numpy log2 OLS: slope={slope:.6f} intercept={intercept:.4f} "
          f"r2={r2:.6f}  (doubling every {1/abs(slope):.2f} rows)")
    xx = xg.tolist()
    # exact closed-form OLS over Fractions of the same (x, log2 b) points;
    # yv copies the doubles exactly, so both fits use identical data.
    isum = sum(Fraction(int(x)) for x in xx) / len(xx)
    yv = [Fraction(yi) for yi in y.tolist()]     # exact copy of the doubles
    ybar = sum(yv) / len(yv)
    Sxy = sum((Fraction(int(x)) - isum) * (yy - ybar) for x, yy in zip(xx, yv))
    Sxx = sum((Fraction(int(x)) - isum) ** 2 for x in xx)
    slope_f = Sxy / Sxx
    inter_f = ybar - slope_f * isum
    resid_f = [yy - (slope_f * Fraction(int(x)) + inter_f) for x, yy in zip(xx, yv)]
    ss_res = sum(rr * rr for rr in resid_f)
    ss_tot = sum((yy - ybar) * (yy - ybar) for yy in yv)
    r2_f = 1 - ss_res / ss_tot
    print(f"exact Fraction OLS: slope={float(slope_f):.6f} "
          f"intercept={float(inter_f):.4f} r2={float(r2_f):.6f}")
    print(f"agreement numpy vs exact: |slope diff| = "
          f"{abs(slope - float(slope_f)):.2e} (must be ~0)")
    yrel = np.diff(y)
    print(f"per-giant log2 b_land increments: {[f'{v:.3f}' for v in yrel]}")
    print(f"relative growth factors b_land[i+1]/b_land[i]: "
          f"{[f'{g_land[t + 1] / g_land[t]:.3f}' for t in range(len(g_land) - 1)]}")
    # --- linear model for comparison (b vs row0, plain OLS) ---
    s_lin, i_lin = np.polyfit(xg, np.array(land_g, dtype=np.float64), 1)
    resid_lin = np.array(land_g, dtype=np.float64) - (s_lin * xg + i_lin)
    ss_res_lin = float(np.sum(resid_lin * resid_lin))
    ybar_all = float(np.mean(land_g))
    ss_tot_all = float(np.sum((np.array(land_g, dtype=np.float64) - ybar_all) ** 2))
    r2_lin = 1 - ss_res_lin / ss_tot_all
    print(f"linear b vs row0 OLS: slope={s_lin:.3f} intercept={i_lin:.3f} "
          f"r2={r2_lin:.6f}")
else:
    print("fewer than 2 genuine giants: fits skipped")

# --- durability: write giants_1e9.json ---
os.makedirs(OUTDIR, exist_ok=True)
out = {
    "limit": LIMIT, "num_primes": W, "depth": DEPTH, "pi_1e9": PI_1E9,
    "k_star_no_intruder": k_star, "k_near_floor1000": k_near,
    "giants_1based_rows": g_rows1, "giants_0based_rows": g_rows0,
    "jumps": g_jumps, "prejump_blocks": g_pre, "landing_blocks": g_land,
    "landing_floors": g_floor, "genuine": genuine, "inter_giant_gaps": g_gaps,
    "max_gap": max(g_gaps) if g_gaps else None,
    "gap_of_last": g_gaps[-1] if g_gaps else None,
    "ratios_gap_over_jplus1": [g / (j + 1) for g, j in zip(g_gaps, g_jumps[1:])],
    "odd_0based_rows": odd0,
    "b": b_list,
    "floor_list": floor_list,
    "fits_genuine": {"rows": grow_g, "landing_blocks": land_g,
                     "log2_slope_numpy": float(slope), "log2_intercept_numpy": float(intercept),
                     "log2_slope_fraction": float(slope_f), "r2_numpy": float(r2),
                     "r2_fraction": float(r2_f)},
}
with open(os.path.join(OUTDIR, OUTNAME), "w") as f:
    json.dump(out, f)
print(f"wrote {OUTDIR}/{OUTNAME}", flush=True)
print(f"total wall {time.time() - t0:.1f}s", flush=True)
sys.exit(0)