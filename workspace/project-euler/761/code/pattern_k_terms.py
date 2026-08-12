#!/usr/bin/env python3
"""Print K(n) terms for n=3..N as a comma list for the sequence tools,
and estimate K(n)/n slope at large n."""
import sympy as sp

def K_of_n(n):
    th = sp.pi / n
    t = sp.tan(th)
    # root-finding is expensive; reuse incrementally not needed here
    best = 0
    for k in range(0, n):
        if sp.sin(k*th) - (k+n)*t*sp.cos(k*th) < 0:
            best = k
    return best

N = 200
Ks = [K_of_n(n) for n in range(3, N+1)]
print("K(3..%d):" % N)
print(Ks)
# slope
print("K(200)/200 =", Ks[-1], "/", 200, "=", Ks[-1]/200.0)
print("3/7 =", 3/7.0)
# print some distant ratio
for n in [86,100,150,200]:
    print(n, K_of_n(n), K_of_n(n)/n)
