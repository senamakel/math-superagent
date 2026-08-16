"""The objects of Ghosh (arXiv:2501.09272) section 2, implemented exactly.

Faithful to the held source research/sources/ghosh2025_proof_html.full.md
(lines 105-121):

  (a) HD^i_k -- the i-th multivariate Hasse-Schmidt derivation, eq (2.1):
        HD^i_k x_1^{a_1}...x_k^{a_k} =
            sum_{j_1+...+j_k=i} prod_l binom(a_l, j_l) x_l^{a_l-j_l},
      applied to the monomial x_k := x_1...x_k.  One checks
        HD^i_k x_k = e_{k-i}(x_1,...,x_k)   (elementary symmetric).

  (b) Phi^#_{d,j} -- the K-algebra automorphism of K[x_1..x_d], eq (2.2):
        x_l -> x_l - x_j  (l != j),   x_j -> -x_j,   Phi^#_{d,d+1} = identity.
      Implemented as a simultaneous substitution (expr.xreplace), so each
      generator image is a polynomial in the *new* generators, exactly as an
      algebra map requires -- no second substitution inside the images.

  (c) F(i,j,n) := Phi^#_{n,j}(HD^{i-1}_n x_n).  Since HD^{i-1}_n x_n =
      e_{n-i+1} is multilinear (degree <= 1 in every variable) and Phi is
      affine in every variable, F has degree <= 1 in x_n, so exactly:
        F = x_n * f(i,j,n) + g(i,j,n),   f, g in K[x_1..x_{n-1}].

Why these objects matter (the char-p break, per eq (4.18) of the proof):
the isomorphism R_n/(F(1,j_1,n),...,F(n,j_n,n)) ~= R_{n-1}/(Delta_{1n},...)
needs the leading coefficient f(n,j_n,n) to be a unit.  It equals 1 for
j_n != n and -n for j_n == n.  Over F_p with p | n the unit -n vanishes,
which is exactly where the char-0-only step of the downward induction breaks.

Every function is exact over QQ (char=0) or GF(p) (char=p) via sympy Poly
domains (domain=QQ / modulus=p).  No floating point anywhere.

Functions
---------
- hd_monomial_image(alphas, i, xvars, char)   HD^i of x_1^{a1}...x_k^{ak},
                                               literal sum of eq (2.1).
- e_symmetric(k, xvars, char)                 e_k(x_1,...,x_n).
- phi(poly, d, j, xvars, char)                Phi^#_{d,j}(poly).
- F_ij(i, j, n, xvars, char)                  F(i,j,n) as a Poly in x_1..x_n.
- x_n_decompose(F, xn)                        exact (f, g) with F = xn*f + g.
- f_ij(i, j, n, xvars, char)                  the x_n-coefficient f(i,j,n).

Correctness is established by code/ghosh_charp/verify_break.py (all checks
PASS, captured in code/out/ghosh_break.captured.txt): f(n,j,n) = 1 (j != n)
and -n (j == n) for n = 2..10 over QQ and GF(p), vanishing iff p | n and
j == n; the hand-verified identities Phi^#_{n,n}(e_1) = e_1 - n*x_n and
Phi^#_{n,j}(e_1) = e_1 - (n+1)*x_j (j != n) are asserted there.
"""

from itertools import combinations, product

from sympy import Poly, QQ, Integer, binomial, expand, symbols

__all__ = [
    "hd_monomial_image",
    "e_symmetric",
    "phi",
    "F_ij",
    "x_n_decompose",
    "f_ij",
]


def _to_poly(expr, xvars, char=0):
    """Normalise ``expr`` to an exact sympy Poly over QQ (char=0) or GF(p).

    Coefficients are reduced exactly: domain=QQ for char 0, modulus=p for
    char p.  ``xvars`` is the full generator tuple the Poly lives in.
    """
    expr = expand(expr)
    if char == 0:
        return Poly(expr, *xvars, domain=QQ)
    return Poly(expr, *xvars, modulus=char)


