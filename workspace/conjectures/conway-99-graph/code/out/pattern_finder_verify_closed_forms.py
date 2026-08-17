# Verify all claimed family closed forms exactly with sympy over the
# feasible index set u in {1,3,4,10,31} (a = 2u+1 | 63).
# Correct relations:
#   k = u^2+u+2 ;  v = 1 + k + k(k-2)/2
#   char x^2 - (lam-mu)x - (k-mu) with lam=1,mu=2: x^2 + x - (k-2)
#   roots: r = u, s = -(u+1)   (check u=1: r=1,s=-2; u=3: r=3,s=-4; u=4: 4,-5)
#   a = r - s = 2u+1 = sqrt(4k-7)
#   coclique Hoffman: alpha <= v*(-s)/(k-s) = v*(u+1)/(k+u+1)
import sympy as sp

u = sp.symbols('u')
us = [1, 3, 4, 10, 31]

k_expr = sp.Poly(u**2 + u + 2, u).as_expr()
v_expr = sp.expand(1 + k_expr + k_expr*(k_expr-2)/2)

def ev(expr):
    return [sp.nsimplify(expr.subs(u, uu)) for uu in us]

def show(name, expr):
    vals = ev(expr)
    print(f"{name:34s} {vals}")
    return vals

tris   = sp.expand(v_expr*k_expr/6)
hex0   = sp.expand(v_expr*k_expr*(k_expr-2)*(2*k_expr**2-21*k_expr+53)/12)
p5     = sp.expand(v_expr*k_expr*(k_expr-2)*(k_expr-4)/5)
cocl   = sp.expand(v_expr*(u+1)/(k_expr+u+1))
mr     = sp.expand((k_expr - v_expr*(-(u+1)))/(u - (-(u+1))))
ms     = sp.expand((k_expr - v_expr*u)/((-(u+1)) - u))

print("k   ", ev(k_expr))
print("v   ", ev(v_expr))
show("triangles vk/6", tris)
show("hexagons (n3=0)", hex0)
show("induced C5", p5)
show("coclique Hoffman", cocl)
show("multiplicity m_r", mr)
show("multiplicity m_s", ms)
show("multiplicity m_s (alt)", sp.expand(v_expr - 1 - mr))

# compare against recorded tables
print("\n=== compare to recorded ===")
print("triangles recorded  [6, 231, 891, 117096, 81842481]")
print("  computed          ", ev(tris))
print("C5 recorded         [0, 33264, 384912, 1669320576, 96451036488576]")
print("  computed          ", ev(p5))
print("coclique recorded   [3, 22, 45, 561, 15408]")
print("  computed          ", ev(cocl))
