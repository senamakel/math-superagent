#!/usr/bin/env python3
"""Independent verification of the asymptotic slope c = root of tan(c*pi)=pi*(c+1),
and check K(n)/n -> c numerically at several n, plus double-check c != 3/7.
This is an independent route to the slope (different from pattern_k_* scripts):
solve the fixed point directly, then compare K(n)/n from the definition."""
import mpmath as mp
mp.mp.dps = 60

f = lambda c: mp.sin(c*mp.pi) - mp.pi*mp.cos(c*mp.pi)*(c+1)
c = mp.findroot(f, (0.2, 0.49))
print("c =", c)
print("3/7 =", mp.mpf(3)/7)
# c also satisfies sin(c pi) = pi cos(c pi)(c+1)
print("check sin(c*pi)=pi*cos(c*pi)(c+1):",
      mp.sin(c*mp.pi) - mp.pi*mp.cos(c*mp.pi)*(c+1))

def K_of_n(n):
    th = mp.pi/n
    t = mp.tan(th)
    best = 0
    for k in range(0, n+1):
        if mp.sin(k*th)-(k+n)*t*mp.cos(k*th) < 0:
            best = k
    return best

for n in [100,1000,10000,100000,1000000]:
    k = K_of_n(n)
    print(f"n={n}: K={k}, K/n={mp.mpf(k)/n}, c-K/n={c - mp.mpf(k)/n}")
