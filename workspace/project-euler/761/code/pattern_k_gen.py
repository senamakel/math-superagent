#!/usr/bin/env python3
"""Generate K(n) terms exactly (mpmath high precision) and print as a list.

K(n) = floor of the unique root r in [1, n/2) of tan(r*pi/n) = (r+n)*tan(pi/n)
     = largest integer k with sin(k*pi/n) - (k+n)*tan(pi/n)*cos(k*pi/n) < 0
"""
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

N = 200
Ks = [K_of_n(n) for n in range(3, N + 1)]
print("cnt", len(Ks))
print(", ".join(str(x) for x in Ks))
