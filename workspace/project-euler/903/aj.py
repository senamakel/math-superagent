#!/usr/bin/env python3
"""Decompose Q(n)=sum_j (n-j)! A_j + (n!)^2, where
A_j = sum_{i=1}^{n!} sum_pi c_j(pi^i), and c_j(pi)=#{k>j: pi_k<pi_j} (Lehmer code).
rank(pi)=1+sum_j c_j(pi)*(n-j)!.
Verify Q and extract A_j values for pattern."""
import itertools
from math import factorial
from collections import Counter

def lex_ranks_and_c(n):
    # returns dict pi->(rank, tuple c_1..c_{n-1})
    res={}
    for p in itertools.permutations(range(1,n+1)):
        c=[]
        for j in range(1,n):   # j is index 1..n-1 in 1-based
            v=p[j-1]
            cj=sum(1 for k in range(j,n) if p[k]<v)
            c.append(cj)
        rank=1+sum(c[t]*factorial(n-(t+1)) for t in range(len(c)))
        res[p]=(rank,tuple(c))
    return res

def power(pi,i):
    n=len(pi); out=list(range(1,n+1))
    for _ in range(i):
        out=[pi[v-1] for v in out]
    return tuple(out)

for n in [2,3,4,5]:
    nf=factorial(n)
    info=lex_ranks_and_c(n)
    A=[0]*(n)   # A[0] unused, A[1..n-1]
    Q=0
    for pi in itertools.permutations(range(1,n+1)):
        r0,c0=info[pi]
        for i in range(1,nf+1):
            pw=power(pi,i)
            r,cc=info[pw]
            Q+=r
            for t in range(1,n):
                A[t]+=cc[t-1]
    # reconstruct
    rec=nf*nf + sum(factorial(n-j)*A[j] for j in range(1,n))
    print(f"n={n}: Q={Q}  reconstruct={rec}  match={Q==rec}")
    print(f"   A_j (j=1..{n-1}) = {[A[j] for j in range(1,n)]}")
    # Q(2)=5 check
