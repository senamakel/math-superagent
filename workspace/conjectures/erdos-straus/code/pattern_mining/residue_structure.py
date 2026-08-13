#!/usr/bin/env python3
"""Analyze the algebraic structure of the covered residue sets t mod p
for each prime modulus p in the sub-progression covering of n=840K+1.

Each family (a=840M, b) with b==1 mod 840 covers t == (b-1)/840 mod M where
n=840t+1. Question: is the realizable set (reduced mod the odd prime factor of M)
closed under structurally-relevant operations? In particular:
  1. closed under negation t -> -t (mod p)?
  2. invariant under the Salez/Mordell conj-of-conditions that generated families?
  3. a subgroup/union-of-cosets of Z_p^*?

This constrains the saturation question for the open residue of modulus 23.
"""
import re
from collections import defaultdict

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

def odd_prime_factors(M):
    facs = []
    mm = M
    q = 2
    while q*q <= mm:
        if mm % q == 0:
            if q != 2 and q != 3:
                facs.append(q)
            while mm % q == 0:
                mm //= q
        q += 1
    if mm > 1 and mm not in (2, 3):
        facs.append(mm)
    return facs

prime_cover = defaultdict(set)   # p -> set of t mod p realized
for M, S in per.items():
    for p in odd_prime_factors(M):
        prime_cover[p].update(c % p for c in S)

print("Covered residues t mod p for each prime modulus p:")
for p in sorted(prime_cover):
    S = sorted(prime_cover[p])
    print(f"  p={p:3}: {len(S)}/{p}  covered={S}")

print()
print("=== structural checks ===")
for p in sorted(prime_cover):
    S = prime_cover[p]
    # exclude 0 when treating multiplicatively
    Spos = S - {0}
    # primitive root
    phip = p - 1
    facs = []
    mm = phip
    q = 2
    while q*q <= mm:
        if mm % q == 0:
            facs.append(q)
            while mm % q == 0:
                mm //= q
        q += 1
    if mm > 1:
        facs.append(mm)
    gen = next(g for g in range(2, p) if all(pow(g, phip//f, p) != 1 for f in facs))
    QR = {pow(gen, 2*e, p) for e in range(phip//2)}
    NQR = set(range(1, p)) - QR
    neg_closed = all((p - s) % p in S for s in S)
    # multiplicative closure within Spos (subgroup test)
    is_subgroup = bool(Spos) and all((a*b) % p in Spos for a in Spos for b in Spos)
    # union of cosets of the QR subgroup
    is_QR_cosets = (len(Spos & QR) == 0 or len(Spos & NQR) == 0) or \
                   (len(Spos & QR)==len(Spos & NQR))
    print(f"  p={p:3}: neg-closed={neg_closed}  subgroup={is_subgroup}  "
          f"|Spos&QR|={len(Spos&QR)} |Spos&NQR|={len(Spos&NQR)}  "
          f"|S&{{0}}|={1 if 0 in S else 0}")
