#!/usr/bin/env python3
"""Directive 24 compute: width-degradation caveat + geometric-growth test.

Reads code/out/blocks_depth1000.json (dict: b[0..1000), the leading {0,2}
block lengths B[r] = b[r-1] of the prime Gilbreath triangle rows r=1..1000;
W = num_primes = 1,270,607). Exact integer arithmetic only. Row convention
(verified against code/out/bigjump_characterization.captured.txt):

    event at 1-based row i  <->  JSON step b[i-1] -> b[i]  (b[i] > b[i-1])
    post-jump block b_{i+1} = JSON b[i]
    row r has W - r columns; block occupies positions 1..b_{r-1}, so the
    directive's flooring is  flooring(r) = (W - r - 1) - b[r-1].
    The characterization table's floor is this same quantity evaluated at
    the landing row r = i+1:  (W - i - 2) - b[i].

(a) k* = first r in 1..1000 with flooring(r) < J_MIN=1000. Report flooring
    at the 13 giant event rows (event row and landing row) and, per giant,
    the first row past it with flooring < 1000.

(b) Giants detected from the b array via the step law (b[i] > b[i-1]).
    12 genuine post-jump blocks b[i] for i in {34,56,64,68,94,96,110,112,
    126,130,134,146}; i=161 (b[161]=1,270,444) is the capped artifact.
    Least-squares fits on (index 0..n-1, y):  log y vs x (geometric) and
    y vs x (linear), computed as exact rationals; slope, intercept, R^2,
    residuals, per-step ratios, doubling factor 2^(slope/ln2). Same for the
    full 13 as a robustness check.

Time O(n), n=1000. Space O(n). No search, no enumeration.
"""
import json
import math
from fractions import Fraction

J_MIN = 1000

with open('code/out/blocks_depth1000.json') as f:
    data = json.load(f)

b = data['b']          # b[i] = block length B_{i+1}; i = 0..999
D = data['D']
W = data['num_primes']
assert D == 1000 and len(b) == 1000 and W == 1_270_607
assert data['max_block'] == 1_270_444 and data['first_bad'] is None

# ---- row-convention checks against CONTEXT.md / characterization table ----
assert b[0] == 2 and b[1] == 7 and b[2] == 13            # rows 1,2,3
assert b[33] == 865 and b[34] == 2179                    # giant row 34 -> 35
assert b[160] == 1_094_263 and b[161] == 1_270_444       # giant row 161 -> 162 = cap
assert (W - 162 - 1) - b[161] == 0                       # flooring(162) == 0
assert (W - 35 - 1) - b[34] == 1_268_392                 # directive flooring(35) = 1,268,392
print('RANGE-CONVENTION-CHECK: row mapping and anchor floors match CONTEXT.md')
print(f'W = {W}  D = {D}')

# ---------------- (a) width degradation ----------------
def flooring(r):
    """Directive formula: row r (1-based) has W-r columns (0..W-r-1);
    block occupies 1..b[r-1]; distance to the right edge."""
    return (W - r - 1) - b[r - 1]

def landing_floor(i):
    """Characterization-table formula: floor at landing row i+1 of event i."""
    return (W - i - 2) - b[i]

kstar = next(r for r in range(1, 1001) if flooring(r) < J_MIN)
print()
print(f'(a) WIDTH-DEGRADATION CAVEAT  (J_min = {J_MIN})')
print(f'k* = {kstar}   (first row r with flooring(r) = (W-r-1) - b[r-1] < {J_MIN})')
print(f'    flooring({kstar}) = {flooring(kstar)};  '
      f'flooring before it: flooring({kstar-1}) = {flooring(kstar-1)}')
print(f'    note: all rows r >= {kstar} have flooring = {flooring(kstar)} exactly '
      f'(block glued to the finite right edge, one-column-per-row retraction)')
below = [r for r in range(1, 1001) if flooring(r) < J_MIN]
print(f'    rows with flooring < {J_MIN}: {below[0]}..{below[-1]} '
      f'({len(below)} rows)')

GIANTS = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161]
print('\nflooring across the 13 giant event rows (1-based row i, event row '
      'and landing row i+1):')
print('  i  |   b_i       | b_{i+1}     | event-row  | landing-row | '
      'genuine?')
REF_TABLE = {34: 1_268_392, 56: 1_264_607, 64: 1_247_276, 68: 1_239_038,
             94: 1_177_891, 96: 1_166_536, 110: 1_128_789, 112: 998_864,
             126: 945_389, 130: 754_569, 134: 536_907, 146: 176_186, 161: 0}
for i in GIANTS:
    assert b[i] > b[i - 1], i                     # step law at this row
    ev = flooring(i)
    ld = landing_floor(i)
    assert ld == REF_TABLE[i], (i, ld, REF_TABLE[i])   # exact cross-check
    genuine = 'no (capped)' if i == 161 else 'yes'
    print(f'{i:3d} | {b[i-1]:10d} | {b[i]:10d} | {ev:11d} | {ld:11d} | '
          f'{genuine}')
print(f'  (landing-row floors above match the characterization table exactly '
      f'for all 13)')
print(f'  => minimum event-row flooring among the giants = {min(flooring(i) for i in GIANTS)} '
      f'(row {min(GIANTS, key=flooring)}) — all far above {J_MIN}')

