"""Irregularity of the small double-Wieferich primes via Kummer's criterion:
p is irregular iff p | h^-(Q(zeta_p)) iff p divides the numerator of the
reduced Bernoulli number B_(2k) for some even 2k with 2 <= 2k <= p-3.
v_p(h^-) = number of such k (the 'index of irregularity'). Exact integer
arithmetic on Bernoulli numerators (sympy.bernoulli, exact rationals)."""
from sympy import bernoulli, Rational
from fractions import Fraction

def bernoulli_num(n):
    """Numerator of Bernoulli number B_n as reduced fraction."""
    b = bernoulli(n)
    return b.p  # numerator

def irregularity(p, bound=None):
    """Return list of even k (2<=2k<=p-3) with p | numerator(B_2k), computing
    B_2k as exact reduced fraction and testing numerator divisibility."""
    if bound is None:
        bound = p - 3
    hits = []
    for k in range(2, bound + 2, 2):  # k even, 2<=k<=p-3
        num = bernoulli_num(k)
        if num % p == 0:
            hits.append(k)
    return hits

primes = [83, 2903, 4871, 18787]
for p in primes:
    hits = irregularity(p)
    print("p=%5d  irregular %s  index_of_irregularity(v_p(h^-))=%d  bad_k=%s among 2..%d"
          % (p, bool(hits), len(hits), hits, p-3))

# sanity check on known irregular primes: 37, 59, 67, 101
for p in [37, 59, 67, 101]:
    hits = irregularity(p)
    print("sanity p=%d bad_k=%s" % (p, hits))
