"""Exploratory helper: compute score and first-failing j for candidate polys.

Not the scorer (score.py is the canonical one). This is a scratch companion
to *choose* diverse candidate instances before writing the module files. It
reports, for each candidate polynomial: construction label, score, and the
first j in 1..19 where deg(gcd(f, f^(j)))==0.
"""
import sympy
from sympy import Poly, symbols

x = symbols('x')
N = 20


def analyze(label, f):
    f = Poly(f, x).set_domain(sympy.QQ)
    assert f.degree() == N and f.LC() == 1
    passing = []
    failing = []
    d = f
    for j in range(1, N):
        d = d.diff()
        if f.gcd(d).degree() > 0:
            passing.append(j)
        else:
            failing.append(j)
    first_fail = failing[0] if failing else None
    return (label, len(passing), first_fail, passing, failing)


def try_many():
    cases = {}

    # ---- Family A: trinomials (3 terms, all in {x^20, x^k, x^m}) ----
    cases['trinomial_a'] = x**20 - 3*x**3 - 2*x**2
    cases['trinomial_b'] = x**20 - 3*x**14 - 2*x**2
    cases['trinomial_c'] = x**20 - x**11 - x**9
    cases['trinomial_d'] = x**20 + x**5 + x**4
    cases['trinomial_high'] = x**20 - x**18 - x**17

    # ---- Family B: cyclotomic-derived ----
    phi20 = sympy.cyclotomic_poly(20, x)          # degree 8
    cases['cyclo_shift'] = (x-1)**12 * phi20       # degree 20
    cases['cyclo_x20m1'] = x**20 - 1               # degree 20, all simple roots
    cases['cyclo_roots_unity_repeat'] = (x**4 - 1)**5   # deg 20
    cases['cyclo_phi20_alone'] = phi20 * (x-1)**12     # same but root 1 mult 12

    # ---- Family C: Chebyshev-derived ----
    t20 = sympy.chebyshevt(20, x)
    cases['chebyshev_T20'] = t20
    cases['chebyshev_shift'] = (x-1)**12 * sympy.chebyshevt(8, x)  # deg 20
    cases['chebyshev_x19T'] = x**19 - sympy.chebyshevt(19, x)      # hmm not monic deg, skip
    cases['chebyshev_perturb'] = sympy.chebyshevt(20, x) - 1

    # ---- Family D: prescribed root multiset (factorized) ----
    cases['roots_14_6'] = x**14 * (x-1)**6
    cases['roots_13_7'] = x**13 * (x-2)**7
    cases['roots_12_5_3'] = x**12 * (x-1)**5 * (x+1)**3
    cases['roots_9_9_2'] = (x-1)**9 * (x-2)**9 * (x-3)**2
    cases['roots_two_mult10_plus_d'] = (x-1)**10 * (x-2)**10 * (x-3)**0

    # ---- Family E: f = (x-r)^m g with g covering higher derivatives ----
    cases['factored_g1'] = x**13 * ((x-1)**6 + 0)      # = x^13 (x-1)^6
    cases['factored_g2'] = x**13 * (x**6 - 2)          # g = x^6-2
    cases['factored_g3'] = x**14 * (x**6 - 1)          # g=x^6-1
    cases['factored_g4'] = (x-1)**14 * ((x-2)**6 - 0)  # = (x-1)^14 (x-2)^6
    cases['factored_g5'] = x**13 * (x-1)**7

    rows = []
    for label, f in cases.items():
        try:
            rows.append(analyze(label, f.expand()))
        except Exception as e:
            rows.append((label, 'ERR', str(e), None, None))
    for label, score, first, passing, failing in rows:
        print(f"{label:24s} score={score!s:4s} first_fail={first!s:5s} "
              f"passing={passing}")
    return rows


if __name__ == "__main__":
    try_many()
