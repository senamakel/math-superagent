# Census v2: polynomial-in-u counts vs rational-function-but-integer-valued invariants.
import sympy as sp
u = sp.symbols('u')
us = [1,3,4,10,31]
k = sp.Poly(u**2+u+2, u).as_expr()
v = sp.expand(1 + k + k*(k-2)/2)

def poly_info(name, expr):
    p = sp.Poly(sp.expand(expr), u)
    vals = tuple(int(sp.simplify(sp.expand(expr).subs(u,uu))) for uu in us)
    print("%-40s POLY degree=%2d LC=%5d vals=%s" % (name, int(sp.degree(p)), int(sp.LC(p)), vals))

def rat_info(name, expr):
    vals = tuple(sp.nsimplify(expr.subs(u,uu)) for uu in us)
    integ = all(sp.Eq(v, sp.Integer(int(v))) for v in vals)
    print("%-40s RATIONAL values=%s  all-integer-at-feasible=%s" % (name, [int(sp.nsimplify(x)) for x in vals], integ))

print("=== polynomial-in-u family counts (degree in u) ===")
poly_info("k = u^2+u+2", k)
poly_info("v = 1+k(k-2)/2", v)
poly_info("triangles vk/6", v*k/6)
poly_info("induced C5 vk(k-2)(k-4)/5", v*k*(k-2)*(k-4)/5)
poly_info("hexagons n3=0", v*k*(k-2)*(2*k**2-21*k+53)/12)
poly_info("n3-cap k(k-2)(k^2+2)/8", k*(k-2)*(k**2+2)/8)
poly_info("distance-2 k(k-2)/2", k*(k-2)/2)
poly_info("outer blocks k(k-2)(k-4)/12", k*(k-2)*(k-4)/12)
poly_info("replication (k-4)/2", (k-4)/2)
poly_info("matching-pair/vertex k(k-2)/8", k*(k-2)/8)

print()
print("=== rational-in-u, integer-valued at the 5 feasible index points ===")
# eigenvalues r=u, s=-(u+1); a=2u+1
mr = sp.expand((sp.Rational(1,2))*((v-1) - (2*k-(v-1))/(2*u+1)))
ms = sp.expand((sp.Rational(1,2))*((v-1) + (2*k-(v-1))/(2*u+1)))
rat_info("coclique Hoffman v(u+1)/(k+u+1)", v*(u+1)/(k+u+1))
rat_info("multiplicity m_r", mr)
rat_info("multiplicity m_s", ms)

print()
print("=== divisibility driver: a = 2u+1 divides 63 ===")
for uu in us:
    print("u=%3d  a=2u+1=%3d  63/a=%3d  (exact)  k=%d" % (uu, 2*uu+1, 63%(2*uu+1) and None or 63//(2*uu+1), uu*uu+uu+2))
