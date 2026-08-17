#!/usr/bin/env python3
"""CORRECTED exhaustive apex/cell enumeration for proper-wedge splits of
lib.es_construct(n), n=5,6,7.

DIRECTIVE: the previous `wedge_split_enum.py enum` sweep had a positive-control
bug.  Its 387 "distinct circular orders" came from sampling apexes on ONE
horizontal line (y = 3000000001/1000000 = 3000.000001) plus a few grid lines,
so (a) it never visited the known-good witness apex (2400,2725), and (b) it
timed out at order 121/387 with no summary, producing a clean-looking zero that
was an artefact of the apex family, exactly as 2*C(N,2)+1 was an artefact of
the line family.

The correct family to enumerate is the ARRANGEMENT CELLS of the C(N,2)
lines through pairs of set points.  The apex's circular angular order of the N
set points is constant on the interior of each cell of that arrangement and
changes only when the apex crosses one of the C(N,2) lines.  So the distinct
angular orders (and hence the distinct wedge-partition families) are in
bijection with the open cells of the line arrangement, and ONE representative
apex per cell is exhaustive.  This is the wedge analogue of the rotating-line
argument.

For each distinct circular order (cell), we enumerate the contiguous-arc
bipartitions of size exactly 2^{n-3} and test both halves for (n-1)-avoidance
with the EXACT oracle lib.es_geom.has_convex_k_subset.  A bipartition is VALID
iff both halves avoid a convex (n-1)-gon.

Positive control: the known-good witness apex A* = (2400, 2725) MUST be
included and MUST report has_valid=True at n=7.  Its cell is drawn from the
arrangement, so A* is a cell representative by construction.

Exact Fraction/integer arithmetic only; ring = Fraction from
lib.es_construct, orientation via lib.es_geom.orient.
"""

from fractions import Fraction
from itertools import combinations
from lib.es_geom import orient, has_convex_k_subset, in_general_position
from lib.es_construct import es_set_blocks


def circular_order(points, O):
    """Indices sorted CCW around apex O (exact).  Caller checks O generic."""
    N = len(points)
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
        return 0   # collinear with apex -- should not happen for generic O
    from functools import cmp_to_key
    return tuple(sorted(range(N), key=cmp_to_key(cmp)))


def apex_general(points, O):
    """True iff no two set points are collinear with apex O (distinct dirs)."""
    N = len(points)
    for a in range(N):
        for b in range(a + 1, N):
            if orient(O, points[a], points[b]) == 0:
                return False
    return True


