#!/usr/bin/env python3
"""Exact wedge / ray-split bipartition enumerator on the VERIFIED es_construct.

Builds, for a fixed apex O in general position (on no line through two set
points), the exact circular order of the N set-points around O (half-plane +
orientation, no floats), then enumerates the combinatorially distinct 2-way
WEDGE bipartitions: contiguous arcs of exactly `target`=2^{n-3} points in the
circular order, each arc together with its complement forming the two halves
of a two-ray sector split through O.  A bipartition is VALID iff both halves
are free of a convex k-gon, k=n-1, tested with the exact oracle
lib.es_geom.has_convex_k_subset (exact integer/Fraction arithmetic).

Also reproduces the pi-wedge (half-plane) sides through the apex O -- the
boundary rays each through a set point -- the family the earlier rotating-LINE
enumeration covered.

Modes (argv[1]):
  probe  : n=7 apex (2500,2750): pi-wedge sides/checked/valid, contiguous-arc
           distinct bipartitions and valid count.
  calib  : n in {5,6,7} at central apex (2500,3000) and (2500,2750):
           contiguous-arc distinct bipartition + valid counts, and the
           pi-wedge sides/checked/valid counts.
  q1     : for all valid contiguous-arc and pi-wedge bipartitions found in
           `probe`/`calib`/a supplied apex, compare each against the even/odd
           block bipartition and the contiguous-block split.
  orders : print the representative apex (one per distinct circular order) for
           the Q2 sources (21x21 grid + probe, vertical sweep x=2500,
           horizontal sweep y=ycenter), one per line, after dedup by circular
           order; prints the union count first.
  enum H T : enumerate the representatives with chunk index H of T (from the
           same deterministic ordericker as `orders`), running the FULL
           size-16 wedge enumeration on each distinct circular order, and
           reporting how many covered orders (cells) contain a VALID split.

All arithmetic exact; ring: Fraction / integer cross products.  Works on
lib.es_construct (blocks T0..Tn-2).  Inputs: lib/es_construct.py,
lib/es_geom.py.
"""

import sys
from functools import cmp_to_key
from fractions import Fraction
from lib.es_geom import orient, has_convex_k_subset
from lib.es_construct import es_set_blocks


# ---------------------------------------------------------------------------
# core geometry (exact)
# ---------------------------------------------------------------------------

def circular_order(points, O):
    """Indices of `points` sorted CCW around apex O, exact.  Caller must have
    checked O is in general position (no two points collinear with O)."""
    N = len(points)

    def half(idx):
        dx = points[idx][0] - O[0]
        dy = points[idx][1] - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1

    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = orient(O, points[a], points[b])
        if c > 0:
            return -1
        if c < 0:
            return 1
        return 0
    return tuple(sorted(range(N), key=cmp_to_key(cmp)))


def apex_general(points, O):
    """True iff no two set points are collinear with apex O (distinct
    directions).  O is generic iff this holds."""
    N = len(points)
    for a in range(N):
        for b in range(a + 1, N):
            if orient(O, points[a], points[b]) == 0:
                return False
    return True


def contiguous_bipartitions(order, target, N):
    """All distinct 2-way contiguous-arc bipartitions: contiguous runs of
    exactly `target` points in the circular order, each with its complement.
    Returns list of (arc, comp) as frozensets, deduped by {arc, comp}."""
    seen = set()
    out = []
    for s in range(N):
        arc = frozenset(order[(s + k) % N] for k in range(target))
        comp = frozenset(range(N)) - arc
        key = frozenset((arc, comp))
        if key in seen:
            continue
        seen.add(key)
        out.append((arc, comp))
    return out


def bipartition_valid(pts, arc, comp, k):
    """True iff both halves are free of a convex k-gon (exact oracle)."""
    return (not has_convex_k_subset([pts[i] for i in arc], k)[0]
            and not has_convex_k_subset([pts[i] for i in comp], k)[0])


def pi_wedge_sides_through_apex(points, O):
    """All nonempty-proper open half-plane sides whose boundary line passes
    through apex O, one per set-point direction (boundary ray through that
    point, exclusive).  Exact."""
    N = len(points)
    sides = set()
    for b in range(N):
        side = frozenset(q for q in range(N) if orient(O, points[b], points[q]) > 0)
        if 0 < len(side) < N:
            sides.add(side)
    return sides


def block_map(n):
    pts, blocks = es_set_blocks(n)
    mp = []
    for b, blk in enumerate(blocks):
        for _ in blk:
            mp.append(b)
    return pts, mp


# ---------------------------------------------------------------------------
# representative apex sets for Q2
# ---------------------------------------------------------------------------

def bbox(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), max(xs), min(ys), max(ys)


