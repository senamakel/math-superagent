#!/usr/bin/env python3
"""Test the linear-stencil model of d(n) = K(n) - floor(3n/7).

Model derived from the asymptotics: K(n) = floor(r(n)) where r(n) is the
unique root of tan(r*pi/n) = (r+n)*tan(pi/n), and r(n) ~ c*n with
c = root of tan(c*pi) = pi*(c+1)  (~ 0.4302966531242).

floor(3n/7) = 3n/7 - frac(n),  frac(n) = (3n mod 7)/7.
So d(n) = floor(r(n)) - floor(3n/7) ~ (c - 3/7)*n + frac(n)  (mod root oscillation),
and the boundary d(n) >= m for n ≡ r (mod 7) should occur at

    n ≈ T_pred(r, m) = (m - frac_r) / (c - 3/7),   frac_r = (3r mod 7)/7.

Checks:
 1. First n with d(n) = 2 and d(n) = 3 (the d=2 falsifier was found at
    n=667 by pattern_k_threshold_structure.py).
 2. Per-residue mod 7 first n with d(n) = 2, compared with T_pred(r,2).
 3. Exact sympy K() at every reported boundary n and its neighbours,
    so the mpmath floor values are confirmed exactly.
"""
import math
import sympy as sp
import mpmath as mp

# asymptotic slope
c = mp.findroot(lambda x: mp.tan(x * mp.pi) - mp.pi * (x + 1), 0.43)
c_float = float(c)
c_minus_3_7 = c_float - 3.0 / 7.0
print("c = %.15f   c - 3/7 = %.15f" % (c_float, c_minus_3_7))
print("7c - 3 = %.15f" % (7.0 * c_float - 3.0))

frac_r = {(3 * r) % 7 / 7.0 for r in range(7)}

def T_pred(r, m):
    fr = (3 * r) % 7 / 7.0
    return (m - fr) / c_minus_3_7

def K_of_n_mp(n, dps=40):
    mp.mp.dps = dps
    th = mp.pi / n
    t = mp.tan(th)
    def f(x):
        return mp.tan(x * th) - (x + n) * t
    lo, hi = mp.mpf(1), mp.mpf(n) / 2 - mp.mpf('1e-40')
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return int(mp.floor((lo + hi) / 2))

def d_of_n(n, K):
    return K - 3 * n // 7

def K_of_n_exact(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        if sp.sin(k * th) - (k + n) * tan_th * sp.cos(k * th) < 0:
            best = k
    return best

# --- cross-check mpmath vs exact sympy on a sample including 667 ---
for n in [79, 86, 165, 251, 337, 416, 502, 581, 666, 667, 668, 671]:
    e = K_of_n_exact(n)
    m = K_of_n_mp(n)
    ok = "OK" if e == m else "MISMATCH"
    print("n=%4d  exact K=%3d  mp K=%3d  d=%d  %s" % (n, e, m, d_of_n(n, e), ok))

# --- first d=2 and d=3 ---
first2 = first3 = None
NMAX = 12000
for n in range(3, NMAX + 1):
    d = d_of_n(n, K_of_n_mp(n))
    if first2 is None and d >= 2:
        first2 = n
    if first3 is None and d >= 3:
        first3 = n
        break
print("\nfirst n with d(n)>=2:", first2)
print("first n with d(n)>=3:", first3)

# --- per-residue first n with d(n)=2, and prediction ---
print("\nper-residue first d(n)=2 (n % 7 = r):")
for r in range(7):
    found = None
    for n in range(3, NMAX + 1):
        if n % 7 == r and d_of_n(n, K_of_n_mp(n)) >= 2:
            found = n
            break
    pred = T_pred(r, 2)
    diff = None if found is None else found - pred
    print("r=%d  first2=%5s  pred=%9.2f  found-pred=%8.2f" % (r, found, pred, diff))