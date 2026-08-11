#!/usr/bin/env python3
"""Compute the exact dyadic CGT value of the n=6 board under the Simplicity Rule:
g(0)=0; g(k)=simplest dyadic strictly between max(Left=g(delete-a-1-bit)) and
min(Right=g(delete-a-0-bit)); board G(6)=sum_{k=1..6} k*g(k); S_theory=ceil(G(6)).
"""
import sys
sys.path.insert(0, "/workspace/code")
from fractions import Fraction
from math import floor, ceil
from toolkits.simplest_dyadic import simplest_between

def deletions(x, bit):
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == bit:
            t = s[:i] + s[i + 1:]
            out.add(0 if t == "" else int(t, 2))
    return sorted(out)

def one_deletions(x):
    return deletions(x, "1")

def zero_deletions(x):
    return deletions(x, "0")

g = {0: Fraction(0)}
for k in range(1, 7):
    L = [g[j] for j in one_deletions(k)]
    R = [g[j] for j in zero_deletions(k)]
    lo = max(L) if L else None
    hi = min(R) if R else None
    g[k] = simplest_between(lo, hi)
    print(f"g({k}) = {g[k]}   (decimal {float(g[k])})  L={[str(v) for v in L]} R={[str(v) for v in R]}")

G = sum(k * g[k] for k in range(1, 7))
print(f"\nG(6) = sum k*g(k) (k=1..6) = {G} = {float(G)}")
print(f"S_theory = ceil(G(6)) = {ceil(G)}")
