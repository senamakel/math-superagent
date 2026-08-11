#!/usr/bin/env python3
"""Study g(k) structure, computed directly without importing gtable's main."""
from fractions import Fraction

def one_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '1':
            out.add(0 if s[:i]+s[i+1:]=='' else int(s[:i]+s[i+1:],2))
    return out

def zero_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '0':
            out.add(0 if s[:i]+s[i+1:]=='' else int(s[:i]+s[i+1:],2))
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

def eval_g(maxk):
    g = {0: Fraction(0)}
    for k in range(1, maxk+1):
        L = [g[j] for j in one_deletions(k)]
        R = [g[j] for j in zero_deletions(k)]
        lo = max(L) if L else None
        hi = min(R) if R else None
        g[k] = simplest_dyadic(lo, hi)
    return g

g = eval_g(4096)

print("g(2k) vs g(k)/2  -- first divergences:")
cnt=0
for k in range(1,2048):
    if g[2*k] != g[k]/2:
        print(f"  k={k}: g(2k)={g[2*k]}  g(k)/2={g[k]/2}")
        cnt+=1
        if cnt>=8: break

print("\nSample g around powers of 2:")
for m in range(1,8):
    p=2**m
    print(f"  g({p})={g[p]}, g({p}+1)={g[p+1]}, g({p}-1)={g[p-1]}")
