#!/usr/bin/env python3
"""Wedge / ray-split arbiter on the verified es_construct at n=5,6,7.

STEP A (wedge split). Enumerate 2-way wedge (sector) bipartitions of
es_construct(n) into two halves of size exactly 2^{n-3} and test each half for
a convex (n-1)-gon with the EXACT oracle lib.es_geom.has_convex_k_subset.  Two
separator families:

  * pi-wedge (half-plane) CONTROL: the full rotating-LINE enumeration (all
    N(N-1) open half-plane sides, exactly the verified `ordered_pair_sides`
    construction from code/out/gsplit_enum_definitive.py).  This must
    reproduce valid splits 4 / 2 / 0 at n = 5, 6, 7.  Every line is a pi-wedge,
    so the wedge code is a superset of the line code; this control proves the
    avoidance-testing path is exact.

  * PROPER wedge (angle < pi): for each swept apex O through the central
    region, build O's circular angular order of the N points (EXACT angular
    sort via half-plane + cross product) and enumerate the sectors, i.e. the
    contiguous runs of exactly 2^{n-3} points.  Each such run and its
    complement form the two halves of a two-ray bipartition through O; test
    both for (n-1)-avoiding.  Report whether any PROPER wedge split exists,
    in particular at n = 7 where the single-line split fails (0).

STEP B (split-6-gon spectrum). On the WHOLE es_construct(7): for every point r
as the shared rightmost (max-x) point, the largest a with an a-cap ending at r
and the largest u with a u-cup ending at r.  Report max(a), max(u), max(a+u)
and compare the a+u = 8 split-6-gon boundary against the Baek-Balko threshold
ESsplit(6) = 2^4 + 1 = 17.

Exact Fraction/integer arithmetic throughout; orientation only via
lib.es_geom.orient (integer/Fraction determinants, never floats).
"""

import math
from itertools import combinations
from lib.es_geom import orient, has_convex_k_subset
from lib.es_construct import es_set_blocks


# ---------------------------------------------------------------------------
# pi-wedge control: full rotating-line (open half-plane side) enumeration
# (the verified `ordered_pair_sides` construction, re-emitted here so the
#  capture runs standalone; identical to code/out/gsplit_enum_definitive.py)
# ---------------------------------------------------------------------------

def ordered_pair_sides(points):
    """Set of all nonempty-proper open half-plane sides of a general-position
    set: for each ORDERED pair (a,b), the strict-left side plus the 4
    inclusions of the two on-line points, deduped.  Count = N(N-1)."""
    N = len(points)
    res = set()
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            strict = frozenset(x for x in range(N)
                               if orient(points[a], points[b], points[x]) > 0)
            for extra in (frozenset(), frozenset([a]), frozenset([b]),
                          frozenset([a, b])):
                side = strict | extra
                if 0 < len(side) < N:
                    res.add(side)
    return res


# ---------------------------------------------------------------------------
# proper-wedge enumeration from a fixed apex
# ---------------------------------------------------------------------------

def angular_order(points, O):
    """Indices of `points` sorted CCW around apex O, exact (half-plane then
    cross product).  Requires no two points collinear with O (checked by
    caller)."""
    def half(idx):
        x, y = points[idx]
        dx, dy = x - O[0], y - O[1]
        # upper half-plane (including positive x-axis) = 0, else 1
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    order = list(range(len(points)))
    from functools import cmp_to_key
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = orient(O, points[a], points[b])
        if c > 0:
            return -1
        if c < 0:
            return 1
        return 0   # degenerate: collinear with apex (caller must exclude)
    return sorted(order, key=cmp_to_key(cmp))


def apex_general(points, O):
    """True iff no two points are collinear with apex O (distinct directions)."""
    for a, b in combinations(range(len(points)), 2):
        if orient(O, points[a], points[b]) == 0:
            return False
    return True


def run_sector_pairs(order, target, N):
    """All ordered pairs (sector, complement) for contiguous runs of exactly
    `target` points in the circular order.  Yields (frozenset_sector,
    frozenset_complement)."""
    seen = set()
    for s in range(N):
        sector = frozenset(order[(s + k) % N] for k in range(target))
        comp = frozenset(range(N)) - sector
        key = frozenset((sector, comp))
        if key in seen:
            continue
        seen.add(key)
        yield sector, comp


