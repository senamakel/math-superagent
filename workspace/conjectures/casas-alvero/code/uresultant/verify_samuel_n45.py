"""Verify the Samuel / Valabrega-Valla identity for the CA traceless-slice
scheme at n=4,5:

    |QQ[a_2..a_n]/I_n|  ==  prod_{i=1}^{n-1} ord_0(R_i) / prod_{j=2}^{n} w(a_j)

with w(a_j) = j (x weight 1, a_j weight j).  ord_0 = weighted order of the
resultant at the origin.  If it holds, the scheme is a complete

intersection whose associated graded at 0 is Cohen-Macaulay, and the
quotient's multiplicity, computable by the multiplication map (no lex GB),
certifies V(I_n) = {0} = CA in degree n.

Establishes the conjectured closed form  |Q[a_2..a_n]/I_n| = n^{n-2}
==========================================================
(Cayley's number of labeled trees on n vertices), for n = 3,4,5.
"""
from sympy import symbols, Poly, expand, resultant, binomial, prod as sprod

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def slice_resultants(n):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    return [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]


def weighted_order(poly, n):
    """ord_0: smallest weighted degree, w(a_j)=j."""
    a = symbols(f"a_1:{n+1}")
    sl = list(a[1:])
    W = list(range(2, n + 1))
    P = Poly(poly, *sl, domain=sympy_QQ)
    return min(sum(e * w for e, w in zip(m, W)) for m, c in P.terms())


from sympy import QQ as sympy_QQ

lengths = {3: 3, 4: 16, 5: 125}  # from Singular vdim (trusted engine)
for n in (4, 5):
    a = symbols(f"a_1:{n+1}")
    sl = list(a[1:])
    R = slice_resultants(n)
    ords = [weighted_order(r, n) for r in R]
    W = list(range(2, n + 1))
    lhs = sprod(ords) / sprod(W)
    print(f"n={n}: ords={ords}, prod ords={sprod(ords)}, prod w={sprod(W)}")
    print(f"   Samuel RHS = {lhs},  Singular length = {lengths[n]},  "
          f"match = {lhs == lengths[n]}")
    print(f"   n^(n-2) = {n ** (n - 2)},  match = {n ** (n - 2) == lengths[n]}")
