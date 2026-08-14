#!/usr/bin/env python3
"""
minkowski_growth_fit.py

Exact polynomial fit of the measured Minkowski-sum census counts
(code/out/spindle_minkowski_census_k{1..6}.captured.txt):

    k : 1     2     3     4     5     6
    n : 7    26    70   155   301   532
    e : 11   69   240   628  1375  2659

Questions settled exactly here (Fraction arithmetic, no floats):

  1. Is n(k) a quartic polynomial in k?  Fit degree 4 through k=1..5 and
     evaluate at k=6: if the predicted value equals the measured 532, the
     degree-4 model survives an out-of-sample check (fit on 1..5, tested on
     6). Report the exact rational coefficients.
  2. What is the degree of the monic leading term of the degree-5
     interpolation through all six points?  If the k^5 coefficient is
     exactly 0, the quartic fit is exact for all measured k; if not, report
     its value as the failure of quarticity.

This is a check on measured data, not a proof about the infinite family
A^1, A^2, ... — the fit is reported as computed-and-checked for k <= 6 only.
"""

from fractions import Fraction as F

n_measured = {1: 7, 2: 26, 3: 70, 4: 155, 5: 301, 6: 532}
e_measured = {1: 11, 2: 69, 3: 240, 4: 628, 5: 1375, 6: 2659}


def interpolate(points_x, points_y):
    """ Lagrange interpolation with Fraction arithmetic over x = 1..m.
        points_x, points_y: equal-length lists. Returns coefficients of the
        polynomial in x, lowest degree first. """
    m = len(points_x)
    # build via Lagrange basis
    coeffs = [F(0)] * m
    for i in range(m):
        xi = points_x[i]
        # basis poly L_i(x) = prod_{j!=i} (x - xj)/(xi - xj)
        num = [F(1)]
        den = F(1)
        for j in range(m):
            if j == i:
                continue
            xj = points_x[j]
            # multiply num by (x - xj):  new[t] = old[t-1] - xj*old[t]
            old = num
            num = [F(0)] * (len(old) + 1)
            for t in range(len(num)):
                if t >= 1:
                    num[t] += old[t - 1]
                if t < len(old):
                    num[t] -= xj * old[t]
            den *= (xi - xj)
        yi = points_y[i]
        for d in range(m):
            coeffs[d] += num[d] * yi / den
    return coeffs


def evaluate(coeffs, x):
    acc = F(0)
    for d, c in enumerate(coeffs):
        acc += c * (x ** d)
    return acc


def main():
    xs = list(range(1, 7))
    print("=== n(k): fit degree 4 through k=1..5, test at k=6 ===")
    n4 = interpolate(xs[:5], [n_measured[k] for k in xs[:5]])
    pred6 = evaluate(n4, 6)
    print(f"quartic coefficients (lowest first): "
          f"{[str(c) for c in n4]}")
    print(f"predicted n(6) = {pred6}   measured n(6) = {n_measured[6]}   "
          f"match? {pred6 == n_measured[6]}")

    print()
    print("=== n(k): degree-5 interpolation through all six points ===")
    n5 = interpolate(xs, [n_measured[k] for k in xs])
    print(f"k^5 coefficient = {n5[5]}   "
          f"(0 means the quartic model is exact on k=1..6)")

    print()
    print("=== e(k): degree-5 fit, leading coefficients ===")
    e5 = interpolate(xs, [e_measured[k] for k in xs])
    print(f"k^5 coeff = {e5[5]},  k^4 coeff = {e5[4]},  k^3 coeff = {e5[3]}")

    print()
    print("=== measured table (recap) ===")
    print(f"{'k':>2} {'n':>5} {'e':>6} {'e/n':>8}")
    for k in range(1, 7):
        ratio = F(e_measured[k]) / n_measured[k]
        print(f"{k:>2} {n_measured[k]:>5} {e_measured[k]:>6} "
              f"{(ratio.numerator / ratio.denominator):>8.4f}")
    print()
    print("GROWTH FIT DONE.")


if __name__ == "__main__":
    main()