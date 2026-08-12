#!/usr/bin/env python3
"""Derive/verify first-order asymptotics of the root r(n) of
tan(r*pi/n) = (r+n)*tan(pi/n).

From the tangent expansion: with x = cn + delta,
  tan(c*pi + delta*pi/n) = T + (delta*pi/n)(1+T^2) + ...,  T = tan(c*pi) = pi*(c+1),
  (cn+delta+n)*tan(pi/n) = T + pi^3(c+1)/(3n^2) + delta*pi/n + ...
=> delta * pi (1 + T^2) / n  =  pi^3 (c+1) / (3 n^2)
=> n * delta(n)  ->  k := pi^2 (c+1) / (3 (1 + pi^2 (c+1)^2))
   ~ 0.3178...  (to be confirmed numerically)

Check: r(n) - cn ~ k/n, i.e. n*(r(n)-cn) -> k, and the recorded boundary
roots (n=165: 71.00036; n=3809: 1639.00001) should satisfy
r(n) - cn = (root - int) + (cn - floor(cn)) ~ k/n.
"""
import mpmath as mp
mp.mp.dps = 60

def root_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    def f(x): return mp.tan(x*th) - (x+n)*t
    lo, hi = mp.mpf(1), mp.mpf(n)/2 - mp.mpf('1e-30')
    for _ in range(400):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
c1 = c + 1
k_pred = mp.pi**2 * c1 / (3 * (1 + mp.pi**2 * c1**2))
print("c =", mp.nstr(c, 20))
print("k_pred = pi^2(c+1)/(3(1+pi^2(c+1)^2)) =", mp.nstr(k_pred, 20))

print("\nn,  r(n)-cn,  n*(r(n)-cn),  k_pred")
for n in [100, 165, 1000, 3809, 10000, 50000, 200000]:
    r = root_n(n)
    d = r - c*n
    print("%7d  %12.8f  %12.8f" % (n, d, n*d))

# boundary cases: check the reported "root just above integer" values
for n in [165, 3809]:
    r = root_n(n)
    rint = mp.floor(r)
    frac = r - rint
    print("n=%d: r=%s, floor=%s, r-floor=%s, r-cn=%s" %
          (n, mp.nstr(r,12), int(rint), mp.nstr(frac,10), mp.nstr(r - c*n, 12)))