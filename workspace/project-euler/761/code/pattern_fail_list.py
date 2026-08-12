#!/usr/bin/env python3
"""Find ALL n in [3, N] where K(n) != floor(c*n), c = root of tan(c*pi)=pi*(c+1).
K via bisection (same as pattern_k_find_mismatch.py)."""
import mpmath as mp
mp.mp.dps = 40

def root_c():
    lo, hi = mp.mpf("0.42"), mp.mpf("0.44")
    def f(x): return mp.tan(x*mp.pi) - mp.pi*(x+1)
    for _ in range(400):
        mid = (lo+hi)/2
        if f(mid) < 0: lo = mid
        else: hi = mid
    return (lo+hi)/2

c = root_c()

def K_of_n(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return 0
    for _ in range(120):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return int(mp.floor((lo+hi)/2))

N = 20000
fails = []
for n in range(3, N+1):
    K = K_of_n(n)
    fl = int(mp.floor(c*n))
    if K != fl:
        fails.append((n, K, fl, mp.nstr(c*n - K, 8)))
print("count fails in [3,%d]:" % N, len(fails))
for row in fails:
    print(" n=%d: K=%d floor(cn)=%d margin(cn-K)=%s" % row)
