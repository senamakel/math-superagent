#!/usr/bin/env python3
"""Study F_i(n)=sum_pi rank(pi^i), how it depends on i (gcd with n!, divisors)."""
import itertools
from math import factorial, gcd

def lex_ranks(n):
    return {p:r for r,p in enumerate(itertools.permutations(range(1,n+1)),1)}

def power(pi,i):
    n=len(pi); out=list(range(1,n+1))
    for _ in range(i):
        out=[pi[v-1] for v in out]
    return tuple(out)

for n in [4,5]:
    rank=lex_ranks(n); nf=factorial(n)
    perms=list(itertools.permutations(range(1,n+1)))
    from collections import defaultdict
    byg=defaultdict(list)
    for i in range(1,nf+1):
        Fi=sum(rank[power(p,i)] for p in perms)
        byg[gcd(i,nf)].append((i,Fi))
    print(f"\n=== n={n} (n!={nf}): F_i grouped by gcd(i,{nf})")
    for g in sorted(byg):
        s=byg[g]
        vals=sorted(set(v for _,v in s))
        print(f"  gcd={g}: count={len(s)}, distinct F values={vals}")
    # also group by i's quotient
    # Q check
    Q=sum(v for s in byg.values() for _,v in s)
    print(f"  Q(n)={Q}")
