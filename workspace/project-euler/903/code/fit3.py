#!/usr/bin/env python3
"""Systematic exact search: can alpha_n, beta_n be an integer combination of
basis functions?  alpha_n = A/(n!(n-1)!), beta_n=B/(n!(n-1)!).  We test
alpha_n approx and see residuals against candidate bases."""
from fractions import Fraction as F
from math import factorial

def H(n):
    s=F(0)
    for i in range(1,n+1): s+=F(1,i)
    return s

M = {
 4:[552,368,184,0],
 5:[19560,14832,9996,5052,0],
 6:[920160,743328,562896,378864,191232,0],
 7:[55974240,47167200,38151360,28926720,19493280,9851040,0],
 8:[4293596160,3717480960,3128947200,2527994880,1914624000,1288834560,650626560,0],
 9:[406306575360,358782359040,310325541120,260936121600,210614100480,159359477760,107172253440,54052427520,0],
 10:[46556342784000,41724639129600,36807629644800,31805314329600,26717693184000,21544766208000,16286533401600,10942994764800,5514150297600,0],
}
ns=[4,5,6,7,8,9,10]
base=lambda n: factorial(n)*factorial(n-1)
alpha={}; beta={}
for n in ns:
    f1=M[n][n-2]; f2=M[n][n-3]-M[n][n-2]; B=f1-f2; A=f1
    alpha[n]=F(A,base(n)); beta[n]=F(B,base(n))

# candidate basis functions (as sympy-free, callable n->Fraction)
def b_1(n): return F(1)
def b_Hh(n): return H(n-1)
def b_H(n): return H(n)
def b_n(n): return F(n)
def b_1n(n): return F(1,n)
def b_1nm(n): return F(1,n-1)
def b_2n(n): return F(n,n-1)      # 1+1/(n-1)
basis={
 'H(n-1)':b_Hh, 'H(n)':b_H, 'n':b_n, '1':b_1,
 '1/n':b_1n, '1/(n-1)':b_1nm, 'n/(n-1)':b_2n,
}

print("residuals: alpha_n - [lincomb], for single bases scaled to match n=10:")
for name,fn in basis.items():
    # solve c s.t. c*b(n) best matches alpha; check exactness coefficient c
    # c = alpha[10]/b(10)
    c = alpha[10]/fn(10)
    res=[alpha[n]-c*fn(n) for n in ns]
    print(f"  c*{name}(c={float(c):.6f}): residuals {[float(r) for r in res]}")

# try alpha_n = c1*H(n-1)+c2  (two param) solved at n=4,10
def show(name, expr):
    print(f"\n{name}: {[float(expr(n)) for n in ns]}")
print("\nalpha:", [float(alpha[n]) for n in ns])
print("H(n-1):",[float(H(n-1)) for n in ns])
print("H(n):",[float(H(n)) for n in ns])
