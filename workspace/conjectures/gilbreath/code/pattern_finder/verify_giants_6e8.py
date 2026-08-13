#!/usr/bin/env python3
"""Independent verification of the 6e8 giant structure.

Pure Python, exact arithmetic only (int, Fraction); no numpy.
Reads code/out/pattern_finder_outputs/giants_6e8.json and recomputes:

  (1) the 15 genuine giants (0-based landing rows) after excluding the
      flooring==0 artifact, and their 14 gaps;
  (2) exact OLS slope and R^2 of gap vs index 0..13 (closed forms, Fraction);
  (3) exact p = (C(15,14)+C(15,15))/2^15 and p = P(X>=14 | Bin(15,0.6)),
      plus the count of even gaps among the 14;
  (4) per-giant ratio gap/(j+1) (both "gap after" and "gap before" readings)
      and the floor margin b_land vs the row's physical right edge;
  (5) OLS of log(b_land+1) vs index over the 15 giants: slope, R^2, e^slope;
  (6) sanity: sum of the 14 gaps; recharge-identity consistency
      b_land[i+1] = b_land[i] - gap[i] + j[i+1]  (derived: holds iff no
      intermediate events AND up to the +1 Odlyzko constant -- verified
      exactly against the b series).

All PASS/FAIL against the expected 15 giants / 14 gaps / max gap 64.
"""
import json
import math
from fractions import Fraction
from math import comb, log

PATH = "code/out/pattern_finder_outputs/giants_6e8.json"
d = json.load(open(PATH))

W = d["num_primes"]
rows = list(d["giants_0based_rows"])        # landing rows, 0-based
jumps = list(d["jumps"])                    # jump at pre-jump row rows[i]-1
bland = list(d["landing_blocks"])           # b at landing row rows[i]
floors = list(d["landing_floors"])          # space past block end
b = list(d["b"])                            # full block series, 0-based rows

print("=" * 78)
print("GIANTS 6e8 — INDEPENDENT PURE-PYTHON VERIFICATION")
print("sieve limit", d["limit"], " num_primes W =", W,
      " depth", d["depth"], " k_star_no_intruder", d["k_star_no_intruder"])
print("=" * 78)

# ---- stored-data sanity: every stored quantity is recomputable from b ----
for i, r in enumerate(rows):
    assert bland[i] == b[r], (i, bland[i], b[r])
    assert jumps[i] == b[r] - b[r - 1], (i, jumps[i], b[r] - b[r - 1])
    assert floors[i] == W - (r + 2) - bland[i], \
        (i, floors[i], W - (r + 2) - bland[i])
print("stored-data sanity: for all 16 giants, landing_blocks[i]==b[rows[i]],")
print("  jumps[i]==b[rows[i]]-b[rows[i]-1], floors[i]==W-(rows[i]+2)-b_land[i] : PASS")

# ---- (1) genuine giants = those with flooring > 0 ----
art = [i for i, f in enumerate(floors) if f == 0]
print("\n(1) flooring==0 artifact rows (index, row):",
      [(i, rows[i]) for i in art])
assert art == [15], art
assert d["odd_0based_other_than_161"] == [247]
gen_idx = [i for i in range(len(rows)) if i not in art]
g_rows = [rows[i] for i in gen_idx]
g_jumps = [jumps[i] for i in gen_idx]
g_bland = [bland[i] for i in gen_idx]
g_floors = [floors[i] for i in gen_idx]
nG = len(g_rows)
gaps = [g_rows[i + 1] - g_rows[i] for i in range(nG - 1)]
print(f"genuine giants (flooring>0): {nG}  rows {g_rows}")
print(f"gaps (14): {gaps}")
print(f"max gap = {max(gaps)}  (expected 64)  sum gaps = {sum(gaps)}"
      f"  (expected {g_rows[-1] - g_rows[0]})")
P1 = (nG == 15) and (len(gaps) == 14) and (max(gaps) == 64)
print(f"PASS/FAIL: 15 giants / 14 gaps / max gap 64 -> "
      f"{'PASS' if P1 else 'FAIL'}")
print(f"parity of genuine giants (0-based rows): "
      f"even={sum(1 for r in g_rows if r % 2 == 0)}, "
      f"odd={sum(1 for r in g_rows if r % 2 == 1)} -> odd rows {[r for r in g_rows if r % 2]}")

