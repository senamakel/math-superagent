#!/usr/bin/env python3
"""Per-permutation analysis: for each pi, compute ord(pi), the cyclic-subgroup
rank sum Sum_{tau in <pi>} rank(tau), and S(pi)=(n!/ord)*that. Look for whether
these depend on pi through simple statistics (cycle structure, etc.)"""
import itertools, time
from math import factorial, gcd
from collections import Counter

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

def cycle_type(pi):
    n=len(pi); seen=[False]*n; lens=[]
    for s in range(n):
        if not seen[s]:
            L=0; c=s
            while not seen[c]:
                seen[c]=True; c=pi[c]-1; L+=1
            lens.append(L)
    return tuple(sorted(lens))

n=5
rank=lex_ranks(n); nf=factorial(n)
# aggregate per cycle-type: total over pi of (rank-sum over subgroup), and count
agg=Counter()
count=Counter()
for pi in itertools.permutations(range(1,n+1)):
    ct=cycle_type(pi); d=order_of(pi)
    pw=distinct_powers(pi)
    rs=sum(rank[t] for t in pw)
    agg[ct]+=rs
    count[ct]+=1
for ct in sorted(agg):
    print(f"cycletype {ct}: #pi={count[ct]}, sum over pi of (subgroup ranksum) = {agg[ct]}, avg ranksum per pi = {agg[ct]/count[ct]:.3f}")
