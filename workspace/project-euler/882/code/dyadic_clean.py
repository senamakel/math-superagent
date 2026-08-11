#!/usr/bin/env python3
"""Clean dyadic CGT value of the single-number bit-deletion game.

g(k): game {one_deletions | zero_deletions}. g(0)=0. If both option sets are
numbers and max(L) < min(R), then g(k) = simplest dyadic strictly between.
Board = disjoint sum => G(n) = sum_k k*g(k). With m Right-skips adding -m,
Zero (Right) wins iff G(n)-m <= 0, i.e. S(n) = ceil(G(n)).
"""
from fractions import Fraction

def one_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '1':
            t = s[:i] + s[i+1:]
            out.add(0 if t == '' else int(t, 2))
    return out

def zero_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '0':
            t = s[:i] + s[i+1:]
            out.add(0 if t == '' else int(t, 2))
    return out

def simplest_dyadic(lo, hi):
    """simplest dyadic strictly between lo and hi (inclusive->exclusive bound
    context). lo can be None (=-inf), hi None (=+inf). Scan birthday n."""
    for n in range(0, 40):
        den = 2**n
        if lo is None:
            m0 = -1
        else:
            m0 = (lo*den).numerator // (lo*den).denominator + 1
            while Fraction(m0, den) <= lo:
                m0 += 1
        if hi is None:
            m1 = 10**18
        else:
            m1 = (hi*den).numerator // (hi*den).denominator
            while Fraction(m1, den) >= hi:
                m1 -= 1
        if m1 < m0:
            continue
        return Fraction(m0, den)
    return None

def eval_g(maxk):
    g = {0: Fraction(0)}
    for k in range(1, maxk+1):
        L = [g[j] for j in one_deletions(k)]
        R = [g[j] for j in zero_deletions(k)]
        lo = max(L) if L else None
        hi = min(R) if R else None
        if lo is not None and hi is not None and not (lo < hi):
            g[k] = 'NOT-A-NUMBER'
            continue
        g[k] = simplest_dyadic(lo, hi)
    return g

g = eval_g(30)
for k in range(1, 31):
    v = g[k]
    print(f"g({k:2d}) = {str(v):>10s}   {float(v) if isinstance(v,Fraction) else ''}")

from math import ceil
print("\n n    G(n)           S=ceil(G)   real-oracle(if known)")
real = {1:1,2:2,3:8,4:9,5:17,10:64}
G = Fraction(0)
for n in range(1, 31):
    gv = g[n]
    if isinstance(gv, Fraction):
        G += n*gv
        print(f"{n:2d}  {float(G):12.5f}  {ceil(G):8d}   {real.get(n)}")
    else:
        print(f"{n:2d}  NOT-A-NUMBER at n={n}")
        break
