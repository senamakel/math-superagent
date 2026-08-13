#!/usr/bin/env python3
"""Verify the Schinzel-QNR structure of the realized residue sets and compute
the theoretical coverage ceiling for the sub-progression approach.

Key claims to establish exactly:
  A. Every realized family (M, s) is Schinzel-legal: b=840s+1 is a QNR mod 840M
     (equivalently QNR mod at least one prime-power factor of M) -- i.e. realized
     set never contains a QR-blocked residue.
  B. Per-prime gap: realized ⊂ QNR-allowed strictly; list the QNR-allowed-but-
     not-realized residues (the achievable targets).
  C. Ceiling: QR-blocked residues can NEVER be covered by a single polynomial
     family of any modulus (Schinzel Thm 1), so the union coverage has a hard
     ceiling 1 - prod_p[(p+1)/2p] given the set of used primes.
"""
import re
from collections import defaultdict
from math import gcd

def legendre(a, p):
    return pow(a % p, (p - 1) // 2, p)  # 1 QR, p-1 NQR, 0 divisible

txt = open('/workspace/code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
per = defaultdict(set)
for ln in lines:
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        M = a // 840
        c = (b - 1) // 840
        per[M].add(c)

# realized residues mod each odd prime factor
def odd_prime_factors(M):
    facs = []
    mm = M
    q = 2
    while q*q <= mm:
        if mm % q == 0:
            if q not in (2, 3):
                facs.append(q)
            while mm % q == 0:
                mm //= q
        q += 1
    if mm > 1 and mm not in (2, 3):
        facs.append(mm)
    return facs

prime_cover = defaultdict(set)
for M, S in per.items():
    for p in odd_prime_factors(M):
        prime_cover[p].update(c % p for c in S)

print("=== Claim A: realized residues are all Schinzel-legal (QNR-allowed) ===")
viol = False
for p in sorted(prime_cover):
    S = prime_cover[p]
    for s in S:
        # 840s+1 mod p: is it a QR mod p?
        val = (840 * s + 1) % p
        if val == 0:
            print(f"  p={p}: realized s={s} -> 840s+1 divisible by p (n composite, trivially solved)" )
            continue
        leg = legendre(val, p)
        if leg == 1:
            print(f"  VIOLATION p={p}: s={s} is QR-blocked but realized")
            viol = True
print(f"  any violation: {viol}")

print()
print("=== Claim B: per-prime realized vs QNR-allowed vs QR-blocked ===")
gaps = {}
for p in sorted(prime_cover):
    S = prime_cover[p]
    nqr_allowed = []   # 840s+1 QNR mod p (coprime)
    qr_blocked = []    # 840s+1 QR mod p
    nonunit = []
    for s in range(p):
        val = (840 * s + 1) % p
        if val == 0:
            nonunit.append(s)
        elif legendre(val, p) == 1:
            qr_blocked.append(s)
        else:
            nqr_allowed.append(s)
    gap = [s for s in nqr_allowed if s not in S]
    gaps[p] = gap
    assert all(s in nqr_allowed for s in S), f"realized not subset of allowed at p={p}"
    print(f"  p={p}: realized {len(S)}/{p} | QNR-allowed {len(nqr_allowed)} "
          f"(realized {len(S)}, GAP {gap}) | QR-blocked {len(qr_blocked)} "
          f"({qr_blocked}) | nonunit {nonunit}")

print()
print("=== Claim C: coverage ceiling given primes {11,13,17,19,23,29,31,37} ===")
# For a single modulus p (prime), a family can only cover t with 840t+1 a QNR mod p.
# QR-blocked residues (840t+1 QR mod p) are unreachable by ANY single-family modulus.
# Per branch (mod 2 x mod 3 fixed), coverage <= 1 - prod_p (fraction of t mod p that
# are QR-blocked or nonunit on the reachable part)... The right ceiling: t is coverable
# only if for every prime p it is QNR-allowed (using coupling moduli and the fact that
# a family eliminates that prime only when its own p-residue is QNR-allowed and matches).
primes = [11, 13, 17, 19, 23, 29, 31, 37]
# fraction of s mod p that are "usable" by any family whose modulus includes p:
usable = {}
for p in primes:
    c = 0
    for s in range(p):
        val = (840 * s + 1) % p
        if val != 0 and legendre(val, p) == p - 1:  # QNR
            c += 1
    usable[p] = c / p
    print(f"  p={p}: usable(legal) fraction = {c}/{p}")
# The floor on uncovered within a branch (factoring over primes as independent):
floor = 1.0
for p in primes:
    floor *= usable[p]
ceiling = 1 - (1 - floor)  # placeholder; correct logic below
# Max coverage within a branch = 1 - prod_p (1 - usable_p) IF we could reach every
# usable residue for every prime independently and combine freely.
maxcov = 1.0
for p in primes:
    maxcov *= (1 - usable[p])
maxcov = 1 - maxcov
print(f"  max achievable coverage within a branch (all usable residues per prime, "
      f"fully combined): {maxcov:.6f}")
print(f"  irreducible uncovered fraction within a branch: {1-maxcov:.6f}")
print(f"  = 1 - {maxcov:.6f}")
# sanity: compute it as product of (1-usable)
m = 1.0
for p in primes:
    m *= (1 - usable[p])
print(f"  check product(1-usable) = {m:.6f}")
