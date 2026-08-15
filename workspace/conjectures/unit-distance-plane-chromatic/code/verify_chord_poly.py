"""Verify the chord/edge-condition polynomial claimed in
research/approaches/unit-circle-projective-parametrization.md.

p(t) = ((1-t^2)/(1+t^2), 2t/(1+t^2)) parametrises the unit circle.
Two unit-direction points p(t1), p(t2) differ by a unit vector iff
|p(t1)-p(t2)|^2 = 1, i.e. p(t1).p(t2) = 1/2.

The approach file claims the edge condition clears to
    t1^2 t2^2 - 3 t1^2 - 3 t2^2 + 8 t1 t2 + 1 = 0
and checks t1=0, t2=1/sqrt(3) (60 deg) satisfy it, t1=t2 never.

Exact rational/symbolic check.
"""
import sympy as sp

t1, t2 = sp.symbols('t1 t2', real=True)
def p(t):
    return sp.Matrix([(1-t**2)/(1+t**2), 2*t/(1+t**2)])

v = p(t1) - p(t2)
sq = sp.simplify((v.T * v)[0, 0])  # |p(t1)-p(t2)|^2

print("|p(t1)-p(t2)|^2 =", sp.factor(sq))

# Edge condition: sq == 1  <=>  sq - 1 == 0
edge = sp.factor(sp.together(sq - 1))
print("sq-1 =", edge)

# The approach's cleared polynomial (I'll trust only what sympy says):
claimed = t1**2*t2**2 - 3*t1**2 - 3*t2**2 + 8*t1*t2 + 1

# check: numerator of (sq-1) proportional to claimed?
num, den = sp.fraction(sp.together(sq - 1))
print("numerator =", sp.factor(num))
print("claimed   =", sp.expand(claimed))
print("num / claimed =", sp.simplify(sp.factor(num)/sp.expand(claimed)))

# Cross-check the claimed roots: t1=0, t2=1/sqrt3  => 60 deg edge
print("claimed(0, 1/sqrt3) =", sp.simplify(claimed.subs({t1:0, t2:1/sp.sqrt(3)})))
print("claimed(t1=t2)       =", sp.factor(claimed.subs(t2, t1)))
print("|p(0)-p(1/sqrt3)|^2  =", sp.simplify(sq.subs({t1:0, t2:1/sp.sqrt(3)})))

# t = 1/sqrt(11) -> cos=5/6, sin=sqrt(11)/6 (Moser rotation)
t = sp.symbols('t')
print("t=1/sqrt11: x =", sp.simplify((1-t**2)/(1+t**2).subs(t,1/sp.sqrt(11))),
      " y =", sp.simplify((2*t/(1+t**2)).subs(t,1/sp.sqrt(11))))
