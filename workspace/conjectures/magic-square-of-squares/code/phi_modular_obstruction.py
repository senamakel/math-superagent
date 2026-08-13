#!/usr/bin/env python3
"""Look for a modular obstruction to an additive triple in Phi.

A triple q1,q2,q1+q2 all in Phi.  If, modulo some p^a, the set of achievable
residues R = { f(m,n) mod p^a : primitive m>n>=1 } has the property that no
two residues r1,r2 in R satisfy r1+r2 ≡ r3 (mod p^a) with r3 in R, then no
triple can exist (a genuine proof of the conjecture *assuming every q in Phi
is captured by these residues, which it is since residues depend only on
(m,n) mod p^a and primitive pairs cover all residue reps).

We check this for small primes p and precision a.  f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2
computed mod p^a; denominators invertible when p | (m^2+n^2) -> those (m,n)
don't give a residue (skip; they'd be the problematic q=k/p... but primitivity
means p can't divide both, and (m^2+n^2) could still be 0 mod p; such (m,n)
give no finite residue -> exclude from the representative set).
"""
import sys

def reduce_mod(m, n, mod):
    """f(m,n) mod mod, if invertible; else None."""
    m2 = m*m % mod; n2 = n*n % mod
    sn = (m2 + n2) % mod   # denominator
    if sn == 0:
        return None
    try:
        inv = pow(sn, -1, mod)
    except ValueError:
        return None
    num = (4*m*n*(m2 - n2)) % mod
    return (num * inv * inv) % mod

def residue_set(mod):
    """Achievable residues r in Z/mod for primitive m>n>=1 (we take m mod mod,
    n mod mod, primitive pairs, m>n>0)."""
    R = set()
    for m in range(1, mod):
        for n in range(1, m+1) if False else range(1, mod):
            # primitive + m>n; but we need residue reps with m>n not required
            # in Z/p^a an ordering isn't meaningful; take both orders
            if n == 0 or m == 0: 
                continue
            if n % mod == m % mod and n % mod == 0:
                continue
            # allow any nonzero residue pair; m>n irrelevant over residue ring
            # (f is symmetric up to sign? f(m,n) not symmetric; keep both)
            r = reduce_mod(m % mod, n % mod, mod)
            if r is not None:
                R.add(r)
    return R

def additively_closed(R, mod):
    """Does there exist r1,r2 in R with (r1+r2)%mod in R?  (triple)"""
    S = set(R)
    for r1 in R:
        for r2 in R:
            if (r1 + r2) % mod in S:
                return True
    return False

def main():
    for p in [3,5,7,11,13,17,19,23,29,31]:
        mod = p
        R = residue_set(mod)
        closed = additively_closed(R, mod)
        # also report how big R is, and whether there's a SINGLE residue r in R
        # with 2r in R (q1=q2 degenerate) - exclude that as trivial?  triples with
        # q1=q2 allowed? The MSS needs q1>q2 distinct; but a modular obstruction
        # should exclude even the non-degenerate.  Check non-degenerate: exists
        # r1!=r2 with r1+r2 in R.
        nondeg = False
        for r1 in R:
            for r2 in R:
                if r1==r2: continue
                if (r1+r2)%mod in R:
                    nondeg=True; break
            if nondeg: break
        print(f"p={p}: |R|={len(R)}/mod={mod}, has-triple(deg+nondeg)="
              f"{closed}, has-triple(non-degenerate)={nondeg}")

if __name__ == "__main__":
    main()
