#!/usr/bin/env python3
"""Independent numerical check that V(5)^2 is NOT a quadratic surd a+b*sqrt(c)
(for integer/squarefree c). If it were, then (V(5)^2 - a)^2 / b^2 = c would be
a small integer, i.e. there'd exist integers a,b with the satisfy exact near-integer.
We test a,b over a wide range and show no integrality occurs; also confirm the
hexagon V(6)^2 DOES satisfy it (sanity control)."""
import mpmath as mp
mp.mp.dps = 80

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

def is_quadratic_surd(x, Amax=2000, Bmax=2000):
    # check if x = a + b*sqrt(D) with small integer a,b (squarefree D)
    # => there exist integers a,b with D = ((x-a)/b)^2 a positive integer near-square
    best = None
    for a in range(-Amax, Amax+1):
        for b in range(1, Bmax+1):
            d = ((x - a)/b)**2
            dd = int(mp.nint(d))
            if dd >= 0 and abs(d - dd) < mp.mpf('1e-30'):
                # check squarefree-ish (not needed; present it)
                return (a, b, dd, mp.nstr(dd))
    return None

for n in [3,4,5,6,7]:
    v2 = V2(n)
    r = is_quadratic_surd(v2)
    if r:
        a,b,dd,_ = r
        print(f"V({n})^2 = {mp.nstr(v2,20)}  IS quadratic: a={a} b={b} D={dd}")
    else:
        print(f"V({n})^2 = {mp.nstr(v2,20)}  NOT quadratic (no small a,b in tested range)")
