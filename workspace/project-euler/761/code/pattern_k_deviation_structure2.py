#!/usr/bin/env python3
"""Examine d(n) = K(n) - floor(3n/7) over an exact sympy range.
Question: is there a clean exact structure to where d(n) is nonzero
and its growth, beyond 'asymptotically linear with slope c-3/7'?"""
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
prev = None
first_nonzero = None
rows = []
max_d = 0
for n in range(3, N+1):
    K = K_of_n(n)
    d = K - 3*n//7
    if d != 0 and first_nonzero is None:
        first_nonzero = n
    max_d = max(max_d, d)
    if d != 0:
        rows.append((n, K, 3*n//7, d))

print("first n with nonzero deviation:", first_nonzero)
print("max d up to n=%d: %d" % (N, max_d))
print("sample nonzero deviations (n, K, floor(3n/7), d):")
print(rows[:40])
# residues mod 7 of deviating n
import collections
res = collections.Counter(n % 7 for n,_,_,_ in rows)
print("residue distribution of deviating n mod 7 (count of first deviations if small):", dict(res))
