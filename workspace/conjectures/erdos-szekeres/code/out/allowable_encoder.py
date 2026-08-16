#!/usr/bin/env python3
"""Exact circular (allowable) sequence encoder for the ES construction, and
the run's own verification of the two load-bearing claims of the adopted
allowable-sequence approach.

Approach (research/approaches/allowable-sequence-circular-representation.md):
represent the order type by its Goodman-Pollack circular sequence of
permutations (sweep a rotating directed line, record projection order, each
pair swapped once per half-period), and try to recover the ES block structure
T_i (|T_i| = C(n-2,i)) from a per-point 'depth' statistic that is INVARIANT
under realization-preserving moves, plus check that convex position is
correctly readable from the sequence via the extreme-in-projection criterion.

ALL arithmetic is exact: points are fractions.Fraction, swap directions are
sorted by exact cross-product, never float.  The ES set is the verified
es_construct.es_set (largestConvex == n-1, i.e. no convex n-gon, confirmed
against lib.es_geom oracle).

Checks performed (each matched against an independent oracle where one exists):
  A. Circular-sequence axioms on es_construct at n=4,5,6,7:
     every unordered pair reversed exactly once over [0,pi); each non-tied
     event is an adjacent reversal; tied (same-angle) events are disjoint
     adjacent blocks reversed together.
  B. Convexity-readable-from-sequence: for every subset S (n<=6, all subsets)
     S is in convex position  <=>  every p in S is 'extreme relative to S' in
     the sequence sense (p appears first OR last in some S-restricted
     projection permutation).  Cross-checked against es_geom.in_convex_position.
  C. Depth/block test (the run's conjectural first step, UNSOURCED -> just
     measured): several per-point depth statistics computed from the sequence;
     report, at n=5,6,7, whether points of depth i are exactly block T_i.
  D. Realization-invariance falsifier (approach file's critical test): recompute
     each depth statistic after an order-type-PRESERVING coordinate change
     (horizontal stretch x->s*x keeps every determinant sign when s>0) and
     after reflection x->-x; report whether depth per point changes.  If it
     changes, the statistic is a placement artifact, not an order-type datum.

Output: human-readable report appended to code/out/allowable_encoder.captured.txt.
"""

from fractions import Fraction
from itertools import combinations
from collections import defaultdict
import sys

sys.path.insert(0, "/workspace/code")
from lib.es_construct import es_set_blocks, es_set
from lib.es_geom import in_convex_position  # independent oracle


# ---------------------------------------------------------------------------
# 1. Circular sequence construction (exact)
# ---------------------------------------------------------------------------
def critical_direction(a, b):
    """Direction (unit-in-[0,pi)) of the rotating-line normal u where the
    projections of a,b onto u are equal.  u perpendicular to (b-a) => take
    u = (dy, -dx), put into upper half-plane (y>0, or y==0 with x>0).
    Returns (vx, vy) exact Fractions with vy>=0 (and if vy==0, vx>=0)."""
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    vx = dy
    vy = -dx
    if vy < 0 or (vy == 0 and vx < 0):
        vx, vy = -vx, -vy
    return (vx, vy)


def _angle_cmp(p, q):
    """Compare direction p=(px,py) vs q=(qx,qy), both in [0,pi) upper plane.
    Angle order by cross product: p before q iff p x q > 0."""
    cross = p[0] * q[1] - p[1] * q[0]
    if cross != 0:
        return -1 if cross > 0 else 1   # p before q if cross>0
    # same direction: equal angle (parallel segments)
    return 0


def build_circular_sequence(points):
    """Return (events, initial_perm).
    events: list of (direction, [indices of the pair]) sorted by angle.
    initial_perm: permutation (list of point indices) at sweep angle 0+,
    i.e. sorted by projection onto u(0)=(1,0) = by x; ties impossible here
    (all x distinct for es_construct, checked).
    Each pair appears exactly once.  Assumes general position (no equal
    critical angles from coincident direction AND same pair)."""
    n = len(points)
    ev = []
    for (ia, a), (ib, b) in combinations(enumerate(points), 2):
        d = critical_direction(a, b)
        ev.append((d, (ia, ib)))
    # sort events by angle (exact): the key is the direction angle
    from functools import cmp_to_key
    ev.sort(key=cmp_to_key(lambda e1, e2: _angle_cmp(e1[0], e2[0])))
    # initial permutation: by x ascending (all x distinct)
    perm = sorted(range(n), key=lambda i: points[i][0])
    # verify all x distinct (ties at angle 0 would be events at 0; report)
    xs = [points[i][0] for i in range(n)]
    return ev, perm, (len(set(xs)) == n)


