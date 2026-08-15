"""Compute h^-(Q(zeta_p)) = relative class number for EVERY odd prime p,
consecutively, to see the true integer sequence (not the ld subsequence the
run had computed: 3,5,7,11,13,23,31,37,43 skipped 17,19,29,41)."""
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
    return h.as_fraction()


from sympy import primerange

def primes_upto(limit):
    return list(primerange(3, limit + 1))


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    ps = primes_upto(limit)
    vals = []
    t0 = time.time()
    for p in ps:
        h = h_minus(p)
        vals.append(int(h))
        print("p=%3d  h^-=%d" % (p, int(h)), flush=True)
    dt = time.time() - t0
    print("SEQUENCE over primes <= %d:" % limit)
    print(vals)
    print("primes:", ps)
    print("runtime %.2fs" % dt)
