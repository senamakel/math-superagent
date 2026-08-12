#!/usr/bin/env python3
"""Check the cleanest candidate closed form for K(n): K(n) = floor(c*n) vs
K(n) = round(c*n) with c solving tan(c*pi)=pi*(c+1), across small AND large n.
Also report K(n) - floor(c*n) residual to see if it's a bounded / floor behavior."""
import mpmath as mp
mp.mp.dps = 40

def K_of_n(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return 0
    for _ in range(250):
        mid=(lo+hi)/2
        if f(mid) > 0: hi=mid
        else: lo=mid
    return int(mp.floor((lo+hi)/2))

def root_c():
    lo,hi=mp.mpf('0.40'),mp.mpf('0.46')
    def f(c): return mp.tan(c*mp.pi)-mp.pi*(c+1)
    for _ in range(400):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

c = root_c()
print("c =", mp.nstr(c,25))

# residual: K(n) - floor(c*n)
mismatch_floor = 0
mismatch_round = 0
worst = 0
for n in range(3, 600):
    K = K_of_n(n)
    fl = int(mp.floor(c*n))
    rnd = int(mp.floor(c*n + mp.mpf('0.5')))  # nearest-ish
    if K != fl: mismatch_floor += 1
    if K != rnd: mismatch_round += 1
    worst = max(worst, abs(K - fl))
print(f"small n (3..599): K=floor(cn)? mismatches={mismatch_floor}, worst residual {worst}")
print(f"small n (3..599): K=round(cn)? mismatches={mismatch_round}")

# large-range residual sample
for n in [600, 1000, 2500, 5000, 10000, 25000, 50000, 100000]:
    K = K_of_n(n)
    cn = c*n
    fl = int(mp.floor(cn))
    print(f"n={n}: K={K}  floor(cn)={fl}  K-floor(cn)={K-fl}   c*n-cn_frac={mp.nstr(cn-mp.floor(cn),4)}")
