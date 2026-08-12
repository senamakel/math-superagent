#!/usr/bin/env python3
"""Run the naive oracle code/brute.py against every worked example in the
PE597 statement.

Part A (deterministic, exact): construct an Exp(1) speed triple for each of the
five n=3,L=160 rows that realizes exactly that bump pattern, then check brute's
simulated (new order, parity) against the statement's table.

Part B (MC): estimate the five row probabilities and p(3,160) over iid Exp(1)
speeds; they must land near 4/15, 8/45, 1/3, 4/27, 2/27 and 56/135, and sum to 1.

Part C (MC): estimate p(4,400) near the given 0.5107843137.

This is a check of the oracle's meaning, not the efficient method.
"""
import math
import random
from fractions import Fraction

from brute import simulate_order, parity_of_new_order, outcome_parity

EXPECTED = [
    # (speeds realizing the row, expected order, expected parity, fraction)
    ([1.0, 1.0, 1.0],        [0, 1, 2], 0, Fraction(4, 15)),
    ([1.0, 1.6, 1.0],        [0, 2, 1], 1, Fraction(8, 45)),
    ([2.0, 1.0, 1.0],        [1, 0, 2], 1, Fraction(1, 3)),
    ([2.0, 1.6, 0.5],        [2, 0, 1], 0, Fraction(4, 27)),
    ([3.0, 1.6, 1.0],        [2, 1, 0], 1, Fraction(2, 27)),
]

def check_partA():
    print("=== Part A: deterministic new order + parity per row (n=3, L=160) ===")
    all_ok = True
    for i, (spd, exp_order, exp_par, frac) in enumerate(EXPECTED, 1):
        above = simulate_order(3, 160, spd)
        par, order = parity_of_new_order(3, above)
        ok = (par == exp_par) and (list(order) == exp_order)
        all_ok &= ok
        print(f"row {i}: speeds={spd} new_order={list(order)} (expect {exp_order}) "
              f"parity={par} (expect {exp_par}) prob-want={frac} -> {'MATCH' if ok else 'MISMATCH'}")
    print(f"Part A: {'ALL 5 MATCH' if all_ok else 'SOME MISMATCH'}")
    return all_ok

def partB(n_samples=400_000, seed=1):
    print(f"\n=== Part B: MC row probabilities + p(3,160) over {n_samples} Exp(1) samples ===")
    rng = random.Random(seed)
    counts = [0]*5          # by expected-row index
    def classify(order):
        # map observed ascending order to expected row
        if list(order) == [0,1,2]: return 0
        if list(order) == [0,2,1]: return 1
        if list(order) == [1,0,2]: return 2
        if list(order) == [2,0,1]: return 3
        if list(order) == [2,1,0]: return 4
        return -1
    n_even = 0
    for _ in range(n_samples):
        spd = [-math.log(rng.random()) for _ in range(3)]
        above = simulate_order(3, 160, spd)
        par, order = parity_of_new_order(3, above)
        if par == 0:
            n_even += 1
        c = classify(list(order))
        if c >= 0:
            counts[c] += 1
    print("row | MC-prob | exact")
    names = ["none","B->C","A->B","B->C,A->C","A->B,B->C"]
    for i in range(5):
        mc = counts[i]/n_samples
        print(f"  {names[i]:<12} {mc:.6f}  {float(EXPECTED[i][3]):.6f}")
    even = n_even/n_samples
    print(f"p(3,160) MC = {even:.6f}   exact = {float(Fraction(56,135)):.6f}")
    print(f"sum of row probs = {sum(counts)/n_samples:.6f} (unclassified decays at default float only)")
    return even

def partC(n_samples=400_000, seed=2):
    print(f"\n=== Part C: MC p(4,400) over {n_samples} Exp(1) samples ===")
    rng = random.Random(seed)
    n_even = 0
    for _ in range(n_samples):
        spd = [-math.log(rng.random()) for _ in range(4)]
        if outcome_parity(4, 400, spd) == 0:
            n_even += 1
    est = n_even/n_samples
    se = math.sqrt(est*(1-est)/n_samples)
    print(f"p(4,400) MC = {est:.6f} +/- {se:.6f}   given = 0.5107843137")
    return est

if __name__ == "__main__":
    okA = check_partA()
    partB()
    partC()
