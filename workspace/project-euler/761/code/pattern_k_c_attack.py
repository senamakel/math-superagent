#!/usr/bin/env python3
"""Attack the conjecture K(n) = floor(c*n), c root of tan(c*pi)=pi*(c+1), c=0.43029665312..
Find the FIRST n where it fails."""
import mpmath as mp
mp.mp.dps = 40

# asymptotic c
lo, hi = mp.mpf("0.42"), mp.mpf("0.44")
def f(x): return mp.tan(x*mp.pi) - mp.pi*(x+1)
for _ in range(500):
    mid = (lo+hi)/2
    if f(mid) < 0: lo = mid
    else: hi = mid
c = (lo+hi)/2
print("c =", mp.nstr(c, 18))

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = None
    for k in range(0, n + 1):
        if mp.sin(k*th) - (k + n)*t*mp.cos(k*th) < 0:
            K = k
    return K

fails = []
for n in range(3, 3000):
    K = K_of_n(n)
    if K != int(mp.floor(c*n)):
        fails.append((n, K, int(mp.floor(c*n))))
        if len(fails) <= 6:
            print(f"FAIL n={n}: K={K}, floor(c*n)={int(mp.floor(c*n))}, c*n-margin={mp.nstr(c*n - K, 6)}")
print("total fails in n in [3,2999]:", len(fails))
print("first five:", fails[:5])
