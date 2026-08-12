"""Efficient exact solution: E = 7*(1 - C(60,20)/C(70,20)).

70 balls, 7 colours (labels 0..6), 10 per colour, draw 20 without
replacement. Exact rational arithmetic via fractions.Fraction and math.comb.
Cross-checks equality against brute.py's independent result and prints the
answer to 9 decimals.
"""
from fractions import Fraction
from math import comb
import brute

N_COL = 7
N = 20

def expected():
    return N_COL * (1 - Fraction(comb(60, N), comb(70, N)))

def main():
    E = expected()
    Brute = brute.brute_route()
    print("solution.py")
    print("  exact Fraction (solution)   =", E)
    print("  decimal                     =", float(E))
    print("  matches brute.py exactly    =", E == Brute)
    # Round to 9 decimals
    nines = int(round(float(E) * 10**9))
    print("  answer to 9 decimals        = %d.%09d" % (nines // 10**9, nines % 10**9))
    # more digits
    print("  more digits                 = %.15f" % float(E))

if __name__ == "__main__":
    main()
