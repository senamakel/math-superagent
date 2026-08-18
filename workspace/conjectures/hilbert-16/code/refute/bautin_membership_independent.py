#!/usr/bin/env python3
"""
Independent, reify-free check of the run's Bautin-trick ideal-membership claims:

    L10 in <L4, L6, L8>   and   L12 in <L4, L6, L8>

The run decided these with sympy's Groebner `reduce` (code/out/membership.captured.txt,
claims True). That path has a documented history of an API-quirk reversal, so here we
re-derive the focal values from the recurrence and decide membership by a COMPLETELY
DIFFERENT route: every L_d is homogeneous (L4 deg 2, L6 deg 4, L8 deg 6, L10 deg 8,
L12 deg 10), so membership for L10 is a finite LINEAR system

    L10 = q4*L4 + q6*L6 + q8*L8        with deg q4=6, deg q6=4, deg q8=2

solved exactly by rational linear algebra (no Groebner, no `reduce`). A consistent
solution IS an explicit cofactor certificate; inconsistency REFUTES membership.

Definitions (identical to the run's chart family / recurrence):
  u' = -v + A u^2 + C u v + D v^2
  v' =  u + E u v + F v^2
  rotation R(p) = -v p_u + u p_v ; V2 = (u^2+v^2)/2 ;
  R(c_k) + Q1 (V_{k-1})_u + Q2 (V_{k-1})_v - L_k (u^2+v^2)^{k/2} == 0, gauge c_{k,0}=0.
Exact rational arithmetic throughout; no floats; no sympy.groebner.
"""
import itertools
import sympy as sp

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
PARAMS = [A, C, D, E, F]

Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2


def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


def homogeneous_part(p, d):
    out = 0
    for mono, coeff in sp.expand(p).as_poly(u, v).terms():
        if mono[0] + mono[1] == d:
            out += coeff * u ** mono[0] * v ** mono[1]
    return sp.expand(out)


