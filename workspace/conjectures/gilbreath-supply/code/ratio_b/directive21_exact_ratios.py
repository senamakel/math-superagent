#!/usr/bin/env python3
"""Directive 21 — exact decrement-ratio arithmetic for Ratio B.

The premature print in code/out/ratio_b_extension_d21.txt printed decrements
rounded to 3 decimals as the OPERANDS of ratio equations, but computed the
QUOTIENTS from the unrounded values. 0.021/0.024 = 0.875 while the quoted
quotient was 0.899, and 0.019/0.021 = 0.905 while the quoted quotient was
0.878: the printed equations were false, and the two readings (rising-centred
simple-division set vs dipping exact set) lean opposite ways.

This script does it honestly: every decrement is taken from the SAME exact
measured s2_N values used to make RatioB, and every ratio is the quotient of
two of those exact decrements, so the operands actually produce the quotient.

- RatioB(N) = s2_N * 4N / ln N   (identical formula to measure_ratio_b.py)
- d_k = RatioB[k] - RatioB[k+1]  (per ~2x-doubling decrement)
- r_k = d_{k+1} / d_k, k = 1..4

Nothing is searched, rounded to hide a set, or extrapolated. The only numbers
printed as data are derived here from the given s2_N. LABEL: measured, not
proved.
"""
import math
import os
import tempfile

N = [1000, 4000, 10000, 20000, 40000, 80000]
S2 = [
    2.4916322565e-03,
    7.2163270955e-04,
    3.1327239902e-04,
    1.6548686662e-04,
    8.7121263299e-05,
    4.5749115971e-05,
]

def ratio_b(s2v, n):
    return s2v * 4.0 * n / math.log(n)

def build():
    RB = [ratio_b(s, n) for s, n in zip(S2, N)]

    lines = []
    A = lines.append
    A("=== Directive 21 — EXACT decrement-ratio arithmetic (from given s2_N) ===")
    A("")
    A("  N        s2_N              RatioB = s2*4N/lnN")
    for n, s, r in zip(N, S2, RB):
        A("  %6d  %.10e  %.10f" % (n, s, r))
    A("")

    # exact per-doubling decrements (full precision)
    decs = [RB[i] - RB[i + 1] for i in range(len(RB) - 1)]
    A("=== PER-DOUBLING DECREMENTS (exact, full precision) ===")
    A("  k   from->to      d_k = RatioB[k]-RatioB[k+1]")
    for i, d in enumerate(decs):
        A("  d_%d   %5d -> %5d   %.10f" % (i + 1, N[i], N[i + 1], d))
    A("")

    # exact decrement ratios from the SAME full-precision decrements
    ratios = [decs[i + 1] / decs[i] for i in range(len(decs) - 1)]
    A("=== DECREMENT RATIOS r_k = d_{k+1}/d_k  (same full-precision operands) ===")
    for i, r in enumerate(ratios):
        A("  r_%d = %.6f / %.6f = %.9f" % (i + 1, decs[i + 1], decs[i], r))
    A("")
    A("  r_1 = %.9f" % ratios[0])
    A("  r_2 = %.9f" % ratios[1])
    A("  r_3 = %.9f" % ratios[2])
    A("  r_4 = %.9f" % ratios[3])
    A("")

    # (3) direction of final ratio vs the previous one
    if ratios[3] > ratios[2]:
        move = "r_4 RISES relative to r_3"
    elif ratios[3] < ratios[2]:
        move = "r_4 FALLS relative to r_3"
    else:
        move = "r_4 equals r_3"
    A("=== (3) DIRECTION: %s ===" % move)
    A("  r_3 = %.9f   r_4 = %.9f" % (ratios[2], ratios[3]))
    A("")

    # (5) operator's approximations are NOT data; do not print them.
    A("=== (4) HONEST READING (depends on the single number above) ===")
    if ratios[3] < ratios[2]:
        A("  The last ratio r_4 FALLS below r_3. To be precise: neither limit is")
        A("  favoured by this final step — `limit of Ratio B = 1` (uniform) and")
        A("  `limit > 1` (constant above 1) both remain open; 6 points cannot")
        A("  separate them. A sub-1 last ratio would lean toward a convergent")
        A("  tail (limit > 1), but the evidence is thin and nothing is declared.")
    else:
        A("  The last ratio r_4 does not fall below r_3; see full values above.")
    A("")
    A("LABEL: measured, not proved.  Operator approximations (0.63,0.75,0.875,")
    A("0.905) are deliberately NOT repeated as data; the exact values above are")
    A("the record.")
    return "\n".join(lines) + "\n"

def main():
    text = build()
    # atomic capture: write temp, fsync, os.replace on success
    out = "/workspace/code/out/directive21_exact_ratios.captured.txt"
    fd, tmp = tempfile.mkstemp(dir="/workspace/code/out",
                               prefix=".d21_tmp_", suffix=".txt")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, out)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    print(text, end="")
    print(">> captured atomically to", out)

if __name__ == "__main__":
    main()
