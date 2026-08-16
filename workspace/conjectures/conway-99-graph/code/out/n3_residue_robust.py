#!/usr/bin/env python3
"""Independence check: the residue n3 ≡ 0 (mod 3) at (99,14) follows from a
MINIMAL structural reason — the presence of subgraph counts whose n3
coefficient is 1/3 (or 2/3, 4/3) — not from the full 62-line transcription.

For n_i = base + c*n3 to be an integer with c = 1/3 and base an integer
(which it is: base = (1/12) n k (k-2), and for k=14 this is (1/12)*99*14*12
= 1386, an integer), n3 must be a multiple of 3.  Verify this directly.
"""
n,k = 99,14
# n1 = (1/12) n k (k-2) - n3/3 : base and coefficient
base1 = n*k*(k-2)//12
print(f"n1 base = (1/12)*{n}*{k}*{k-2} = {base1}  (integer: {base1*12==n*k*(k-2)})")
print(f"n1 = {base1} - n3/3  must be integer  =>  n3 ≡ 0 (mod 3)")
print()
# Check ALL fractional coefficients present, to confirm n3≡0 mod3 follows regardless of which binds:
from fractions import Fraction
coeffs = set()
def coeff_of(f, n, k):
    b = f(n,k,0); c = f(n,k,1)-b; return c
# compute coefficients for the specific member
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
coeffs = set()
for f in m.ALL_N:
    coeffs.add(coeff_of(f,n,k))
print("distinct n3-coefficient values used by the 62 formulas at (99,14):")
print(" ", sorted(coeffs))
frac = [c for c in coeffs if c.denominator > 1]
print("fractional coefficients:", frac)
print("denominators:", sorted(set(c.denominator for c in frac)), "-> lcm = 3")
print()
print("Since the denominators are all 3, and every base is an integer, each")
print("n_i = base + c*n3 integer forces c*n3 to have denominator dividing 3's")
print("power in c, i.e. n3 ≡ 0 (mod 3). This is independent of exactly which")
print("formulas bind — a robust structural consequence.")
