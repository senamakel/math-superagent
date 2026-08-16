#!/usr/bin/env python3
"""Mod-4 and switch-structure probes on nu2(n) exact terms (n up to N).
Reports:
 - nu2(n) restricted to n=1 mod 4, 3 mod 4 (the parity classes)
 - nu2(n) mod 2 pattern (is nu2(n) even/odd seemingly random?)
 - ratio nu2(n)/n trend over decades [10^a, 10^(a+1)]
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

def main():
    import sys
    N=int(sys.argv[1]) if len(sys.argv)>1 else 4000
    ps=primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    rows=[None]*N
    rows[0]=[h[b] for b in range(N)]
    for d in range(1,N):
        m=hpow(d); d1=d-m; r1=rows[d1]; L=N-1-d
        new=[0]*(L+1)
        for base in range(L+1):
            new[base]=r1[base]^r1[base+m]
        rows[d]=new
    nu=[sum(rows[d][n-1-d] for d in range(2,n)) for n in range(2,N+1)]
    print("nu2(n) for n=1 mod 4 (first 40):", [nu[n-2] for n in range(5,N+1,4)][:40])
    print("nu2(n) for n=3 mod 4 (first 40):", [nu[n-2] for n in range(3,N+1,4)][:40])
    print("nu2(n) parity for n=2..41 (1 if odd):", [nu[n-2]%2 for n in range(2,42)])
    # ratio by decade
    print("\nmean nu2/n by decade:")
    for a in range(2, len(str(N))):
        lo=10**a; hi=min(N,10**(a+1))
        if lo>=hi: break
        m=sum(nu[n-2]/n for n in range(lo,hi+1))/(hi-lo+1)
        print(f"  [{lo},{hi}]: {m:.4f}")

if __name__=="__main__":
    main()
