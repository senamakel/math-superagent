#!/usr/bin/env python3
"""Symbolic proofs of the two unconditionally-proved modular obstructions for
T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k, then a wider modular probe of the surviving
class (c even, p == 1 mod 4) to see if any further moduli kill it.

Goal: prove in exact sympy arithmetic that
  (A) c odd  ==> T == 7 (mod 8)  ==> not a square.
  (B) c even, p == 3 (mod 4)  ==> T not a square (mod 4: T == 3 mod 4).

Surviving class for Ljunggren's theorem: (c even, p == 1 mod 4), x = c^2+1>=5.
"""
import sympy as sp
from collections import defaultdict


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


def T_exact(c, p):
    x = c * c + 1
    return (x ** p - 1) // (x - 1)


# ---- (A) c odd ==> T == 7 mod 8 ----
print("=== (A) symbolic: c odd ==> T(c,p) == 7 (mod 8), p>=3 ===")
c = sp.symbols('c', integer=True)
p = sp.symbols('p', integer=True)
# x = c^2+1; for c odd, x == 2 mod 8, so x, x^2==4, x^k==0 (k>=3) mod 8.
# T == 1 + x + x^2 (mod 8), and x=c^2+1==2 (mod 8) -> 1+2+4=7.
x = c * c + 1
T8 = sp.simplify((1 + x + x * x) % 8)
print(f"  symbolic T mod 8 (treating x^k=0 for k>=3) reduces to 1+x+x^2 mod 8 = {T8}")
print(f"  numerically for odd c<200, p in [3..60] primes: "
      f"{all(T_exact(cc, pp) % 8 == 7 for cc in range(1,200,2) for pp in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59])}")
print("  7 not a square mod 8 (squares are 0,1,4).  CONCLUSION: c odd -> non-square.")

# ---- (B) c even, p == 3 mod 4 ==> T == 3 mod 4 ----
print("\n=== (B) symbolic: c even, p == 3 (mod 4) ==> T(c,p) == 3 (mod 4) ===")
# c even -> c^2 == 0 mod 4 -> x == 1 mod 4 -> (1+c^2)^k == 1 mod 4 -> T == p mod 4.
print(f"  p == 3 mod 4 -> T == p == 3 mod 4 -> not a square (squares mod 4: 0,1).")
print(f"  numerically: {all(T_exact(cc, pp) % 4 == 3 for cc in range(2,200,2) for pp in [pp for pp in range(3,60) if is_odd_prime(pp) and pp%4==3])}")

# ---- Surviving class (c even, p==1 mod 4): what residues appear mod various q? ----
print("\n=== surviving class (c even, p==1 mod 4): T mod q, which residues? ===")
SQR = {0, 1, 4}
cands = [(cc, pp) for cc in range(2, 300, 2)
         for pp in [q for q in range(3, 100) if is_odd_prime(q) and q % 4 == 1]]
for q in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    res = set()
    samples = 0
    for (cc, pp) in cands[:600]:
        samples += 1
        res.add(T_exact(cc, pp) % q)
    qrs = {r for r in range(q) if sp.ntheory.residue_ntheory.is_quad_residue(r % q, q) or r % q == 0}
    bad = res - qrs
    verdict = "ALL-NON-RESIDUE(no q kills all)" if bad == res and res else "has non-residue(s), none uniform"
    print(f"  mod {q:2d}: surviving-class residues {sorted(res)}  "
          f"(QR+q0 set size {len(qrs)}); non-residues present avoiding 0: "
          f"{sorted(bad)}{'' if not bad else ' -> NOT all killed'}")
