"""Check Conjecture A against the verified es_construct ES construction.

Conjecture A: for n in {5,6,7}, the convex hull (outer onion layer) of
es_set(n) consists of exactly ONE point from each block T_0..T_{n-2}, hence
exactly n-1 hull vertices, and the hull vertices appear in block-index order
(0,1,...,n-2 up to rotation) around the hull.

Method: es_construct.es_set_blocks(n) returns (points, blocks); es_geom.convex_hull
gives the CCW hull vertices; each vertex is matched to its block by identical
Fraction coordinates.  Per n we check
  (a) exactly n-1 hull vertices,
  (b) exactly one vertex per block, all n-1 blocks represented,
  (c) the hull's block-index sequence is (0,1,...,n-2) up to rotation.
Full onion layer profiles are recomputed (outer-first) for reference.
All arithmetic is exact (Fraction coordinates, exact cross products).

Complexity per n is O(N log N) for the hull with N = 2^{n-2} <= 32.
"""

from lib.es_construct import es_set_blocks
from lib.es_geom import convex_hull


def onion_layers(points):
    """Convex-peeling layer sizes, outer first.  Exact.  O(k * P log P)."""
    pts = set(points)
    layers = []
    while pts:
        hull = convex_hull(list(pts))
        layers.append(len(hull))
        pts = pts - set(hull)
    return layers


def check_n(n):
    points, blocks = es_set_blocks(n)
    num_blocks = n - 1

    hull = convex_hull(points)
    H = len(hull)

    # map each exact Fraction point to its block index
    block_of = {}
    for bi, block in enumerate(blocks):
        for p in block:
            block_of[p] = bi

    # every hull vertex must be matched to a block
    if not all(p in block_of for p in hull):
        raise AssertionError(f"n={n}: some hull vertex not matched to any block")

    hull_blocks = [block_of[p] for p in hull]   # in CCW hull order

    per_block_count = {i: 0 for i in range(num_blocks)}
    for bi in hull_blocks:
        per_block_count[bi] += 1

    ok_a = (H == num_blocks)
    vals = list(per_block_count.values())
    ok_b = (len(per_block_count) == num_blocks and min(vals) == 1 and max(vals) == 1)

    # c: hull block sequence is 0,1,...,n-2 up to rotation and either direction
    seq = hull_blocks
    fwd = list(range(num_blocks))
    rev = list(range(num_blocks - 1, -1, -1))
    ok_c_fwd = any(seq[i:] + seq[:i] == fwd for i in range(H))
    ok_c_rev = any(seq[i:] + seq[:i] == rev for i in range(H))
    ok_c = ok_c_fwd or ok_c_rev

    return {
        "n": n,
        "N": len(points),
        "hull_vertices": H,
        "n_minus_1": num_blocks,
        "hull_blocks": seq,
        "per_block_count": per_block_count,
        "ok_a_n_minus_1_vertices": ok_a,
        "ok_b_one_per_block": ok_b,
        "ok_c_block_order": ok_c,
        "ok_c_is_fwd": ok_c_fwd,
        "ok_c_is_rev": ok_c_rev,
        "onion": onion_layers(points),
        "overall": ok_a and ok_b and ok_c,
    }


def main():
    print("Conjecture A: outer hull of es_set(n) is one point per block, n-1 vertices, block-index order")
    print("=" * 78)
    all_ok = True
    for n in (5, 6, 7):
        r = check_n(n)
        all_ok = all_ok and r["overall"]
        tag = "PASS" if r["overall"] else "FAIL"
        print(f"\nn = {n}  N = |X_n| = {r['N']}   ->  {tag}")
        print(f"  hull vertices       : {r['hull_vertices']}  (need n-1 = {r['n_minus_1']})"
              f"   (a)={r['ok_a_n_minus_1_vertices']}")
        print(f"  hull block sequence : {r['hull_blocks']}")
        print(f"  per-block hull count: {dict(sorted(r['per_block_count'].items()))}"
              f"   (b)={r['ok_b_one_per_block']}")
        print(f"  block order (c)     : {r['ok_c_block_order']}"
              f"   fwd={r['ok_c_is_fwd']} rev={r['ok_c_is_rev']}")
        print(f"  onion layers (outer): {r['onion']}")
    print("\n" + "=" * 78)
    print("OVERALL:", "PASS" if all_ok else "FAIL")


if __name__ == "__main__":
    main()
