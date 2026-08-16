"""Exact machinery for the Schaub-Spivakovsky bad-prime-minors criterion
(arXiv:2411.13967, Theorem 3.1).

Setup (degree n, x = (x_1..x_{n-1}), sigma_i = i-th elementary symmetric):
for j in 1..n-1, Phi_j is the involution x_i -> x_i - x_j (i != j),
x_j -> -x_j;  Phi_n = id.  For a tuple T = (j_1..j_{n-1}) in {1..n}^{n-1},
G_{T,i} = Phi_{j_i}(sigma_i(x)) is homogeneous of degree i.

    d = (n^2 - 3n + 4)/2
    C = number of monomials of degree d in n-1 variables
      = binomial((n^2 - n)/2, n - 2)
    D = sum_{i=1}^{n-1} (number of monomials of degree d - i)   (D >= C)

M_T is the D x C integer matrix whose rows are the coefficient vectors of
G_{T,i} * x^alpha (|alpha| = d - i, i = 1..n-1); columns are indexed by the
monomials of degree d (lexicographic order, x_1 > x_2 > ... > x_{n-1}).
J_T = gcd of all C x C minors of M_T.

Theorem 3.1: a prime p is a BAD prime for degree n iff p | J_T for some T
(equivalently iff p | lcm_T J_T).  Mechanically: p | J_T  <=>  every C x C
minor vanishes mod p  <=>  rank_{F_p}(M_T) < C.

Computation of J_T: the gcd of all C x C minors is the C-th determinantal
divisor d_C = s_1 * ... * s_C of M_T, with s_k the Smith-normal-form
invariant factors.  Exact integer arithmetic throughout.  The identity
d_C = |prod of SNF diagonal| is cross-checked against brute-force minor
enumeration (jt_bruteforce) on small matrices, and the prime set is
cross-checked against rank drops over GF(p) (rank_mod_p).

Functions
---------
lex_monomials(nvars, d)        exponent tuples of degree d, lex order x1>...
elementary_sigma(i, syms)      sigma_i as a sympy expression
GT_poly(n, j, i, syms)         Phi_j(sigma_i) as a sympy Poly
matrix_MT(n, T)                the D x C integer matrix M_T
jt_from_matrix(M)              |prod of SNF invariant factors| = gcd of
                               all C x C minors of M (exact)
jt_bruteforce(M, max_minors)   same gcd by explicit minor enumeration
                               (bounded oracle only)
jt_of_T(n, T)                  J_T for the tuple T
lcm_jt_over_T(n)               (lcm of all J_T, dict T -> J_T)
rank_mod_p(M, p)               exact rank of M mod p (fraction-free
                               modular Gaussian elimination)
criterion_bad_primes(n)        primes p with p | C(n,i) - 1 for some i
                               (Schaub-Spivakovsky SUFFICIENT bad-prime
                               criterion, Cor 8 of arXiv:2307.05997)
"""

from __future__ import annotations

import math
from itertools import combinations, product

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def lex_monomials(nvars, d):
    """All exponent tuples alpha in N^nvars with |alpha| = d, ordered
    lexicographically with x_1 > x_2 > ... > x_nvars (descending
    lexicographic tuple order).  Exact; returns a list of tuples."""
    if nvars <= 0:
        return [()] if d == 0 else []
    out = []

    def rec(k, remaining, prefix):
        if k == nvars - 1:
            out.append(tuple(prefix + [remaining]))
            return
        for v in range(remaining, -1, -1):
            rec(k + 1, remaining - v, prefix + [v])

    rec(0, d, [])
    out.sort(reverse=True)
    return out


def elementary_sigma(i, syms):
    """The i-th elementary symmetric polynomial of ``syms`` as a sympy
    expression (0 if i out of range).  Computed from
    prod_k (1 + t x_k) = sum_i sigma_i t^i, exactly."""
    t = sp.symbols("t")
    prod = sp.Integer(1)
    for xk in syms:
        prod = prod * (1 + t * xk)
    p = sp.Poly(prod.expand(), t)
    return p.coeff_monomial(t ** i)


def GT_poly(n, j, i, syms):
    """G_{T,i} = Phi_j(sigma_i(x_1..x_{n-1})) as a homogeneous degree-i sympy
    Poly in ``syms`` (n-1 symbols) with QQ coefficients.  j in {1..n};
    j == n is the identity."""
    sigma = elementary_sigma(i, syms)
    if j == n:
        return sp.Poly(sigma, *syms, domain=sp.QQ)
    xj = syms[j - 1]
    pairs = []
    for k in range(n - 1):
        pairs.append((syms[k], syms[k] - xj if k != j - 1 else -xj))
    return sp.Poly(_simultaneous_subs(sigma, pairs), *syms, domain=sp.QQ)


def _simultaneous_subs(expr, pairs):
    """Substitute each variable in ``pairs`` simultaneously (sympy's dict
    .subs is SEQUENTIAL, which corrupts simultaneous linear changes like
    x_i -> x_i - x_j).  Fresh dummy variables are used, then released.
    pairs: list of (symbol, replacement-expr)."""
    dummies = [sp.symbols("__d%d" % k) for k in range(len(pairs))]
    e = expr
    for (v, d) in zip([p[0] for p in pairs], dummies):
        e = e.subs(v, d)
    for (d, (v, rep)) in zip(dummies, pairs):
        e = e.subs(d, rep)
    return e


