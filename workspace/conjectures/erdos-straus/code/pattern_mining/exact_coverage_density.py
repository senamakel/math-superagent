#!/usr/bin/env python3
"""Exact density (not a sample) of the finite sub-covering of the open class
n = 840K + 1 by the verified identity families.

Union indicator is periodic with period L = lcm of the moduli M = a/840 used.
Compute coverage exactly over one period.
"""
from math import gcd
from functools import reduce

# (a, MODULUS M, residue c)  : covers n=840K+1 with K≡c (mod M)
FAMS = [
    (9240, 11, 5), (9240, 11, 7), (9240, 11, 10),
    (10920, 13, 7), (10920, 13, 9), (10920, 13, 11), (10920, 13, 12),
    (14280, 17, 4),
]
lcm = lambda x, y: x // gcd(x, y) * y
L = reduce(lcm, [m for (_, m, _) in FAMS], 1)
print("period L =", L)

def covered(K):
    for (a, m, c) in FAMS:
        if K % m == c:
            return True
    return False

cnt = sum(1 for K in range(L) if covered(K))
print(f"exact density over one period: {cnt}/{L} = {cnt/L:.6f}")

# Also list the individual residue coverage per modulus
from collections import defaultdict
per = defaultdict(set)
for (a, m, c) in FAMS:
    per[m].add(c)
for m in sorted(per):
    print(f"M={m}: residues {sorted(per[m])}  -> {len(per[m])}/{m} = {len(per[m])/m:.4f}")
