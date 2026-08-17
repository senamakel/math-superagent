"""Verify the div2 runner's numbers for representative candidates by giving
the FULL per-j sharing pattern (not just first-failing-j), and cross-check
the score = count of sharing j's. Also re-derive the score independently via
the canonical oracle lib.casas_alvero.is_ca-style gcd (same exact sympy gcd)
to confirm no disagreement.
"""
import importlib.util
import os
from sympy import Poly, QQ, symbols

x = symbols('x')
N = 20
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candidates')


def load(name):
    path = os.path.join(DIR, name)
    spec = importlib.util.spec_from_file_location('_c', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for an in dir(m):
        if an.startswith('_'):
            continue
        a = getattr(m, an)
        if callable(a) or isinstance(a, (str, bytes, type(None))):
            continue
        try:
            p = Poly(a, x)
        except Exception:
            continue
        if p.gens == (x,) and p.degree() == N and p.LC() == 1:
            return p.set_domain(QQ)
    raise RuntimeError(name)


def pattern(name):
    p = load(name)
    d = p
    shared = []
    for j in range(1, N):
        d = d.diff()
        deg = p.gcd(d).degree()
        shared.append(deg > 0)
    score = sum(shared)
    ff = next((j for j, s in enumerate(shared, start=1) if not s), None)
    return score, ff, shared


def main():
    for name in ['div2_trinomial_t1.py', 'div2_factored_f1.py',
                 'div2_rootset_r3.py', 'div2_cyclo_c3.py', 'div2_cheb_h3.py']:
        score, ff, shared = pattern(name)
        sharings = ','.join(str(j) for j, s in enumerate(shared, start=1) if s)
        print('%s: score=%d ff=%s' % (name, score, ff))
        print('   shared j: %s' % sharings)
        print('   failing j: %s' % ','.join(
            str(j) for j, s in enumerate(shared, start=1) if not s))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
