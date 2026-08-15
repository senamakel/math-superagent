"""Relative (minus) class number h^-(Q(zeta_p)) via exact Bernoulli-character product.

Formula (analytic class number formula for the minus part):
    h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (-1/2 * B_{1,chi})
    B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) * a,   chi a primitive odd character.

Values of chi lie in Q(zeta_{p-1}); we compute the product exactly in that
field with exact rational arithmetic (lib.cyclo.Cyclo), then read off the
single rational coefficient — the result must be a positive integer.

Cross-checks (Washington / standard tables of relative class numbers):
    p=3  -> 1
    p=5  -> 1
    p=7  -> 1
    p=11 -> 1
    p=13 -> 1
    p=23 -> 3
    p=31 -> 9
    p=37 -> 37
"""
from fractions import Fraction
from lib.cyclo import Cyclo, zero, zeta_pow


def primitive_root(p):
    from sympy import factorint
    qs = list(factorint(p - 1).keys())
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g


def index_table(p, g):
    """a -> discrete log base g, for a in 1..p-1."""
    logtab = {}
    v = 1
    for e in range(p - 1):
        logtab[v] = e
        v = (v * g) % p
    return logtab


def h_minus(p):
    """Exact relative class number h^-(Q(zeta_p)), p an odd prime."""
    n = p - 1                 # characters live in Q(zeta_n), n even
    g = primitive_root(p)
    logtab = index_table(p, g)
    prod = Cyclo(n, {0: Fraction(1)})
    for k in range(1, p - 1, 2):          # k odd  <=> chi_k odd
        s = zero(n)
        for a in range(1, p):
            e = logtab[a]
            s = s + zeta_pow(n, k * e) * Fraction(a)
        B1 = s * Fraction(1, p)
        prod = prod * (Cyclo(n, {0: Fraction(-1, 2)}) * B1)
    h = prod * Fraction(2 * p)            # multiply by the integer 2p
    # result must be a rational (in fact integer); pull out constant coefficient
    return h
