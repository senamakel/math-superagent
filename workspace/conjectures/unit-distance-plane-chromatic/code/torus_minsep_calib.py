#!/usr/bin/env python3
"""
Calibration/verification: does ANY flat-torus periodic row (p,q) with
gcd(p,q,D)=1, D in {7,13}, p in 1..D-1, q in -D..D, satisfy BOTH
   (A) shortest nonzero sublattice vector > 1 + 2L    AND
   (B) the corrected coset-separation graph is 6-colourable ?

Exact arithmetic only (sympy, Q(sqrt3); L = rho = 2/5).

Background (from lib/torus_minsep.py): centre(u,v) = (sqrt3 L (u - v/2), 3/2 L v),
so squared PHYSICAL distance for lattice-coordinate difference (du,dv) is
   3 L^2 * N(du,dv),   N(du,dv) = du^2 - du*dv + dv^2.
The periodic colour is PROPER iff
   (A) two distinct cells of the SAME coset are at centre distance > 1+2rho,
       i.e. the shortest nonzero vector of Lambda' = <g1,g2> has physical
       length > 1+2rho,   AND
   (B) two cells of DIFFERENT cosets are at centre distance > 1+2rho, i.e.
       the coset-separation graph F (edge iff min-coset-distance <= 1+2rho)
       is 6-colourable.
The existing corrected_sweep checks ONLY (B); its "6-colourings" are
suspected artifacts violating (A).  This program checks both.

With L=rho=2/5:  physical length^2 = 3 L^2 N = (12/25) * N ; threshold
(1+2L)^2 = (9/5)^2 = 81/25.  (A) holds iff  (12/25) N_min > 81/25  iff
N_min > 81/12 = 27/4 = 6.75  iff  N_min >= 7  (N_min an integer).

Certified nonzero minimum: any nonzero generator g1=(q_,-p_) <= a value
best0 = N(g1) > 0 achievable as a nonzero sublattice vector.  Any sublattice
vector with N < best0 satisfies u^2+v^2 <= 2*N < 2*best0, so scanning u,v in
[ -ceil(sqrt(2*best0)) .. ceil(sqrt(2*best0)) ] provably finds the global
nonzero minimum of N over Lambda' (N >= (u^2+v^2)/2).  All exact integers.
"""
import math
import time

import sympy as sp

from lib.torus_minsep import (row_kernel_generators, in_sublattice, N,
                              corrected_separation_graph)
from lib.satcolor import is_k_colorable, verify_witness

Lv = sp.Rational(2, 5)                 # L = rho = 2/5
T2 = sp.expand((1 + 2 * Lv) ** 2)      # (1+2L)^2 = 81/25
SQDIST_FACTOR = sp.simplify(3 * Lv ** 2)   # 12/25
N_CUTOFF = sp.Rational(81, 12)         # = 27/4 ; A holds iff N_min > this


def min_nonzero_N(g1, g2):
    """Exact integer minimum of N(u,v) over NONZERO (u,v) in Lambda'=<g1,g2>,
    provably the global minimum (certified box as derived above)."""
    best0 = N(g1[0], g1[1])            # nonzero, in Lambda' -> achievable upper bound
    assert best0 > 0
    R = int(math.ceil(math.sqrt(2 * best0))) + 1
    best = None
    for u in range(-R, R + 1):
        for v in range(-R, R + 1):
            if (u, v) == (0, 0):
                continue
            if in_sublattice(u, v, g1, g2):
                val = N(u, v)
                if best is None or val < best:
                    best = val
    assert best is not None and best <= best0
    return best


def sweep_rows(D):
    rows = []
    for p in range(1, D):
        for q in range(-D, D + 1):
            if math.gcd(p, q, D) == 1:
                rows.append((p, q))
    return rows


