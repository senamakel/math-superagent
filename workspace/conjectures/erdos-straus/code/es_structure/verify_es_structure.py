"""Verify the structural claims behind the 'six open classes mod 840' picture.

Oracle and claims checked:
  0. solves() exact rational check of 4/n = 1/x+1/y+1/z on examples.
  1. Symbolic verification that the classical identity families are genuine:
          4/(3t-1) = 1/t + 1/(3t-1) + 1/(t(3t-1))        [n ≡ 2 mod 3]
          4/(4t-1) = 1/t + 1/(t(4t-1))  (two terms; third split) [n ≡ 3 mod 4]
          4/(8t-3) = 1/(2t) + 1/(t(8t-3)) + 1/(2t(8t-3))  [n ≡ 5 mod 8]
     (The mod 5 and mod 7 families are attested by Mordell/Wikipedia but their
     explicit polynomial forms are not in this run's sources; only the residue
     covering is computed here.)
  2. Among prime-candidate residue classes (odd, coprime to 3,5,7) mod 840,
     the five families n≡2 mod 3, 3 mod 4, 2/3 mod 5, 3/5/6 mod 7, 5 mod 8
     cover everything except {1,121,169,289,361,529}.
  3. Those six survivor classes are exactly the quadratic residues among the
     prime-candidate classes mod 840, and all ≡ 1 mod 24.
  4. Smallest prime in the union of the six classes is 1009.
  5. Each six-class contains odd squares (so the six classes contain infinitely
     many odd perfect squares => Prop 1.6 applies to members).
  6. Numerically (ELT Prop 1.6): for odd squares n = 9..169, no solution in
     the search box is Type I or Type II under the COPRIMMALITY-constrained
     definitions (Type I: n | x, gcd(n,y)=gcd(n,z)=1; Type II: n|y,n|z,
     gcd(n,x)=1).  Finite box (x,y,z <= 6n); NOT a proof.
"""
from fractions import Fraction
from math import gcd
import sympy

def solves(n, x, y, z):
    if not all(isinstance(v,int) for v in (x,y,z)):
        return False
    if min(x,y,z) <= 0:
        return False
    return Fraction(4, n) == Fraction(1,x) + Fraction(1,y) + Fraction(1,z)

print("Claim0: oracle checks...")
assert solves(5, 2, 4, 20)
assert solves(5, 2, 5, 10)
assert solves(9, 3, 18, 18)
assert not solves(5, 1, 1, 1)
print("   OK: n=5 (two solutions), n=9 (3,18,18), n=5 negative check.")

# ---------- Claim 1: symbolic identity families ------------------------
from sympy import symbols, simplify, Rational
t = symbols('t', integer=True)

def ident(name, n_expr, *denoms):
    s = Rational(4) / n_expr - sum(1/d for d in denoms)
    ok = (simplify(s) == 0)
    print(f"Claim1: {name}: {'OK' if ok else 'FAIL'}")
    assert ok

N1 = 3*t - 1            # n ≡ 2 mod 3
ident("n=3t-1 (2 mod 3): 4/n=1/t+1/n+1/(tn)", N1, t, N1, t*N1)
N2 = 4*t - 1            # n ≡ 3 mod 4
ident("n=4t-1 (3 mod 4): 4/n=1/t+1/(t(4t-1)) [2-term]", N2, t, t*N2)
N3 = 8*t - 3            # n ≡ 5 mod 8
ident("n=8t-3 (5 mod 8): 4/n=1/(2t)+1/(t n)+1/(2t n)", N3, 2*t, t*N3, 2*t*N3)

# ---------- Claim 2: covering mod 840 ---------------------------------
def covered(r):
    return (r%3==2) or (r%4==3) or (r%5 in (2,3)) or (r%7 in (3,5,6)) or (r%8==5)

prime_cands = [r for r in range(840) if r%2==1 and r%3!=0 and r%5!=0 and r%7!=0]
uncovered = [r for r in prime_cands if not covered(r)]
print("Claim2: uncovered among prime candidates:", uncovered)
expected = [1,121,169,289,361,529]
assert uncovered == expected
print("   == literature six classes.")

# ---------- Claim 3: survivors are squares, ≡1 mod 24 ------------------
sq840 = sorted(set((s*s) % 840 for s in range(840)))
assert all(r in sq840 for r in expected)
assert all(r % 24 == 1 for r in expected)
squares_among_cands = [r for r in prime_cands if r in sq840]
print("Claim3: squares among prime candidates mod 840:", squares_among_cands)
assert squares_among_cands == expected
print("   survivors == squares among candidates; all ≡ 1 mod 24.")

# ---------- Claim 4: smallest prime in six classes ----------------------
smallest = {}
for r in expected:
    for p in range(2, 1200):
        if p % 840 == r and sympy.isprime(p):
            smallest[r] = p
            break
print("Claim4: smallest prime per class:", smallest)
assert min(smallest.values()) == 1009

# ---------- Claim 5: odd square members ---------------------------------
odd_sq = sorted(set((s*s) % 840 for s in range(1, 840, 2)))
print("Claim5: odd-square residues mod 840:", odd_sq)
assert all(r in odd_sq for r in expected)
# Explicit odd square representatives:
for r in expected:
    s0 = [s for s in range(1,840,2) if (s*s)%840 == r][0]
    print(f"   class {r}: n = {s0}^2 = {s0*s0} ≡ {r} (mod 840)")
print("   so each class contains the odd square n=s0^2, and (s0+840m)^2 too")

# ---------- Claim 6: Prop 1.6 numeric -----------------------------------
def type_of(n,x,y,z):
    if (x % n == 0) and gcd(y,n)==1 and gcd(z,n)==1:
        return 'I'
    if (y % n == 0) and (z % n == 0) and gcd(x,n)==1:
        return 'II'
    return None

def all_solutions(n, bound_factor=6):
    out = []
    for x in range(n//4+1, bound_factor*n+1):
        r1 = Fraction(4,n) - Fraction(1,x)
        if r1 <= 0: continue
        # y >= x, and 1/y < r1 so y > 1/r1
        ymin = max(x, int(1/r1) + (1 % r1 != 0))
        for y in range(ymin, bound_factor*n+1):
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
    print(f"Claim6: n={n:4d}: solutions={len(sols):3d}, Type I/II={len(ti)}")
    assert len(ti) == 0
print("Claim6: no Type I/II among odd-square solutions in box <= 6n (finite).")

print("ALL CHECKS PASSED")