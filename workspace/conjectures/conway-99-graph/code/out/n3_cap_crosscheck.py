#!/usr/bin/env python3
"""Independent cross-check of cap at (99,14) by a second route:
n3_upper_cap (min over negative-coefficient formulas of base/(-c)) vs
linear_bounds U (the interval upper bound from the same nonnegativity
constraints), plus the analytic closed form. Three independent routes."""
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

n,k = 99,14
route1 = m.n3_upper_cap(n,k)[0]     # min of base/(-c) over c<0
L,U,_ = m.linear_bounds(n,k)        # interval [L,U]
route2 = int(U)                     # upper endpoint of the interval
v = 1 + k*k//2
route3 = v*k*(k-2)//4               # closed form
print(f"(99,14): route1 (n3_upper_cap) = {route1}")
print(f"         route2 (linear_bounds U) = {route2}  (float {float(U):.6g})")
print(f"         route3 (v*k(k-2)/4)       = {route3}")
print(f"         ALL THREE AGREE: {route1==route2==route3}")
print()
# Verify n3=4158 is admissible (all 62 formulas nonneg integer) and 4159 not
ok38 = all(f(n,k,4158).denominator==1 and f(n,k,4158)>=0 for f in m.ALL_N)
ok39 = all(f(n,k,4159).denominator==1 and f(n,k,4159)>=0 for f in m.ALL_N)
print(f"n3=4158 admissible: {ok38};  n3=4159 admissible: {ok39}  (sharp bound)")
print()
# minimal positive admissible n3 = 3
small = next(x for x in range(1,10) if all(f(n,k,x).denominator==1 and f(n,k,x)>=0 for f in m.ALL_N))
print(f"smallest positive admissible n3 at (99,14): {small}")
print(f"=> with Makhnev n3>=1, forced n3 >= {small} and n3≡0 mod 3.")
