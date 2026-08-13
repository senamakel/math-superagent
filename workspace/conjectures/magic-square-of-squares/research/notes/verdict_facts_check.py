"""Analytic verification of two structural facts used in the approach verdicts.

FACT A (candidate 1): f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 is homogeneous of
degree 0, so its level sets are unions of rational lines (genus 0), not
genus>=2 curves. Hence Faltings' finiteness does not apply to the fibre the
candidate proposes to compute genus of.

FACT B (candidate 3): d = 4k^2 mn(m^2-n^2) = k^2 * Im((m+ni)^4).  This checks
the candidate's Gaussian quartic-residue description of the congruent-number
difference d. (Holds: Im((m+ni)^4) = 4mn(m^2-n^2).)
"""
import sympy as sp

# ---- FACT A : f homogeneous degree 0 ----
m, n, t = sp.symbols('m n t')
f = 4*m*n*(m**2 - n**2)/(m**2 + n**2)**2
num  = 4*m*n*(m**2 - n**2)
den  = (m**2 + n**2)**2
print("numerator scales:  num(tm,tn)/num(m,n) =",
      sp.simplify(num.subs({m: t*m, n: t*n}) / num))
print("denominator scales:den(tm,tn)/den(m,n) =",
      sp.simplify(den.subs({m: t*m, n: t*n}) / den))
print("f(tm,tn) == f(m,n):", sp.simplify(f.subs({m: t*m, n: t*n}) - f) == 0)
# level set f(p,q)=C depends only on ratio r=q/p ; degree in r = 4
r, C = sp.symbols('r C')
g = sp.simplify(f.subs(n, r*m))
poly = sp.Poly(sp.expand(4*r*(1-r**2) - C*(1+r**2)**2), r)
print("f(p,q)=C  <=>  g(r)=C in r=q/p ; degree in r =", poly.degree())
print("=> each level set is a union of <= 4 lines through the origin; "
      "rational, genus 0.")
print()

# ---- FACT B : quartic-residue description of d (candidate 3) ----
z = (m + sp.I*n)**4
print("Im((m+ni)^4) =", sp.expand(sp.im(z)))
print("4mn(m^2-n^2)  =", sp.expand(4*m*n*(m**2 - n**2)))
print("d (run's value, 4k^2 mn(m^2-n^2)) = k^2 * Im((m+ni)^4):",
      sp.expand(4*m*n*(m**2-n**2)) == sp.expand(sp.im(z)))
