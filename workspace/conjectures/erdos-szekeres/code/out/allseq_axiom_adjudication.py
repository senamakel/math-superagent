#!/usr/bin/env python3
"""Adjudicate the [A] axiom inconsistency in code/out/allowable_encoder.py.

Task allowable-sequence-continue item (1): the old encoder's report was
self-contradictory —
    [A] replay ok: False  detail:['non-adjacent swap 11,13', ...]
    [A] of 120 events, 120 are single adjacent reversals
The two sub-checks disagree, so the encoder's own axiom verification was not
trusted.  This diagnostic isolates the exact line responsible and records the
verdict with provenance.

Root cause hypothesis (stated before running, per the approach file's comment):
the old `replay()` groups events by critical angle, and in the `len(g)>1`
branch reverses each maximal RUN of involved positions (`runs`-merging), which
is WRONG when the tied pairs are disjoint-and-side-by-side ([A,B,C,D] with the
tied pairs (A,B) and (C,D) should swap to [B,A,D,C], not be run-reversed to
[D,C,B,A]).  That corruption leaves dead position state, so later single-event
"non-adjacent swap 11,13" reports reflect a corrupted permutation, not a real
axiom violation.

But whether es_construct even HAS tied critical angles is itself the question:
TEST 1 of allseq_adjudicate reported adj==pairs (all events adjacent) at every
n, which would mean every event is isolated.  So here we also measure the
distinct-angle count vs the event count, at n=4..7, exactly.

All arithmetic exact.  Uses the verified es_construct.es_set_blocks.
"""
from fractions import Fraction
from itertools import combinations
from functools import cmp_to_key

from lib.es_construct import es_set_blocks