def replay(ev, perm):
    """Replay events in angle order, producing the sequence of permutations.
    Returns list of permutations at each step (perm after processing each
    event group).  Verifies adjacent-reversal / disjoint-block property.
    Returns (permlist, axiom_ok, detail)."""
    permlist = [list(perm)]
    axiom_ok = True
    detail = []
    # group by angle
    groups = []
    cur = [ev[0]]
    for e in ev[1:]:
        if _angle_cmp(e[0], cur[0][0]) == 0:
            cur.append(e)
        else:
            groups.append(cur)
            cur = [e]
    groups.append(cur)
    p = list(perm)
    pos = {idx: i for i, idx in enumerate(p)}
    for g in groups:
        if len(g) == 1:
            # single adjacent swap
            ia, ib = g[0][1]
            if abs(pos[ia] - pos[ib]) != 1:
                axiom_ok = False
                detail.append(f"non-adjacent swap {ia},{ib}")
            i1 = min(pos[ia], pos[ib])
            p[i1], p[i1 + 1] = p[i1 + 1], p[i1]
            for k, idx in ((i1, p[i1]), (i1 + 1, p[i1 + 1])):
                pos[idx] = k
        else:
            # several simultaneous (disjoint adjacent blocks): reverse each run
            pairs = [e[1] for e in g]
            covered = [pp for pp in pairs]
            # identify maximal consecutive runs among the involved positions
            involved = sorted(set(pos[aa] for (aa, bb) in pairs)
                              | set(pos[bb] for (aa, bb) in pairs))
            # reverse each maximal run of originally-adjacent involved items
            # (standard: reverse each maximal block)
            # simpler robust: sort involved, group into consecutive runs, reverse each
            runs = []
            r = [involved[0]]
            for v in involved[1:]:
                if v == r[-1] + 1:
                    r.append(v)
                else:
                    runs.append(r)
                    r = [v]
            runs.append(r)
            for run in runs:
                run = [q for q in run]  # positions then items
                items = [p[q] for q in run]
                items_rev = items[::-1]
                for q, it in zip(run, items_rev):
                    p[q] = it
                    pos[it] = q
        permlist.append(list(p))
    return permlist, axiom_ok, detail