def main():
    rows_all = [(D, p, q) for D in [7, 13] for (p, q) in sweep_rows(D)]
    out = []
    def emit(s=""):
        out.append(str(s))

    emit("=" * 92)
    emit("FLAT-TORUS PERIODIC 6-COLOUR CALIBRATION: (A) shortest-vector AND (B)")
    emit("corrected-separation-graph 6-colourability, both enforced, exact Q(sqrt3)")
    emit("=" * 92)
    emit(f"L = rho = 2/5 ;  edge threshold (1+2L)^2 = {T2}")
    emit(f"physical sqdist = 3L^2 * N = {SQDIST_FACTOR} * N ;  "
         f"(A) holds iff {SQDIST_FACTOR}*N_min > {T2}  iff  N_min > {N_CUTOFF}  "
         f"(integer N_min >= 7)")
    emit(f"rows: gcd(p,q,D)=1, D in {{7,13}}, p in 1..D-1, q in -D..D  "
         f"(total {len(rows_all)})")

    both_pass = []
    a_pass_rows = []
    b_pass_rows = []
    a_fail_of_b_pass = []

    header = (f"{'D':>2} {'row':>7} {'N_min':>5} {'phys^2':>12} {'A?':>4} "
              f"{'|E|':>4} {'6-col?':>7} {'BOTH?':>6}")
    emit("\n" + header)
    emit("-" * 92)

    t_start = time.time()
    for D, p, q in rows_all:
        g1, g2 = row_kernel_generators(p, q, D)
        N_min = min_nonzero_N(g1, g2)
        phys2 = SQDIST_FACTOR * N_min               # exact rational 12/25 * N_min
        A_ok = N_min > N_CUTOFF                       # exact: N_min >= 7
        # (B) corrected coset separation graph 6-colourability
        n, edges, reps = corrected_separation_graph(g1, g2, D, Lv)
        sat6, w6 = is_k_colorable(edges, 6, n)
        B_ok = bool(sat6)
        if B_ok:
            verify_witness(edges, w6, 6)
        both = A_ok and B_ok

        if A_ok:
            a_pass_rows.append((D, p, q, N_min))
        if B_ok:
            b_pass_rows.append((D, p, q, N_min, len(edges)))
            if not A_ok:
                a_fail_of_b_pass.append((D, p, q, N_min))
        if both:
            both_pass.append((D, p, q, N_min, len(edges)))

        emit(f"{D:>2} {('('+str(p)+','+str(q)+')'):>7} {N_min:>5} "
             f"{str(sp.nsimplify(phys2)):>12} {('Y' if A_ok else 'n'):>4} "
             f"{len(edges):>4} {('Y' if B_ok else 'n'):>7} "
             f"{('YES' if both else 'no'):>6}")

    dt = time.time() - t_start
    emit("-" * 92)

    emit(f"\nSUMMARY  ({dt:.1f}s):")
    emit(f"  rows with (A) shortest-vector>1+2L  : {len(a_pass_rows)}")
    emit(f"  rows with (B) corrected graph 6-col : {len(b_pass_rows)}  "
         f"(these are the 'previously 6-colourable' rows)")
    emit(f"  of the (B)-pass rows, (A) FAILS     : {len(a_fail_of_b_pass)}  "
         f"-> these are the ARTIFACTS (6-colourable but not proper)")
    before = len(b_pass_rows)
    after = len(a_fail_of_b_pass)
    emit(f"  rows passing BOTH (A) and (B)       : {len(both_pass)}")
    emit(f"  => of the {before} rows reported as 6-colourable, {after} are "
         f"artifacts violating (A); {len(both_pass)} remain genuinely proper 6-colourings")

    emit("\nARTIFACT ROWS (B ok, A fails):  'previously 6-colourable' rows refuted")
    if a_fail_of_b_pass:
        for (D, p, q, N_min) in a_fail_of_b_pass:
            emit(f"    D={D} row=({p},{q}): N_min={N_min} -> physical^2={SQDIST_FACTOR}*{N_min}"
                 f"={sp.nsimplify(SQDIST_FACTOR*N_min)} <= {T2}, so (A) FAILS")
    else:
        emit("    (none)")

    if both_pass:
        emit("\nROWS PASSING BOTH:")
        for (D, p, q, N_min, ec) in both_pass:
            emit(f"    D={D} row=({p},{q}): N_min={N_min}, |E|={ec}")
    else:
        emit("\nROWS PASSING BOTH: NONE")

    emit("\nFINAL ANSWER: does ANY row satisfy BOTH (A) and (B)?  "
         f"{bool(both_pass)}")
    emit(f"  {len(both_pass)} row(s) pass both "
         f"(of {len(rows_all)} rows, {len(a_pass_rows)} pass A, "
         f"{len(b_pass_rows)} pass B).")

    print("\n".join(out))


if __name__ == "__main__":
    main()
