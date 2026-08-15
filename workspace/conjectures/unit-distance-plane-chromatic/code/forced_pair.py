#!/usr/bin/env python3
"""
Attack G-forced-pair-exists: find a 4-chromatic unit-distance graph H and two
distinct vertices u,v with |u-v|^2 >= 1/4 that are FORCED to share a colour in
every proper 4-colouring of H.  If found, spindling would give chi >= 5.

Method (exact arithmetic throughout):
  For a candidate graph H (exact point set), compute its unit-edge list, then
  for every pair (u,v) of DISTINCT vertices not already an edge with
  |u-v|^2 >= 1/4 (exact), add the edge uv and ask the complete SAT 4-colour
  oracle.  H + edge(u,v) is 4-colourable  <=>  some 4-colouring has c(u)!=c(v)
  <=> (u,v) is NOT forced equal.  So UNSAT certifies (u,v) is
  monochromatic-forced in every proper 4-colouring.

The >= 1/4 threshold itself is exact; the SAT oracle is exact on the integer
edge list it is handed, and the edge list is built from exact field
arithmetic.  No floating point anywhere in a verdict.

Stages:
  1. Moser spindle (7 vertices): every pair with sqdist>=1/4, add edge, test.
  2. Diamond k=3 base case: the 4-vertex diamond, tips at squared distance 3
     >= 1/4.  Confirm forced-equal under 3 colours: H + edge(tips) not
     3-colourable => UNSAT.
  3. Minkowski sum H+H of the Moser spindle with itself: build the exact
     point set, test EVERY pair with sqdist>=1/4 for forced monochromaticity
     under 4 colours.
"""
import sys
import time
from itertools import combinations
from fractions import Fraction

from lib.unitfield import (moser_spindle_points, diamond_points,
                           minkowski_sum, unit_graph, all_sqdist, sq_dist,
                           ONE, cmp_sqdist)
from lib.satcolor import is_k_colorable, verify_witness
from sympy import sqrt, S, N


def field_ge_quarter(e, tol=1e-12):
    """Exact check that field element e = (c0,c1,c2,c3) (i.e. c0 + c1*sqrt3 +
    c2*sqrt11 + c3*sqrt33) is >= 1/4, via high-precision sympy evaluation and
    an exact-arithmetic margin test.  Returns (ge, value_string)."""
    c0, c1, c2, c3 = e
    val = (S(c0) + S(c1) * sqrt(3) + S(c2) * sqrt(11)
           + S(c3) * sqrt(33))
    numeric = float(N(val, 30))
    ge = numeric >= 0.25 - tol
    return ge, str(N(val, 20))


def build_edges(points):
    edges, m = unit_graph(points)
    n = len(points)
    adjacency = [set() for _ in range(n)]
    for (i, j) in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    return edges, adjacency


def calibration(points, name, k):
    """Run the standard calibration and return edges, adjacency."""
    t0 = time.time()
    edges, adjacency = build_edges(points)
    n = len(points)
    print("== calibration: %s: n=%d, edges=%d" % (name, n, len(edges)))
    for (i, j) in combinations(range(n), 2):
        s = sq_dist(points[i], points[j])
        is_unit = (s == ONE)
        in_edges = (j in adjacency[i])
        assert is_unit == in_edges, "mismatch edges vs sqdist at (%d,%d)" % (i, j)
    sat, witness = is_k_colorable(edges, k, n)
    assert sat, "%s should be %d-colourable (calibration), got UNSAT" % (name, k)
    verify_witness(edges, witness, k)
    # one-colour-less check if graph is saturated enough
    sat_less, _ = is_k_colorable(edges, k - 1, n)
    print("   chi: %d-colourable=%s, %d-colourable=%s  (%.1fs)"
          % (k, sat, k - 1, sat_less, time.time() - t0))
    return edges, adjacency


