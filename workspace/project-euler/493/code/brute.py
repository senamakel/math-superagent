"""Naive exact computation of expected number of distinct colours.

70 balls, 7 colours labelled 0..6, 10 balls per colour (k=10). Draw 20
without replacement uniformly over all C(70,20) subsets. Compute E[#distinct
colours] exactly with fractions.

Route (a): closed form E = 7*(1 - C(60,20)/C(70,20)).
Route (b): independent algebraic / inclusion-exclusion route over colour
subsets (only 2^7 = 128 subsets, no blowup): for each |S|=d the number of
20-subsets whose colour-set is exactly S is
    sum_{j=0}^{d} (-1)^{d-j} C(d,j) C(k*j, 20),
valid since k*|S| >= 20 for d>=2 and handled separately for d=1.
E = [sum_d d * C(7,d) * (exact count for d)] / C(70,20).
"""
from fractions import Fraction
from math import comb

K = 10      # balls per colour
N_COL = 7   # number of colours
TOTAL = 70  # balls
N = 20      # balls drawn

def closed_form():
    return N_COL * (1 - Fraction(comb(60, N), comb(70, N)))

def count_exact_d(d):
    """# of 20-subsets whose colour set is exactly S for a fixed |S|=d."""
    # Inclusion-exclusion: sum_{j=0}^{d} (-1)^{d-j} C(d,j) C(k*j, 20)
    # C(k*j,20) is 0 when k*j < 20, so that term contributes nothing.
    total = 0
    for j in range(0, d + 1):
        term = comb(d, j) * comb(K * j, N)
        if (d - j) % 2 == 1:
            total -= term
        else:
            total += term
    return total

def brute_route():
    total_draws = comb(TOTAL, N)
    # expected value = sum over d of d * (#draws with exactly d colours) / total
    numerator = 0
    for d in range(1, N_COL + 1):
        per_subset = count_exact_d(d)
        num_subsets = comb(N_COL, d)
        numerator += d * num_subsets * per_subset
    return Fraction(numerator, total_draws)

def main():
    a = closed_form()
    b = brute_route()
    print("brute.py")
    print("  closed form                 =", a)
    print("  closed form decimal         =", float(a))
    print("  brute-force exact           =", b)
    print("  brute-force decimal         =", float(b))
    print("  routes equal                =", a == b)
    print("  exact Fraction (brute)      =", b)

if __name__ == "__main__":
    main()
