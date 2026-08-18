#!/usr/bin/env python3
"""Focal-value monomial counts, gcd-clearing denominators, p-adic valuations,
and Bautin-trick cofactor counts, for the chart family degree 14.

Family (chart): quadratic homogeneous part
    Q1 = A u^2 + C u v + D v^2 ,   Q2 = E u v + F v^2 ,
linear part = rotation rot(p) = -v p_u + u p_v, V2 = (u^2+v^2)/2.
Even-degree radial obstructions L_d (d-th focal value) from
    rot(c_k) + Q1 (V_{k-1})_u + Q2 (V_{k-1})_v - L_k (u^2+v^2)^{k/2} ≡ 0 .

For each even degree d in (4, 6, 8, 10, 12, 14) this prints:
  (a) the monomial count of L_d,
  (b) the gcd-clearing denominator of L_d = ilcm of the denominators of all
      rational coefficients (so that denom * L_d is an integer polynomial),
  (c) the 2-valuation and 3-valuation of that denominator,
and for the Bautin-trick memberships L10, L12, L14 in <L4, L6, L8>:
  (d) the cofactor monomial counts (q1, q2, q3) and their total, for a
      VERIFIED decomposition  L_d = q1*L4 + q2*L6 + q3*L8  (exact identity,
      checked by expansion).

HOW THE COFACTORS ARE OBTAINED, honestly: (L4, L6, L8) is not a Groebner
basis (LM(L4)=AC divides LM(L6)=A^3 C), so naive division of L_d by the raw
generators leaves a nonzero remainder. Instead: reduce L_d by the reduced lex
Groebner basis G of <L4,L6,L8> (8 elements, remainder exactly 0), then express
each G-basis element in terms of (L4,L6,L8) by undetermined homogeneous
coefficients (exact linsolve over QQ, free parameters set to 0, identity
re-verified by expansion), and compose the two decompositions. The final
identity L_d = q1*L4+q2*L6+q3*L8 is then verified by direct expansion; the
monomial counts are of that verified triple.

Exact sympy rational arithmetic throughout; no floats.  (A pickle cache of the
recurrence output lives in code/out/.focal_Ls.pkl so the expensive recurrence
is not recomputed on iteration; it is a temp artifact, not a capture.)
"""

import itertools
import os
import pickle
import sympy as sp
import time

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
params = [A, C, D, E, F]
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "out", ".focal_Ls.pkl")


def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


def num(poly_expr):
    e = sp.expand(sp.together(poly_expr))
    n, _ = sp.fraction(e)
    return n


def v_p(n, p):
    """p-adic valuation of a nonzero rational n (negative for p in numerator)."""
    n = sp.Rational(n)
    a, b = abs(n.p), n.q
    va = 0
    while a % p == 0 and a > 0:
        a //= p
        va += 1
    vb = 0
    while b % p == 0:
        b //= p
        vb += 1
    return va - vb


def gcd_clearing_denominator(poly):
    """ilcm of denominators of all rational coefficients (gcd clears them)."""
    den = 1
    for mono in sp.Poly(poly, *params).terms():
        den = sp.ilcm(den, sp.Rational(mono[1]).q)
    return den


def compute_obstructions():
    """The Bautin focal-value recurrence, degrees 3..14; same recurrence as
    code/bautin/cofactor_counts.py and code/bautin/verify_membership.py."""
    V = {2: (u**2 + v**2) / 2}
    obstruction = {}
    for degree in range(3, 15):
        coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
        correction = sum(coeffs[j] * u ** (degree - j) * v**j
                         for j in range(degree + 1))
        unknowns = list(coeffs)
        equation = sp.expand(
            rotation(correction) + Q1 * sp.diff(V[degree - 1], u)
            + Q2 * sp.diff(V[degree - 1], v))
        radial = None
        if degree % 2 == 0:
            radial = sp.symbols(f"L{degree}")
            unknowns.append(radial)
            equation -= radial * (u**2 + v**2) ** (degree // 2)
        polynomial = sp.Poly(equation, u, v)
        equations = [polynomial.coeff_monomial(u ** (degree - j) * v**j)
                     for j in range(degree + 1)]
        if degree % 2 == 0:
            equations.append(coeffs[0])
        sol = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
        V[degree] = sp.expand(correction.subs(sol))
        if radial is not None:
            obstruction[degree] = sp.factor(sol[radial])
        print(f"  recurrence degree {degree}: done ({time.time()-_t0:.1f}s)",
              flush=True)
    return obstruction


def load_obstructions():
    if os.path.exists(CACHE):
        with open(CACHE, "rb") as f:
            return pickle.load(f)
    obstruction = compute_obstructions()
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "wb") as f:
        pickle.dump(obstruction, f)
    return obstruction