print('\nfirst row past each giant where flooring < 1000:')
for i in GIANTS:
    found = None
    for r in range(i + 1, 1001):
        if flooring(r) < J_MIN:
            found = r
            break
    tag = ('landing row immediately below threshold (capped event)'
           if i == 161 else 'row 162 = k* (not this giant; degradation is global)')
    print(f'  event row i={i:3d}: first row past it with flooring < {J_MIN}: '
          f'row {found}   [{tag}]')

# ---------------- (b) geometric growth test ----------------
events = [j for j in range(1, len(b)) if b[j] > b[j - 1]]   # 1-based event rows
GENUINE = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146]
assert events.count(161) == 1 and all(i in events for i in GIANTS)
print()
print(f'(b) GEOMETRIC GROWTH TEST')
print(f'step-law events (1-based rows i with b[i] > b[i-1] in the b array): '
      f'{len(events)} total')
print(f'    {events}')
print(f'    the 13 giants (j > 1000) are {GIANTS}; 12 genuine, i=161 capped.')

def fit_ols(xs, ys):
    """Exact least squares y = a + m*x on Fractions; returns m, a, r2,
    fitted values, residuals."""
    n = len(xs)
    Sx, Sy = sum(xs), sum(ys)
    Sxx = sum(x * x for x in xs)
    Sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * Sxx - Sx * Sx
    m = Fraction(n * Sxy - Sx * Sy, den)
    a = Fraction(Sy - m * Sx, n)
    fitted = [a + m * x for x in xs]
    res = [y - f for f, y in zip(fitted, ys)]
    mean = Fraction(Sy, n)
    SStot = sum((y - mean) ** 2 for y in ys)
    SSres = sum(r * r for r in res)
    r2 = Fraction(1) - SSres / SStot if SStot else Fraction(1)
    return m, a, r2, fitted, res

def report(name, event_rows):
    n = len(event_rows)
    xs = list(range(n))
    yb = [b[i] for i in event_rows]                      # post-jump blocks
    yl = [math.log(y) for y in yb]                       # log base e
    m1, a1, r2_1, fit1, res1 = fit_ols(xs, [Fraction(v) for v in yl])
    m2, a2, r2_2, fit2, res2 = fit_ols(xs, [Fraction(v) for v in yb])
    print(f'\n  --- {name}: n = {n}  (event rows {event_rows[0]}..'
          f'{event_rows[-1]}, post-jump blocks b[i] = '
          f'{yb[0]}..{yb[-1]}) ---')
    print('  per-step ratios b_next/b_prev (consecutive post-jump blocks):')
    for k in range(n):
        if k == 0:
            print(f'    i={event_rows[k]:3d}: b={yb[k]:9d}  (first)')
        else:
            r = Fraction(yb[k], yb[k - 1])
            print(f'    i={event_rows[k]:3d}: b={yb[k]:9d}  ratio={float(r):.4f} '
                  f'({r.numerator}/{r.denominator})')
    m1f, a1f = float(m1), float(a1)
    m2f, a2f = float(m2), float(a2)
    print(f'  GEOMETRIC (log b vs index): slope = {m1f:+.6f} (= log growth per '
          f'event), intercept = {a1f:.6f}')
    print(f'    R^2 = {float(r2_1):.6f}; fitted log b: '
          + ' '.join(f'{float(v):.4f}' for v in fit1))
    print(f'    residuals (log): ' + ' '.join(f'{float(v):+.4f}' for v in res1))
    print(f'    doubling factor = 2^(slope/ln2) = {2 ** (m1f / math.log(2)):.4f} '
          f'per event  (x{2 ** (m1f / math.log(2)):.2f}/event)')
    print(f'  LINEAR (b vs index): slope = {m2f:+.2f}, intercept = {a2f:.1f}')
    print(f'    R^2 = {float(r2_2):.6f}; fitted b: '
          + ' '.join(f'{int(round(float(v)))}' for v in fit2))
    print(f'    residuals (b): ' + ' '.join(f'{float(v):+.1f}' for v in res2))
    winner = 'GEOMETRIC' if r2_1 > r2_2 else ('LINEAR' if r2_2 > r2_1 else 'TIE')
    print(f'  VERDICT: R^2_geom = {float(r2_1):.6f} vs R^2_lin = '
          f'{float(r2_2):.6f} -> {winner} wins by {abs(float(r2_1 - r2_2)):.6f}')
    return m1f, a1f, float(r2_1), m2f, a2f, float(r2_2), yb

g = report('GENUINE 12 (drop capped i=161)', GENUINE)
a_all = report('ALL 13 (incl. capped i=161) — robustness check',
               GIANTS)
print()
print(f'SUMMARY: genuine-12 geometric slope = {g[0]:+.6f}, doubling factor = '
      f'{2 ** (g[0] / math.log(2)):.4f}/event; R^2_geom={g[2]:.6f} vs '
      f'R^2_lin={g[5]:.6f}')
print(f'         all-13  geometric slope = {a_all[0]:+.6f}, doubling factor = '
      f'{2 ** (a_all[0] / math.log(2)):.4f}/event; R^2_geom={a_all[2]:.6f} vs '
      f'R^2_lin={a_all[5]:.6f}')
print('DONE')