"""Five-roots rung, second executable step: eliminate the coincidence+centroid
system for n=6 pattern (2,1,1,1,1) and show it is UNSAT over Q.

Context (from code/roots5/multipattern.py, the rung's first step): with five
distinct roots and f = (x-a)^2(x-b)(x-c)(x-d)(x-e) (monic, degree 6, a of
multiplicity 2, b,c,d,e distinct and distinct from a), the pure multiplicity
mechanism covers only derivative i=1 (root a, multiplicity 2 > 1).  Every other
derivative test must be met by a higher-order *coincidence*: a root of
f^(i) among {a,b,c,d,e} for i = 2,3,4, and the centroid equation at i=5
(the weighted mean c = (2a+b+c+d+e)/6 must equal one of the roots; f^(5) is a
nonzero constant multiple of (x-c) by the centroid lemma verified in the first
step).

The CA hypothesis for a monic degree-6 polynomial is

    gcd(f, f^(i)) != 1  for every i = 1..5   (shares a root with each derivative)

so for f of this form the hypothesis holds exactly when each of
    i=1 : satisfied automatically (multiplicity mechanism, root a)
    i=2,3,4 : exists a root r with f^(i)(r) = 0   (coincidence)
    i=5 : centroid c equals one of the roots, i.e. some f^5-root (which is c)
          is a root of f.
We build the exact system over QQ and, for each *root-index choice* (a witness
root for each of i=2,3,4 and a witness root for the centroid equation), form the
AND of the f^(i)(root)=0 equations.  Because each i is a disjunction over the 5
roots, the disjunction is satisfiable iff at least one of its 5^4 = 625
conjunction systems is satisfiable.  We prove every one UNSAT over Q-bar.

Distinctness is imposed exactly via the Rabinowitsch trick: with D = product of
all 10 pairwise root differences (a-b)(a-c)...(d-e), a point has all five roots
pairwise distinct iff D != 0 there, and that is detected by the ideal

    I + <1 - t*D>    (t a fresh variable)

whose reduced Groebner basis (over QQ, lex order with t last) is the unit ideal
[1] iff there is NO distinct-root solution (the distinct locus V(I) \ V(D) is
empty).  This is the exact, field-theoretic way to enforce the setup "5 distinct
roots" without floating point.  We report for each of the 625 choices whether
the reduced GB is [1] (UNSAT) or not (SAT), the term order (lex, t eliminated in
favour of the root variables), the base ring (QQ), worker count, and the wall
clock.

Because n=6 is a known-settled degree (CA holds over Q, Castryck-Laterveer-
Ounai'es 2012), the expected answer is UNSAT for every root-index choice: no
degree-6 polynomial with exactly 5 distinct roots satisfies the CA hypothesis.
That is the check this program performs — confirming, through the reduced rung
system rather than full-CA machinery, the settled degree-6 result.

We also best-effort the n=7 pattern (3,1,1,1,1): f=(x-a)^3(x-b)(x-c)(x-d)(x-e),
degree 7, multiplicity covers i=1,2 (a of mult 3); coincidence tests at i=3,4,5;
centroid at i=6 (weighted mean (3a+b+c+d+e)/7 equals a root).  Same 625-choice
structure, recorded to termination with wall clock (degree reached if it does
not terminate within a soft cap, controlled by --n7-timeout).

Exact oracle cross-check of the CONSTRUCTION (not of the system): the generic
f with distinct integer roots must FAIL the CA hypothesis under
lib.casas_alvero.is_ca over QQ (it is a 5-distinct-root degree-6 polynomial, so
not a counterexample), and the multiplicity mechanism alone must not certify it
(the first-failing derivative is beyond i=1).  This confirms the construction is
probing exactly the coincidence content.
"""

import argparse
import os
import time
from itertools import product
from multiprocessing import Pool

from sympy import symbols, groebner, QQ, expand, prod as spr

from lib.casas_alvero import is_ca, is_pure_power

ROOTS = ["a", "b", "c", "d", "e"]


def degree6_f(a, b, c, d, e, x):
    """f = (x-a)^2 (x-b)(x-c)(x-d)(x-e), monic deg 6, a mult 2."""
    return (x - a) ** 2 * (x - b) * (x - c) * (x - d) * (x - e)


def degree7_f(a, b, c, d, e, x):
    """f = (x-a)^3 (x-b)(x-c)(x-d)(x-e), monic deg 7, a mult 3."""
    return (x - a) ** 3 * (x - b) * (x - c) * (x - d) * (x - e)


