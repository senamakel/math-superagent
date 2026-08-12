#!/usr/bin/env python3
"""Exact check: does K(n) = floor(n*sqrt(3)/4) (Beatty A308358) or floor(3n/7)?
K(n) = largest integer k with sin(k*th) - (k+n)*tan(th)*cos(k*th) < 0, th=pi/n.
Reproduce K(n) exactly with sympy and compare against both candidate closed forms."""
import sympy as sp

def K_of_n(n):
    th = sp.pi / n
    t = sp.tan(th)
    best = 0
    for k in range(0, n):
        val = sp.sin(k*th) - (k+n)*t*sp.cos(k*th)
        if val < 0:
            best = k
    return best

sqrt3o4 = sp.sqrt(3)/4
N = 200
Ks = [K_of_n(n) for n in range(3, N+1)]

# candidate 1: floor(3n/7)
dev_floor37 = [(n, Ks[i], 3*n//7) for i, n in enumerate(range(3, N+1)) if Ks[i] != 3*n//7]
# candidate 2: floor(n*sqrt(3)/4)
dev_beatty = [(n, Ks[i], sp.floor(n*sqrt3o4)) for i, n in enumerate(range(3, N+1)) if Ks[i] != sp.floor(n*sqrt3o4)]

print("n where K(n) != floor(3n/7):  first 12 =", dev_floor37[:12])
print("  count =", len(dev_floor37))
print("n where K(n) != floor(n*sqrt3/4): first 12 =", dev_beatty[:12])
print("  count =", len(dev_beatty))
