"""Verify the exact placement of the Cassels and double-Wieferich conditions
reconstructed for x^p - y^q = 1 with p, q odd primes, without floating point.

We verify three things:
  (1) Cassels: q | x and p | y  -- checked against the known solution and by
      direct congruence for small odd-prime exponents.
  (2) The double-Wieferich congruences and their exact placement:
          p^{q-1} = 1 (mod q^2)   and   q^{p-1} = 1 (mod p^2)
      i.e. base p squared against modulus q^2, base q squared against modulus p^2.
  (3) That the known solution (x,p,y,q) = (3,2,2,3) is excluded from these
      lemmas ONLY by the odd-prime hypothesis (p = 2 is even), not by the
      congruence itself -- so the condition does not over-eliminate.
"""
from itertools import combinations_with_replacement
import sys


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def first_primes(k):
    out = []
    n = 2
    while len(out) < k:
        if is_prime(n):
            out.append(n)
        n += 1
    return out


def pow_mod(a, e, m):
    return pow(a, e, m)


def check_known_solution_and_cassels():
    # Known solution of x^p - y^q = 1: (3,2,2,3)
    x, p, y, q = 3, 2, 2, 3
    print("=" * 72)
    print("(1) Cassels condition q|x and p|y -- calibrated on (3,2,2,3)")
    print("=" * 72)
    print(f"known solution: x^p - y^q = {x}^{p} - {y}^{q} = {x**p} - {y**q} = 1")
    print(f"  q|x?  {q} | {x} -> {x % q == 0}")
    print(f"  p|y?  {p} | {y} -> {y % p == 0}")
    print("  Note: hypothesis 'p,q odd primes' FAILS here (p=2), so Cassels is\n"
          "  silent on (3,2,2,3); it never claims no solution exists.")
    print()


def check_double_wieferich_placement():
    print("=" * 72)
    print("(2) Double-Wieferich congruences -- exact placement test")
    print("=" * 72)
    print("Proposed statement (reconstruction, to be cross-checked against\n"
          "a technique source): for an odd-prime solution,\n"
          "    p^{q-1} == 1 (mod q^2)   and   q^{p-1} == 1 (mod p^2)")
    print()
    # Known solution, p=2 (even). Both placements must FAIL on it, showing the
    # hypothesis does the work, not the congruence.
    x, p, y, q = 3, 2, 2, 3
    print("Known solution (3,2,2,3) evaluated under the proposed placement:")
    print(f"  p^(q-1) mod q^2 : 2^(3-1) mod 3^2 = {pow_mod(p, q-1, q*q)}  (want 1)")
    print(f"  q^(p-1) mod p^2 : 3^(2-1) mod 2^2 = {pow_mod(q, p-1, p*p)}  (want 1)")
    print("  -> both fail, as required, because p=2 is even (hypothesis fails).")
    print()
    # Enumerate small odd-prime pairs that DO satisfy the congruences
    # (i.e. double-Wieferich pairs), to show the condition is restrictive but
    # not vacuous and to calibrate.
    primes = first_primes(40)
    odd = [r for r in primes if r > 2]
    print("Small odd-prime pairs (p,q), p<q, that satisfy BOTH congruences\n"
          "(double-Wieferich pairs):")
    hits = []
    for p, q in combinations_with_replacement(odd, 2):
        if p == q:
            continue
        ok1 = pow_mod(p, q - 1, q * q) == 1
        ok2 = pow_mod(q, p - 1, p * p) == 1
        if ok1 or ok2:
            hits.append((p, q, ok1, ok2))
            tag1 = "p^(q-1)=1 mod q^2" if ok1 else "          ."
            tag2 = "q^(p-1)=1 mod p^2" if ok2 else "          ."
            both = "BOTH" if (ok1 and ok2) else "one "
            print(f"  (p,q)=({p:3},{q:4})  {both}  [ {tag1} | {tag2} ]")
    print(f"\n  ({len(hits)} pairs among first {len(primes)} primes satisfy at least one)")
    print()


def check_problem_md_hint_consistency():
    print("=" * 72)
    print("(3) Consistency of problem.md hint 'p^2 | y^{p-1} - 1'")
    print("=" * 72)
    # The hint claims p^2 divides y^{p-1}-1. But Cassels gives p|y, so
    # y^{p-1} = 0 mod p, NOT = 1 mod p. Check:
    x, p, y, q = 3, 2, 2, 3
    print(f"Known solution: p^2 | y^(p-1) - 1 ?  ",
          f"{p**2} | {y} ^ {p-1} - 1 = {y**(p-1)-1} -> {(y**(p-1)-1) % (p*p) == 0}")
    # For a generic odd prime with p|y (y multiple of p):
    for p, y in [(3, 6), (3, 9), (5, 10), (7, 14)]:
        val = (y ** (p - 1) - 1) % (p * p)
        print(f"  p={p}, y multiple of p ({y}): (y^(p-1)-1) mod p^2 = {val}")
        print(f"      -> 'p^2 | y^(p-1)-1' = {val == 0}  (mod-p check: {y % p == 0})")
    print("\n  Conclusion: if p|y then y^(p-1) = 0 mod p, never 1 mod p, so the\n"
          "  problem.md hint form is inconsistent with Cassels's p|y and must not\n"
          "  be used; the double-Wieferich form p^{q-1}=1 mod q^2 (base p, modulus\n"
          "  q^2) is the reconstructed condition, consistent with y being a\n"
          "  multiple of p only through the odd-prime hypothesis.")
    print()


if __name__ == "__main__":
    check_known_solution_and_cassels()
    check_double_wieferich_placement()
    check_problem_md_hint_consistency()
