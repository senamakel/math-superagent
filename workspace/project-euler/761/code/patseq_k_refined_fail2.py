#!/usr/bin/env python3
"""Find first failure of refined K(n)=floor(c*n + k/n) model over a bigger range."""
import mpmath as mp
mp.mp.dps = 40

def root_and_K(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return None, 0
    for _ in range(230):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    r = (lo+hi)/2
    return r, int(mp.floor(r))

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
k = 1/(3*(1+c))

NMAX = 40000
fails = []
for n in range(3, NMAX+1):
    r, K = root_and_K(n)
    model = int(mp.floor(c*n + k/n))
    if K != model:
        fails.append((n, K, model))
        if len(fails) >= 10:
            break
print("first failures of refined model in [3,%d]: %s" % (NMAX, fails))