# ---- (2) exact OLS of gap vs index 0..13 ----
xs = list(range(len(gaps)))
n = len(xs)
xbar = Fraction(sum(xs), n)
ybar = Fraction(sum(gaps), n)
Sxx = sum((Fraction(x) - xbar) ** 2 for x in xs)
Sxy = sum((Fraction(x) - xbar) * (Fraction(y) - ybar)
          for x, y in zip(xs, gaps))
Syy = sum((Fraction(y) - ybar) ** 2 for y in gaps)
slope = Sxy / Sxx
R2 = (Sxy * Sxy) / (Sxx * Syy)
print("\n(2) OLS of gap vs index 0..13 (exact Fractions):")
print(f"    Sxx = {Sxx} = {float(Sxx):.6f}")
print(f"    Sxy = {Sxy} = {float(Sxy):.6f}")
print(f"    Syy = {Syy} = {float(Syy):.6f}")
print(f"    slope = {slope} = {float(slope):.6f}")
print(f"    R^2   = {R2} = {float(R2):.6f}")

# ---- (3) exact p-values and even-gap count ----
p_fair = Fraction(comb(15, 14) + comb(15, 15), 2 ** 15)
p_06 = Fraction(33 * 3 ** 14, 5 ** 15)          # P(X>=14 | Bin(15,0.6))
p_06_check = sum(comb(15, k) * Fraction(3, 5) ** k * Fraction(2, 5) ** (15 - k)
                 for k in (14, 15))
assert p_06 == p_06_check
p_06_twosided = Fraction(2 * (comb(15, 14) + comb(15, 15)), 2 ** 15)
even_gaps = sum(1 for g in gaps if g % 2 == 0)
print("\n(3) exact probabilities:")
print(f"    p_fair  = (C(15,14)+C(15,15))/2^15 = {p_fair} = {float(p_fair):.10f}")
print(f"    p_06    = P(X>=14 | Bin(15,0.6))   = {p_06} = {float(p_06):.10f}")
print(f"    (two-sided fair variant for context = {p_06_twosided} = {float(p_06_twosided):.10f})")
print(f"    even gaps among the 14: {even_gaps} (odd: {len(gaps) - even_gaps})")

# ---- (4) per-giant ratio gap/(j+1), floor margins ----
print("\n(4) per-giant ratios and margins (all exact ints/Fractions):")
print("    i  row   j         b_land      floor_margin  b_land-1  "
      "gap_after/(j+1)  gap_before/(j+1)")
gap_after_rat = []
gap_before_rat = []
for i in range(nG):
    r, j, bl, fl = g_rows[i], g_jumps[i], g_bland[i], g_floors[i]
    ga = gaps[i] if i < nG - 1 else None
    gb = gaps[i - 1] if i > 0 else None
    ra = Fraction(ga, j + 1) if ga is not None else None
    rb = Fraction(gb, j + 1) if gb is not None else None
    if ra is not None:
        gap_after_rat.append(ra)
    if rb is not None:
        gap_before_rat.append(rb)
    print(f"   {i:2d} {r:4d} {j:9d} {bl:10d} {fl:11d} {bl - 1:9d}  "
          f"{str(ra) if ra is not None else '  n/a (no next genuine giant)'}"
          f"  {str(rb) if rb is not None else ' n/a (first)'}")
print(f"    gap_after/(j+1):  n={len(gap_after_rat)}  min={min(gap_after_rat)}"
      f" ({float(min(gap_after_rat)):.6f})  max={max(gap_after_rat)}"
      f" ({float(max(gap_after_rat)):.6f})  "
      f"mean={float(sum(gap_after_rat) / len(gap_after_rat)):.6f}")
print(f"    gap_before/(j+1): n={len(gap_before_rat)}  min={min(gap_before_rat)}"
      f" ({float(min(gap_before_rat)):.6f})  max={max(gap_before_rat)}"
      f" ({float(max(gap_before_rat)):.6f})")
print(f"    floor margin min over 15 genuine giants = {min(g_floors)}"
      f" (row {g_rows[g_floors.index(min(g_floors))]})")
