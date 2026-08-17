#!/usr/bin/env python3
"""Wedge-split exhaustive enumeration for lib.es_construct(n=7), via the
steering-directive side-pair reduction.

STEERING (takes precedence over the per-cell design): the cell enumeration is
intractable as written (~10^5 cells * per-cell scan on 496 point-lines), so it
is REPLACED by a reduction that reuses the already-validated component.  The
complete, brute-force-validated list of the N(N-1) open half-plane sides of
the set is exactly what gsplit_enum_definitive proved exhaustive against the
2^N oracle (zero missing, zero extra, count = N(N-1)).  A convex wedge of
angle < pi is exactly the intersection of two open half-planes whose boundary
lines meet at the apex; so every wedge-realizable bipartition is an
intersection of two open half-plane sides, and enumerating PAIRS of sides is a
SUPERSET of the wedge-realizable bipartitions.  A zero valid count here
therefore rules out every proper-wedge cut, strictly stronger than a zero over
wedges.

Pipeline
--------
(1) POSITIVE CONTROL FIRST (assert): the known-good witness apex
    A* = (2400,2725) must be in general position and its angular-order
    contiguous-arc bipartitions of size 16 must include a (6-avoiding) valid
    split; the resulting witness split L=[1,2,3,4,5,16..26], R=[0,6..15,27..31]
    must be one of them.
(2) Independent witness re-verification by a SECOND route:
    lib.es_geom.largest_convex_subset on each half separately (2^16 subsets
    each, exact) -- largest convex subset must be <= 5 on both, i.e. no convex
    6-gon.
(3) FAMILY: the full side-pair superset enumeration.  Every unordered pair of
    the 992 open half-plane sides; keep pairs whose intersection has size
    exactly 2^{n-3}=16; the complement is the other half.  Each distinct split
    is then tested for (n-1)=6-avoidance on BOTH halves.
(4) Control verdict: the witness bipartition MUST appear among the size-16
    side-pair intersections and among the VALID splits.  If it does not, the
    enumeration is wrong and nothing it reports counts.
(5) Parallel exact validity: has_convex_k_subset(...,6) over frozenset halves,
    memoized (halves repeat across orders), across all 28 workers via
    multiprocessing (exact integer/Fraction arithmetic, no floats).
(6) Wedge-realizability: every valid bipartition found by the side-pair
    superset is checked for realizability by an actual wedge -- an apex A and
    two rays bounding a cone of angle < pi whose interior exactly contains the
    half.  The witness apex is verified to realize the witness split.
"""

from fractions import Fraction
from itertools import combinations
from functools import cmp_to_key
from multiprocessing import Pool
import sys, time

from lib.es_geom import orient, has_convex_k_subset, largest_convex_subset
from lib.es_construct import es_set_blocks

N = 32
TARGET = 16          # 2^(n-3), n=7
K = 6                # n-1 avoid
FULL = frozenset(range(N))

# ---------------------------------------------------------------------------
# open half-plane sides (validated complete by gsplit_enum_definitive)
# ---------------------------------------------------------------------------
def ordered_pair_sides(points):
    Np = len(points)
    res = set()
    for a in range(Np):
        for b in range(Np):
            if a == b:
                continue
            strict = frozenset(x for x in range(Np)
                               if orient(points[a], points[b], points[x]) > 0)
            for extra in (frozenset(), frozenset([a]), frozenset([b]),
                          frozenset([a, b])):
                side = strict | extra
                if 0 < len(side) < Np:
                    res.add(side)
    return res

# ---------------------------------------------------------------------------
# apex circular order (exact) -- for the positive control
# ---------------------------------------------------------------------------
def circular_order(points, O):
    def half(idx):
        dx = points[idx][0] - O[0]
        dy = points[idx][1] - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = orient(O, points[a], points[b])
        if c > 0:
            return -1
        if c < 0:
            return 1
        return 0
    return tuple(sorted(range(len(points)), key=cmp_to_key(cmp)))

def apex_general(points, O):
    for a in range(len(points)):
        for b in range(a + 1, len(points)):
            if orient(O, points[a], points[b]) == 0:
                return False
    return True


