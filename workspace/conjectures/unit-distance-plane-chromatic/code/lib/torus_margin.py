#!/usr/bin/env python3
"""
Flat-torus periodic colouring: separation graph F(Lambda, rho) on lattice
quotients, exact arithmetic.

The (adopted) approach, research/approaches/flat-torus-periodic-6col.md:

  A Lambda-periodic colouring of the plane, constant on the cells of a
  Lambda-periodic tiling of cell radius rho (max |point - centre|), is proper
  iff for every pair of same-coloured cells the exact lattice inequality
      |u - v| > 1 + 2*rho
  holds (then the closest points of two same-colour cells are > 1 apart, and
  cells of diameter 2*rho < 1 rule out the within-cell case).

  This reduces the search to a **finite** object: the separation graph
  F(Lambda, rho) whose vertices are the cell centres (lattice points modulo a
  finite-index sublattice) and whose edges join two centres exactly when their
  Euclidean distance is <= 1 + 2*rho.  A k-colouring of F is exactly a
  Lambda-periodic k-colouring of the plane by radius-rho tiles.

Two inputs:
  * a lattice (basis vectors in physical units), 
  * a tiling cell radius rho.

Coordinates live in Q(sqrt3) (the Eisenstein/A2 triangular lattice): a lattice
point (u, v) maps to the physical point
      centre(u,v) = ( sqrt3*L*(u - v/2),  3/2 * L * v )     [side length L]
so the nearest-neighbour centre spacing is sqrt(3)*L and the tiling cell
circumradius is L = rho.  We keep rho = L throughout.

All verdicts are exact: squared distances are compared with (1+2*rho)^2 using
sympy simplification in Q(sqrt3) (no floats), and k-colourability is decided by
the calibrated complete SAT oracle in lib.satcolor.is_k_colorable.
"""
import itertools
from fractions import Fraction

import sympy as sp

from lib.satcolor import is_k_colorable, verify_witness

THREE = sp.Integer(3)
HALF = sp.Rational(1, 2)
THREE_HALF = sp.Rational(3, 2)


# ---------------------------------------------------------------------------
# A2 lattice -> physical coordinates, exact in Q(sqrt3)
# ---------------------------------------------------------------------------

def a2_centre(u, v, Lv):
    """Physical coordinate of lattice point (u, v) for a tiling of side L.

    Triangular (A2) lattice, nearest-neighbour centre spacing = sqrt(3)*L.
    centre(u,v) = ( sqrt3 L (u - v/2), 3/2 L v ).  Exact in Q(sqrt3).
    """
    x = sp.sqrt(3) * Lv * (u - sp.Rational(v, 2))
    y = THREE_HALF * Lv * v
    return sp.simplify(x), sp.simplify(y)


