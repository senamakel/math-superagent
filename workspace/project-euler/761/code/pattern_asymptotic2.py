#!/usr/bin/env python3
"""Asymptotic slope c of K(n)/n solves: as n->inf, root g~cn with
tan(g*pi/n)=(g+n)tan(pi/n). LHS->tan(c pi), RHS->(cn+n)(pi/n)=pi(c+1).
So c is the root of tan(c pi) = pi*(c+1).
Solve exactly-ish (bisection) and compare with numerical g(n)/n at large n."""
import math

def root_c():
    # tan(c*pi)=pi*(c+1); c in (0.4,0.45)
    lo, hi = 0.40, 0.46
    def f(c):
        return math.tan(c*math.pi) - math.pi*(c+1)
    # f increasing near root? check
    for _ in range(300):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

c = root_c()
print("asymptotic c from tan(c*pi)=pi*(c+1):", c)

# compare with K(n)/n from exact root at large n
def root_numerical(n):
    th = math.pi/n
    t = math.tan(th)
    lo, hi = 1.0, n/2.0 - 1e-12
    def f(x): return math.tan(x*th) - (x+n)*t
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

for n in [2000, 5000, 10000]:
    r = root_numerical(n)
    print(f"n={n}: g/n={r/n:.7f}")
print("3/7 =", 3/7.0)
