#!/usr/bin/env python3
"""Fit exact rational function p3(m) = N(m)/D(m) in m=L/40 to exact data.
Try to find small-degree polynomial numerator/denominator via exact solving.
"""
from fractions import Fraction as F
from exact_p3_data import DATA
from sympy import symbols, Eq, solve, Rational, expand

x = symbols('x')
pairs = [(F(L)//40, F(DATA[L])) for L in DATA]
pairs.sort()

print("data (m=L/40, p):")
for m, p in pairs:
    print(f"  m={m:3d}  p={p} = {float(p):.8f}")

# Try p = (a0 + a1 m + a2 m^2)/(b0 + b1 m + b2 m^2)  with best normalization
# Solve using enough points, then check all.
def fit(dn, nn):
    # unknowns a0..a_nn, b0..b_dn with b set scale-free: fix b_dn? use b0=1 alternative.
    # Use variable: p = (A0+...+A_nn x^nn)/(B0+...+B_dn x^dn), fix B_dn=1
    a = symbols(f'a0:{nn+1}')
    b = list(symbols(f'b0:{dn}')) + [1]
    # need nn+1 + dn unknowns; use first nn+1+dn points
    pts = pairs[:nn+1+dn]
    eqs = []
    for (m, p) in pts:
        num = sum(a[i]*m**i for i in range(nn+1))
        den = sum(b[i]*m**i for i in range(dn+1))
        eqs.append(Eq(p*den, num))
    sol = solve(eqs, list(a)+list(b[:dn]), dict=True)
    out = []
    for s in sol:
        A = [s.get(a[i], 0) for i in range(nn+1)]
        B = [s.get(b[i], 0) for i in range(dn)] + [1]
        # check all points
        ok = True
        for (m, p) in pairs:
            num = sum(A[i]*m**i for i in range(nn+1))
            den = sum(B[i]*m**i for i in range(dn+1))
            if den != 0 and F(num)/F(den) != p:
                ok = False
                break
        out.append((ok, A, B))
    return out

for nn in range(0, 5):
    for dn in range(0, 5):
        if nn+1+dn > len(pairs): continue
        if nn == 0 and dn == 0: continue
        try:
            res = fit(dn, nn)
            for (ok, A, B) in res:
                if ok:
                    print(f"\nFIT p3(m)=N/D with deg N={nn} deg D={dn} EXACT on all {len(pairs)} pts:")
                    print("  N:", A)
                    print("  D:", B)
        except Exception as e:
            pass
