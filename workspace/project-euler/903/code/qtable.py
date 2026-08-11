#!/usr/bin/env python3
"""Compute Q(n) for n up to a feasible size via the period/orbit formula and
print normalization-related quantities to look for structure."""
import itertools, time
from math import factorial, gcd
from fractions import Fraction

def lex_ranks(n):
    return {p: r for r, p in enumerate(itertools.permutations(range(1, n+1)), 1)}

def order_of(pi):
    n=len(pi); seen=[False]*n; o=1
    for s in range(n):
        if not seen[s]:
            L=0; c=s
            while not seen[c]:
                seen[c]=True; c=pi[c]-1; L+=1
            o=o*L//gcd(o,L)
    return o

def distinct_powers(pi):
    out=[]; seen=set(); cur=pi
    while cur not in seen:
        seen.add(cur); out.append(cur)
        cur=tuple(pi[v-1] for v in cur)
    return out

def q(n):
    rank=lex_ranks(n); nf=factorial(n); total=0
    for pi in itertools.permutations(range(1,n+1)):
        d=order_of(pi)
        pw=distinct_powers(pi)
        total += (nf//d)*sum(rank[t] for t in pw)
    return total

for n in range(2,11):
    t0=time.perf_counter()
    qn=q(n)
    nf=factorial(n)
    print(f"n={n} Q={qn}")
    print(f"   Q/n! = {Fraction(qn,nf)}  ~ {qn/nf:.6f}")
    print(f"   Q/(n!)^2 = {Fraction(qn,nf*nf)}  ~ {qn/(nf**2):.6f}")
    print(f"   time {time.perf_counter()-t0:.2f}s")
