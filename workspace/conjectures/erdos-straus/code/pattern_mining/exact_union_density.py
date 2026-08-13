#!/usr/bin/env python3
"""Exact union density of the finite sub-covering of n=840K+1 over the lcm
period, exploiting that coverage depends only on K mod 6 x (big primes).
For fixed (K mod 2, K mod 3), the coverage factors independently over the
big primes, giving (1/6)*sum of per-branch densities.
"""
import re
from math import gcd
from collections import defaultdict

txt = open('code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
per = defaultdict(set)
for ln in lines:
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        M = a // 840
        assert b % 840 == 1
        per[M].add((b - 1) // 840)

print("cov moduli:", sorted(per))
# Moduli that couple with 2 or 3: 22=2*11,26=2*13,33=3*11,34=2*17
def coord(c, m2):  # c mod M, m2 in {2,3}? return residue of the prime factor
    # each coupling modulus is q*p with q in {2,3}, p a prime; return c mod p
    for p in [11,13,17]:
        if M % p == 0:
            return c % p
    return None

# For each prime p and mod-2/3 residue, allowed residues from coupling moduli
S = {}
# pure-prime coverage sets per modulus
for M in sorted(per):
    S[M] = per[M]

primes = [11,13,17,19,23,29,31,37]

def fixpoint(a2, a3):
    """return dict p -> set of K mod p that are covered, given K mod 2 = a2, K mod 3 = a3"""
    cov = {p: set() for p in primes}
    # pure prime moduli
    for M in [11,13,17,19,23,29,31,37]:
        if M in S:
            cov[M] |= S[M]
    # coupling moduli
    for M in [22,26,33,34]:
        if M in S:
            q = 2 if M % 2 == 0 and M % 3 != 0 else (3 if M % 3 == 0 else None)
            # find prime factor p
            p = M // q if q else next(r for r in [11,13,17] if M % r == 0)
            # for fixed (a2,a3), the residue a2 mod 2 / a3 mod 3 that applies
            given = a2 if q == 2 else a3
            # c in S[M] => n=840K+1 with K≡c mod M.  K mod q = c mod q must equal given.
            for c in S[M]:
                if c % q == given:
                    cov[p].add(c % p)
    return cov

density = 0.0
details = []
for a2 in [0,1]:
    for a3 in [0,1,2]:
        cov = fixpoint(a2, a3)
        # within-branch density = 1 - prod_p (1 - |cov[p]|/p)
        frac = 1.0
        for p in primes:
            frac *= (1 - len(cov[p]) / p)
        branch = 1 - frac
        density += branch / 6.0
        details.append((a2, a3, branch, {p: len(cov[p]) for p in primes}))
print(f"\nEXACT union density of n=840K+1 covered = {density:.6f}")
for (a2,a3,branch,cov) in details:
    print(f"  K≡{a2} mod2, K≡{a3} mod3: branch coverage {branch:.5f}  cov={cov}")
