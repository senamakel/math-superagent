#!/usr/bin/env python3
"""Residue-class / self-similar structure of nu2(n)/n.

Does nu2(n)/n depend on n mod 2^k (residue classes), or on n's 2-adic/ binary
shape? The Lucas/submask fold reads the binary structure of the depth d, so a
block/residue dependence would be the exploitable regularity. Probes, exactly
over n <= N:
  (a) mean of nu2(n)/n by residue class mod small powers of 2
  (b) mean by popcount/2-adic v2(n)
  (c) self-similarity: correlation between nu2(2n)/(2n) and nu2(n)/n
"""
import sys
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    ps = primes_upto_index(N + 2)
    h = [((ps[j+1]-ps[j])//2) % 2 for j in range(N+1)]
    nu = [0]*(N+1)
    for n in range(2, N+1):
        _, ones = s_sos(n, h[:n])
        nu[n] = ones
    # ratios are floats; store exact ratio as float for grouping
    r = [nu[n]/n for n in range(2, N+1)]
    def mean_of(inds):
        if not inds: return float('nan')
        return sum(r[i] for i in inds)/len(inds)
    # (a) residue class mod 2^k
    for k in [2,3,4]:
        mod = 1<<k
        print(f"residue mod {mod}: ", end="")
        print(" ".join(f"{c}:{mean_of([n-2 for n in range(mod+2,N+1) if n%mod==c]):.4f}" for c in range(mod)))
    # (b) v2(n)
    print("mean by v2(n):")
    for v in range(0,9):
        inds=[n-2 for n in range(2,N+1) if n%(1<<(v+1))==0 and n%(1<<(v+2))!=0] if v<8 else [n-2 for n in range(2,N+1) if n>=(1<<v)]
        print(f"  v2={v}: n={len(inds):5d}  mean={mean_of(inds):.5f}  n= {[inds[0]+2 if inds else None]}")
    # (c) self-similarity
    pairs=[(r[(2*n)-2], r[n-2]) for n in range(2, N//2)]
    a=[p[0]- (sum(x[0] for x in pairs)/len(pairs)) for p in pairs]
    b=[p[1]- (sum(x[1] for x in pairs)/len(pairs)) for p in pairs]
    va=sum(x*x for x in a)/len(a); vb=sum(x*x for x in b)/len(b)
    cov=sum(x*y for x,y in zip(a,b))/len(a)
    print(f"\ncorr(nu2(2n)/2n, nu2(n)/n) = {cov/(va**0.5*vb**0.5+1e-12):.4f}")

if __name__ == "__main__":
    main()
