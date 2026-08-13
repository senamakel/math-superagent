#!/usr/bin/env python3
"""Directive 30: step-6 ratio bound table for Gilbreath giants (sieve 6e8).

Consumes the existing 6e8 extraction
(code/out/pattern_finder_outputs/giants_6e8.json).  NO new sieve; 1 worker;
pure analysis.  State: W = 31,324,703 primes (pi(6e8)), depth 400,
k* (first no-intruder row, 1-based) = 248.

Mathematics: the step law (proved, research/notes/step_law_proved.md) gives
b_{k+1} = b_k - 1 unless the boundary pair (A_k[b_k], A_k[b_k+1]) == (2,4),
in which case b_{k+1} = b_k + j_k (a regen event; jump j_k).  A giant is a
regen event with jump j > 1000.  The step-6 ratio bound under test: the
row-gap g_i between consecutive giant pre-jump rows stays below j_i + 1
(ratio bound) and below b_land_i - 1 (cumulative margin), so the block
cannot die inside any inter-giant gap.

Flooring convention (matches giants_6e8.py and the "1-based row 239 lands at
b=23163290 with flooring 8161173" convention): for a giant at 0-based
pre-jump row r with landing block b_land,
    flooring = W - (1-based landing row) - 1 - b_land
             = W - (r+1) - 1 - b_land = W - r - 2 - b_land,
the number of columns past the landing block on the landing row.
flooring == 0 means the block meets the row's right edge: the width
artifact (at k*), excluded before any statistics.

Complexity: reads one JSON (O(n_giants)), constant-time arithmetic in W.
No exponential time or space anywhere; no search over the row data.
"""
import json
import math
from fractions import Fraction

import numpy as np

SRC = "code/out/pattern_finder_outputs/giants_6e8.json"
OUT_TXT = "code/out/step6_ratio_table.captured.txt"
OUT_JSON = "code/out/step6_ratio_table.json"

W = 31_324_703          # pi(6e8)
DEPTH = 400

data = json.load(open(SRC))
assert data["num_primes"] == W, (data["num_primes"], W)
assert data["depth"] == DEPTH

rows0 = list(data["giants_0based_rows"])      # 0-based pre-jump rows
jumps = list(data["jumps"])
bland = list(data["landing_blocks"])          # block length after the jump
floors = list(data["landing_floors"])         # as stored
kstar = data["k_star_no_intruder"]            # first 1-based no-intruder row

print("=" * 92)
print("STEP-6 RATIO BOUND TABLE  (Directive 30)  -- Gilbreath giants, sieve 6e8")
print(f"W = {W} primes (pi(6e8))   depth = {DEPTH}   k* (first no-intruder row, "
      f"1-based) = {kstar}")
print(f"source: {SRC}   (no new sieve, 1 worker)")
print("=" * 92)

# ----------------------------------------------------------------- step 1
# Recompute flooring independently of the stored column to check ourselves:
# flooring = W - (1-based landing row) - 1 - b_land, 1-based landing row = r+1.
calc_floor = [W - (r + 1) - 1 - b for r, b in zip(rows0, bland)]
assert calc_floor == floors, "recomputed flooring disagrees with stored JSON"
print("\n--- Step 1: all 16 giant events (0-based pre-jump row, landing block, "
      "jump, flooring) ---")
print(f"{'#':>2} {'row(0b)':>7} {'row(1b)':>7} {'b_land':>10} {'jump':>10} "
      f"{'flooring':>10}")
for t, (r, b, j, f) in enumerate(zip(rows0, bland, jumps, floors)):
    print(f"{t:>2} {r:>7} {r + 1:>7} {b:>10} {j:>10} {f:>10}")

# ----------------------------------------------------------------- step 2
art_idx = [t for t, f in enumerate(floors) if f == 0]
assert len(art_idx) == 1, f"expected exactly one flooring==0 entry, got {art_idx}"
t_art = art_idx[0]
row_art = rows0[t_art]
print("\n--- Step 2: exclude the width artifact ---")
print(f"excluded 0-based pre-jump row {row_art} (1-based row {row_art + 1}): "
      f"flooring == 0.  This row is k* = {kstar}: b_land = {bland[t_art]} = "
      f"W - {row_art + 1} - 1 = {W - (row_art + 1) - 1}, the block reaches the "
      f"row's right edge, so its jump {jumps[t_art]} is a finite-width "
      f"truncation, not genuine dynamics (true jump >= {jumps[t_art] + 1}).")
