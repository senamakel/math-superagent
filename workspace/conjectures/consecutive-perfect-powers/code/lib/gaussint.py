#!/usr/bin/env python3
"""Exact Gaussian-integer arithmetic on pairs (re, im) of Python ints.

Z[i] = { a + b*i : a, b in Z }. Every function here uses exact integer
arithmetic only (no floats, no sympy, no math.pow). Built for the Lebesgue
theorem proof (x^p - y^2 = 1 has no solution, p odd prime); the module is
general enough to reuse: norm, conjugation, exact multiplication/factorisation
by the Euclidean algorithm, gcd (unit-exact), division with remainder.

A Gaussian integer is represented as a tuple (re, im). None of these helpers
reads globals or files; each is callable from any working directory once
code/ is on PYTHONPATH:

    from lib.gaussint import G, gmul, gnorm, gconj, gdivmod, ggcd, gis_unit
"""
import math


def G(re, im=0):
    """Normalise a Gaussian integer (re, im) to canonical (re, im) form."""
    return (re, im)


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    """(a0+a1 i)(b0+b1 i) = (a0b0 - a1b1) + (a0b1 + a1b0) i, exactly."""
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def gnorm(a):
    """N(a0+a1 i) = a0^2 + a1^2, a non-negative exact integer."""
    return a[0] * a[0] + a[1] * a[1]


def gconj(a):
    return (a[0], -a[1])


def gsmul(k, a):
    """Scalar multiplication by an integer k."""
    return (k * a[0], k * a[1])


def gpow(a, n):
    """Exact integer n-th power of a Gaussian integer by square-and-multiply.

    Exact throughout; used with n = p (an odd prime) but valid for any n >= 0.
    """
    if n < 0:
        raise ValueError("gpow with negative exponent")
    if n == 0:
        return (1, 0)
    result = (1, 0)
    base = a
    e = n
    while e:
        if e & 1:
            result = gmul(result, base)
        base = gmul(base, base)
        e >>= 1
    return result


def _nearest_int(r):
    """Nearest integer to a rational r == n/d (exact; round half away from 0).

    Only the 'closest' property matters for the Euclidean division bound; any
    valid nearest choice terminates. Implemented with exact integer arithmetic.
    """
    q, rem = divmod(r)
    # tie-break half away from zero
    if 2 * abs(rem) >= r._denominator:   # rem positive by divmod of positive d
        q = q + (1 if r >= 0 else -1)
    return q


def gdivmod(a, b):
    """Euclidean division a = q*b + r in Z[i], with N(r) < N(b) if b != 0.

    q = round(a * conj(b) / N(b)) componentwise (nearest integer); the
    remainder then satisfies N(r) <= N(b)/2 < N(b) (standard nearest-neighbour
    argument for Z[i], which is Euclidean with respect to the norm).
    """
    if b == (0, 0):
        raise ZeroDivisionError("gdivmod by zero")
    nb = gnorm(b)
    numer = gmul(a, gconj(b))          # (a * conj b) -- Gaussian integer
    # q_re, q_im = round(numer/nb)
    from fractions import Fraction
    qre = Fraction(numer[0], nb)
    qim = Fraction(numer[1], nb)
    q = (round(qre), round(qim))
    r = gsub(a, gmul(q, b))
    return q, r


def ggcd(a, b):
    """A greatest common divisor of Gaussian integers a, b via Euclid; exact.

    Returns a Gaussian integer g with (g) = (a) + (b) as ideals. Uniqueness is
    only up to unit; the returned representative is not normalised to a
    canonical quadrant.
    """
    a, b = a, b
    while b != (0, 0):
        _, r = gdivmod(a, b)
        a, b = b, r
    return a


def gis_unit(a):
    """True iff a is a unit of Z[i], i.e. norm(a) == 1."""
    return gnorm(a) == 1


def gim(a):
    """Imaginary part."""
    return a[1]


def gre(a):
    """Real part."""
    return a[0]


def binom_re_im(a, n):
    """Real and imaginary parts of (a+bi)^n by the exact binomial theorem.

    (a+bi)^n = sum_{k=0}^{n} C(n,k) a^{n-k} (bi)^k. Real part = sum over even k,
    imaginary part = sum over odd k. Returns (re, im). Exact (math.comb).
    """
    re, im = 0, 0
    for k in range(n + 1):
        term = math.comb(n, k) * (a[0] ** (n - k)) * (a[1] ** k)  # a^(n-k) b^k
        if k % 2 == 0:
            re += term * ((-1) ** (k // 2))
        else:
            im += term * ((-1) ** ((k - 1) // 2))
    return (re, im)


def verify_binom_gpow(a, n):
    """Check binom_re_im(a, n) == gpow(a, n) exactly; returns True/False."""
    return binom_re_im(a, n) == gpow(a, n)
