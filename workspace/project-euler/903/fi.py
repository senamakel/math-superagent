#!/usr/bin/env python3
"""Compute F_i(n)=sum_pi rank(pi^i) for n=4,5 and look for structure/periodicity.
Q(n)=sum_{i=1}^{n!} F_i(n)."""
import itertools
from math import factorial
from collections import Counter

def lex_ranks(n):
    return {p:r for r,p in enumerate(itertools.permutations(range(1,n+1)),1)}

def power(pi,i):
    res=tuple(range(1,len(pi)+1)); cur=pi
    # too slow generally; use repeated squaring won't work since map not a group hom... 
    # pi^i via functional composition
    n=len(pi)
    out=list(range(1,n+1))
    for _ in range(i):
        out=[pi[v-1] for v in out]
    return tuple(out)

for n in [4,5]:
    rank=lex_ranks(n)
    nf=factorial(n)
    freqs=Counter()
    for i in range(1,nf+1):
        F=sum(rank[power(p,i)] for p in itertools.permutations(range(1,n+1)))
        freqs[F]+=1
    # print distinct values of F_i and frequencies
    vals=sorted(freqs)
    print(f"\nn={n}: number distinct F_i values = {len(vals)}")
    for v in vals[:20]:
        print(f"   F={v} occurs {freqs[v]} times")
    base=nf*(nf+1)//2  # n!(n!+1)/2 = sum_pi rank = F for bijection assumption
    print(f"   sum_pi rank(pi) = {base} (constant would give F_i=this)")
    # check average
    avg=sum(F*c for F,c in freqs.items())/nf
    print(f"   mean F over i == base? {avg==base}")
