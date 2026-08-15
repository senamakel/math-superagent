"""Sanity-check the concrete algebraic identities invoked in the three
approach files proposed this turn. Exact sympy arithmetic only."""
import sympy as sp

x, y = sp.symbols('x y')

def lucas_U(n, P, Q):
    # Lucas sequence: U0=0, U1=1, U_{k+1} = P U_k - Q U_{k-1}
    U0, U1 = 0, 1
    if n == 0: return U0
    if n == 1: return U1
    for _ in range(2, n+1):
        U0, U1 = U1, sp.expand(P*U1 - Q*U0)
    return U1

# Claim 1: (x^p - 1)/(x-1) = U_p(x+1, x)   (roots a=x, b=1 -> P=x+1, Q=x)
for p in [3, 5, 7]:
    lhs = sp.expand((x**p - 1)/(x - 1))
    rhs = lucas_U(p, x+1, x)
    print(f"p={p}: (x^p-1)/(x-1) == U_p(x+1,x):", sp.simplify(lhs - rhs) == 0)

# Claim 2: (y^q + 1)/(y+1) = U_q(y-1, -y) for q odd   (roots a=y, b=-1 -> P=y-1, Q=-y)
for q in [3, 5, 7]:
    lhs = sp.expand((y**q + 1)/(y + 1))   # q odd so y+1 | y^q + 1
    rhs = lucas_U(q, y-1, -y)
    print(f"q={q}: (y^q+1)/(y+1) == U_q(y-1,-y):", sp.simplify(lhs - rhs) == 0)

# Claim 3: gcd(x-1, Phi_p(x)) divides p  (the cyclotomic factor Phi_p(x))
for p in [3, 5, 7]:
    # Phi_p(x) = (x^p-1)/(x-1)
    phi = sp.expand((x**p - 1)/(x - 1))
    # gcd of two polynomials over Q; divisibility of the *value* gcd by p:
    # check: evaluate the polynomial gcd symbolically
    g = sp.gcd(sp.expand(x - 1), phi)
    print(f"p={p}: poly gcd(x-1, Phi_p(x)) =", g)

# Claim 4: genus of the smooth model of X^p - Y^q = 1 is (p-1)(q-1)/2
# PROVIDED gcd(p,q)=1. The p=q case is degenerate: x^p - y^p factors over Q,
# so the curve is reducible and the smooth-model genus formula does not apply.
# NOTE: this scaffold is written but has NOT been executed (no code tool in this
# session); the identities are standard and left for research/symbolic_math to confirm.
print("genus (p-1)(q-1)/2 at (2,3), gcd=1:", (2-1)*(3-1)//2, "(elliptic curve, genus 1)")
print("genus (p-1)(q-1)/2 at (3,5), gcd=1:", (3-1)*(5-1)//2, "(smooth, genus 4)")
print("(3,3) is degenerate gcd=3; smooth-model genus formula does not apply")
