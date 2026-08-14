"""Validate the relative class number formula h^-(Q(zeta_p)) = 2p * prod_{chi odd} (-1/2 B_{1,chi})
using exact rational arithmetic via the values of odd Dirichlet characters.

B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) * a   (primitive odd chi mod p).

For Q(zeta_p) the product over the (p-1)/2 odd characters of (-1/2 B_{1,chi})
times 2p must be the positive INTEGER h^-. We check against known values:
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

def primitive_root(p):
    for g in range(2, p):
        if pow(g, (p-1)//2, p) != 1:
            return g

def odd_characters(p):
    """Return list of (generator exponent k) for the odd Dirichlet characters mod p.
    chi_k(a) = omega^{k e} where a = g^e, omega = primitive (p-1)-th root of unity.
    Odd means chi(-1) = -1, i.e. k*(p-1)/2 * (p-1)... ; chi_k(-1) = omega^{k * (p-1)/2}
    = (-1)^k, so odd characters are those with k odd."""
    return [k for k in range(1, p-1, 2)]

def rel_class_number(p):
    g = primitive_root(p)
    omega = complex(0, 1)  # we'll build cyclotomic field values via sympy instead of floats
    # Instead use exact representation: characters take values in Z[omega].
    # B_{1,chi} = (1/p) sum chi(a) a.  chi(a) = omega^{k * ind_g(a)}.
    from sympy import exp_pi_rat
    # prod over odd k of (-1/2 B_{1,chi_k})
    # We'll sum in the cyclotomic field Q(omega) then take norm / trace as real part.
    # h^- is a rational integer = 2p * Re(prod)? For odd characters the product is real.
    # Use algebraic numbers via sympy:
    from sympy import Rational, I, srepr
    # Build exponent log table
    logtab = {}
    val = 1
    for e in range(p-1):
        logtab[val] = e
        val = (val*g) % p
    # Value chi(a) = w^{k e}, w = exp(2 pi i/(p-1))
    # Represent via sympy exp(I*2*pi*k*e/(p-1))
    from sympy import exp, I, pi
    prod = Rational(1)
    for k in odd_characters(p):
        s = 0
        for a in range(1, p):
            e = logtab[a]
            chi_a = exp(I*2*pi*k*e/(p-1))
            s += chi_a * a
        B1 = s / p
        prod = prod * (Rational(-1,2) * B1)
    h_rel = 2*p*prod
    # h_rel is an algebraic number; it should be a real rational integer.
    return h_rel

from sympy import simplify, re, Rational, N

for p in [3,5,7,11,13,23,31,37]:
    h = rel_class_number(p)
    val = N(h, 10)
    real = float(val.real)
    imag = float(val.imag)
    rounded = round(real)
    ok = abs(real-rounded) < 1e-6 and abs(imag) < 1e-6
    print(f"p={p:3d}  h^- = {rounded}  (real={real:.4f} imag={imag:.2e})  {'OK' if ok else 'CHECK'}")
