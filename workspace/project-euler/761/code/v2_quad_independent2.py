#!/usr/bin/env python3
"""Proper independent numerical check of the V(n)^2 quadratic-surd question.

A number is a quadratic surd / degree-2 algebraic iff its minimal polynomial
over Q has degree <= 2. Sympy's exact computation gave:
  n=3: V2 minpoly x^2 - 56x + 64   (V2 = 28 + 12sqrt5, i.e. 28+sqrt720)
  n=4: V2 minpoly x^2 - 35x + 50
  n=6: V2 minpoly 9x^2 - 240x + 256
  n=5,7,...: NotAlgebraic (higher-degree field).

Independently verify each candidate minpoly by plugging the high-precision float
in, and show V(5)^2 is NOT roots of any integer quadratic x^2+px+q with
|p|,|q| bounded (PSLQ-ish search on V5^2 and V5^4)."""
import mpmath as mp
mp.mp.dps = 90

def V2(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = None
    for k in range(0, n+1):
        if mp.sin(k*th) - (k+n)*t*mp.cos(k*th) < 0:
            K = k
    inner = 2*mp.sin(K*th)/((K+n)*t) - mp.cos(K*th)
    alpha = mp.mpf(1)/2*(K*th + mp.acos(inner))
    return (1/mp.cos(alpha))**2

# n -> (p, q) for minpoly x^2 + p x + q
quads = {3: (-56, 64), 4: (-35, 50), 6: (-240/9, 256/9)}
for n, (p, q) in quads.items():
    v2 = V2(n)
    resid = v2*v2 + p*v2 + q
    print(f"V({n})^2: |x^2 + {p}x + {q}| evaluated = {mp.nstr(resid, 3)}  (should be ~0)")

# V(5)^2: search for integer quadratic x^2 + p x + q vanishing at V5^2
v5 = V2(5)
v5s = v5*v5
found = None
for p in range(-2000, 2001):
    # q = -(v5^4 + p v5^2) must be near-integer
    qf = -(v5s + p*v5)
    qq = int(mp.nint(qf))
    if abs(qf - qq) < mp.mpf('1e-60'):
        found = (p, qq)
        break
print(f"V(5)^2: integer quadratic with |p|<=2000, |q|<=? -> {found if found else 'NONE (consistent with non-quadratic)'}")
print("V(5)^2 =", mp.nstr(v5, 20))
