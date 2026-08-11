#!/usr/bin/env python3
"""Compute A_j = M_j (Lehmer-coefficient sums) for n=9,10 using the efficient
orbit method (each distinct power counted n!/d times). Then extract f(1)=A_{n-2}
and the linear step.  Exact integers."""
import itertools, time
from math import factorial

def compute(n):
    perms=[tuple(p) for p in itertools.permutations(range(1,n+1))]
    def lehmer(p):
        c=[0]*(n-1)
        for j in range(n-1):
            v=p[j]
            cj=sum(1 for k in range(j+1,n) if p[k]<v)
            c[j]=cj
        return tuple(c)
    codes={p:lehmer(p) for p in perms}
    nf=factorial(n)
    A=[0]*n
    for pi in perms:
        # orbit of distinct powers pi^1..pi^d
        seen={}; cur=pi; pl=[cur]; seen[cur]=0
        while True:
            nxt=tuple(pi[v-1] for v in cur)
            if nxt in seen: break
            seen[nxt]=len(pl); pl.append(nxt); cur=nxt
        d=len(pl); mult=nf//d
        for pw in pl:
            cc=codes[pw]
            for j in range(n-1):
                A[j]+=mult*cc[j]
    return A

for n in (9,10):
    t0=time.perf_counter()
    A=compute(n)
    print(f"n={n}: A_j={A}  ({time.perf_counter()-t0:.2f}s)", flush=True)
