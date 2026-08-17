"""Sanity-check the planned div2 candidate constructions (robust version).

For each: build the polynomial, confirm it is a monic degree-20 rational (the
scorer's contract; all exact sympy facts), and get an exact LOWER BOUND on the
number of distinct complex roots from the exact QQ factorisation:
  distinct_roots >= (#distinct linear factors) + (#nonlinear irreducible
  factors with their multiplicity collapsed to a contribution of >=1 each,
  and each nonlinear irreducible of degree d>=2 contributes at least 2
  distinct roots, degree d>=3 at least 3 -- but we only need >=3, so we count
  each distinct nonlinear irreducible as one extra root).
This is an exact guard: no floats anywhere. A monic degree-20 rational with
>=3 distinct roots passes.
"""
from sympy import symbols, Poly, QQ, chebyshevt, cyclotomic_poly
x = symbols('x')


def build(name):
    if name == 'trinomial_1':
        return x**20 - 3*x**7 - 2*x**3
    if name == 'trinomial_2':
        return x**20 + x**13 - 5*x**5
    if name == 'trinomial_3':
        return x**20 - x**11 + 2*x**6
    if name == 'trinomial_4':
        return x**20 - 5*x**15 + 3*x**9
    if name == 'trinomial_5':
        return x**20 + 2*x**17 - 4*x**2
    if name == 'rootset_1':
        return x**16*(x-1)**2*(x-2)**2
    if name == 'rootset_2':
        return (x-1)**15*(x-2)**3*(x-3)**2
    if name == 'rootset_3':
        return x**8*(x-1)**7*(x+1)**5
    if name == 'factored_1':
        return (x-1)**15*(x**5 - 2)
    if name == 'factored_2':
        return (x+2)**14*(x**6 - x - 1)
    if name == 'factored_3':
        return (x-1)**16*(x**4 - 3*x**2 + 1)
    if name == 'factored_4':
        return x**15*(x**5 - x - 1)
    if name == 'cyclo_1':
        return (x**5 - 1)**4
    if name == 'cyclo_2':
        return (x**10 - 1)**2
    if name == 'cyclo_3':
        return (x-1)**12*cyclotomic_poly(20, x-1)
    if name == 'cheb_1':
        return chebyshevt(10, x)**2/2**18
    if name == 'cheb_2':
        return chebyshevt(20, x-1)/2**19
    if name == 'cheb_3':
        return chebyshevt(10, x-1)**2/2**18
    raise KeyError(name)


def distinct_roots_lower_bound(poly):
    """Exact lower bound on #distinct complex roots from QQ factor_list."""
    content, fac = poly.factor_list()
    count = 0
    for base, mult in fac:
        if base.degree() == 1:
            count += 1          # one distinct rational root
        else:
            count += 2          # an irreducible of degree>=2 has >=2 distinct roots
    return count


def main():
    names = ['trinomial_1','trinomial_2','trinomial_3','trinomial_4','trinomial_5',
             'rootset_1','rootset_2','rootset_3',
             'factored_1','factored_2','factored_3','factored_4',
             'cyclo_1','cyclo_2','cyclo_3',
             'cheb_1','cheb_2','cheb_3']
    allok = True
    for nm in names:
        expr = build(nm)
        poly = Poly(expr, x).set_domain(QQ)
        monic = poly.LC() == 1
        deg = poly.degree()
        rational = all(c.is_rational for c in poly.all_coeffs())
        lb = distinct_roots_lower_bound(poly)
        ok = monic and deg == 20 and rational and lb >= 3
        allok = allok and ok
        print(f"{nm:14s} monic={monic} deg={deg} rational={rational} "
              f"distinct-roots(>=)={lb} {'OK' if ok else 'FAIL'}")
    print("ALL PLANS VALID" if allok else "SOME PLANS INVALID")
    return 0 if allok else 1


if __name__ == '__main__':
    raise SystemExit(main())
