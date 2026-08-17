#!/usr/bin/env python3
"""Focal values (Lyapunov quantities) of the general quadratic focus, exactly.

The object Bautin's theorem is about. For the planar family with a linear
centre part and a general quadratic perturbation,

    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2

we build a formal Lyapunov function V = (u^2+v^2)/2 + V3 + V4 + ... and solve
degree by degree.  Writing rot(p) = -v p_u + u p_v for the linear part,

    X(V)_d = rot(V_d) + a-part * V_{d-1,u} + b-part * V_{d-1,v}

and rot, acting on homogeneous polynomials of degree d, has as its cokernel on
even d exactly the span of (u^2+v^2)^{d/2}.  So at even d there is one
obstruction L_d, a polynomial in (a1,a2,a3,b1,b2,b3): the d-th focal value.
Odd degrees are always solvable and contribute nothing.

Everything is exact rational arithmetic.  No floats anywhere.

Output: L4, L6, L8 (the three Bautin quantities in this grading, classically
V3, V5, V7), then the ideal tests Bautin's finite-generation theorem predicts:
L8 in <L4,L6>?  L10 in <L4,L6,L8>?
"""

import sympy as sp

u, v = sp.symbols("u v")
a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
PARAMS = [a1, a2, a3, b1, b2, b3]

P2 = a1 * u**2 + a2 * u * v + a3 * v**2
Q2 = b1 * u**2 + b2 * u * v + b3 * v**2


def rot(p):
    return sp.expand(-v * sp.diff(p, u) + u * sp.diff(p, v))


def homogeneous_part(p, d):
    p = sp.expand(p)
    out = 0
    for mono, coeff in p.as_poly(u, v).terms():
        if mono[0] + mono[1] == d:
            out += coeff * u ** mono[0] * v ** mono[1]
    return sp.expand(out)


def coeff_vector(p, d):
    """Coefficients of a homogeneous degree-d poly in u,v, as a list."""
    p = sp.expand(p)
    return [sp.expand(p).coeff(u, d - i).coeff(v, i) for i in range(d + 1)]


