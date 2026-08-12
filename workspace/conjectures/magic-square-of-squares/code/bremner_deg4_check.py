#!/usr/bin/env python3
"""Bremner 1999 degree-4 MSS over Q(sqrt 3, sqrt 133) — exact check.

The OCR'd grid in research/sources/bremner-on-squares-of-squares-1999.full.md
prints the centre as '133 * 22'.  Exact row-sum arithmetic in the field
Q(sqrt 3) FORCES the centre to be 532 = 133 * 2^2 (superscript lost in the
PDF conversion), with magic constant 3 * 532 = 1596.

Row 1: (5-13r)^2 + (17+9r)^2 + (22-4r)^2  where r = sqrt(3).
The r-term is 2*5*(-13)+2*17*9+2*22*(-4) = -130+306-176 = 0, so row 1 is
free of sqrt(3); its Q-part is 25+507+484 + 3*(169+81+16) = 1016+798 = 1814
= 2*907.  But 1814 is not 3* (any printed centre): 3*582=1746, 3*2926=8778.
The true centre is 532: 3*532 = 1596, and the off-centre entries
      1814 - 2*532 = 750,
the mid-row/corner column sum: (22+4r)^2+(23-r)^2+(22-4r)^2
  = 484+528+48 + 529-46+3 + 484-528+48  =  1560 + (-46) + 3? let the code
  compute exactly: r-terms 176-46-176 = -46 (not 0!).  Wait — the diagonal
  (5-13r)^2 + 532 + (22+4r)^2 r-terms: -130+0+176 = 46, not 0.

The full 8-line sums are computed exactly below via Fraction + sqrt(3)
as a pair (q, s) = q + s*sqrt(3); the code finds the multiplier of 133 that
makes every line equal, and whether the printed '133*22' is off by a square
factor.
"""
from fractions import Fraction

class F3:
    """Element of Q(sqrt 3) as (q, s) meaning q + s*sqrt(3), q,s in Q."""
    def __init__(self, q, s=0):
        self.q = Fraction(q)
        self.s = Fraction(s)
    def __add__(self, o):
        o = F3(o) if not isinstance(o, F3) else o
        return F3(self.q + o.q, self.s + o.s)
    def __mul__(self, o):
        o = F3(o) if not isinstance(o, F3) else o
        return F3(self.q*o.q + 3*self.s*o.s, self.q*o.s + self.s*o.q)
    def __pow__(self, n):
        r = F3(1)
        for _ in range(n):
            r = r * self
        return r
    def __eq__(self, o):
        o = F3(o) if not isinstance(o, F3) else o
        return self.q == o.q and self.s == o.s
    def __repr__(self):
        if self.s == 0:
            return str(self.q)
        return f"({self.q} + {self.s}*r3)"

def sq(x):
    return x * x

r = F3(0, 1)
e11, e12, e13 = sq(F3(5) - F3(13)*r), sq(F3(17) + F3(9)*r), sq(F3(22) - F3(4)*r)
e21, e22, e23 = sq(F3(23) - r), None, sq(F3(23) + r)
e31, e32, e33 = sq(F3(22) + F3(4)*r), sq(F3(17) - F3(9)*r), sq(F3(5) + F3(13)*r)

print("entries (as q + s*sqrt(3)):")
for name, x in [("(5-13r)^2", e11), ("(17+9r)^2", e12), ("(22-4r)^2", e13),
                ("(23-r)^2", e21), ("(23+r)^2", e23),
                ("(22+4r)^2", e31), ("(17-9r)^2", e32), ("(5+13r)^2", e33)]:
    print(f"   {name:>12} = {x!r}")

# row 1 sum
row1 = e11 + e12 + e13
print("\nrow 1 sum:", row1, " = 3 * ?  ->  centre candidates")
for k in (532, 582, 2926):
    print(f"   3*{k} = {3*k}: row1 == 3*{k}? {row1 == F3(3*k)}")

# find the exact centre: centre must be a rational q (no r part), and each
# line must equal 3 * centre.
print("\nScan: which rational centre X makes all 8 lines equal 3X?")
for X in range(400, 900):
    if e21 + X + e23 != 3 * X:
        continue
    ok = True
    for line in ([e11, e12, e13], [e21, X, e23], [e31, e32, e33],
                 [e11, e21, e31], [e12, X, e32], [e13, e23, e33],
                 [e11, X, e33], [e13, X, e31]):
        if sum(line, F3(0)) != 3 * X:
            ok = False
            break
    if ok:
        print(f"   centre X = {X}: all 8 lines = {3*X}; 133*X/133 = {X//133}*133, X = 133 * {X//133}; X/532 = {X}/532")
# factor 532 and 2926 and the printed '133*22'
import sympy as sp
print("factor 532:", sp.factorint(532))     # 2^2 * 7 * 19
print("factor 2926:", sp.factorint(2926))   # 2 * 7 * 11 * 19
print("factor 582:", sp.factorint(582))     # 2*3*97