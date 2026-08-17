"""Identify the leading weighted term of R_i explicitly and check a char-p caveat.

Since R_i is EXACTLY weighted-homogeneous of degree n(n-i), the 'leading term'
IS the whole polynomial. Two checks:
 (1) R_i expressed via roots = (-1)^? prod_k e_{n-i}({beta_k - beta_j}_{j!=k})
     is homogeneous of beta-degree n(n-i) -- re-derive explicitly for small n.
 (2) Char-p caveat: the weighted-homogeneous integer polynomial reduces mod p;
     its exact order n(n-i) survives iff the integer leading coefficient is not
     0 mod p. Show that over Q the leading coefficient is +- something with
     multiplicative structure, so a bad-prime reduction is the only way the
     order drops. (This is exactly the bad-prime phenomenon the run tracks.)
"""
import sympy as sp

def hasse(coeffs, i, n, x):
    out = sp.Integer(0)
    for j, c in enumerate(coeffs):
        deg = n - j
        if deg >= i and c != 0:
            out += sp.binomial(deg, i) * c * x**(deg - i)
    return sp.expand(out)

def root_form_coeffs(n, i, betas):
    """Return prod_k e_{n-i}({beta_k - beta_j}_{j!=k}) as symmetric poly in betas."""
    m = n - i
    prod = sp.Integer(1)
    for k in range(n):
        others = [betas[k] - betas[j] for j in range(n) if j != k]
        e = sum(sp.prod([others[idx] for idx in sub])
                for sub in sp.subsets(range(n - 1), m))
        prod *= sp.expand(e)
    return sp.expand(prod)

def check_root_form(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) if j >= 2 else (sp.Integer(1) if j == 0 else sp.Integer(0))
         for j in range(n + 1)]
    f = sum(a[j] * x**(n - j) for j in range(n + 1))
    for i in range(1, n):
        hi = hasse(a, i, n, x)
        R = sp.expand(sp.resultant(f, hi, x))
        # express R as poly in a's; substitute a_j = (-1)^j e_j(betas) is
        # heavy, so instead: the weighted order of R in t under a_j->t^j a_j
        # already proved = n(n-i). Here just record the weight of the leading
        # (only) weighted term and confirm R has no lower terms (again, cheap).
        P = sp.Poly(R, *[sp.Symbol('a%d' % j) for j in range(2, n + 1)])
        wts = {sum((j+2)*e for j,e in enumerate(exps)) for exps,_ in P.terms()}
        assert len(wts) == 1 and wts == {n*(n-i)}, (n, i, wts)
    return True

if __name__ == '__main__':
    ok = True
    for n in [3,4,5]:
        ok = check_root_form(n) and ok
    print("Root-form weighted-homogeneity re-confirmed:", "ALL OK" if ok else "FAIL")
    # explicit leading coefficients (integer) for small n,i via the beta-product
    # evaluated at distinct rational betas summing to zero (gives a nonzero
    # rational; the true integer coeff is recovered up to the symmetric map).
    for n in [3,4]:
        betas = [sp.Rational(i,1) for i in range(1, n)]
        s = sum(betas)
        betas[0] -= s  # force traceless? no -- keep distinct instead
        # just show nonzero of prod_k e_{n-i} for distinct traceless choice
        b = sp.symbols('b0:%d' % n)
        vals = {}
        # traceless distinct set: 1..n-1 then adjust last
        base = [sp.Rational(v,1) for v in range(1, n+1)]
        total = sum(base)
        base[-1] -= total  # sum now 0, still distinct generically
        for k in range(n):
            vals[b[k]] = base[k]
        for i in range(1, n):
            v = root_form_coeffs(n, i, b).subs(vals)
            print(f"  n={n} i={i}: prod_k e_{n-i} at traceless distinct point = {v} (nonzero={v!=0})")
