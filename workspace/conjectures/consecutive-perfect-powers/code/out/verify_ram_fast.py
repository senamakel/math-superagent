"""Faster exact verification that (1-zeta_p)^{p-1} = p * unit in Z[zeta_p].

We verify the ideal equality (p) = (1-zeta)^{p-1} without computing norms of
full elements (which uses resultants and is slow).  Equivalent exact checks:

  (A) Norm identity: N(1-zeta_p) = p.
  (B) The polynomial identity in the quotient ring: reduce (1-x)^{p-1} modulo
      Phi_p over integer polynomials, and verify it equals p * (an integer
      polynomial) whose coefficients, after reducing mod Phi_p, are all
      integers — i.e. (1-zeta)^{p-1} / p is in Z[zeta_p] (integral coefficients
      after reduction).  Since the norm of (1-zeta)^{p-1} is p^{p-1} and the
      norm of p is p^{p-1}, the quotient u=(1-zeta)^{p-1}/p automatically has
      norm 1 if it is integral (norm is multiplicative: N(u) = N(pow)/N(p) =
      p^{p-1}/p^{p-1} = 1).  So integrality of u IS the unit statement, and it
      is exactly the ideal equality (p) = (1-zeta)^{p-1}.
  (C) p in (1-zeta): p/(1-zeta) = (1-zeta)^{p-2} * u integral (u integral).

So checking (B) integrality of u is the key.  We do all polynomial work with
sympy exact integer polynomials.
"""
import sys
import sympy as sp
from lib.cyclo import cyclotomic_coeffs


def verify(p):
    x = sp.symbols('x')
    Phi = sp.expand(sp.Poly(cyclotomic_coeffs(p)).as_expr()) if False else None
    # cyclotomic_coeffs returns dict; build integer poly
    Ph = cyclotomic_coeffs(p)
    phi_poly = sum(int(c) * x**k for k, c in Ph.items())  # monic deg phi(p)=p-1
    # (1-x)^{p-1} mod phi_poly, exact integer polys
    poly = sp.Poly((1 - x)**(p - 1), x)
    phi = sp.Poly(phi_poly, x)
    q, rem = poly.div(phi)
    # u = rem / p  must have integer coefficients (i.e. each rem coeff divisible by p)
    coeffs = rem.all_coeffs()  # leading first; reverse to index by degree
    coeffs = list(reversed(coeffs))
    divok = all(int(c) % p == 0 for c in coeffs)
    u_int = [int(c) // p for c in coeffs]
    # N(1-zeta)=p: for prime p, Phi_p(1)=p directly is the known value; verify
    # independently: product of (1 - zeta^i) = p.  We trust Phi_p(1)=p exactly.
    norm_ok = (sp.expand(phi_poly).subs(x, 1) == p)  # Phi_p(1) = p
    return divok, u_int, norm_ok


def main(ps):
    print("p | (1-z)^{p-1} = p*u with u in Z[z] ? | Phi_p(1)=p (N(1-z)=p)")
    allok = True
    for p in ps:
        divok, u_int, norm_ok = verify(p)
        ok = divok and norm_ok
        allok &= ok
        print(f"{p:3d} | {str(divok):5s} | {norm_ok}   {'PASS' if ok else 'FAIL'}")
    print("ALL PASS" if allok else "SOME FAILED")


if __name__ == "__main__":
    ps = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    if len(sys.argv) > 1:
        ps = [int(a) for a in sys.argv[1:]]
    main(ps)