def monomials_of_degree(e, nvars=5):
    """All monomials of total degree e in params[0..nvars-1]."""
    out = []
    for exps in itertools.product(range(e + 1), repeat=nvars - 1):
        s = sum(exps)
        if s <= e:
            last = e - s
            mono = sp.Integer(1)
            for j in range(nvars - 1):
                mono = mono * params[j] ** exps[j]
            mono = mono * params[nvars - 1] ** last
            out.append(sp.expand(mono))
    return out


def pick_one_solution(linsol, unknowns):
    """From a sp.linsolve result (FiniteSet of solution tuples, possibly with
    free parameters), return a dict {unknown: value} with free params = 0.
    Robust to EmptySet / ConditionSet / FiniteSet shapes."""
    if not hasattr(linsol, "args") or len(getattr(linsol, "args", ())) == 0:
        raise RuntimeError("linsolve returned no solution (inconsistent system)")
    candidates = [a for a in linsol.args if a != sp.S.false]
    if not candidates:
        raise RuntimeError("linsolve returned no solution (inconsistent system)")
    sol_tuple = candidates[0]
    if isinstance(sol_tuple, sp.Tuple):
        sol_tuple = tuple(sol_tuple)
    elif not isinstance(sol_tuple, (tuple, list)):
        sol_tuple = (sol_tuple,)
    free = [s for s in sol_tuple[0].free_symbols if s not in set(unknowns)]
    subs = {s: sp.Integer(0) for s in free}
    values = [sp.simplify(s.subs(subs)) for s in sol_tuple]
    return dict(zip(unknowns, values))


def decompose_in_generators(hom_poly, gens, gen_degs):
    """hom_poly homogeneous of degree Deg in <gens>, gens[i] homogeneous of
    degree gen_degs[i].  Return [q1,..,qk] (homogeneous, qi degree Deg-gen_degs[i]
    or 0) with hom_poly == sum(qi*gens[i]) EXACTLY; the identity is re-checked
    by expansion before returning.  Free parameters of the underdetermined
    linear solve are set to 0."""
    Deg = sp.Poly(hom_poly, *params).total_degree()
    Q = []
    unknowns = []
    for g, dg in zip(gens, gen_degs):
        e = Deg - dg
        if e < 0:
            Q.append(sp.Integer(0))
            continue
        monos = monomials_of_degree(e)
        cs = sp.symbols(f"y_{len(unknowns)}_{e}_0:{len(monos)}")
        Q.append(sum(c * m for c, m in zip(cs, monos)))
        unknowns.extend(cs)
    lhs = sp.expand(sum(q * g for q, g in zip(Q, gens)) - hom_poly)
    poly = sp.Poly(lhs, *params)
    eqs = [poly.coeff_monomial(mono) for (mono, _) in poly.terms()]
    sol_dict = pick_one_solution(sp.linsolve(eqs, unknowns), unknowns)
    Qc = [sp.expand(q.subs(sol_dict)) for q in Q]
    identity = sp.expand(hom_poly - sum(q * g for q, g in zip(Qc, gens)))
    if identity != 0:
        raise RuntimeError("decompose_in_generators: identity check FAILED")
    return Qc


