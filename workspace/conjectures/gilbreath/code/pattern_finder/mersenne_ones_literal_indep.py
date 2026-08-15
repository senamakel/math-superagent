#!/usr/bin/env python3
"""Fully independent check of the ones-position law using ONLY the literal
from-scratch full-triangle builder (no lib.rightdiag).  This is the second
route for the ones-position law and the whole recursive closed form.

Checks: for P=2^k-1, k=3..8, the positions where c_r/2==1 are exactly the
descending binary partial sums {0, 2^{k-1}, 2^{k-1}+2^{k-2}, ..., 2^k-2}.
"""
def q_seq(word, n_terms):
    q=[2,3]; P=len(word)
    while len(q)<n_terms:
        bit=word[(len(q)-2)%P]; q.append(q[-1]+(2 if bit else 4))
    return q[:n_terms]

def right_diag(q):
    row=list(q); n=len(row)-1; diag=[row[n]]
    for k in range(1,n+1):
        nxt=[abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        row=nxt; diag.append(row[n-k])
    return diag

def nu2(diag):
    body=diag[:-1]; i=len(body)
    while i>2 and body[i-1] in (0,2): i-=1
    return body[i:].count(2)

def literal_nu2(word,n):
    return nu2(right_diag(q_seq(word,n+1)))

def order2(P):
    k=1;v=2%P
    while v!=1: v=(v*2)%P;k+=1
    return k

okall=True
for k in range(3,9):
    P=2**k-1; L=P
    nmin=P*3+5; nmax=nmin+P*3
    v={n:literal_nu2([0]*(P-1)+[1],n) for n in range(nmin,nmax+P+1)}
    seen={}
    for n in range(nmin,nmax-P+1):
        d=v[n+P]-v[n]; r=n%P
        if r in seen and seen[r]!=d: raise RuntimeError(f"not affine k={k}")
        seen[r]=d
    c2=[seen[r]//2 for r in range(P)]
    ones=[r for r in range(P) if c2[r]==1]
    # predicted: 0 plus partial sums after adding 2^{k-1}, 2^{k-2}, ..., 2^1
    s=0; pred=[0]
    for j in range(k-1,0,-1):
        s+=2**j; pred.append(s)
    match=(sorted(ones)==sorted(set(pred)))
    okall = okall and match
    print(f"k={k} P={P} ones={ones} pred={sorted(set(pred))} match={match}")
print("ALL MATCH (literal, no lib)" if okall else "MISMATCH")
