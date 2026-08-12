#!/usr/bin/env python3
"""Confirm the K(n)-floor(3n/7) deviation grows linearly in n (true slope c != 3/7)."""
import mpmath as mp
mp.mp.dps = 40

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return 0
    for _ in range(250):
        mid=(lo+hi)/2
        if f(mid) > 0: hi=mid
        else: lo=mid
    r=(lo+hi)/2
    return int(mp.floor(r))

# slope c from tan(c*pi)=pi(c+1)
def root_c():
    lo,hi=mp.mpf('0.40'),mp.mpf('0.46')
    def f(c): return mp.tan(c*mp.pi)-mp.pi*(c+1)
    for _ in range(300):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2
c=root_c()
print("true slope c =", mp.nstr(c,15), "  3/7 = 0.428571428571")
print("delta = c-3/7 =", mp.nstr(c-mp.mpf(3)/7, 8))

print("\nn:  K  floor(3n/7)  diff   predicted-diff((c-3/7)n)")
for n in [1000, 2000, 5000, 10000, 20000, 50000, 100000]:
    K=K_of_n(n); fl=n*3//7
    pred = (c - mp.mpf(3)/7)*n
    print(f"{n:7d}: {K:6d} {fl:6d}  {K-fl:3d}    {mp.nstr(pred,6)}")
