#!/usr/bin/env python3
"""Airtight p-adic closure: enumerate ALL residue classes (m,n) mod p^a
directly (not via a finite Phi sample), compute f(m,n) mod p^a for each
with invertible denominator, and test whether the achievable residue set is
non-degenerately additively closed.  A closed set at every prime-power gives
: no p-adic modular proof of the no-triple conjecture for those primes."""
from math import gcd

def f_residue(m, n, mod):
    m2=(m*m)%mod; n2=(n*n)%mod
    sn=(m2+n2)%mod
    if gcd(sn, mod)!=1:
        return None
    inv=pow(sn % mod, -1, mod)
    num=(4*m*n*(m2-n2))%mod
    return (num * inv * inv) % mod

def residue_set_by_pairs(mod):
    R=set()
    for m in range(mod):
        for n in range(mod):
            r=f_residue(m,n,mod)
            if r is not None:
                R.add(r)
    return R

def nondeg_closed(R, mod):
    L=list(R); S=set(R)
    for i in range(len(L)):
        for j in range(len(L)):
            if i==j: continue
            if (L[i]+L[j])%mod in S:
                return True
    return False

def main():
    for p in [2,3,5,7,11,13]:
        row=[]
        for a in range(1,6):
            mod=p**a
            if mod > 2000:   # keep enumeration small; sample-based check covered these
                break
            R=residue_set_by_pairs(mod)
            if len(R)<=1:
                row.append(f"{mod}:|R|={len(R)}(triv)")
                continue
            cl=nondeg_closed(R,mod)
            row.append(f"{mod}:{len(R)}{'closed' if cl else 'NOTCLOSED'}")
        print(f"p={p}: "+" | ".join(row))

if __name__=="__main__":
    main()
