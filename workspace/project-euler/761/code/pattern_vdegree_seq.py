#!/usr/bin/env python3
"""Compute deg_Q(V(n)^2) = deg_Q(cos 2alpha) for n=3..N.

V(n)=1/cos(alpha), alpha = (K*theta + acos(inner))/2.
cos(2alpha) = cos(K*theta+acos(inner))
            = cos(K*theta)*inner - sin(K*theta)*sqrt(1-inner^2)
inner = 2 sin(K theta)/((K+n)t) - cos(K theta), theta=pi/n, t=tan(theta).

cos(2alpha) and the sqrt term live in the real cyclotomic field
Q(zeta_2n)^+ (real subfield). Compute its exact minimal polynomial by
working over Q with z = exp(i pi/n): express sin/cos of multiples of
pi/n in terms of z, build cos(2alpha) as an algebraic element, then take
minimal_polynomial.
"""
import sympy as sp


def v2_degree(n):
    th = sp.pi / n
    t = sp.tan(th)
    # K = largest int with sin(K th) - (K+n) t cos(K th) < 0
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    inner = 2 * sp.sin(K * th) / ((K + n) * t) - sp.cos(K * th)
    inner = sp.simplify(inner)

    # Work in Q(z), z = exp(I*pi/n). Represent cos, sin algebraically.
    z = sp.symbols('z')
    def trig(k):
        # cos(k*pi/n) = (z^k + z^-k)/2, sin(k*pi/n) = (z^k - z^-k)/(2 I)
        # avoid I by noting z^k = exp(I*k*pi/n); use cosh/sinh in z? Handle via
        # substituting with explicit real expression instead.
        return None
    # Simpler: build cos(2alpha) as a symbolic expression and let sympy
    # find its minpoly over Q by rewriting trig of rational*pi via exp.
    # cos(2a) = cos(K th) cos(ac) - sin(K th) sin(ac), where ac=acos(inner)
    #         = cos(K th)*inner - sin(K th)*sqrt(1-inner^2)
    cosKa = sp.cos(K * th)
    sinKa = sp.sin(K * th)
    sq = sp.sqrt(1 - inner**2)
    cos2a = cosKa * inner - sinKa * sq
    cos2a = sp.simplify(cos2a)

    # Now reduce trig(pi/n) multiples to algebraic via exp_polar-free real
    # substitution: use SymPy's ability to get the minpoly of a real
    # algebraic constructed from cos(pi/n) (which sympy handles).
    # Build the element over Q(cos(pi/n))? Simpler robust route:
    # numerically evaluate to high precision then find minpoly via PSLQ.
    import mpmath as mp
    mp.mp.dps = 300
    val = complex(sp.N(cos2a, 200))
    # try minimal_polynomial of the exact expr first
    try:
        x = sp.symbols('x')
        mpoly = sp.minimal_polynomial(cos2a, x, compose=False)
        return sp.degree(mpoly), 'exact'
    except Exception as e:
        # fall back on sympy's composition-free numerical minpoly
        try:
            approx = sp.N(cos2a, 120)
            m = sp.minpoly(sp.nsimplify(approx, [sp.sqrt(2), sp.sqrt(3)],
                                        rational=False))
            return sp.degree(m), 'nsimplify'
        except Exception as e2:
            return None, str(type(e2).__name__)


for n in range(3, 17):
    d, how = v2_degree(n)
    print(f"n={n}: deg_Q(V^2)=V^2deg={d}   ({how})")
