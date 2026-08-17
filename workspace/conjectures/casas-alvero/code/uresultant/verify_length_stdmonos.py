"""Compute quotient length via standard monomials (monomials not divisible by
any leading monomial of the reduced Groebner basis). n=3,4.
"""
import sympy as sp
from itertools import product

def built(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) for j in range(n + 1)]
    coeffs = [sp.Integer(1)] + [sp.Integer(0)] + [a[j] for j in range(2, n + 1)]
    f = sum(coeffs[j] * x ** (n - j) for j in range(n + 1))
    R = []
    for i in range(1, n):
        hi = sum(sp.binomial(n - j, i) * coeffs[j] * x ** (n - j - i)
                 for j in range(n + 1) if (n - j) >= i)
        R.append(sp.resultant(f, hi, x))
    return a, R

def standard_basis_count(G, ring_vars, cap):
    """Count monomials not divisible by any leading monomial of G, up to cap."""
    lms = [sp.Poly(g, *ring_vars).LM(order=G.order) for g in G.polys]
    # sympy Poly LM returns (dict(exp), coeff); reinterpret as exponent tuple
    def exp_of(g, ring_vars):
        P = sp.Poly(g, *ring_vars)
        # leading monomial by the given monomial ordering
        return P.LM(order=G.order)
    count = 0
    lmdicts = []
    for g in G.polys:
        P = sp.Poly(g, *ring_vars)
        lm = P.terms(order=G.order)[0][0]
        lmdicts.append(lm)
    for deg in range(cap + 1):
        for es in product(range(deg + 1), repeat=len(ring_vars)):
            if sum(es) != deg:
                continue
            # divisible by any leading exponent tuple?
            if any(all(es[k] >= lm[k] for k in range(len(es))) for lm in lmdicts):
                continue
            count += 1
    return count

for n in [3, 4]:
    a, R = built(n)
    ring_vars = [a[j] for j in range(2, n + 1)]
    G = sp.groebner(R, *ring_vars, order='lex')
    cnt = standard_basis_count(G, ring_vars, 3 * n * n)
    print(f"n={n}: standard-monomial count = {cnt}, n^(n-2)={n**(n-2)}")