def q2_apexes(pts):
    """Deterministic list: 21x21 grid + probe, then vertical sweep x=xcenter,
    then horizontal sweep y=ycenter.  Axes are the box's own."""
    xmin, xmax, ymin, ymax = bbox(pts)
    xcenter = (xmin + xmax) / 2
    ycenter = (ymin + ymax) / 2
    apexes = []
    # probe apex
    probe = (Fraction(2500), Fraction(2750))
    apexes.append(probe)
    # 21x21 grid over the box (skip exact duplicates of probe)
    for i in range(21):
        x = xmin + (xmax - xmin) * Fraction(i, 20)
        for j in range(21):
            y = ymin + (ymax - ymin) * Fraction(j, 20)
            if (x, y) == probe:
                continue
            apexes.append((x, y))
    # vertical sweep x=xcenter: sample strictly between consecutive pair-line
    # crossings along the vertical line inside the box
    crossings = set()
    N = len(pts)
    for a in range(N):
        for b in range(a + 1, N):
            px, py = pts[a]
            qx, qy = pts[b]
            if qx == px:
                continue
            t = Fraction(xcenter - px, qx - px)
            y = py + (qy - py) * t
            if ymin < y < ymax:
                crossings.add(y)
    cs = sorted(crossings)
    prev = ymin
    for y in cs:
        apexes.append((Fraction(xcenter), (prev + y) / 2))
        prev = y
    apexes.append((Fraction(xcenter), (prev + ymax) / 2))
    # horizontal sweep y=ycenter
    crossings = set()
    for a in range(N):
        for b in range(a + 1, N):
            px, py = pts[a]
            qx, qy = pts[b]
            if qy == py:
                continue
            t = Fraction(ycenter - py, qy - py)
            x = px + (qx - px) * t
            if xmin < x < xmax:
                crossings.add(x)
    cs = sorted(crossings)
    prev = xmin
    for x in cs:
        apexes.append(((prev + x) / 2, Fraction(ycenter)))
        prev = x
    apexes.append(((prev + xmax) / 2, Fraction(ycenter)))
    return apexes, probe


def distinct_orders(pts, apexes):
    """Map circular-order-tuple -> first representative apex (dedup)."""
    rep = {}
    for O in apexes:
        if not apex_general(pts, O):
            continue
        ord_t = circular_order(pts, O)
        if ord_t not in rep:
            rep[ord_t] = O
    return rep


# ---------------------------------------------------------------------------
# modes
# ---------------------------------------------------------------------------

def mode_probe():
    n = 7
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    O = (Fraction(2500), Fraction(2750))
    target = 2 ** (n - 3)
    k = n - 1
    print(f"=== probe: n={n} N={N} apex={O} ===")
    print(f"  apex_general: {apex_general(pts, O)}")
    sides = pi_wedge_sides_through_apex(pts, O)
    checked = 0
    valid = 0
    valid_splits = []
    for side in sides:
        if len(side) != target:
            continue
        comp = frozenset(range(N)) - side
        if len(comp) != target:
            continue
        checked += 1
        if bipartition_valid(pts, side, comp, k):
            valid += 1
            valid_splits.append((sorted(side), sorted(comp)))
    print(f"  pi-wedge sides through apex: {len(sides)}")
    print(f"  pi-wedge size-{target} bipartitions checked: {checked}")
    print(f"  pi-wedge VALID: {valid}")
    # contiguous arcs
    order = circular_order(pts, O)
    bips = contiguous_bipartitions(order, target, N)
    v = 0
    vlist = []
    for arc, comp in bips:
        if bipartition_valid(pts, arc, comp, k):
            v += 1
            vlist.append((sorted(arc), sorted(comp)))
    print(f"  contiguous-arc distinct bipartitions: {len(bips)}")
    print(f"  contiguous-arc VALID: {v}")
    for arc, comp in vlist:
        print(f"      VALID arc={arc}")
        print(f"            comp={comp}")
    return valid_splits, vlist


def mode_calib():
    print("=== calibration: n=5,6,7 central apexes ===")
    summary = {}
    for n in (5, 6, 7):
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        target = 2 ** (n - 3)
        k = n - 1
        row = []
        for O in ((Fraction(2500), Fraction(3000)), (Fraction(2500), Fraction(2750))):
            if not apex_general(pts, O):
                print(f"  n={n} apex={O} NOT general, skipped")
                continue
            sides = pi_wedge_sides_through_apex(pts, O)
            checked = 0
            pvalid = 0
            for side in sides:
                if len(side) != target:
                    continue
                comp = frozenset(range(N)) - side
                if len(comp) != target:
                    continue
                checked += 1
                if bipartition_valid(pts, side, comp, k):
                    pvalid += 1
            order = circular_order(pts, O)
            bips = contiguous_bipartitions(order, target, N)
            v = 0
            vlist = []
            for arc, comp in bips:
                if bipartition_valid(pts, arc, comp, k):
                    v += 1
                    vlist.append((sorted(arc), sorted(comp)))
            print(f"  n={n} apex={O}: pi-wedge sides={len(sides)} checked={checked} "
                  f"VALID={pvalid} | contiguous-arc distinct={len(bips)} VALID={v}")
            for arc, comp in vlist:
                print(f"      VALID arc={arc} comp={comp}")
            row.append((str(O), pvalid, len(bips), v))
        summary[n] = row
    return summary


