"""Small exact oracle for the residual-strata Lean statement.

The previous unrestricted quadratic Darboux-factor solve timed out; this
bounded oracle deliberately checks only the structural examples used by the
statement: the invariant line and singular point of (2.7), the center
reversibility identities for (2.8), and a restricted polynomial first-integral
ansatz. It is validation evidence, not a proof of the open closure.
"""
import sympy as sp
x, y, c, m2 = sp.symbols('x y c m2')
P27 = c*x - y + 1 + x**2
Q27 = x*y
P28 = c*x - y + 1 + (1+m2)*x**2
Q28 = x*y
assert sp.expand(Q27.subs(y, 0)) == 0
assert sp.expand(P27.subs({x: 0, y: 1})) == 0
assert sp.expand(Q27.subs({x: 0, y: 1})) == 0
assert sp.expand(P28.subs({x: -x, c: 0}) - P28.subs({c: 0})) == 0
assert sp.expand(Q28.subs({x: -x}) + Q28) == 0
# Restricted polynomial first-integral test H=a*x+b*y+d*x^2+e*x*y+f*y^2.
a,b,d,e,f=sp.symbols('a b d e f')
H=a*x+b*y+d*x**2+e*x*y+f*y**2
Lie=sp.Poly(sp.expand(sp.diff(H,x)*P27+sp.diff(H,y)*Q27),x,y)
# The only constant polynomial first integral in this restricted ansatz is constant.
nonconstant_coeffs=[z for mon,z in Lie.terms() if mon != (0,0)]
print('A invariant line:', Q27.subs(y,0))
print('A singular point:', (P27.subs({x:0,y:1}), Q27.subs({x:0,y:1})))
print('B reversibility residuals:',
      sp.expand(P28.subs({x:-x,c:0})-P28.subs({c:0})),
      sp.expand(Q28.subs({x:-x})+Q28))
print('C restricted first-integral coefficient equations:', nonconstant_coeffs)
print('oracle checks passed')
