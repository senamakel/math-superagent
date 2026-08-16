#!/usr/bin/env python3
"""Sharpen: is n3 forced to be a positive multiple of 3 at (99,14)?
- n3 admissible set from Reimbayev 62 = multiples of 3 in [0, cap], cap=4158.
- Makhnev re-derived: any putative (99,14,1,2) has n3 >= 1 (n3=0 ruled out).
- Hence n3 in {3,6,9,...} is forced, i.e. n3 >= 3 AND n3 in {0,3,6,...},
  so the minimum possible n3 for a putative 99-graph is 3.
Report the exact admissible set at (99,14) and the forced lower bound.
"""
from fractions import Fraction
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

n,k = 99,14
cap = m.n3_upper_cap(n,k)[0]
adm = [x for x in range(cap+1)
       if all(f(n,k,x).denominator==1 and f(n,k,x)>=0 for f in m.ALL_N)]
res = sorted(set(x%3 for x in adm))
print(f"(99,14): admissible n3 = multiples of 3 in [0,{cap}], count={len(adm)}")
print(f"  residues mod 3 present: {res}")
print(f"  n3=0 admissible (arithmetically): {0 in adm}  -> integrality alone forces NO n3")
print(f"  n3=3 admissible (arithmetically): {3 in adm}")

# Under Makhnev re-derived (n3>=1 for a putative 99 graph), remove 0:
pos = [x for x in adm if x>=1]
print(f"\nWITH Makhnev n3>=1: admissible n3 = {pos[:6]} ... -> minimum = {min(pos)}")
print(f"FORCED CONSEQUENCE: if srg(99,14,1,2) exists, n3 in {{3,6,9,...}} i.e. n3>=3 and n3≡0 mod 3")
