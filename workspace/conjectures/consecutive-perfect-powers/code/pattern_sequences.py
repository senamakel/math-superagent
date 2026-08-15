"""Pattern analysis for the Catalan descent data.

1. v_p(h^-(Q(zeta_p))): the p'-adic valuation of h^- at p, i.e. the p-part /
   index-of-irregularity quantity the descent would need to control. For p itself
   it is the local p-torsion of the minus class group. We compute h^- exactly
   (lib.cyclo, Fraction arithmetic) and factor out p.
2. Double-Wieferich odd-prime pairs (p<q): both p^(q-1)===1 mod q^2 and
   q^(p-1)===1 mod p^2, searched to a larger B, because these are the ONLY
   pairs the conditional theorem does not already exclude.
All exact integer arithmetic.
"""
from fractions import Fraction
from lib.cyclo import Cyclo, zero, zeta_pow
import sys, time


def primitive_root(p):
    from sympy import factorint
    qs = list(factorint(p - 1).keys())
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g


def index_table(p, g):
    logtab = {}
    v = 1
    for e in range(p - 1):
        logtab[v] = e
        v = (v * g) % p
    return logtab


def h_minus(p):
    n = p - 1
    g = primitive_root(p)
    logtab = index_table(p, g)
    prod = Cyclo(n, {0: Fraction(1)})
    for k in range(1, p - 1, 2):          # k odd <=> chi_k odd
        s = zero(n)
        for a in range(1, p):
            e = logtab[a]
            s = s + zeta_pow(n, k * e) * Fraction(a)
        B1 = s * Fraction(1, p)
        prod = prod * (Cyclo(n, {0: Fraction(-1, 2)}) * B1)
    h = prod * Fraction(2 * p)
    return int(h.as_fraction())


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def odd_primes_upto(B):
    return [n for n in range(3, B + 1) if is_prime(n)]


# ---------- Part 1: v_p(h^-(p)) for odd primes ----------
print("=" * 70)
print("Part 1: h^-(Q(zeta_p)) and its p-adic valuation v_p(h^-)")
print("=" * 70)
raw = {}
for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
    t = time.time()
    h = h_minus(p)
    raw[p] = h
    print("p=%3d  h^-=%d  v_p(h^-)=%d  p|h^-? %s  (%.1fs)"
          % (p, h, vp(h, p), h % p == 0, time.time() - t))
print("SEQUENCE h^-:", [raw[p] for p in sorted(raw)])
print("SEQUENCE v_p(h^-):", [vp(raw[p], p) for p in sorted(raw)])
print("irregular primes (p | h^-):", [p for p in sorted(raw) if raw[p] % p == 0])

# ---------- Part 2: double-Wieferich pairs ----------
print("=" * 70)
print("Part 2: double-Wieferich odd-prime pairs (p<q), p,q <= B")
print("=" * 70)
for B in [500, 2000, 10000]:
    t = time.time()
    ps = odd_primes_upto(B)
    pairs = []
    n = len(ps)
    for i in range(n):
        p = ps[i]
        for j in range(i + 1, n):
            q = ps[j]
            if (pow(q, p - 1, p * p) == 1) and (pow(p, q - 1, q * q) == 1):
                pairs.append((p, q))
    print("B=%6d: %d double-Wieferich pair(s) %s  (%.1fs)"
          % (B, len(pairs), pairs[:12], time.time() - t))
