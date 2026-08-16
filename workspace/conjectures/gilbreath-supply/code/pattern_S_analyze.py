#!/usr/bin/env python3
"""Extract and analyze the S(n) deviation sequence (the cleanest integer
object): S(n)=sum_{d=2}^{n-1} (-1)^{T(n,d)}, nu2=(n-2-S)/2.

Questions:
  - sign of S(n): does it drift, alternate, or concentrate near 0?
  - magnitude |S(n)| relative to n and sqrt(n)
  - residue of S mod small numbers, self-similarity
  - autocorrelation structure (already shown to be fold-generic; here just report)
  - bounding shape: is |S(n)| <= n^(1/2+eps) (which would give nu2 within
    n/2 +- small = strong) ?
"""
def main():
    Ss=[]; ns=[]
    for line in open('code/out/supply_endpoint_density.txt'):
        parts=line.split()
        if len(parts)<2: continue
        n=int(parts[0]); S=int(parts[1].replace('S=',''))
        Ss.append(S); ns.append(n)
    # n from 2..4014
    print(f"n range {ns[0]}..{ns[-1]}, {len(ns)} terms")
    # bound shape: max |S(n)|/n and /sqrt(n)
    import math
    print("max |S(n)|/sqrt(n):", max(abs(s)/math.sqrt(n) for s,n in zip(Ss,ns)))
    print("max |S(n)|/n:", max(abs(s)/n for s,n in zip(Ss,ns)))
    print("mean |S(n)|/sqrt(n):", sum(abs(s)/math.sqrt(n) for s,n in zip(Ss,ns))/len(Ss))
    print("last few S:", list(Ss[-5:]))
    # sign balance: fraction positive
    pos=sum(1 for s in Ss if s>0); neg=sum(1 for s in Ss if s<0)
    print(f"sign: pos={pos} neg={neg} zero={len(Ss)-pos-neg}")
    # S mod 4 distribution near the tail
    from collections import Counter
    tail=Ss[len(Ss)//2:]
    print("S mod 4 in tail:", Counter(s%4 for s in tail))
    # self-similarity of S: corr(S(2n), S(n))
    pairs=[(Ss[(2*n)-ns[0]], Ss[n-ns[0]]) for n in range(max(2,ns[0]),ns[-1]//2) if (2*n)<=ns[-1]]
    a=[p[0]-(sum(x[0] for x in pairs)/len(pairs)) for p in pairs]
    b=[p[1]-(sum(x[1] for x in pairs)/len(pairs)) for p in pairs]
    va=sum(x*x for x in a)/len(a); vb=sum(x*x for x in b)/len(b)
    cov=sum(x*y for x,y in zip(a,b))/len(a)
    print(f"corr(S(2n),S(n)) = {cov/(va**0.5*vb**0.5+1e-12):.4f} (n={len(pairs)})")
    print("S terms (n=2..60):", Ss[:59])

if __name__=="__main__":
    main()
