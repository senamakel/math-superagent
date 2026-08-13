"""Matveev 2000 (Izv. Math. 62:4, 723-772) explicit lower bounds for
homogeneous rational linear forms in logarithms, specialized to K = Q.

Primary source: research/sources/matveev-2000-homogeneous-linear-form.full.md
Theorem 2.2 constants with K = Q (real field):
    kappa = 1 (K subset R), D = D_K/kappa = 1,
    rho = rank_R{ln alpha_1, ..., ln alpha_n} = 1
          (all ln alpha_j are real numbers, so their R-span is R^1),
    C3 = n/rho = n.
For alpha_j = distinct primes p_j,
    A_j = max{h(p_j), |ln p_j|/D, 1/(D C1)} = ln p_j
          (h(p) = ln p for a positive integer prime, and 1/C1 < 1 < ln 2 <= ln p_j),
so the theorem's hypotheses hold with A_j = ln p_j.  This is also exactly the
setting of Theorem 2.3(ii) (K=Q, alpha_j in Z, alpha_j > 0, A_j = ln alpha_j).

Formulae used (paper's numbering):
    (2.4)   C1 = (1 + e^{-2n}/148)(n ln 2 + 2)(1 + 1/n) C3,
            C2 = 4(n+1)(6 + 5/(n ln 2 + 2)) e^{2n} n^{1/2} C3,
    (2.5)   omega = Omega * (C1 D theta/e)^n * (C3 exp(C3) E e^{2 theta})^rho,
    (2.14)  B = max_{1<=j<=n} |b_j| A_j / A_n  (A_1 <= ... <= A_n),
    (2.15)  C0' = ln(C2 D omega / (C1 A_n)),
    (2.16)  ln|Lambda| > -112 * 2^n * C2 * C0' * D^2 * omega * ln(2 e B).

Kummer condition (1.5): [K(sqrt(alpha_1),...,sqrt(alpha_n)):K] = 2^n.
For distinct primes it holds automatically: no nonempty subset product is a
perfect square, which is exactly the criterion checked by
kummer_subset_verification (standard field theory: squarefree integers with
distinct primes give degree 2^n; equivalently the subset products are distinct
modulo Q*^2).
"""

import math

__all__ = [
    "two_sided_products",
    "linear_form",
    "kummer_subset_verification",
    "matveev_constants",
    "binomial_reduction_identity",
]


def binomial_reduction_identity():
    """Return (ok, lhs, rhs) for the direct algebra check

        C(x,2) = C(y,3)  <=>  3 x (x-1) = y (y-1) (y-2),

    verified symbolically via sympy:  6(C(x,2) - C(y,3)) is exactly
    3x(x-1) - y(y-1)(y-2) as a polynomial identity, so the two equations are
    equivalent (multiplying by the nonzero constant 6).
    """
    from sympy import symbols, binomial, expand

    x, y = symbols("x y")
    lhs = expand(6 * (binomial(x, 2) - binomial(y, 3)))   # 6C(x,2) - 6C(y,3)
    rhs = expand(3 * x * (x - 1) - y * (y - 1) * (y - 2))
    ok = (lhs == rhs) and (expand(3 * x * (x - 1)) != 0)
    return ok, lhs, rhs


def two_sided_products(x, y):
    """For the (2,3) curve C(x,2) = C(y,3) the cross-multiplied equality is
    3 x (x-1) = y (y-1) (y-2)  (each side equals 6 * a where a = C(x,2)).

    Returns (P, Q, factP, factQ) with P = 3x(x-1), Q = y(y-1)(y-2) and
    factP, factQ their exact prime factorizations (sympy.factorint).
    """
    from sympy import factorint

    P = 3 * x * (x - 1)
    Q = y * (y - 1) * (y - 2)
    return P, Q, factorint(P), factorint(Q)


def linear_form(factP, factQ):
    """Exhibit the linear form Lambda = sum_j b_j ln(alpha_j) attached to the
    two factorizations: b_j = v_{p_j}(P) - v_{p_j}(Q) over the union of primes,
    so Lambda = ln P - ln Q exactly (by unique factorization Lambda = 0 iff
    P = Q entry-by-entry, iff every b_j = 0).

    Returns (primes, bs, Lambda_float) with primes sorted ascending (so
    A_n = max A_j as Theorem 2.2 requires) and only the primes with b_j != 0
    kept (a zero coefficient contributes nothing and is dropped, reducing n).
    If P == Q then (primes, bs) = ([], []) and Lambda_float = 0.0.
    """
    allp = sorted(set(factP) | set(factQ))
    nonz = [(p, factP.get(p, 0) - factQ.get(p, 0)) for p in allp]
    nonz = [(p, b) for (p, b) in nonz if b != 0]
    primes = [p for (p, b) in nonz]
    bs = [b for (p, b) in nonz]
    Lambda = sum(b * math.log(p) for (p, b) in nonz)
    return primes, bs, Lambda


