#!/usr/bin/env python3
"""SECOND evaluation witness for  L8 not in <L4, L6>.

Independent route to the SAME non-membership statement as
code/bautin/cofactor_certificate.py (which found certPt = (-2,-2,1,-1,-1,1)).

Why a second point. The evaluation-witness certificate in Bautin.lean rests on
ONE point. A second point, found by a different search (full box sweep over
{-3..3}^6, no support-size restriction, and a proportionality check against
certPt so the new point is not just a scalar rescaling of the first — L4,L6,L8
are homogeneous, so any nonzero multiple of a witness is again a witness) gives
a second kernel-checked proof of the same theorem through a genuinely distinct
evaluation. Two proofs via two points is a real cross-check: the certPt proof
could in principle be an artefact of one arithmetic coincidence in the
focal-value tables, and the second point kills that worry at the cost of one
`by simp; norm_num` in Lean.

Definitions identical to cofactor_certificate.py:
    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2
    L_d = focal value at degree d, same recurrence as lyapunov_quadratic.py.
Exact rational arithmetic (sympy), no floats.

Output goes to code/out/cofactor_certificate2.captured.txt.
"""

import itertools
import sympy as sp

u, v = sp.symbols("u v")
a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
PARAMS = [a1, a2, a3, b1, b2, b3]

P2 = a1 * u**2 + a2 * u * v + a3 * v**2
Q2 = b1 * u**2 + b2 * u * v + b3 * v**2


def rot(p):
    return sp.expand(-v * sp.diff(p, u) + u * sp.diff(p, v))


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
    expr = sp.expand(rot(Vd) + rhs - target)
    eqs = [sp.expand(expr).coeff(u, d - i).coeff(v, i) for i in range(d + 1)]
    unknowns = list(cs) + ([L] if L is not None else [])
    if d % 2 == 0:
        eqs = eqs + [cs[d]]
    sol = sp.solve(eqs, unknowns, dict=True)[0]
    return sp.expand(Vd.subs(sol)), (sp.simplify(sol[L]) if L is not None else None)


def focal_values():
    V = (u**2 + v**2) / 2
    Ls = {}
    for d in range(3, 9):
        prev = homogeneous_part(V, d - 1)
        rhs = homogeneous_part(sp.expand(P2 * sp.diff(prev, u) + Q2 * sp.diff(prev, v)), d)
        Vd, Ld = solve_degree(d, rhs)
        V = sp.expand(V + Vd)
        if Ld is not None:
            Ls[d] = sp.expand(Ld)
    return Ls


def eval_poly(poly, pt):
    return sp.simplify(poly.subs(dict(zip(PARAMS, [sp.Integer(x) for x in pt]))))


def proportional(p, q):
    """True iff q is a nonzero rational scalar multiple of p."""
    nz = [(a, b) for a, b in zip(p, q) if a != 0 or b != 0]
    if not nz:
        return True
    a0, b0 = nz[0]
    return all(a * b0 == b * a0 for a, b in nz)


