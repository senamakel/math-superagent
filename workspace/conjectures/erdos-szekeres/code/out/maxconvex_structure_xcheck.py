"""Cross-check the pattern-distribution counts by an independent code path.

Main run (maxconvex_structure.py): C(N,n-1) subsets, full hull test.
This run:  1) sum of reported per-pattern counts == total convex count;
           2) full C(N,n-1) enumeration over point-index combinations with
              the *4-point criterion* instead of the full hull test, comparing
              the per-pattern distribution one-to-one.

Both exact; the two convexity tests are independent implementations of two
forms of the same criterion (hull-vertex vs every-4-subset-convex).
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter
from time import time

from lib.es_construct import es_set_blocks
from lib.es_geom import convex_hull

MAIN_PATTERNS = {
    5: {(0, 0, 3, 1): 1, (0, 2, 1, 1): 9, (0, 2, 2, 0): 9, (1, 1, 1, 1): 9,
        (1, 1, 2, 0): 9, (1, 3, 0, 0): 1},
    6: {(0, 0, 0, 4, 1): 1, (0, 0, 3, 1, 1): 40, (0, 0, 3, 2, 0): 60,
        (0, 2, 1, 1, 1): 144, (0, 2, 1, 2, 0): 216, (0, 2, 3, 0, 0): 60,
        (1, 1, 1, 1, 1): 96, (1, 1, 1, 2, 0): 144, (1, 1, 3, 0, 0): 40,
        (1, 4, 0, 0, 0): 1},
    7: {(0, 0, 0, 0, 5, 1): 1, (0, 0, 0, 4, 1, 1): 205, (0, 0, 0, 4, 2, 0): 410,
        (0, 0, 3, 1, 1, 1): 2300, (0, 0, 3, 1, 2, 0): 4600, (0, 0, 3, 3, 0, 0): 2116,
        (0, 2, 1, 1, 1, 1): 5000, (0, 2, 1, 1, 2, 0): 10000, (0, 2, 1, 3, 0, 0): 4600,
        (0, 2, 4, 0, 0, 0): 410, (1, 1, 1, 1, 1, 1): 2500, (1, 1, 1, 1, 2, 0): 5000,
        (1, 1, 1, 3, 0, 0): 2300, (1, 1, 4, 0, 0, 0): 205, (1, 5, 0, 0, 0, 0): 1},
}


def four_point_convex(sub):
    """Convex iff every 4-subset is a convex quadrilateral (independent path)."""
    for quad in combinations(sub, 4):
        if len(convex_hull(quad)) != 4:
            return False
    return True


def block_of_map(blocks):
    m = {}
    for bidx, blk in enumerate(blocks):
        for p in blk:
            m[(p[0], p[1])] = bidx
    return m


def main():
    for n in (5, 6, 7):
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        r = n - 1
        bof = block_of_map(blocks)
        main_pats = MAIN_PATTERNS[n]

        # 1) consistency: main run's per-pattern sums == its total
        summed = sum(main_pats.values())
        # the main run's reported total for each n:
        main_totals = {5: 38, 6: 802, 7: 39648}
        main_total = main_totals[n]
        print(f"n={n}: main per-pattern sum {summed} vs main total {main_total}: "
              f"{'OK' if summed == main_total else 'MISMATCH'}")

        # 2) independent enumeration with the 4-point criterion
        t0 = time()
        cnt = Counter()
        for comb in combinations(range(N), r):
            sub = [pts[i] for i in comb]
            if four_point_convex(sub):
                counts = tuple(bof[(p[0], p[1])] for p in sub)
                pat = tuple(counts.count(b) for b in range(len(blocks)))
                cnt[pat] += 1
        dt = time() - t0
        equal = dict(cnt) == main_pats
        print(f"  independent enumeration: {sum(cnt.values())} convex subsets "
              f"({dt:.2f}s); pattern dict equality with main run: "
              f"{'EXACT MATCH' if equal else 'MISMATCH'}")
        if not equal:
            only_indep = {k: v for k, v in cnt.items() if main_pats.get(k) != v}
            only_main = {k: v for k, v in main_pats.items() if cnt.get(k) != v}
            print(f"    in indep-not-main: {only_indep}")
            print(f"    in main-not-indep: {only_main}")
        print()


if __name__ == "__main__":
    main()