def wedge_is_halfplane(points, O, sector):
    """Heuristic (float) label: True if the sector subtends ~pi.  Only used to
    label, never to decide membership (membership is by exact angular order).
    A proper wedge split is one where the boundary rays are NOT antipodal."""
    ang = {}
    for idx in sector:
        dx = points[idx][0] - O[0]
        dy = points[idx][1] - O[1]
        ang[idx] = math.atan2(float(dy), float(dx))
    # angular width of the sector = max CCW gap that contains no sector point
    # is not what we need; approximating by span of sector angles mod 2pi.
    vals = sorted((v % (2 * math.pi)) for v in ang.values())
    # width if contiguous run (it is): wrap-gap
    gaps = [vals[(i + 1) % len(vals)] - vals[i] if i + 1 < len(vals)
            else (vals[0] + 2 * math.pi) - vals[-1]
            for i in range(len(vals))]
    empty = max(gaps)          # the empty angular gap (the complement sector)
    width = 2 * math.pi - empty
    return abs(width - math.pi) < 1e-9


def is_avoiding(pts_sub, k):
    """True iff pts_sub contains NO convex k-gon (exact oracle)."""
    return not has_convex_k_subset(pts_sub, k)[0]


# ---------------------------------------------------------------------------
# STEP A main
# ---------------------------------------------------------------------------

def step_a_control(ns=(5, 6, 7)):
    print("=== STEP A / control: pi-wedge = full rotating-LINE enumeration ===")
    results = {}
    for n in ns:
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        sides = ordered_pair_sides(pts)
        match = (len(sides) == N * (N - 1))
        target = 2 ** (n - 3)
        valid = []
        checked = 0
        for side in sides:
            if len(side) != target:
                continue
            comp = frozenset(range(N)) - side
            if len(comp) != target:
                continue
            checked += 1
            if (is_avoiding([pts[i] for i in side], n - 1)
                    and is_avoiding([pts[i] for i in comp], n - 1)):
                valid.append((sorted(side), sorted(comp)))
        cnt = len(set(frozenset((frozenset(L), frozenset(R))) for L, R in valid))
        results[n] = cnt
        print(f"n={n}: N={N}  sides_enum={len(sides)} (=N(N-1)={N*(N-1)}? {match})"
              f"  size-target checked={checked}  VALID line splits={len(valid)} "
              f"(distinct bipartitions={cnt})")
        for (L, R) in valid[:6]:
            print(f"     L={L}  R={R}")
    return results


def apex_sweep(n, apexes):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    target = 2 ** (n - 3)
    print(f"\n=== STEP A / proper-wedge apex sweep: n={n} N={N} target={target} ===")
    grand = []          # (apex, L, R) valid
    for O in apexes:
        if not apex_general(pts, O):
            print(f"  apex {O}: NOT in general position w.r.t. points -- SKIPPED")
            continue
        order = angular_order(pts, O)
        valid_here = []
        for sector, comp in run_sector_pairs(order, target, N):
            if is_avoiding([pts[i] for i in sector], n - 1) and \
               is_avoiding([pts[i] for i in comp], n - 1):
                hp = wedge_is_halfplane(pts, O, sector)
                valid_here.append((sorted(sector), sorted(comp), hp))
        print(f"  apex {O}: distinct size-{target} bipartitions swept; "
              f"both-halves-({n-1})-avoiding: {len(valid_here)}")
        for (L, R, hp) in valid_here:
            tag = "HALFPLANE(=pi)" if hp else "PROPER wedge"
            print(f"      {tag}: L={L}")
            print(f"             R={R}")
        grand.extend((O, L, R) for (L, R, hp) in valid_here)
    return grand


# ---------------------------------------------------------------------------
# STEP B: split-6-gon spectrum via per-point cap/cup chain ends
# ---------------------------------------------------------------------------