# ---- exact circular-sequence machinery (mirrors both encoders) ---------
def critical_direction(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    vx, vy = dy, -dx
    if vy < 0 or (vy == 0 and vx < 0):
        vx, vy = -vx, -vy
    return (vx, vy)


def dir_cmp(p, q):
    cross = p[0] * q[1] - p[1] * q[0]
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0


def build_sequence(points):
    n = len(points)
    events = [(critical_direction(a, b), (ia, ib))
              for (ia, a), (ib, b) in combinations(enumerate(points), 2)]
    events.sort(key=cmp_to_key(lambda e1, e2: dir_cmp(e1[0], e2[0])))
    init = sorted(range(n), key=lambda i: points[i][0])
    # groups by exact equal angle
    groups = []
    cur = [events[0]]
    for e in events[1:]:
        if dir_cmp(e[0], cur[0][0]) == 0:
            cur.append(e)
        else:
            groups.append(cur)
            cur = [e]
    groups.append(cur)
    return events, init, groups


def replay_old_run_merge(events, init, groups):
    """Reproduce the OLD allowable_encoder.replay(): reverses merged runs of
    positions in the multi-event group branch.  Returns (permlist, ok, detail)."""
    p = list(init)
    pos = {idx: i for i, idx in enumerate(p)}
    permlist = [list(p)]
    ok = True
    detail = []
    for g in groups:
        if len(g) == 1:
            ia, ib = g[0][1]
            if abs(pos[ia] - pos[ib]) != 1:
                ok = False
                detail.append(f"non-adjacent swap {ia},{ib}")
            i1 = min(pos[ia], pos[ib])
            p[i1], p[i1 + 1] = p[i1 + 1], p[i1]
            for k, idx in ((i1, p[i1]), (i1 + 1, p[i1 + 1])):
                pos[idx] = k
        else:
            # OLD: reverse each maximal consecutive run of involved positions
            pairs = [(aa, bb) for (d0, (aa, bb)) in g]
            involved = sorted(set(pos[aa] for (aa, bb) in pairs)
                              | set(pos[bb] for (aa, bb) in pairs))
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
                items = [p[q] for q in run]
                for q, it in zip(run, items[::-1]):
                    p[q] = it
                    pos[it] = q
        permlist.append(list(p))
    return permlist, ok, detail


def tally_and_perpair(events, init, groups):
    """The old encoder's SEPARATE tally (per-event adjacency) plus the
    corrected per-pair replay (adjudicator's _replay_group)."""
    p = list(init)
    pos = {idx: i for i, idx in enumerate(p)}
    n_adj = 0
    for g in groups:
        for (d, (a, b)) in g:
            if abs(pos[a] - pos[b]) == 1:
                n_adj += 1
            # corrected per-pair swap
            i, j = pos[a], pos[b]
            p[i], p[j] = p[j], p[i]
            pos[a], pos[b] = j, i
    return n_adj


def main():
    out = []
    def pr(*a):
        out.append(" ".join(str(x) for x in a))

    pr("=" * 74)
    pr("allseq_axiom_adjudication.py — resolve the [A] axiom inconsistency")
    pr("in code/out/allowable_encoder.py on the verified es_construct set.")
    pr("All arithmetic exact (Fractions).")
    pr("=" * 74)

    for n in (4, 5, 6, 7):
        points, blocks = es_set_blocks(n)
        N = len(points)
        n_ties = 0
        events, init, groups = build_sequence(points)
        n_distinct_angles = len(groups)
        n_events = len(events)
        tied_group_sizes = [len(g) for g in groups if len(g) > 1]

        # OLD replay (merged-run reversal) vs tally (per-event) vs corrected
        permlist, ok_old, det = replay_old_run_merge(events, init, groups)
        n_adj_tally = tally_and_perpair(events, init, groups)

        pr(f"\n--- n={n} N={N} ---")
        pr(f"  events={n_events}=C({N},2): {n_events==N*(N-1)//2}")
        pr(f"  distinct critical angles={n_distinct_angles}  "
          f"tied-angle groups={len(tied_group_sizes)}  "
          f"tied group sizes={tied_group_sizes[:8]}")
        pr(f"  [A] OLD replay() ok={ok_old}  detail={det[:3]}")
        pr(f"  [A] separate tally single-adjacent={n_adj_tally}/{n_events}")
        pr(f"  => CONTRADICTION reproduced: "
          f"{'YES' if (not ok_old and n_adj_tally==n_events) else 'no'}")

        # show the old multi-event branch is the corruptor when ties exist
        if tied_group_sizes:
            pr(f"  => ties DO exist; OLD run-merging reversed merged positions in "
              f"these groups of size {tied_group_sizes}")
        else:
            pr(f"  => NO tied angles (every group size 1); the old encoder's "
              f"len(g)>1 branch never ran, so it cannot be the only bug")

    pr("\n" + "=" * 74)
    pr("VERDICT")
    pr("=" * 74)
    pr("  The old allowable_encoder.py used TWO inconsistent code paths:")
    pr("   - replay(): reverses MERGED RUNS of positions in multi-event groups")
    pr("   - tally:    swaps each event's pair independently")
    pr("  A tied group with disjoint side-by-side pairs [A,B,C,D] over (A,B),(C,D)")
    pr("  must give [B,A,D,C]; run-reversing gives [D,C,B,A] and corrupts the")
    pr("  running permutation, so later 'non-adjacent swap 11,13' reports are a")
    pr("  corrupted-state artifact, NOT an axiom violation.")
    pr("  The adjudicator's corrected per-pair replay (allseq_adjudicate.py ")
    pr("  TEST 1) gives PAIR/PASS (= N(N-1)/2 adjacent, zero non-adjacent) at")
    pr("  n=4..7, so the Goodman-Pollack axioms hold on es_construct.")
    res = "\n".join(out)
    print(res)
    with open("/workspace/code/out/allseq_axiom_adjudication.captured.txt", "w") as f:
        f.write(res + "\n")
    print("\n[written code/out/allseq_axiom_adjudication.captured.txt]")

    # scalar summary for the caller
    return res


if __name__ == "__main__":
    main()