def a2_sqdist_units(u1, v1, u2, v2, Lv):
    """Exact squared physical distance between lattice centres, in Q(sqrt3)."""
    c1 = a2_centre(u1, v1, Lv)
    c2 = a2_centre(u2, v2, Lv)
    return sp.expand((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)


# ---------------------------------------------------------------------------
# Sublattice / quotient machinery (exact integer)
# ---------------------------------------------------------------------------

def coset_key(u, v, g1, g2):
    """Canonical integer key for the coset of (u,v) mod Z^2/<g1,g2>.

    g1 = (a1, b1), g2 = (a2, b2).  The quotient has |det|=D cosets.  We reduce
    (u,v) by subtracting integer multiples of g1, g2 in a canonical way and
    return the 2-vector residue (the point of the fundamental parallelogram).
    """
    M = (g1[0], g2[0], g1[1], g2[1])      # columns
    det = M[0] * M[3] - M[1] * M[2]
    D = abs(det)
    # Solve (u,v) = a*g1 + b*g2 + r with a,b integers chosen so r lies in a
    # fixed fundamental cell.  We find r by reducing mod the Smith-normal-ish
    # structure; here we just return the reductions of the coordinates against
    # the lattice's unimodular action via a deterministic nearest-residue.
    return _reduce(u, v, g1, g2, D)


def _reduce(u, v, g1, g2, D):
    """Deterministically reduce (u,v) into the fundamental parallelogram of
    the sublattice (so reps are unique).  Correct because subtracting a
    lattice vector does not change the coset."""
    best = (u, v)
    best_d = u * u + v * v
    for a in range(-4, 5):
        for b in range(-4, 5):
            r0 = u - (a * g1[0] + b * g2[0])
            r1 = v - (a * g1[1] + b * g2[1])
            d = r0 * r0 + r1 * r1
            if d < best_d or (d == best_d and (r0, r1) < best):
                best_d = d
                best = (r0, r1)
    return best


def reps_of_sublattice(g1, g2, D):
    """Return the D canonical coset representatives of Z^2 / <g1,g2> (as
    (u,v) pairs), each one the point of its coset closest to the origin
    (integer lattice distance)."""
    seen = set()
    reps = []
    # scan a generous box; the fundamental parallelogram fits well within it
    R = 2 * (abs(g1[0]) + abs(g2[0]) + abs(g1[1]) + abs(g2[1]) + 2)
    for u in range(-R, R + 1):
        for v in range(-R, R + 1):
            key = _reduce(u, v, g1, g2, D)
            if (u, v) == key and key not in seen:
                seen.add(key)
                reps.append(key)
            if len(seen) == D:
                break
        if len(seen) == D:
            break
    return reps


# ---------------------------------------------------------------------------
# The separation graph
# ---------------------------------------------------------------------------

def separation_graph(basis, rho, index, return_data=False):
    """The exact finite separation graph F on the lattice quotient.

    basis : (g1, g2)  integer vectors generating a finite-index sublattice of
            the integer A2 lattice (each g_i is (du, dv)).  index = |det|.
    rho   : tiling cell radius (= side length L here).  Exact (int, Fraction,
            Rational, or sympy exact).
    Edge between two centres (mod the sublattice) iff their physical distance
    <= 1 + 2*rho.  Vertices are numbered 0..index-1 in the order returned by
    reps_of_sublattice.

    Returns (n, edges).  edges is a list of (i, j) with i < j.
    """
    Lv = sp.sympify(rho)
    g1, g2 = tuple(basis)
    D = abs(g1[0] * g2[1] - g1[1] * g2[0])
    reps = reps_of_sublattice(g1, g2, D)
    assert len(reps) == D, (len(reps), D)
    T2 = sp.expand((1 + 2 * Lv) ** 2)

    edges = []
    for i in range(D):
        for j in range(i + 1, D):
            d2 = a2_sqdist_units(reps[i][0], reps[i][1], reps[j][0],
                                 reps[j][1], Lv)
            # exact comparison d2 <= T2 in Q(sqrt3)
            if sp.simplify(d2 - T2) <= 0:
                edges.append((i, j))
    if return_data:
        return D, edges, reps
    return D, edges


# ---------------------------------------------------------------------------
# Calibration helpers
# ---------------------------------------------------------------------------

def a2_seven_colouring_margin(Lv=None):
    """Exact A2 hexagonal 7-colouring margin facts.

    Same-colour centre distance = sqrt(21)*L  (in physical units), so the
    same-colour margin (centre distance - 2L) is (sqrt(21)-2)*L, valid window
    1/(sqrt21-2) < L < 1/2.  Returns a dict of exact sympy values.
    """
    sqrt21 = sp.sqrt(21)
    win_lo = 1 / (sqrt21 - 2)
    win_hi = sp.Rational(1, 2)
    out = {
        "same_colour_centre_factor": sqrt21,   # x L
        "margin_factor": sqrt21 - 2,           # x L
        "window_lo": win_lo,
        "window_hi": win_hi,
        "window_open_lower": win_lo,
        "window_open_upper": win_hi,
        "margin_at_half": (sqrt21 - 2) * sp.Rational(1, 2),
    }
    if Lv is not None:
        Lv = sp.sympify(Lv)
        out["margin_at_L"] = sp.simplify((sqrt21 - 2) * Lv)
        out["same_colour_centre_distance_at_L"] = sp.simplify(sqrt21 * Lv)
        out["threshold_1_plus_2L"] = sp.simplify(1 + 2 * Lv)
        okay = (win_lo < Lv) and (Lv < win_hi)
        out["in_window"] = bool(okay)
    return out


def index7_sublattice():
    """The norm-7 sublattice of the integer A2 lattice, generated by the
    Einstein ideal (2 - omega): generators (2,-1) and (1,3), det = 7."""
    return ((2, -1), (1, 3)), 7


def check_F_k_colourable(basis, rho, index, k, return_data=False):
    """Build F(basis, rho) on the quotient and test k-colourability with the
    calibrated exact SAT oracle.  Returns (n, sat, witness, t_sec).
    If return_data, also returns reps."""
    D, edges, reps = separation_graph(basis, rho, index, return_data=True)
    import time
    t0 = time.time()
    sat, witness = is_k_colorable(edges, k, D)
    dt = time.time() - t0
    r = (D, sat, witness, dt, edges)
    if return_data:
        r = r + (reps,)
    return r


def run_calibration():
    """Drive the A2 calibration and the sweep; writes a full text report."""
    import time
    lines = []
    def emit(s=""):
        lines.append(str(s))

    emit("=" * 78)
    emit("FLAT-TORUS PERIODIC COLOURING — exact-arithmetic calibration")
    emit("approach: research/approaches/flat-torus-periodic-6col.md")
    emit("=" * 78)

    # ---- 1. exact margin & window (sympy) ----
    emit("\n[1] A2 hexagonal 7-colouring margin (exact, Q(sqrt3))")
    m = a2_seven_colouring_margin()
    emit(f"  same-colour centre distance factor (xL) = {m['same_colour_centre_factor']}")
    emit(f"    numeric ~ {sp.N(m['same_colour_centre_factor'], 12)}")
    emit(f"  same-colour margin factor (centre-2L, xL) = {m['margin_factor']}")
    emit(f"  valid side-length window: {sp.N(m['window_lo'],12)} < L < 1/2")
    emit(f"  window lower bound 1/(sqrt21-2) = 1/({m['window_lo']})")
    emit(f"  margin at L=1/2 = (sqrt21-2)/2 = {m['margin_at_half']} ~ "
         f"{sp.N(m['margin_at_half'],12)} > 1  [rich margin for 7 colours]")

    # ---- 2. chi(F(A2,L)) = 7 in the window via the SAT oracle ----
    emit("\n[2] chi(F(A2, L)) = 7 on the index-7 quotient (complete SAT oracle)")
    basis, index = index7_sublattice()
    for Lv in [sp.Rational(2, 5), sp.Rational(9, 20), sp.Rational(49, 100)]:
        # exact window membership
        m = a2_seven_colouring_margin(Lv)
        D, sat6, w6, t6, edges = check_F_k_colourable(basis, Lv, index, 6)
        D7, sat7, w7, t7, edges7 = check_F_k_colourable(basis, Lv, index, 7)
        emit(f"  L = {sp.N(Lv,8)} ({Lv}); in_window={m['in_window']}; "
             f"F has {len(edges)} edges on {D} vertices (=K7={len(edges)==D*(D-1)//2})")
        emit(f"      6-colourable? {sat6}  ({t6:.3f}s)   "
             f"7-colourable? {sat7} (witness={w7}, {t7:.3f}s)")
        assert sat6 is False, "expected F not 6-colourable in the window"
        assert sat7 is True, "expected F 7-colourable (it is K7)"

    # ---- 3. 6-colour sweep over rational-slope sublattices of A2 ----
    emit("\n[3] 6-colour sweep over rational-slope sublattices of A2")
    emit("  (search for a Lambda-periodic 6-colouring / periodic-impossibility census)")

    # helper to enumerate index-D sublattices given by two generators; we
    # parameterise by a sublattice as the set { (u,v) : a*u + b*v ≡ 0 (mod D) }
    # for coprime (a,b) with gcd(a,b,D)=1 and a index-D row; but a cleaner
    # enumeration is: sublattices are kernels of a surjective Z^2 -> Z/D.
    # We enumerate surjective maps given by a row (p,q) with gcd(p,q,D) = 1.

    def row_generators(p, q, D):
        """Second generator completing row (p,q): find g1 with p*g1[0]+q*g1[1]
        ≡ 0 mod D and a vector making det = D (or -D).  We construct the kernel
        of the map (u,v) -> p u + q v mod D.  A convenient basis:
        v1 = (q/g, -p/g) scaled so it maps to 0; and a vector mapping to 1.
        We just take the kernel basis directly: (q', -p') where
        q'=q/g, p'=p/g, g = gcd(p,q), is in the kernel, and a second vector
        spanning the full kernel lattice.  For simplicity we build the kernel
        as: L = { (u,v) : p u + q v = 0 mod D }.
        """
        import math
        g = math.gcd(p, q)
        gg = math.gcd(g, D)
        # (q/g, -p/g) is in the kernel (integer)
        w1 = (q // g, -(p // g))
        # need a second lattice vector (in kernel) so that w1 and w2 span a
        # superlattice of index D.  We look for the full set of reps.
        return w1, D

    # Simpler, robust enumeration: for each surjective row (p,q) mod D, list
    # all cosets and build the quotient graph.  We enumerate D up to a budget.
    def sublattice_reps_row(p, q, D):
        """Representatives of the kernel sublattice { (u,v): p u + q v ≡ 0
        mod D } inside Z^2/<D>.  The quotient Z^2 / kernel has size D, so the
        kernel has index D."""
        # The kernel inside the coarse torus Z^2/DZ^2 has size D (the image of
        # (u,v)->p u+q v mod D is Z/D since gcd(p,q,D)=1, kernel size D^2/D=D).
        # Cosets of the kernel inside Z^2/<D>: each coset is a residue class
        # of the row map value.  We take reps = {(u,v) : p u + q v ≡ r} for
        # r=0..D-1, choosing smallest (u,v).
        reps = []
        for r in range(D):
            cand = None
            for u in range(D):
                for v in range(D):
                    if (p * u + q * v) % D == r:
                        if cand is None or (u * u + v * v) < (cand[0] * cand[0] + cand[1] * cand[1]):
                            cand = (u, v)
            reps.append(cand)
        return reps

    # For the calibration sweep we test up to a modest order and a few rows.
    import time as _time
    results = []
    sweep_L = sp.Rational(2, 5)          # a representative L in the window
    reported = False
    for D in [7, 13]:
        # test a small sample of rows at this index
        rows = []
        for p in range(1, 4):
            for q in range(-2, 3):
                import math
                if math.gcd(p, q, D) == 1 and (p, q) not in rows:
                    rows.append((p, q))
        for (p, q) in rows:
            # kernel rows; for D=7 the standard index-7 colouring sublattice
            # corresponds to row (3,-1) [3u - v ≡ 0 mod 7].
            reps = sublattice_reps_row(p, q, D)
            # distinct physical centres
            Lv = sweep_L
            T2 = sp.expand((1 + 2 * Lv) ** 2)
            edges = []
            for i in range(D):
                for j in range(i + 1, D):
                    d2 = a2_sqdist_units(reps[i][0], reps[i][1],
                                         reps[j][0], reps[j][1], Lv)
                    if sp.simplify(d2 - T2) <= 0:
                        edges.append((i, j))
            t0 = _time.time()
            sat6, w6 = is_k_colorable(edges, 6, D)
            dt = _time.time() - t0
            tag = "canonical-index7" if (p, q) == (3, -1) else ""
            results.append((D, (p, q), len(edges), sat6, dt, tag))
            emit(f"  D={D} row=({p},{q}) {tag}: {len(edges)} edges, "
                 f"6-colourable={sat6} ({dt:.2f}s)")
            reported = True
            if sat6 is True:
                emit("    ** FOUND a 6-colouring — a periodic 6-colouring! **")
    if not reported:
        emit("  (sweep enumeration produced no rows)")

    total = sum(rr[4] for rr in results)
    n_sat = sum(1 for rr in results if rr[3])
    emit(f"\n  census: {len(results)} sublattices tested, {n_sat} with a 6-colouring, "
         f"{len(results)-n_sat} needing 7; total SAT time {total:.2f}s")
    return lines, results


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    lines, results = run_calibration()
    print("\n".join(lines))