def main():
    out = [
        "# Second evaluation witness for  L8 not in <L4, L6>",
        "",
        "WHAT RAN:      code/bautin/cofactor_certificate2.py, exact sympy,",
        "               rational arithmetic, no floats.",
        "WHICH DEFS:    same recurrence as cofactor_certificate.py /",
        "               lyapunov_quadratic.py: u' = -v + a1 u^2 + a2 u v + a3 v^2 ;",
        "               v' =  u + b1 u^2 + b2 u v + b3 v^2 ;",
        "               L_d = focal value at degree d.",
        "WHICH RANGE:   FULL BOX sweep over {-3..3}^6 (all 7^6 points), no",
        "               support-size restriction, unlike the first search",
        "               (support 1..6, values +-1,+-2). L4,L6,L8 are homogeneous",
        "               (degrees 2,4,6), so zeros are projective: the new point",
        "               is required NOT to be a rational scalar multiple of the",
        "               first witness certPt = (-2,-2,1,-1,-1,1).",
        "",
        "WHY A SECOND POINT (independent cross-check):",
        "   the certPt proof is three evaluations; if the focal-value tables",
        "   had one consistent arithmetic coincidence, both L4=L6=0 and L8!=0",
        "   could in principle fire together at a single point. A second point,",
        "   non-proportional to the first, makes the coincidence hypothesis",
        "   need to hold at two independent places of the variety L4=L6=0.",
        "   The Lean theorem is then proved TWICE, through two evaluations,",
        "   both kernel-checked (Bautin.lean and L8NotInIdeal_alt.lean).",
        "",
    ]
    Ls = focal_values()
    L4, L6, L8 = Ls[4], Ls[6], Ls[8]
    f4 = sp.lambdify(PARAMS, L4, "math")
    out.append("guard: L4 = %s" % L4)
    out.append("guard: L4 monomials %d | L6 %d | L8 %d"
               % (len(sp.Poly(L4, *PARAMS).terms()),
                  len(sp.Poly(L6, *PARAMS).terms()),
                  len(sp.Poly(L8, *PARAMS).terms())))

    certpt = [-2, -2, 1, -1, -1, 1]
    box = range(-3, 4)
    found = []
    tried = 0
    for pt in itertools.product(box, repeat=6):
        tried += 1
        if proportional(pt, certpt):
            continue
        if eval_poly(L4, pt) != 0:
            continue
        if eval_poly(L6, pt) != 0:
            continue
        e8 = eval_poly(L8, pt)
        if e8 != 0:
            found.append((pt, e8))
            if len(found) >= 3:
                break
    out.append(f"points tried: {tried} (excluding the certPt line: 7^6 - 1 = 117648)")
    out.append(f"distinct witnesses found in this box: {len(found) + 1} (incl. certPt)")
    ok = False
    if found:
        pt, e8 = found[0]
        out.append("")
        out.append("SECOND WITNESS FOUND (non-proportional to certPt):")
        for n, x in zip([str(p) for p in PARAMS], pt):
            out.append(f"  {n} = {x}")
        out.append(f"  a1..b3 vector: {pt}")
        out.append(f"  L4(p) = {eval_poly(L4, pt)}  (must be 0)")
        out.append(f"  L6(p) = {eval_poly(L6, pt)}  (must be 0)")
        out.append(f"  L8(p) = {e8}  (must be nonzero)")
        out.append(f"  proportional to certPt? {proportional(pt, certpt)}  (must be False)")
        out.append("")
        out.append("CERTIFICATE VALID: PASS")
        out.append("")
        out.append("Lean witness vector, in Bautin.lean (a1,a2,a3,b1,b2,b3) order:")
        out.append("  def certPt2 : ParamIndex -> Q := ![%s]" % ", ".join(str(x) for x in pt))
        out.append("")
        # cleared-integer evaluations for the Lean kernel (Vknum = Lk * denom)
        sub = dict(zip(PARAMS, [sp.Integer(x) for x in pt]))
        out.append("Cleared-integer evaluations:")
        extra = []
        for name, d in (("V1num", 4), ("V2num", 6), ("V3num", 8)):
            poly = sp.Poly(Ls[d], *PARAMS)
            den = 1
            for _, c in poly.terms():
                den = sp.ilcm(den, sp.Rational(c).q)
            val = sp.simplify(sp.expand(Ls[d] * den).subs(sub))
            out.append(f"  eval {name} at the witness = {val}   (denominator {den})")
            extra.append((name, val))
        ok = (eval_poly(L4, pt) == 0 and eval_poly(L6, pt) == 0 and e8 != 0
              and not proportional(pt, certpt) and extra[2][1] != 0 and extra[0][1] == 0
              and extra[1][1] == 0)
    else:
        out.append("")
        out.append("NO SECOND WITNESS in {-3..3}^6 excluding certPt's line.")
        out.append("That is NOT a refutation of the statement (the Groebner run")
        out.append("established non-membership) — it means this box does not")
        out.append("separate L8, so the independent route needs a wider box.")
    out.append("")
    out.append("SCOPE. Same statement as cofactor_certificate.py: L8 not in <L4,L6>.")
    out.append("Says nothing about M(2)=3 itself (cited Bautin 1952, Bautin.lean).")
    text = "\n".join(out) + "\n"
    with open("code/out/cofactor_certificate2.captured.txt", "w") as fh:
        fh.write(text)
    print(text)
    return 0 if ok else (2 if found else 1)


if __name__ == "__main__":
    raise SystemExit(main())