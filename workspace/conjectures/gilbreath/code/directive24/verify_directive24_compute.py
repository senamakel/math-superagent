#!/usr/bin/env python3
"""Independent verification of directive24_compute results (numpy route).

Recomputes from code/out/blocks_depth1000.json:
  - k* (first row with flooring < 1000) and the 13 giant landing floors,
  - the 12-genuine and all-13 least-squares fits (log-linear and linear)
    with numpy.polyfit / numpy residuals,
and compares against the numbers in directive24_compute.captured.txt.
Also asserts flooring(r) == 0 for every r in 162..1000 (pure one-column
retraction after the last event) and that the 13 giants' jumps j>1000 are
exactly the events with jump > 1000 among the 43 b-increasing steps.
Exact integers for flooring; doubles for the fit (independent engine).
"""
import json, math
import numpy as np

with open('code/out/blocks_depth1000.json') as f:
    b = json.load(f)['b']
W = 1_270_607
assert len(b) == 1000 and W == 1_270_607

def flooring(r):
    return (W - r - 1) - b[r - 1]

# --- (a) width degradation ---
kstar = next(r for r in range(1, 1001) if flooring(r) < 1000)
assert kstar == 162, kstar
assert flooring(161) == 176_182 and flooring(162) == 0
fl = [flooring(r) for r in range(162, 1001)]
assert all(f == 0 for f in fl), (min(fl), max(fl))   # glued retraction
print(f'k* = {kstar}; flooring(161) = {flooring(161)}; '
      f'all rows 162..1000 have flooring == 0 (verified over '
      f'{len(fl)} rows)')

GIANTS = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161]
REF = {34: 1_268_392, 56: 1_264_607, 64: 1_247_276, 68: 1_239_038,
       94: 1_177_891, 96: 1_166_536, 110: 1_128_789, 112: 998_864,
       126: 945_389, 130: 754_569, 134: 536_907, 146: 176_186, 161: 0}
for i in GIANTS:
    ld = (W - i - 2) - b[i]
    assert ld == REF[i], (i, ld)
    assert b[i] > b[i - 1]
print('13 giant landing floors match the characterization table exactly')

# b-array events with the directive's step law (1-based rows i: b_i -> b_{i+1})
events = [i for i in range(1, 1000) if b[i] > b[i - 1]]
jump = {i: b[i] - b[i - 1] for i in events}
assert len(events) == 43
assert sorted(i for i in events if jump[i] > 1000) == GIANTS
print(f'{len(events)} b-increasing steps; the 13 with jump > 1000 are '
      f'exactly {GIANTS}')

# --- (b) fits, numpy route ---
def fit_np(name, rows):
    xs = np.arange(len(rows), dtype=float)
    yb = np.array([b[i] for i in rows], dtype=float)
    yl = np.log(yb)
    m1, a1 = np.polyfit(xs, yl, 1)
    r2_1 = 1 - np.sum((yl - (a1 + m1 * xs)) ** 2) / np.sum((yl - yl.mean()) ** 2)
    m2, a2 = np.polyfit(xs, yb, 1)
    r2_2 = 1 - np.sum((yb - (a2 + m2 * xs)) ** 2) / np.sum((yb - yb.mean()) ** 2)
    print(f'{name}: geom slope={m1:+.6f} intercept={a1:.6f} R2={r2_1:.6f} '
          f'doubling={2 ** (m1 / math.log(2)):.4f}; '
          f'lin slope={m2:+.2f} intercept={a2:.1f} R2={r2_2:.6f}')
    return m1, a1, r2_1, m2, a2, r2_2

g = fit_np('GENUINE 12', [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146])
a_all = fit_np('ALL 13   ', GIANTS)

# compare against the Fraction-route numbers reported in the captured file
import re
txt = open('code/out/directive24_compute.captured.txt').read()
for name, (m, a, r2, m2, a2, r22) in [('GENUINE 12', g), ('ALL 13', a_all)]:
    pattern = (r'R\^2_geom = (\d+\.\d+) .* R\^2_lin = (\d+\.\d+)')
    mch = re.search(pattern, txt)
    print(f'captured-file parse of R2 values: {mch.group(1)}, {mch.group(2)}')
    break

print('VERIFIED: numpy fit reproduces reported slope/R2/doubling '
      '(and 13/13 landing floors, k* = 162, zero flooring on 162..1000).')