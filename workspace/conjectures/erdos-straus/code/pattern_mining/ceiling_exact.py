#!/usr/bin/env python3
"""Exact ceiling of the sub-progression polynomial-family approach to
n=840K+1 (open class r=1), derived from Schinzel Thm 1.

A family n = a*k + b, a = 840*M, covering n == b mod a exists only if b is a
quadratic NON-residue mod a. Since b = 840t+1 with t = (b-1)/840:

  * b == 1 mod 840  => b is a QR mod every prime power dividing 840 (2^3,3,5,7).
  * For a prime p not dividing 840, 840t+1 mod p runs over all residues, and
    b is a QR mod p^e (e>=1) iff its mod-p value is a QR (Hensel).

So a family whose modulus M has odd-prime factors P = {p1,..,pk} (all not
dividing 840) can cover t only if 840t+1 is a QNR mod at least one pi, i.e.
when t is QR-blocked mod EVERY factor pi, the family is Schinzel-forbidden.

If the approach is restricted to a fixed prime set P, the density of t that are
QR-blocked (840t+1 a nonzero QR) mod every p in P is, by CRT independence,

    core(P) = product_{p in P} (p+1)/2p,     (each p contributes (p-1)/2p QR + 1/p zero)

so the coverage of n=840K+1 is capped at  1 - core(P)  in every (K mod 2,K mod 3)
branch.  The 0-contribution (840t+1 == 0 mod p, i.e. p | n) is NOT part of the
hard core: those n are composite with factor p and are solved by the factor
reduction.  We subtract only the nonzero-QR-blocked fraction (p-1)/2p.
"""
from math import prod

def core_for_primes(primes):
    # per prime: nonzero QR-blocked fraction = (p-1)/2p
    frac = 1.0
    log_detail = []
    for p in primes:
        f = (p - 1) / (2 * p)
        frac *= f
        log_detail.append((p, f))
    return frac, log_detail

set37 = [11, 13, 17, 19, 23, 29, 31, 37]
set43 = set37 + [41, 43]

for name, P in [("primes {11..37}", set37), ("primes {11..43}", set43)]:
    core, detail = core_for_primes(P)
    print(f"{name}:")
    print(f"   per-prime nonzero-QR-blocked fractions: {[(p, round(f,5)) for p,f in detail]}")
    print(f"   irreducible core density (per branch):  {core:.7f}  = {core*100:.4f}%")
    print(f"   coverage ceiling (per branch):          {1-core:.7f}  = {(1-core)*100:.4f}%")
    print()

# Cross page: current realized coverage 94.53% (603 fam, M up to 37) vs ceiling.
# residual up to ceiling = 99.4118 - 94.53 (for set37) approx
core37, _ = core_for_primes(set37)
core43, _ = core_for_primes(set43)
print(f"Reachable-but-not-yet-realized (94.53% -> {100*(1-core37):.2f}%): "
      f"{100*(1-core37)-94.53:.2f} percentage points (all QNR-allowed residues "
      f"not yet found by the parameter-bounded search)")
print(f"Structurally blocked with this prime set: {100*core37:.4f}% of the class.")
print(f"Adding primes 41,43 would reduce the core to {100*core43:.5f}% (only if "
      f"those residues are realized), raising the ceiling to {100*(1-core43):.5f}%.")
