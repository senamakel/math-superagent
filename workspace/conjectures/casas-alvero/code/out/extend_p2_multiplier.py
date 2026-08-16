"""Fast exact p=2 Hasse-CA satisfier count for monic degree-n polys over F2.

Represents a polynomial sum c_j x^j as the integer whose bits are c_j.
Over F2, the i-th Hasse derivative H_i has coeff of x^j equal to
C(j,i) mod 2 = 1 iff (i & j) == i (Lucas).  gcd computed by Euclidean
algorithm on bit-polynomials, exact, no floats, no sympy.

Hasse-CA holds for monic f iff gcd(f, H_i) is non-constant for every
i = 1..n-1 (gcd(f,0)=f is trivially non-constant, so a vanishing H_i passes).

This extends the run's n<=16 enumeration to n=17..20, itself verified by the
rule-9 oracle at small n (compare against lib.casas_alvero.is_ca_hasse where
feasible).  What the larger n settle: whether m(n,2)=sat/2 = 1 exactly at the
2-powers 4,8,16 (the good-primes-for-2^k hypothesis) and where new spikes land.
"""
from math import gcd as _int_gcd  # not used; placeholder to keep import intent clear


def Cparity(n, k):
    """C(n,k) mod 2 = 1 iff (k & n) == k (Lucas)."""
    return (k & n) == k


def hasse_deriv(fbits, i):
    """H_i(f) as bit-polynomial, given fbits (bit j = coeff of x^j)."""
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i:
                out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out


def pmod(a, b):
    """a mod b over F2 (polynomial remainder), b != 0."""
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    """Euclidean gcd of two bit-polynomials (mod 2)."""
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue          # gcd(f,0)=f, non-constant -> passes
        if pgcd(fbits, hi) == 1:
            return False
    return True


def is_pure_power_f2(fbits, n):
    """Over F2 the only monic degree-n pure power is (x+a)^n; over F2 pure
    powers have all coefficients a single pattern.  Use: f = (x+c)^n.  Expand
    and compare.  (x+1)^n and x^n."""
    # (x)^n = x^n -> fbits == 1<<n
    if fbits == (1 << n):
        return True
    # (x+1)^n over F2: coeff of x^j is C(n,j) mod 2
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j):
            bits |= 1 << j
    return fbits == bits


def counts(n, p=2):
    sat = ce = 0
    nones = 0
    for v in range(1 << n):
        fbits = (1 << n) | v    # monic
        if is_ca_f2(fbits):
            sat += 1
            if not is_pure_power_f2(fbits, n):
                ce += 1
    return sat, ce


if __name__ == "__main__":
    # --- oracle check at small n against lib.casas_alvero ----------------
    from lib.casas_alvero import is_ca_hasse as ref_ca, is_pure_power as ref_pp
    from sympy import symbols, Poly, GF
    x = symbols("x")
    ok = True
    for n in (3, 4, 5):
        for v in range(1 << n):
            fbits = (1 << n) | v
            f = Poly(x**n + sum(((v >> j) & 1) * x**j for j in range(n)),
                     x, domain=GF(2))
            mine_ca = is_ca_f2(fbits)
            mine_pp = is_pure_power_f2(fbits, n)
            refc = ref_ca(f, 2)
            refp = ref_pp(f, 2)
            if mine_ca != refc or mine_pp != refp:
                ok = False
                print(f"MISMATCH n={n} v={v}: mine({mine_ca},{mine_pp}) "
                      f"ref({refc},{refp})")
    print("oracle check (n=3,4,5, all 2^n polys):", "PASS" if ok else "FAIL")

    print("p=2 multiplier m=sat/2, counterexamples ce, n=17..20")
    for n in (16, 17, 18, 19, 20):
        if (1 << n) > 2_100_000:
            print(f"n={n}: SKIP 2^n={1<<n}")
            continue
        sat, ce = counts(n)
        print(f"n={n:2d}: 2^n={1<<n:7d} sat={sat:8d} m=sat/2={sat//2:6d} "
              f"(m==1? {sat//2==1}) ce={ce}")
