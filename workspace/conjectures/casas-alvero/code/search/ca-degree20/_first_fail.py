"""First-failing-j reporter for the diverse degree-20 families.

Reads each candidate module in candidates/div_d*.py, loads its polynomial,
and reports: construction family, score, and the FIRST j in 1..19 with
deg(gcd(f, f^(j))) == 0 over QQ. The scoring/gcd logic replicates score.py
exactly (sympy Poly.gcd over QQ), so the first-failing-j it reports is the
one the canonical scorer's decision logic sees.
"""
import glob
import importlib.util
import os

from sympy import Poly, QQ, symbols

x = symbols('x')
N = 20

FAMILY = {
    'div_d1': 'TRINOMIAL',
    'div_d2': 'CYCLOTOMIC',
    'div_d3': 'CHEBYSHEV',
    'div_d4': 'ROOT-MULTISET',
    'div_d5': 'FACTORED f=(x-r)^m g',
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
    raise RuntimeError("no monic deg-20 poly in %s" % path)


def first_fail(poly):
    d = poly
    pas = []
    for j in range(1, N):
        d = d.diff()
        if poly.gcd(d).degree() > 0:
            pas.append(j)
        else:
            return j, len(pas)
    return None, len(pas)


def main():
    rows = []
    for path in sorted(glob.glob('candidates/div_d*.py')):
        base = os.path.basename(path)
        # filename prefix is div_d1 / div_d2 / div_d3 / div_d4 / div_d5
        famk = base[:6]  # "div_d1"
        fam = FAMILY.get(famk, base)
        poly = load(path)
        ff, cnt = first_fail(poly)
        rows.append((base, fam, cnt, ff))
    rows.sort(key=lambda r: r[2])
    print(f"{'file':40s} {'family':22s} {'score':>5s} {'first_fail':>9s}")
    for base, fam, cnt, ff in rows:
        print(f"{base:40s} {fam:22s} {cnt:5d} {str(ff):>9s}")

    # ---- distribution of first-failing j, by family ----
    print("\n=== first-failing-j distribution (which j first breaks) ===")
    hist = {}
    for _, fam, _c, ff in rows:
        hist[(fam, ff)] = hist.get((fam, ff), 0) + 1
    for (fam, ff), n in sorted(hist.items()):
        print(f"  family={fam:20s} first_fail j={str(ff):>4s}: {n}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
