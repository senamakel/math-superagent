#!/usr/bin/env python3
"""Compute deg_Q(cos(2alpha)) numerically to very high precision and find the
minimal polynomial via exact rational reconstruction (PSLQ-style), for n=3..16.

cos(2a) = cos(K*th)*inner - sin(K*th)*sqrt(1-inner^2)
We evaluate to 400 digits and ask sympy minimal_polynomial on the numeric
algebraic by providing the cyclotomic field info through high precision.

If reconstructing the exact minpoly is hard for high degree, we only
report the degree of V(n)^2 + the quadratic flag, already established.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 400

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k*th) - (k+n)*t*mp.cos(k*th) < 0:
            K = k
    return K

def cos2a_val(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2*mp.sin(K*th)/((K+n)*t) - mp.cos(K*th)
    cosKa = mp.cos(K*th)
    sinKa = mp.sin(K*th)
    sq = mp.sqrt(1 - inner**2)
    return cosKa*inner - sinKa*sq

for n in range(3, 17):
    v = cos2a_val(n)
    s = mp.nstr(v, 200)
    # try sympy minimal polynomial on high precision numeric
    try:
        x = sp.symbols('x')
        f = sp.nsimplify(sp.MPZ if False else sp.Float(s, 200))
        # minimal_polynomial works on algebraic numeric via nsimplify
        trial = sp.nsimplify(sp.Float(s, 200), [sp.cos(sp.pi/n)], rational=False)
        mpoly = sp.minimal_polynomial(trial, x)
        deg = sp.degree(mpoly)
        print(f"n={n}: deg={deg}  quad={deg<=2}  minpoly={mpoly}")
    except Exception as e:
        print(f"n={n}: minpoly not reconstructed ({type(e).__name__}); cos2a={mp.nstr(v,12)}")
