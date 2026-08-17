#!/usr/bin/env python3
"""Adjudicate the allowable-sequence approach on the verified es_construct set.

Adjudication targets (from the steering directive / approach file):
  1. Reconstruct the exact Goodman-Pollack circular (allowable) sequence of an
     exact point set by sweeping a directed line and recording the ordered
     projection permutation at every swap.  All arithmetic exact (Fractions);
     swap directions compared by exact cross product, never floating point.
  2. Define the "reversal depth" of each point as the number of other points it
     crosses, i.e. its reversal count over one half-period (the number of
     circular-sequence events [0, pi) in which that point participates).  Test
     whether this depth equals the block index T_i on es_construct(n) for
     n = 4,5,6,7.
  3. Test the staircase/contiguous-block convexity characterization for subsets
     of size >= 4 against the exact oracle es_geom.in_convex_position:
        S is in convex position  <=>  there is a projection order (over the
        sweep) in which the elements of S occupy one contiguous block.
     (Reported literally, with exact agreed / disagreed counts.)

The two load-bearing claims of the approach are (2) and (3); each gets an
explicit PASS / FAIL with exact numbers.  Items (1) and the axiom check are
reported for pedigree only.

Exactness: every coordinate, slope comparison, and orientation is an exact
Fraction/int computation.  No floats anywhere in the geometry.
"""
from fractions import Fraction
from itertools import combinations
from functools import cmp_to_key

from lib.es_construct import es_set_blocks          # verified 2^{n-2} no-convex-n-gon set
from lib.es_geom import in_convex_position          # independent exact oracle


# ---------------------------------------------------------------------------
# 1. Exact circular (allowable) sequence construction
# ---------------------------------------------------------------------------
def critical_direction(a, b):
    """Direction u (unit-in-[0,pi)) of the sweep normal where projections of
    a,b onto u tie.  u is perpendicular to (b-a): u = (dy,-dx), put into the
    upper half-plane (vy>0, or vy==0 with vx>0).  Returns exact (vx,vy)."""
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    vx, vy = dy, -dx
    if vy < 0 or (vy == 0 and vx < 0):
        vx, vy = -vx, -vy
    return (vx, vy)


def dir_cmp(p, q):
    """Compare two upper-half-plane directions by angle in [0,pi) via exact
    cross product.  p before q (smaller angle) iff p x q > 0."""
    cross = p[0] * q[1] - p[1] * q[0]
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0


def build_sequence(points):
    """Reconstruct the circular sequence of an exact point set.

    Returns (events, initial_perm, permlist, counts):
      events      : sorted list of (direction, (ia, ib)) over [0, pi), each
                    unordered pair exactly once.
      initial_perm: projection order at angle 0+ (by increasing x).
      permlist    : [initial, after event-group 1, after event-group 2, ...]
                    i.e. the ordered projection permutation at every stage.
      counts      : dict point -> number of events it participates in over
                    the half-period (its reversal count / depth).
    All x are required distinct (no angle-0 event); verified and asserted.
    """
    n = len(points)
    events = []
    for (ia, a), (ib, b) in combinations(enumerate(points), 2):
        events.append((critical_direction(a, b), (ia, ib)))
    events.sort(key=cmp_to_key(lambda e1, e2: dir_cmp(e1[0], e2[0])))

    init = sorted(range(n), key=lambda i: points[i][0])
    xs = [points[i][0] for i in range(n)]
    assert len(set(xs)) == n, "angle-0 tie: duplicate x present"

    # groups of events at the same critical angle (parallel segments)
    groups = []
    cur = [events[0]]
    for e in events[1:]:
        if dir_cmp(e[0], cur[0][0]) == 0:
            cur.append(e)
        else:
            groups.append(cur)
            cur = [e]
    groups.append(cur)

    counts = {p: 0 for p in range(n)}
    permlist = [list(init)]
    p = list(init)
    pos = {idx: i for i, idx in enumerate(p)}

    def _replay_group(pairlist):
        """Apply a group of simultaneous swaps (disjoint adjacent pairs at one
        critical angle).  In general position each event is one adjacent
        length-2 block (parallel segments sharing an endpoint would imply
        collinearity), so the group is applied as independent pairwise swaps.
        Reversing merged runs of positions would be wrong: two disjoint
        parallel pairs side by side swap to [B,A,D,C], not [D,C,B,A]."""
        nonlocal p, pos
        for (a, b) in pairlist:
            i, j = pos[a], pos[b]
            assert abs(i - j) == 1, "non-adjacent pair in group"
            p[i], p[j] = p[j], p[i]
            pos[a], pos[b] = j, i

    for g in groups:
        for (d, (ia, ib)) in g:
            counts[ia] += 1
            counts[ib] += 1
        _replay_group([e[1] for e in g])
        permlist.append(list(p))

    return events, init, permlist, counts