def chain_end_lengths(points):
    """points with distinct x, sorted by x.  Returns (cup_ending, cap_ending)
    where cup_ending[i] = longest cup ending exactly at point i, and
    cap_ending[i] likewise for caps.  Exact slope comparisons (reduced
    (dy,dx), dx>0)."""
    pts = sorted(points, key=lambda p: p[0])
    m = len(pts)
    def slope(a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        # reduce
        import math as _m
        g = _m.gcd(dx, dy)
        return (dy // g, dx // g)
    cup = [1] * m   # length ending at i
    cup_last = [None] * m
    cap = [1] * m
    cap_last = [None] * m
    for i in range(m):
        # cup
        best_len, best_s = 1, None
        for j in range(i):
            s = slope(pts[j], pts[i])
            if cup_last[j] is None:
                cand = cup[j] + 1
                if cand > best_len:
                    best_len, best_s = cand, s
            else:
                # need s > last  (cross multiply, dx>0 so denominators positive)
                lj = cup_last[j]
                if s[0] * lj[1] > lj[0] * s[1]:
                    cand = cup[j] + 1
                    if cand > best_len:
                        best_len, best_s = cand, s
        cup[i] = best_len
        cup_last[i] = best_s
        # cap
        best_len, best_s = 1, None
        for j in range(i):
            s = slope(pts[j], pts[i])
            if cap_last[j] is None:
                cand = cap[j] + 1
                if cand > best_len:
                    best_len, best_s = cand, s
            else:
                lj = cap_last[j]
                if s[0] * lj[1] < lj[0] * s[1]:   # s < last
                    cand = cap[j] + 1
                    if cand > best_len:
                        best_len, best_s = cand, s
        cap[i] = best_len
        cap_last[i] = best_s
    return cup, cap, pts


def step_b(n=7):
    print(f"\n=== STEP B: split-(6)-gon spectrum of WHOLE es_construct({n}) ===")
    pts, blocks = es_set_blocks(n)
    cup, cap, pts_sorted = chain_end_lengths(pts)
    m = len(pts_sorted)
    print(f"  N={m} points (index i is the i-th smallest x)")
    best_sum = 0
    best_i = None
    for i in range(m):
        s = cup[i] + cap[i]
        if s > best_sum:
            best_sum, best_i = s, i
    # also global maxima
    maxcup = max(cup)
    maxcap = max(cap)
    print(f"  global longest cup={maxcup}, longest cap={maxcap}")
    print(f"  per-rightmost-point cap[i],cup[i]; max(cap+cup) over rightmost r:")
    for i in range(m):
        print(f"    r=(x={pts_sorted[i][0]}): cap={cap[i]} cup={cup[i]} sum={cap[i]+cup[i]}")
    print(f"  => max(a+u) = {best_sum} at rightmost point x={pts_sorted[best_i][0]}")
    print(f"  split-6-gon needs a+u=8; threshold ESsplit(6)=2^4+1=17 points.")
    print(f"  N={m} >= 17, so the theorem forces a split 6-gon iff max(a+u) >= 8.")
    print(f"  max(a+u) reached: {best_sum}  -> split 6-gon present: {best_sum >= 8}")


def block_index_map(n):
    pts, blocks = es_set_blocks(n)
    mp = []
    for b, blk in enumerate(blocks):
        for _ in blk:
            mp.append(b)
    return mp


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    from fractions import Fraction
    ctrl = step_a_control()

    apexes56 = [(Fraction(2500), Fraction(2750)), (Fraction(2500), Fraction(3000))]
    print("\n--- proper-wedge apex sweep n=5,6 (named apexes) ---")
    step_a_apex = []
    for n in (5, 6):
        step_a_apex.append((n, apex_sweep(n, apexes56)))

    # n=7: sweep a grid of central apexes (drop any w/ collinear ties)
    print("\n--- n=7 proper-wedge apex sweep grid ---")
    apex7 = []
    for xx in (2300, 2400, 2500, 2600, 2700):
        for yy in (2600, 2725, 2750, 2850, 3000):
            apex7.append((Fraction(xx), Fraction(yy)))
    # ensure the named probes are included
    for ap in apexes56:
        if ap not in apex7:
            apex7.append(ap)
    res7 = apex_sweep(7, apex7)

    print("\n=== SUMMARY ===")
    print(f"Control pi-wedge (full line) valid bipartitions: n=5 -> {ctrl[5]}, "
          f"n=6 -> {ctrl[6]}, n=7 -> {ctrl[7]}")
    for n, g in step_a_apex:
        print(f"n={n}: proper-wedge valid splits over named apexes: {len(g)}")
    print(f"n=7: proper-wedge valid splits over swept apex grid: {len(res7)} "
          f"(apexes used: {len(apex7)})")
    if res7:
        print("  A PROPER WEDGE SPLIT EXISTS AT n=7:")
        for (O, L, R) in res7:
            print(f"    apex {O}: L={L}")
            print(f"             R={R}")
    else:
        print("  NO proper-wedge split at n=7 yields two 16-point 6-avoiding "
              "halves over the swept apex grid.")

    # even/odd block-bipartition comparison
    mp = block_index_map(7)
    even = [i for i in range(32) if mp[i] % 2 == 0]
    odd = [i for i in range(32) if mp[i] % 2 == 1]
    print(f"\n  [context] even-index block indices (size {len(even)}):")
    print("   ", even)
    print(f"  [context] odd-index block indices  (size {len(odd)}):")
    print("   ", odd)
    print("  (compare against any valid wedge split index sets above)")


if __name__ == "__main__":
    main()
