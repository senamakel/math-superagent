#!/usr/bin/env python3
"""Check which n3 in [0, 4158] are genuinely admissible (all 62 formulas
nonneg integer) at (99,14), and confirm the smallest positive is 3.
Also confirm residue 0 mod 3 and cap exact for all five members."""
from fractions import Fraction
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

n,k = 99,14
cap = m.n3_upper_cap(n,k)[0]
admissible = [x for x in range(cap+1)
              if all(m.ALL_N[i](n,k,x).denominator==1 and m.ALL_N[i](n,k,x)>=0
                     for i in range(62))]
print(f"(99,14): cap={cap}, admissible n3 values (first 12): {admissible[:12]} ... total {len(admissible)}")
print("residues of admissible values:", sorted(set(x % 3 for x in admissible)))
print("smallest positive admissible:", next((x for x in admissible if x>0), None))

# Could there be an UNCONDITIONAL n3>=3 at 99 from order-6 integrality alone?
# No: n3=0 is admissible (it is in the list), so integrality does NOT force n3>=3.
print("\nn3=0 admissible at (99,14)?", 0 in admissible, " (so integrality alone does not force any n3)")

# closed form confirmation
print("\ncap closed form: v*k(k-2)/4 = k(k-2)(k^2+2)/8")
for (nn,kk) in [(9,4),(99,14),(243,22),(6273,112),(494019,994)]:
    vv = 1 + kk*kk//2
    ana = vv*kk*(kk-2)//4
    brute = m.n3_upper_cap(nn,kk)[0]
    print(f"  ({nn:>6},{kk:>3}): brute={brute} ana={ana} match={brute==ana}")
