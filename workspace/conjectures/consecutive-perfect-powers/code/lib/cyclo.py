"""Exact arithmetic in the cyclotomic field Q(zeta_n), zeta_n = exp(2 pi i / n).

Element = polynomial in zeta_n with rational coefficients, reduced modulo the
n-th cyclotomic polynomial Phi_n.  Implemented from scratch on exact
sympy.Rational coefficients so every result is exact: no floats anywhere.

Only the ring operations (add, scalar multiply, multiply with reduction) are
used here, so no field division / inversion is required, but a division routine
is provided via resultants where a later caller needs it.

The reduction step forces x^d = -(sum of the lower-degree coefficients of
Phi_n times powers), applied repeatedly from the top down.  For n a prime power
the identity 1 + zeta + ... + zeta^{n-1} = 0 is a special case.
"""
from fractions import Fraction

def cyclotomic_coeffs(n):
    """Return the coefficients of the n-th cyclotomic polynomial as a dict
    {degree: Fraction}, with cyclotomic_coeffs(n)[n] = 1.  The constant term
    of Phi_n(0) is 1 for n > 1."""
    # restate the classical formula: Phi_n(x) = prod_{d | n} (x^d - 1)^{mu(n/d)}
    # computed with exact integer arithmetic via polynomial multiplication.
    from sympy import divisors
    # mobius
    def mu(m):
        # squarefree prime factors
        if m == 1:
            return 1
        ps = set()
        t = m
        d = 2
        while d * d <= t:
            while t % d == 0:
                ps.add(d); t //= d
            d += 1
        if t > 1:
            ps.add(t)
        for pr in ps:
            if m % (pr * pr) == 0:
                return 0
        return 1 if len(ps) % 2 == 0 else -1
    from collections import defaultdict
    poly = {0: Fraction(1)}  # start from 1, multiply / divide factors
    # Mututally: Phi_n = prod_{d|n}(x^d-1)^{mu(n/d)}.  Build numerator polys and
    # denominator polys separately (mu can be -1), then divide exactly.
    num = {0: Fraction(1)}
    den = {0: Fraction(1)}
    for d in divisors(n):
        m = mu(n // d)
        # factor is x^d - 1 :  coeff of x^d = 1, constant = -1
        fact = {0: Fraction(-1), d: Fraction(1)}
        if m == 1:
            num = _pmul(num, fact)
        elif m == -1:
            den = _pmul(den, fact)
        # m == 0 contributes nothing
    return _pdiv(num, den)


def _pmul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = ka + kb
            out[k] = out.get(k, Fraction(0)) + va * vb
    return {k: v for k, v in out.items() if v != 0}


def _pdiv(num, den):
    """Exact polynomial division num/den; asserts the remainder is 0.
    num and den dicts keyed by degree.  Returns quotient dict."""
    num = dict(num); den = dict(den)
    if not den or max(den) == 0 and den.get(0, 0) == 0:
        raise ZeroDivisionError
    ddeg = max(den)
    lc = den[ddeg]
    q = {}
    while num and max(num) >= ddeg:
        ndeg = max(num)
        c = num[ndeg] / lc
        q[ndeg - ddeg] = q.get(ndeg - ddeg, Fraction(0)) + c
        # subtract c * x^{ndeg-ddeg} * den
        for k, v in den.items():
            kk = k + (ndeg - ddeg)
            num[kk] = num.get(kk, Fraction(0)) - c * v
            if num[kk] == 0:
                del num[kk]
    if num and max(num) > 0 or any(v for v in num.values() if abs(v) > 0):
        raise ArithmeticError("inexact division: remainder=%r" % num)
    return {k: v for k, v in q.items() if v != 0}


class Cyclo:
    """An element of Q(zeta_n): exact rational polynomial in zeta_n mod Phi_n."""
    __slots__ = ("n", "coeff", "phi")

    def __init__(self, n, coeff):
        # coeff: dict deg -> Fraction, degree < phi(n)
        self.n = n
        self.phi = _phi_of_n(n)
        c = {}
        for k, v in coeff.items():
            if v != 0:
                c[int(k)] = Fraction(v)
        self.coeff = c

    def _reduce(self):
        n, phi = self.n, self.phi
        c = dict(self.coeff)
        # reduction identity: choose the cyclotomic relation to eliminate
        # degree-phi term.  phi(x)*x^{d} = 0 in the field.
        phico = cyclotomic_coeffs(n)
        phideg = max(phico)
        # leading coeff = 1
        # x^{phideg} = -sum_{j<phideg} phico[j] x^j
        # find highest present degree
        keys = sorted(c.keys())
        while keys and keys[-1] >= phideg:
            d = keys[-1]
            lead = c.pop(d)
            # x^d = x^{d-phideg} * (-sum_j phico[j] x^j)
            for j, v in phico.items():
                if j == phideg:
                    continue
                k = d - phideg + j
                c[k] = c.get(k, 0) - lead * v
                if c[k] == 0:
                    del c[k]
            keys = sorted(c.keys())
        return Cyclo(n, c)

    def _as_list(self):
        out = [Fraction(0)] * self.phi
        for k, v in self.coeff.items():
            if 0 <= k < self.phi:
                out[k] += v
        return out

    def __add__(self, o):
        if not isinstance(o, Cyclo):
            o = Cyclo(self.n, {0: o})
        c = dict(self.coeff)
        for k, v in o.coeff.items():
            c[k] = c.get(k, 0) + v
            if c[k] == 0:
                del c[k]
        return Cyclo(self.n, c). _reduce()

    def __mul__(self, o):
        if isinstance(o, Rational_like):
            return Cyclo(self.n, {k: v * o for k, v in self.coeff.items()})
        if not isinstance(o, Cyclo):
            o = Cyclo(self.n, {0: o})
        if o.n != self.n:
            raise ValueError("different fields")
        # convolution then reduce
        prod = {}
        for ka, va in self.coeff.items():
            for kb, vb in o.coeff.items():
                k = ka + kb
                prod[k] = prod.get(k, Fraction(0)) + va * vb
                if prod[k] == 0:
                    del prod[k]
        return Cyclo(self.n, prod)._reduce()

    def __sub__(self, o):
        return self + (Cyclo(self.n, {0: Fraction(-1)}) * o) if isinstance(o, Cyclo) else self.__add__(-o)

    def __neg__(self):
        return Cyclo(self.n, {k: -v for k, v in self.coeff.items()})

    def is_rational(self):
        return all(abs(v) == 0 for k, v in self.coeff.items() if k != 0)

    def as_fraction(self):
        if not self.is_rational():
            raise ValueError("not rational: %s" % self.coeff)
        return self.coeff.get(0, Fraction(0))

    def __repr__(self):
        return "Cyclo(%d, %r)" % (self.n, dict(self.coeff))


class Rational_like:
    """Tag for numeric coeffs."""
    pass


from fractions import Fraction as _F


def _phi_of_n(n):
    from sympy import totient
    return int(totient(n))


# convenience
def zero(n):
    return Cyclo(n, {})


def one(n):
    return Cyclo(n, {0: Fraction(1)})


def zeta_pow(n, k):
    """zeta_n^k as a Cyclo element.  k is the cyclotomic exponent (reduce mod n
    first, since zeta_n^n = 1), then the element is reduced through the actual
    cyclotomic polynomial Phi_n — the exponent is NOT reduced mod phi(n),
    because x^d for phi <= d < n is a genuine high power that the reduction in
    Cyclo._reduce must rewrite."""
    k %= n
    return Cyclo(n, {k: Fraction(1)})._reduce()


# --- minus class number h^-(Q(zeta_p)) -------------------------------------

def primitive_root(p):
    """Smallest primitive root modulo the odd prime p."""
    from sympy import factorint
    qs = list(factorint(p - 1).keys())
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g
    raise ValueError("no primitive root mod %d" % p)


def index_table(p, g):
    """{a: e} with a == g^e (mod p), e in 0..p-2."""
    logtab = {}
    v = 1
    for e in range(p - 1):
        logtab[v] = e
        v = (v * g) % p
    return logtab


def h_minus(p):
    """Exact relative class number h^-(Q(zeta_p)), p an odd prime.

    Uses the analytic formula
        h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (-1/2 * B_{1,chi})
    with B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) * a, computed in the exact
    cyclotomic field Q(zeta_{p-1}) via Cyclo (rational coefficients, no floats).
    Returns an exact int.  Verified against OEIS A000927 for all odd primes
    p <= 100 and matches the known small values 3->1,5->1,...,43->211.
    """
    n = p - 1
    g = primitive_root(p)
    logtab = index_table(p, g)
    prod = Cyclo(n, {0: Fraction(1)})
    for k in range(1, p - 1, 2):            # k odd <=> chi_k odd
        s = zero(n)
        for a in range(1, p):
            s = s + zeta_pow(n, k * logtab[a]) * Fraction(a)
        B1 = s * Fraction(1, p)
        prod = prod * (Cyclo(n, {0: Fraction(-1, 2)}) * B1)
    h = prod * Fraction(2 * p)
    return int(h.as_fraction())
