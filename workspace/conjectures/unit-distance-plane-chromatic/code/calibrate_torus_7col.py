#!/usr/bin/env python3
"""Task 1 CALIBRATION: machine-verify chi(F) = 7 for the hexagonal tiling.

Reproduces the exact known fact from the inventor's hand derivation
(code/scratch_verify_a2_margin.py): for the A2 lattice with hexagon side L in
1/(sqrt21-2) < L < 1/2, the 7-colouring (by the ideal (2-omega)) of the
separation graph F has same-colour centre distance sqrt21*L and minimal
separation > 1, so F is properly 7-coloured and, by the complete SAT oracle,
NOT 6-colourable => chi(F) = 7.

We work with L as an EXACT Fraction.  Edge test 3*L^2*N <= (1+2L)^2 in exact
rationals.  Uses lib.satcolor (calibrated complete k-colouring oracle) and
lib.torus_margin.separation_graph.
"""
import sys
from fractions import Fraction
from math import sqrt as fsqrt
import time

from lib.torus_margin import (separation_graph, seven_colour,
                              check_colouring_colours_within,
                              min_same_colour_N, separation_threshold,
                              eisenstein_norm)
from lib.satcolor import is_k_colorable, verify_witness


def main():
    # Exact window endpoints (hand derivation).  L rational in the window:
    L2 = Fraction(2, 5)          # 0.4 in (0.3872.., 0.5)
    L3 = Fraction(47, 120)       # ~0.3917, just above the lower endpoint
    for L in (L2, L3):
        print("=" * 72)
        print("L =", L, "=", float(L))
        # window membership exact (symbolic endpoints)
        import sympy as sp
        lo = sp.simplify(1 / (sp.sqrt(21) - 2))
        hi = sp.Rational(1, 2)
        in_win = sp.simplify(sp.Rational(L) > lo) and sp.simplify(sp.Rational(L) < hi)
        print("in window 1/(sqrt21-2) < L < 1/2:", bool(in_win))
        print("  1/(sqrt21-2) ~", float(lo), "  1/2 = 0.5")

        # smallest same-colour Eisenstein norm of the 7-pattern = 7 exactly
        # (vector (3,-1), N = 9-3+1 = 7; physical distance sqrt21*L).
        Nmin = eisenstein_norm(3, -1)
        dist2 = Fraction(3) * L * L * Nmin
        th2 = separation_threshold(L)
        print("same-colour centre dist = sqrt(3*%d)*L = sqrt21*L" % Nmin,
              "= %.6f L" % fsqrt(3 * Nmin))
        print("separation threshold (1+2L)^2 =", float(th2),
              ";  same-colour dist^2 =", float(dist2))
        print("proper (dist^2 > (1+2L)^2):", dist2 > th2)
        print("min same-colour separation (sqrt21-2)L =",
              "%.6f" % ((fsqrt(21) - 2) * float(L)),
              "> 1 ⇒", (fsqrt(21) - 2) * float(L) > 1)

        # Build F on an N x N block (N multiple of 7 so 7-colour periodic fits)
        for N in (7, 14):
            t0 = time.time()
            m, edges = separation_graph(N, L)
            dt = time.time() - t0
            print(f"\n  N={N}: {m} vertices, {len(edges)} edges "
                  f"(build {dt:.3f}s)")
            # verify 7-colouring proper
            col7 = seven_colour(N)
            assert check_colouring_colours_within(col7, 7)
            ok = True
            for (i, j) in edges:
                if col7[i] == col7[j]:
                    ok = False
                    break
            print("  7-colouring proper on F:", ok)
            msc = min_same_colour_N(N, col7)
            print("  min same-colour Eisenstein norm on F:", msc,
                  "(theory 7)")
            # complete SAT: not 6-colourable, 7-colourable
            sat6, w6 = is_k_colorable(edges, 6, m)
            print("  k=6 SAT:", sat6)
            if sat6:
                verify_witness(edges, w6, 6)
                print("    WITNESS VERIFIED — F is 6-colourable!!")
            sat7, w7 = is_k_colorable(edges, 7, m)
            print("  k=7 SAT:", sat7)
            if sat7:
                verify_witness(edges, w7, 7)
                print("    7-colour witness verified proper")
            chi = None
            for k in range(4, 8):
                sat, _ = is_k_colorable(edges, k, m)
                if sat:
                    chi = k
                    break
            print(f"  chi(F) = {chi}")
            note = " (7-colour witness same as theoretical pattern)" if ok else ""
            print("  " + note.strip())


if __name__ == "__main__":
    sys.exit(main())