def kummer_subset_verification(primes):
    """Exact numeric verification of the Kummer condition (1.5) for the field
    K = Q and alpha_j = primes p_j:

        [Q(sqrt(p_1), ..., sqrt(p_n)) : Q] = 2^n

    Criterion used (standard field theory): the 2^n subset products
    prod_{j in S} p_j are distinct modulo Q*^2, equivalently every nonempty
    subset product is not a perfect square.  Both are checked exactly
    (math.isqrt and sympy.factorint).  Returns (ok: bool, detail: str).
    """
    from sympy import factorint

    n = len(primes)
    if len(set(primes)) != n:
        return False, f"primes not distinct: {primes}"
    parts = []
    for mask in range(1, 1 << n):
        prod = 1
        for j in range(n):
            if (mask >> j) & 1:
                prod *= primes[j]
        r = math.isqrt(prod)
        if r * r == prod:
            return False, f"subset mask {mask:b} product {prod} IS a perfect square"
        # squarefree part (for distinct primes this is prod itself, computed
        # anyway as the honest modulo-squares representative)
        sf = 1
        for p, e in factorint(prod).items():
            sf *= p ** (e % 2)
        parts.append(sf)
    if len(set(parts)) != len(parts):
        return False, "two subset products have the same squarefree part (linearly dependent mod squares)"
    return (
        True,
        f"verified: all {2**n - 1} nonempty subset products are non-squares, "
        f"{2**n} subset classes distinct mod Q*^2  =>  "
        f"[Q(sqrt({', '.join(map(str, primes))})):Q] = 2^{n} = {2**n}",
    )


def matveev_constants(primes, bs, theta=1.0, Eval=1.0):
    """Matveev 2000 Theorem 2.2 constants for Lambda = sum b_j ln p_j.

    primes: the alpha_j, sorted ascending by value (so A_j = ln p_j ascending,
            A_n = max), with nonzero integer coefficients bs (b_n != 0 by
            construction after linear_form drops zero coefficients).
    theta, Eval: theorem parameters; Theorem 2.2 fixes theta = E = 1.  Passing
            theta = 1/(2 - 2/(n e^{n+1})) reproduces the improved Theorem
            2.3(ii) case (K=Q, alpha_j positive integers, A_j = ln alpha_j).

    Raises ValueError if the form is empty (Lambda identically zero: B = 0 and
    ln(2eB) is undefined, and Theorem 2.2 requires Lambda != 0, b_n != 0).

    Returns a dict with n, rho, D, C3, C1, C2, A, Omega, omega, C0prime, B,
    exponent (the right-hand side of (2.16) as given: ln|Lambda| > exponent),
    and log10_bound = exponent / ln 10.
    """
    n = len(primes)
    if n == 0 or len(bs) != n:
        raise ValueError("empty multiplicative form: Lambda == 0 identically, "
                         "Theorem 2.2 does not apply (needs Lambda != 0, b_n != 0)")
    if not all(b != 0 for b in bs):
        raise ValueError("zero coefficients must be dropped before calling (n counts nonzero terms)")
    if any(p <= 1 for p in primes):
        raise ValueError("alpha_j must be integers > 1")

    rho = 1.0     # rank_R{ln alpha_j} for real logarithms is 1
    D = 1.0       # K = Q subset R: D_K = 1, kappa = 1, D = D_K/kappa = 1
    C3 = n / rho  # Theorem 2.2 sets C3 = n/rho

    ln2 = math.log(2)
    C1 = (1 + math.exp(-2 * n) / 148) * (n * ln2 + 2) * (1 + 1 / n) * C3
    C2 = 4 * (n + 1) * (6 + 5 / (n * ln2 + 2)) * math.exp(2 * n) * math.sqrt(n) * C3

    A = [math.log(p) for p in primes]       # = h(p_j) for primes (2.13)
    Omega = 1.0
    for a in A:
        Omega *= a
    # (2.5) with theta, Eval as given (Theorem 2.2: theta = E = 1)
    omega = Omega * (C1 * D * theta / math.e) ** n * (
        C3 * math.exp(C3) * Eval * math.exp(2 * theta)
    ) ** rho

    An = A[-1]                              # A_1 <= ... <= A_n, A_n = max
    C0prime = math.log(C2 * D * omega / (C1 * An))          # (2.15)
    B = max(abs(b) * a / An for (b, a) in zip(bs, A))       # (2.14), B >= 1 > 0
    exponent = -112 * 2 ** n * C2 * C0prime * D ** 2 * omega * math.log(2 * math.e * B)  # (2.16)

    return {
        "n": n, "rho": rho, "D": D, "C3": C3,
        "C1": C1, "C2": C2,
        "A": A, "Omega": Omega, "omega": omega,
        "C0prime": C0prime, "B": B,
        "exponent": exponent,
        "log10_bound": exponent / math.log(10),
    }