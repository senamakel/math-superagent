#!/usr/bin/env python3
"""Precise variance-decay exponent and self-similarity of nu2(n)/n.

Two checkable regularities that bear on the averaged-form theorem (GOAL pty 1):
  (A) tail variance sigma_N^2 = var(nu2(n)/n over [N/2,N)) as a power of N.
      If sigma_N^2 ~ C N^-a, the Chebyshev/strong-law route has rate N^(1-a/2).
      Compute successive-doubling exponents from the exact nu2 string.
  (B) self-similarity corr(nu2(2n)/2n, nu2(n)/n); test if prime-specific vs
      random (fold artifact).
"""
import sys, random
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def ratios(N, h):
    nu=[0]*(N+1)
    for n in range(2,N+1):
        _,ones=s_sos(n,h[:n]); nu[n]=ones
    return [nu[n]/n for n in range(2,N+1)]

def tail_var(rs, N):
    # rs indexed by n-2 ; window [N//2, N)
    lo=N//2-2; hi=N-2
    seg=rs[lo:hi]
    m=sum(seg)/len(seg)
    return sum((x-m)**2 for x in seg)/len(seg)

def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 8192
    ps=primes_upto_index(N+2)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+1)]
    rs=ratios(N,h)
    # (A) successive doubling tail variance
    print("tail variance over [N/2,N), successive doubling:")
    pts=[N//(1<<k) for k in range(1,6) if N//(1<<k)>=200]
    vals=[(n, tail_var(rs,n)) for n in sorted(set(pts))]
    for i,(n,v) in enumerate(vals):
        if i==0: continue
        n0,v0=vals[i-1]
        exp=- ( (v*0 and 0) )  # placeholder
        # v ~ C n^-a : a = -log(v/v0)/log(n/n0)
        a=-((v/v0).__float__()) if False else - ( (v).real and 0)
        # just compute directly
        import math
        if v>0 and v0>0:
            a=-math.log(v/v0)/math.log(n/n0)
            print(f"  n={n:5d}: sigma^2={v:.4e}  doubling exponent a={a:.3f}")
    # (B) self-similarity, primes
    pairs=[(rs[(2*n)-2], rs[n-2]) for n in range(2,N//2)]
    a=[p[0]-(sum(x[0] for x in pairs)/len(pairs)) for p in pairs]
    b=[p[1]-(sum(x[1] for x in pairs)/len(pairs)) for p in pairs]
    va=sum(x*x for x in a)/len(a); vb=sum(x*x for x in b)/len(b)
    cov=sum(x*y for x,y in zip(a,b))/len(a)
    print(f"\nprimes corr(nu2(2n)/2n, nu2(n)/n) = {cov/(va**0.5*vb**0.5+1e-12):.4f}  (n={len(pairs)})")
    # random h same N
    random.seed(11)
    hr=[random.randint(0,1) for _ in range(N+1)]
    rr=ratios(N,hr)
    pairs=[(rr[(2*n)-2], rr[n-2]) for n in range(2,N//2)]
    a=[p[0]-(sum(x[0] for x in pairs)/len(pairs)) for p in pairs]
    b=[p[1]-(sum(x[1] for x in pairs)/len(pairs)) for p in pairs]
    va=sum(x*x for x in a)/len(a); vb=sum(x*x for x in b)/len(b)
    cov=sum(x*y for x,y in zip(a,b))/len(a)
    print(f"random corr(nu2(2n)/2n, nu2(n)/n) = {cov/(va**0.5*vb**0.5+1e-12):.4f}")

if __name__=="__main__":
    main()
