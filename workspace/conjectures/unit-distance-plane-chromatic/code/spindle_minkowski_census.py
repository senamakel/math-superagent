#!/usr/bin/env python3
"""
spindle_minkowski_census.py

Exact census of Minkowski sums of the 7-vertex spindle A from problem.md.

  A = moser_spindle_points()          # 7 points in Q(sqrt3, sqrt11)
  A^k = { a_1 + ... + a_k }           # k-fold Minkowski sum

For level k (argv[1], default 2) this measures, EXACT arithmetic throughout:

    n  = number of distinct points of A^k
    e  = number of pairs at distance exactly 1, certified by TWO
         independent engines:
           (1) brute.is_unit  -- |p-q|^2 == 1 as tuple equality in the
               hand-written field Q(sqrt3,sqrt11) (the calibrated oracle);
           (2) sympy          -- the same statement on the same points by a
               different code path (sqrt objects, expansion, zero test via
               Q-linear independence of {1, sqrt3, sqrt11, sqrt33}).
         The two edge lists must be identical (both directions: every
         certified pair is unit, every non-certified pair is not).
    chi = chromatic number by TWO independent complete tests
          (lattice_census.chromatic, DSATUR exhaustive backtracking with
          witness re-verification; brute.coloring_test, plain backtracking),
          which must agree on each k.

Structural fact the measurement rests on (proved, not computed):
  A embeds in A^k as an induced subgraph via a |-> a + 0 + ... + 0, and A is
  4-chromatic (calibrated), so chi(A^k) >= 4 for every k >= 1. The
  measurement decides whether 4 colours suffice (chi = 4) or the sum is
  5-chromatic (which would demand independent re-verification before any
  further claim).

Complexity: construction is O(m^2) exact field operations with m <= 7^k
distinct points (m = 49 at k = 2); the colouring test is exhaustive
backtracking, worst-case exponential, used here strictly as a bounded oracle
(m <= 49 vertices, <= 4 colours) under the caller's hard `timeout 540`.
"""

import sys
import time

from brute import (moser_spindle_points, unit_graph, cadd,
                   coloring_test as naive_coloring_test)   # calibrated oracle

from lattice_census import chromatic as dsur_chromatic      # independent test

# ---------------------------------------------------------------------------
# Independent edge certification by sympy (different arithmetic engine)
# ---------------------------------------------------------------------------

import sympy as sp

S3 = sp.sqrt(3)
S11 = sp.sqrt(11)


def to_sympy(field_el):
    """ field element c0 + c1*sqrt3 + c2*sqrt11 + c3*sqrt33 -> sympy expr.
        sqrt33 is represented as sqrt3*sqrt11, which sympy auto-combines to
        sqrt(33) under the sqrt objects. """
    c0, c1, c2, c3 = field_el
    return (sp.Rational(c0) + sp.Rational(c1) * S3
            + sp.Rational(c2) * S11 + sp.Rational(c3) * S3 * S11)


def point_to_sympy(p):
    re_el, im_el = p
    return to_sympy(re_el), to_sympy(im_el)


def sympy_is_unit(p, q):
    """ |p - q|^2 == 1, decided symbolically.

    After expansion the expression is a Q-linear combination of the basis
    {1, sqrt3, sqrt11, sqrt33} (powers of the sqrt objects auto-reduce).
    The basis is Q-linearly independent (Q(sqrt3,sqrt11) has degree 4:
    neither sqrt3 nor sqrt11 lies in the other's quadratic field), so the
    element is zero iff every coefficient is zero. """
    pre, pim = point_to_sympy(p)
    qre, qim = point_to_sympy(q)
    expr = sp.expand((pre - qre) ** 2 + (pim - qim) ** 2 - 1)
    if expr == 0:
        return True
    coeffs = expr.as_coefficients_dict()
    return all(v == 0 for v in coeffs.values())


