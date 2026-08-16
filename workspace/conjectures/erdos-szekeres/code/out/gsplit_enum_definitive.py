#!/usr/bin/env python3
"""CORRECTED complete enumeration of open half-plane sides (k-sets).

The classical k-set fact: every distinct open half-plane side of a general
position point set is realized by a directed line through an ORDERED pair
(a,b), with the two on-line points a,b assigned to the left side in each of
the 4 inclusion patterns (neither / a / b / both), combined with the strict
left side of the directed line a->b.

So: for each ordered pair (a,b), a in {0..N-1}, b != a,
    strict = { x : orient(a,b,x) > 0 }
    sides = { strict, strict|{a}, strict|{b}, strict|{a,b} }  (as frozensets)
Dedup across all ordered pairs.  For a general position set this set equals
the set of all nonempty-proper open half-plane sides, of cardinality N(N-1).

Validated EXACTLY (zero missing, zero extra) against a 2^N brute-force oracle
(strict convex-hull separation, which does not use any line construction) for
general-position integer sets at N = 8,10,12,14,16.

Then re-runs the n=7 gsplit question on the verified es_construct set using
this complete, validated enumeration.

Exact integer arithmetic throughout (orient via determinants); no floats.
"""

from itertools import combinations
from lib.es_geom import orient, convex_hull, in_general_position, has_convex_k_subset


# ------------------------- brute-force oracle -------------------------

def segs_intersect_closed(a, b, c, d):
    o1 = orient(a, b, c); o2 = orient(a, b, d)
    o3 = orient(c, d, a); o4 = orient(c, d, b)
    if o1 == 0: return on_segment(c, a, b)
    if o2 == 0: return on_segment(d, a, b)
    if o3 == 0: return on_segment(a, c, d)
    if o4 == 0: return on_segment(b, c, d)
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


def on_segment(q, a, b):
    if orient(a, b, q) != 0:
        return False
    return (min(a[0], b[0]) <= q[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= q[1] <= max(a[1], b[1]))


def point_in_poly(p, h):
    if len(h) < 3:
        return False
    m = len(h)
    signs = [orient(h[t], h[(t + 1) % m], p) for t in range(m)]
    return all(s >= 0 for s in signs) or all(s <= 0 for s in signs)


def hulls_overlap(S, T):
    hS = convex_hull(S); hT = convex_hull(T)
    for t in range(len(hS)):
        a, b = hS[t], hS[(t + 1) % len(hS)]
        for u in range(len(hT)):
            c, d = hT[u], hT[(u + 1) % len(hT)]
            if segs_intersect_closed(a, b, c, d):
                return True
    for p in S:
        if point_in_poly(p, hT): return True
    for p in T:
        if point_in_poly(p, hS): return True
    return False


def oracle_open_sides(points):
    N = len(points)
    res = set()
    for mask in range(1, (1 << N) - 1):
        S = [points[i] for i in range(N) if (mask >> i) & 1]
        T = [points[i] for i in range(N) if not ((mask >> i) & 1)]
        if not S or not T:
            continue
        if not hulls_overlap(S, T):
            res.add(frozenset(i for i in range(N) if (mask >> i) & 1))
    return res


# ------------------------- corrected ordered-pair enumeration -------------------------

def ordered_pair_sides(points):
    """For each ORDERED pair (a,b), the strict-left side plus the 4 inclusions
    of the two on-line points.  Dedup.  Returns set of nonempty-proper sides."""
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


# ------------------------- main -------------------------

def main():
    import random
    rng = random.Random(2025)

    print("=== Phase 1: validate corrected ordered-pair enumeration vs 2^N oracle ===")
    all_ok = True
    for N in (8, 10, 12, 14, 16):
        pts = []
        while len(pts) < N:
            p = (rng.randint(0, 2000), rng.randint(0, 2000))
            if in_general_position(pts + [p]):
                pts.append(p)
        oracle = oracle_open_sides(pts)
        op = ordered_pair_sides(pts)
        missing = oracle - op
        extra = op - oracle
        ok = (not missing) and (not extra) and (len(op) == N * (N - 1))
        all_ok = all_ok and ok
        print(f"N={N}: oracle={len(oracle)}  ordered_pair={len(op)}  N(N-1)={N*(N-1)}")
        print(f"   missing={len(missing)}  extra={len(extra)}  EXACT MATCH: {ok}")
        if missing:
            print("     example missing:", sorted(missing)[:3])
        if extra:
            print("     example extra  :", sorted(extra)[:3])
    print(f"ALL N EXACT (zero missing, zero extra, count=N(N-1)): {all_ok}")

    print("\n=== Phase 2: re-run n=7 gsplit question on verified es_construct ===")
    from lib.es_construct import es_set_blocks
    for n in (5, 6, 7):
        all_pts, blocks = es_set_blocks(n)
        N = len(all_pts)
        op = ordered_pair_sides(all_pts)
        match = (len(op) == N * (N - 1))
        target = 2 ** (n - 3)
        valid = []
        checked = 0
        for side in op:
            if len(side) != target:
                continue
            checked += 1
            comp = frozenset(range(N)) - side
            if len(comp) != target:
                continue
            L_av = not has_convex_k_subset([all_pts[i] for i in side], n - 1)[0]
            R_av = not has_convex_k_subset([all_pts[i] for i in comp], n - 1)[0]
            if L_av and R_av:
                valid.append((sorted(side), sorted(comp)))
        print(f"n={n}: N={N}  sides_enum={len(op)} (=N(N-1)={N*(N-1)}? {match})"
              f"  size-target checked={checked}"
              f"  VALID splits (halves {target} pts, (n-1)-avoiding): {len(valid)}")
        for (L, R) in valid[:5]:
            print(f"      L={L}  R={R}")


if __name__ == "__main__":
    main()
