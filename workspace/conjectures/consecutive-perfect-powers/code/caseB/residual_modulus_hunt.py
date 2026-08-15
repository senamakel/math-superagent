#!/usr/bin/env python3
"""Hunt for a fixed modulus M on which T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k
is NEVER a square mod M over the residual class (c even >= 2, p odd prime
== 1 mod 8).  Case B of Catalan reduces x^p - y^2 = 1 to m^2 = T(c,p); the
mod-8 argument already closes every class except c even & p == 1 mod 8, and
this program asks whether one fixed M closes that last class.

STRUCTURAL RESULT (stated before running):

  For EVERY modulus M, take c = 2M (even, >= 2).  Then c^2 == 0 (mod M), so
    (c^2+1) == 1 (mod M)  and  (c^2+1)^k == 1 (mod M) for all k,
  hence
    T(2M, p) == sum_{k=0}^{p-1} 1 = p   (mod M).
  By Dirichlet's theorem there are infinitely many primes p == 1
  (mod lcm(8, M)); such a p is an odd prime with p == 1 mod 8 and
  p == 1 mod M, giving
    T(2M, p) == 1 == 1^2   (mod M),
  a square mod M.  So the residual class contains, for every M, a pair
  (c even, p==1 mod 8 prime) with T a square mod M.  Hence NO fixed modulus
  closes the class.  This program confirms the construction per candidate M
  (method A: uniform witness) and independently by enumeration (method B),
  then runs the sanity oracle (0 true squares in a box, consistent with
  Ljunggren).

All arithmetic exact (Python ints).  No floats.  T is summed directly
(never the (x^p-1)/(x-1) division) so the gcd(c^2, M) > 1 case is harmless.
"""

from math import isqrt


def is_prime(n):
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


def primes_1mod8_below(Pmax):
    return [p for p in range(17, Pmax) if p % 8 == 1 and is_prime(p)]


def least_prime_1mod(n):
    """Least odd prime p with p == 1 (mod n).  Exists by Dirichlet (gcd(1,n)=1)."""
    k = 1
    while True:
        cand = 1 + k * n
        if is_prime(cand):
            return cand
        k += 1


def squares_mod(M):
    return {(a * a) % M for a in range(M)}


def T_mod(c, p, M):
    """sum_{k=0}^{p-1} (c^2+1)^k mod M, direct summation (safe when
    gcd(c^2, M) > 1).  Exact integers."""
    x = (c * c + 1) % M
    t = 0
    term = 1  # x^0
    for _ in range(p):
        t = (t + term) % M
        term = (term * x) % M
    return t


def T_exact(c, p):
    x = c * c + 1
    return (x ** p - 1) // (x - 1)


def build_moduli():
    explicit = [3, 5, 7, 11, 13, 16, 17, 32, 9, 25, 49, 15, 21, 33]
    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    moduli = list(explicit)
    moduli += small_primes
    moduli += [q * q for q in small_primes]
    seen = set()
    out = []
    for m in moduli:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return sorted(out)


def main():
    moduli = build_moduli()
    Pmax_enum = 1000  # primes == 1 mod 8 below this, for method B
    enum_primes = primes_1mod8_below(Pmax_enum)

    print("=== Candidate moduli ===")
    print("M =", moduli)
    print()

    # Sanity oracle first: true squares in the exact box (must be 0).
    print("=== Sanity oracle: true integer squares of T(c,p), c even in [2,400],")
    print("    p prime == 1 mod 8 in [17,300]  (expect 0, consistent with Ljunggren) ===")
    oracle_primes = [p for p in primes_1mod8_below(301) if p <= 300]
    n_sq = 0
    first_hits = []
    for c in range(2, 401, 2):
        for p in oracle_primes:
            T = T_exact(c, p)
            r = isqrt(T)
            if r * r == T:
                n_sq += 1
                if len(first_hits) < 5:
                    first_hits.append((c, p, T))
    print(f"  true squares found: {n_sq}  (oracle_primes={oracle_primes})")
    if first_hits:
        print("  (unexpected) first hits:", first_hits)
    print()

    print("=== Per-modulus verdict (obstruction FAILS if ANY square residue exists) ===")
    print(f"{'M':>5} {'witness p':>10} {'T mod M':>8} {'is sq':>5} | {'enum any-sq':>11} | verdict")
    any_closes = False
    for M in moduli:
        sq = squares_mod(M)
        # Method A: uniform construction witness
        L = 8 * M // 2 if (8 % 2 == 0) else 0  # lcm(8,M) = 8*M/gcd(8,M)
        from math import gcd
        lcm8M = 8 * M // gcd(8, M)
        c_wit = 2 * M
        p_wit = least_prime_1mod(lcm8M)
        t_wit = T_mod(c_wit, p_wit, M)
        wit_sq = t_wit in sq
        # Method B: enumeration over even residues c in 0..M-1 and primes ==1 mod 8
        enum_any = False
        wit_enum = None
        for c in range(0, M):          # c mod M
            if c % 2 != 0:
                continue               # keep even residues only
            for p in enum_primes:
                if T_mod(c, p, M) in sq:
                    enum_any = True
                    wit_enum = (c, p)
                    break
            if enum_any:
                break
        closes = not (wit_sq or enum_any)   # obstruction succeeded?
        if closes:
            any_closes = True
        print(f"{M:>5} {p_wit:>10} {t_wit:>8} {str(wit_sq):>5} | {str(enum_any):>11} | "
              f"{'CLOSES' if closes else 'FAILS (class open)'}"
              + (f"   enum witness (c,p)={wit_enum}" if wit_enum and not wit_sq else ""))

    print()
    print("=== Overall ===")
    if any_closes:
        print("A modulus closes the residual class: RESULT (the class is closed elementarily).")
    else:
        print("NO fixed modulus M in the candidate set closes the residual class.")
        print("For EVERY M there is a pair (c even, p==1 mod 8 prime) with T a square mod M.")
        print("Uniform construction: c = 2M and p = least prime == 1 mod lcm(8,M);")
        print("then T(c,p) == p == 1 (mod M), the square 1^2.")
    print("EXIT_OK")


if __name__ == "__main__":
    main()