surv_t = [t for t in range(len(rows0)) if t != t_art]
sr = [rows0[t] for t in surv_t]
sb = [bland[t] for t in surv_t]
sj = [jumps[t] for t in surv_t]
sf = [floors[t] for t in surv_t]
print(f"surviving giants: {len(sr)} (rows {sr[0]}..{sr[-1]})")

# ----------------------------------------------------------------- step 3
expected_rows = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161,
                 174, 238]
sg = [sr[t + 1] - sr[t] for t in range(len(sr) - 1)]   # gaps, derived from rows
expected_gaps = [22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15, 13, 64]
print("\n--- Step 3: assert survivor list and gaps (operator's worked "
      "examples) ---")
ok_rows = sr == expected_rows
ok_gaps = sg == expected_gaps
print(f"surviving 15 0-based rows == {expected_rows}: "
      f"{'PASS' if ok_rows else 'FAIL'}")
print(f"surviving rows:                                        {sr}")
print(f"14 gaps == {expected_gaps}: {'PASS' if ok_gaps else 'FAIL'}")
print(f"gaps:                                                  {sg}")
assert ok_rows and ok_gaps, "worked-example assertion failed"

# ----------------------------------------------------------------- step 4
t238 = sr.index(238)
b238 = sb[t238]
f238 = sf[t238]
print("\n--- Step 4: row-238 confirmation (0-based) ---")
print(f"row 238: landing b = {b238}, flooring = {f238} (must be > 1000, "
      f"~8.16M)")
assert b238 == 23_163_290 and f238 == 8_161_173
print(f"flooring = W - (239) - 1 - b_land = {W} - 239 - 1 - {b238} = {f238}")
print(f"row 238 genuine: {'yes' if f238 > 1000 and 238 < kstar - 1 else 'no'} "
      f"(flooring >> 0 and well inside the k*={kstar} edge)")

# ----------------------------------------------------------------- step 5
print("\n--- Step 5: ratio table (14 gap rows; last giant's forward gap "
      "unknown -> --) ---")
hdr = (f"{'giant':>5} {'row(0b)':>7} {'b_land':>10} {'j_i':>10} {'gap_i':>6} "
       f"{'gap/(j+1)':>10} {'margin b-1':>10} {'flooring':>10}")
print(hdr)
table = []
for t, r in enumerate(sr):
    b, j, f = sb[t], sj[t], sf[t]
    gap = sg[t] if t < len(sg) else None
    ratio = (Fraction(gap, j + 1) if gap is not None else None)
    margin = b - 1
    table.append({
        "giant": t + 1, "row0": r, "row1": r + 1, "b_land": b, "j": j,
        "gap": gap, "ratio": (float(ratio) if ratio is not None else None),
        "margin": margin, "flooring": f,
    })
    gs = f"{gap}" if gap is not None else "--"
    rs = f"{float(ratio):.6f}" if ratio is not None else "--"
    print(f"{t + 1:>5} {r:>7} {b:>10} {j:>10} {gs:>6} {rs:>10} {margin:>10} "
          f"{f:>10}")

# ----------------------------------------------------------------- step 6
print("\n--- Step 6: gap trend over the 14 genuine gaps ---")
x = np.arange(14, dtype=np.float64)
y = np.asarray(sg, dtype=np.float64)
slope_np, intercept_np = np.polyfit(x, y, 1)
yhat = slope_np * x + intercept_np
ss_res = float(np.sum((y - yhat) ** 2))
ss_tot = float(np.sum((y - y.mean()) ** 2))
r2 = 1.0 - ss_res / ss_tot
# independent exact-arithmetic closed form: slope = Sxy / Sxx, rational
xf = [Fraction(i) for i in range(14)]
yf = [Fraction(v) for v in sg]
xbar = sum(xf) / 14
ybar = sum(yf) / 14
sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(xf, yf))
sxx = sum((xi - xbar) ** 2 for xi in xf)
slope_exact = sxy / sxx
slope_exact_f = float(slope_exact)
agree6 = abs(slope_exact_f - slope_np) < 1e-12
print(f"numpy polyfit:      slope = {slope_np:.12f}, intercept = "
      f"{intercept_np:.6f}, R^2 = {r2:.6f}")