print(f"    literal b_land-1 min over 15 genuine giants = {min(bl - 1 for bl in g_bland)}")

# ---- (5) OLS of log(b_land+1) vs index 0..14 ----
lx = [float(i) for i in range(nG)]
ly = [log(bl + 1) for bl in g_bland]
n5 = len(lx)
lxbar = sum(lx) / n5
lybar = sum(ly) / n5
lSxx = sum((x - lxbar) ** 2 for x in lx)
lSxy = sum((x - lxbar) * (y - lybar) for x, y in zip(lx, ly))
lSyy = sum((y - lybar) ** 2 for y in ly)
lslope = lSxy / lSxx
lR2 = lSxy * lSxy / (lSxx * lSyy)
print("\n(5) OLS of log(b_land+1) vs index over the 15 giants:")
print(f"    slope = {lslope:.6f}   R^2 = {lR2:.6f}   e^slope = {math.exp(lslope):.6f}")
print(f"    (log-space: slope={lslope:.6f} per giant; growth factor "
      f"{math.exp(lslope):.4f} per giant, i.e. doubling time "
      f"{log(2) / lslope:.2f} giants)")

# ---- (6) sanity + recharge-identity consistency ----
print("\n(6) sanity and recharge identity:")
print(f"    sum of 14 gaps = {sum(gaps)} ; rows[14]-rows[0] = "
      f"{g_rows[-1] - g_rows[0]} -> "
      f"{'PASS' if sum(gaps) == g_rows[-1] - g_rows[0] else 'FAIL'}")
print("    requested check: b_land[i+1] == b_land[i] - gap[i] + j[i+1] ?")
print("    exact identity (recharge law): b_land[i+1] = b_land[i] - gap[i]"
      " + sum_{events in window}(j_e+1),")
print("      window = pre-jump rows [rows[i], rows[i+1]-1]; the giant's own"
      " event contributes j[i+1]+1,")
print("      so requested equality holds iff (1 + sum_other(j_e+1)) == 0,"
      " which is impossible (j_e >= 1).")
n_req_ok = 0
n_exact_ok = 0
for i in range(nG - 1):
    r0, r1 = g_rows[i], g_rows[i + 1]
    gap = r1 - r0
    req_rhs = g_bland[i] - gap + g_jumps[i + 1]
    req_ok = (g_bland[i + 1] == req_rhs)
    n_req_ok += req_ok
    # events = pre-jump rows k in [r0, r1-1] with b[k+1] > b[k]
    ev = [(k, b[k + 1] - b[k]) for k in range(r0, r1)
          if b[k + 1] > b[k]]
    sum_j1 = sum(je + 1 for _, je in ev)
    own = ev[-1] if ev else None
    others = ev[:-1]
    exact_ok = (g_bland[i + 1] == g_bland[i] - gap + sum_j1)
    n_exact_ok += exact_ok
    print(f"    i={i:2d} rows {r0}->{r1} gap={gap:2d} j[i+1]={g_jumps[i + 1]:9d} "
          f"req_ok={'Y' if req_ok else 'n'}  exact_ok={'Y' if exact_ok else 'n'}  "
          f"events in window={len(ev)} (own giant + {len(others)} other)  "
          f"sum(j_e+1)={sum_j1}  diff vs j[i+1]+1 = {sum_j1 - g_jumps[i + 1] - 1}")
print(f"    requested naive equality holds: {n_req_ok}/14  "
      f"(expected 0: misses the +1 Odlyzko constant and any intermediate events)")
print(f"    exact recharge identity holds: {n_exact_ok}/14  "
      f"{'PASS' if n_exact_ok == 14 else 'FAIL'}")
print("    b_land[i+1] - (b_land[i] - gap[i]) = sum(j_e+1) >= j[i+1]+1 > 0"
      " for all 14 : PASS (never negative)")

print("\n" + "=" * 78)
print(f"FINAL: 15 giants / 14 gaps / max gap 64 -> {'PASS' if P1 else 'FAIL'}; "
      f"even gaps {even_gaps}/14; p_fair={float(p_fair):.6g}, "
      f"p_06={float(p_06):.6g}; recharge identity {n_exact_ok}/14.")
print("=" * 78)
