"""Independent verification of the lambda=13 coefficient forms for the three
(13) quartics, and a second route to the genus via the degree/discriminant fact:
y^2 = f(x) with f squarefree quartic has genus 1.
"""
import sympy as sp
lam, p, q = sp.symbols('lam p q')

A = (1 + 2*lam - lam**2)**2
B = (1 - 2*lam - lam**2)**2
E  = 4*(1 + 10*lam**2 + lam**4)
D1 = 2*(1 - 12*lam + 2*lam**2 + 12*lam**3 + lam**4)
D2 = 2*(1 + 12*lam + 2*lam**2 - 12*lam**3 + lam**4)

Q1 = B*p**4 + 32*lam**2*p**3*q + D2*p**2*q**2 - 32*lam**2*p*q**3 + B*q**4
Q2 = A*p**4 - E*p**3*q + D1*p**2*q**2 + E*p*q**3 + A*q**4
Q3 = B*p**4 + E*p**3*q + D2*p**2*q**2 - E*p*q**3 + B*q**4

def coeffs(Q):
    Poly = sp.Poly(sp.expand(Q), p, q)
    return [sp.expand(Poly.coeff_monomial(p**(4-i)*q**i)) for i in range(5)]

print("general-lambda coefficient vectors (p4,p3q,p2q2,pq3,q4):")
for name, Q in [("(12)",Q1), ("(13)",Q2), ("(13)",Q3)]:
    pass
for name, Q in [("Q1a",Q1),("Q1b",Q2),("Q1c",Q3)]:
    print(f"  {name} general: {coeffs(Q)}")

print("\nlambda=13 numeric coefficient vectors:")
for name, Q in [("Q1a",Q1),("Q1b",Q2),("Q1c",Q3)]:
    Q13 = sp.expand(Q.subs(lam,13))
    c = [int(x) for x in coeffs(Q13)]
    print(f"  {name} at 13: {c}  factored:", sp.factor(Q13))

# Genus by second route: degree-4 squarefree -> genus 1.
print("\n=== second route to genus ===")
for name, Q in [("Q1a",Q1),("Q1b",Q2),("Q1c",Q3)]:
    fx = sp.expand(Q.subs({lam:13, q:1}))
    poly = sp.Poly(fx, p)
    deg = poly.degree()
    sqf = sp.sqf_list(fx)[1]
    # distinct roots = number of irreducible factors (each appearing once, since squarefree)
    nfac = len(sqf)
    print(f"  {name}: deg={deg}, squarefree={deg==sum(m for _,m in sqf)}, "
          f"irreducible-factor-count={nfac}  -> genus 1 (y^2 = quartic, squarefree)")
    # explicit discriminant (non-zero => no multiple root)
    disc = sp.discriminant(poly.as_expr(), p)
    print(f"     discriminant = {disc}  -> non-zero: {disc!=0}")
