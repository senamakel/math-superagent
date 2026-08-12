#!/usr/bin/env python3
"""Lighter refined K(n) model test: K(n) = floor(c*n + k/n), k=1/(3(1+c)).
Find the FIRST failure over n in [3, 60000]."""
import mpmath as mp
mp.mp.dps = 50

def root_and_K(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-30')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return None, 0
    for _ in range(300):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    r = (lo+hi)/2
    return r, int(mp.floor(r))

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
k = 1/(3*(1+c))
print("c =", mp.nstr(c, 25))
print("k = 1/(3(1+c)) =", mp.nstr(k, 25))

fails = []
for n in range(3, 60001):
    r, K = root_and_K(n)
    model = int(mp.floor(c*n + k/n))
    if K != model:
        fails.append((n, K, model))
        if len(fails) >= 15:
            break
print("first failures of K(n)=floor(cn+k/n) in [3,60000]:")
for f in fails:
    print("   n=%d K=%d model=%d" % f)