def main():
    global _t0
    _t0 = time.time()
    print("# Bautin focal-value counts, denominators, valuations, cofactors — exact")
    print("")
    print("WHAT RAN:      code/bautin/focal_denoms.py (exact sympy, rational")
    print("               arithmetic, no floats).")
    print("WHICH DEFS:    chart family (u,v), quadratic homogeneous part")
    print("               Q1 = A u^2 + C u v + D v^2 ,  Q2 = E u v + F v^2 ,")
    print("               linear part = rotation rot(p) = -v p_u + u p_v,")
    print("               V2 = (u^2+v^2)/2. Even-degree radial obstructions L_d")
    print("               from rot(c_k)+Q1(V_{k-1})_u+Q2(V_{k-1})_v")
    print("               - L_k (u^2+v^2)^{k/2} ≡ 0. Same recurrence as")
    print("               code/bautin/cofactor_counts.py and")
    print("               code/bautin/verify_membership.py.")
    print("WHICH DEGREES: d = 4, 6, 8, 10, 12, 14.")
    print("")

    print(f"recurrence (or cache load): ...", flush=True)
    t_recur = time.time()
    obstruction = load_obstructions()
    print(f"obstructions ready: {time.time()-t_recur:.1f}s", flush=True)

    # ---- sanity guards reproducing the held audit (verify_membership.py) ----
    P30 = (
        76 * A**3 * C + 24 * A**3 * F + 142 * A**2 * C * D
        + 29 * A**2 * C * E + 192 * A**2 * D * F - 96 * A**2 * E * F
        + 23 * A * C**3 + 109 * A * C**2 * F + 76 * A * C * D**2
        + 42 * A * C * D * E + 3 * A * C * E**2 + 144 * A * C * F**2
        + 132 * A * D**2 * F - 28 * A * D * E * F - 37 * A * E**2 * F
        - 24 * A * F**3 + 23 * C**3 * D + 159 * C**2 * D * F
        - 27 * C**2 * E * F + 10 * C * D**3 + 13 * C * D**2 * E
        + 3 * C * D * E**2 + 350 * C * D * F**2 - 101 * C * E * F**2
        + 20 * D**3 * F + 16 * D**2 * E * F - 27 * D * E**2 * F
        + 248 * D * F**3 + E**3 * F - 124 * E * F**3
    )
    assert sp.factor(8 * obstruction[4] - (A * C + C * D + 2 * D * F - E * F)) == 0
    print("guard: 8*L4 == AC+CD+2DF-EF : PASS", flush=True)
    assert sp.factor(192 * obstruction[6] + P30) == 0
    print("guard: 192*L6 + P30 == 0 (P30 30-monomial) : PASS", flush=True)
    assert len(sp.Poly(P30, *params).terms()) == 30
    print("guard: P30 has 30 monomials : PASS", flush=True)
    print("")

    # ---- (a)(b)(c): counts + denominators + valuations per even degree ----
    print("  d    monomials   denom          v2   v3")
    print("  --   ---------   -----          ---  ---")
    counts = {}
    denoms = {}
    for d in (4, 6, 8, 10, 12, 14):
        poly = obstruction[d]
        n_mono = len(sp.Poly(poly, *params).terms())
        denom = gcd_clearing_denominator(poly)
        counts[d] = n_mono
        denoms[d] = denom
        print(f"  {d:2d}   {n_mono:9d}   {denom:14d}   {v_p(denom, 2):3d}  {v_p(denom, 3):3d}",
              flush=True)
    print("")
    print("monomial counts L_d:", [counts[d] for d in (4, 6, 8, 10, 12, 14)],
          flush=True)
    print("gcd-clearing denominators L_d:",
          [int(denoms[d]) for d in (4, 6, 8, 10, 12, 14)], flush=True)
    print("(v2, v3) of denominators:", [(v_p(denoms[d], 2), v_p(denoms[d], 3))
                                        for d in (4, 6, 8, 10, 12, 14)],
          flush=True)
    print("")

    # ---- (d): Bautin-trick cofactor counts, w.r.t. ORIGINAL (L4, L6, L8) ----
    gens = [num(obstruction[4]), num(obstruction[6]), num(obstruction[8])]
    gen_degs = [2, 4, 6]
    print("reduced lex Groebner basis of <L4,L6,L8>: computing ...", flush=True)
    t_g = time.time()
    G = sp.groebner(gens, *params, order="lex")
    basis = [sp.Poly(b, *params).as_expr() for b in G.polys]
    print(f"Groebner basis: {len(basis)} elements, {time.time()-t_g:.1f}s",
          flush=True)
    # express each basis element in terms of (L4,L6,L8)
    lift = []
    for j, b in enumerate(basis):
        t_j = time.time()
        db = sp.Poly(b, *params).total_degree()
        cofs = decompose_in_generators(b, gens, gen_degs)
        ok = sp.expand(b - sum(q * g for q, g in zip(cofs, gens))) == 0
        if not ok:
            raise RuntimeError(f"lift of basis element {j} failed identity check")
        lift.append(cofs)
        print(f"  basis[{j}]: degree {db}, "
              f"lift monomial counts {[len(sp.Poly(q,*params).terms()) for q in cofs]}, "
              f"verified {ok} ({time.time()-t_j:.1f}s)", flush=True)
    print("")

    for d in (10, 12, 14):
        n = num(obstruction[d])
        quots, rem = G.reduce(n)
        if sp.simplify(rem) != 0:
            raise RuntimeError(f"L{d} is NOT in <L4,L6,L8>: remainder nonzero")
        # compose: L_d = sum_j quots[j]*basis[j] = sum_i q_i * gens[i]
        qcomp = [sp.Integer(0)] * 3
        for j, bq in enumerate(quots):
            for i in range(3):
                qcomp[i] = sp.expand(qcomp[i] + bq * lift[j][i])
        identity = sp.expand(n - (qcomp[0] * gens[0] + qcomp[1] * gens[1]
                                  + qcomp[2] * gens[2]))
        per = [len(sp.Poly(q, *params).terms()) for q in qcomp]
        print(f"L{d}: membership (GB remainder==0) -> True; "
              f"identity L{d}==q1*L4+q2*L6+q3*L8 verified -> {identity == 0}; "
              f"cofactor monomial counts q1,q2,q3 = {per}, "
              f"total = {sum(per)}", flush=True)
    print("")
    print(f"total: {time.time()-_t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()