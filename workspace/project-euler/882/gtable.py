#!/usr/bin/env python3
"""Compute g(k) (dyadic CGT value) up to large k efficiently, print S(n)=ceil(G(n)).
g(k) = simplest dyadic strictly between max(L) and min(R) where L,R are the
CGT values of the deletion options.
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
    for n in range(0, 40):
        den = 1 << n
        if lo is None:
            m0 = -1
        else:
            m0 = (lo*den).numerator // (lo*den).denominator + 1
            while Fraction(m0, den) <= lo:
                m0 += 1
        if hi is None:
            m1 = 1 << 40
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
        g[k] = simplest_dyadic(lo, hi)
    return g

import sys
maxk = int(sys.argv[1]) if len(sys.argv)>1 else 60
g = eval_g(maxk)
print("k\tg(k)")
for k in range(1, maxk+1):
    print(f"{k}\t{g[k]}")
