#!/usr/bin/env python3
"""Find ALL n in a range where K(n) != floor(c*n), c = root of tan(c*pi)=pi*(c+1)."""
import mpmath as mp
mp.mp.dps = 50

# c
lo, hi = mp.mpf("0.42"), mp.mpf("0.44")
def f(x): return mp.tan(x*mp.pi) - mp.pi*(x+1)
for _ in range(500):
    mid=(lo+hi)/2
    if f(mid)<0: lo=mid
    else: hi=mid
c=(lo+hi)/2

def K_of_n(n):
    th = mp.pi/n; t = mp.tan(th)
    L = []
    best = -1
    for k in range(0, n):   # k in [0,n-1], need k=n? K<=n but root in [1,n/2) so k<n
        if mp.sin(k*th) - (k+n)*t*mp.cos(k*th) < 0:
            best = k
    return best

# careful: real K can equal n? root in [1,n/2) so K < n/2, k in [0,n-1] enough
fails = []
for n in range(3, 20001):
    K = K_of_n(n)
    fl = int(mp.floor(c*n))
    if K != fl:
        fails.append((n, K, fl))
print("count fails in [3,20000]:", len(fails))
print("list:", fails)

# check whether fails are exactly {165, 3809} in this range and print margin c*n-K at fails
for n,K,fl in fails:
    print(f"n={n}: K={K} floor(cn)={fl} margin c*n-K={mp.nstr(c*n-K,8)}")
