"""Test whether the double-Wieferich prime 83 (part of the only pair (83,4871)
below 10^4) is an irregular prime, i.e. whether p | h^-(Q(zeta_p)). This links
the two data structures: the double-Wieferich condition (the conditional-theorem
hypothesis) and the irregular primes (the p-part of the minus class group, the
descent obstruction). Exact Fraction arithmetic via lib.cyclo."""
from fractions import Fraction
from lib.cyclo import Cyclo, zero, zeta_pow
import time


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
    for k in range(1, p - 1, 2):
        s = zero(n)
        for a in range(1, p):
            e = logtab[a]
            s = s + zeta_pow(n, k * e) * Fraction(a)
        B1 = s * Fraction(1, p)
        prod = prod * (Cyclo(n, {0: Fraction(-1, 2)}) * B1)
    h = prod * Fraction(2 * p)
    return int(h.as_fraction())


from sympy import factorint, primerange

# double-Wieferich primes of the only pair below 10^4
p, q = 83, 4871
t = time.time()
h83 = h_minus(83)
print("h^-(83) =", h83)
print("83 | h^-(83)?", h83 % 83 == 0)
print("factorization of h^-(83):", factorint(h83))
print("v_83(h^-) =", (lambda n, p_: max(c for c in range(50) if n % p_**c == 0))
      if h83 % 83 == 0 else 0, "(%.1fs)" % (time.time() - t))

# report structure: does the OTHER double-Wieferich prime q=4871 enter h^-(83)?
print("4871 | h^-(83)?", h83 % 4871 == 0)

# general: irregular primes up to 83, and v_p(h^-) for each
print("\nIrregular primes (p | h^-(p)) and v_p(h^-):")
for pr in primerange(3, 84):
    h = h_minus(pr) if pr not in (83,) else h83
    if h % pr == 0:
        print("  p=%3d  v=%d" % (pr, sum(1 for _ in iter(lambda: None, None) if False) or (lambda n: max(c for c in range(20) if n % pr**c == 0))(h)))
