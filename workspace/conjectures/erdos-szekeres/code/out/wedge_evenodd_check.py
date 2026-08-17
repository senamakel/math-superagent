#!/usr/bin/env python3
"""Direct answer to the directive-16 framing question: which CUT FAMILY
realizes the known even/odd block split on es_construct(7)?

Context established by wedge_split_v2.py (captured2, EXIT 0):
  * single open half-plane (rotating-line) cuts: 0 valid size-16 splits at n=7
  * double-wedge cuts = intersections of two open half-plane sides
    (exhaustive SUPERSET of wedge-realizable cuts): 27 valid splits at n=7,
    positive control (witness apex (2400,2725) split) PASS
The even/odd block bipartition is a valid split (both halves 6-avoiding) by
gsplit_consistent.py at n=5,6,7.  This script settles: is it realized as an
intersection of two open half-plane sides (i.e. is it inside the double-wedge
family)?  It recomputes the 2454 size-16 intersections from scratch, checks
membership of the even/odd bipartition, and independently re-verifies the
6-avoidance of both halves by largest_convex_subset (2^16 subsets each, exact).

Exact integer/Fraction arithmetic throughout (lib.es_geom.orient); no floats.
"""

from lib.es_geom import largest_convex_subset, has_convex_k_subset
from lib.es_geom import orient
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
    n = 7
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    TARGET = 2 ** (n - 3)          # 16
    FULL = frozenset(range(N))

    mp = block_index_map(blocks)
    even = frozenset(i for i in range(N) if mp[i] % 2 == 0)
    odd = frozenset(i for i in range(N) if mp[i] % 2 == 1)
    assert len(even) == len(odd) == TARGET
    eo_bip = frozenset((even, odd))
    print(f"n={n}: even-index block half = {sorted(even)}")
    print(f"        odd-index block half  = {sorted(odd)}")

    # independent re-verification: both halves 6-avoiding (exact, 2^16 each)
    print("\n=== independent 6-avoidance of even/odd halves ===")
    ok = True
    for name, half in (("even", even), ("odd", odd)):
        k, w = largest_convex_subset([pts[i] for i in half])
        has6 = has_convex_k_subset([pts[i] for i in half], 6)[0]
        print(f"  {name} half size={len(half)}: largest convex subset = {k} "
              f"(no convex 6-gon: {not has6})")
        ok = ok and (k <= 5 and not has6)
    print(f"  both halves (n-1)-avoiding: {ok}")

    # recompute the size-16 double-wedge intersections from scratch
    print("\n=== double-wedge family (intersections of two open half-plane sides) ===")
    sides = list(ordered_pair_sides(pts))
    M = len(sides)
    print(f"  open half-plane sides: {M} (=N(N-1)={N*(N-1)}? {M == N*(N-1)})")
    splits = {}          # bip -> (halfA, halfB)
    seen = set()
    size16_pairs = 0
    for i in range(M):
        for j in range(i + 1, M):
            inter = sides[i] & sides[j]
            if len(inter) == TARGET:
                size16_pairs += 1
                comp = FULL - inter
                if len(comp) != TARGET:
                    continue
                bip = frozenset((inter, comp))
                if bip not in seen:
                    seen.add(bip)
                    a, c = tuple(bip)
                    splits[bip] = (frozenset(a), frozenset(c))
    print(f"  pairs of sides: {M*(M-1)//2}")
    print(f"  pairs with |inter|=={TARGET}: {size16_pairs}")
    print(f"  distinct size-{TARGET} split bipartitions: {len(splits)}")

    eo_in_family = eo_bip in splits
    print(f"\n  even/odd bipartition among double-wedge intersections: "
          f"{eo_in_family}")
    if eo_in_family:
        a, c = splits[eo_bip]
        print(f"    realized as intersection of two open half-plane sides: "
              f"L={sorted(a)} R={sorted(c)}")
    # if it IS in the family, is it 6-avoiding (i.e. among the 27 valid)?
    if eo_in_family:
        okA = not has_convex_k_subset([pts[i] for i in splits[eo_bip][0]], 6)[0]
        okB = not has_convex_k_subset([pts[i] for i in splits[eo_bip][1]], 6)[0]
        print(f"    both halves 6-avoiding (so among valid splits): {okA and okB}")

    print("\n=== verdict ===")
    print("  line family (open half-planes): 0 valid splits at n=7 "
          "(established by wedge_split_v2 / gsplit_phase2)")
    print(f"  double-wedge side-pair family: {len(splits)} distinct size-16 "
          f"bipartitions; even/odd among them: {eo_in_family}")
    print("  independent even/odd 6-avoidance (largest_convex_subset):",
          "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()