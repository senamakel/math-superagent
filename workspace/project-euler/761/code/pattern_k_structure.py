#!/usr/bin/env python3
"""Fast, exact-enough investigation of K(n) structure at LARGE n.

K(n) = floor of the unique root r in [1, n/2) of  tan(r*pi/n) = (r+n)*tan(pi/n).
Use mpmath high precision (fast) rather than sympy symbolic trig (slow).

Goal: describe K(n) - floor(3n/7) deviation and confirm asymptotic slope c.
"""
import mpmath as mp
mp.mp.dps = 40

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    lo, hi = mp.mpf(1), mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x):
        return mp.tan(x*th) - (x+n)*t
    # f increasing; f(1) may be pos or neg; bracket root properly
    # find sign change; f decreasing at small x? handle by scanning
    if f(lo) > 0:
        return 0  # no root in range
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    r = (lo+hi)/2
    return int(mp.floor(r))

# check small n against known exact values
print("K(3..30) should be 1,1,2,2,3,3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,9,10,10,11,11,12,12,12,13,13")
print([K_of_n(n) for n in range(3,31)])

# deviation at large n
for n in [86, 100, 165, 200, 500, 1000, 5000, 10000]:
    K = K_of_n(n)
    fl = n*3//7
    print(f"n={n}: K={K}  floor(3n/7)={fl}  K/n={K/n:.7f}  diff={K-fl}")

# slope vs prediction c (tan(c pi)=pi(c+1))
def root_c():
    lo, hi = mp.mpf('0.40'), mp.mpf('0.46')
    def f(c): return mp.tan(c*mp.pi) - mp.pi*(c+1)
    for _ in range(300):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2
c = root_c()
print("\npredicted asymptotic c = tan(c*pi)=pi(c+1) root:", mp.nstr(c, 12))
print("3/7 =", mp.nstr(mp.mpf(3)/7, 12))
