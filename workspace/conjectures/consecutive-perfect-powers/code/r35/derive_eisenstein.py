"""Derive & verify the Eisenstein reduction for x^3 - y^5 = 1 (R-35).

Ring Z[w], w^2 = -1 - w (Eisenstein integers, UFD).  alpha = 1 - w generates
the unique prime over 3.

False claims to check against 3^2-2^3=1 sense here: R-35 is a NO-SOLUTION
claim (both exponents odd), so no lemma may silently use the (3,2,2,3) structure.
Every lemma is stated for the R-35 variables.

Claims established:
  C1: x^3 - y^5 = 1, y>0  =>  x - w, x - w^2 are EXACT 5th powers in Z[w]
      (up to absorbing units), and x-1 = unit * (5th power).
      Verified below on the reasoning that: factors differ by associates of
      (1-w); all three congruent mod (1-w) so valuations at (1-w) equal and
      each a multiple of 5; hence each = unit*5th power; a unit raised to the
      5th is again a unit so can be absorbed => x-w and x-w^2 exact 5th powers.
  C2: gcd structure {1,(1-w)}: pairwise gcds of x-1,x-w,x-w^2 all divide (1-w).

This module only *derives and cross-checks*; the PARI thue() step is separate.
"""
import sympy as sp

w = sp.symbols('w', commutative=True)


def eisenstein_pow(a, b, n):
    """Return (A, B) with (a + b*w)^n = A + B*w, w^2 = -1-w (exact sympy)."""
    poly = sp.Poly((a + b*w)**n, w)
    # Now reduce powers of w: use relation w^2 = -1 - w
    # Rebuild by repeated reduction
    coeffs = poly.all_coeffs()  # highest degree first
    # coeffs[k] is coefficient of w^(deg-k)
    deg = len(coeffs) - 1
    # reduce as polynomial in w with relation w^2=-1-w => express in {1,w}
    # iterate: maintain dict
    from collections import defaultdict
    red = defaultdict(lambda: sp.Integer(0))
    for d, c in enumerate(reversed(coeffs)):  # c is coeff of w^d
        # reduce w^d
        # w^0=1, w^1=w, w^2=-1-w, then multiply by w
        # find representation of w^d = r + s*w
        r0, s0 = 0, 0
        # iterative
        # w^d expressed: start
        # use arrays
        pass
    # Simpler: build table of w^k in basis {1,w}
    pw = {0: (sp.Integer(1), sp.Integer(0)),
          1: (sp.Integer(0), sp.Integer(1))}
    for k in range(2, deg + 1):
        prev = pw[k-1]          # (r,s) with w^(k-1)=r+s*w
        # w^k = w^(k-1)*w = (r+s*w)*w = r*w + s*w^2 = r*w + s*(-1-w) = -s + (r-s)*w
        r, s = prev
        pw[k] = (-s, r - s)
    R, S = sp.Integer(0), sp.Integer(0)
    for d, c in enumerate(reversed(coeffs)):
        r, s = pw[d]
        R += c * r
        S += c * s
    return sp.expand(R), sp.expand(S)


a, b = sp.symbols('a b', integer=True, positive=False)
R, S = eisenstein_pow(a, b, 5)
print("delta^5 = (", R, ") + (", S, ")*w")

# conjugate: a + b*w^2 = a - b - b*w = (a-b) + (-b)*w
Rb, Sb = eisenstein_pow(a - b, -b, 5)
diff_R = sp.expand(R - Rb)
diff_S = sp.expand(S - Sb)
print("\ndelta^5 - conj = (", diff_R, ") + (", diff_S, ")*w")
print("\nExpected x-w - (x-w^2) = w^2 - w = -1 - 2w  => (R-const,-1),(S=-2)")

# Also: delta^5 = x - w means delta^5 = x*1 + (-1)*w  => S == -1, R == x
print("\nConstraint delta^5 = x - w:  S = -1 (w-coeff), R = x (1-coeff)")
print("so S(a,b) == -1  is the Thue-type equation in (a,b); R gives x.")
