"""Bremner, On squares of squares II (Acta Arith. 99.3, 2001), equations (12) & (13).

Extract the exact quartics, verify the lambda=13,p=9,q=2 square for (12),
factor the three quartics of (13) and compute the genus of quartic(p,q)=Y^2.
"""
import sympy as sp

lam, p, q = sp.symbols('lam p q', real=True)

# ---- Equation (12) ---------------------------------------------------------
# (1+2l-l^2)^2 p^4 -32l^2 p^3 q + 2(1-12l+2l^2+12l^3+l^4) p^2 q^2
#   + 32l^2 p q^3 + (1+2l-l^2)^2 q^4  =  square
A = (1 + 2*lam - lam**2)**2
C12 = A*p**4 - 32*lam**2*p**3*q + 2*(1 - 12*lam + 2*lam**2 + 12*lam**3 + lam**4)*p**2*q**2 \
      + 32*lam**2*p*q**3 + A*q**4
print("EQ(12) =", sp.expand(C12))

# ---- Equation (13), three quartics ------------------------------------------
B = (1 - 2*lam - lam**2)**2
D2 = 2*(1 + 12*lam + 2*lam**2 - 12*lam**3 + lam**4)        # p^2 q^2 coeff (uses +)
D1 = 2*(1 - 12*lam + 2*lam**2 + 12*lam**3 + lam**4)        # p^2 q^2 coeff (uses -)
E  = 4*(1 + 10*lam**2 + lam**4)                            # p^3 q / p q^3 coeff

Q1 = B*p**4 + 32*lam**2*p**3*q + D2*p**2*q**2 - 32*lam**2*p*q**3 + B*q**4
Q2 = A*p**4 - E*p**3*q + D1*p**2*q**2 + E*p*q**3 + A*q**4
Q3 = B*p**4 + E*p**3*q + D2*p**2*q**2 - E*p*q**3 + B*q**4
for name, Q in [("(13)a", Q1), ("(13)b", Q2), ("(13)c", Q3)]:
    print(name, "=", sp.expand(Q))

print()
print("=== TASK 1: eq (12) at lam=13, p=9, q=2 ===")
val = C12.subs({lam: 13, p: 9, q: 2})
print("value          =", val)
r = sp.isqrt(val)
print("isqrt          =", r, " squared =", r**2, " is a perfect square:", r*r == val)
print("12682/34       =", sp.Rational(12682, 34))
print("373*34         =", 373*34)
print("425*34         =", 425*34)

print()
print("=== TASK 2: genus of quartic(p,q)=Y^2 for the three (13) quartics at lam=13 ===")
for name, Q in [("(13)a", Q1), ("(13)b", Q2), ("(13)c", Q3)]:
    Ql = sp.Poly(sp.expand(Q.subs(lam, 13)), p, q)
    fac = sp.factor(Ql.as_expr())
    print(f"\n{name} at lam=13:")
    print("  factored:", fac)
    # dehomogenize x = p/q:  F(x,1)
    Fx = Q.subs(lam, 13).subs(q, 1)
    poly = sp.Poly(sp.expand(Fx), p)
    roots = sp.roots(poly)
    print("  roots of F(x,1):", {sp.nsimplify(k): v for k, v in roots.items()})
    # squarefree?
    sqfree = sp.sqf_list(poly.as_expr())
    print("  sqf decomposition:", sqfree)
    n_distinct = sum(1 for _, m in sqfree[1] if sp.degree(poly) > 0)
    deg = poly.degree()
    print("  degree in x =", deg, "  distinct roots count (with mult):", n_distinct,
          "  integral:", all(sp.Integer(i) == i for i, _ in sqfree[1]))
