#!/usr/bin/env python3
"""Complete the directive-16 framing answer: for n=5,6,7, is the even/odd
block bipartition of es_construct realized by (a) a single open half-plane
side, (b) an intersection of two open half-plane sides (double wedge)?

Extends wedge_evenodd_check.py (which answered n=7 only) to all three n.
Exact integer/Fraction arithmetic throughout; no floats.
"""

from lib.es_geom import orient, has_convex_k_subset
from lib.es_construct import es_set_blocks


def ordered_pair_sides(points):
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


def block_index_map(blocks):
    mp = []
    for b, blk in enumerate(blocks):
        for _ in blk:
            mp.append(b)
    return mp


def main():
    for n in (5, 6, 7):
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        TARGET = 2 ** (n - 3)
        FULL = frozenset(range(N))
        mp = block_index_map(blocks)
        even = frozenset(i for i in range(N) if mp[i] % 2 == 0)
        odd = frozenset(i for i in range(N) if mp[i] % 2 == 1)
        assert len(even) == len(odd) == TARGET, (n, len(even), len(odd))
        eo_bip = frozenset((even, odd))

        sides = list(ordered_pair_sides(pts))
        sides_size16 = [s for s in sides if len(s) == TARGET]
        in_line = any(frozenset((s, FULL - s)) == eo_bip for s in sides_size16)

        in_dwedge = False
        for i in range(len(sides)):
            for j in range(i + 1, len(sides)):
                inter = sides[i] & sides[j]
                if len(inter) != TARGET:
                    continue
                comp = FULL - inter
                if len(comp) != TARGET:
                    continue
                if frozenset((inter, comp)) == eo_bip:
                    in_dwedge = True
                    break
            if in_dwedge:
                break

        av = (not has_convex_k_subset([pts[i] for i in even], n - 1)[0]
              and not has_convex_k_subset([pts[i] for i in odd], n - 1)[0])
        print(f"n={n}: even/odd split (sizes {len(even)}/{len(odd)}, "
              f"(n-1)-avoiding={av}) "
              f"in open-half-plane sides: {in_line}, "
              f"in double-wedge intersections: {in_dwedge}")


if __name__ == "__main__":
    main()