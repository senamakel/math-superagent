#!/usr/bin/env python3
"""Independent verification of giants_1e9.json — second route.

Re-derives the giant table (events, jumps, gaps, floors), the parity tail
values, and the fits directly from the JSON's saved b array, using only pure
Python (no numpy) for the event extraction, and numpy only for the fit —
so the program's inline computation and this checker share no code path.
Also verifies the block-lemma protection bound that the full-width row-248
block implies, and re-checks rows 1..247 against the 6e8 record.
"""
import json
from fractions import Fraction
from math import comb, log2

import numpy as np

G = json.load(open("code/out/pattern_finder_outputs/giants_1e9.json"))
B6 = json.load(open("code/out/pattern_finder_outputs/giants_6e8.json"))
b = G["b"]
W = G["num_primes"]
DEPTH = G["depth"]
GIANT = 1000

# --- 1. re-derive events/giants from the raw b array, pure Python ---
events = [r for r in range(2, DEPTH + 1) if b[r - 1] > b[r - 2]]
giants = [(r, b[r - 1] - b[r - 2], b[r - 2], b[r - 1])
          for r in events if b[r - 1] - b[r - 2] > GIANT]
rows1 = [r for (r, _, _, _) in giants]
rows0 = [r - 1 for r in rows1]
jumps = [j for (_, j, _, _) in giants]
bland = [bl for (_, _, _, bl) in giants]
floors = [W - r - 1 - bl for (r, _, _, bl) in giants]
gaps = [rows1[t + 1] - rows1[t] for t in range(len(rows1) - 1)]
print(f"re-derived: {len(giants)} giants, W = {W}")
assert rows0 == G["giants_0based_rows"], "0-based rows mismatch"
assert jumps == G["jumps"], "jumps mismatch"
assert bland == G["landing_blocks"], "landings mismatch"
assert floors == G["landing_floors"], "floors mismatch"
assert gaps == G["inter_giant_gaps"], "gaps mismatch"
print("JSON giant table re-derived identically (rows/jumps/landings/floors/gaps): OK")

# --- 2. cross-check rows 1..247 vs 6e8, row 248 vs the 6e8 capped value ---
m = [i + 1 for i in range(247) if b[i] != B6["b"][i]]
print(f"rows 1..247 vs 6e8: mismatches = {m}")
assert m == [], "row mismatch vs 6e8!"
print(f"row 248: 6e8 = {B6['b'][247]} (capped), 1e9 = {b[247]} "
      f"(extends {b[247] - B6['b'][247]:,} columns past the 6e8 edge)")

# --- 3. settlement numbers ---
last = giants[-1]
print(f"\n16th giant: row0={last[0]-1} row1={last[0]} jump={last[1]:,} "
      f"b_land={last[3]:,} floor={W - last[0] - 1 - last[3]} "
      f"-> {'GENUINE' if W - last[0] - 1 - last[3] > 0 else 'CAPPED (floor=0)'}")
print(f"16th giant gap: {gaps[-1]} (prev row1 {rows1[-2]} -> {rows1[-1]}) "
      f"-> {'TREND > 64' if gaps[-1] > 64 else 'NOISE <= 64'}")
print(f"max gap: {max(gaps)} at {gaps.index(max(gaps))} (rows1 "
      f"{rows1[gaps.index(max(gaps))]} -> {rows1[gaps.index(max(gaps))+1]})")
ratios = [g / (j + 1) for g, j in zip(gaps, jumps[1:])]
print(f"ratios gap/(j+1): max {max(ratios):.4e} min {min(ratios):.4e} "
      f"(all < 0.1: {all(r < 0.1 for r in ratios)})")

# --- 4. parity, exact arithmetic ---
odd0 = [r for r in rows0 if r % 2 == 1]
n = len(rows0)
print(f"\nparity: {n} giants, odd 0-based rows: {odd0}")
p_le1 = Fraction(comb(n, 1) + comb(n, 0), 2 ** n)
p_le2 = Fraction(comb(n, 2) + comb(n, 1) + comb(n, 0), 2 ** n)
print(f"(C(n,1)+C(n,0))/2^n = ({comb(n,1)}+{comb(n,0)})/{2**n} = {p_le1} "
      f"= {float(p_le1):.4g}")
print(f"observed-tail P(<=2 odd) = {p_le2} = {float(p_le2):.4g}")

# --- 5. fits on genuine landing blocks (floor > 0), numpy re-derivation ---
gen = [f > 0 for f in floors]
grow = [r for t, r in enumerate(rows1) if gen[t]]
gl = [bl for t, bl in enumerate(bland) if gen[t]]
y = np.log2(np.array(gl, dtype=np.float64))
xg = np.array(grow, dtype=np.float64)
slope, intercept = np.polyfit(xg, y, 1)
r2 = 1.0 - float(np.sum((y - (slope * xg + intercept)) ** 2)
                 / np.sum((y - y.mean()) ** 2))
print(f"\ngeometric fit over {len(gl)} genuine landings: log2 slope = "
      f"{slope:.6f} (doubling every {1/abs(slope):.2f} rows), r2 = {r2:.6f}")
assert abs(slope - G["fits_genuine"]["log2_slope_numpy"]) < 1e-9
s_lin, i_lin = np.polyfit(xg, np.array(gl, dtype=np.float64), 1)
r2_lin = 1.0 - float(np.sum((np.array(gl, dtype=np.float64)
                             - (s_lin * xg + i_lin)) ** 2)
                     / np.sum((np.array(gl, dtype=np.float64)
                               - np.mean(gl)) ** 2))
print(f"linear fit r2 = {r2_lin:.6f}  -> geometric wins: "
      f"{'YES' if r2 > r2_lin else 'NO'}")
print(f"agreement with program's slope: {abs(slope - G['fits_genuine']['log2_slope_numpy']):.2e}")

# --- 6. block-lemma protection bound from the full-width row 248 ---
n248 = b[247]                       # block length of row 248 (0-based index 247)
K = 248
print(f"\nrow 248 block length n = {n248:,} = W - 248 - 1 "
      f"({'all {0,2}' if n248 == W - K - 1 else 'NOT full'})")
prot = n248 + 1
print(f"block lemma (n+1 rows of protection): leading 1 guaranteed for rows "
      f"{K}..{K + n248} = 248..{K + n248:,}")
print(f"=> A_k(0) = 1 verified/protected for all rows 1..{K + n248:,}")
assert n248 == W - K - 1
print("checks complete")
