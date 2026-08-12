#!/usr/bin/env python3
"""Check the two reasons the Hilbert-reciprocity/four-conics approach dies.

1. If c+d = A^2 and c-d = B^2 are both perfect squares, then the quaternion
   algebra (c+d, c-d) has Hilbert symbol (A^2, B^2)_p = 1 at every prime p
   (a square in an entry makes the symbol trivial), i.e. the algebra is the
   zero element of Br(Q). We verify the Hilbert-symbol fact (a^2, b)_p == 1.

2. All four AP points lie on the single conic X^2 + Y^2 = 2c, and that conic has
   the obvious rational point X=Y=e (c=e^2). We verify on Bremner's 7-square
   witness (c = 425^2) that each realized AP difference gives both c±d squares,
   and that the conic X^2+Y^2 = 2c has the rational point (e,e).
"""
import sympy
from sympy.ntheory.residue_ntheory import is_quad_residue

def legendre(a, p):
    """Legendre symbol (a/p) with p an odd prime, using Euler's criterion."""
    a = a % p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def hilbert_symbol_odd(a, b, p):
    """Hilbert symbol (a,b)_p for odd prime p, standard formula with units."""
    def v(x):
        n = 0
        x = int(x)
        while x % p == 0:
            x //= p
            n += 1
        return n
    ai, bi = int(a), int(b)
    va, vb = v(ai), v(bi)
    ua = ai // (p ** va)
    ub = bi // (p ** vb)
    # (p^a u, p^b v)_p = (-1)^{ab (p-1)/2} * ((u/p)^b * (v/p)^a)
    sgn = 1
    if (va * vb) % 2 == 1 and p % 4 == 3:
        sgn *= -1
    if vb % 2 == 1:
        sgn *= legendre(ua, p)
    if va % 2 == 1:
        sgn *= legendre(ub, p)
    return sgn

def check_splitness(c, d, primes):
    """If c+d=A^2 and c-d=B^2, verify (c+d,c-d)_p = 1 for all given primes."""
    A2, B2 = c + d, c - d
    A, B = sympy.isqrt(A2), sympy.isqrt(B2)
    assert A * A == A2 and B * B == B2, "assumption c±d both squares failed"
    ok = True
    for p in primes:
        s = hilbert_symbol_odd(A2, B2, p)
        if s != 1:
            ok = False
            print(f"  FAIL: (A^2, B^2)_{p} = {s}") 
    return (A, B, ok)

# ---- Brenner 7-square witness: c = 425^2 ----
c = 425 * 425
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("c =", c, "= e^2 with e =", 425)

# Realized AP differences from the witness: v=138600, u+v=97104
for label, d in [("v=138600", 138600), ("u+v=97104", 97104)]:
    A, B, ok = check_splitness(c, d, primes)
    print(f"{label}: c+d={c+d}={A}^2, c-d={c-d}={B}^2, "
          f"quaternion (c+d,c-d) split at all tested primes: {ok}")

# Half-realized difference: u=-41496 (c+u square, c-u not)
d = -41496
print(f"\nu=-41496: c+u={c+d} is square? {sympy.is_square(c+d)}, "
      f"c-u={c-d} is square? {sympy.is_square(c-d)}")

# ---- Conic X^2 + Y^2 = 2c : rational point (e, e) always exists since c=e^2 ----
print("\nConic X^2 + Y^2 = 2c: e^2 + e^2 =", 2 * c, "= 2c. Rational point (e,e) verified.")

# General fact check: (a^2, b)_p == 1 at several primes for random a,b
print("\nGeneral fact (a^2,b)_p == 1:")
import random
random.seed(1)
allok = True
for _ in range(200):
    a = random.randint(2, 2000)
    b = random.randint(2, 2000)
    for p in [3, 5, 7, 11, 13, 17, 19]:
        if hilbert_symbol_odd(a * a, b, p) != 1:
            allok = False
            print("  counterexample!", a, b, p)
print("  (a^2,b)_p == 1 for all 200 random (a,b) across 7 primes:", allok)
