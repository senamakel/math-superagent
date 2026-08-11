#!/usr/bin/env python3
"""Exact search for alpha_n, beta_n as integer-coefficient combinations of a
functional basis.  alpha_n = f(1)/[n!(n-1)!], beta_n = (f(1)-f(2))/[n!(n-1)!].
Data n=4..10 are exact integers (verified linearity of f).  Try every
combination of up to `K` basis functions, solve the over-determined system by
checking small integer coefficient vectors via direct fit: for a chosen subset
of basis functions, solve exactly at the first |subset| data points and verify
on all points."""
from fractions import Fraction as F
from math import factorial
from itertools import combinations

def H(n):
    s=F(0)
    for i in range(1,n+1): s+=F(1,i)
    return s
def H2(n):
    s=F(0)
    for i in range(1,n+1): s+=F(1,i*i)
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

# basis functions
bf = {
 '1':          lambda n:F(1),
 'n':          lambda n:F(n),
 'n^2':        lambda n:F(n*n),
 '1/n':        lambda n:F(1,n),
 '1/(n-1)':    lambda n:F(1,n-1),
 '1/n^2':      lambda n:F(1,n*n),
 '1/(n-1)^2':  lambda n:F(1,(n-1)*(n-1)),
 'H(n-1)':     lambda n:H(n-1),
 'H(n)':       lambda n:H(n),
 'H(n)/n':     lambda n:H(n)/n,
 'H(n-1)/n':   lambda n:H(n-1)/n,
 'n*H(n-1)':   lambda n:n*H(n-1),
 'H2(n-1)':    lambda n:H2(n-1),
 '1/(n(n-1))': lambda n:F(1,n*(n-1)),
}

def fit(names, target):
    # solve target[n]=sum c_i b_i(n) for c_i (rational) at first m points
    # then check exactness on all points.
    m=len(names)
    funcs=[bf[x] for x in names]
    pts=ns[:m]
    # Gaussian elimination with fractions
    A=[[ funcs[i](n) for i in range(m)] for n in pts]
    y=[ target[n] for n in pts]
    # solve
    import copy
    A=[row[:]+[y[i]] for i,row in enumerate(A)]
    for col in range(m):
        # pivot
        piv=col
        while piv<m and A[piv][col]==0: piv+=1
        if piv==m: return None
        A[col],A[piv]=A[piv],A[col]
        pv=A[col][col]
        A[col]=[x/pv for x in A[col]]
        for r in range(m):
            if r!=col and A[r][col]!=0:
                f=A[r][col]; A[r]=[a-f*b for a,b in zip(A[r],A[col])]
    coeff=[A[i][-1] for i in range(m)]
    # check all points
    for n in ns:
        tot=sum(coeff[i]*funcs[i](n) for i in range(m))
        if tot!=target[n]:
            return None
    return {names[i]:coeff[i] for i in range(m)}

print("=== alpha_n ===")
pool=list(bf.keys())
for K in (1,2,3,4):
    for names in combinations(pool,K):
        r=fit(list(names), alpha)
        if r:
            print(f"  alpha fit (K={K}) {r}")
print("=== beta_n ===")
for K in (1,2,3,4):
    for names in combinations(pool,K):
        r=fit(list(names), beta)
        if r:
            print(f"  beta fit (K={K}) {r}")
