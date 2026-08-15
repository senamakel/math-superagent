#!/usr/bin/env python3
"""Clean exact proofs of the two unconditional modular lemmas for
T(c,p) = (x^p-1)/(x-1),  x = c^2+1,  p odd prime >= 3:

  LEMMA A: c odd  ==>  T(c,p) == 7 (mod 8).   (mod-8 residue is p-independent)
  LEMMA B: c even, p == 3 (mod 4)  ==>  T(c,p) == 3 (mod 4).

Both make T not a perfect square (squares mod 8 are 0,1,4; mod 4 are 0,1).
All arithmetic exact (sympy Mod with explicit value substitutions).

Proof of A: c odd  =>  c^2 == 1 (mod 8)  =>  x = c^2+1 == 2 (mod 8).
  x^k = 0 (mod 8) for k >= 3 (x has exactly one factor of 2, so x^3 has
  2^3 = 8).  Hence  T = 1 + x + x^2 (mod 8) = 1 + 2 + 4 = 7 (mod 8).
  (x^2 = (c^2+1)^2 = c^4 + 2c^2 + 1 == 1 + 2 + 1 = 4 mod 8.)
Proof of B: c even  =>  c^2 == 0 (mod 4)  =>  x == 1 (mod 4)  =>  x^k == 1
  (mod 4) for all k  =>  T = sum of p ones = p == 3 (mod 4)  (p == 3 mod 4).
"""
import sympy as sp

c = sp.symbols('c', integer=True)
p = sp.symbols('p', integer=True)


def T(cv, pv):
    x = cv * cv + 1
    return (x ** pv - 1) // (x - 1)


def is_odd_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


print("=== LEMMA A: c odd  ==>  T(c,p) == 7 mod 8 ===")
# symbolic residue for any c: T mod 8 restricted to x=c^2+1, k>=3 vanish
expr = sp.Mod(1 + (c * c + 1) + (c * c + 1) ** 2, 8)
print(f"  1 + x + x^2 mod 8 as function of c:  {expr}")
oddw = []
for cmod in (1, 3, 5, 7):
    v = int(expr.subs(c, cmod))
    oddw.append((cmod, v))
print(f"  evaluating at c mod 8 = 1,3,5,7: {oddw} -> always 7")
okA = all(int(expr.subs(c, m)) == 7 for m in (1, 3, 5, 7))
# numeric confirmation on a wide range
okA_num = all(T(cc, pp) % 8 == 7
              for cc in range(1, 2000, 2)
              for pp in [q for q in range(3, 101) if is_odd_prime(q)])
print(f"  symbolic: {okA}   numpy (odd c<2000, primes<101): {okA_num}")
print("  Since 7 is a non-square mod 8,  c odd  ==>  T not a square.")

print("\n=== LEMMA B: c even, p == 3 mod 4  ==>  T == 3 mod 4 ===")
okB = all(T(cc, pp) % 4 == 3
          for cc in range(2, 2000, 2)
          for pp in [q for q in range(3, 101)
                     if is_odd_prime(q) and q % 4 == 3])
print(f"  numpy (even c<2000, primes<101 with p==3 mod4): {okB}")
print("  Since 3 is a non-square mod 4,  T not a square.")

print("\n=== surviving class ===")
print("  Only (c even, p == 1 mod 4) remains.  x = c^2+1 = 5, 10, 17, 26, "
      "37, ... (x >= 5).")
print("  This is the class governed by Ljunggren's theorem (see note).")
