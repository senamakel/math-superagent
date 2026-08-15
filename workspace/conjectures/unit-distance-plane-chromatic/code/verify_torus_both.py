#!/usr/bin/env python3
"""
Flat-torus periodic 6-colouring: enforce BOTH constraints, exact arithmetic.

A Lambda'-periodic colouring of the plane, constant on radius-rho Voronoi
cells of the A2 lattice, coloured by coset of the finite-index sublattice
Lambda'=<g1,g2>, is PROPER (separation margin > 1) iff

  (A) two distinct cells of the SAME coset are at centre distance > 1+2*rho.
      Same-coset cells always share a colour, so the shortest nonzero vector
      of Lambda' must have physical length > 1+2*rho.
  (B) two cells of DIFFERENT cosets that share a colour are at centre
      distance > 1+2*rho, i.e. the corrected coset-separation graph F
      (edge iff min coset-to-coset distance <= 1+2*rho) is 6-colourable.

The previous corrected sweep checked ONLY (B); this program checks both.
Prediction (to verify): the earlier "6-colourable" rows are artifacts whose
shortest sublattice vector is <= 1+2L, and NO row passes both.

Exact arithmetic in Q(sqrt3) / integers:  centre(u,v) = (sqrt3 L (u-v/2),
3/2 L v), physical sqdist = 3 L^2 * N(du,dv), N = du^2 - du*dv + dv^2.
With L = rho = 2/5: (1+2L)^2 = 81/25, 3L^2 = 12/25, so (A) iff N_min > 81/12
= 27/4, i.e. N_min >= 7 (integer).

Formatting is deliberately str()-only; no sympy value is given a format spec.
"""
import math
import time

import sympy as sp

from lib.torus_minsep import (row_kernel_generators, in_sublattice, N,
                              corrected_separation_graph)
from lib.satcolor import is_k_colorable, verify_witness

Lv = sp.Rational(2, 5)                     # L = rho = 2/5
T2 = sp.expand((1 + 2 * Lv) ** 2)          # 81/25
FAC = sp.simplify(3 * Lv ** 2)             # 12/25
CUT = sp.Rational(81, 12)                  # 27/4 ; A holds iff N_min > CUT


def min_nonzero_N(g1, g2):
    """Exact global minimum of N over NONZERO vectors of <g1,g2>.

    best0 = N(g1) is an achievable nonzero value.  Any sublattice vector with
    N < best0 satisfies u^2+v^2 <= 2N < 2*best0, so the box
    [-ceil(sqrt(2*best0)), +ceil(sqrt(2*best0))]^2 provably contains every
    vector that could beat best0.  All exact integers."""
    best0 = N(g1[0], g1[1])
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


def main():
    rows = [(D, p, q) for D in [7, 13]
            for p in range(1, D) for q in range(-D, D + 1)
            if math.gcd(p, q, D) == 1]
    out = []

    def emit(s=""):
        out.append(str(s))

    emit("=" * 92)
    emit("FLAT-TORUS PERIODIC 6-COLOUR: BOTH (A) shortest-vector AND (B)")
    emit("corrected coset-separation-graph 6-colourability enforced; exact")
    emit("=" * 92)
    emit("L = rho = 2/5 ; threshold (1+2L)^2 = " + str(T2))
    emit("physical sqdist = 3L^2 * N = " + str(FAC) + " * N ; "
         "(A) iff " + str(FAC) + "*N_min > " + str(T2) +
         " iff N_min > " + str(CUT) + " iff N_min >= 7 (integer)")
    emit("rows: gcd(p,q,D)=1, D in {7,13}, p in 1..D-1, q in -D..D  (total "
         + str(len(rows)) + ")")

    both_pass = []
    a_pass = 0
    b_pass = 0
    artifacts = []     # B ok but A fails  -> previously reported 6-colourings
    a_fail_of_b = 0

    emit("")
    emit(" D  row     N_min   phys^2     A?  |E|  6-col?  BOTH?")
    emit("-" * 92)
    t0 = time.time()
    for D, p, q in rows:
        g1, g2 = row_kernel_generators(p, q, D)
        N_min = min_nonzero_N(g1, g2)
        phys2 = FAC * N_min
        A_ok = bool(N_min > CUT)               # N_min >= 7
        n, edges, reps = corrected_separation_graph(g1, g2, D, Lv)
        sat6, w6 = is_k_colorable(edges, 6, n)
        B_ok = bool(sat6)
        if B_ok:
            verify_witness(edges, w6, 6)
        both = A_ok and B_ok

        if A_ok:
            a_pass += 1
        if B_ok:
            b_pass += 1
            if not A_ok:
                a_fail_of_b += 1
                artifacts.append((D, p, q, N_min, len(edges)))
        if both:
            both_pass.append((D, p, q, N_min, len(edges)))

        emit(" " + str(D).rjust(2) + " (" + str(p) + "," + str(q) + ")"
             .rjust(7) + " " + str(N_min).rjust(5) + " " +
             str(phys2).rjust(12) + " " +
             ("Y" if A_ok else "n").rjust(3) + " " +
             str(len(edges)).rjust(4) + " " +
             ("Y" if B_ok else "n").rjust(6) + " " +
             ("YES" if both else "no").rjust(6))

    dt = time.time() - t0
    emit("-" * 92)
    emit("SUMMARY (" + ("%.1f" % dt) + "s):")
    emit("  rows with (A) shortest-vector > 1+2L     : " + str(a_pass))
    emit("  rows with (B) corrected graph 6-colourable: " + str(b_pass) +
         "  <-- the 'previously 6-colourable' rows")
    emit("  of the (B)-pass rows, (A) FAILS           : " + str(a_fail_of_b) +
         "  <-- these are ARTIFACTS")
    emit("  rows passing BOTH (A) and (B)             : " + str(len(both_pass)))

    emit("")
    emit("ARTIFACT ROWS (B ok, A fails): previously reported 6-colourings "
         "refuted by the same-coset constraint")
    if artifacts:
        for (D, p, q, N_min, ec) in artifacts:
            emit("  D=" + str(D) + " row=(" + str(p) + "," + str(q) +
                 "): N_min=" + str(N_min) + " -> phys^2=" + str(FAC * N_min) +
                 " <= " + str(T2) + " so (A) FAILS (same-colour cells too close)")
    else:
        emit("  (none)")
    if both_pass:
        emit("")
        emit("ROWS PASSING BOTH:")
        for (D, p, q, N_min, ec) in both_pass:
            emit("  D=" + str(D) + " row=(" + str(p) + "," + str(q) +
                 "): N_min=" + str(N_min) + " |E|=" + str(ec))
    else:
        emit("")
        emit("ROWS PASSING BOTH: NONE")

    emit("")
    emit("FINAL ANSWER: any row satisfying BOTH (A) and (B)?  " +
         str(bool(both_pass)))
    emit("  (" + str(len(both_pass)) + " of " + str(len(rows)) +
         " rows; " + str(a_pass) + " pass A, " + str(b_pass) + " pass B)")

    print("\n".join(out))


if __name__ == "__main__":
    main()
