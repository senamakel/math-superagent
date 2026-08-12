#!/usr/bin/env python3
"""Verify the refined K(n) model's k-value derivation:
r(n) = c*n + k/n + O(1/n^2), k = 1/(3(1+c)).
Check n*(r(n) - c*n) -> k numerically at large n."""
import mpmath as mp
mp.mp.dps = 60

def root_r(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-40')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return None
    for _ in range(400):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
k = 1/(3*(1+c))
print("c  =", mp.nstr(c, 20))
print("k  = 1/(3(1+c)) =", mp.nstr(k, 20))

print("n*(r - c*n) should approach k:")
for n in [1000, 10000, 100000, 10**6, 10**7]:
    r = root_r(n)
    val = n*(r - c*n)
    print("  n=%8d:  n(r-cn) = %.12f   (k=%.12f, diff=%.2e)" % (n, float(val), float(k), abs(float(val-k))))