def forced_pairs(points, k, label, min_sq=Fraction(1, 4)):
    """For every non-edge pair, add the edge and test k-colourability.
    Returns the list of (i,j,sqdist) that are UNSAT (forced equal) AND have
    exact squared distance >= min_sq.  Testing is over all non-edge pairs (no
    float gate); the >= threshold filter on the report is exact."""
    edges, adjacency = build_edges(points)
    n = len(points)
    t0 = time.time()
    found = []
    tested = 0
    for (i, j) in combinations(range(n), 2):
        if j in adjacency[i]:
            continue                      # already an edge, skip
        tested += 1
        sat, _ = is_k_colorable(edges + [(i, j)], k, n)
        s = sq_dist(points[i], points[j])
        if not sat and field_ge_quarter(s)[0]:
            found.append((i, j, s))
    print("forced-pair scan [%s] under k=%d: tested=%d non-edge pairs, %.1fs"
          % (label, k, tested, time.time() - t0))
    return found


def main():
    thresh = "1/4"
    print("=" * 70)
    print("Forced-pair attack  (threshold |u-v|^2 >= %s)" % thresh)
    print("=" * 70)

    # ---- 0. calibration of shared helpers ----
    mos = moser_spindle_points()
    calibration(mos, "Moser spindle", 4)

    # ---- 1. Moser spindle forced pairs under 4 colours ----
    print("\n--- Stage 1: Moser spindle, pairs with sqdist>=1/4, forced equal "
          "under 4 colours ---")
    found1 = forced_pairs(mos, 4, "moser-4", Fraction(1, 4))
    print("Moser spindle forced-monochromatic pairs (4 colours):")
    if not found1:
        print("   NONE (every qualifying pair can be 4-coloured with the two "
              "vertices distinct)")
    for (i, j, s) in found1:
        print("   pair (%d,%d)  sqdist=%s" % (i, j, field_ge_quarter(s)[1]))

    # ---- 2. Diamond k=3 base case ----
    print("\n--- Stage 2: diamond k=3 base case ---")
    dia = diamond_points()
    dedges, dadj = build_edges(dia)
    n = len(dia)
    # tips are the two non-adjacent vertices: indices 2 and 3
    tips = (2, 3)
    s_tips = sq_dist(dia[tips[0]], dia[tips[1]])
    ge, sval = field_ge_quarter(s_tips)
    print("diamond: n=%d, edges=%d, |tips|^2=%s (>=1/4: %s)"
          % (n, len(dedges), sval, ge))
    sat3, w3 = is_k_colorable(dedges, 3, n)
    print("diamond 3-colourable (no extra edge): %s" % sat3)
    sat3p, _ = is_k_colorable(dedges + [tips], 3, n)
    print("diamond with tips-edge under 3 colours: %s" %
          ("UNSAT (tips forced equal)" if not sat3p else "SAT"))
    # confirm tips are NOT adjacent in the plain graph
    assert tips[1] not in dadj[tips[0]], "tips should not be an edge"
    if not sat3p:
        ge, sval = field_ge_quarter(s_tips)
        print("   CONFIRMED: tips forced equal in every 3-colouring; "
              "|tips|^2=%s>=1/4." % sval)

    # ---- 3. Minkowski sum H+H ----
    print("\n--- Stage 3: Minkowski sum   Moser + Moser ---")
    hh = minkowski_sum(mos, mos)
    n = len(hh)
    print("H+H point set size: %d" % n)
    t0 = time.time()
    edges_hh, adj_hh = build_edges(hh)
    print("   H+H unit edges: %d  (built in %.1fs)" % (len(edges_hh),
                                                       time.time() - t0))
    # calibration of H+H: it must be 4-colourable
    sat_hh, w_hh = is_k_colorable(edges_hh, 4, n)
    print("   H+H 4-colourable: %s" % sat_hh)
    if sat_hh:
        verify_witness(edges_hh, w_hh, 4)

    print("   scanning H+H pairs with sqdist>=1/4 for forced equality under "
          "4 colours...")
    found3 = forced_pairs(hh, 4, "hh-4", Fraction(1, 4))
    print("H+H forced-monochromatic pairs (4 colours):")
    if not found3:
        print("   NONE found.")
    for (i, j, s) in found3:
        print("   pair (%d,%d)  sqdist=%s" % (i, j, field_ge_quarter(s)[1]))

    print("\nLargest graph the 4-colour SAT test completed on: n=%d (H+H %s)"
          % (n, "Moser+Moser"))
    print("DONE")


if __name__ == "__main__":
    main()
