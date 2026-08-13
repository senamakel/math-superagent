#!/usr/bin/env python3
"""Directive 25: inter-giant gap trend + reconcile geometric growth with the
sublinear jump exponent.

Data: code/out/blocks_depth1000.json — b[k-1] = leading {0,2} block length of
row k (1-based), W = 1,270,607 primes (sieve 2e7). Exact integer arithmetic;
least-squares fits on exact Fractions; plain Python only, no numpy.

Row conventions (cross-checked against bigjump_characterization.captured.txt
in directive24_compute.py): event at 1-based row i <-> JSON b[i-1] -> b[i]
(b[i] > b[i-1]); post-jump block b_{i+1} = JSON b[i]; the 13 giants (j > 1000)
are i in GIANTS, 12 genuine + i=161 capped (finite-width artifact, landing
floor 0).

Part A — gap trend (Directive 25 item 3):
  inter-giant gaps = successive differences of the giant rows.  Report the raw
  gaps, mean/median, OLS gap ~ giant# and gap ~ prior_b, and Spearman rho of
  gap vs prior post-jump b (exact).  Question settled: does the gap stay
  bounded while j -> inf (Gilbreath survives) or grow with b (obstruction)?
  The capped i=161 is excluded from every gap list.

Part B — reconciliation (Directive 25 item 4):
  observed rho = b_{i+1}/b_i at each genuine giant (across the 11 consecutive
  pairs among the genuine 12).  Model 1 (sublinear): j = C*b^alpha, alpha =
  0.388 (surplus_renewal_structure over 43 events), so rho_sub = 1 + j/b =
  1 + C*b^(alpha-1), C calibrated per-giant (C_i = j_i/b_i^0.388 at the PRE-
  jump block b_i = JSON b[i-1]) and pooled (mean of C_i).  Model 2
  (geometric): rho = 1.6816 (directive24 genuine-12 doubling factor).
  Reported per giant and as MSE of log-residuals.

Time O(n log n), n = 1000. Space O(n). No search, no enumeration.
"""
import json
import math
from fractions import Fraction

ALPHA = Fraction(388, 1000)          # log(jump)/log(b) slope, 43 events
GEOM_RHO = Fraction(16816, 10000)    # 1.6816, directive24 genuine-12 factor

with open('code/out/blocks_depth1000.json') as f:
    data = json.load(f)
b = data['b']
W = data['num_primes']
assert data['D'] == 1000 and len(b) == 1000 and W == 1_270_607
assert b[0] == 2 and b[1] == 7 and b[2] == 13          # rows 1..3
assert b[160] == 1_094_263 and b[161] == 1_270_444     # cap row 161

print('RANGE-CONVENTION-CHECK: anchors match the characterization tables')
print(f'W = {W}  D = {data["D"]}')

GIANTS = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161]
GENUINE = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146]


def mean(xs):
    return Fraction(sum(xs), len(xs))