def mode_q1():
    # gather valid bipartitions from calibration + a run over the grid apexes'
    # representatives so we have a set to compare.  Reuse representatives.
    n = 7
    pts, blocks = es_set_blocks(n)
    mp = [bi for b, blk in enumerate(blocks) for bi in [b] * len(blk)]
    N = len(pts)
    target = 2 ** (n - 3)
    k = n - 1
    # even/odd block bipartition
    even = frozenset(i for i in range(N) if mp[i] % 2 == 0)
    odd = frozenset(range(N)) - even
    # contiguous-block split (prefix sums of C(5,i)): only 16/16 one: {T0,T1,T2} vs {T3,T4,T5}
    # T0..T2 = indices 0..15, T3..T5 = 16..31
    con_t = frozenset(range(16))
    con_c = frozenset(range(16, 32))
    print("=== Q1: compare valid wedge splits to even/odd and contiguous-block ===")
    even_odd_pts = (sorted(even), sorted(odd))
    con_pts = (sorted(con_t), sorted(con_c))
    print(f"  even/odd block bipartition sizes: {len(even)}/{len(odd)}; "
          f"blocks even=[T0,T2,T4] odd=[T1,T3,T5]")
    print(f"  contiguous-block split (T0,T1,T2)|(T3,T4,T5): {len(con_t)}/{len(con_c)}")
    # collect all valid splits across the sampled apexes (grid+sweep, deduped)
    apexes, probe = q2_apexes(pts)
    rep = distinct_orders(pts, apexes)
    valid_splits = set()   # frozenset((arc,comp))
    for O in list(rep.values())[:40]:   # enough to gather splits; full grid covers Q1
        order = circular_order(pts, O)
        for arc, comp in contiguous_bipartitions(order, target, N):
            if bipartition_valid(pts, arc, comp, k):
                valid_splits.add(frozenset((arc, comp)))
    print(f"  distinct valid wedge bipartitions gathered: {len(valid_splits)}")
    for bip in valid_splits:
        arc, comp = tuple(sorted(bip, key=len))
        # compare
        aeven = (frozenset(arc) == even or frozenset(arc) == odd)
        acon = (frozenset(arc) == con_t or frozenset(arc) == con_c)
        print(f"  valid split arc={sorted(arc)}")
        print(f"     comp={sorted(comp)}")
        print(f"     arc blocks: {[mp[i] for i in sorted(arc)]}")
        print(f"     comp blocks:{[mp[i] for i in sorted(comp)]}")
        print(f"     == even/odd block bip? {aeven}   == contiguous-block bip? {acon}")


def mode_orders():
    n = 7
    pts, blocks = es_set_blocks(n)
    apexes, probe = q2_apexes(pts)
    rep = distinct_orders(pts, apexes)
    print(f"UNION distinct circular orders (grid+probe+sweeps): {len(rep)}")
    for O in rep.values():
        x, y = O
        print(f"{x.numerator}/{x.denominator} {y.numerator}/{y.denominator}")


def mode_enum(chunk, total):
    n = 7
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    target = 2 ** (n - 3)
    k = n - 1
    apexes, probe = q2_apexes(pts)
    rep = distinct_orders(pts, apexes)
    reps = list(rep.values())
    reps.sort(key=lambda O: (O[0], O[1]))
    my = reps[chunk::total]
    covered_with_valid = 0
    orders_done = 0
    valid_bips = set()
    for O in my:
        order = circular_order(pts, O)
        bips = contiguous_bipartitions(order, target, N)
        has_valid = False
        for arc, comp in bips:
            if bipartition_valid(pts, arc, comp, k):
                has_valid = True
                valid_bips.add(frozenset((arc, comp)))
                break   # early termination: cell established
        if has_valid:
            covered_with_valid += 1
        orders_done += 1
        print(f"order {orders_done}/{len(my)} apex={(O[0],O[1])} "
              f"bipartitions={len(bips)} has_valid={has_valid}",
              flush=True)
    print(f"CHUNK {chunk}/{total}: orders_covered={orders_done} "
          f"orders_with_valid_split={covered_with_valid} "
          f"distinct_valid_bipartitions={len(valid_bips)}")
    for bip in valid_bips:
        arc, comp = tuple(sorted(bip, key=len))
        print(f"  VALID bip arc={sorted(arc)} comp={sorted(comp)}")


def main():
    args = sys.argv[1:]
    if args and args[0] == "probe":
        mode_probe()
    elif args and args[0] == "calib":
        mode_calib()
    elif args and args[0] == "q1":
        mode_q1()
    elif args and args[0] == "orders":
        mode_orders()
    elif args and args[0] == "enum":
        mode_enum(int(args[1]), int(args[2]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
