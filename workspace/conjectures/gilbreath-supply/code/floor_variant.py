#!/usr/bin/env python3
"""Test whether the dip at n=53 (nu2/n=0.3585) persists under the alternative
'floor at index 2' convention vs the all-submask fold form. 
The fold convention counts d in [2,n-1]. 'floor at index 2' may mean d in
[3,n-1] or [2,n-2] etc. We test each variant's min ratio and whether a
counterexample to >=0.42 survives in [50,4000].
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
    # T(n,d) = rows[d][n-1-d]
    # variants: count d in ranges R
    R_variants = {
        "d in [2,n-1] (canonical fold)": (2, lambda n: n-1),
        "d in [3,n-1]": (3, lambda n: n-1),
        "d in [2,n-2]": (2, lambda n: n-2),
    }
    for name,(dlo,dhi_f) in R_variants.items():
        nu=[0]*(N+1)
        for n in range(2,N+1):
            dhi=dhi_f(n)
            if dhi<dlo: continue
            nu[n]=sum(rows[d][n-1-d] for d in range(dlo,min(dhi,n)+1))
        m=min(nu[n]/n for n in range(50,N+1) if n>=dlo+1)
        mn=min([n for n in range(50,N+1) if n>=dlo+1], key=lambda n: nu[n]/n)
        below=[n for n in range(50,N+1) if n>=dlo+1 and nu[n]/n<0.42]
        print(f"{name}: min={m:.4f} at n={mn}, points<0.42 in [50,{N}]: count={len(below)}, first={below[:12]}")

if __name__=="__main__":
    main()
