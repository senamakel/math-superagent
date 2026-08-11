#!/usr/bin/env python3
"""Symbolic search for closed forms of alpha_n, beta_n where
f_n(k) = n!(n-1)! * [alpha_n - beta_n*(k-1)], and Q(n)=n!^2 + sum_j (n-j)!*M_j
with f linear (verified for n=4..8).
alpha,beta are exact rationals; we search combinations of n, 1/n, 1/n!, 1/(n-1),
H_n, H_{n-1}, etc. with small rational coefficients."""
from fractions import Fraction as F
from math import factorial

def H(n):
    s=F(0)
    for i in range(1,n+1): s+=F(1,i)
    return s

# data
A = {4:184, 5:5052, 6:191232, 7:9851040, 8:650626560}
B = {4:0,   5:108,  6:3600,   7:208800,  8:12418560}
al = {}
be = {}
for n in (4,5,6,7,8):
    base=factorial(n)*factorial(n-1)
    al[n]=F(A[n],base)
    be[n]=F(B[n],base)

print("alpha:", {n:al[n] for n in al})
print("beta :", {n:be[n] for n in be})

# candidate expansions; try to express alpha_n as c0 + c1*H_{n-1} + c2/n + ...
# First look at alpha directly against H
for n in (4,5,6,7,8):
    print(f"n={n}  alpha={float(al[n]):.6f}  beta={float(be[n]):.6f}  "
          f"H(n-1)={float(H(n-1)):.6f}  Hn={float(H(n)):.6f}  "
          f"1/(n-1)={1/(n-1):.4f}  1/n={1/n:.4f}  H(n-1)-1={float(H(n-1)-1):.6f}")
