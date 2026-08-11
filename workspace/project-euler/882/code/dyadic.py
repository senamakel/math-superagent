#!/usr/bin/env python3
"""Compute the dyadic CGT value g(k) of the single-number game for each k,
and the board value G(n)=sum_{k=1..n} k*g(k).  Under the CONTEXT structural
rule (Simplicity Rule for canonical Numbers), S(n) = ceil(G(n)).

g(k): One(Left) option: delete a 1-bit -> some j.  Zero(Right) option: delete
a 0-bit -> some j.  g(0)=0.  g(k) = simplest dyadic strictly between
max(Left values) and min(Right values).  "Simplest" = lowest birthday.
"""
from fractions import Fraction

def one_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i,ch in enumerate(s):
        if ch=='1':
            t = s[:i]+s[i+1:]
            out.add(0 if t=='' else int(t,2))
    return out

def zero_deletions(x):
    if x == 0: return []
    s = bin(x)[2:]
    out = set()
    for i,ch in enumerate(s):
        if ch=='0':
            t = s[:i]+s[i+1:]
            out.add(0 if t=='' else int(t,2))
    return out

# simplest dyadic strictly between lo and hi
# enumerate dyadics by birthday (denominator power of 2), check strictly inside
def simplest_dyadic(lo, hi):
    # lo, hi are Fractions or None (no left/right option)
    L = lo if lo is not None else None
    H = hi if hi is not None else None
    # find smallest birthday n such that some dyadic m/2^n with L < m/2^n < H
    # (with L = -inf, H = +inf handling)
    for n in range(0, 60):
        # all dyadics with denominator <= 2^n have birthday <= n (actually
        # birthday = n for 2^n denominator).  Simplest first: check n ascending.
        # m ranges over integers
        # we search m/2^n strictly between bounds
        # find integer m with m/2^n in (L,H); pick any (they all have birthday n
        # unless reducible, but that's fine, we prefer smallest n)
        # lower bound: m/2^n > L and m/2^n < H
        step = Fraction(1, 2**n)
        # m > L*2^n and m < H*2^n
        from math import floor, ceil
        if L is None:
            mlo = None
        else:
            mlo = L*2**n
        if H is None:
            mhi = None
        else:
            mhi = H*2**n
        # find integer m with mlo < m < mhi
        lo_int = -10**18 if mlo is None else ceil(float(mlo - step)) if False else None
        if mlo is not None:
            # m > mlo  => m >= floor(mlo)+1
            lo_m = int(mlo.numerator // mlo.denominator) + 1
            # careful with exact: m >= floor(mlo)+1 may allow m == mlo if mlo integer
            # adjust: need m/2^n > mlo strictly
            while Fraction(lo_m, 2**n) <= mlo:
                lo_m += 1
        else:
            lo_m = -1  # dummy
        if mhi is not None:
            hi_m = int(mhi.numerator // mhi.denominator)
            while Fraction(hi_m, 2**n) >= mhi:
                hi_m -= 1
        else:
            hi_m = 10**18
        m = max(lo_m if L is not None else -10**9, -10**9)
        # check if any integer strictly between
        start = lo_m if L is not None else -1
        for mm in range(start, min(hi_m, start+2)+2):
            v = Fraction(mm, 2**n)
            if (L is None or v>L) and (H is None or v<H):
                return v
        # also if L is None, cross check beyond start
        if L is None:
            for mm in range(-1, 2):
                v = Fraction(mm, 2**n)
                if (H is None or v<H):
                    return v

def eval_g(maxk):
    g = {0: Fraction(0)}
    for k in range(1, maxk+1):
        Lvals = [g[j] for j in one_deletions(k)]
        Rvals = [g[j] for j in zero_deletions(k)]
        lo = max(Lvals) if Lvals else None
        hi = min(Rvals) if Rvals else None
        g[k] = simplest_dyadic(lo, hi)
    return g

g = eval_g(20)
for k in range(1, 21):
    print(f"g({k}) = {g[k]}   (decimal {float(g[k])})")

# G(n) and S_theory = ceil(G(n))
from math import ceil
print("\n n    G(n)     S=ceil(G)  given")
for n in range(1, 11):
    G = sum(k*g[k] for k in range(1, n+1))
    given = {2:2, 5:17, 10:64}.get(n, None)
    print(f"{n:2d}  {float(G):9.4f}  {ceil(G):9d}   {given}")
