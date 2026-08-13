"""Verify the structural claims behind the 'six open classes mod 840' picture.

Oracle and claims checked:
  0. solves(): exact rational check of 4/n = 1/x+1/y+1/z.
  1. The classical identities (Salez 1.1, Salez Example 0; Wikipedia):
       n = 3t-1  (n ≡ 2 mod 3):   4/n = 1/t + 1/(3t-1) + 1/(t(3t-1))
       n = 4t-1  (n ≡ 3 mod 4):   4/n = 1/t + 1/(t(4t-1))        (two terms;
                                   the third is supplied by splitting 1/t)
       n = 8t-3  (n ≡ 5 mod 8):   4/n = 1/(2t) + 1/(t(8t-3)) + 1/(2t(8t-3))
     are genuine algebraic identities (checked with sympy).
  2. Covering: among the residue classes that can hold infinitely many primes
     (odd, coprime to 3,5,7), the five families
       n ≡ 2 mod 3, n ≡ 3 mod 4, n ≡ 2 or 3 mod 5, n ≡ 3,5,6 mod 7,
       n ≡ 5 mod 8
     cover every class mod 840 EXCEPT {1,121,169,289,361,529}.
     (The mod-5 and mod-7 families are attested by Mordell/Wikipedia; their
     explicit polynomials are not in this run's sources, so only the residue
     covering is computed here, not their polynomial form.)
  3. The six survivor classes are exactly the quadratic residues (squares)
     among the prime-candidate classes mod 840; all six are ≡ 1 mod 24.
  4. Smallest prime in the union of the six classes is 1009.
  5. Each of the six classes contains infinitely many odd perfect squares.
  6. Numerically (ELT Prop 1.6): for odd squares n = 9,25,... every solution
     in the finite search box has NO coordinate-divisibility pattern that is
     Type I or Type II under the coprimality-constrained definition; the only
     solutions present have gcd(x,n)>1 with n|x (or similar), so they are
     neither type.  Finite bound, not a proof.
"""
import math
from fractions import Fraction
from math import gcd
import sympy

def solves(n, x, y, z):
    if not all(isinstance(v,int) for v in (x,y,z)):
        return False
    if min(x,y,z) <= 0: return False
    return Fraction(4, n) == Fraction(1,x) + Fraction(1,y) + Fraction(1,z)

# ---------- Claim 0: exact rational oracle on knowns -----------------
assert solves(5, 2, 4, 20)
assert solves(5, 2, 5, 10)
assert solves(9, 3, 18, 18)
assert not solves(5, 1, 1, 1)
print("Claim0: exact rational oracle works on n=5, n=9 examples.")

# ---------- Claim 1: the classical identities ------------------------
from sympy import symbols, simplify, Rational
k = symbols('k', integer=True)

def ident(name, n_expr, *denoms, max_terms=3):
    """Check 4/n - sum(1/denom) == 0 symbolically."""
    s = Rational(4) / n_expr - sum(1/d for d in denoms)
    d = simplify(s)
    ok = (d == 0)
    print(f"Claim1: {name}: {'OK' if ok else 'FAIL'}  terms={len(denoms)}")
    assert ok

# n = 3t-1  (2 mod 3): 4/(3t-1) = 1/t + 1/(3t-1) + 1/(t(3t-1))
t = k; N1 = 3*t - 1
ident("n=3t-1 (2 mod 3), 3 terms", N1, t, N1, t*N1)
# n = 4t-1  (3 mod 4): 4/(4t-1) = 1/t + 1/(t(4t-1))  [2 terms]
N2 = 4*t - 1
ident("n=4t-1 (3 mod 4), 2 terms", N2, t, t*N2)
# n = 8t-3  (5 mod 8): 4/(8t-3) = 1/(2t) + 1/(t(8t-3)) + 1/(2t(8t-3))
N3 = 8*t - 3
ident("n=8t-3 (5 mod 8), 3 terms", N3, 2*t, t*N3, 2*t*N3)

# ---------- Claim 2: covering mod 840 --------------------------------
def covered(r):
    return (r%3==2) or (r%4==3) or (r%5 in (2,3)) or (r%7 in (3,5,6)) or (r%8==5)

prime_cands = [r for r in range(840) if r%2==1 and r%3!=0 and r%5!=0 and r%7!=0]
uncovered = [r for r in prime_cands if not covered(r)]
print("Claim2: uncovered classes among prime-candidate residues:", uncovered)
expected = [1,121,169,289,361,529]
assert uncovered == expected
print("   matches the six literature classes.")

# ---------- Claim 3: six classes are the squares, ≡ 1 mod 24 ---------
squares_mod840 = sorted(set((s*s) % 840 for s in range(840)))
assert all(r in squares_mod840 for r in expected)
assert all(r % 24 == 1 for r in expected)
print("Claim3: all six are squares mod 840 and ≡ 1 mod 24.")
# indeed, among prime candidates, the squares mod 840 are exactly expected?
squares_among_cands = [r for r in prime_cands if r in squares_mod840]
print("   squares among prime-candidate classes:", squares_among_cands)
assert squares_among_cands == expected

# ---------- Claim 4: smallest prime in the six classes ---------------
primes_in_six = []
for r in expected:
    for p in range(2, 1200):
        if (p % 840) == r and sympy.isprime(p):
            primes_in_six.append(p)
            break
print("Claim4: smallest prime per six class:", dict(zip(expected, primes_in_six)))
assert min(primes_in_six) == 1009

# ---------- Claim 5: each class has odd square members ---------------
odd_sq = sorted(set((s*s) % 840 for s in range(1, 840, 2)))
assert all(r in odd_sq for r in expected)
# members: n = s^2 ≡ r (mod 840); along s = s0 + 840m these are n = s^2 hitting r
print("Claim5: the six classes are hit by odd squares mod 840:",
      [r for r in expected if r in odd_sq])

# ---------- Claim 6: Prop 1.6 numerically (coprimality-aware) --------
def type_of(n,x,y,z):
    """Type I: n|x, gcd(n,y)=gcd(n,z)=1.  Type II: n|y and n|z, gcd(n,x)=1."""
    if n % x == 0:
        pass
    if (x % n == 0) and gcd(y,n)==1 and gcd(z,n)==1:
        return 'I'
    if (y % n == 0) and (z % n == 0) and gcd(x,n)==1:
        return 'II'
    return None

def all_solutions(n, bound_factor=6):
    """All (x<=y<=z) solutions with denominators <= bound_factor*n."""
    out = []
    for x in range(n//4+1, bound_factor*n+1):
        r1 = Fraction(4,n) - Fraction(1,x)
        if r1 <= 0: continue
        for y in range(x, bound_factor*n+1):
            r2 = r1 - Fraction(1,y)
            if r2 <= 0: continue
            if r2.numerator != 1: continue
            z = r2.denominator
            if z < y or z > bound_factor*n: continue
            if solves(n,x,y,z):
                out.append((x,y,z,type_of(n,x,y,z)))
    return out

for n in [9,25,49,81,121,169]:
    sols = all_solutions(n, bound_factor=6)
    ti = [s for s in sols if s[3] is not None]
    print(f"Claim6: n={n:4d} solutions={len(sols):3d} TypeI/II={len(ti)}")
    assert len(ti) == 0
print("Claim6: no coprimality-correct Type I/II for odd squares 9..169 (finite box).")

print("ALL CHECKS PASSED")