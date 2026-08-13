"""Check the geometry of the phi-triple "fibre curve" for candidate
phi-triple-curve-genus-faltings.

f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 , homogeneous of degree 0 in (m,n).
So f(tm,tn) = f(m,n): level set f = C is a union of rays/lines through origin.

Claim being tested: fixing q1 and the ratio r (hence q2 fixed), the fibre
q1 + q2 = f(p,q) is a CURVE whose genus is the deciding quantity (>=2 ->
Faltings).  We show instead that f(p,q)=C is a union of lines through (0,0)
(genus 0 fibres) because f only depends on the ratio p/q.
"""
import sympy as sp

m, n = sp.symbols('m n')
f = 4*m*n*(m**2 - n**2)/(m**2 + n**2)**2

# 1. homogeneous of degree 0: f(t m, t n) == f(m,n)
t = sp.symbols('t')
print("f(tm,tn) == f(m,n) :",
      sp.simplify(f.subs({m: t*m, n: t*n}) - f) == 0)

# 2. depends only on ratio r = n/m : write r = n/m, verify f = g(r) single var
r = sp.symbols('r')
g = sp.simplify(f.subs(n, r*m))
print("f(m, r m) =", sp.simplify(g))
g = sp.simplify(g)
# g(r) should have no m left
print("independent of m:", sp.diff(g, m) == 0)

# 3. The equation f(p,q) = C.  With q = r p, f = g(r).  So f(p,q)=C  <=>
#    g(r)=C, i.e. r is one of finitely many roots.  For each such r the whole
#    line {(p, r p)} with p != 0 satisfies it.  So the fibre is a union of
#    lines through the origin : genus 0 (rational), NOT genus >=2.
# Solve g(r) = C symbolically-degree in r after clearing denominator:
#   4 r (1-r^2) = C (1+r^2)^2   ->  C r^4 + 2C r^2 + 4 r^3 - 4 r + C = 0
C = sp.symbols('C')
poly = sp.expand(C*(1+r**2)**2 - 4*r*(1-r**2))
print("g(r)-C numerator (as poly in r):", sp.collect(sp.expand(4*r*(1-r**2) - C*(1+r**2)**2), r))
deg = sp.degree(sp.Poly(sp.expand(4*r*(1-r**2) - C*(1+r**2)**2), r), r)
print("degree of g(r)=C in r:", deg, "-> finitely many (<=4) ratios r per C")
print()
print("CONCLUSION: the level set f(p,q)=C is a finite union of lines through")
print("the origin (one line per ratio r solving g(r)=C).  Each line is a")
print("rational curve (genus 0).  The 'fibre genus' of candidate 1 is 0, not")
print(">=2, so Faltings' genus>=2 finiteness does NOT apply to this fibration.")