def solve_degree(d, rhs):
    """Find V_d and (for even d) the obstruction L_d with

        rot(V_d) + rhs = L_d * (u^2+v^2)^(d/2)      (even d)
        rot(V_d) + rhs = 0                          (odd d)

    Returns (V_d, L_d or None).  Gauge: for even d the coefficient of v^d in
    V_d is set to zero (rot's kernel on even d is spanned by (u^2+v^2)^(d/2),
    so V_d is unique only up to that; pinning one coefficient fixes it).
    """
    cs = sp.symbols(f"c_{d}_0:{d+1}")
    Vd = sum(cs[i] * u ** (d - i) * v**i for i in range(d + 1))
    L = sp.Symbol(f"L{d}") if d % 2 == 0 else None
    target = L * (u**2 + v**2) ** (d // 2) if d % 2 == 0 else 0
    expr = sp.expand(rot(Vd) + rhs - target)
    eqs = coeff_vector(expr, d)
    unknowns = list(cs) + ([L] if L is not None else [])
    if d % 2 == 0:
        eqs = eqs + [cs[d]]  # gauge
    sol = sp.solve(eqs, unknowns, dict=True)
    if not sol:
        raise RuntimeError(f"degree {d}: no solution")
    sol = sol[0]
    Vd_sol = sp.expand(Vd.subs(sol))
    L_sol = sp.simplify(sol[L]) if L is not None else None
    return Vd_sol, L_sol


def main():
    print("# Focal values of the general quadratic focus — exact")
    print()
    print("WHAT RAN:      lyapunov_quadratic.py, exact sympy rational arithmetic,")
    print("               no floats.  Formal Lyapunov function solved degree by")
    print("               degree; obstruction at each even degree is the focal value.")
    print("WHICH DEFS:    u' = -v + a1 u^2 + a2 u v + a3 v^2")
    print("               v' =  u + b1 u^2 + b2 u v + b3 v^2")
    print("               rot(p) = -v p_u + u p_v ;  V = (u^2+v^2)/2 + V3 + V4 + ...")
    print("               L_d = coefficient of (u^2+v^2)^(d/2) obstructing degree d.")
    print("WHICH RANGE:   degrees 3..8; focal values L4, L6, L8. Degree 10 NOT computed.")
    print()

    V = (u**2 + v**2) / 2
    Ls = {}
    for d in range(3, 9):
        prev = homogeneous_part(V, d - 1)
        rhs = sp.expand(P2 * sp.diff(prev, u) + Q2 * sp.diff(prev, v))
        rhs = homogeneous_part(rhs, d)
        Vd, Ld = solve_degree(d, rhs)
        V = sp.expand(V + Vd)
        if Ld is not None:
            Ld = sp.expand(sp.factor(Ld))
            Ls[d] = Ld
            print(f"L{d} = {Ld}")
            print(f"     monomials: {len(Ld.as_poly(*PARAMS).terms())}")
            print()

    print("## Ideal tests (exact Groebner over QQ)")
    print()
    L4, L6, L8 = Ls[4], Ls[6], Ls[8]

    def reduces_to_zero(f, gens):
        num = [sp.numer(sp.together(g)) for g in gens]
        G = sp.groebner([sp.expand(g) for g in num], *PARAMS, order="grevlex")
        return sp.simplify(G.reduce(sp.expand(sp.numer(sp.together(f))))[1]) == 0

    r8 = reduces_to_zero(L8, [L4, L6])
    print(f"L8  in <L4,L6>      : {r8}")
    print("L10 in <L4,L6,L8>   : NOT RUN (degree 10 not computed this run)")
    print()
    print("Bautin's finite-generation theorem needs three generators, so L8 must")
    print("NOT lie in <L4,L6> -- otherwise two would suffice. That is the check")
    print("above. Whether L10 lies in <L4,L6,L8>, which is what finite generation")
    print("asserts next, is NOT tested here: degree 10 was not computed.")
    print()
    emit_lean(Ls)
    ok = (r8 is False)
    print("CHECK (L8 independent of L4,L6):", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def emit_lean(Ls):
    """Emit Lean for the three focal values.

    V1 (6 terms) is emitted as an explicit polynomial term, small enough to
    elaborate and to prove nonvanishing about directly.  V2 (56) and V3 (220)
    are emitted as DATA TABLES — a coefficient vector and a matching table of
    exponent vectors — because a 220-term `+`-chain of `C c * X i ^ e` products
    exhausts Lean's elaboration budget (measured: still times out at 2,000,000
    heartbeats), while the same content as data elaborates.  Coefficients are
    cleared to integers in every case.
    """
    idx = {a1: 0, a2: 1, a3: 2, b1: 3, b2: 4, b3: 5}
    out = []

    def cleared(d):
        poly = sp.Poly(Ls[d], *PARAMS)
        den = 1
        for _, c in poly.terms():
            den = sp.ilcm(den, sp.Rational(c).q)
        return poly, den

    # V1: explicit term
    poly, den = cleared(4)
    terms = []
    for mono, c in poly.terms():
        c = sp.Rational(c) * den
        fac = []
        for var, e in zip(PARAMS, mono):
            if e == 1:
                fac.append(f"X {idx[var]}")
            elif e > 1:
                fac.append(f"X {idx[var]} ^ {e}")
        terms.append(f"C ({c.p} : \u211a) * " + (" * ".join(fac) if fac else "1"))
    out.append(
        f"/-- `V1num = 8 * L4`: {len(terms)} terms, integer coefficients.\n"
        f"Machine-emitted; common denominator {den}. -/\n"
        f"def V1num : LyapunovRing :=\n  " + "\n    + ".join(terms) + "\n")
    out.append(f"/-- The first focal value, `L4 = V1num / {den}`. -/\n"
               f"def V1 : LyapunovRing := C (1 / {den} : \u211a) * V1num\n")

    # V2, V3: data tables
    for name, d in (("V2", 6), ("V3", 8)):
        poly, den = cleared(d)
        rows = list(poly.terms())
        n = len(rows)
        cs = ", ".join(str((sp.Rational(c) * den).p) for _, c in rows)
        ms = ", ".join("![" + ",".join(str(e) for e in mono) + "]" for mono, _ in rows)
        low = name.lower()
        out.append(
            f"/-- UNTRUSTED DATA: the {n} integer coefficients of `{name}num`,\n"
            f"the focal value L{d} cleared by its common denominator {den}.\n"
            f"Machine-emitted by code/bautin/lyapunov_quadratic.py. -/\n"
            f"def {low}coeffs : Fin {n} \u2192 \u2124 :=\n  ![{cs}]\n")
        out.append(
            f"/-- UNTRUSTED DATA: the {n} exponent vectors of `{name}num`, in the\n"
            f"same order as `{low}coeffs`. Index order is (a1,a2,a3,b1,b2,b3). -/\n"
            f"def {low}ms : Fin {n} \u2192 ParamIndex \u2192 \u2115 :=\n  ![{ms}]\n")
        out.append(
            f"/-- `{name}num`, reconstructed from its two data tables. -/\n"
            f"def {name}num : LyapunovRing :=\n"
            f"  \u2211 k : Fin {n}, C (({low}coeffs k : \u211a)) * mono ({low}ms k)\n")
        out.append(f"/-- The focal value `L{d} = {name}num / {den}`. -/\n"
                   f"def {name} : LyapunovRing := C (1 / {den} : \u211a) * {name}num\n")
        out.append(
            f"/-- The coefficient table of `{name}num` is not identically zero, so the\n"
            f"focal value is not the zero polynomial for a trivial reason. Ground\n"
            f"check over `Fin {n}`, closed by `decide`. -/\n"
            f"theorem {low}coeffs_nontrivial : \u2203 k : Fin {n}, {low}coeffs k \u2260 0 := by\n"
            f"  refine \u27e80, by decide\u27e9\n")
    open("/w-out/bautin_defs.lean", "w").write("\n".join(out))
    print("emitted Lean: V1 explicit term; V2, V3 as data tables")


if __name__ == "__main__":
    raise SystemExit(main())
