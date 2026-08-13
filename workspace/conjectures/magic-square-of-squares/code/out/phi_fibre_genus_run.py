"""Executable twin that actually runs the phi-fibre geometry check.
Run with python; prints whether f is homogeneous degree 0 and the fibre
structure conclusion for candidate phi-triple-curve-genus-faltings.
"""
import sympy as sp

m, n = sp.symbols('m n')
f = 4*m*n*(m**2 - n**2)/(m**2 + n**2)**2

t = sp.symbols('t')
print("homogeneous degree 0 (f(tm,tn)==f(m,n)):",
      sp.simplify(f.subs({m: t*m, n: t*n}) - f) == 0)

r = sp.symbols('r')
g = sp.simplify(f.subs(n, r*m))
print("f(m, r m) =", sp.simplify(g))
print("depends on ratio only (no m left):", sp.diff(g, m) == 0)

C = sp.symbols('C')
# g(r) = 4 r (1-r^2)/(1+r^2)^2 = C
num = sp.expand(4*r*(1-r**2) - C*(1+r**2)**2)
poly = sp.Poly(num, r)
print("g(r)-C numerator degree in r:", poly.degree())
print("  => for each constant C, at most 4 ratios r = n/m solve f=C")
print()
print("Each such ratio r sweeps the whole line {(p, r p)} : f is constant on it.")
print("So the 'fibre' f(p,q)=C is a finite union of rational lines (genus 0).")
print("Faltings (genus>=2 finite points) does NOT apply to this fibration.")
print()
# Concrete: q_v = 5544/7225 = f(9,2).  Instantiate C and show the fibre is lines.
C_v = sp.Rational(5544, 7225)
poly_v = sp.expand(4*(C_v)*(1+r**2)**2 - 4*r*(1-r**2))  # solved against C_v
roots_v = sp.solve(sp.Eq(4*r*(1-r**2) - C_v*(1+r**2)**2, 0), r)
print("ratios r with f(1,r)=f(9,2):", roots_v)
print("(9,2) itself is ratio n/m = 2/9; the listed roots are the full level set)")
