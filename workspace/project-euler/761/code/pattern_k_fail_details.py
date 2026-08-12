#!/usr/bin/env python3
"""Find ALL fails of K(n)=floor(cn) in a range, and report the fractional part
of c*n + the actual root at each fail (is the root within epsilon of an int?)."""
import mpmath as mp
mp.mp.dps = 50

def root_and_K(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return None, 0
    for _ in range(300):
        mid=(lo+hi)/2
        if f(mid) > 0: hi=mid
        else: lo=mid
    r=(lo+hi)/2
    return r, int(mp.floor(r))

def root_c():
    lo,hi=mp.mpf('0.40'),mp.mpf('0.46')
    def f(c): return mp.tan(c*mp.pi)-mp.pi*(c+1)
    for _ in range(400):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2
c=root_c()

fails=[]
for n in range(3, 20000):
    r,K = root_and_K(n)
    fl = int(mp.floor(c*n))
    if K != fl:
        fails.append((n, K, fl, r, (c*n - mp.floor(c*n))))
print("fails in 3..19999:", len(fails))
for n,K,fl,r,frac in fails[:20]:
    print(f"  n={n}: K={K} floor(cn)={fl}  root r={mp.nstr(r,20)}  c*n-frac={mp.nstr(frac,6)}")
