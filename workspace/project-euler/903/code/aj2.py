#!/usr/bin/env python3
"""Compute A_j(n)=sum_{i=1}^{n!} sum_pi c_j(pi^i) for the Lehmer coefficients,
for n up to 8. Q = n!*n! + sum_j (n-j)!*A_j."""
import itertools
from math import factorial
import time

def compute(n):
    nf=factorial(n)
    perms=[tuple(p) for p in itertools.permutations(range(1,n+1))]
    # rank table using Lehmer from scratch each time (build once)
    def lehmer(p):
        c=[0]*(n-1)
        for j in range(n-1):
            v=p[j]
            cj=sum(1 for k in range(j+1,n) if p[k]<v)
            c[j]=cj
        return tuple(c)
    codes={p:lehmer(p) for p in perms}
    A=[0]*n  # A[j] for j in 0..n-2 used
    # for each pi
    for pi in perms:
        # precompute powers? iterate i
        cur=pi
        # i from 1..nf, cur=pi^i
        # but need also each power's code
        # iterate powers of pi with multiplicity
        # pi^i: i=1..nf; pi^nf=id
        # walk the orbit
        seen={}
        power_rank={}
        pow_list=[]
        p0=pi
        k=0
        cur=pi
        seen[cur]=0
        pow_list=[cur]
        while True:
            nxt=tuple(pi[v-1] for v in cur)
            if nxt in seen: break
            seen[nxt]=len(pow_list)
            pow_list.append(nxt)
            cur=nxt
        d=len(pow_list)  # order
        nf_=nf
        mult=nf//d
        # each power appears mult times among i=1..nf
        for pw in pow_list:
            cc=codes[pw]
            for j in range(n-1):
                A[j]+=mult*cc[j]
    Q=nf*nf+sum(factorial(n-j)*A[j] for j in range(n-1))
    return A,Q

for n in range(2,9):
    t0=time.perf_counter()
    A,Q=compute(n)
    print(f"n={n}: Q={Q}  A_j={[A[j] for j in range(n-1)]}  ({time.perf_counter()-t0:.2f}s)")
