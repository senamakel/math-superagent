#!/usr/bin/env python3
"""Verify Q(n)=sum_{d|n!} psi(d)*phi(n!/d) where psi(d)=F-value for i with gcd(i,n!)=d,
and print psi(d) for all divisors to look for structure."""
import itertools
from math import factorial, gcd
from fractions import Fraction

def phi(x):
    r=x; p=2
    while p*p<=x:
        if x%p==0:
            while x%p==0: x//=p
            r-=r//p
        p+=1
    if x>1: r-=r//x
    return r

def lex_ranks(n): return {p:r for r,p in enumerate(itertools.permutations(range(1,n+1)),1)}
def power(pi,i):
    n=len(pi); out=list(range(1,n+1))
    for _ in range(i): out=[pi[v-1] for v in out]
    return tuple(out)

def divisors(x):
    ds=[1]
    p=2
    while p*p<=x:
        if x%p==0:
            add=[]
            while x%p==0:
                x//=p
                ds=ds+[d*p for d in ds]
        p+=1
    if x>1:
        ds=ds+[d*x for d in ds]
    return sorted(set(ds))

n=5
rank=lex_ranks(n); nf=factorial(n)
perms=list(itertools.permutations(range(1,n+1)))
from collections import defaultdict
# compute psi(d) for each divisor d of n!
# F_i as function of gcd: pick representative i with gcd(i,n!)=d
psid={}
for d in divisors(nf):
    # find i in 1..nf with gcd(i,nf)=d
    cand=next(i for i in range(d,nf+1,d) if gcd(i,nf)==d)
    psid[d]=sum(rank[power(p,cand)] for p in perms)
# verify Q = sum psi(d)*phi(nf//d)
Q=sum(psid[d]*phi(nf//d) for d in psid)
print("Q(5)=",Q,"expected 597876",Q==597876)
print("psi(d) for divisors d of",nf,":")
for d in sorted(psid):
    print(f"  d={d:4d} psi={psid[d]:6d}  phi({nf//d})={phi(nf//d):4d}")