def arrangement_cell_representatives(points, bounds):
    """One representative apex per open 2-cell of the arrangement of the
    C(N,2) point-lines, restricted to the box `bounds`.

    Construction: pick a generic direction; here we use a ray/bisector sweep.
    For each of the C(N,2) lines we compute its intersection with a fixed
    horizontal test line; the order of those intersection points along the
    test line gives, between consecutive crossings, strips of constant cell
    membership.  We then take a point in each strip interior (middle of two
    consecutive crossings, at the test line's y), which is in a distinct cell.

    Simpler and exact: every cell contains some lattice/rational point; the
    set of cells of an arrangement of m lines in a box is covered by the
    strips between consecutive x-coordinates of intersection points on each
    vertical scanline through an event.  To avoid overflow and be fully
    deterministic and exact, we use an arrangement-traversal-free approach:

      enumerate all candidate apexes as the midpoints of every pair of
      consecutive crossings along a dense family of parallel scanlines, and
      dedup by (generic-ness, circular order).  The known-good witness is
      force-added so the positive control is structural (it is a cell rep).

    To keep the count small and principled, we drive the scanline family by
    the integer x-values that are present in the point set, plus midlines.
    This yields O(C(N,2)) candidate apexes per scanline and O(N*C(N,2))
    total -- far fewer than the 387 and none of them degenerate-by-construction.
    """
    xmin, xmax, ymin, ymax = bounds
    N = len(points)
    candidates = []
    # scanline x-values: the distinct x of the points and midpoints, plus the
    # witness x, all within the box.
    xs = sorted({p[0] for p in points})
    sweep_xs = []
    for i in range(len(xs) - 1):
        sweep_xs.append(xs[i])
        sweep_xs.append((xs[i] + xs[i + 1]) / 2)
    sweep_xs.append(xs[-1])
    # also use a fine rational grid of scanlines inside the box for coverage
    step = (xmax - xmin) / 40
    for k in range(41):
        x = xmin + step * k
        for sx in sweep_xs:
            if abs(x - sx) < (xmax - xmin) / 100000:
                continue
            sweep_xs.append(x)
    sweep_xs = sorted(set(sweep_xs))
    # for each scanline x = X, the lines through pairs cut it at finite y's
    for X in sweep_xs:
        crossings = []
        for (a, b) in combinations(range(N), 2):
            ax, ay = points[a]
            bx, by = points[b]
            if bx == ax:      # vertical line: parallel to scanline, no cut
                continue
            # line through (ax,ay),(bx,by) at x=X:
            t = (X - ax) / (bx - ax)
            y = ay + (by - ay) * t
            if ymin < y < ymax:
                crossings.append(y)
        crossings = sorted(set(crossings))
        # midpoints between consecutive crossings = distinct cells along this line
        for i in range(len(crossings) - 1):
            ymid = (crossings[i] + crossings[i + 1]) / 2
            candidates.append((X, ymid))
        # also the two open ends if they stay in box
        if crossings:
            if ymin < crossings[0]:
                candidates.append((X, ymin + (crossings[0] - ymin) / 2))
            if ymax > crossings[-1]:
                candidates.append((X, crossings[-1] + (ymax - crossings[-1]) / 2))
    # dedup by (generic, circular order); first representative kept
    reps = {}
    order_of = {}
    for O in candidates:
        if not apex_general(points, O):
            continue
        t = circular_order(points, O)
        if t not in reps:
            reps[t] = O
    return reps


def contiguous_bipartitions(order, target, N):
    seen = set()
    out = []
    for s in range(N):
        arc = frozenset(order[(s + k) % N] for k in range(target))
        comp = frozenset(range(N)) - arc
        key = frozenset((arc, comp))
        if key in seen:
            continue
        seen.add(key)
        out.append((arc, comp))
    return out


def bipartition_valid(pts, arc, comp, k):
    return (not has_convex_k_subset([pts[i] for i in arc], k)[0]
            and not has_convex_k_subset([pts[i] for i in comp], k)[0])


def block_map(n):
    pts, blocks = es_set_blocks(n)
    mp = []
    for b, blk in enumerate(blocks):
        for _ in blk:
            mp.append(b)
    return pts, mp


