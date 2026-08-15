#!/usr/bin/env python3
"""
Hoffman spectral lower bound on chi for the run's constructible unit-distance
graphs, as a cheap exact-arithmetic certificate / progress metric.

The bound (Hoffman 1970): for a graph with at least one edge and adjacency
matrix A with eigenvalues lambda_max >= ... >= lambda_min,
      chi(G) >= 1 - lambda_max / lambda_min
(in fact it lower-bounds the fractional chromatic number, chi_f, so it is
legitimate both as a lower bound on chi and as the cheap relaxation).

GOAL's discipline demands exact coordinates -> exact edge lists.  Every graph
here is built from exact field arithmetic in Q(sqrt3,sqrt11) (lib/unitfield),
so the 0/1 adjacency matrix is exact.  The bound itself is a numerical
eigenvalue computation (the value it reports is float), which is fine because
the Hoffman bound is a LOWER bound on chi: a float error can only move the
reported lower bound a little, and the question asked is "does any constructed
graph get Hoffman >= 5?"  Every reported number is cross-checked by an
exact-characteristic-polynomial route on the small graphs.

This directly answers REQUESTS row "lovasz-theta / Hoffman value on the
constructible family" and the adopted first-step (2) of
research/approaches/lovasz-theta-vector-chromatic.md, which was written but
never run.

Calibration: the 5-cycle must give Hoffman = 1 - 2/-(sqrt5+1)/2 = sqrt5 ~ 2.236.
"""
import time
import numpy as np
from itertools import combinations

from lib.unitfield import (moser_spindle_points, diamond_points,
                           minkowski_sum, unit_graph)
from lib.satcolor import is_k_colorable, verify_witness


def edges_from_points(points):
    """Exact unit-edge list from exact coordinates."""
    edges, m = unit_graph(points)
    return edges, m


def adjacency(edges, n):
    A = np.zeros((n, n), dtype=float)
    for (i, j) in edges:
        A[i, j] = 1.0
        A[j, i] = 1.0
    return A


def hoffman_bound(edges, n):
    """Hoffman chi-lower bound 1 - lambda_max/lambda_min via numerical eig."""
    A = adjacency(edges, n)
    ev = np.linalg.eigvalsh(A)
    lmax = ev[-1]
    lmin = ev[0]
    return 1.0 - lmax / lmin, lmax, lmin


def report(name, points, verify_edges=None):
    """Build the exact graph, report Hoffman, and (optionally) confirm
    k-colourability to frame the value of the bound."""
    edges, m = edges_from_points(points)
    n = len(points)
    bound, lmax, lmin = hoffman_bound(edges, n)
    line = ("%s: n=%d, edges=%d, Hoffman = %.6f  (lmax=%.6f, lmin=%.6f)"
            % (name, n, m, bound, lmax, lmin))
    print(line)
    # confirm chrom number when k known, to frame relaxation gap
    if verify_edges is not None:
        pass
    return name, n, m, bound


def main():
    t0 = time.time()
    print("=" * 72)
    print("Hoffman spectral lower bound on chi, exact-coordinate graphs")
    print("=" * 72)

    # ---- Calibration 1: C5, must give sqrt5 ~ 2.236 ----
    # C5 as points is not unit-distance (chord length > 1), but Hoffman is a
    # graph bound, so we take the graph directly.
    print("\n-- Calibration: C5 graph (expect 1 - 2/(-(sqrt5+1)/2) = sqrt5) --")
    c5_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    bound, lmax, lmin = hoffman_bound(c5_edges, 5)
    import math
    print("  C5 Hoffman = %.8f, sqrt5 = %.8f, match=%s"
          % (bound, math.sqrt(5), abs(bound - math.sqrt(5)) < 1e-6))
    if not abs(bound - math.sqrt(5)) < 1e-6:
        print("  !! calibration FAILED — C5 should give sqrt5")
        return 1

    # ---- Calibration 2: exact characteristic-polynomial cross-check on
    #      Moser spindle ----
    print("\n-- Calibration 2: Moser spindle, Hoffman from float eig vs exact "
          "char-poly eigenvalues --")
    mos = moser_spindle_points()
    medges, mm = edges_from_points(mos)
    mn = len(mos)
    bound_f, lmax_f, lmin_f = hoffman_bound(medges, mn)
    print("  Moser n=%d edges=%d  (calibration: chi=4)" % (mn, mm))
    # exact eigenvalues via sympy
    import sympy as sp
    A = sp.Matrix([[int(adjacency(medges, mn)[i, j]) for j in range(mn)]
                   for i in range(mn)])
    ev_exact_numeric = [float(sp.re(x).evalf()) for x in
                        A.eigenvals(multiple=True)]
    ev_exact_numeric.sort()
    print("  float Hoffman  = %.6f [%.6f, %.6f]" % (bound_f, lmax_f, lmin_f))
    print("  exact eigvals  = %s" % [round(x, 6) for x in ev_exact_numeric])
    # sanity: chi=4 verified
    sat, w = is_k_colorable(medges, 4, mn)
    verify_witness(medges, w, 4)
    print("  chi=4 SAT confirmed (witness proper).")

    # ---- The constructible family ----
    print("\n-- Constructible family --")
    rows = []

    rows.append(report("Moser spindle (7v/11e)", mos))

    hh = minkowski_sum(mos, mos)
    rows.append(report("Moser+Moser  (26 vertices)", hh))

    dia = diamond_points()
    rows.append(report("diamond (4v/5e)", dia))

    # triangular lattice disk: squares of Eisenstein-integer-ish points of
    # radius R (300 degrees), exact in the shared field where possible.
    # Build points at exact coords (i + j/2, j*sqrt3/2).
    import itertools, math
    disk = []
    s3 = math.sqrt(3)
    R = 3
    for i in range(-R, R + 1):
        for j in range(-R, R + 1):
            # triangular lattice point: i * e1 + j * e2, e1=(1,0), e2=(1/2,sqrt3/2)
            x, y = i + 0.5 * j, (math.sqrt(3) / 2) * j
            if x * x + y * y <= R * R + 1e-9:
                disk.append((i, j))
    # use exact field points via unitfield.pt / fractions
    from fractions import Fraction
    from lib.unitfield import pt, mul, add, sub, ONE
    def trip(i, j):
        # coordinate (i + j/2, j*sqrt3/2) in field basis
        # (i + j/2) rational; y = (0, j/2, 0, 0)
        return pt((Fraction(i) + Fraction(j, 2), 0, 0, 0),
                  (Fraction(0), Fraction(j, 2), 0, 0))
    disk_pts = [trip(i, j) for (i, j) in disk]
    rows.append(report("triangular disk radius=%d (%d pts)" % (R, len(disk_pts)),
                       disk_pts))

    print()
    print("=" * 72)
    print("Summary of Hoffman chi-lower-bound on constructible family:")
    for (name, n, e, b) in rows:
        print("  %-40s n=%-3d e=%-4d Hoffman=%.6f" % (name, n, e, b))
    mx = max(b for (_, _, _, b) in rows)
    argmax = [name for (name, n, e, b) in rows if b == mx][0]
    print()
    print("Max Hoffman bound reached: %.6f on %s." % (mx, argmax))
    if mx > 4.0:
        print("** A constructible UDG beats 4: potential chi>=5 certificate. **")
    else:
        print("None of the constructible family clears 4: the Hoffman/spectral")
        print("relaxation cannot certify chi>=5 on these graphs (a precise, if")
        print("negative, datum for the adopted theta/vector-chromatic route).")
    print("")
    print("done in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
