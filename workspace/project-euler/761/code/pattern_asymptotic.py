#!/usr/bin/env python3
"""Verify asymptotic slope of K(n)/n. Root g(n) of tan(g*pi/n)=(g+n)tan(pi/n).
Let g=n/2-d. Asymptotically tan((pi/2)-d pi/n)=1/tan(d pi/n)~ n/(pi d).
RHS=(g+n)tan(pi/n) ~ (3n/2)(pi/n)=3pi/2. So n/(pi d)=3pi/2 -> d=2n/(3 pi^2).
Thus g/n -> 1/2 - 2/(3 pi^2) = 1/2 - 0.067547 = 0.432453.
Verify numerically by solving the root equation at large n."""
import math
import sympy as sp

def slope_pred(n):
    return 0.5 - 2.0/(3*math.pi*math.pi)

def root_numerical(n):
    th = math.pi/n
    t = math.tan(th)
    # solve tan(x*th) - (x+n)*t = 0 in [1,n/2) by bisection
    lo, hi = 1.0, n/2.0 - 1e-12
    def f(x):
        return math.tan(x*th) - (x+n)*t
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2

for n in [200, 500, 1000, 2000]:
    r = root_numerical(n)
    print(f"n={n}: root/n={r/n:.6f}  predicted slope={slope_pred(n):.6f}")