def matrix_MT(n, T):
    """The D x C integer matrix M_T (see module docstring).  Columns indexed
    by lex_monomials(n-1, d); rows are the coefficient vectors of
    G_{T,i} * x^alpha for i = 1..n-1 and |alpha| = d - i (alpha in the same
    lex order).  Returns a sympy Matrix with ZZ entries."""
    syms = sp.symbols("x1:%d" % n)  # x_1 .. x_{n-1}
    d = (n * n - 3 * n + 4) // 2
    cols = lex_monomials(n - 1, d)
    col_index = {alpha: k for k, alpha in enumerate(cols)}
    rows = []
    for i in range(1, n):
        gi = GT_poly(n, T[i - 1], i, syms)
        terms = {tuple(m): int(c) for (m, c) in gi.terms()}
        for alpha in lex_monomials(n - 1, d - i):
            row = [0] * len(cols)
            for beta, c in terms.items():
                gamma = tuple(beta[k] + alpha[k] for k in range(n - 1))
                row[col_index[gamma]] += c
            rows.append(row)
    return sp.Matrix(rows)


def jt_from_matrix(M):
    """gcd of all C x C minors of M (C = number of columns), exactly.

    Uses the classical identity d_C = s_1 * ... * s_C with s_k the Smith
    normal form invariant factors of M; |.| removes the sign ambiguity of
    the SNF.  Returns 0 iff rank(M) < C over QQ."""
    S = smith_normal_form(M)
    prod = 1
    for i in range(min(S.shape)):
        prod *= S[i, i]
    return abs(prod)


def jt_bruteforce(M, max_minors=50000):
    """gcd of all C x C minors of M by explicit enumeration of the
    C(D, C) minors (bareiss determinants over ZZ).  BOUNDED ORACLE only:
    refuses to run when the number of minors exceeds ``max_minors``.
    Existence: validates jt_from_matrix on small matrices."""
    rows, cols = M.shape
    C = cols
    n_minors = math.comb(rows, C)
    if n_minors > max_minors:
        raise ValueError(
            "%d minors exceed the oracle bound %d" % (n_minors, max_minors))
    g = 0
    for comb in combinations(range(rows), C):
        sub = M.extract(list(comb), list(range(C)))
        d = sub.det(method="bareiss")
        g = math.gcd(g, d)
    return g


def jt_of_T(n, T):
    """J_T = gcd of all C x C minors of M_T for the tuple T, exactly."""
    return jt_from_matrix(matrix_MT(n, T))


def lcm_jt_over_T(n):
    """(lcm over all T in {1..n}^{n-1} of J_T, dict T -> J_T).  Exact."""
    all_T = list(product(range(1, n + 1), repeat=n - 1))
    js = {T: jt_of_T(n, T) for T in all_T}
    return math.lcm(*js.values()), js


def rank_mod_p(M, p):
    """Exact rank of the integer matrix M over GF(p), by fraction-free
    modular Gaussian elimination (p prime).  O(D * C^2) arithmetic ops
    mod p.  Used for the independent bad-prime route: p | J_T  <=>
    rank_{F_p}(M_T) < C."""
    rows = M.tolist()
    R = len(rows)
    C = len(rows[0]) if rows else 0
    A = [[int(v) % p for v in row] for row in rows]
    r = 0
    for col in range(C):
        pivot = None
        for rr in range(r, R):
            if A[rr][col] % p != 0:
                pivot = rr
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][col], p - 2, p)
        A[r] = [(v * inv) % p for v in A[r]]
        for rr in range(R):
            if rr != r and A[rr][col] % p != 0:
                f = A[rr][col] % p
                A[rr] = [(A[rr][k] - f * A[r][k]) % p for k in range(C)]
        r += 1
    return r


def criterion_bad_primes(n):
    """Primes p with p | C(n, i) - 1 for some i in {1..n-1}, exactly.

    By Schaub-Spivakovsky (arXiv:2307.05997, Cor 8) every such prime is a
    bad prime for degree n: the SUFFICIENT binomial criterion.  The full
    minor criterion (Thm 3.1 of arXiv:2411.13967) can certify more primes.
    """
    bad = set()
    for i in range(1, n):
        v = sp.binomial(n, i) - 1
        for p in sp.factorint(v):
            bad.add(p)
    return sorted(bad)


def minor_identity_checks(sizes=((6, 4), (8, 5), (9, 6)), seeds=(0, 1, 2),
                          lo=-9, hi=9):
    """Check d_C = |prod of SNF diagonal| against brute-force minor
    enumeration on random small matrices.  Returns (ok, lines)."""
    ok = True
    lines = []
    for (r, c) in sizes:
        for seed in seeds:
            M = sp.randMatrix(r, c, min=lo, max=hi, seed=seed)
            a = jt_bruteforce(M)
            b = jt_from_matrix(M)
            match = a == b
            ok = ok and match
            lines.append("brute=%d snf=%d match=%s (%dx%d seed=%d)"
                         % (a, b, match, r, c, seed))
    return ok, lines
