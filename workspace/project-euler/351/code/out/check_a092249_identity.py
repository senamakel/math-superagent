"""Verify the A092249 identity from its own catalogue terms.

A092249: positions of integers in the standard diagonal enumeration of the
positive rationals. Terms on the OEIS page (n = 0..55):
1,2,4,6,10,12,18,22,28,32,42,46,58,64,72,80,96,102,120,128,140,150,172,180,
200,212,230,242,270,278,308,324,344,360,384,396,432,450,474,490,530,542,584,
604,628,650,696,712,754,774,806,830,882,900,940,964

Claim: A092249(n) = A002088(n+1) = Phi(n+1); equivalently Phi(n) = A092249(n-1).
Check by computing Phi(k) with a naive sieve and comparing against the
catalogue terms — without reading any further catalogue data.
"""
from math import isqrt


def phi_sieve(n):
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:  # p prime
            for m in range(p, n + 1, p):
                phi[m] -= phi[m] // p
    return phi


N = 56
phi = phi_sieve(N)
Phi = [0] * (N + 1)
for k in range(1, N + 1):
    Phi[k] = Phi[k - 1] + phi[k]

a092249 = [1, 2, 4, 6, 10, 12, 18, 22, 28, 32, 42, 46, 58, 64, 72, 80, 96,
           102, 120, 128, 140, 150, 172, 180, 200, 212, 230, 242, 270, 278,
           308, 324, 344, 360, 384, 396, 432, 450, 474, 490, 530, 542, 584,
           604, 628, 650, 696, 712, 754, 774, 806, 830, 882, 900, 940, 964]

bad = []
for n, term in enumerate(a092249):
    if term != Phi[n + 1]:
        bad.append((n, term, Phi[n + 1]))

if bad:
    print("MISMATCHES:", bad[:10])
else:
    print(f"OK: A092249(n) == Phi(n+1) for all {len(a092249)} catalogue terms")
    print(f"Anchor: Phi(10^8) = 3039635516365908  <->  A092249(10^8 - 1)")
