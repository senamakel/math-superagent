#!/usr/bin/env python3
"""Compute f(k)=N(j,j+k) for n=2..9 and check affine/arithmetic structure.

f(k) = #{ (pi,i,m),\ m=j+k,  0<=i<n! : (pi^i)[m] < (pi^i)[j] }
       = sum_pi (nf/ord) * sum_{t in orbit} [pi^t(m) < pi^t(j)].
"""
import itertools
from math import factorial

def explore_f(n):
    nf = factorial(n)
    perms = [tuple(p) for p in itertools.permutations(range(n))]
    F = [0]*(n)          # F[k] = f(k), k=1..n-1
    for pi in perms:
        # orbit of distinct powers of pi (pi^0,pi^1,...)
        orbit = []
        seen = {}
        cur = tuple(range(n))
        while cur not in seen:
            seen[cur] = len(orbit)
            orbit.append(cur)
            cur = tuple(pi[v] for v in cur)
        d = len(orbit)
        mult = nf // d
        for tau in orbit:
            for j in range(n):
                for m in range(j+1, n):
                    if tau[m] < tau[j]:
                        F[m-j] += mult
    return F

def affine(F, n):
    """Fit f(k)=A - B*k for k=1..n-1; return (A,B) if exact affine."""
    if n-1 < 2:
        return None
    # f(k)=A-Bk -> consecutive diffs are -B
    diffs = [F[k]-F[k-1] for k in range(2, n)]
    B = -diffs[0]
    if any(d != -B for d in diffs):
        return None
    A = F[1] + B   # f(1) = A - B
    return A, B

for n in range(2, 10):
    F = explore_f(n)
    ab = affine(F, n)
    print(f"n={n}: f(k)={F[1:]}  affine(A-Bk)={ab}")
