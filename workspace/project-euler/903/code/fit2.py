#!/usr/bin/env python3
"""Fit alpha_n, beta_n against candidate basis functions with small rational
coefficients, using exact data n=4..10.  alpha_n = A/n!(n-1)!, beta_n=B/n!(n-1)!."""
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

al={}; be={}
for n in (4,5,6,7,8,9,10):
    base=factorial(n)*factorial(n-1)
    f1=M[n][n-2]
    f2=M[n][n-3]-M[n][n-2]
    B=f1-f2
    A=f1
    al[n]=F(A,base); be[n]=F(B,base)
    print(f"n={n}: A={A} B={B}  alpha={al[n]}={float(al[n]):.8f}  beta={be[n]}={float(be[n]):.8f}")
print()

for n in al:
    print(f"n={n}: alpha={float(al[n]):.8f}  1/(n-1)!?; H(n-1)={float(H(n-1)):.8f}  "
          f"H(n)={float(H(n)):.8f}  H(n-1)-1={float(H(n-1)-1):.8f}")
