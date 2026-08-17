"""Verify the Horton (1983) construction S_k = {(i,d(i))} : i=0..2^k-1,
d(i) = sum_{j=0}^{k-1} a_j c^j, c = 2^k+1, a_j = j-th bit of i (fixed-width
binary expansion, LSB-first), against the exact oracle lib.es_geom.

Checks:
 1. general position (no three collinear) -- exact integer 3x3 determinants
 2. the set contains NO EMPTY convex 7-gon  for k = 3,4 (and k=5 with --k5):
    no 7-subset in convex position with no other point of the set inside.

This is the EMPTY analogue (Erdos-Szekeres-Horton / empty-hexagon side),
kept strictly separate from the ES(n) convex-position question.  It does NOT
bear on ES(n) = 2^{n-2}+1; it confirms the freshly-digested Horton primary
source (claim horton-no-empty-7gon).

CORRECTNESS FIX over the previous (never-run) version: convexity is decided
by the verified hull-based oracle lib.es_geom.in_convex_position (a subset is
in convex position iff it IS its own hull), and emptiness by an exact
cyclic-edge side test on the CCW hull (q inside-or-on iff orient(edge,q)>=0
for every directed edge; under general position "on" cannot occur).  The old
version tested orientation-sign consistency in the x-sorted subset order,
which is not the cyclic hull order in general, so it could declare a convex
set non-convex and report "no empty 7-gon" vacuously.

Hand-known self-tests of the checker, run before the main verification:
  * positive: 7 points (i,i^2), i=0..6, in convex position plus (3,30) which
    lies strictly OUTSIDE the 7-gon  -> has_empty_convex_7gon = True
  * negative: same 7 plus (3,10) which lies strictly INSIDE the 7-gon
    (9 < 10 < 18 = chord at x=3)      -> has_empty_convex_7gon = False
Both are exact integer configurations; the pass of both pins the checker.

Bit-order robustness control (the handoff warned the bit convention is the
likely bug site): the claim-summary convention (a_1 LSB) and the bit-reversed
(MSB-first) reading are BOTH verified to have no empty convex 7-gon.  The
trefoil structure is bit-order-robust, so both must pass.

Exact integer arithmetic throughout (Python ints; numpy not needed).
"""
import itertools
import sys
import time

from lib.es_geom import orient, in_general_position, in_convex_position, convex_hull


def build(k, reverse_bits=False):
    """S_k = {(i, d(i)) : 0 <= i < 2^k}, d(i) = sum_j a_j c^j, c = 2^k + 1.

    a_j = j-th bit of i (j from 0, LSB first) matches the claim-summary
    convention (a_1..a_k the fixed-width binary expansion, a_1 least
    significant).  reverse_bits=True reads the bits MSB-first as a control.
    """
    c = 2**k + 1
    pts = []
    for i in range(2**k):
        bits = [(i >> j) & 1 for j in range(k)]
        if reverse_bits:
            bits = bits[::-1]
        d = sum(b * (c**j) for j, b in enumerate(bits))
        pts.append((i, d))
    return pts


def has_empty_7gon(pts):
    """Exact: does some 7-subset form a convex 7-gon with no other point of
    pts inside (strictly inside or on the boundary)?  Returns (found, witness)."""
    n = len(pts)
    for sub_i in itertools.combinations(range(n), 7):
        sub = [pts[t] for t in sub_i]
        if not in_convex_position(sub):
            continue
        hull = convex_hull(sub)          # CCW, len == 7 by convexity
        interior = [pts[t] for t in range(n) if t not in sub_i]
        bad = False
        for q in interior:
            inside = True
            for i in range(7):
                a, b = hull[i], hull[(i + 1) % 7]
                if orient(a, b, q) < 0:      # strictly right of an edge: outside
                    inside = False
                    break
            if inside:
                bad = True
                break
        if not bad:
            return True, (sub_i, [(p[0], p[1]) for p in sub])
    return False, None


def self_test():
    """Hand-known positive/negative controls for the empty-7-gon checker."""
    outer = [(i, i * i) for i in range(7)]          # 7-parabola cup: convex 7-gon
    # chord (0,0)-(6,36) at x=3 has y=18; parabola at x=3 has y=9.
    pos_pts = outer + [(3, 30)]                     # (3,30): y=30 > 18 -> outside
    neg_pts = outer + [(3, 10)]                     # (3,10): 9 < 10 < 18 -> inside
    assert in_convex_position(outer), "outer 7-parabola must be convex"
    f_pos, w_pos = has_empty_7gon(pos_pts)
    f_neg, _ = has_empty_7gon(neg_pts)
    print("  self-test positive (point outside): has_empty_convex_7gon =", f_pos,
          " witness-subset =", w_pos[0] if w_pos else None)
    print("  self-test negative (point inside):  has_empty_convex_7gon =", f_neg)
    ok = f_pos and not f_neg
    print("  CHECKER SELF-TEST:", "PASS" if ok else "FAIL")
    return ok


def run_k(k, reverse_bits):
    pts = build(k, reverse_bits)
    gp, tri = None, None
    for i, j, kk in itertools.combinations(range(len(pts)), 3):
        if orient(pts[i], pts[j], pts[kk]) == 0:
            gp, tri = False, (i, j, kk)
            break
    if gp is None:
        gp = True
    tag = "LSB" if not reverse_bits else "MSB-first(control)"
    print(f"k={k} n={len(pts)} c={2**k+1} convention={tag} general_position={gp}",
          flush=True)
    if not gp:
        print("  collinear triple:", tri)
        return None
    found, witness = has_empty_7gon(pts)
    print(f"  has_empty_convex_7gon = {found}", flush=True)
    if found:
        print("   WITNESS (7-subset):", witness[0])
        print("   WITNESS coords:", witness[1])
    return found


def main():
    print("=== Horton S_k empty-convex-7-gon verification (exact integer,",
          "lib.es_geom oracle) ===")
    print("  checker self-tests first:")
    if not self_test():
        print("  ABORT: checker self-test failed; results would not be trusted")
        return 1

    for k in [3, 4]:
        for rev in [False, True]:
            run_k(k, rev)

    if "--k5" in sys.argv:
        t0 = time.time()
        for rev in [False, True]:
            run_k(5, rev)
        print(f"  k=5 wall: {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())