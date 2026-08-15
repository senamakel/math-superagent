#!/usr/bin/env python3
"""Calibration driver for the flat-torus periodic-colouring attack (adopted
approach flat-torus-periodic-6col.md), the smallest unfinished item with the
machinery (`code/lib/torus_margin.py`) already built but never captured.

Delegates the real work to lib.torus_margin and captures it to
code/out/calibrate_torus_margin.captured.txt.  This is the file TASKS.md
marks as "waiting on code/out/torus_margin.captured.txt".
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from lib.torus_margin import run_calibration, check_F_k_colourable, index7_sublattice, a2_seven_colouring_margin
import sympy as sp


def main():
    lines, results = run_calibration()

    # Re-derive the two exact critical values independently for the report.
    m = a2_seven_colouring_margin()
    factor = m["same_colour_centre_factor"]
    assert sp.simplify(factor - sp.sqrt(21)) == 0

    print("\n".join(lines))
    print("\nINDEPENDENT CROSS-CHECK:")
    print("  same_colour_centre_factor =", factor, "~", sp.N(factor, 10))
    print("  expected sqrt(21) ~", sp.N(sp.sqrt(21), 10))
    ok = sp.simplify(factor - sp.sqrt(21)) == 0
    print("  factor == sqrt21 :", ok)

    # 6-colourability of the canonical index-7 F in-window, as a final explicit verdict.
    basis, index = index7_sublattice()
    L = sp.Rational(2, 5)
    D, sat6, w6, t6, edges = check_F_k_colourable(basis, L, index, 6)
    D2, sat7, w7, t7, edges2 = check_F_k_colourable(basis, L, index, 7)
    print(f"\nFINAL VERDICT at L=2/5 (in window): chi(F) == 7 "
          f"(6-col? {sat6}, 7-col? {sat7}); edges on {D} vertices = {len(edges)}")


if __name__ == "__main__":
    main()