# worker globals (set via initializer)
_PTS = None
def _init(pts):
    global _PTS
    _PTS = pts

def half_avoids_6(half):
    """Return True iff frozenset `half` contains no convex 6-gon (exact)."""
    return not has_convex_k_subset([_PTS[i] for i in half], 6)[0]


def main():
    t0 = time.time()
    global _PTS
    pts, blocks = es_set_blocks(7)
    _PTS = pts
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    print(f"=== wedge-split side-pair enumeration, n=7 es_construct "
          f"(N={N}, target={TARGET}, avoid k={K}) ===", flush=True)
    print(f"  point box: x in [{min(xs)},{max(xs)}], y in [{min(ys)},{max(ys)}]",
          flush=True)
    print(f"wall t0 = {t0}", flush=True)

    # =================================================================
    # (1) POSITIVE CONTROL FIRST
    # =================================================================
    W = (Fraction(2400), Fraction(2725))
    print("\n=== (1) POSITIVE CONTROL: known-good witness apex "
          f"A* = (2400,2725) ===", flush=True)
    gW = apex_general(pts, W)
    print(f"  apex_general(A*): {gW}", flush=True)
    assert gW, "POSITIVE CONTROL: witness apex must be in general position"
    orderW = circular_order(pts, W)
    witness_L = frozenset(list(range(1, 6)) + list(range(16, 27)))
    witness_R = frozenset(list(range(0, 1)) + list(range(6, 16)) +
                          list(range(27, 32)))
    assert witness_L | witness_R == FULL and len(witness_L) == len(witness_R) == 16
    witness_bip = frozenset((witness_L, witness_R))
    # all contiguous-arc bipartitions of size 16 around the witness apex
    bipsW = []
    for s in range(N):
        arc = frozenset(orderW[(s + k) % N] for k in range(TARGET))
        comp = FULL - arc
        bipsW.append(frozenset((arc, comp)))
    vlist = []
    for b in bipsW:
        a, c = tuple(b)
        if half_avoids_6(a) and half_avoids_6(c):
            vlist.append((sorted(a), sorted(c)))
    print(f"  distinct size-{TARGET} contiguous-arc bipartitions around A*: "
          f"{len(bipsW)}", flush=True)
    print(f"  VALID splits among them: {len(vlist)}", flush=True)
    for a, c in vlist:
        print(f"      VALID arc={a}", flush=True)
        print(f"             comp={c}", flush=True)
    witness_in = any(frozenset((frozenset(a), frozenset(c))) == witness_bip
                     for (a, c) in vlist)
    print(f"  witness split present among A* valid splits: {witness_in}",
          flush=True)
    assert len(vlist) >= 1, "POSITIVE CONTROL FAILED: witness apex must yield >=1 valid split"
    assert witness_in, "POSITIVE CONTROL FAILED: witness split not found via A*"
    print("  POSITIVE CONTROL: PASS", flush=True)

    # =================================================================
    # (2) INDEPENDENT witness re-verification by largest_convex_subset
    # =================================================================
    print("\n=== (2) INDEPENDENT witness re-verification "
          "(largest_convex_subset per half, 2^16 each, exact) ===", flush=True)
    for name, half in (("L", witness_L), ("R", witness_R)):
        kk, w = largest_convex_subset([pts[i] for i in half])
        print(f"  half {name} size={len(half)}: largest convex subset = {kk} "
              f"(must be <= 5 for no convex 6-gon)", flush=True)
        assert kk <= 5, f"INDEPENDENT CHECK FAILED: half {name} has convex {kk}-gon"
    print("  INDEPENDENT re-verification: PASS (both halves avoid a convex 6-gon)",
          flush=True)

    # =================================================================
    # (3) FAMILY: full side-pair superset enumeration
    # =================================================================
    print("\n=== (3) FAMILY: enumerate PAIRS of open half-plane sides, "
          "intersect, keep |inter|=16 ===", flush=True)
    sides = list(ordered_pair_sides(pts))
    M = len(sides)
    print(f"  open half-plane sides: {M}  (=N(N-1)={N*(N-1)}? {M == N*(N-1)})",
          flush=True)
    npairs = M * (M - 1) // 2
    size16_pairs = 0
    splits = {}          # split_bip -> (list of (L,R) index sets)
    splits_seen = set()
    witnessed_split = False
    for i in range(M):
        for j in range(i + 1, M):
            inter = sides[i] & sides[j]
            if len(inter) == TARGET:
                size16_pairs += 1
                comp = FULL - inter
                if len(comp) != TARGET:
                    continue
                bip = frozenset((inter, comp))
                if bip not in splits_seen:
                    splits_seen.add(bip)
                    a, c = tuple(bip)
                    splits[bip] = (frozenset(a), frozenset(c))
                if bip == witness_bip:
                    witnessed_split = True
    nsplits = len(splits_seen)
    print(f"  pairs of sides: {npairs}", flush=True)
    print(f"  pairs with |inter|=={TARGET}: {size16_pairs}", flush=True)
    print(f"  distinct size-{TARGET} split bipartitions: {nsplits}", flush=True)
    print(f"  control: witness bipartition among intersections: "
          f"{witnessed_split}", flush=True)
    assert witnessed_split, "CONTROL FAILED: witness bipartition not among side-pair intersections"

    # collect all distinct halves (with multiplicity info for memoization)
    halves_needed = {}
    for (a, c) in splits.values():
        halves_needed.setdefault(a, 0)
        halves_needed.setdefault(c, 0)
        halves_needed[a] += 1
        halves_needed[c] += 1
    uniq_halves = list(halves_needed.keys())
    print(f"  distinct halves to test for 6-avoidance: {len(uniq_halves)}",
          flush=True)

    # =================================================================
    # (5) PARALLEL exact validity over all halves
    # =================================================================
    print("\n=== (5) parallel exact validity of halves "
          "(has_convex_k_subset(.,6), memoized, multiprocessing) ===", flush=True)
    nworkers = 28
    print(f"  workers: {nworkers}", flush=True)
    av_res = {}
    with Pool(processes=nworkers, initializer=_init, initargs=(pts,)) as pool:
        # chunk to reduce IPC
        results = pool.map(half_avoids_6, uniq_halves, chunksize=8)
    for h, r in zip(uniq_halves, results):
        av_res[h] = r
    navoid = sum(1 for r in results if r)
    print(f"  halves tested: {len(uniq_halves)}; halves avoiding a convex 6-gon: "
          f"{navoid}", flush=True)

    # =================================================================
    # valid splits
    # =================================================================
    valid_splits = []
    for (a, c) in splits.values():
        if av_res[a] and av_res[c]:
            valid_splits.append((frozenset(a), frozenset(c)))
    valid_bips = set(frozenset((a, c)) for (a, c) in valid_splits)
    print(f"\n=== VALID SPLITS (both halves 6-avoiding): {len(valid_bips)} ===",
          flush=True)
    wvalid = witness_bip in valid_bips
    print(f"  witness bipartition among valid splits: {wvalid}", flush=True)
    assert wvalid, "CONTROL FAILED: witness bipartition must be a valid split"
    for (a, c) in sorted(valid_splits, key=lambda bc: sorted(bc[0])):
        print(f"      L={sorted(a)}", flush=True)
        print(f"      R={sorted(c)}", flush=True)

    # =================================================================
    # (6) WEDGE-REALIZABILITY of the valid splits
    # =================================================================
    # A split is wedge-realizable iff its half is the exact interior set of a
    # cone of angle < pi rooted at some apex (contiguous angular block).
    # We test this apex-realizably: for a candidate apex A, S is a wedge iff in
    # the circular angular order around A, S appears as a contiguous block of
    # width < pi.  We probe with a family of apexes (the witness apex is
    # guaranteed to realize the witness split).  For a full claim we report how
    # many valid splits are realized by the witness apex's own cell.
    #
    # Honest scoping: the side-pair superset is exhaustive; realizability over
    # ALL apex cells would require the (intractable) cell enumeration.  We
    # report: (a) the superset valid count, (b) which valid splits are realized
    # by wedges at the witness apex and by wedges at a coarse sweep of apexes.
    print("\n=== (6) WEDGE-REALIZABILITY ===", flush=True)

    def wedge_block(points, A, S):
        """Return the contiguous block indices (in circular order around A)
        occupied by S, or None if S is not a contiguous block."""
        Np = len(points)
        order = circular_order(points, A)
        want = set(S)
        # find a start such that the block of length |S| cyclically equals S
        L = len(S)
        for s in range(Np):
            blk = set(order[(s + k) % Np] for k in range(L))
            if blk == want:
                return [order[(s + k) % Np] for k in range(L)]
        return None

    def proper_wedge(points, A, S):
        """Exact: S is exactly the interior of a proper cone at A of angle < pi.
        Equivalent to: S is a contiguous block in the circular order around A,
        and some point j in the block sees every other block point strictly on
        the same side (cross==orient>0 for all, or orient<0 for all)."""
        if len(S) < 2:
            return len(S) == 1
        blk = wedge_block(points, A, S)
        if blk is None:
            return False
        for j in blk:
            pos = all(orient(A, points[j], points[i]) > 0 for i in blk if i != j)
            neg = all(orient(A, points[j], points[i]) < 0 for i in blk if i != j)
            if pos or neg:
                return True
        return False

    # every valid split: is its smaller-labelled half a proper wedge section at
    # the witness apex W (which is guaranteed to realize the witness split)?
    # We also report how many valid splits are wedge-consistent with W's cell.
    realizable = 0
    whalf = min(witness_L, witness_R, key=lambda h: sorted(h))
    ww = proper_wedge(pts, W, whalf)
    print(f"  witness apex (2400,2725) realizes witness split as proper wedge: "
          f"{ww}", flush=True)
    for vs in sorted(valid_bips, key=lambda b: sorted(min(tuple(b),
                                                          key=lambda h: sorted(h)))):
        a, c = tuple(vs)
        S = min(a, c, key=lambda h: sorted(h))
        # is S a contiguous block (proper wedge section) at the witness apex?
        okW = proper_wedge(pts, W, S)
        # and is the wedgeness witnessed generically: is S a proper sector at
        # SOME apex in a coarse exact rational grid (exact test)?
        okGrid = False
        for gx in range(800, 6001, 1000):
            for gy in range(500000, 7000001, 1000000):
                A = (Fraction(gx), Fraction(gy))
                if not apex_general(pts, A):
                    continue
                if proper_wedge(pts, A, S):
                    okGrid = True
                    break
            if okGrid:
                break
        if okW or okGrid:
            realizable += 1
        print(f"      split L={sorted(a)}  proper-wedge@W={okW} "
              f"wedge-consistent(exact grid)={okGrid}", flush=True)
    print(f"  valid splits wedge-consistent at witness apex or coarse exact "
          f"grid: {realizable}/{len(valid_bips)}", flush=True)
    print("  NOTE: every valid split above is the INTERSECTION of two open "
          "half-plane sides (the exhaustive superset).  Full apex-cell "
          "wedge-realizability would require the intractable cell "
          "enumeration; the apex probe here is a lower bound.", flush=True)

    t1 = time.time()
    print("\n=== SUMMARY ===", flush=True)
    print(f"  cells(side-pairs) tested: {npairs}", flush=True)
    print(f"  size-target pairs (|inter|=={TARGET}): {size16_pairs}", flush=True)
    print(f"  distinct size-{TARGET} splits enumerated: {nsplits}", flush=True)
    print(f"  distinct valid splits (both halves 6-avoiding): {len(valid_bips)}",
          flush=True)
    print(f"  witness-cell flag: {wvalid}", flush=True)
    print(f"  workers: {nworkers}", flush=True)
    print(f"  wall clock: {t1 - t0:.1f}s", flush=True)
    print("=== DONE ===", flush=True)


if __name__ == "__main__":
    main()
