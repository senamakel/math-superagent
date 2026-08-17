"""Fit a closed form for N(i;k) = # distinct length-k factors with 1 at position i.

From verification: N(i;k) in {floor((k+1)a), ceil((k+1)a)}, a=(3-sqrt5)/2.
We now characterize exactly WHICH i have the +1 (ceil) value, trying candidate
mechanical/floor forms in (k,i), and checking against all k<=40.

We also confirm sum_i N(i;k) = sum_j (ones in factor j) as a cross-check, and
characterize the +1 (ceil) column sets as the empirical function.
"""
import json
import os
from mpmath import mp, mpf, sqrt, floor

mp.dps = 60
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
ALPHA = mpf(3) / 2 - sqrt(5) / 2  # = 1/phi^2


def load():
    return json.load(open(DATA))


def main():
    data = load()

    print("N(i;k) and its +1 (ceil) column set for k=1..40\n")
    ceil_sets = {}
    for k in range(1, 41):
        facs = data[str(k)]
        N = [sum(1 for f in facs if f[i] == '1') for i in range(k)]
        lo = int(floor(mpf(k + 1) * ALPHA))
        plus = [i for i, n in enumerate(N) if n == lo + 1]
        ceil_sets[k] = set(plus)
        # cross-check sum
        total_cols = sum(N)
        total_rows = sum(sum(1 for c in f if c == '1') for f in facs)
        assert total_cols == total_rows, (k, total_cols, total_rows)
        print(f"k={k:2d}: (k+1)*a={mp.nstr((k+1)*ALPHA,8):>10} floor={lo} | +1 columns (ceil) = {plus}")

    print()
    print("Hypothesis A: +1 set = {{ i : floor((i+1)*t) - floor(i*t) == 1 }} (mechanical word)")
    print("Hypothesis B: +1 set = {{ i : {i*ALPHA + c} < \u03b5 }} (fractional near integer)")
    print("Test several t / c candidates against all k<=40:")

    # t candidates: try t in [ALPHA*n for small n], and c in a set
    from itertools import product
    t_cands = [ALPHA, 2 * ALPHA, ALPHA * 1.5, 1 - ALPHA, (mpf(1) - ALPHA) / 2,
               ALPHA * 2.618, mpf(1) / 3, mpf(1) / 5, mpf(1) / 4]
    thresh = mpf('1e-12') if False else mpf('0.001')

    best = None
    for t in t_cands:
        mismatch = 0
        for k in range(1, 41):
            pred = {i for i in range(k)
                    if (frac((i + 1) * t) < 1 and floor((i + 1) * t) - floor(i * t) == 1)}
            if pred != ceil_sets[k]:
                mismatch += 1
        if best is None or mismatch < best[0]:
            best = (mismatch, 't', t)
        print(f"  t={mp.nstr(t,8)}: mismatched-k = {mismatch}")

    print("best:", best)


def frac(x):
    return x - floor(x)


if __name__ == "__main__":
    main()
