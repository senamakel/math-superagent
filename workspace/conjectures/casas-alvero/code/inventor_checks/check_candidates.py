"""Grounding checks for three new inventor candidates, exact sympy only.
Checks:
 (1) centroid claim: gcd(f, f^(n-1)) != 1  <=>  f(centroid) = 0  (centroid = -a_1/n),
     the engine of candidate 'centroid-recursion'.
 (2) e_m-vanishing: if e_1..e_{n-1}(d_1..d_{n-1}) all vanish then all d_j = 0,
     the engine of candidate 'convex-difference-covering'.
 (3) interior-root coverage: for a non-vertex root beta*, which derivative levels i
     does it cover (H_i(f)(beta*) = 0), on a small squarefree example.
"""
from sympy import symbols, Poly, gcd, Matrix, expand, prod

x = symbols('x')

# ---- (1) centroid claim -------------------------------------------------
def centroid_claim(n, seed=7):
    from sympy import randpoly
    a = symbols('a1:'+str(n))
    # monic f = x^n + a1 x^{n-1} + ... + an ; centroid = -a1/n
    # test the logical equivalence on random numeric specialisations
    from random import Random
    rnd = Random(seed)
    for _ in range(200):
        vals = [rnd.randint(-20,20) for _ in range(n)]
        subs = dict(zip(a, vals))
        coeffs = [1] + vals
        f = Poly(sum(coeffs[k]*x**(n-k) for k in range(n+1)), x)
        fd = f.diff(x, n-1)
        shared = gcd(f, fd).degree() > 0
        centroid = -vals[0]/n
        f_at_c = f.eval(centroid)
        if shared != (f_at_c == 0):
            return False, (vals, shared, f_at_c)
    return True, None

for n in (3,4,5,6):
    ok, wit = centroid_claim(n)
    print(f"(1) centroid claim n={n}: {ok}", "" if ok else wit)

# ---- (2) e_m vanishing ---------------------------------------------------
def e_m_vanish(n):
    d = symbols('d1:'+str(n))  # n-1 difference vectors, n = len
    from sympy import symbols as S
    dv = list(d)
    # polynomial prod_{j}(t + d_j) = t^{m} + e1 t^{m-1} + ... ; all e vanish => t^m
    t = S('t')
    P = prod(t + dd for dd in dv)
    P = Poly(P, t)
    m = len(dv)
    coeffs = [P.coeff_monomial(t**(m-k)) for k in range(1, m+1)]  # e1..em
    # solve e1..em = 0
    sol = {}
    try:
        from sympy import solve
        sol = solve(coeffs, dv, dict=True)
    except Exception as e:
        print(f"(2) e_m vanish n={n}: solve failed {e}")
        return
    # every solution has all d_j = 0
    allzero = all(all(v == 0 for v in s.values()) for s in sol)
    print(f"(2) e_m vanish n={n}: all-zero-only = {allzero}   ({len(sol)} solution(s))")
    for s in sol[:3]:
        print("    ", s)

for n in (3,4,5):
    e_m_vanish(n)

# ---- (3) interior-root coverage -----------------------------------------
def interior_coverage():
    # f = (x^2 - 1)(x - 2)(x - 3) = roots -1,1,2,3 ; centroid not a root here,
    # just measure coverage sets.  Interior (non-vertex) root on the real line: 1
    # (between -1 and 2).  For each beta in {-1,1,2,3}, find i with H_i(f)(beta)=0.
    roots = [-1,1,2,3]
    f = Poly(prod(x-r for r in roots), x)
    n = 4
    from sympy import binomial
    def H(f, i):
        # Hasse derivative: sum_{k>=i} C(k,i) a_k x^{k-i}
        coeffs = f.all_coeffs()  # leading first
        deg = f.degree()
        terms = {}
        for k in range(deg+1):
            a_k = coeffs[deg-k]  # coefficient of x^k
            if k >= i:
                terms[k-i] = terms.get(k-i, 0) + binomial(k, i)*a_k
        return Poly(terms, x) if terms else Poly(0, x)
    for beta in roots:
        covered = [i for i in range(1, n) if H(f, i).eval(beta) == 0]
        print(f"(3) root {beta}: covers derivative levels {covered}")

interior_coverage()
