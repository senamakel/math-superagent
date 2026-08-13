#!/usr/bin/env python3
"""Thorough check: is there ANY prime-power modulus for which the achievable
residue set R of Phi = {4mn(m^2-n^2)/(m^2+n^2)^2} fails to be non-degenerately
additively closed?  If every R is additively closed at all precisions, no pure
p-adic modular proof of the no-triple conjecture exists (for the primes tried).
Also proves/confirms the valuation facts v2>=3, v3>=1 with full enumeration.
"""
from math import gcd
from fractions import Fraction

def f_frac(m,n):
    num=4*m*n*(m*m-n*n); den=(m*m+n*n)**2
    g=gcd(num,den)
    return Fraction(num//g, den//g)

def phi_set(M):
    return {f_frac(m,n) for m in range(2,M+1) for n in range(1,m)}

def residue_set(Phi, mod):
    """Achievable q mod mod (q = A/B, B invertible mod mod)."""
    R=set()
    skip=0
    for q in Phi:
        num,den=q.numerator,q.denominator
        if gcd(den, mod) != 1:
            skip+=1
            continue
        r=(num * pow(den % mod, -1, mod)) % mod
        R.add(r)
    return R, skip

def nondeg_closed(R, mod):
    """exists distinct r1,r2 in R with (r1+r2)%mod in R."""
    S=R
    L=list(R)
    for i in range(len(L)):
        for j in range(len(L)):
            if i==j: continue
            if (L[i]+L[j])%mod in S:
                return True
    return False

def main():
    M=200
    Phi=phi_set(M)
    print(f"Phi({M}): |Phi|={len(Phi)}")
    from collections import Counter
    for p in [2,3,5,7,11,13,17,19,23]:
        dist=Counter()
        for q in Phi:
            num,den=q.numerator,q.denominator
            v=0
            while num%p==0 and den%p!=0:  # crude; use vp properly via factor
                break
            # proper p-adic val: factor num and den
            def vp(x):
                c=0
                while x%p==0: x//=p; c+=1
                return c
            dist[vp(num)-vp(den)] += 1
        print(f"  p={p}: vp(q) range [{min(dist)}, {max(dist)}], "
              f"all vp>=0: {min(dist)>=0}; distribution heads: "
              f"{sorted(dist.items())[:3]}...")
    print()
    # additive closure at various moduli
    for p in [2,3,5,7,11,13]:
        row=[]
        for a in range(1,6):
            mod=p**a
            R,skip=residue_set(Phi,mod)
            if len(R)<=1:
                row.append(f"{mod}:|R|={len(R)}(triv)")
                continue
            cl=nondeg_closed(R,mod)
            row.append(f"{mod}:|R|={len(R)},closed={cl}" + (f",skip={skip}" if skip else ""))
        print(f"p={p}: "+" | ".join(row))

if __name__=="__main__":
    main()
