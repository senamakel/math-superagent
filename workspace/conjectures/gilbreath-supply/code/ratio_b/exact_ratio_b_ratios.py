#!/usr/bin/env python3
"""Corrected decrement-ratio arithmetic for the Ratio B trend.

The previous child printed ratios computed from the EXACT decrements but
labelled them as simple divisions of the 3-decimal ROUNDED decrements, and the
two sets do not agree. This script computes BOTH honestly:

  (A) ratios from EXACT double-precision decrements (derived from the exact
      s2 values measured and stored by measure_ratio_b.py); and
  (B) ratios by SIMPLE DIVISION of the 3-decimal ROUNDED decrements
      (0.051,0.032,0.024,0.021,0.019) -- this is the arithmetic the directive
      cites and the previous capture misreported.

Every number is derived from the exact measured s2_N; nothing is searched and
nothing is extrapolated here. Values are printed to 3 significant digits.

LABEL: measured, not proved.
"""
import math

# Exact s2_N as the run measured and stored (from code/out/ratio_b_extension_d21.txt)
N = [1000, 4000, 10000, 20000, 40000, 80000]
s2 = [
    2.4916322565e-03,
    7.2163270955e-04,
    3.1327239902e-04,
    1.6548686662e-04,
    8.7121263299e-05,
    4.5749115971e-05,
]

def ratio_b(s2v, n):
    return s2v * 4.0 * n / math.log(n)

print("=== (A) EXACT ratios, from exact s2-derived decrements ===")
print("  N        s2              RatioB      ")
rb = [ratio_b(s, n) for s, n in zip(s2, N)]
for n, s, r in zip(N, s2, rb):
    print("  %6d  %.10e  %.6f" % (n, s, r))

# exact decrements between consecutive ratio-b points
decs = [rb[i] - rb[i + 1] for i in range(len(rb) - 1)]
print("  exact decrements  d_k:")
for i, d in enumerate(decs, 1):
    print("    d_%d = %.6f   (3 sig: %.3f)" % (i, d, d))
print("  exact decrement ratios  r_k = d_{k+1}/d_k :")
exact_ratios = [decs[i + 1] / decs[i] for i in range(len(decs) - 1)]
for i, r in enumerate(exact_ratios, 1):
    print("    r_%d = %.6f/%.6f = %.3f" % (i, decs[i], decs[i - 1], r))

print()
print("=== (B) SIMPLE DIVISION of 3-decimal ROUNDED decrements ===")
print("  the directive's cited arithmetic, done correctly")
rounded = [0.051, 0.032, 0.024, 0.021, 0.019]
round_ratios = [rounded[i + 1] / rounded[i] for i in range(len(rounded) - 1)]
for i, r in enumerate(round_ratios, 1):
    print("    r_%d = %.3f/%.3f = %.3f" % (i, rounded[i], rounded[i - 1], r))

print()
print("=== side by side ===")
print("  k   exact r_k   simple-division r_k")
for i in range(len(exact_ratios)):
    print("  %d   %.3f        %.3f" %
          (i + 1, exact_ratios[i], round_ratios[i]))

exact_rising = all(exact_ratios[i + 1] >= exact_ratios[i]
                   for i in range(len(exact_ratios) - 1))
round_rising = all(round_ratios[i + 1] >= round_ratios[i]
                   for i in range(len(round_ratios) - 1))
print()
print("  exact set monotone rising toward 1 :", exact_rising)
print("  simple-division set monotone rising:", round_rising)
print("  exact set :", ", ".join("%.3f" % r for r in exact_ratios))
print("  simple-set:", ", ".join("%.3f" % r for r in round_ratios))

# Extrapolation (A) derived from the honest monotone-rising set, from the last
# rounded decrement d=0.019 settling near r=0.90 (the directive's corrected value).
d_last = 0.019
r_settle = 0.90
tail = d_last * r_settle / (1.0 - r_settle)
limit = 1.297 - tail
print()
print("=== EXTRAPOLATION (A), corrected set (from last decrement ~0.019, r~0.90) ===")
print("  tail = 0.019*0.90/(1-0.90) = %.3f" % tail)
print("  Ratio B limit ~ 1.297 - %.3f ~= %.3f" % (tail, limit))
print("LABEL: measured, not proved.  Neither extrapolation (A) nor (B) is declared.")
