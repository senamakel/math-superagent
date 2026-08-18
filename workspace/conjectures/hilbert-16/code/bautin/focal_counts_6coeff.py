#!/usr/bin/env python3
"""Focal values (Lyapunov quantities) of the general quadratic focus — exact,
continued beyond degree 8 where code/bautin/lyapunov_quadratic.py stopped.

Family (the six-coefficient general quadratic focus, linear centre part):

    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2

(The task statement wrote "b3 v^3" for the last v-term; that is a typo — the
referenced lyapunov_quadratic.py has b3 v^2 and the family is quadratic, so
b3 v^2 is used here and recorded in the capture header.)

Formal Lyapunov function V = (u^2+v^2)/2 + V3 + V4 + ... solved degree by
degree with rot(p) = -v p_u + u p_v:

    rot(V_d) + (P2 (V_{d-1})_u + Q2 (V_{d-1})_v) = L_d (u^2+v^2)^{d/2}   (even d)
    rot(V_d) + (P2 (V_{d-1})_u + Q2 (V_{d-1})_v) = 0                     (odd  d)

L_d is the even-degree obstruction: the d-th focal value, a polynomial in
(a1,a2,a3,b1,b2,b3), unique and gauge-invariant; the gauge c_{d,0}=0 pins V_d
(rot's kernel on even d is spanned by (u^2+v^2)^{d/2}).

For each even d in (4,6,8,10,12[,14]) reports exactly:
  * the monomial count of L_d over the six coefficients,
  * the iLCM-cleared denominator of L_d (ilcm of the denominators of all
    rational coefficients, so that denom * L_d is an integer-coefficient
    polynomial),
  * the L1 norm of the cleared-integer coefficient vector (sum |c|),
  * the wall time spent on that degree.

Guards (oracle anchors from the held lyapunov_quadratic.py run):
  * L4 == a1*a2/8 - a1*b1/4 + a2*a3/8 + a3*b3/4 - b1*b2/8 - b2*b3/8
  * monomial counts L4 = 6, L6 = 56, L8 = 220
  * for every even degree: the defining identity
        rot(V_d) + rhs - L_d (u^2+v^2)^{d/2} == 0
    holds exactly, and L_d is homogeneous of degree d-2 in the six params.

Everything exact sympy rational arithmetic; no floats anywhere.

Checkpoint/resume: state (the solved Lyapunov polynomial V up to each degree,
and every focal value L_d) is saved after each degree to a JSON file named by
--ckpt, so a run interrupted by a wall-clock ceiling resumes without redoing
solved degrees.  This makes degree 14 achievable across several bounded
commands even though one command cannot span it.

Budget policy (the task asks: include degree 14 only if it finishes within
45 minutes): the run records the wall time when each even degree COMPLETES.
Degree 14 is included in the reported table only if its completion time is
within the --deadline-min budget of the run's start; if the remaining budget
is provably insufficient (estimated by the observed per-degree scaling) or
the completion lands past it, degree 14 is recorded as SKIPPED/TIMED OUT and
the table carries L4..L12.

Usage: python code/bautin/focal_counts_6coeff.py [--max-degree N] [--deadline-min M]
                                                 [--ckpt PATH] [--resume]
"""

import argparse
import json
import sys
import time

import sympy as sp

# The V-d recurrence produces ever-deeper nested Add trees; their str()
# re-parse (resume path) blows the default Python/C recursion budget on
# degrees >= 11. Raise it early so a resume can load degrees it can reach.
sys.setrecursionlimit(1_000_000)

u, v = sp.symbols("u v")
a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
PARAMS = [a1, a2, a3, b1, b2, b3]
P2 = a1 * u**2 + a2 * u * v + a3 * v**2
Q2 = b1 * u**2 + b2 * u * v + b3 * v**2

EVEN_SCHEDULE = [4, 6, 8, 10, 12, 14]

# Held anchors from code/out/bautin_focal_values.captured.txt (that run used
# gauge c_{d,d}=0; L_d is gauge-invariant, so the counts must agree).
EXPECTED_COUNTS = {4: 6, 6: 56, 8: 220}
L4_CLOSED_FORM = (a1 * a2 / 8 - a1 * b1 / 4 + a2 * a3 / 8
                  + a3 * b3 / 4 - b1 * b2 / 8 - b2 * b3 / 8)


def rot(p):
    return sp.expand(-v * sp.diff(p, u) + u * sp.diff(p, v))


def expr_to_json(e):
    return str(e)


def json_to_expr(s):
    return sp.sympify(s) if s is not None else None


