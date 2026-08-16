#!/usr/bin/env python3
"""Exhaustive test of G-split-consistent for the es_construct ES construction.

Question (directive): for n = 5, 6, 7, does ANY line (containing no point of
the set) split the ES 2^{n-2}-point extremal set into two halves each free of
a convex (n-1)-gon?  Because total = 2^{n-2} and each (n-1)-avoiding half has
<= 2^{n-3} points, a valid split forces each half to be EXACTLY 2^{n-3} points.

Every combinatorially distinct half-plane bipartition of a finite planar set is
realized by a line through a pair of points (standard k-set fact), so it
suffices to enumerate, for each of the C(N,2) pairs, the lines through the
pair and the small perturbations off them (assigning the two on-line points to
each side), and test each bipartition.

Exact arithmetic throughout (Fractions in es_construct; integer determinants
here).  Reports the exact count of bipartitions tried and what an empty result
rules out.
"""
from itertools import combinations
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, in_general_position, has_convex_k_subset


def equal_sized_parts(total, nminus1):
    """Return (side_size, avoid_size) parameterization."""
    return 2 ** (nminus1 - 1)  # 2^{n-3} target per side


def candidate_bipartitions(pts):
    """Yield distinct frozenset side-subsets reached by lines through pairs,
    with the two pair-points placed on each side in all ways.
    Returns list of (left_set) as frozenset of indices; complement is right."""
    N = len(pts)
    seen = {}
    for (i, j) in combinations(range(N), 2):
        left = set()   # strict side (orient>0)
        right = set()  # orient<0
        for p in range(N):
            if p == i or p == j:
                continue
            if orient(pts[i], pts[j], pts[p]) > 0:
                left.add(p)
            else:
                right.add(p)
        # now place i and j: 4 assignments
        cands = [
            left | {i, j},                 # both to left
            right | {i, j},                # both to right
            left | {i}, right | {j},       # i left, j right
            left | {j}, right | {i},       # j left, i right
        ]
        for c in cands:
            seen[frozenset(c)] = True
    return list(seen.keys())


def main():
    print("=== G-split-consistent: exhaustive line-split test on es_construct ===")
    for n in (4, 5, 6, 7):
        all_pts, blocks = es_set_blocks(n)
        N = len(all_pts)
        gp = in_general_position(all_pts)
        # confirm no convex n-gon
        has_n = has_convex_k_subset(all_pts, n)[0]
        print(f"\nn={n}: N={N} (want 2^{n-2}={2**(n-2)}) "
              f"generalPosition={gp} has_convex_{n}_gon={has_n}")
        if not gp:
            print("   !!! construction not in general position; cannot test split")
            continue
        target = 2 ** (n - 3)            # exact size of each valid half
        total_tried = 0
        valid = []
        bipartitions = candidate_bipartitions(all_pts)
        print(f"   distinct line-bipartitions enumerated: {len(bipartitions)}")
        for left in bipartitions:
            total_tried += 1
            if len(left) != target:
                continue
            # complement is right
            right = frozenset(range(N)) - left
            if len(right) != target:
                continue
            left_pts = [all_pts[i] for i in left]
            right_pts = [all_pts[i] for i in right]
            L_av = not has_convex_k_subset(left_pts, n - 1)[0]
            R_av = not has_convex_k_subset(right_pts, n - 1)[0]
            if L_av and R_av:
                valid.append((sorted(left), sorted(right)))
        print(f"   splits tried (size-target candidates): {total_tried}")
        print(f"   VALID splits (both halves exactly {target} pts, both (n-1)-avoiding): {len(valid)}")
        for (L, R) in valid[:5]:
            print(f"      L={L}  R={R}")

    print("\nWhat an empty result rules out: for THIS es_construct ES construction "
          "at n=5,6,7, no line splits it into two (n-1)-avoiding halves, so the "
          "G-split-consistent claim fails exactly on this template. It does NOT "
          "rule out other extremal sets or the general G-split lemma.")


if __name__ == "__main__":
    main()
