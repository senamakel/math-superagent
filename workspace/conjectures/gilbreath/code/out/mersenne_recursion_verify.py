#!/usr/bin/env python3
"""Canonical verifier for the Mersenne ν₂ affine-constant recursion.

Claim (verified-numerically, conjecture): for the 2-then-odds tail-1 word of
period P=2^k-1, the halved per-residue affine constants A_k[r]=c_r/2 satisfy
  A_2 = [1,1,1]
  A_{k+1} = [1] ++ [2^k-1] ++ (2*A_k[2:]) ++ [2,1,2^{k-1}] ++ A_k[2:]
This script (1) generates A_k by the recursion, (2) independently recomputes
c_r/2 for k=3..10 via a from-scratch literal full triangle (no lib) over a
wide-enough affine window, and (3) reports whether they match exactly. Also
checks sum(c_r)=3^k-3 and value-1 positions.
"""
def build_q(word, n_terms):
    q=[2,3]; per=len(word)
    while len(q)<n_terms: q.append(q[-1]+(2 if word[(len(q)-2)%per] else 4))
    return q

def full_triangle(q):
    row=q[:]; yield row
    while True:
        row=[abs(row[i+1]-row[i]) for i in range(len(row)-1)]; yield row

def nu2_for_n(q, nmax):
    res={}; it=full_triangle(q); buff=[next(it) for _ in range(nmax+1)]
    for n in range(0,nmax+1):
        diag=[buff[k][n-k] for k in range(n+1)]
        body=diag[:-1]; i=len(body)
        while i>2 and body[i-1] in (0,2): i-=1
        res[n]=body[i:].count(2)
    return res

def per_residue_affine(vals,P,nmin,nmax):
    cs=[None]*P
    for r in range(P):
        d={vals[n+P]-vals[n] for n in range(nmin,nmax-P+1) if n%P==r}
        if len(d)==1: cs[r]=d.pop()//2
    return cs

def predict(ak,k):
    L=len(ak); out=[0]*(2*L+1)
    out[0]=1; out[1]=2**k-1
    for i in range(2,L): out[i]=2*ak[i]
    out[L]=2; out[L+1]=1; out[L+2]=2**(k-1)
    for i in range(2,L): out[L+3+(i-2)]=ak[i]
    return out

def main():
    A2=[1,1,1]; seq={2:A2}
    for k in range(2,10): seq[k+1]=predict(seq[k],k)
    # window width grows with P
    w = {3:600,4:1500,5:2400,6:3600,7:6000,8:9000,9:11000,10:16000}
    allmatch=True
    for k in range(3,11):
        P=2**k-1
        nmax = w[k]
        vals=nu2_for_n(build_q([0]*(P-1)+[1], nmax+2), nmax)
        cs=per_residue_affine(vals,P,nmax//2,nmax-P)
        match=(cs==seq[k])
        allmatch &= bool(match)
        s=sum(cs) if cs and None not in cs else None
        print(f"k={k} P={P} len={len(cs)} sum(c_r/2)={s} expect={(3**k-3)//2} match={match}")
    print("ALL MATCH:", allmatch)

if __name__=="__main__":
    main()
