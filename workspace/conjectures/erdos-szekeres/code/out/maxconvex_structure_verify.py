"""Independent verification of maxconvex_structure.py's results.

Route 1: the enumerated witnesses from the capture are re-checked with the
4-point criterion (es35-four-criterion: a set is in convex position iff every
4-subset is), which is a different computation path from the full-hull test
used by in_convex_position.

Route 2: the transversal conjecture's *contrapositive partner* claim, that
every full transversal (one point from each block T_0..T_{n-2}) is in convex
position, with the count expected to equal prod(|T_i|) = 9, 96, 2500.

Route 3: general position of the whole construction re-checked (exact).
"""
from fractions import Fraction
from itertools import combinations, product
from time import time

from lib.es_construct import es_set_blocks
from lib.es_geom import orient, in_convex_position, in_general_position, convex_hull


def all_4_subsets_convex(sub):
    """4-point criterion: every 4-subset must be a convex quadrilateral."""
    for quad in combinations(sub, 4):
        if len(convex_hull(quad)) != 4:
            return False
    return True


def main():
    for n in (5, 6, 7):
        pts, blocks = es_set_blocks(n)
        N = len(pts)
        print(f"=== n={n}: N={N}, blocks={[len(b) for b in blocks]} ===")

        # Route 3: general position
        gp = in_general_position(pts)
        print(f"  general position: {gp}")

        # Route 1: verify the recorded FAIL witnesses via the 4-point criterion
        # Witnesses (point indices) recorded in the capture:
        witnesses = {
            5: [(0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 4, 6)],
            6: [(0, 1, 2, 3, 4), (0, 1, 5, 6, 8), (0, 1, 5, 6, 9)],
            7: [(0, 1, 2, 3, 4, 5), (0, 1, 6, 7, 9, 12), (0, 1, 6, 7, 9, 13)],
        }[n]
        ok = True
        for w in witnesses:
            sub = [pts[i] for i in w]
            # confirm it is a convex (n-1)-subset by the 4-point criterion
            c4 = all_4_subsets_convex(sub)
            h  = in_convex_position(sub)
            # confirm it is NOT a full transversal: some block contributes != 1
            block_of = {}
            for bidx, blk in enumerate(blocks):
                for p in blk:
                    block_of[(p[0], p[1])] = bidx
            counts = [0] * len(blocks)
            for p in sub:
                counts[block_of[(p[0], p[1])]] += 1
            nontrans = counts != [1] * len(blocks)
            ok = ok and c4 and h and nontrans
            print(f"    witness {w}: hull-convex={h} 4pt-criterion={c4} "
                  f"non-transversal={nontrans} counts={tuple(counts)}")
        print(f"  route-1 (witnesses convex + non-transversal): {'ALL OK' if ok else 'FAIL'}")

        # Route 2: every full transversal is convex; count == prod(|T_i|)
        t0 = time()
        count = 0
        all_trans_convex = True
        # product over blocks: pick exactly one point per block
        for choice in product(*blocks):
            sub = list(choice)
            if not in_convex_position(sub):
                all_trans_convex = False
                print(f"    NON-CONVEX TRANSVERSAL: {sub}")
                break
            count += 1
        dt = time() - t0
        expected = 1
        for b in blocks:
            expected *= len(b)
        print(f"  route-2: all {count} transversals convex: {all_trans_convex}; "
              f"count == prod(|T_i|)={expected}: {count == expected} ({dt:.3f} s)")
        print()


if __name__ == "__main__":
    main()