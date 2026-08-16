#!/usr/bin/env python3
"""Symbolically verify the closed form of the n3 upper cap.

cap(n,k) = tightest nonneg upper bound on n3 from the 62 Reimbayev order-6
formulas = min over formulas with negative n3-coefficient c of base/(-c).

For k>=6 the argmin is n1 = (1/12) n k (k-2) - n3/3, giving cap = n k (k-2)/4.
For k=4 the argmin is n5 = (1/8) n k (k-2)(k-4) - n3 whose base vanishes, cap=0.
"""
import sympy as sp

n, k = sp.symbols('n k', integer=True)
# v = 1 + k^2/2 ... actually v = 1 + k + k(k-2)/2 = 1 + k^2/2
v_expr = 1 + sp.Rational(1,2)*k**2

# n1 formula base = (1/12) n k (k-2), coefficient -1/3  =>  cap1 = base/(1/3)
cap1 = sp.Rational(1,12)*k*(k-2)*(v_expr)
cap1 = sp.simplify(cap1 / sp.Rational(1,3))
print("cap from n1 (k>=6):", sp.factor(cap1), " = n*k*(k-2)/4 with n=v:", sp.factor(cap1 - k*(k-2)*v_expr/4) == 0)

# Now express in u: k = u^2+u+2, v = 1+k^2/2
u = sp.symbols('u')
ku = u**2 + u + 2
vu = 1 + sp.simplify(ku**2)/2
capu = sp.expand(ku*(ku-2)*vu/4)
print("cap(u) polynomial:", sp.Poly(capu, u))
print("degree in u:", sp.degree(capu, u))

feas_u = [1,3,4,10,31]
feas = [(9,4),(99,14),(243,22),(6273,112),(494019,994)]
# verify cap = n*k*(k-2)/4 matches brute for k>=6 members
from fractions import Fraction

def cap_analytic(n,k):
    return (k*(k-2)*n)//4

print("\nverify cap = n k (k-2)/4 against brute (k>=6):")
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("n3f", os.path.join(here,"n3_order6_feasibility.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for (nn,kk) in [(99,14),(243,22),(6273,112),(494019,994)]:
    brute = m.n3_upper_cap(nn,kk)[0]
    ana = cap_analytic(nn,kk)
    print(f"  k={kk:>4}: brute={brute:>12} ana={ana:>12} match={brute==ana}")

print("\nsequence for tools: cap values at five feasible members:", [0,4158,26730,19320840,121781611728])