def sympy_edge_certification(pts, brute_edges):
    """ Re-certify EVERY pair by the sympy route; require the two edge lists
        to be identical. Returns the sympy edge list. """
    n = len(pts)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if sympy_is_unit(pts[i], pts[j]):
                edges.append((i, j))
    assert edges == brute_edges, \
        f"sympy and brute disagree: sympy {len(edges)} edges, " \
        f"brute {len(brute_edges)} edges"
    return edges


# ---------------------------------------------------------------------------
# Construction of the k-fold Minkowski sum (exact point set)
# ---------------------------------------------------------------------------

def minkowski_level(A, k):
    """ Distinct points of the k-fold Minkowski sum A + ... + A, as sets at
        each stage (set semantics make the result exact: dedupe by exact
        field tuple equality at every level). """
    pts = list(A)
    for _ in range(k - 1):
        pts = [cadd(p, q) for p in pts for q in A]
        seen = set()
        uniq = []
        for p in pts:
            key = (p[0], p[1])
            if key not in seen:
                seen.add(key)
                uniq.append(p)
        pts = uniq
    return pts


# ---------------------------------------------------------------------------
# Census, one level
# ---------------------------------------------------------------------------

def census_level(k):
    print(f"=== level k = {k} ===  (A^k, A = 7-vertex calibrated spindle)",
          flush=True)
    A = moser_spindle_points()   # sanity: A itself is the calibration graph
    t0 = time.perf_counter()
    pts = minkowski_level(A, k)
    t1 = time.perf_counter()
    n = len(pts)
    print(f"distinct points: {n}   (construction {t1-t0:.3f} s)", flush=True)

    verts, edges = unit_graph(pts)          # calibrated oracle, exact
    t2 = time.perf_counter()
    e = len(edges)
    print(f"unit edges (brute exact oracle): {e}   ({t2-t1:.3f} s)", flush=True)

    edges2 = sympy_edge_certification(pts, edges)     # independent engine
    t3 = time.perf_counter()
    print(f"unit edges (sympy independent re-certification): {len(edges2)}   "
          f"({t3-t2:.3f} s)  agree? {edges == edges2}", flush=True)

    # complete colouring, DSATUR test first (stronger pruning)
    k4, witness, dt3 = dsur_chromatic(n, edges, 4)
    print(f"DSATUR complete test: k <= 4 ?  k = {k4}  ({dt3:.3f} s)", flush=True)
    if witness is not None:
        print(f"  witness: {witness}", flush=True)
    if k4 != 4:
        print("  !! no 4-colouring found --- chi(A^k) >= 5 CANDIDATE; "
              "requires independent re-verification before any claim",
              flush=True)
        return False

    # independent complete test, plain backtracking
    ok3, _w3 = naive_coloring_test(n, edges, 3)
    ok4, w4 = naive_coloring_test(n, edges, 4)
    t4 = time.perf_counter()
    print(f"plain backtracking cross-check: 3-colourable? {ok3}   "
          f"4-colourable? {ok4}  witness {w4}   ({t4-t3:.3f} s)", flush=True)

    ok3d = not (k4 == 3)      # k4 is the minimal k found by DSATUR
    assert k4 == 4 and ok4 and not ok3, \
        f"colour tests disagree: DSATUR k={k4}, plain 3-ok={ok3}, 4-ok={ok4}"
    print(f"colour tests agree: chi(A^{k}) = 4, not 3.", flush=True)
    return True


def main():
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    # level-1 internal smoke test: must reproduce the calibration exactly
    A = moser_spindle_points()
    verts, edges = unit_graph(A)
    assert len(verts) == 7 and len(edges) == 11, "calibration graph changed"
    ok3, _ = naive_coloring_test(7, edges, 3)
    ok4, _ = naive_coloring_test(7, edges, 4)
    assert (not ok3) and ok4
    print(f"internal check: A^1 = calibration graph, n=7, e=11, "
          f"3-ok={ok3}, 4-ok={ok4}  (reproduces calibration)", flush=True)
    ok = census_level(k)
    print(flush=True)
    print(f"CENSUS LEVEL k={k} FINISHED: {'chi = 4' if ok else 'open'}",
          flush=True)


if __name__ == "__main__":
    main()