#!/usr/bin/env python3
"""Naive oracle for Project Euler 493.

Problem: 70 balls in an urn, 10 of each of the 7 rainbow colours.
We draw 20 balls uniformly without replacement.  What is the expected
number of *distinct colours* among the drawn balls?

The statement gives no smaller worked example, so this oracle does two
things:

  1. PINS DOWN THE DEFINITION on small instances.  For (c colours, m
     balls each, k drawn) it exhaustively enumerates every k-subset of
     the c*m labelled balls, counts the distinct colours in each, and
     averages.  This is the obviously-correct reading of the problem.

  2. CROSS-CHECKS the exact linearity-of-expectation formula
         E = c * (1 - C((c-1)*m, k) / C(c*m, k))
     against that exhaustive average on the small instances.  When they
     agree on a range of (c,m,k), the formula is pinned as correct and
     is then evaluated exactly on the real problem (7,10,20).

Exact integer/rational arithmetic throughout (Python fractions).
"""

import itertools
import math
from fractions import Fraction

import sys

def exhaustive_expected(c, m, k):
    """Average number of distinct colours over all C(c*m, k) draws.

    Trivially correct: enumerate every possible set of labelled balls.
    Only usable when C(c*m, k) is small.
    """
    colour_of = [i // m for i in range(c * m)]  # ball i has colour i//m
    total = 0
    count = 0
    for subset in itertools.combinations(range(c * m), k):
        distinct_colours = len({colour_of[i] for i in subset})
        total += distinct_colours
        count += 1
    return Fraction(total, count)

def linearity_expected(c, m, k):
    """E = c * P(one given colour is drawn)
             = c * (1 - C((c-1)m, k) / C(c*m, k)).
    """
    absent = math.comb((c - 1) * m, k)
    present_all = math.comb(c * m, k)
    p_colour = Fraction(1) - Fraction(absent, present_all)
    return c * p_colour

def main():
    print("=== Part 1: pin down the definition on small instances ===")
    small = [
        (1, 10, 5),        # one colour: every non-empty draw has 1 distinct colour
        (2, 2, 2),         # two colours, two balls each, draw 2
        (2, 3, 3),
        (3, 2, 2),
        (3, 2, 3),
        (3, 3, 3),
        (2, 10, 10),       # draw every ball cap (2*10 choose 10 = 184756 ok)
        (3, 2, 4),         # draw all four of six? no: k=4 of 6
    ]
    all_ok = True
    for (c, m, k) in small:
        comb = math.comb(c * m, k)
        print(f"\nc={c} m={m} k={k}  (C({c*m},{k}) = {comb} subsets)")
        if comb > 2_000_000:
            print("  too large to enumerate; skipping exhaustive check")
            continue
        e_exh = exhaustive_expected(c, m, k)
        e_lin = linearity_expected(c, m, k)
        match = (e_exh == e_lin)
        all_ok = all_ok and match
        print(f"  exhaustive = {float(e_exh):.8f}  ({e_exh})")
        print(f"  linearity  = {float(e_lin):.8f}  ({e_lin})")
        print(f"  MATCH: {match}")

    print("\n=== Part 2: real problem (7,10,20) by the cross-checked formula ===")
    c, m, k = 7, 10, 20
    E = linearity_expected(c, m, k)
    print(f"E = {E}")
    print(f"E as float = {float(E):.12f}")
    print(f"nine digits after decimal point: {float(E):.9f}")
    print("\nexhaustive matches formula on all small cases:", all_ok)

if __name__ == "__main__":
    main()