# ---------------------------------------------------------------------------
# 2. Convexity from the sequence: projection permutations
# ---------------------------------------------------------------------------
def contiguous_convex(S, permlist):
    """Literal contiguous-block criterion: S is 'contiguous' if in some
    permutation of permlist the positions of the elements of S form a single
    consecutive run (among all N points)."""
    Sset = set(S)
    for perm in permlist:
        posn = [i for i, x in enumerate(perm) if x in Sset]
        if posn == list(range(posn[0], posn[0] + len(S))):
            return True
    return False


def restricted_permutations(S, events):
    """Projection-order permutations of S alone, restricted to events whose
    two endpoints are both in S.  events: list of (direction, (a,b)) already
    sorted by angle over the half-period (exactly what build_sequence yields)."""
    Sset = set(S)
    evS = [(d, (a, b)) for d, (a, b) in events if a in Sset and b in Sset]
    init = sorted(S, key=lambda i: xdict_global[i])
    perms = [list(init)]
    p = list(init)
    posS = {idx: k for k, idx in enumerate(p)}
    # group events in evS by angle
    groups = []
    if evS:
        cur = [evS[0]]
        for e in evS[1:]:
            if dir_cmp(e[0], cur[0][0]) == 0:
                cur.append(e)
            else:
                groups.append(cur)
                cur = [e]
        groups.append(cur)
    for g in groups:
        pairlist = [e[1] for e in g]
        for (a, b) in pairlist:
            i, j = posS[a], posS[b]
            assert abs(i - j) == 1, "non-adjacent restricted pair in group"
            p[i], p[j] = p[j], p[i]
            posS[a], posS[b] = j, i
        perms.append(list(p))
    return perms


def extreme_in_projection_convex(S, events):
    """True convexity-from-sequence criterion: S is in convex position iff
    every p in S is a vertex of conv(S), i.e. p appears as the FIRST element
    or the LAST element of the S-restricted projection order for some sweep
    direction (min- or max-extreme along some normal).  This is a proven
    characterization; reported as a positive anchor only."""
    permsS = restricted_permutations(S, events)
    firsts = set()
    lasts = set()
    # permsS[0] is the projection order at angle 0+ (by x): a legitimate
    # sweep direction, so its min-x and max-x points are extreme too.
    for perm in permsS:
        firsts.add(perm[0])
        lasts.add(perm[-1])
    return all(p in firsts or p in lasts for p in S)


# ---------------------------------------------------------------------------
# 3. Main
# ---------------------------------------------------------------------------
def block_of_each(points, blocks):
    """global index -> block index, by exact coordinate identity."""
    coord_to_gi = {p: i for i, p in enumerate(points)}
    bof = {}
    for bi, blk in enumerate(blocks):
        for p in blk:
            bof[coord_to_gi[p]] = bi
    return bof


