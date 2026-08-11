#!/usr/bin/env python3
"""Explore Q = sum_tau rank(tau)*N(tau), N(tau)=#{(pi,i): pi^i=tau, i in 1..nf}.
Check whether N(tau) depends only on cycle type of tau."""
import itertools
from math import factorial
from collections import defaultdict

def power(pi,i):
    n=len(pi); out=list(range(1,n+1))
    for _ in range(i): out=[pi[v-1] for v in out]
    return tuple(out)

def cycle_type(pi):
    n=len(pi); seen=[False]*n; lens=[]
    for s in range(n):
        if not seen[s]:
            L=0; c=s
            while not seen[c]:
                seen[c]=True; c=pi[c]-1; L+=1
            lens.append(L)
    return tuple(sorted(lens))

def lex_ranks(n): return {p:r for r,p in enumerate(itertools.permutations(range(1,n+1)),1)}

for n in [3,4]:
    nf=factorial(n)
    perms=list(itertools.permutations(range(1,n+1)))
    rank=lex_ranks(n)
    # N(tau) = sum_i #{pi: pi^i=tau}
    # compute by iterating (pi,i)
    N=defaultdict(int)
    for pi in perms:
        pw=pi
        for i in range(1,nf+1):
            N[pw]+=1
            pw=tuple(pi[v-1] for v in pw)
    # check dependence on cycle type
    bytype=defaultdict(set)
    for tau in perms:
        bytype[cycle_type(tau)].add(N[tau])
    print(f"n={n}: does N(tau) depend only on cycle type?")
    for ct in sorted(bytype):
        vals=bytype[ct]
        print(f"  cycletype {ct}: N values {sorted(vals)}", "CONSTANT" if len(vals)==1 else "<-not constant")
    Q=sum(rank[t]*N[t] for t in perms)
    print(f"  Q(n)={Q}  (check against known: n=3 ->88, n=4->4808)")
