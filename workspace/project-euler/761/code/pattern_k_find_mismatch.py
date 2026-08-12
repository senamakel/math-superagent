#!/usr/bin/env python3
"""Locate the single n in 3..599 where K(n) != floor(c*n), and extend the search
widely to count how often floor(c*n) fails across a huge range."""
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
c=root_c()

# find the one mismatch in 3..599
mism=[]
for n in range(3,600):
    if K_of_n(n) != int(mp.floor(c*n)):
        mism.append(n)
print("3..599 mismatches:", mism)

# scan a large sparse+ dense range counting failures
fails=0
first_fail=None
for n in range(3, 5000):
    if K_of_n(n) != int(mp.floor(c*n)):
        if first_fail is None: first_fail=n
        fails+=1
print(f"3..4999: fails={fails}, first_fail={first_fail}")

# sparse big samples
for n in [10000,20000,50000,100000,200000,500000,1000000]:
    K=K_of_n(n); fl=int(mp.floor(c*n))
    print(f"n={n}: K={K} floor(cn)={fl} equal={K==fl}")