def main():
    lines = []
    def pr(*a):
        lines.append(" ".join(str(x) for x in a))

    pr("=" * 74)
    pr("allseq_adjudicate.py — adjudicate the allowable-sequence approach")
    pr("on the verified es_construct ES construction.  All arithmetic exact.")
    pr("=" * 74)

    # ---- sequence axiom check (pedigree of the reconstruction) ----------
    pr("\n[TEST 1] CIRCULAR-SEQUENCE AXIOMS (Goodman-Pollack)")
    pr("  every unordered pair reversed exactly once over [0,pi); every event")
    pr("  is a single adjacent swap (general position => no tied angles).")
    for n in (4, 5, 6, 7):
        points, blocks = es_set_blocks(n)
        N = len(points)
        events, init, permlist, counts = build_sequence(points)
        pairs = len(events)
        # adjacent-swap check along the actual replay
        p = list(init)
        pos = {idx: i for i, idx in enumerate(p)}
        adj = 0
        groups = []
        cur = [events[0]]
        for e in events[1:]:
            if dir_cmp(e[0], cur[0][0]) == 0:
                cur.append(e)
            else:
                groups.append(cur)
                cur = [e]
        groups.append(cur)
        for g in groups:
            for (d, (a, b)) in g:
                if abs(pos[a] - pos[b]) == 1:
                    adj += 1
                i, j = pos[a], pos[b]
                p[i], p[j] = p[j], p[i]
                pos[a], pos[b] = j, i
        ok = (pairs == N * (N - 1) // 2 and adj == pairs)
        pr(f"  n={n} N={N}: pairs={pairs}/{N*(N-1)//2}  single-adjacent-swaps="
          f"{adj}/{pairs}  -> {'PASS' if ok else 'FAIL'}")

    # ---- (2) reversal depth vs block index ------------------------------
    pr("\n[TEST 2] REVERSAL DEPTH = block index T_i ?")
    pr("  depth(p) := number of circular-sequence events [0,pi) involving p,")
    pr("  i.e. the number of other points it crosses over one half-period.")
    depth_fails = {}
    for n in (4, 5, 6, 7):
        points, blocks = es_set_blocks(n)
        N = len(points)
        expected_sizes = {i: len(b) for i, b in enumerate(blocks)}
        events, init, permlist, counts = build_sequence(points)
        depths = counts
        # sanity: each pair crossed exactly once (half-period axiom)
        total_pairs = len(events)
        # every point crosses exactly N-1 others
        const_ok = all(depths[p] == N - 1 for p in range(N))
        # depth == block index test
        bof = block_of_each(points, blocks)
        match = all(depths[p] == bof[p] for p in range(N))
        depth_fails[n] = not match
        distinct_depths = sorted(set(depths.values()))
        distinct_blocks = sorted(set(bof.values()))
        sizes = {}
        for v in distinct_depths:
            sizes[v] = sum(1 for p in range(N) if depths[p] == v)
        pr(f"  n={n}  N={N}: pairs={total_pairs} (={N*(N-1)//2} OK)"
          f"  depth-per-point all equal N-1={N-1}: {const_ok}")
        pr(f"      depth value multiset: {sizes}")
        pr(f"      block sizes T_i: {expected_sizes}")
        pr(f"      depth == block index: {'PASS' if match else 'FAIL'}")
    pr("  => depth is a CONSTANT N-1 for every point (every unordered pair is")
    pr("     reversed exactly once per half-period), while block sizes are the")
    pr("     binomial coefficients C(n-2,i); they cannot coincide for n>=4")
    pr("     where block sizes differ.  VERDICT: refuted.")

    # ---- (3) contiguous-block convexity vs oracle -----------------------
    pr("\n[TEST 3] STAIRCASE / CONTIGUOUS-BLOCK convexity characterization")
    pr("  claim: S (|S|>=4) is in convex position  <=>  some projection order")
    pr("         in the sweep has the elements of S as ONE CONTIGUOUS BLOCK.")
    pr("  compared against exact oracle es_geom.in_convex_position.")
    for n in (4, 5, 6):
        points, blocks = es_set_blocks(n)
        N = len(points)
        events, init, permlist, counts = build_sequence(points)
        agree = disagree = 0
        first_disagree = None
        # also track false-positive (predicted convex, oracle says not) kind
        from collections import Counter
        kinds = Counter()
        for r in range(4, N + 1):
            for comb in combinations(range(N), r):
                S = list(comb)
                pred = contiguous_convex(S, permlist)
                orc = in_convex_position([points[i] for i in S])
                if pred == orc:
                    agree += 1
                else:
                    disagree += 1
                    kinds[(pred, orc)] += 1
                    if first_disagree is None:
                        first_disagree = (S, pred, orc)
        verdict = "PASS" if disagree == 0 else "FAIL"
        pr(f"  n={n}: |S|>=4 subsets: agree={agree}  disagree={disagree}  "
          f"-> {verdict}")
        pr(f"      disagreement kinds (pred,oracle): {dict(kinds)}")
        if first_disagree:
            pr(f"      first disagreement: S={first_disagree[0]} pred="
              f"{first_disagree[1]} oracle={first_disagree[2]}")
    pr("  Notes on the (pred,oracle) kind map: (True,False)=predicted convex")
    pr("  but not (a false positive, e.g. any full set is trivially one")
    pr("  contiguous block even when not convex); (False,True)=predicted not")
    pr("  convex but actually convex (e.g. a 4-set whose four points are not")
    pr("  separable from an interior point in any projection).  The correct")
    pr("  convexity characterization is instead: every p in S is a vertex of")
    pr("  conv(S), i.e. p is the unique extreme of its own projection within S")
    pr("  for some direction.")

    # ---- (3b) positive anchor: the proven extreme-in-projection criterion --
    pr("\n[TEST 3b] ANCHOR — proven characterization: S convex  <=>  every p in")
    pr("  S is first OR last in some S-restricted projection order (i.e. p is")
    pr("  a vertex of conv(S): min- or max-extreme along some sweep normal).")
    pr("  Against oracle (n=5,6).")
    global xdict_global
    for n in (5, 6):
        points, blocks = es_set_blocks(n)
        N = len(points)
        xdict_global = {i: points[i][0] for i in range(N)}
        events, init, permlist, counts = build_sequence(points)
        a_agree = a_dis = 0
        a_dis_details = []
        for r in range(4, N + 1):
            for comb in combinations(range(N), r):
                S = list(comb)
                pred = extreme_in_projection_convex(S, events)
                orc = in_convex_position([points[i] for i in S])
                if pred == orc:
                    a_agree += 1
                else:
                    a_dis += 1
                    if n == 6 and len(a_dis_details) < 8:
                        a_dis_details.append((S, pred, orc))
        pr(f"  n={n}: |S|>=4 agree={a_agree} disagree={a_dis} -> "
          f"{'PASS' if a_dis == 0 else 'FAIL'}")
        for det in a_dis_details:
            pr(f"      detail: S={det[0]} pred={det[1]} oracle={det[2]}")

    res = "\n".join(lines)
    print(res)
    with open("/workspace/code/out/allseq_adjudicate.captured.txt", "w") as f:
        f.write(res + "\n")
    print("\n[written code/out/allseq_adjudicate.captured.txt]")


if __name__ == "__main__":
    main()
