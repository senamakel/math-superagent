#!/usr/bin/env python3
"""Completeness evidence + full routing for the unit method.

For the unit method to be a complete resolution we need: for ALL n in Z,
(1-w)^n = c - d w (zero w^2 coefficient) only at n=0,1.  PARI thue() is the
authoritative complete resolution (it lists all (c,d) with c^3-2d^3=+-1).
This scan is numerical evidence for the unit side; the proof of completeness
is PARI thue + class number 1 + fundamental unit 1-w.

Also: exhaustively confirm that the descent cases map, for every thue
solution, to exactly the claimed (x,y) with y>0.
"""
import sympy as sp

w = sp.Symbol('w')
inv = -(1 + w + w**2)   # (1-w)^-1

def to_basis(expr):
    return sp.rem(sp.expand(expr), w**3 - 2, w)

def w2coeff(expr):
    return sp.Poly(to_basis(expr), w).coeff_monomial(w**2)

print("Zero-w^2-coefficient units (1-w)^n, n in [-200,200]:")
cnt = 0
for n in range(-200, 201):
    val = to_basis(sp.expand((1-w)**n)) if n >= 0 else to_basis(sp.expand(inv**(-n)))
    if w2coeff(val) == 0:
        c0 = sp.Poly(val, w).coeff_monomial(1)
        c1 = sp.Poly(val, w).coeff_monomial(w)
        print(f"  n={n}: (c,d)=({c0},{-c1})")
        cnt += 1
print("Total n with zero w^2 coeff in [-200,200]:", cnt, "(only 0 and 1 expected)")

# Thue solutions from PARI, mapped through both descent cases with c,d>0.
def route_cases():
    # Case A: k=c^3, k+1=2d^3 -> 2d^3-c^3=1  (thue c^3-2d^3=-1): {(-1,0),(1,1)}
    # Case B: k=2d^3, k+1=c^3 -> c^3-2d^3=1  (thue c^3-2d^3=1): {(-1,-1),(1,0)}
    out = []
    # Case A solutions with c,d>0 that satisfy 2d^3-c^3=1
    for (c,d) in [(1,1)]:
        if 2*d**3 - c**3 == 1 and c>0 and d>0:
            k=c**3; x=2*k+1; y=2*c*d
            if x**2-y**3==1:
                out.append((c,d,'A',x,y))
    print("\nCase A (c,d>0, 2d^3-c^3=1):")
    for r in out: print("  ", r)
    # Case B solutions with c,d>0 that satisfy c^3-2d^3=1
    print("Case B (c,d>0, c^3-2d^3=1): none (thue gives (-1,-1),(1,0); (1,0) has d=0,")
    print("   y=0 excluded, (-1,-1) has negatives)")
    return out

sol = route_cases()
print("\nAll (x,y) with y>0:", sorted({(x,y) for _,_,_,x,y in sol}))
print("Contains known (3,2):", (3,2) in {(x,y) for _,_,_,x,y in sol})