def hd_monomial_image(alphas, i, xvars, char=0):
    """HD^i of the monomial x_1^{a1}...x_k^{ak}, literal sum of eq (2.1).

    HD^i_k x^alpha = sum_{j_1+...+j_k=i} prod_l binom(a_l, j_l)
                     x_l^{a_l - j_l},  the sum over 0 <= j_l <= a_l.
    Returns a Poly over QQ or GF(p).  For alphas = (1,)*n this is
    e_{n-i}(x_1,...,x_n); verify_break.py asserts that identity.
    """
    k = len(alphas)
    assert len(xvars) == k
    expr = Integer(0)
    for js in product(*[range(a + 1) for a in alphas]):
        if sum(js) != i:
            continue
        term = Integer(1)
        for l in range(k):
            jl = js[l]
            term *= binomial(alphas[l], jl)
            if alphas[l] - jl:
                term *= xvars[l] ** (alphas[l] - jl)
        expr += term
    return _to_poly(expr, xvars, char)


def e_symmetric(k, xvars, char=0):
    """Elementary symmetric polynomial e_k(x_1,...,x_n) over QQ or GF(p)."""
    n = len(xvars)
    expr = Integer(0)
    for S in combinations(range(n), k):
        term = Integer(1)
        for l in S:
            term *= xvars[l]
        expr += term
    return _to_poly(expr, xvars, char)


def phi(poly, d, j, xvars, char=0):
    """Apply the algebra automorphism Phi^#_{d,j} (eq 2.2) to ``poly``.

    For 1 <= j <= d: x_l -> x_l - x_j (l != j), x_j -> -x_j.
    For j = d+1: the identity.  ``xvars`` must have at least d entries; the
    result is a Poly in xvars[:d].  The substitution is simultaneous
    (expr.xreplace), so images of generators are polynomials in the NEW
    generators -- the algebra-map semantics, not a sequential substitution.
    """
    if not isinstance(poly, Poly):
        poly = _to_poly(poly, xvars[:d], char)
    if j == d + 1:
        return poly
    assert 1 <= j <= d
    reps = {}
    xj = xvars[j - 1]
    for l in range(1, d + 1):
        xl = xvars[l - 1]
        reps[xl] = -xj if l == j else xl - xj
    return _to_poly(poly.as_expr().xreplace(reps), xvars[:d], char)


def F_ij(i, j, n, xvars, char=0):
    """F(i,j,n) := Phi^#_{n,j}(HD^{i-1}_n x_n), a Poly in x_1..x_n.

    HD^{i-1}_n x_n is computed from the definition (2.1) (not from the
    e_{n-i+1} closed form), then Phi^#_{n,j} is applied -- faithful to the
    source.  1 <= i <= n, 1 <= j <= n+1.
    """
    assert 1 <= i <= n and 1 <= j <= n + 1
    hd = hd_monomial_image((1,) * n, i - 1, xvars[:n], char)
    return phi(hd, n, j, xvars[:n], char)


def x_n_decompose(F, xn):
    """Exact decomposition F = xn * f + g for F of degree <= 1 in xn.

    f = F|_{xn=1} - F|_{xn=0},  g = F|_{xn=0}.  Returns plain sympy
    expressions (exact integers / rationals, reduced mod p when F is over
    GF(p)).  The caller must have established degree <= 1 in xn; f_ij
    asserts it.
    """
    e = F.as_expr()
    e1 = expand(e.subs(xn, Integer(1)))
    e0 = expand(e.subs(xn, Integer(0)))
    return expand(e1 - e0), e0


def f_ij(i, j, n, xvars, char=0):
    """The x_n-coefficient f(i,j,n) of F(i,j,n) = x_n f + g.

    Exact: since F has degree <= 1 in x_n (asserted), f is obtained by
    evaluating at x_n = 1 and x_n = 0; no truncation of a higher expansion.
    """
    F = F_ij(i, j, n, xvars, char)
    assert F.degree(xvars[n - 1]) <= 1
    f, _g = x_n_decompose(F, xvars[n - 1])
    return f
