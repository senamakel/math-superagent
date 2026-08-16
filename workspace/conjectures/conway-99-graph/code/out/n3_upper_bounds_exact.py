#!/usr/bin/env python3
"""Compute the exact n3 upper caps (tightest nonneg upper bound on n3 from
the Reimbayev 62 order-6 count formulas) for the five feasible family members."""
from fractions import Fraction

# Re-create the 62 formulas' n3 coefficients + base values by importing the
# existing transcription module's functions via exec of its definitions is
# fragile; instead just import the exact caps by re-deriving the tightest
# negative-coefficient bound.  We replicate the function list minimally by
# importing from the sibling script.
import importlib.util, sys, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here, "n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

FAMILY = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]
print("family        n3_upper_cap (exact)   argmin_formula  L(frac)         U(frac)")
for (n,k) in FAMILY:
    cap, argmin = m.n3_upper_cap(n,k)
    L,U,fixed = m.linear_bounds(n,k)
    # exact fractions
    print(f"({n:>6},{k:>3})   {cap:>18}     n{argmin:<3}      L={str(L):<12} U={str(U)}")

print()
print("n3 upper-cap sequence over feasible members (k=4,14,22,112,994):")
seq = [m.n3_upper_cap(n,k)[0] for (n,k) in FAMILY]
print(seq)
print()
print("triangles T=nk/6 over the same members:")
print([n*k//6 for (n,k) in FAMILY])
print()
print("ratio cap/T over members:")
for (n,k),cap in zip(FAMILY,seq):
    print(f"  k={k:>4}: cap={cap:>12}  T={n*k//6:>12}  cap/T={Fraction(cap, n*k//6) if n*k//6 else '-'}")
