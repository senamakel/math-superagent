#!/usr/bin/env python3
"""Derive, with exact sympy algebra, the closed form for V_hexagon.

stewbasic formula for n=6:  K=2, theta=pi/6,
    alpha = 1/2*( K*theta + acos( 2*sin(K*theta)/((K+n)*tan(theta)) - cos(K*theta) ) )
         = 1/2*( pi/3   + acos( 2*sin(pi/3)/(8*tan(pi/6)) - cos(pi/3) ) )
    V = 1/cos(alpha)

We evaluate this symbolically (exact radicals) and reduce the surd.
"""
import sympy as sp

# Exact ingredients
sin_pi3 = sp.sqrt(3)/2
cos_pi3 = sp.Rational(1, 2)
tan_pi6 = sp.sqrt(3)/3
K, n = 2, 6

# inner argument of acos
inner = 2*sin_pi3/((K+n)*tan_pi6) - cos_pi3
inner = sp.simplify(inner)
print("inner (acos argument) =", sp.simplify(inner), "=", sp.nsimplify(sp.N(inner)))

# alpha = 1/2*( pi/3 + acos(inner) )
# cos(2*alpha) = cos(pi/3 + acos(inner))
c2a = sp.cos(sp.pi/3)*inner - sp.sin(sp.pi/3)*sp.sqrt(1 - inner**2)
c2a = sp.simplify(c2a)
print("cos(2*alpha) =", c2a, "=", sp.N(c2a))

# V = 1/cos(alpha);  cos(alpha)^2 = (1+cos(2alpha))/2
cos2 = (1 + c2a)/2
V2 = 1/cos2                      # V^2
V_exact = sp.sqrt(V2)
print("V^2 =", sp.simplify(V2))
print("V   =", sp.powsimp(sp.nsimplify(V_exact), force=True))
print("V   numeric =", sp.N(V_exact, 30))

# canonical radical form
print("canonical (sqrt of (40+8*sqrt21)/3):")
print("  predicted closed form =", sp.sqrt((40 + 8*sp.sqrt(21))/3))
print("  equals V_exact? ->", sp.simplify(sp.sqrt((40+8*sp.sqrt(21))/3) - V_exact) == 0)

# Compare to numeric answer cited by the run (5.0550504633038933)
from decimal import Decimal, getcontext
getcontext().prec = 30
num = sp.N(V_exact, 25)
print("\nHexagon closed form to 25 dp:", num)
print("Rounded 8 dp:", f"{float(num):.8f}")
