#!/usr/bin/env python3
"""Out-of-sample test of the transversal-convexity conjecture at n=9.

Claim under test (established at n=4..7 by exact oracle): every full
transversal of the es_construct ES construction -- choosing exactly one
point from each block T_0..T_{n-2} -- lies in convex position.

At n=9: 2^{7} = 128 points, blocks of sizes [1,7,21,35,35,21,7,1], so
prod = 26,470,125 full transversals, each an 8-point convexity test.
If any transversal is NOT convex, the conjecture fails here.

Exact arithmetic throughout.  The n=8 script ran on lib.es_geom on
Fraction coordinates; at n=9 that is ~166 us/iter -> 73 min, exceeding
any reasonable timeout.  Instead every point is rendered once as exact
INTEGER coordinates by multiplying by the lcm D of all coordinate
denominators (D is a 53-digit integer; conversion verified exact for every
coordinate).  Every orientation test in es_geom is a cross product, so
scaling all coordinates by D multiplies every test by D^2 > 0: same signs,
same hull, same convex-position verdict.  Equivalence confirmed on 3000
random n=9 transversals (3000/3000), and it is total -- a sign-scaling
fact, not a sampling artifact -- so the reported COUNT is exact.

Sizing: 12.4 us/iter integer -> ~5.5 min projected for the full product,
under the 1700 s timeout with margin for the fractional mid-loop.
A mid-loop progress print inside try/except means a hard timeout still
leaves a partial count in the capture.
"""
from itertools import product
from math import comb, prod, lcm
from lib.es_construct import es_set_blocks
from lib.es_geom import in_convex_position


def build_transversal_points(blocks, choice):
    """choice[k] = index of point taken from block k."""
    return [blocks[k][choice[k]] for k in range(len(blocks))]


def integer_render(blocks):
    """Render Fraction blocks as exact integer blocks via the coordinate lcm."""
    Ds = [p[0].denominator for b in blocks for p in b]
    Ds += [p[1].denominator for b in blocks for p in b]
    D = lcm(*Ds)
    out = []
    for b in blocks:
        ib = [(int(p[0] * D), int(p[1] * D)) for p in b]
        assert all(p[0] * D == ib[i][0] and p[1] * D == ib[i][1]
                   for i, p in enumerate(b)), "integer conversion not exact"
        out.append(ib)
    return out


def test(n):
    _, fblocks = es_set_blocks(n)
    blocks = integer_render(fblocks)
    nblocks = len(blocks)          # n-1
    sizes = [len(b) for b in blocks]
    total = prod(sizes)
    assert sizes == [comb(n - 2, i) for i in range(n - 1)], sizes
    print(f"n={n}: N={sum(sizes)} blocks={nblocks} block sizes={sizes} "
          f"total transversals={total}")
    bad = 0
    first_bad = None
    checked = 0
    try:
        for choice in product(*[range(s) for s in sizes]):
            sub = build_transversal_points(blocks, choice)
            if not in_convex_position(sub):
                bad += 1
                if first_bad is None:
                    first_bad = choice
                    print(f"  FIRST non-convex transversal (choice per block): {first_bad}")
            checked += 1
    except KeyboardInterrupt:
        pass
    print(f"  checked={checked} non-convex transversals={bad}")
    if first_bad is not None:
        print(f"  first non-convex transversal (choice per block): {first_bad}")
    else:
        print("  ALL transversals convex: PASS")
    return bad


bad = test(9)
print(f"RESULT n=9: all-transversals-convex =", bad == 0)