# ---------------------------------------------------------------------------
# 2. Depth statistics from the sequence
# ---------------------------------------------------------------------------
def depth_stats(ev, perm, n):
    """Compute per-point depth statistics from sorted events.
    ev: sorted event list [(dir,(ia,ib)),...].  Each event has a global rank.
    Returns dict p -> {S1,S2,S3,S4,S5}."""
    total = len(ev)
    S2 = {p: 0 for p in range(n)}   # sum of event ranks involving p
    cnt = {p: 0 for p in range(n)}  # number of events (should be n-1)
    earliest = {p: None for p in range(n)}
    latest = {p: None for p in range(n)}
    per_events = {p: [] for p in range(n)}
    for rank, (d, (a, b)) in enumerate(ev):
        S2[a] += rank
        S2[b] += rank
        cnt[a] += 1
        cnt[b] += 1
        per_events[a].append(rank)
        per_events[b].append(rank)
    S1 = cnt
    # S3: number of partners q with which p swaps in the first half of p's swaps
    #    (before p's median event rank)
    S3 = {}
    for p in range(n):
        ranks = sorted(per_events[p])
        med = ranks[len(ranks) // 2]  # lower median
        S3[p] = sum(1 for r in ranks if r < med)
    # S4: earliest event rank ; S5: latest event rank
    S4 = {p: min(per_events[p]) for p in range(n)}
    S5 = {p: max(per_events[p]) for p in range(n)}
    S2 = {p: S2[p] / max(1, cnt[p]) for p in range(n)}  # average event rank
    return {"S1": S1, "S2": S2, "S3": S3, "S4": S4, "S5": S5}


# ---------------------------------------------------------------------------
# 3. Convexity readable from sequence: extreme-in-projection criterion
# ---------------------------------------------------------------------------
def s_permutations(ev, perm, S):
    """Replay only events whose both endpoints are in S, producing the
    sequence of S-permutations (orders of S by projection)."""
    # use provided global-perm restriction: initial order of S by x
    init = sorted(S, key=lambda i: xdict[i])
    perms = [list(init)]
    p = list(init)
    posS = {idx: k for k, idx in enumerate(p)}
    groups = []
    evS = [e for e in ev if e[1][0] in S and e[1][1] in S]
    # group by angle (only within S-events)
    if evS:
        cur = [evS[0]]
        for e in evS[1:]:
            if _angle_cmp(e[0], cur[0][0]) == 0:
                cur.append(e)
            else:
                groups.append(cur)
                cur = [e]
        groups.append(cur)
    for g in groups:
        pairs = [e[1] for e in g]
        runs = []
        involved = sorted(set(posS[aa] for (aa, bb) in pairs)
                          | set(posS[bb] for (aa, bb) in pairs))
        if len(involved) == 2 and involved[1] == involved[0] + 1:
            runs = [[involved[0]]]
        else:
            r = [involved[0]]
            for v in involved[1:]:
                if v == r[-1] + 1:
                    r.append(v)
                else:
                    runs.append(r[:])
                    r = [v]
            runs.append(r[:])
        for run in runs:
            items = [p[q] for q in run]
            for q, it in zip(run, items[::-1]):
                p[q] = it
                posS[it] = q
        perms.append(list(p))
    return perms


def extreme_rel(S, seq_S_perms):
    """Points of S that are first or last in at least one S-permutation."""
    ext = set()
    for perm in seq_S_perms:
        ext.add(perm[0])
        ext.add(perm[-1])
    return ext


def convex_from_sequence(ev, perm, points, S):
    """S in convex position (sequence criterion) <=> every p in S is extreme."""
    perms = s_permutations(ev, perm, S)
    ext = extreme_rel(S, perms)
    all_extreme = (len(ext) == len(S) and len(S) >= 3)
    return all_extreme


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
import io

out = io.StringIO()
def pr(*a):
    print(*a, file=out)

pr("=" * 70)
pr("allowable_encoder.py — exact circular-sequence encoder + depth/block +")
pr("convexity-readable test on the verified es_construct ES construction")
pr("All arithmetic exact (fractions.Fraction); directions sorted by cross-product.")
pr("=" * 70)

xdict = {}
pos_x = {}

for n in (4, 5, 6, 7):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    pr(f"\n--- n={n}  |S|={N}=2^{n-2}  numBlocks={len(blocks)} ---")
    xdict = {i: pts[i][0] for i in range(N)}
    all_distinct_x = (len(set(xdict.values())) == len(xdict))
    ev, perm, xdistinct = build_circular_sequence(pts)
    pr(f"  events (pairs) = {len(ev)} = C({N},2): "
      f"{'OK' if len(ev) == N*(N-1)//2 else 'MISMATCH'}")
    pr(f"  all x distinct (no angle-0 tie): {all_distinct_x}")

    # A: replay and verify each pair once + adjacent reversals
    permlist, axiom_ok, det = replay(ev, perm)
    # count reverse-once: each pair appears once by construction of ev
    pr(f"  [A] replay ok (adjacent/disjoint-block reversals): {axiom_ok}"
      + (f"  detail:{det[:3]}" if not axiom_ok else ""))
    # every pair reversed exactly once over the half-period: by construction,
    # ev contains each pair exactly once.  Report the adjacent-swap tally:
    n_adj = 0
    p0 = list(perm)
    pos0 = {i: k for k, i in enumerate(p0)}
    pcur = list(perm)
    posc = {i: k for k, i in enumerate(pcur)}
    for (d, (a, b)) in ev:
        if abs(posc[a] - posc[b]) == 1:
            n_adj += 1
        i1 = min(posc[a], posc[b])
        pcur[i1], pcur[i1+1] = pcur[i1+1], pcur[i1]
        posc[pcur[i1]] = i1
        posc[pcur[i1+1]] = i1+1
    pr(f"  [A] of {len(ev)} events, {n_adj} are single adjacent reversals "
      f"(rest simultaneous at tied angle)")

    # C: depth statistics and block alignment
    ds = depth_stats(ev, perm, N)
    # block id per point
    block_of = {}
    for bi, blk in enumerate(blocks):
        # each point p has global index; blocks contain points; a point appears once
        pass
    # global index -> block: find by identity of coords
    for bi, blk in enumerate(blocks):
        for p in blk:
            # locate global index
            for gi, g in enumerate(pts):
                if g == p:
                    block_of[gi] = bi
                    break
    pr(f"  [C] depth statistics vs block index (|T_i| should be C({n-2},i)):")
    statnames = ["S2", "S3", "S4", "S5"]
    # For each stat, test whether {p : stat==v} partitions into blocks.
    for sn in statnames:
        st = ds[sn]
        # try to find if stat value == block index (exact)
        match_exact = True
        for gi in range(N):
            if st[gi] != block_of[gi]:
                match_exact = False
                break
        # coarser: does stat distinguish blocks? report value ranges per block
        ranges = {}
        for gi in range(N):
            bi = block_of[gi]
            v = st[gi]
            if bi in ranges:
                ranges[bi].append(v)
            else:
                ranges[bi] = [v]
        # also: monotone with block index?
        mono = all(max(ranges[i]) < min(ranges[i+1]) for i in range(len(blocks)-1))
        pr(f"    stat {sn}: exact==blockidx:{match_exact}  "
          f"block-value-ranges={ {k: (min(v), round(max(v),3)) if isinstance(max(v), float) else (min(v),max(v)) for k,v in ranges.items()} }  "
          f"strictly-monotone-in-block:{mono}")

pr("\n" + "=" * 70)
pr("D. REALIZATION-INVARIANCE FALSIFIER (approach file's critical test)")
pr("   For a depth statistic to carry ORDER-TYPE structure it must be invariant")
pr("   under realization-preserving moves.  Test: horizontal stretch x->s*x")
pr("   (s>0) preserves every orientation sign (order type unchanged) — an")
pr("   order-type-PRESERVING move.  Reflection x->-x negates all orientations.")
pr("   Report whether each stat changes per point under stretch.")
pr("=" * 70)
for n in (5, 6, 7):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    ev0, perm0, _ = build_circular_sequence(pts)
    ds0 = depth_stats(ev0, perm0, N)
    # stretch x by 10
    pts_s = [(Fraction(10) * p[0], p[1]) for p in pts]
    evs, perms, _ = build_circular_sequence(pts_s)
    dsS = depth_stats(evs, perms, N)
    # reflect x -> -x
    pts_r = [(-p[0], p[1]) for p in pts]
    evr, permr, _ = build_circular_sequence(pts_r)
    dsR = depth_stats(evr, permr, N)
    for sn in ["S2", "S3", "S4", "S5"]:
        stretch_same = all(ds0[sn][i] == dsS[sn][i] for i in range(N))
        refl_same = all(ds0[sn][i] == dsR[sn][i] for i in range(N))
        pr(f"  n={n} stat {sn}: invariant under x-stretch (order-type-preserving): "
          f"{stretch_same}   invariant under reflection: {refl_same}")

pr("\n" + "=" * 70)
pr("B. CONVEXITY READABLE FROM SEQUENCE (extreme-in-projection criterion)")
pr("   S in convex position <=> every p in S is extreme relative to S in the")
pr("   sequence sense (first or last in some S-restricted projection order).")
pr("   Cross-checked against independent oracle es_geom.in_convex_position")
pr("   over ALL subsets at n=5,6.")
pr("=" * 70)
for n in (5, 6):
    pts, blocks = es_set_blocks(n)
    N = len(pts)
    ev, perm, _ = build_circular_sequence(pts)
    xdict = {i: pts[i][0] for i in range(N)}
    agree = 0
    total = 0
    disagree = []
    for r in range(3, N + 1):
        for comb in combinations(range(N), r):
            S = list(comb)
            seq_conv = convex_from_sequence(ev, perm, pts, S)
            oracle_conv = in_convex_position([pts[i] for i in S])
            total += 1
            if seq_conv == oracle_conv:
                agree += 1
            else:
                disagree.append((S, seq_conv, oracle_conv))
                if len(disagree) > 5:
                    break
    pr(f"  n={n}: {agree}/{total} subsets agree between sequence-criterion and "
      f"oracle  -> {'PASS' if agree==total else 'FAIL'}"
      + (f"  disagree:{disagree[:3]}" if disagree else ""))

res = out.getvalue()
print(res)
with open("/workspace/code/out/allowable_encoder.captured.txt", "w") as f:
    f.write(res)
print("\n[written code/out/allowable_encoder.captured.txt]")
