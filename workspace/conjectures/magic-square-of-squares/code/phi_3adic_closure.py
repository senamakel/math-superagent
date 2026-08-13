#!/usr/bin/env python3
"""Test whether the 3-adic residue set of Phi is additively closed.

Every q in Phi has v3(q) >= 1 (proved: numerator 4mn(m^2-n^2) always div by 3,
denominator (m^2+n^2)^2 coprime to 3 for primitive pairs).  For an additive
triple q1+q2=q3 all in Phi, we need the 3-adic units (odd part after stripping
v3) to combine: if v3(q1)=v3(q2)=v then q1+q2 = 3^v * (u1+u2 + 3*carry...),
and the unit part of q3 must equal u1+u2 mod 3.  Since all q have v3>=1, the
sum q1+q2 = q3 needs v3(q1+q2) = v3(q3) >= 1 which holds automatically.

So no 3-adic obstruction from the mere congruence 0 mod 3.  We push to 3^K:
is the set of residues r = q / 3^{v3(q)} * 3^{...} ... actually we test: the
set R_K of achievable q mod 3^K (as 3-adic integers) -- is it additively
closed (non-degenerately)?  If NOT closed, that IS a proof of no-triple.
"""
from math import gcd
from fractions import Fraction
import itertools

def f_frac(m,n):
    num = 4*m*n*(m*m-n*n)
    den = (m*m+n*n)**2
    g = gcd(num,den)
    return Fraction(num//g, den//g)

def phi_set(M):
    return {f_frac(m,n) for m in range(2,M+1) for n in range(1,m)}

def additively_closed_nondeg(R):
    S = set(R)
    for r1 in R:
        for r2 in R:
            if r1==r2: continue
            if (r1+r2) in S:
                return True
    return False

def main():
    M = 200
    Phi = phi_set(M)
    # residue of a rational A/B mod 3^K as 3-adic integer when B coprime to 3
    for K in [1,2,3,4]:
        mod = 3**K
        R = set()
        skipped = 0
        for q in Phi:
            num,den = q.numerator, q.denominator
            if den % 3 == 0:
                skipped += 1
                continue
            r = (num * pow(den % mod, -1, mod)) % mod
            R.add(r)
        closed = additively_closed_nondeg(R)
        print(f"3^{K}={mod}: |R|={len(R)}, nondeg-additively-closed: {closed}, "
              f"den=0 mod3 skipped: {skipped}")
        # also: are all residues 0 mod 3 (consistent with v3>=1)?
        all0 = all(r % 3 == 0 for r in R)
        print(f"   all residues ==0 mod 3: {all0}")

if __name__ == "__main__":
    main()
