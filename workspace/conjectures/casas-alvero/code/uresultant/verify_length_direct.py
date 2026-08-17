"""Verify actual quotient length at n=3 (2 variables a2,a3) and n=4 against
the Samuel formula: L = prod_j (weighted order)/prod weight = n^(n-2).
Direct Groebner quotient-basis count, and confirm ord_0(R_i) via substitution.
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

for n in [3, 4]:
    a, R = built(n)
    ring_vars = [a[j] for j in range(2, n + 1)]
    G = sp.groebner(R, *ring_vars, order='lex')
    # Count quotient basis monomials (not in leading ideal) up to cap
    deg_cap = 2 * n * n
    basis = []
    for deg in range(deg_cap + 1):
        for es in product(range(deg + 1), repeat=n - 1):
            if sum(es) != deg:
                continue
            m = sp.Mul(*[v ** e for v, e in zip(ring_vars, es)])
            if G.reduce(m) != 0:
                basis.append(m)
    L = len(basis)
    print(f"n={n}: quotient length (basis count)= {L}, n^(n-2)={n**(n-2)}, "
          f"match={L == n**(n-2)}")
