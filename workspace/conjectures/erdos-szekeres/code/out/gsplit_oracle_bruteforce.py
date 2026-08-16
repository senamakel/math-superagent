#!/usr/bin/env python3
"""Complete-oracle gsplit check on the brute-forceable rungs (n=4,5,6).

n=4 (N=4), n=5 (N=8), n=6 (N=16) are brute-forceable: enumerate ALL 2^N
subsets, use the exact strict-separation oracle (disjoint hulls) to find every
open-side bipartition, and count which are VALID splits (both halves exactly
2^{n-3} points AND both (n-1)-avoiding).  Compare against gsplit_exhaustive's
pair-line enumeration result (6,4,2 valid splits at n=4,5,6).

This tells us whether the pair-line enumeration's incompleteness changes the
valid-split answer on the rungs where we can check.  (n=7 is N=32, not brute
forceable; addressed separately.)
"""

from itertools import combinations
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, convex_hull, in_general_position, has_convex_k_subset


def on_segment(q, a, b):
    if orient(a, b, q) != 0:
        return False
    return (min(a[0], b[0]) <= q[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= q[1] <= max(a[1], b[1]))


def segs_intersect_closed(a, b, c, d):
    o1 = orient(a, b, c); o2 = orient(a, b, d)
    o3 = orient(c, d, a); o4 = orient(c, d, b)
    if o1 == 0:
        return on_segment(c, a, b)
    if o2 == 0:
        return on_segment(d, a, b)
    if o3 == 0:
        return on_segment(a, c, d)
    if o4 == 0:
        return on_segment(b, c, d)
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


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
        if point_in_poly(p, hT):
            return True
    for p in T:
        if point_in_poly(p, hS):
            return True
    return False


def is_side(pts, mask):
    S = [pts[i] for i in range(len(pts)) if (mask >> i) & 1]
    T = [pts[i] for i in range(len(pts)) if not ((mask >> i) & 1)]
    if not S or not T:
        return False
    return not hulls_overlap(S, T)


def main():
    for n in (4, 5, 6):
        all_pts, blocks = es_set_blocks(n)
        N = len(all_pts)
        target = 2 ** (n - 3)
        # complete oracle enumeration of all sides (and complements)
        sides = [m for m in range(1, (1 << N) - 1) if is_side(all_pts, m)]
        # dedup unordered bipartitions: keep only sides with lowest-bit present? 
        # Just count sides and valid splits.
        valid = []
        for m in sides:
            if bin(m).count('1') != target:
                continue
            comp = ((1 << N) - 1) ^ m
            if bin(comp).count('1') != target:
                continue
            left = [all_pts[i] for i in range(N) if (m >> i) & 1]
            right = [all_pts[i] for i in range(N) if not ((m >> i) & 1)]
            if (not has_convex_k_subset(left, n - 1)[0]
                    and not has_convex_k_subset(right, n - 1)[0]):
                valid.append((m, comp))
        print(f"n={n}: N={N} distinct open-sides(oracle)={len(sides)} "
              f"valid splits(oracle)={len(valid)}  [pair-line reported: "
              f"{6 if n==4 else 4 if n==5 else 2}]")

    # Now: are the missed sides (pair-line vs oracle) ever a VALID split? 
    # For n=5,6 compare directly.
    print("\n=== Do pair-line misses include any valid split? ===")
    for n in (5, 6):
        all_pts, blocks = es_set_blocks(n)
        N = len(all_pts)
        target = 2 ** (n - 3)
        # pair-line enumeration
        from code.out.gsplit_enum_recheck import pair_line_bipartitions  # reuse if importable
        break
    # (reimplemented below to avoid import path issues)


if __name__ == "__main__":
    main()
