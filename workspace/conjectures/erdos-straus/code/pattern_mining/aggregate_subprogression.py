#!/usr/bin/env python3
"""Parse the FOUND lines from the extended sub-progression search and compute
the exact union density (moduli M, residues c) of the finite sub-covering of
n=840K+1 (open class r=1)."""
import re
from math import gcd
from collections import defaultdict

txt = open('code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
fam = []
cur = None
for ln in lines:
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        fam.append((a, b))
print(f"parsed {len(fam)} families")

per = defaultdict(set)
for (a, b) in fam:
    M = a // 840
    r = b % 840
    assert r == 1, (a, b, r)
    c = (b - 1) // 840
    per[M].add(c)

for M in sorted(per):
    print(f"M={M:4}: {sorted(per[M])}  -> {len(per[M])}/{M} = {len(per[M])/M:.4f}")

if per:
    bound = sum(len(s)/m for m, s in per.items())
    print(f"sum-of-moduli coverage (upper bound on union): {bound:.4f}")
    L = 1
    for m in per:
        L = L // gcd(L, m) * m
    print(f"period L = {L}")
    if L <= 20_000_000:
        covered = 0
        for K in range(L):
            if any(K % m in s for m, s in per.items()):
                covered += 1
        print(f"EXACT union density over period L={L}: {covered}/{L} = {covered/L:.6f}")
    # Distinct residues per modulus with no covered residue
    print("\nmoduli with partial coverage:")
    for M in sorted(per):
        if len(per[M]) < M:
            missing = sorted(set(range(M)) - per[M])
            print(f"  M={M}: covered {len(per[M])}, missing {len(missing)}: {missing[:12]}{'...' if len(missing)>12 else ''}")