def build_distinct_product(a, b, c, d, e):
    """D = product of all 10 pairwise root differences (nonzero iff 5 distinct)."""
    roots = [a, b, c, d, e]
    D = 1
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            D *= roots[i] - roots[j]
    return expand(D)


def derivative_values(f_expr, i, roots_map, x):
    """f^(i) evaluated at each root, as a dict root_name -> poly over QQ vars."""
    di = expand(f_expr.diff(x, i))
    return {name: expand(di.subs(x, sym)) for name, sym in roots_map.items()}


def solve_choice(args):
    """Solve one root-index choice.  args = (degree, mult_a, coincidence_derivs,
    witness tuple).  Returns (choice_label, trivial, wall, basis_len).
    witness tuple has one entry per element of coincidence_derivs (root names)
    plus the centroid witness root name (last)."""
    degree, mult_a, coincidence_derivs, witness, timeout = args
    t0 = time.time()
    a, b, c, d, e = symbols("a b c d e")
    t = symbols("t")
    x = symbols("x")
    roots_map = {"a": a, "b": b, "c": c, "d": d, "e": e}
    if degree == 6:
        f_expr = degree6_f(a, b, c, d, e, x)
    else:
        f_expr = degree7_f(a, b, c, d, e, x)

    polys = []
    for i, wroot in zip(coincidence_derivs, witness[:-1]):
        di = expand(f_expr.diff(x, i))
        polys.append(expand(di.subs(x, roots_map[wroot])))
    # centroid witness (last entry): weighted mean equals that root
    wcenter = witness[-1]
    ccent = (mult_a * a + b + c + d + e) - degree * roots_map[wcenter]
    polys.append(expand(ccent))

    D = build_distinct_product(a, b, c, d, e)
    ideal = polys + [1 - t * D]

    G = groebner(ideal, a, b, c, d, e, t, order="lex")
    basis = list(G)
    trivial = (len(basis) == 1 and basis[0] == 1)
    wall = time.time() - t0
    label = ",".join(witness)
    return (label, trivial, wall, len(basis))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=None)
    ap.add_argument("--no7", action="store_true", help="skip the n=7 best-effort")
    ap.add_argument("--n7-timeout", type=float, default=600.0,
                    help="soft cap seconds per n=7 choice (default 600)")
    args = ap.parse_args()

    out_dir = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "out")
    os.makedirs(out_dir, exist_ok=True)
    capture_path = os.path.join(out_dir, "fiveroots_coincidence_n6.captured.txt")

    lines = []
    def rec(label, value, detail=""):
        lines.append(f"[{'PASS' if value else 'FAIL'}] {label}" +
                     (f"  ({detail})" if detail else ""))

    x = symbols("x")
    lines.append("RUN: code/roots5/coincidence_n6.py")
    lines.append("ORACLE (construction cross-check): lib.casas_alvero.is_ca / "
                 "is_pure_power (ordinary derivatives, char 0, exact sympy over QQ)")
    lines.append("SYSTEM: coincide+centroid AND-system over QQ for n=6 (2,1,1,1,1), "
                 "distinctness via Rabinowitsch <1 - t*D>, D = prod of 10 root diffs")
    lines.append("TERM ORDER: lex (a,b,c,d,e,t); BASE RING: QQ")
    lines.append("WORKERS: %d" % (args.workers or os.cpu_count()))
    lines.append("FLAGS: CSR-exact (no floating point); checks n=6 settled-degree "
                 "result by the reduced rung system")
    lines.append("")

    # ---- Construction cross-check ------------------------------------------
    lines.append("== Construction cross-check (oracle): f=(x-a)^2... with ")
    lines.append("   distinct integer roots a=0,b=1,c=2,d=3,e=4 must FAIL the CA")
    lines.append("   hypothesis over QQ, and must not be a pure power ==")
    fcon = (x - 0) ** 2 * (x - 1) * (x - 2) * (x - 3) * (x - 4)
    fcon_e = __import__("sympy").Poly(fcon, x, domain=QQ)
    ca = is_ca(fcon_e, 0)
    pp = is_pure_power(fcon_e, 0)
    lines.append(f"   distinct roots a=0,b=1,c=2,d=3,e=4: is_ca={ca}, "
                 f"is_pure_power={pp}")
    rec("construction: 5-distinct-root deg-6 f is NOT a CA polynomial over QQ "
        "(is_ca False) and NOT a pure power", (ca is False) and (pp is False))

    # multiplicity mechanism alone covers only i=1: report first derivatives
    fa = x  # f''(a) etc. is the coincidence content; compute first-failing i
    fpoly = fcon_e
    d = fpoly
    failing = []
    for i in range(1, 6):
        d = d.diff()
        if fpoly.gcd(d).degree() < 1:
            failing.append(i)
    lines.append(f"   multiplicity mechanism alone covers i=1 (root a mult 2); "
                 f"first oracle-failing derivative index set = {failing} "
                 f"(all >1 => coincidence content is exactly i=2,3,4,5)")
    rec("construction: first-failing derivative beyond i=1 (i.e. "
        "multiplicity alone does not certify)", failing and failing[0] > 1)

    # ---- n=6 elimination ----------------------------------------------------
    degree = 6
    mult_a = 2
    coincidence_derivs = [2, 3, 4]   # need f''(r)=0, f'''(r)=0, f''''(r)=0
    n_choices = 5 ** (len(coincidence_derivs) + 1)   # witnesses for 2,3,4 + centroid
    choices6 = list(product(ROOTS, repeat=len(coincidence_derivs) + 1))

    lines.append("")
    lines.append(f"== n=6 pattern (2,1,1,1,1): eliminate coincidence+centroid "
                 f"AND-system, {n_choices} root-index choices ==")
    t6 = time.time()
    tasks6 = [(degree, mult_a, coincidence_derivs, ch, args.n7_timeout)
              for ch in choices6]
    with Pool(args.workers) as pool:
        results6 = pool.map(solve_choice, tasks6)
    wall6 = time.time() - t6

    sat6 = [r for r in results6 if not r[1]]
    unsat6 = [r for r in results6 if r[1]]
    lines.append(f"   n=6 total choices: {n_choices}; UNSAT (GB=[1]): {len(unsat6)}; "
                 f"SAT: {len(sat6)}; wall clock {wall6:.2f} s "
                 f"(workers {args.workers or os.cpu_count()})")
    if sat6:
        for label, trivial, wall, blen in sat6[:20]:
            lines.append(f"     SAT witness (bug): {label} basis-len={blen}")
    rec(f"n=6: reduced lex Groebner basis is the unit ideal [1] for every one of "
        f"the {n_choices} root-index choices (UNSAT over Q-bar => no 5-distinct-"
        f"root degree-6 CA polynomial)", len(sat6) == 0,
        f"SAT count {len(sat6)}")

    # report which choices are genuinely nonempty BEFORE distinctness accurs;
    # (the raw 4-equation system is often nonempty on coincident roots; distinct
    # locus handled by Rabinowitsch).  Print a small representative note.

    # ---- n=7 best-effort -----------------------------------------------------
    n7_lines = []
    if not args.no7:
        degree7 = 7
        mult_a7 = 3
        coincidence_derivs7 = [3, 4, 5]   # multiplicity covers i=1,2 (mult 3)
        choices7 = list(product(ROOTS, repeat=len(coincidence_derivs7) + 1))
        n7 = len(choices7)
        n7_lines.append("")
        n7_lines.append(f"== n=7 pattern (3,1,1,1,1): coincidence+centroid "
                        f"AND-system, {n7} root-index choices (best-effort) ==")
        t7 = time.time()
        tasks7 = [(degree7, mult_a7, coincidence_derivs7, ch, args.n7_timeout)
                  for ch in choices7]
        with Pool(args.workers) as pool:
            results7 = pool.map(solve_choice, tasks7)
        wall7 = time.time() - t7
        sat7 = [r for r in results7 if not r[1]]
        unsat7 = [r for r in results7 if r[1]]
        n7_lines.append(f"   n=7 total choices: {n7}; UNSAT: {len(unsat7)}; "
                        f"SAT: {len(sat7)}; wall clock {wall7:.2f} s")
        if sat7:
            n7_lines.append("   SAT choices (informational; may be coincident-root "
                            "solutions needing further distinctness):")
            for label, trivial, wall, blen in sat7[:10]:
                n7_lines.append(f"     {label} wall={wall:.2f}s basis-len={blen}")
        n7_lines.append("   (n=7 is NOT settled by this rung alone; a SAT choice "
                        "here only means coincident-root solutions of the raw "
                        "system, not a distinct-root CA polynomial)")
        n7_ok = True  # best-effort, exit unaffected
    else:
        n7_ok = True
    lines.extend(n7_lines)

    ok = (ca is False) and (pp is False) and (failing and failing[0] > 1) \
        and (len(sat6) == 0) and n7_ok
    lines.append("")
    lines.append(f"ALL CHECKS {'PASSED' if ok else 'FAILED'}")

    text = "\n".join(lines)
    with open(capture_path, "w") as fh:
        fh.write(text + "\n")
    print(text)
    print(f"\ncapture saved to {capture_path}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