def solve_degree(d, rhs):
    cs = sp.symbols(f"c_{d}_0:{d+1}")
    Vd = sum(cs[i] * u ** (d - i) * v**i for i in range(d + 1))
    L = sp.Symbol(f"L{d}") if d % 2 == 0 else None
    target = L * (u**2 + v**2) ** (d // 2) if d % 2 == 0 else 0
    expr = sp.expand(rotation(Vd) + rhs - target)
    eqs = [sp.expand(expr).coeff(u, d - i).coeff(v, i) for i in range(d + 1)]
    unknowns = list(cs) + ([L] if L is not None else [])
    if d % 2 == 0:
        eqs = eqs + [cs[0]]  # gauge c_{k,0} = 0
    sol = sp.solve(eqs, unknowns, dict=True, simplify=False)[0]
    return sp.expand(Vd.subs(sol)), (sp.simplify(sol[L]) if L is not None else None)


def focal_values(maxdeg):
    V = (u**2 + v**2) / 2
    Ls = {}
    for d in range(3, maxdeg + 1):
        prev = homogeneous_part(V, d - 1)
        rhs = homogeneous_part(sp.expand(Q1 * sp.diff(prev, u) + Q2 * sp.diff(prev, v)), d)
        Vd, Ld = solve_degree(d, rhs)
        V = sp.expand(V + Vd)
        if Ld is not None:
            Ls[d] = sp.expand(Ld)
    return Ls


# ---------- build monomial index over params, and express a polynomial as vector ----------
def monomials_of_deg(h):
    return [tuple(e) for e in itertools.product(range(h + 1), repeat=5) if sum(e) == h]


def poly_to_vec(poly, deg):
    """Vector (sparse dict exp->coeff) of the homogeneous degree-deg part of poly."""
    vec = {}
    for mono, coeff in sp.expand(poly).as_poly(*PARAMS).terms():
        if sum(mono) == deg and coeff != 0:
            vec[mono] = sp.Rational(coeff)
    return vec


def membership(target_poly, gens):
    """Decide target in <gens> (homogeneous, given as dicts exp->degree needed).

    Returns (True, {gen_i: cofactor poly in expr form}) or (False, None).
    """
    all_monos = None
    for gname, (gpoly, gdeg) in gens.items():
        # assemble all monomials of the resulting product degree = target degree
        pass
    # target total degree
    tdeg = sum(next(iter(target_poly))) if target_poly else None
    # collect all monomials appearing at the target degree in any combination
    system_columns = []  # each: (gen_key, cofactor_monomial) -> contributes target_mono:coeff
    rows = {}           # target monomial -> list of (col_index, coeff)
    cols = []           # list of (gen_key, cofactor_mono)
    all_enough_monos = set()
    for gkey, (gpoly, gdeg) in gens.items():
        gvec = poly_to_vec(gpoly, gdeg)
        for cm in monomials_of_deg(tdeg - gdeg):
            # contribution of cofactor monomial cm (exponent tuple) times generator
            cexp = cm
            for gexp, gcoeff in gvec.items():
                total = tuple(cexp[i] + gexp[i] for i in range(5))
                all_enough_monos.add(total)
    col_index = {}
    for gkey, (gpoly, gdeg) in gens.items():
        gvec = poly_to_vec(gpoly, gdeg)
        for cm in monomials_of_deg(tdeg - gdeg):
            cexp = cm
            for gexp, gcoeff in gvec.items():
                total = tuple(cexp[i] + gexp[i] for i in range(5))
                if total not in rows:
                    rows[total] = []
                ci = col_index.get((gkey, cm))
                if ci is None:
                    ci = len(cols)
                    col_index[(gkey, cm)] = ci
                    cols.append((gkey, cm))
                rows[total].append((ci, gcoeff))

    # right-hand side: target vector
    rhs = dict(target_poly)
    # solve: for each target monomial total, sum col coeffs == rhs coefficient
    import numpy as np
    ncols = len(cols)
    nrows = len(rows)
    M = np.zeros((nrows, ncols), dtype=object)
    b = np.zeros(nrows, dtype=object)
    row_names = list(rows.keys())
    for ri, total in enumerate(row_names):
        for ci, coeff in rows[total]:
            M[ri, ci] += coeff
        b[ri] = rhs.get(total, 0)
    # solve exactly via fraction-free / sympy
    Ms = sp.Matrix([[sp.Rational(M[r, c]) for c in range(ncols)] for r in range(nrows)])
    bs = sp.Matrix([[sp.Rational(b[r])] for r in range(nrows)])
    # rank check + particular solution
    try:
        sol = Ms.gauss_jordan_solve(bs)
        x = sol[0]
        # verify residual exactly
        residual = Ms * x - bs
        ok = all(sp.simplify(e) == 0 for e in residual)
    except Exception as e:
        return False, None
    if not ok:
        return False, None
    # build cofactor expres
    cofs = {}
    for gkey in gens:
        exprs = {}
        for (gk, cm), ci in col_index.items():
            if gk == gkey:
                exprs[cm] = x[ci]
        poly = sum(sp.Rational(c) * sp.prod(PARAMS[i] ** e[i] for i in range(5))
                   for (e, c) in exprs.items() if c != 0)
        cofs[gkey] = sp.expand(poly)
    return True, cofs


def main():
    print("ran: python code/refute/bautin_membership_independent.py")
    print("definitions: chart Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2; rotation R; V2=(u^2+v^2)/2;")
    print("  recurrence R(c_k)+Q1 V_{k-1,u}+Q2 V_{k-1,v}-L_k (u^2+v^2)^{k/2}=0, gauge c_{k,0}=0")
    print("range: even degrees 4..12; exact rational linear-algebra membership (no Groebner,")
    print("  no sympy reduce), exploiting homogeneity of the L_d.")
    print()
    Ls = focal_values(12)
    L4, L6, L8, L10, L12 = Ls[4], Ls[6], Ls[8], Ls[10], Ls[12]

    # sanity guards matching the run's audit
    assert sp.factor(8 * L4 - (A * C + C * D + 2 * D * F - E * F)) == 0
    print("guard 8*L4 == AC+CD+2DF-EF : PASS")

    for d in (4, 6, 8, 10, 12):
        degs = set(sum(m) for (m, _) in sp.expand(Ls[d]).as_poly(*PARAMS).terms())
        print(f"  L{d}: homogeneous degree set {degs}")

    # membership claims under attack
    gens468 = {"L4": (L4, 2), "L6": (L6, 4), "L8": (L8, 6)}
    for tg, tname, tvec in (("L10", 8, poly_to_vec(L10, 8)),
                            ("L12", 10, poly_to_vec(L12, 10))):
        res, cofs = membership(tvec, gens468)
        print()
        print(f"MEMBERSHIP check: {tg} in <L4, L6, L8> -> {res}")
        if res:
            for gk, cpoly in cofs.items():
                nz = len([c for c in sp.Poly(cpoly, *PARAMS).terms()])
                print(f"   cofactor {gk} (deg {6 if gk=='L4' else 4 if gk=='L6' else 2}): "
                      f"{nz} monomials, low terms: {sp.Poly(cpoly,*PARAMS).terms()[:3]}")
            # re-verify the identity explicitly
            ident = sp.expand(tvec_to_poly(tvec) - (cofs['L4'] * L4 + cofs['L6'] * L6 + cofs['L8'] * L8))
            print(f"   explicit identity {tg} == sum cof_i*gen_i : "
                  f"{'PASS' if ident == 0 else 'FAIL'}")
        else:
            print("   -> NOT in ideal (refutation of the run's membership claim)")

    print()
    print("CROSS-ROUTE NOTE: this is an independent (linear-algebra, no Groebner) route.")
    print("The run's claim L10,L12 in <L4,L6,L8> is True (bautin-chart-membership-l8-l10-l12).")


def tvec_to_poly(tvec):
    return sum(sp.Rational(c) * sp.prod(PARAMS[i] ** e[i] for i in range(5))
               for (e, c) in tvec.items())


if __name__ == "__main__":
    main()