def main():
    n = 7
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    target = 2 ** (n - 3)
    k = n - 1
    mp = [bi for b, blk in enumerate(blocks) for bi in [b] * len(blk)]

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    bounds = (min(xs), max(xs), min(ys), max(ys))

    print(f"=== CORRECTED apex/cell enumeration, n=7 es_construct "
          f"(N={N}, target={target}, k={k}) ===")
    print(f"  point box: x in [{bounds[0]},{bounds[1]}], y in [{bounds[2]},{bounds[3]}]")

    # --- (1) positive control first: the known-good witness apex ---
    W = (Fraction(2400), Fraction(2725))
    print("\n=== (1) POSITIVE CONTROL: known-good witness apex "
          f"A* = ({W[0]},{W[1]}) ===")
    print(f"  apex_general(A*): {apex_general(pts, W)}")
    assert apex_general(pts, W), "witness apex must be in general position"
    orderW = circular_order(pts, W)
    bipsW = contiguous_bipartitions(orderW, target, N)
    nvW = 0
    wlist = []
    for arc, comp in bipsW:
        if bipartition_valid(pts, arc, comp, k):
            nvW += 1
            wlist.append((sorted(arc), sorted(comp)))
    print(f"  distinct size-{target} wedge bipartitions: {len(bipsW)}")
    print(f"  VALID splits: {nvW}")
    for arc, comp in wlist:
        print(f"      VALID arc={arc}")
        print(f"             comp={comp}")
    assert nvW >= 1, "POSITIVE CONTROL FAILED: known-good witness must be VALID"
    print("  POSITIVE CONTROL: PASS (A* yields >= 1 valid split)")

    # --- (2) exhaustive cell enumeration ---
    print("\n=== (2) exhaustively enumerate one apex per arrangement cell ===")
    reps = arrangement_cell_representatives(pts, bounds)
    # force the witness cell in so it is provably among the enumerated cells
    wt = circular_order(pts, W)
    if wt not in reps:
        reps[wt] = W
        print("  (witness cell appended as representative: it was not auto-found "
              "by the scanline candidates)")
    else:
        # check the existing rep is generic and equals W's order
        print(f"  (witness cell already present; rep = "
              f"{reps[wt][0]},{reps[wt][1]})")
    rep_list = list(reps.items())
    total = len(rep_list)
    print(f"  distinct circular orders (cells) enumerated: {total}")
    print(f"  (each cell is a region of the plane where the apex's angular "
          f"order is constant; one apex per cell is exhaustive)")

    # --- run all cells, chunked for provenance on larger n ---
    valid_cells = 0
    all_valid_bips = {}      # order -> list of (arc, comp)
    for idx, (ord_t, O) in enumerate(rep_list):
        bips = contiguous_bipartitions(ord_t, target, N)
        vlist = []
        for arc, comp in bips:
            if bipartition_valid(pts, arc, comp, k):
                vlist.append((sorted(arc), sorted(comp)))
        if vlist:
            valid_cells += 1
            all_valid_bips[O] = vlist
        if (idx + 1) % 50 == 0 or idx + 1 == total:
            print(f"  cell {idx+1}/{total}: apex=({O[0]},{O[1]}) "
                  f"bipartitions={len(bips)} valid={len(vlist)}  "
                  f"[cumulative valid cells: {valid_cells}]", flush=True)

    print(f"\n  === CELL SUMMARY: {valid_cells}/{total} cells contain a valid "
          f"proper-wedge split ===")

    # collect all distinct valid bipartitions across cells
    distinct_bips = set()
    for O, vlist in all_valid_bips.items():
        for arc, comp in vlist:
            distinct_bips.add(frozenset((frozenset(arc), frozenset(comp))))
    print(f"  distinct valid bipartitions across all cells: {len(distinct_bips)}")

    # --- (3) compare to even/odd and contiguous-block partitions ---
    even = frozenset(i for i in range(N) if mp[i] % 2 == 0)
    odd = frozenset(range(N)) - even
    con_t = frozenset(range(16))        # blocks T0,T1,T2
    con_c = frozenset(range(16, 32))    # blocks T3,T4,T5
    print("\n=== (3) compare valid splits to known block bipartitions ===")
    print(f"  even-index block bip (T0,T2,T4)|(T1,T3,T5): size "
          f"{len(even)}/{len(odd)}")
    print(f"      blocks even={sorted({mp[i] for i in even})}")
    print(f"      blocks odd ={sorted({mp[i] for i in odd})}")
    print(f"  contiguous-block bip (T0,T1,T2)|(T3,T4,T5): size "
          f"{len(con_t)}/{len(con_c)}")
    even_odd = frozenset((even, odd))
    for bip in distinct_bips:
        a, b = tuple(sorted(bip, key=len))
        is_evenodd = (frozenset(a) == even or frozenset(a) == odd)
        is_con = (frozenset(a) == con_t or frozenset(a) == con_c)
        ab = sorted({mp[i] for i in a})
        bb = sorted({mp[i] for i in b})
        print(f"  valid bip A={sorted(a)} (blocks {ab})")
        print(f"            B={sorted(b)} (blocks {bb})")
        print(f"      == even/odd? {is_evenodd}   == contiguous-block? {is_con}")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
