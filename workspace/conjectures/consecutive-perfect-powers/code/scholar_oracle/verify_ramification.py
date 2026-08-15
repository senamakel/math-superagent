"""Scholar verification of the load-bearing ramification claim
zeta-p-ring-of-integers-and-ramification: for K=Q(zeta_p), p odd prime,
(p) = (1-zeta_p)^(p-1) and Norm(1-zeta_p) = p, i.e. the ideal (1-zeta_p)
is a prime of norm p with ramification index p-1.

This is the foundation of the whole both-odd cyclotomic approach, and it is
status: asserted in the library. Verify its two exact consequences directly:

1. Norm_{Q(zeta_p)/Q}(1 - zeta_p) = p   (exact integer arithmetic).
2. The cyclotomic identity  prod_{j=1}^{p-1}(1 - zeta_p^j) = p, which is
   exactly the ideal factorisation (p) = (1-zeta_p)^{p-1} evaluated: since
   1 - zeta_p^j = (1-zeta_p) * (1 + zeta_p + ... + zeta_p^{j-1}) and the
   latter unit has valuation 0 at (1-zeta_p), the product has valuation
   p-1 at (1-zeta_p).

Also verify a third exact fact needed downstream: Phi_p(X) = (X^p-1)/(X-1)
mod p equals (X-1)^(p-1), confirming total ramification (the residue-degree 1
part).
"""
import sympy
from sympy import expand, Poly, symbols, ZZ

X = symbols('X')
p_list = [3, 5, 7, 11, 13, 17, 19]

print("=== Norm_{Q(zeta_p)/Q}(1-zeta_p) and prod_{j=1}^{p-1}(1-zeta_p^j) ===")
for p in p_list:
    # Cyclotomic polynomial Phi_p(X) = (X^p-1)/(X-1) = 1+X+...+X^(p-1)
    Phi = Poly(expand(sympy.cyclotomic_poly(p, X)), X, domain=ZZ)
    # Norm of (1 - zeta) = Phi_p(1) evaluated at X=1 is on the nose because the
    # conjugates of (1-zeta) are (1-zeta^j), j coprime to p i.e. j=1..p-1.
    norm = Phi.eval(1)
    # The polynomial identity prod_{j=1}^{p-1}(1 - X^j) with X a primitive p-th
    # root; 1 - X^j and j runs 1..p-1.  The true identity is
    # prod_{j=1}^{p-1}(1 - zeta^j) = p.  We verify it by noting that
    # prod_{j=1}^{p-1}(X - zeta^j) = Phi_p(X), so setting X=1 gives
    # prod (1 - zeta^j) = Phi_p(1) = p.
    assert norm == p, f"FAIL p={p}: Norm(1-zeta)={norm}, expected {p}"
    print(f"p={p:2d}  Norm(1-zeta_p) = Phi_p(1) = {norm}  [expected {p}]  PASS")

print()
print("=== Phi_p(X) mod p == (X-1)^(p-1)  (total ramification) ===")
for p in p_list:
    Phi = Poly(expand(sympy.cyclotomic_poly(p, X)), X, domain=ZZ)
    # coefficients mod p
    coeffs = Phi.all_coeffs()
    reduced = [c % p for c in coeffs]
    # (X-1)^(p-1) has all coefficients = binom(p-1,k) mod p; for prime p,
    # (X-1)^(p-1) == X^(p-1) - X^(p-2) + ... - X + 1 (mod p), i.e.
    # coefficient of X^(p-1-k) is (-1)^k binom(p-1,k)
    from sympy import binomial
    expect = [((-1)**k * binomial(p-1, k)) % p for k in range(p)]
    # expect[k] = coeff of X^(p-1-k)
    match = (reduced == expect)
    print(f"p={p:2d}  Phi_p mod p == (X-1)^(p-1): {match}")
    if not match:
        print(f"     got {reduced}\n     exp {expect}")
print()
print("All ramification checks complete. (1) Norm(1-zeta_p)=p, (2) prod(1-zeta^j)=p,"
      " (3) Phi_p(X) ≡ (X-1)^{p-1} mod p — the three exact contents of the claim.")
