#!/usr/bin/env python3
"""Verify the self-similar structure of Mersenne per-residue constants c_r/2.

Conjectured law (from inspect): for P = 2^k - 1, positions r where c_r/2 = 1
are exactly the partial sums of descending powers: r = 2^{k-1} - 2^{k-1-j}
... check: k=4 P=15 ones at [0,8,12,14] = [2^3-2^3, 2^3-2^2, 2^3-2^1, 2^3-2^0]
i.e. 2^{k-1} - 2^j for j=0..k-1? 8-8=0,8-4=4? no that's 4 not present.
Let me just verify positions == 2^{k-1} and then 2^{k-1}+(2^{k-2}...) 
Actually observed ones: k=4 [0,8,12,14]; k=5 [0,16,24,28,30].
These are: 0, 2^{k-1}, 2^{k-1}+2^{k-2}, 2^{k-1}+2^{k-2}+2^{k-3}, ..., full sum-2^0.
i.e. r = sum_{j=i}^{k-1} 2^j for i=0..k-1 (descending partial sums including 0). 

We compute directly for k=2..10 and test this position law exactly.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2

def build_seq(word, n_terms):
    q=[2,3]; per=len(word)
    while len(q)<n_terms:
        bit=word[(len(q)-2)%per]; q.append(q[-1]+(2 if bit else 4))
    return q[:n_terms]

def nu2_seq(word,nmax):
    q=build_seq(word,nmax+1); out={}
    for k,dd in enumerate(incremental_diagonals(q)):
        if k>=2: out[k]=cycle_and_nu2(dd)[1]
    return out

def order2(P):
    k=1;v=2%P
    while v!=1: v=(v*2)%P;k+=1
    return k

for k in range(2,11):
    P=2**k-1; L=P
    nmax=min(L*4+300,20000); nmin=L+100
    vals=nu2_seq([0]*(P-1)+[1],nmax)
    seen={};ok=True
    for n in range(nmin,nmax-L+1):
        d=vals[n+L]-vals[n];r=n%L
        if r in seen and seen[r]!=d:ok=False;break
        seen[r]=d
    if not ok:
        print(f"k={k} P={P} NOT affine");continue
    c2=[seen[r]//2 for r in range(P)]
    ones=[r for r in range(P) if c2[r]==1]
    # predicted ones: descending partial sums
    pred=[0]
    s=0
    for j in range(k-1,-1,-1):
        s+=2**j
        if s>0: pred.append(s)
    pred=pred[:-1]  # remove the full P-? ; actually sum all = 2^k-1=P => cap
    # observed ones include 0 and P-1? k=4 P=15 ones [0,8,12,14]; 14=P-1. pred=[0,8,12,14] yes
    match=(ones==sorted(set(pred)))
    # sum c_r vs 3^k-3
    S=sum(seen.values());m=min(seen.values())
    print(f"k={k:2d} P={P:5d} affine={ok} ones_positions_ok={match} "
          f"ones={ones}  sum_c_r={S} target={3**k-3} ok={S==3**k-3} min_c={m}")
