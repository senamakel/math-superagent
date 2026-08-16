#!/usr/bin/env python3
"""Verify residue constraint and min positive admissible n3 for Reimbayev 62."""
from fractions import Fraction
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

FAMILY = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]
print("family        cap(ana=v k(k-2)/4)  period  good_residues  min_pos_n3")
for (n,k) in FAMILY:
    cap = m.n3_upper_cap(n,k)[0]
    v = 1 + k*k//2
    ana = v*k*(k-2)//4
    L,U,_ = m.linear_bounds(n,k)
    P, good_r = m.integer_residue_classes(n,k)
    lo = max(Fraction(0), L)
    lo_int = (lo.numerator//lo.denominator) + (1 if lo.numerator%lo.denominator else 0)
    pos_n3 = None
    for r in sorted(good_r):
        x = lo_int + ((r - lo_int) % P)
        if x > U: continue
        if x > 0 and (pos_n3 is None or x < pos_n3): pos_n3 = x
    print(f"  ({n:>6},{k:>3})  match={cap==ana} cap={cap:<12}  P={P:<2}  good={good_r}  min_pos={pos_n3}")
