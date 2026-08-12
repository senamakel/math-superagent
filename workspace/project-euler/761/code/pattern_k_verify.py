#!/usr/bin/env python3
"""Verify K(n) vs floor(3n/7) deviation directly, and confirm structural findings."""
import mpmath as mp
mp.mp.dps = 30

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = None
    for k in range(0, n + 1):
        if mp.sin(k*th) - (k + n)*t*mp.cos(k*th) < 0:
            K = k
    return K

# find first n where K(n) != floor(3n/7)
first = None
for n in range(3, 200):
    K = K_of_n(n)
    fl = 3*n//7
    if K != fl:
        first = n
        break
print("first deviation n where K != floor(3n/7):", first)
print("  K(n), floor(3n/7) at that n:", K_of_n(first), 3*first//7)

# large-n slopes
for n in [500, 1000, 5000, 10000]:
    K = K_of_n(n)
    print(f"n={n}: K={K}, K/n={mp.nstr(mp.mpf(K)/n, 10)}")
