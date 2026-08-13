#!/usr/bin/env python3
"""Verify the sharp structural ceiling of the polynomial-family approach.

Claim: n=840t+1 (in the open class r=1) is coverable by a SINGLE polynomial
identity (some sub-progression n = a*k + b, b≡1 mod 840, b QNR mod a) iff the
number n is NOT a perfect square.

Forward proof idea (verifiable here): if n is coverable by a family with
modulus M (prime factors ∤840 including some prime p), the family forces b=840s+1
QNR mod p with s≡t mod p, so n≡840t+1≡b QNR mod p. Hence n is a QNR mod some
prime, so n is not a perfect square.

Converse: if n is not a perfect square, there is a prime p with n a QNR mod p;
take M=p, s = t mod p; then b=840s+1 ≡ n (mod p) is QNR mod p so Schinzel-legal;
a Salez-type family at (a=840p, b=840s+1) is not forbidden (existence of
realization is the generator's job, but structurally legal).

We VERIFY numerically: for every n=840t+1 < N (non-square), exists a prime
p∤840 with n a QNR mod p; and for every square n=m^2≡1 mod 840 (<N), n is a QR
mod every prime p up to a bound.  The second is the sharp obstruction.
"""
from math import gcd, isqrt

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return pow(a, (p - 1) // 2, p)  # 1 QR, p-1 NQR

def primes_up_to(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]

PRIMES = primes_up_to(2000)          # primes used as candidate moduli (∤840)
NON840 = [p for p in PRIMES if p not in (2, 3, 5, 7)]

def sq_mod840(t):
    n = 840 * t + 1
    # n perfect square?
    r = isqrt(n)
    return r * r == n

# 1) NON-SQUARE n: verify exists prime p∤840 with n QNR mod p
bad_nonsquare = []
nonsquare_checked = 0
t = 0
while 840 * t + 1 < 500_000:
    n = 840 * t + 1
    if not sq_mod840(t):
        nonsquare_checked += 1
        found = any(legendre(n, p) == p - 1 for p in NON840[1:200])
        if not found:
            bad_nonsquare.append(n)
    t += 1
print(f"[1] non-square n=840t+1 < 5e5: {nonsquare_checked} checked, "
      f"{len(bad_nonsquare)} without a QNR-prime p∤840: {bad_nonsquare[:10]}")

# 2) SQUARE n≡1 mod 840: verify n is QR mod every prime p∤840 (sharp obstruction)
bad_square = []
square_cases = 0
t = 0
while 840 * t + 1 < 5_000_000:
    n = 840 * t + 1
    if sq_mod840(t):
        square_cases += 1
        # check n QR mod every prime p up to 2000, p∤840
        viol = [p for p in NON840 if legendre(n, p) == p - 1]
        if viol:
            bad_square.append((n, viol[:5]))
    t += 1
print(f"[2] square n=m^2≡1 mod 840 < 5e6: {square_cases} cases, "
      f"{len(bad_square)} that are NQR mod some prime∤840 (should be 0): "
      f"{bad_square[:5]}")
print("\nSo: the only n≡1 mod 840 that NO single polynomial identity can cover "
      "are the perfect squares m^2≡1 mod 840 (density 0, infinite). "
      "All other n are Schinzel-legal for some prime modulus (existence is the "
      "generator's job, not forbidden).")

# list a few squares ≡1 mod 840 exposed as the hard boundary
print("\nSquares m^2 ≡ 1 mod 840 up to 5e6:", end=" ")
m = 1
out = []
while m * m < 5_000_000:
    if (m * m) % 840 == 1:
        out.append(m * m)
    m += 1
print(out)
