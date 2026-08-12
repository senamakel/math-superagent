#!/usr/bin/env python3
"""Compute the d(n) = K(n) - floor(3n/7) deviation structure exactly (sympy)
for n in [3, 600], and report:
  - first n with d=1 (deviation onset), the gaps between deviating n,
  - check the far gap structure; print for OEIS analysis the deviating-n set.
"""
import sympy as sp

def K_of_n(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            best = k
    return best

N = 600
dev = []
for n in range(3, N+1):
    d = K_of_n(n) - 3*n//7
    if d != 0:
        dev.append(n)
print("deviating n in [3,%d]: count=%d" % (N, len(dev)))
print("first 30:", dev[:30])
gaps = [dev[i+1]-dev[i] for i in range(len(dev)-1)]
print("gaps:", gaps[:60])
print("gap multiset:", sorted(set(gaps)))
# residue distribution of deviating n
from collections import Counter
print("n mod 7 of deviating n:", dict(sorted(Counter(n % 7 for n in dev).items())))
# first deviation per residue
first = {}
for n in dev:
    r = n % 7
    if r not in first:
        first[r] = n
print("first deviating n per residue mod7:", dict(sorted(first.items())))