print(f"closed-form exact:  slope = {slope_exact} = {slope_exact_f:.12f} "
      f"(Sxy = {sxy}, Sxx = {sxx})")
print(f"slopes agree: {'PASS' if agree6 else 'FAIL'}")
assert agree6
max_gap = max(sg)
mg_pair = (sr[sg.index(max_gap)], sr[sg.index(max_gap) + 1])
print(f"max gap = {max_gap}, pair = {mg_pair} "
      f"(rows {sr[sg.index(max_gap)]} -> {sr[sg.index(max_gap) + 1]})")

# ----------------------------------------------------------------- step 7
print("\n--- Step 7: parity of the 15 genuine 0-based pre-jump rows ---")
n = len(sr)
evens = [r for r in sr if r % 2 == 0]
odds = [r for r in sr if r % 2 == 1]
ne = len(evens); no_ = len(odds)
p_fair = Fraction(math.comb(n, ne) + math.comb(n, n), 2 ** n)
p060 = sum(Fraction(math.comb(n, k)) * Fraction(6, 10) ** k
           * Fraction(4, 10) ** (n - k) for k in range(ne, n + 1))
print(f"even rows: {ne} of {n}  -> {evens}")
print(f"odd rows:  {no_} of {n}  -> {odds}")
print(f"p_fair = (C(15,{ne}) + C(15,{n})) / 2^{n} = "
      f"({math.comb(n, ne)} + {math.comb(n, n)}) / {2 ** n} = {p_fair} = "
      f"{float(p_fair):.10f}")
print(f"P(>= {ne} of {n} even | p = 0.600) = "
      f"sum over k = {ne}..{n} of C({n},k) * 0.6^k * 0.4^(n-k) =")
terms = [Fraction(math.comb(n, k)) * Fraction(6, 10) ** k
         * Fraction(4, 10) ** (n - k) for k in range(ne, n + 1)]
for k, tm in zip(range(ne, n + 1), terms):
    print(f"  C({n},{k}) * 0.6^{k} * 0.4^{n - k} = {math.comb(n, k)} * "
          f"0.6^{k} * 0.4^{n - k} = {tm} = {float(tm):.10f}")
print(f"  total = {p060} = {float(p060):.10f}")

# ----------------------------------------------------------------- step 8
print("\n--- Step 8: geometric growth of landing block b_land ---")
x2 = np.arange(len(sr), dtype=np.float64)
y2 = np.log(np.asarray(sb, dtype=np.float64))
slope_g, intercept_g = np.polyfit(x2, y2, 1)
yx = [float(math.log(float(b))) for b in sb]
n2 = len(sr)
x2f = [float(i) for i in range(n2)]
xb2 = sum(x2f) / n2
yb2 = sum(yx) / n2
sxy2 = sum((xi - xb2) * (yi - yb2) for xi, yi in zip(x2f, yx))
sxx2 = sum((xi - xb2) ** 2 for xi in x2f)
slope_g_cf = sxy2 / sxx2
agree8 = abs(slope_g_cf - slope_g) < 1e-9
print(f"numpy polyfit of log(b_land) vs index 0..{len(sr) - 1}: slope = "
      f"{slope_g:.10f}, intercept = {intercept_g:.6f}")
print(f"independent closed-form slope = {slope_g_cf:.10f} "
      f"(Sxy = {sxy2:.6f}, Sxx = {sxx2:.6f})")
print(f"slopes agree: {'PASS' if agree8 else 'FAIL'}")
assert agree8
factor = math.exp(slope_g)
b_next = float(sb[-1]) * factor
b_next_int = int(round(b_next))
next_row = sr[-1] + max_gap
reqW = b_next_int + next_row + 1001
print(f"growth factor e^slope = {factor:.6f}")
print(f"b_next = b_land(row {sr[-1]}) * factor = {sb[-1]} * {factor:.6f} "
      f"= {b_next:.1f}  (rounded {b_next_int})")
