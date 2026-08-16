"""Detailed pass/fail vectors for the genuinely non-trivial diverse candidates.

Prints, for chosen candidates: the full set of j in 1..19 where
deg(gcd(f, f^(j)))>0 (shares) vs where it fails, with the exact factorized
form of f, so cross-root sharing is visible.
"""
import importlib.util

from sympy import Poly, QQ, symbols, factor

x = symbols('x')
N = 20

CANDIDATES = {
    'div_d3_cheb_even_shape': 'candidates/div_d3_cheb_even_shape.py',
    'div_d1_trinomial_d':     'candidates/div_d1_trinomial_d.py',
    'div_d1_trinomial_a':     'candidates/div_d1_trinomial_a.py',
    'div_d4_roots_9_9_2':     'candidates/div_d4_roots_9_9_2.py',
    'div_d5_factored_x14_g_x6m1': 'candidates/div_d5_factored_x14_g_x6m1.py',
    'div_d5_factored_x13_g_x7m2': 'candidates/div_d5_factored_x13_g_x7m2.py',
}


def load(path):
    spec = importlib.util.spec_from_file_location("_cand", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name in dir(mod):
        if name.startswith('_'):
            continue
        attr = getattr(mod, name)
        if callable(attr) or isinstance(attr, (str, bytes, type(None))):
            continue
        try:
            p = Poly(attr, x)
        except Exception:
            continue
        if p.gens == (x,) and p.degree() == N and p.LC() == 1:
            return p.set_domain(QQ)
    raise RuntimeError("no poly in %s" % path)


def vector(poly):
    d = poly
    share, fail = [], []
    for j in range(1, N):
        d = d.diff()
        (share if poly.gcd(d).degree() > 0 else fail).append(j)
    return share, fail


for label, path in CANDIDATES.items():
    p = load(path)
    share, fail = vector(p)
    print(f"\n=== {label} ===")
    print("  factorized:", factor(p.as_expr()))
    print("  shares j:", share)
    print("  fails  j:", fail)
    # expand the factorized form to expose any binomial collapse
    expr = p.as_expr()
    # count nonzero coefficients below degree 20
    coeffs = Poly(expr, x).all_coeffs()  # leading..constant
    nz = [i for i, c in enumerate(reversed(coeffs)) if c != 0]  # exponent of nonzero
    print("  nonzero exponents below 20:", [e for e in nz if e < 20])
