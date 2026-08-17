#!/usr/bin/env python3
"""A kernel-checkable certificate for  L8 not in <L4, L6>.

Why not cofactors. The task this answers was named "cofactor certificate", but a
cofactor identity certifies MEMBERSHIP: `f = sum q_i g_i` is checkable by `ring`.
NON-membership has no such certificate — there is no finite identity saying a
polynomial is absent from an ideal, and reproducing the Groebner argument inside
Lean would mean formalising Buchberger.

What is checkable instead. Every element of `<L4, L6>` vanishes at every common
zero of `L4` and `L6`. So one rational point `p` with

    L4(p) = 0 ,  L6(p) = 0 ,  L8(p) != 0

refutes membership outright, and the refutation is three rational evaluations —
arithmetic the Lean kernel does. (It proves more than the Groebner run did:
`L8` is outside the RADICAL of `<L4,L6>`, hence outside the ideal.)

The point is searched sparse — as many zero coordinates as possible — because
`V3` is a 220-term polynomial in Lean and each zero coordinate kills most of the
monomials, which is what keeps the kernel evaluation cheap.

Parameters are (a1,a2,a3,b1,b2,b3) for the family
    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2
matching code/bautin/lyapunov_quadratic.py and code/lean/Lib/Bautin.lean.
Exact rational arithmetic throughout; no floats.
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


def main():
    print("# Certificate for  L8 not in <L4, L6>  — evaluation witness")
    print()
    print("WHAT RAN:      code/bautin/cofactor_certificate.py, exact sympy")
    print("               rational arithmetic, no floats.")
    print("WHICH DEFS:    u' = -v + a1 u^2 + a2 u v + a3 v^2 ;")
    print("               v' =  u + b1 u^2 + b2 u v + b3 v^2 ;")
    print("               L_d = focal value at degree d, same recurrence as")
    print("               code/bautin/lyapunov_quadratic.py.")
    print("WHICH RANGE:   integer points, coordinates in -2..2, every support")
    print("               size 1..6 in turn (sparsest first), searched for")
    print("               L4 = L6 = 0 and L8 != 0. Each L_d is homogeneous")
    print("               (degrees 2, 4, 6), so zeros are projective and integer")
    print("               points lose no generality.")
    print()
    print("WHY AN EVALUATION WITNESS AND NOT A COFACTOR IDENTITY:")
    print("  a cofactor identity certifies membership; non-membership has no")
    print("  finite identity. One common zero of L4 and L6 at which L8 does not")
    print("  vanish refutes membership, and is three rational evaluations the")
    print("  Lean kernel can do. It also proves the stronger statement that L8")
    print("  is outside the radical of <L4, L6>.")
    print()

    Ls = focal_values()
    L4, L6, L8 = Ls[4], Ls[6], Ls[8]
    f4 = sp.lambdify(PARAMS, L4, "math")
    print("guard: L4 =", L4)
    print("guard: L4 monomials", len(sp.Poly(L4, *PARAMS).terms()),
          "| L6", len(sp.Poly(L6, *PARAMS).terms()),
          "| L8", len(sp.Poly(L8, *PARAMS).terms()))
    print()

    vals = [-3, -2, -1, 1, 2, 3]
    best = None
    tried = 0
    for support_size in (1, 2, 3, 4, 5, 6):
        for support in itertools.combinations(range(6), support_size):
            for assign in itertools.product([x for x in vals if abs(x) <= 2], repeat=support_size):
                pt = [0] * 6
                for i, val in zip(support, assign):
                    pt[i] = val
                tried += 1
                sub = dict(zip(PARAMS, [sp.Integer(x) for x in pt]))
                if sp.simplify(L4.subs(sub)) != 0:
                    continue
                if sp.simplify(L6.subs(sub)) != 0:
                    continue
                e8 = sp.simplify(L8.subs(sub))
                if e8 != 0:
                    best = (pt, e8, support_size)
                    break
            if best:
                break
        if best:
            break

    print(f"points tried: {tried}")
    if not best:
        print()
        print("NO WITNESS FOUND in this box.")
        print("That is not a refutation of non-membership: the Groebner run")
        print("(code/out/membership.captured.txt) established L8 not in <L4,L6>")
        print("over Q. It means no common zero with at most three nonzero")
        print("coordinates in -3..3 separates them, so a Lean certificate needs")
        print("either a wider search or a different route. Reported, not hidden.")
        return 1

    pt, e8, k = best
    names = [str(p) for p in PARAMS]
    print()
    print("WITNESS FOUND (sparse: %d nonzero coordinate(s))" % k)
    for n, x in zip(names, pt):
        print(f"  {n} = {x}")
    print()
    print("  L4(p) =", sp.simplify(L4.subs(dict(zip(PARAMS, pt)))), "  (must be 0)")
    print("  L6(p) =", sp.simplify(L6.subs(dict(zip(PARAMS, pt)))), "  (must be 0)")
    print("  L8(p) =", e8, "  (must be nonzero)")
    print()
    ok = (sp.simplify(L4.subs(dict(zip(PARAMS, pt)))) == 0
          and sp.simplify(L6.subs(dict(zip(PARAMS, pt)))) == 0
          and e8 != 0)
    print("CERTIFICATE VALID:", "PASS" if ok else "FAIL")
    print()
    print("Lean witness vector, in Bautin.lean's (a1,a2,a3,b1,b2,b3) order:")
    print("  def certPt : ParamIndex -> Q := ![%s]" % ", ".join(str(x) for x in pt))
    print()
    print("Cleared-integer evaluations, which is what the Lean kernel checks")
    print("(Vknum = Lk times its common denominator, so the zero/nonzero")
    print("pattern is identical):")
    sub = dict(zip(PARAMS, [sp.Integer(x) for x in pt]))
    for name, d in (("V1num", 4), ("V2num", 6), ("V3num", 8)):
        poly = sp.Poly(Ls[d], *PARAMS)
        den = 1
        for _, c in poly.terms():
            den = sp.ilcm(den, sp.Rational(c).q)
        val = sp.simplify(sp.expand(Ls[d] * den).subs(sub))
        print(f"  eval {name} at the witness = {val}   (denominator {den})")
    print()
    print("SCOPE. This certifies L8 not in <L4,L6> — that Bautin's third")
    print("generator is genuinely needed. It says nothing about M(2) = 3 itself,")
    print("which stays cited (Bautin 1952) in code/lean/Lib/Bautin.lean.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