print(f"next row ~= {sr[-1]} + max_gap = {sr[-1]} + {max_gap} = {next_row}")
print(f"required W = b_next + row + 1001 (margin threshold 1000) = "
      f"{b_next_int} + {next_row} + 1001 = {reqW}")
print(f"  (check: flooring at that row = W - {next_row} - 2 - b_next = "
      f"{reqW - next_row - 2 - b_next_int})")
print(f"required pi(N) = {reqW}")


def sieve_bound_for_pi(target: float) -> int:
    """Smallest integer N with N / ln N >= target (N > e).  Bisection."""
    hi = 16.0
    while hi / math.log(hi) < target:
        hi *= 2.0
    lo = hi / 2.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if mid / math.log(mid) >= target:
            hi = mid
        else:
            lo = mid
    return math.ceil(hi)


N_req = sieve_bound_for_pi(float(reqW))
print(f"sieve bound N solving N / ln N = {reqW}: N = {N_req} "
      f"(N/ln N = {N_req / math.log(N_req):.0f})")

# ----------------------------------------------------------------- step 9
print("\n--- Step 9: sufficiency check over the 14 gaps ---")
ratio_fail = []
margin_fail = []
margins = []
for t in range(len(sg)):
    g, j, b = sg[t], sj[t], sb[t]
    rb = g <= j + 1
    mb = g <= b - 1
    margins.append(b - 1 - g)
    flag = "  " if (rb and mb) else "  <-- VIOLATION"
    print(f"gap {g:>3} (giant {t + 1} row {sr[t]:>3} -> row {sr[t + 1]:>3}): "
          f"gap <= j+1 = {j + 1}: {'yes' if rb else 'NO'}   "
          f"gap <= b_land-1 = {b - 1}: {'yes' if mb else 'NO'}{flag}")
    if not rb:
        ratio_fail.append(t)
    if not mb:
        margin_fail.append(t)
min_margin = min(margins)
min_at = margins.index(min_margin)
print(f"ratio-bound failures: {len(ratio_fail)} ({ratio_fail or 'none'})")
print(f"margin failures:      {len(margin_fail)} ({margin_fail or 'none'})")
print(f"min margin (b_land-1-gap) overall = {min_margin} at gap "
      f"{(sr[min_at], sr[min_at + 1])} (giant {min_at + 1}, row {sr[min_at]})")

# ----------------------------------------------------------------- json
out = {
    "directive": 30,
    "source": SRC,
    "W": W, "num_primes_6e8": W, "depth": DEPTH,
    "k_star_no_intruder_1based": kstar,
    "excluded_row0": row_art,
    "excluded_reason": ("flooring == 0; block meets the row's right edge at "
                        "k*; jump is a finite-width truncation artifact"),
    "n_giants_total": len(rows0), "n_surviving": len(sr),
    "surviving_rows0": sr,
    "gaps": sg,
    "table": table,
    "gap_trend": {
        "slope_numpy": slope_np, "intercept_numpy": intercept_np,
        "r2": r2, "slope_exact_frac": str(slope_exact),
        "slope_exact_float": slope_exact_f, "agree": bool(agree6),
        "max_gap": max_gap, "max_gap_pair": list(mg_pair),
    },
    "parity": {
        "n": n, "even": ne, "odd": no_,
        "p_fair_frac": str(p_fair), "p_fair": float(p_fair),
        "p_given_0p6_frac": str(p060), "p_given_0p6": float(p060),
    },
    "geometric": {
        "slope_numpy": slope_g, "intercept_numpy": intercept_g,
        "slope_closed_form": slope_g_cf, "agree": bool(agree8),
        "factor": factor, "b_next_float": b_next,
        "b_next_int": b_next_int, "next_row": next_row,
        "required_W": reqW, "required_pi": reqW,
        "sieve_bound_N": N_req,
    },
    "sufficiency": {
        "ratio_bound_failures": len(ratio_fail),
        "ratio_bound_failure_gaps": ratio_fail,
        "margin_failures": len(margin_fail),
        "margin_failure_gaps": margin_fail,
        "min_margin": min_margin, "min_margin_at_gap_pair":
            list((sr[min_at], sr[min_at + 1])),
    },
}
with open(OUT_JSON, "w") as f:
    json.dump(out, f, indent=1)
print(f"\nwrote {OUT_JSON}")
print("done")