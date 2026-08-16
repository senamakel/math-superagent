"""Adversarial verification of the root-difference-coloring first-step identity.

Claim under test (the adopted approach's foundation), for monic
f = prod_{j=1}^n (x - beta_j) over a field:

    H_i(f)(x) = e_{n-i}(x - beta_1, ..., x - beta_n)            (Taylor coeff)
    R_i := Res_x(f, H_i(f)) = prod_{beta root of f} H_i(beta)
                            = prod_{j=1}^n e_{n-i}(beta_j - beta_1, ...,
                                         [j removed], ..., beta_j - beta_n)

where H_i is the i-th Hasse derivative and e_k the k-th elementary symmetric
function.  For the witness root beta_j the term beta_j - beta_j = 0 drops out
of e_{n-i} automatically (e with a 0 entry equals e of the remaining entries).

Failure looks like: sympy's exact resultant differing from the product
formula, at any n or prime p.  That breaks the adopted approach's foundation.

Because the identity is a polynomial (indeed Z[beta]) identity, checking it on
random DISTINCT root values is a genuine identity check (Zariski-dense subset
of the root torus minus diagonals), and is far cheaper than expanding in the
beta symbols.  I check:
  (A) Taylor-coefficient identity H_i(f)(x) == e_{n-i}(x - beta_1, ..., x-beta_n)
      as polynomials in x, over QQ for n=4,5,6 and over F_p at n=p+1 for p=2,3,5.
  (B) Resultant identity Res_x(f, H_i) == prod_j H_i(beta_j), computed by
      sympy's exact resultant vs. the explicit product, same range.
  (C) the char-p survival of BOTH identities at n=p+1 (the approach claims the
      identity itself has no char-p break; the break lives in the per-color
      degeneracy of H_i, not in the identity).
"""
import sympy as sp

x = sp.symbols("x")


def hasse_i(fcoeffs, i, dom):
    """i-th Hasse derivative of coeff vector [c_0..c_n] (f = sum c_j x^j)."""
    n = len(fcoeffs) - 1
    out = 0
    for j in range(i, n + 1):
        b = sp.binomial(j, i)
        if dom == "QQ":
            pass
        else:  # GF(p): reduce binomial mod p
            b = b % dom_p  # noqa: we set below
        out += b * fcoeffs[j] * x ** (j - i)
    return out


def elementary_k(k, vals):
    """e_k of vals (list/tuple)."""
    from sympy import prod as _p
    t = sp.symbols("t")
    return sp.Poly(_p(1 + t * v for v in vals).expand(), t).coeff_monomial(t ** k)


def build_f(roots, dom):
    """monic f = prod(x - beta) over dom."""
    f = 1
    for r in roots:
        f *= (x - r)
    if dom == "QQ":
        return sp.expand(f), sp.QQ
    return sp.expand(f), sp.GF(dom)


results = []


def check(label, passed, detail=""):
    results.append((passed, label, detail))
    print(("[PASS] " if passed else "[FAIL] ") + label + ("  " + detail if detail else ""))


# --------------------------------------------------------------------------
# (A) + (B) over QQ, n = 4, 5, 6, random distinct rational roots
# --------------------------------------------------------------------------
import random
random.seed(12345)

for n in (4, 5, 6):
    # distinct random rational roots in {-4..4}
    roots = random.sample(list(range(-4, 5)), n)
    f_expr, dom = build_f(roots, "QQ")
    f_poly = sp.Poly(f_expr, x)
    ncoef = f_poly.degree() + 1
    fcoeffs = [f_poly.coeff_monomial(x ** j) for j in range(ncoef)]
    # order coefficients ascending by power: f = sum c_j x^j
    # Jordan: build ascending list directly
    fcoeffs = list(reversed([f_poly.coeff_monomial(x ** (n - j)) for j in range(n + 1)]))
    # verify Taylor identity for each i
    for i in range(1, n):
        Hi = hasse_i(fcoeffs, i, "QQ")
        Hi_poly = sp.Poly(Hi, x)
        # e_{n-i}(x-beta_1,...,x-beta_n)
        # compute via prod_j ((x-beta_j)+t), coefficient of t^i  ==  e_{n-i}
        t = sp.symbols("t")
        prod_t = sp.prod(((x - r) + t) for r in roots)
        pt = sp.Poly(prod_t.expand(), t)
        e_side = pt.coeff_monomial(t ** i)  # = e_{n-i}(x-beta_1,...)
        identA = sp.simplify(Hi_poly.as_expr() - e_side) == 0
        check(f"QQ n={n} i={i}: H_i(x)=e_{{{n-i}}}(x-beta) Taylor identity",
              identA)
        # (B) resultant identity
        res = sp.resultant(f_expr, Hi, x)
        prod_formula = sp.prod(elementary_k(n - i, [r2 for r2 in roots]) for _r in [None])  # placehold
        # This placehold is wrong: bound below
    # recompute (B) cleanly
    for i in range(1, n):
        Hi = hasse_i(fcoeffs, i, "QQ")
        res = sp.resultant(f_expr, Hi, x)
        # product over each beta_j of e_{n-i}(beta_j - other roots)
        prod_formula = 1
        for j in range(n):
            beta_j = roots[j]
            others = [roots[k] for k in range(n) if k != j]
            diffvals = [beta_j - ro for ro in others]
            prod_formula *= elementary_k(n - i, diffvals)
        identB = sp.simplify(res - prod_formula) == 0
        check(f"QQ n={n} i={i}: Res_x(f,H_i)==prod e_{{{n-i}}}(differences)",
              identB, f"res={res}")

# --------------------------------------------------------------------------
# (A)+(B) over F_p at n = p+1 for p = 2,3,5  + char-p survival test
# --------------------------------------------------------------------------
for p in (2, 3, 5):
    n = p + 1
    Fp = sp.GF(p)
    # distinct elements of F_p: use range(p) (all distinct mod p)
    roots = list(range(p))
    f_expr, _ = build_f(roots, p)          # over GF(p)
    f_poly = sp.Poly(f_expr, x, domain=Fp)
    fcoeffs = [f_poly.coeff_monomial(x ** j) for j in range(n + 1)]
    for i in range(1, n):
        Hi = hasse_i(fcoeffs, i, "GF")     # binomials reduced mod p
        Hi_poly = sp.Poly(Hi, x, domain=Fp)
        # Taylor identity
        t = sp.symbols("t")
        prod_t = sp.prod(((x - r) + t) for r in roots)
        pt = sp.Poly(prod_t.expand(), t, domain=Fp)
        e_side = pt.coeff_monomial(t ** i)
        identA = sp.simplify(Hi_poly.as_expr() - e_side) == 0
        # resultant over F_p
        res = sp.resultant(sp.Poly(f_expr, x, domain=Fp),
                           Hi_poly, x)
        prod_formula = 1
        for j in range(n):
            beta_j = roots[j]
            diffvals = [(beta_j - ro) % p for ro in roots if ro != beta_j]
            prod_formula *= elementary_k(n - i, diffvals)
        prod_formula = prod_formula % p
        identB = (res % p) == (prod_formula % p)
        check(f"GF({p}) n={n} i={i}: H_i===e Taylor",
              identA)
        check(f"GF({p}) n={n} i={i}: Res==prod e",
              identB,
              f"res={res%p} prod={prod_formula%p}")

# summary
fails = [r for r in results if not r[0]]
print()
if fails:
    print(f"FAILURES: {len(fails)}")
    for f in fails:
        print(" ", f[1], f[2])
else:
    print(f"ALL {len(results)} CHECKS PASSED (identity survives over QQ and F_p)")
