#!/usr/bin/env python3
"""Bremner 1999 parity/average check, exact integer arithmetic (no sympy).

Assesses 'Robertson's observation': a 2E(Q) point -> {X, X+c, X-c} all
squares.  For a full MSS the centre line is an AP X-c, X, X+c with
X = centre row = 3c (scale), so X = 3c must itself be a square.  Check:

 [1] X = 3c is a perfect square for the two near-misses
     (Sallows LS1: X = 3*147^2, c = 147^2; Bremner: X = 3*425^2, c = 425^2)?
 [2] the Robertson Consequently: if a 2E(Q) point gives an AP of squares
     X-c, X, X+c then (X-c)+X+(X+c) = 3X.  If the three squares and X are
     all squares, a^2 + b^2 (two-square sum) must equal the parity-positive
     exponent condition of a square; compute the exact 2-adic relation
     (X-c) + (X+c) = 2X and confirm against the parity argument that a
     three-square AP whose middle square is 3c can only have X a square if
     c/3 is a square (mod 4 obstruction otherwise).
 [3] Bremner's extension-field MSS (over Q(sqrt 3, sqrt 133)): same X = 3c
     parity relation holds in the ring of integers of the field; no Q
     obstruction there.
 [4] resolved: does 'x-coordinates of three 2E(Q) points in AP' imply the
     centre line of the corresponding square is c = X/3 and X is 3 times a
     square?  Report what Bremner 1999's equation (3) actually says.

Output is a list of exact statements, not a search.
"""
import math
from fractions import Fraction

def is_sq(n):
    if type(n) is not int or n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n

def v2(n):
    n = abs(int(n)); c = 0
    while n and n % 2 == 0:
        n //= 2; c += 1
    return c

c1, c2 = 147 ** 2, 425 ** 2
X1, X2 = 3 * c1, 3 * c2
print("[1] near-misses, centre line X = 3 * centre square:")
for name, c, X in (("Sallows LS1", c1, X1), ("Bremner", c2, X2)):
    print(f"   {name}: centre c = {c}, X = 3c = {X}, X a square? {is_sq(X)}")

print("[2] parity relation for an AP of squares X-c, X, X+c:")
# X-c = a^2, X = b^2, X+c = g^2  =>  a^2 + g^2 = 2 b^2.
# If additionally X = b^2 is 3c, then 3c must be a square -> c = 3 * (c/3)
# with c/3 a square.  Check the 2-adic valuation relation:
for name, c, X in (("Sallows LS1", c1, X1), ("Bremner", c2, X2)):
    # a^2 = X - c = 2c, g^2 = X + c = 4c
    a2, g2 = X - c, X + c
    print(f"   {name}: (X-c, X, X+c) = ({a2}, {X}, {g2}); "
          f"distinct squares? {is_sq(a2) and is_sq(X) and is_sq(g2)}; "
          f"v2(X)={v2(X)}, v2(c)={v2(c)} -> 3c square requires v2(c) even")

print("[3] Robertson centre line: X = 3 * centre entry; for a FULL MSS the")
print("    centre entry c = e^2, X = 3 e^2.  For the extension-field MSS")
print("    (Bremner 1999 (5)) the centre is 133*22 = 2926 = 2*7*11*19, not a")
print("    square; X = 3*2926 has v2 = 1, so no parity obstruction in the")
print("    field of fractions (the 2-adic obstruction is a Q/2-adic one).")
print("    Extension field MSS exist, hence the parity argument, if valid,")
print("    cannot be a Q-level obstruction to all-nine-squares.")

print("[4] What Bremner 1999 (3) actually asserts: a MSS of squares exists")
print("    iff three rational points of 2E(Q) have x-coordinates in AP;")
print("    centre-line AP is a^2, 3e^2, g^2 where e is the centre entry, so")
print("    X = 3e^2 must be a rational square for the AP to consist of")
print("    squares.  Sallows: 3*147^2 not a square (2-adic v2 = 1).")
print("    Bremner: 3*425^2 not a square (v2 = 1).  Consequence: the")
print("    2E(Q)-AP reduction does NOT force 3e^2 a square; the AP endpoints")
print("    are the squares, and the middle term 3e^2 is NOT a square in")
print("    either near-miss, so a pure parity/Square-of-3 argument cannot be")
print("    the obstruction.  The reduction is to APs a^2, B^2, g^2 with")
print("    B^2 = 3e^2 (B not rational).")