"""Verify the length formula |QQ[a_2..a_n]/(R_1..R_{n-1})| = n^{n-2}.

Compare three quantities for n=3,4,5:
  (a) the true quotient length (Gröbner/sympy), 
  (b) prod_i ord_0(R_i) / n!  where ord_0 is the WEIGHTED order (=n(n-i)),
  (c) prod_i (standard m-adic order of R_i).
f = x^n + sum_{j=2}^n a_j x^{n-j} monic traceless, R_i = Res_x(f, H_i f).
"""
import sympy as sp

def built(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) for j in range(n + 1)]
    coeffs = [sp.Integer(1)] + [sp.Integer(0)] + [a[j] for j in range(2, n + 1)]
    # coeffs[j] = coeff of x^(n-j)
    f = sum(coeffs[j] * x ** (n - j) for j in range(n + 1))
    R = []
    for i in range(1, n):
        hi = sum(sp.binomial(n - j, i) * coeffs[j] * x ** (n - j - i)
                 for j in range(n + 1) if (n - j) >= i)
        R.append(sp.resultant(f, hi, x))
    return a, R

def weighted_order(poly, t, a):
    """t-exponent of poly under a_j -> t^j a_j."""
    Rt = sp.expand(poly.subs({a[j]: a[j] * t ** j for j in range(2, len(a))}))
    P = sp.Poly(Rt, t)
    return P.terms()[0][0][0]

def std_order(poly, a):
    """standard m-adic order = total degree of lowest-homogeneous part."""
    P = sp.Poly(poly, *[a[j] for j in range(2, len(a))])
    return min(sum(e) for (e, c) in P.terms())

def quotient_length(n, a, R):
    """Compute dim_Q QQ[a_2..a_n]/I via Groebner / quotient basis."""
    ring_vars = [a[j] for j in range(2, n + 1)]
    Rpol = [sp.Poly(r, *ring_vars) for r in R]
    G = sp.groebner(Rpol, *ring_vars, order='lex')
    # quotient basis: monomials not in the leading ideal of G (0-dim)
    # simpler: construct quotient ring and use sympy's Groebner ideal with
    # a monomial count via normalForm of all monomials up to degree bound.
    import itertools
    # Find all monomials not reducible to 0 mod G, up to a cap degree.
    deg_cap = 4*n*n
    mono = []
    for deg in range(0, deg_cap + 1):
        for es in itertools.product(range(deg+1), repeat=n-1):
            if sum(es) != deg:
                continue
            m = sp.Mul(*[v**e for v, e in zip(ring_vars, es)])
            if G.reduce(m) == 0:
                mono.append(m)
    return len(mono)

for n in [3, 4, 5]:
    a, R = built(n)
    t = sp.symbols('t')
    wo = [weighted_order(r, t, a) for r in R]
    so = [std_order(r, a) for r in R]
    from math import factorial
    pred_b = 1
    for o in wo: pred_b *= o
    pred_b //= factorial(n)
    pred_c = 1
    for o in so: pred_c *= o
    L = quotient_length(n, a, R)
    print(f"n={n}: weighted orders={wo} std orders={so}")
    print(f"   prod(weighted)/n! = {pred_b}   prod(std) = {pred_c}   actual length = {L}")