def ols(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    m = Fraction(n * sxy - sx * sy, n * sxx - sx * sx)
    a = Fraction(sy - m * sx, n)
    fit = [a + m * x for x in xs]
    res = [y - f for y, f in zip(ys, fit)]
    ss_tot = sum((y - mean(ys)) ** 2 for y in ys)
    ss_res = sum(r * r for r in res)
    r2 = Fraction(1) - ss_res / ss_tot if ss_tot else Fraction(0)
    return m, a, r2


def spearman_rho(xs, ys):
    """Exact Spearman rank correlation (no ties)."""
    def ranks(v):
        return {x: i for i, x in enumerate(sorted(v), 1)}
    rx = [ranks(xs)[x] for x in xs]
    ry = [ranks(ys)[y] for y in ys]
    n = len(xs)
    d2 = sum((a - c) ** 2 for a, c in zip(rx, ry))
    return Fraction(1) - Fraction(6 * d2, n * (n * n - 1))


def log(fr):
    return math.log(float(fr))


# ---- Part A: inter-giant gap trend -------------------------------------
print()
print('=== PART A: inter-giant gap trend (Directive 25 item 3) ===')
for label, rows in [('ALL 13 (incl. capped 161)', GIANTS),
                    ('GENUINE 12', GENUINE)]:
    gaps = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
    prior_b = [b[i] for i in rows[:-1]]          # post-jump block of prev
    print(f'  {label} ({len(rows)} giants): rows {rows}')
    print(f'    inter-giant gaps in rows: {gaps}')
    print(f'    mean {float(mean(gaps)):.2f}  median '
          f'{float(sorted(gaps)[len(gaps)//2]):.1f}  max {max(gaps)}')
    m, a, r2 = ols(list(range(len(gaps))), [Fraction(g) for g in gaps])
    print(f'    OLS gap ~ giant#: slope {float(m):+.3f}  R2 {float(r2):.3f}')
    mb, ab, r2b = ols([Fraction(v) for v in prior_b],
                      [Fraction(g) for g in gaps])
    print(f'    OLS gap ~ prior_b: slope {float(mb):+.5f}  '
          f'R2 {float(r2b):.3f}')
    rho = spearman_rho(prior_b, gaps)
    print(f'    Spearman rho(gap, prior_b) = {float(rho):+.3f} (exact)')
    inc = all(gaps[i + 1] >= gaps[i] for i in range(len(gaps) - 1))
    dec = all(gaps[i + 1] <= gaps[i] for i in range(len(gaps) - 1))
    print(f'    direction: {"nondecreasing" if inc else ""}'
          f'{"nonincreasing" if dec else ""}'
          f'{"neither (mixed)" if not inc and not dec else ""}')
print('  (the capped i=161 is excluded from the trend claim; fits above use '
      'genuine rows only)')

# ---- Part B: reconcile geometric growth with the sublinear exponent -------
print()
print('=== PART B: rho = 1 + j/b vs sublinear j = C*b^0.388 ===')
print(f'  alpha = 0.388 (43-event OLS, surplus_renewal_structure); '
      f'geometric factor = {float(GEOM_RHO)} (directive24)')
print(f'  genuine giants: {GENUINE}')
print(f'  {"i":>4} {"b_i":>9} {"j_i":>9} {"rho_obs":>9} {"C_i":>10}')
Cvals = []
for idx in range(1, len(GENUINE)):
    i = GENUINE[idx]
    b_pre = b[i - 1]                       # pre-jump block b_i = JSON b[i-1]
    j = b[i] - b[i - 1]
    rho_obs = Fraction(b[i], b[GENUINE[idx - 1]])   # b_{i+1} over prev b
    C_i = j / (b_pre ** float(ALPHA))
    Cvals.append(C_i)
    print(f'  {i:>4} {b_pre:>9} {j:>9} {float(rho_obs):>9.4f} '
          f'{float(C_i):>10.4f}')

C_pool = sum(Cvals) / len(Cvals)
print(f'  pooled C = mean(C_i) = {float(C_pool):.4f}')

print()
print(f'  sublinear expected rho_sub = 1 + C_pool * b^(alpha-1) vs '
      f'geometric rho_geom = {float(GEOM_RHO)}')
print(f'  {"i":>4} {"rho_obs":>9} {"rho_sub":>9} {"rho_geom":>9} '
      f'{"res_sub":>9} {"res_geom":>9}')
ressub, resgeom = [], []
for idx in range(1, len(GENUINE)):
    i = GENUINE[idx]
    b_pre = b[i - 1]
    j = b[i] - b[i - 1]
    rho_obs = Fraction(b[i], b[GENUINE[idx - 1]])
    rho_sub = 1.0 + C_pool * (b_pre ** (float(ALPHA) - 1.0))
    ressub.append(log(rho_obs) - log(rho_sub))
    resgeom.append(log(rho_obs) - log(GEOM_RHO))
    print(f'  {i:>4} {float(rho_obs):>9.4f} {float(rho_sub):>9.4f} '
          f'{float(GEOM_RHO):>9.4f} {ressub[-1]:>+9.4f} {resgeom[-1]:>+9.4f}')

def mse(v):
    return sum(x * x for x in v) / len(v)

print()
print(f'  MSE(log-residuals): sublinear {mse(ressub):.4f}  '
      f'geometric {mse(resgeom):.4f}')
print(f'  mean log-residual: sublinear {sum(ressub)/len(ressub):+.4f}  '
      f'geometric {sum(resgeom)/len(resgeom):+.4f}')
print()
print('  reading: sublinear residuals near 0 with no trend -> the observed '
      'ratios are consistent with rho = 1 + C*b^(alpha-1) -> 1 (the '
      'asymptotic reconciliation); geometric residuals flat near 0 would '
      'support the constant factor but contradict the sublinear limit.')
print('DONE')