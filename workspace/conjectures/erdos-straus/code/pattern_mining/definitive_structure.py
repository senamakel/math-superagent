#!/usr/bin/env python3
"""Definitive structural check of the full 1451-family sub-progression set:

1. Parse all three capture files, collect every (a,b) pair.
2. For every family verify the Schinzel legality: b=840s+1 must be a QNR mod
   a=840M (i.e., QNR mod at least one prime factor p of M not dividing 840),
   else the family is IMPOSSIBLE as a single polynomial identity.
3. Collapse to the residue sets per modulus, list per-prime realized residues
   against the Schinzel-allowed set, and print the gap.
4. Confirm the ceiling: products over prime groups of allowed-residue fractions.
"""
import re
from collections import defaultdict
from math import gcd

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return pow(a, (p - 1) // 2, p)

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

def qnr_mod_some_prime(b, M):
    """True if b is QNR mod some odd prime factor p of M (p not dividing 840),
    i.e. Schinzel-legal for modulus a=840*M (b coprime to 840M)."""
    for p in odd_prime_factors(M):
        val = b % p
        if val != 0 and legendre(val, p) == p - 1:
            return True
    return False

fam = []
seen = set()
for path in ['code/out/subprogression.captured.txt',
             'code/out/extended_subprogression.full.txt',
             'code/out/extended_subprogression.captured.txt']:
    try:
        txt = open(path).read()
    except FileNotFoundError:
        print(f"missing {path}")
        continue
    for ln in txt.splitlines():
        m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if (a, b) not in seen:
                seen.add((a, b))
                fam.append((a, b))

print(f"parsed {len(fam)} distinct (a,b) families")

# 1) Schinzel legality of every family
illegal = []
for (a, b) in fam:
    M = a // 840
    assert a % 840 == 0 and b % 840 == 1
    if not qnr_mod_some_prime(b, M):
        illegal.append((a, b))
print(f"[1] Schinzel-legal (b QNR mod some prime ∤840): {len(fam)-len(illegal)}/{len(fam)}")
print(f"    illegal families: {illegal[:10]}")

# 2) residue sets per modulus
per = defaultdict(set)
for (a, b) in fam:
    M = a // 840
    per[M].add(b // 840 - 0)  # b=840t+1 -> t=(b-1)//840
# fix: t = (b-1)//840
per = defaultdict(set)
for (a, b) in fam:
    M = a // 840
    t = (b - 1) // 840
    per[M].add(t)

print(f"\n[2] distinct residue classes (M, t): {sum(len(s) for s in per.values())} over {len(per)} moduli")
for M in sorted(per):
    S = sorted(per[M])
    print(f"    M={M:4}: {len(S):2}/{M:2} residues: {S}")

# 3) per-prime realized vs QNR-allowed
print("\n[3] per-odd-prime realized / Schinzel-allowed / gap:")
prime_cover = defaultdict(set)
for M, S in per.items():
    for p in odd_prime_factors(M):
        prime_cover[p].update(t % p for t in S)

gaps_all = {}
for p in sorted(prime_cover):
    S = prime_cover[p]
    allowed = []
    blocked = []
    for s in range(p):
        val = (840 * s + 1) % p
        if val == 0:
            continue
        if legendre(val, p) == p - 1:
            allowed.append(s)
        else:
            blocked.append(s)
    gap = sorted(s for s in allowed if s not in S)
    gaps_all[p] = (sorted(S), allowed, blocked)
    print(f"    p={p:3}: realized {len(S):2}  QNR-allowed {len(allowed):2} "
          f" gap {len(gap)} {gap}")

# 4) ceiling with all used primes
print("\n[4] structural ceiling over used primes (each allowed-residue fraction):")
used_primes = sorted(prime_cover)
core = 1.0
for p in used_primes:
    _, allowed, _ = gaps_all[p]
    # fraction of nonzero residues that are QNR-allowed = |allowed|/(p-1) or of all p:
    frac_allowed = len(allowed) / p   # including the p|n zero residue as covered-elsewhere
    core *= (1 - frac_allowed) if False else (p - len(allowed)) / p
print(f"    primes: {used_primes}")
detail = [(p, round((p - len(gaps_all[p][1]))/p, 6)) for p in used_primes]
print(f"    per-prime uncovered fractions (QR-blocked incl. zero-residue): {detail}")
ceiling = 1 - core
print(f"    irreducible uncovered density (per K-branch): {core:.7f} = {100*core:.4f}%")
print(f"    coverage ceiling: {ceiling:.7f} = {100*ceiling:.4f}%")