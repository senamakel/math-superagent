#!/usr/bin/env python3
"""Generate K(n) with EXACT sympy arithmetic (no float ambiguity) for n=3..N,
and K(n)-floor(3n/7). K(n) = largest integer < n with
    sin(K*theta) - (K+n)*tan(theta)*cos(K*theta) < 0,  theta=pi/n.
Also first-difference sequence and where K(n) deviates from floor(3n/7)."""
import sympy as sp

def K_of_n(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        val = (sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th))
        if val < 0:
            best = k
    return best

N = 200
Ks = [K_of_n(n) for n in range(3, N+1)]
print("K(3..%d):" % N)
print(Ks)

fl = [3*n//7 for n in range(3, N+1)]
dev = [(n, Ks[i], fl[i], Ks[i]-fl[i]) for i, n in enumerate(range(3, N+1)) if Ks[i] != fl[i]]
print("\nn where K(n)!=floor(3n/7)  (n, K, floor, diff):")
print(dev)

diffs = [Ks[i]-Ks[i-1] for i in range(1, len(Ks))]
print("\nfirst differences (n=4..%d):" % N)
print(diffs)
