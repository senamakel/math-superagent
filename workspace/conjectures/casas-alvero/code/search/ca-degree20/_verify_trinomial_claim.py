"""Verify the trinomial structural claim used in DIVERSIFIED.md: for a
trinomial x^20 + a*x^k + b*x^m with 0 < k < m < 20 and a,b != 0, the failing
derivatives are exactly j = k and j = m. Check all five div2 trinomials and
report the failing-j set vs {k, m}."""
import importlib.util
import os
from sympy import Poly, QQ, symbols
x = symbols('x')
N = 20
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candidates')


def load(name):
    spec = importlib.util.spec_from_file_location('_c', os.path.join(DIR, name))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for an in dir(m):
        if an.startswith('_'): continue
        a = getattr(m, an)
        if callable(a) or isinstance(a,(str,bytes,type(None))): continue
        try: p = Poly(a, x)
        except Exception: continue
        if p.gens==(x,) and p.degree()==N and p.LC()==1: return p.set_domain(QQ)
    raise RuntimeError(name)


def failing_set(name):
    p = load(name)
    d = p; fails = []
    for j in range(1, N):
        d = d.diff()
        if p.gcd(d).degree() == 0: fails.append(j)
    return fails


# reconstruct exposed exponents from the module support (exact)
def exposed(name):
    p = load(name)
    # terms with nonzero coefficient that are not the x^20 leading term
    exp = []
    for (e,), c in p.terms():
        if e != 20 and c != 0:
            exp.append(e)
    return sorted(exp)


def main():
    allok = True
    for name in ['div2_trinomial_t1.py','div2_trinomial_t2.py','div2_trinomial_t3.py',
                 'div2_trinomial_t4.py','div2_trinomial_t5.py']:
        fails = failing_set(name)
        exp = exposed(name)
        ok = set(fails) == set(exp)
        allok = allok and ok
        print('%s: exposed exp=%s failing-j=%s  match=%s' % (
            name, exp, fails, 'YES' if ok else 'NO'))
    print('ALL TRINOMIAL CLAIMS HOLD' if allok else 'DISCREPANCY')
    return 0 if allok else 1


if __name__ == '__main__':
    raise SystemExit(main())