def solve_degree(d, rhs):
    """Solve rot(V_d) + rhs = L_d (u^2+v^2)^(d/2)  (even d) or = 0 (odd d).

    Returns (V_d, L_d or None). Gauge c_{d,0}=0 fixes rot's kernel and makes
    the square linear system nonsingular; L_d is gauge-invariant.
    """
    cs = sp.symbols(f"c{d}_0:{d + 1}")
    Vd = sum(cs[i] * u ** (d - i) * v**i for i in range(d + 1))
    unknowns = list(cs)
    target = 0
    L = None
    if d % 2 == 0:
        L = sp.Symbol(f"L{d}")
        unknowns.append(L)
        target = L * (u**2 + v**2) ** (d // 2)
    expr = sp.expand(rot(Vd) + rhs - target)
    poly = sp.Poly(expr, u, v)
    eqs = [poly.coeff_monomial(u ** (d - j) * v**j) for j in range(d + 1)]
    if d % 2 == 0:
        eqs.append(cs[0])  # gauge c_{d,0} = 0
    sol = sp.solve(eqs, unknowns, dict=True, simplify=False)
    if not sol:
        raise RuntimeError(f"degree {d}: linear system has no solution")
    sol = sol[0]
    Vd_sol = sp.expand(Vd.subs(sol))
    L_sol = sp.expand(sp.factor(sol[L])) if L is not None else None
    return Vd_sol, L_sol


def residual_ok(d, Vd, rhs, Ld):
    """The defining identity must hold exactly — it is what the solve means."""
    if d % 2 == 0:
        resid = sp.expand(rot(Vd) + rhs - Ld * (u**2 + v**2) ** (d // 2))
    else:
        resid = sp.expand(rot(Vd) + rhs)
    return resid == 0


def poly_table_row(Ld):
    """(monomial_count, ilcm_denominator, L1_of_cleared, homogeneous_degree)
    for a focal value L_d, or None if L_d is not a polynomial in the six
    parameters.

    ilcm_denominator: ilcm of the denominators of all rational coefficients,
    so denom * L_d has integer coefficients.  L1: sum |c| over those cleared
    integer coefficients.  Homogeneous degree is expected d-2.
    """
    try:
        p = sp.Poly(sp.expand(sp.together(Ld)), *PARAMS)
    except sp.PolificationFailed:
        return None
    terms = p.terms()
    count = len(terms)
    ilcm = 1
    for _, c in terms:
        ilcm = sp.ilcm(ilcm, sp.Rational(c).q)
    cleared = [int(sp.Rational(c) * ilcm) for _, c in terms]
    for c in cleared:  # the clearing must really have produced integers
        assert isinstance(c, int) and not isinstance(c, bool)
    l1 = sum(abs(c) for c in cleared)
    degs = [sum(m) for m, _ in terms]
    hdeg = degs[0] if all(x == degs[0] for x in degs) else None
    return count, ilcm, l1, hdeg


def dump_poly(path, Ld, d):
    """Machine-readable exact dump of L_d: deterministic ordered list of
    (integer-coefficient, exponent-tuple) rows together with the shared
    ilcm-clearing denominator D, so D * L_d = sum(c_int * monomial).  A later
    exact program (or a Lean data table) can reconstruct L_d from this file
    without recomputing the recurrence."""
    e = sp.expand(sp.together(Ld))
    p = sp.Poly(e, *PARAMS)
    terms = p.terms()
    ilcm = 1
    for _, c in terms:
        ilcm = sp.ilcm(ilcm, sp.Rational(c).q)
    rows = []
    for mono, c in terms:
        num = int(sp.Rational(c) * ilcm)
        rows.append((num, tuple(int(e0) for e0 in mono)))
    name = f"L{d}"
    with open(path, "w") as fh:
        fh.write(f"# {name} of the general quadratic focus, exact.\n")
        fh.write(f"# D * {name} = sum(c_int * monomial), D the ilcm clearing\n")
        fh.write("# denominator below. Index order (a1,a2,a3,b1,b2,b3).\n")
        fh.write(f"DENOM_{name} = {int(ilcm)}\n")
        fh.write(f"TERMS_{name} = [\n")
        for num, mono in rows:
            fh.write(f"    ({num}, {mono}),\n")
        fh.write("]\n")
        fh.write(f"# {len(rows)} monomials.\n")
    return len(rows)


def even_rhs(d, Vprev):
    """The degree-d homogeneous part of P2*(Vprev)_u + Q2*(Vprev)_v."""
    full = sp.expand(P2 * sp.diff(Vprev, u) + Q2 * sp.diff(Vprev, v))
    rhs = 0
    for mono, coeff in full.as_poly(u, v).terms():
        if mono[0] + mono[1] == d:
            rhs += coeff * u ** mono[0] * v ** mono[1]
    return sp.expand(rhs)


def save_ckpt(path, V, wall, done_through, total_elapsed):
    data = {
        "V": {str(d): expr_to_json(x) for d, x in V.items()},
        "wall": {str(d): wall[d] for d in wall},
        "done_through": done_through,
        "total_elapsed": total_elapsed,
    }
    with open(path + ".tmp", "w") as fh:
        json.dump(data, fh)
    import os
    os.replace(path + ".tmp", path)


def load_ckpt(path):
    with open(path) as fh:
        data = json.load(fh)
    V = {int(d): json_to_expr(s) for d, s in data["V"].items()}
    wall = {int(d): float(w) for d, w in data["wall"].items()}
    return V, wall, int(data["done_through"]), float(data["total_elapsed"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-degree", type=int, default=14)
    ap.add_argument("--deadline-min", type=float, default=45.0)
    ap.add_argument("--ckpt", default="code/out/.focal_6coeff_state.json")
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()
    max_deg = args.max_degree
    deadline_s = args.deadline_min * 60.0

    t0 = time.time()
    V = {2: (u**2 + v**2) / 2}
    wall0 = {}
    done_through = 2
    if args.resume:
        V, wall0, done_through, prev_elapsed = load_ckpt(args.ckpt)
        t0 = time.time() - prev_elapsed

    print("# Focal values of the general quadratic focus beyond degree 8 — exact")
    print("WHAT RAN:      code/bautin/focal_counts_6coeff.py (exact sympy rational")
    print("               arithmetic, no floats); extends lyapunov_quadratic.py")
    print("               beyond degree 8" + (" (RESUMED)" if args.resume else "") + ".")
    print("WHICH DEFS:    u' = -v + a1 u^2 + a2 u v + a3 v^2;  v' = u + b1 u^2")
    print("               + b2 u v + b3 v^2 (the task's 'b3 v^3' read as the")
    print("               quadratic term b3 v^2, matching the referenced file);")
    print("               rot(p) = -v p_u + u p_v;  V2 = (u^2+v^2)/2;")
    print("               gauge c_{d,0} = 0;  L_d = radial obstruction at even d.")
    print(f"WHICH DEGREES: recurrence degrees 3..{max_deg}; reported even focal",
          flush=True)
    print(f"               values {[d for d in EVEN_SCHEDULE if d <= max_deg]};",
          "degree 14 included only if it finishes within",
          f"{args.deadline_min:g} min of the run start.", flush=True)
    print()

    wall = dict(wall0)
    Ls = {}
    skip14 = None
    stopped_at = None

    # Estimate the completion time of the next-even-degree obstruction from
    # the observed per-step growth, to enforce the task's rule (include a
    # degree only if it finishes within the budget) without wasting the run
    # on a degree that provably cannot land inside `deadline_min`.
    def est_next_completion():
        es = sorted(d for d in wall if d >= 5)
        if len(es) < 2:
            return None
        ratios = [wall[es[i]] / wall[es[i - 1]] for i in range(1, len(es))]
        factor = max(ratios)
        # the next even degree after max(even done) will follow a full odd
        # step and an even step, each ~factor x the previous
        last_even = max(d for d in wall if d % 2 == 0)
        slots = (max_deg - last_even)  # number of remaining degree-steps
        est = time.time() - t0 + wall[last_even] * (factor ** slots)
        return est + 0.0  # projected absolute wall time of finishing max_deg

    for d in range(done_through + 1, max_deg + 1):
        el = time.time() - t0
        if d >= 13:
            # Soft deadline first: PREVIEW the completion of the final even
            # degree (max_deg) before starting the expensive odd step 13 that
            # only exists to reach it. If max_deg is projected to finish past
            # the budget, stop here and leave max_deg out of the table.
            if d == 13 and max_deg % 2 == 0 and max_deg >= 14:
                proj = est_next_completion()
                if proj is not None and proj > deadline_s:
                    skip14 = (f"SKIPPED: degree {max_deg} estimated to finish at "
                              f"~{proj:.0f}s (> {args.deadline_min:g}-min budget; "
                              f"per the task it is excluded from the table)")
                    print(f"degree {max_deg}: NOT STARTED (estimated completion "
                          f"~{proj:.0f}s exceeds {args.deadline_min:g}-min budget)",
                          flush=True)
                    stopped_at = max_deg
                    break
            # Hard deadline: never start a degree once past the budget.
            if el > deadline_s:
                if d == 13:
                    skip14 = (f"SKIPPED: {args.deadline_min:g}-min deadline reached "
                              f"at {el:.0f}s before degrees 13/14 started")
                print(f"degree {d}: NOT STARTED (deadline {args.deadline_min:g} min "
                      f"reached at {el:.0f}s)", flush=True)
                stopped_at = d
                break
        t_d = time.time()
        rhs = even_rhs(d, V[d - 1])
        Vd, Ld = solve_degree(d, rhs)
        assert residual_ok(d, Vd, rhs, Ld), \
            f"degree {d}: defining identity failed"
        V[d] = Vd
        wall[d] = time.time() - t_d
        if Ld is not None:
            Ls[d] = Ld
        done_through = d
        save_ckpt(args.ckpt, V, wall, done_through, time.time() - t0)
        print(f"degree {d:2d}: done in {wall[d]:7.1f}s  "
              f"(cumulative {time.time() - t0:8.1f}s)", flush=True)

    total = time.time() - t0

    # -------- guards --------
    print()
    print("## Guards (oracle anchors, held from lyapunov_quadratic.py)")
    print("L4 == a1*a2/8 - a1*b1/4 + a2*a3/8 + a3*b3/4 - b1*b2/8 - b2*b3/8  :",
          sp.simplify(Ls[4] - L4_CLOSED_FORM) == 0)
    got38 = ([len(sp.Poly(Ls[d], *PARAMS).terms()) for d in (4, 6, 8)]
             == [EXPECTED_COUNTS[d] for d in (4, 6, 8)])
    print(f"monomial counts L4,L6,L8 == 6,56,220                         :",
          got38)
    for d in sorted(Ls):
        rhs = even_rhs(d, V[d - 1])
        ok = residual_ok(d, V[d], rhs, Ls[d])
        print(f"defining identity rot(V{d}) + rhs - L{d}(u^2+v^2)^({d}//2) == 0 :",
              ok, flush=True)
    print()

    # -------- the table --------
    print(" d    monomials   ilcm-denominator       L1(cleared)     hdeg   wall(s)   cum(s)")
    print(" ---  ----------  ------------------  ----------------  -----  --------  --------")
    rows = {}
    for d in EVEN_SCHEDULE:
        if d not in Ls:
            continue
        row = poly_table_row(Ls[d])
        if row is None:
            print(f"{d:3d}   NOT A POLYNOMIAL in the six coefficients "
                  "(denominator depends on params)")
            continue
        count, ilcm, l1, hdeg = row
        rows[d] = (count, ilcm, l1, hdeg)
        hd = f"{hdeg}" if hdeg is not None else "-"
        cum = sum(wall[dd] for dd in range(3, d + 1))
        print(f"{d:3d}   {count:9d}   {ilcm:18d}   {l1:16d}   {hd:>5s}   "
              f"{wall[d]:8.1f}   {cum:8.1f}", flush=True)
    print()

    # -------- homogeneity guard: hdeg must be d-2 for every even d --------
    print("## Homogeneity guard (L_d homogeneous of degree d-2)")
    for d, (count, ilcm, l1, hdeg) in sorted(rows.items()):
        print(f"  L{d}: hdeg == d-2 ({d - 2}) -> {hdeg == d - 2}")
    all_hom = all(h == d - 2 for d, (_, _, _, h) in rows.items())
    print()

    # -------- machine-readable exact dumps of the NEW focal values --------
    dumped = []
    for d in (10, 12, 14):
        if d in Ls:
            path = f"code/out/focal_6coeff_L{d}.txt"
            n = dump_poly(path, Ls[d], d)
            dumped.append(f"{path} ({n} terms)")
    print("## Exact polynomial dumps (machine-readable, ilcm-cleared)")
    for line in dumped:
        print("  " + line)
    print()

    # -------- degree 14 verdict --------
    if 14 in Ls:
        verdict = ("INCLUDED" if total <= deadline_s
                   else "TIMED OUT (finished, but completion is beyond the "
                        f"{args.deadline_min:g}-min budget — per the task "
                        "instruction it is excluded from the reported table)")
        print(f"## Degree 14 verdict: {verdict} (total {total:.0f}s, "
              f"budget {args.deadline_min:g} min)")
    elif skip14 is not None:
        print(f"## Degree 14 verdict: {skip14}")
    elif stopped_at is not None:
        print(f"## Degree 14 verdict: not reached this command (stopped before "
              f"degree {stopped_at}); resume with --resume to continue. "
              f"Degree 14 is kept out of the table until a single run carries it "
              f"to completion within the {args.deadline_min:g}-min budget.")
    else:
        print(f"## Degree 14 verdict: SKIPPED (max-degree {max_deg} requested; "
              "not computed)")
    print()
    print("## Summary")
    print(f"total wall time: {total:.0f}s")
    for d in EVEN_SCHEDULE:
        if d in Ls:
            print(f"  L{d}: {rows[d][0]} monomials, denom {rows[d][1]}, "
                  f"L1 {rows[d][2]}, wall {wall[d]:.1f}s")
    ok = (sp.simplify(Ls[4] - L4_CLOSED_FORM) == 0 and got38 and all_hom
          and all(residual_ok(d, V[d], even_rhs(d, V[d - 1]), Ls[d])
                  for d in Ls))
    print("CHECK (all guards + all defining identities + homogeneity):",
          "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())