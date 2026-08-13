#!/usr/bin/env python3
"""Verify the mod-3 and mod-5 single-residue claim with REAL primitive pairs,
and check whether a triple is excluded because all q in Phi are congruent to a
common non-zero residue mod p."""
from math import gcd

def f_mod(m, n, mod):
    m2 = (m*m) % mod; n2 = (n*n) % mod
    sn = (m2 + n2) % mod
    if sn == 0:
        return None  # denominator 0 mod p -> no finite residue
    inv = pow(sn, -1, mod)
    num = (4*m*n*(m2 - n2)) % mod
    return (num * inv * inv) % mod

def primitive_pairs(M):
    for m in range(2, M+1):
        for n in range(1, m):
            if gcd(m,n)==1:
                yield m,n

for mod in [3,5]:
    seen = {}
    singleres = None
    allsame = True
    for m,n in primitive_pairs(100):
        r = f_mod(m,n,mod)
        if r is None:
            continue
        seen[r] = seen.get(r,0)+1
        if singleres is None:
            singleres = r
        elif singleres != r:
            allsame = False
    print(f"mod={mod}: distinct residues among primitive pairs m,n<=100: "
          f"{sorted(seen.items())}")
    print(f"   all-same-residue: {allsame}, common residue: {singleres}, "
          f"2r==r mod {mod}? {singleres is not None and (2*singleres)%mod == singleres}")
    # Also check the denominator-nonzero condition: how many pairs skipped?
    skipped = sum(1 for m,n in primitive_pairs(100) if f_mod(m,n,mod) is None)
    print(f"   pairs with denominator 0 mod {mod}: {skipped}")
