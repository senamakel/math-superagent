#!/usr/bin/env python3
"""Examine the structure of the nu2/n dips: are they prime-gap large? 
And test the averaged form: mean of nu2/n over [50,N], variance, and whether
the dips coincide with large prime gaps (switch density deficit).
"""
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok=True; r=isqrt(cand)
        for p in ps:
            if p>r: break
            if cand%p==0: ok=False; break
        if ok: ps.append(cand)
        cand+=2
    return ps

def hpow(d):
    m=1
    while (m<<1)<=d: m<<=1
    return m

def nu2_fast(N,h):
    rows=[None]*N
    rows[0]=[h[b] for b in range(N)]
    for d in range(1,N):
        m=hpow(d); d1=d-m; r1=rows[d1]; L=N-1-d
        new=[0]*(L+1)
        for base in range(L+1):
            new[base]=r1[base]^r1[base+m]
        rows[d]=new
    out=[]
    for n in range(2,N+1):
        cnt=0
        for d in range(2,n):
            cnt+=rows[d][n-1-d]
        out.append(cnt)
    return out

def main():
    import sys
    N=int(sys.argv[1]) if len(sys.argv)>1 else 4000
    ps=primes_upto_index(N+3)
    gaps=[ps[j+1]-ps[j] for j in range(N+2)]
    h=[(g//2)%2 for g in gaps]
    fast=nu2_fast(N,h)
    # gaps near each dip
    dips=[n for n in range(50,N+1) if fast[n-2]/n<0.42]
    print("dips:", dips)
    # prime gap around q_n: gaps[n-1] = q_n - q_{n-1} (q_1=2). q_n index n.
    # also nearby gaps
    med_gap = sorted(gaps)[len(gaps)//2]
    print("median prime gap over first %d: %d"%(len(gaps), med_gap))
    for n in dips:
        g=q=None
        gl = gaps[n-2] if n-2>=0 else 0
        g2 = gaps[n-1] if n-1<len(gaps) else 0
        g3 = gaps[n] if n<len(gaps) else 0
        print(f"  n={n}: nu2/n={fast[n-2]/n:.4f} gaps q_n-q_{'{n-1}'}={gaps[n-1] if n-1<len(gaps) else 0}, q_{'{n+1}'}-q_n={gaps[n] if n<len(gaps) else 0}")

    # averaged form: moving window means
    print("\nMean nu2/n over [50,N]=%.4f"% (sum(fast[n-2]/n for n in range(50,N+1))/(N-49)))
    # long-window average around each dip to see if locally depressed
    for n in dips:
        lo=max(50,n-20); hi=min(N,n+20)
        m=sum(fast[k-2]/k for k in range(lo,hi+1))/(hi-lo+1)
        print(f"  local mean around n={n} over [{lo},{hi}] = {m:.4f}")

if __name__=="__main__":
    main()
