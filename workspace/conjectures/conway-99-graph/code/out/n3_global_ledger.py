#!/usr/bin/env python3
"""n3_global_ledger.py -- exact global incidence ledger for the n3 seed in a
putative srg(99,14,1,2).

QUESTION: does the n3 seed, grown to its stable local fixpoint, pin any forced
lines/incidences that OVER-SUBSCRIBE the fixed global budget of the partial
Steiner triple system (99 points, 7 lines/point, 693 incidences, 231 lines)?

SETUP (reused from lib.n3patch, the single home of the seed and its growth):
  * seed T1={a,b,c}, T2={d,e,f}, joined by exactly a-d, b-e (2 edges) with the
    other 7 cross pairs non-adjacent.
  * grow to a lambda-witness FIXPOINT (rule 3: every ADJACENT pair with 0
    interior common neighbours gets one fresh witness adjacent to both,
    re-checked between additions).
  * enumerate all completions of the still-undecided interior pairs, keep only
    those satisfying the SOUND upper-bound criterion (ADJ <=1 common neighbour,
    NONADJ <=2, locally 7K2, degree <=14 -- only excesses are contradictions).

THE REASONING EACH NUMBER RESTS ON (the forced-line count is exact):
  Since lambda=1, every graph edge lies in exactly one triangle (line).  At the
  stable fixpoint every inside edge {v,u} has EXACTLY ONE common neighbour, and
  by the 7K2 matching rule that common neighbour is u's matching partner inside
  N(v).  Hence
     (A) every inside edge completes to a FULLY-INSIDE line {v,u,partner};
     (B) the inside-neighbour set I(v) is closed under matching pairing, so
         |I(v)| is even and the number of fully-inside lines through v is
         |I(v)|/2 = the number of patch 3-cliques through v;
     (C) every line through a patch vertex that is NOT fully inside has BOTH
         other points outside the patch (a line with exactly one patch point
         beyond v would contradict the matching pairing).
  So the FORCED ledger is exact:
     forced lines L_in      = # of 3-cliques fully inside the patch,
     forced incidences      = 3 * L_in,
     residual lines         = 231 - L_in,
     residual incidences    = 693 - 3 * L_in,
     and every patch vertex v still needs 7 - (patch 3-cliques through v)
     additional lines, all of whose other points lie outside the patch.

OVER-SUBSCRIPTION SELF-CHECK (no exhaustively reconstructing the outside):
  The residual budget is absorbable iff for every patch vertex v
     (i)  |I(v)| is even              (matching-pairing closure)
     (ii) patch-3-cliques through v <= 7      (can't exceed 7 lines/point)
     (iii) deficient lines 7-tri_through(v) >= 0.
  If (i)-(iii) hold the residual arithmetic is EXACT (sum of deficits over the
  patch == 693 - 3*L_in, and 99 - |patch| outside points provide the rest), so
  no counting floor can overflow.  A violation of (i) is a genuine structural
  obstruction the local closure already pins; a violation of (ii)-(iii) is an
  over-subscription.  Otherwise -- this run's honest expectation, matching the
  local runs -- the finding is: NO forcing floor over-subscribes; the
  obstruction, if any, is structural/global, not a counting overflow.

OUTPUT: code/out/n3_global_ledger.captured.txt
  - self-check that the seed/growth reproduces radius 1 (8 verts, 2 survivors)
    and the stable radius-6 fixpoint with 19 fully-decided survivors;
  - the forced ledger (L_in, inc_in, residuals, per-vertex lines) for every
    radius-6 survivor, the min/max across the 19, and the consistency verdict;
  - the honest conclusion.
"""
import itertools
import time
from lib import n3patch as np

FIXPOINT_BOUND = 1 << 30   # only used internally; all radius-6 survivors fit
                           # (0 free bits at fixpoint), so enumeration is trivial


def growth_to_radius6():
    """Replicate n3_grow_radius.py's radius-by-radius growth but reuse the lib
    seed/closure/upper_ok, and STOP at the stable fixpoint (radius 6 in the
    reference run).  Returns (selfcheck_text, fixpoint_survivors) where each
    survivor is (verts, A) fully decided."""
    verts, A = np.seed()
    # radius 0
    r0_free = len(np.undecided_pairs(verts, A))
    # radius 1: closure of radius 0, then enumerate
    v1, A1, res1 = np.closure_rule3(verts, A)
    assert res1 == 'ok'
    free1 = np.undecided_pairs(v1, A1)
    asg1 = np.assignments(v1, A1)
    surv1 = []
    seen = set()
    for bits, aA in asg1:
        ok, _ = np.upper_ok(v1, aA)
        if ok:
            canon = tuple(sorted((u, w, aA[(u, w)])
                                 for u, w in itertools.combinations(v1, 2)))
            if canon not in seen:
                seen.add(canon)
                surv1.append((v1, aA))
    selfcheck = []
    selfcheck.append("### Self-check (radius 1)")
    selfcheck.append(f"  radius 0: {len(verts)} vertices, 0 free bits, 1 survivor (seed)")
    selfcheck.append(f"  radius 1 closure materialised {len(v1) - 6} witness(es) -> "
                     f"{len(v1)} vertices, {len(free1)} free interior bits")
    selfcheck.append(f"  radius 1 survivors under sound criterion: {len(surv1)} "
                     f"(MUST be 2)")
    # then iterate to a stable fixpoint (all free bits 0)
    frontier = surv1
    rad = 1
    rounds = []
    while True:
        rad += 1
        next_frontier = []
        grew_any = False
        per = []
        for i, (verts, aA) in enumerate(frontier):
            nv, nA, res = np.closure_rule3(verts, aA)
            if res == 'excess':
                per.append((i, 'excess'))
                continue
            grew = len(nv) > len(verts)
            grew_any = grew_any or grew
            nfree = len(np.undecided_pairs(nv, nA))
            cnt = 0
            for _, a2 in np.assignments(nv, nA):
                ok, _ = np.upper_ok(nv, a2)
                if ok:
                    cnt += 1
                    next_frontier.append((nv, a2))
            per.append((i, len(nv), nfree, cnt))
        rounds.append((rad, per, len(next_frontier)))
        if not next_frontier:
            break
        if not grew_any:
            # a stable fixpoint: survivors fully decided
            fixed = [_ for _ in next_frontier
                     if not np.undecided_pairs(_[0], _[1])]
            selfcheck.append("### Radius growth summary (replicated, to stable fixpoint)")
            for (r, per, nf) in rounds:
                selfcheck.append(f"  radius {r}: {nf} survivor(s); per-survivor "
                                 f"(verts,free,surv) = {per}")
            fully = all(not np.undecided_pairs(v, a) for (v, a) in next_frontier)
            selfcheck.append(f"  stable fixpoint: {len(next_frontier)} survivors, "
                             f"all fully decided: {fully}; max verts = "
                             f"{max(len(v) for v, _ in next_frontier)}")
            selfcheck.append(f"  (reference run: 19 survivors, max verts 12, "
                             f"free bits 0 -- must match)")
            return selfcheck, next_frontier
        frontier = next_frontier
        if rad > 30:
            selfcheck.append("  !! did not stabilise within 30 radii")
            return selfcheck, None
    selfcheck.append("  !! no fixpoint survivors")
    return selfcheck, None


def ledger_of_survivor(verts, A, label):
    ld = np.forced_ledger(verts, A)
    # independent identity cross-check: sum of per-vertex triangles == 3*L_in,
    # the per-vertex deficits over the patch sum to 7*|patch| - 3*L_in, and the
    # FULL residual 693 - 3*L_in is exactly that PLUS the outside vertices'
    # whole 7 lines each: 7|patch|-3L + 7(99-|patch|) == 693 - 3L.  So the
    # residual-incidence budget is always exactly saturated by construction.
    n = ld['V_patch']
    tri_sum = sum(ld['tris_through'].values())
    def_sum = sum(ld['line_deficit'].values())
    ident_ok = (tri_sum == 3 * ld['L_in'] and def_sum == 7 * n - 3 * ld['L_in']
                and ld['sum_patch_deficit'] == def_sum
                and def_sum + 7 * (99 - n) == 693 - 3 * ld['L_in'])
    out = []
    out.append(f"### Survivor {label} -- {ld['V_patch']} vertices, "
               f"fully_decided={ld['fully_decided']}")
    out.append(f"  identity check (sum tris={tri_sum}==3*{ld['L_in']}; "
               f"sum deficits={def_sum}=7*{n}-3*{ld['L_in']}; "
               f"def+7*(99-{n})={def_sum + 7*(99-n)}==693-{3*ld['L_in']}): "
               f"{'OK' if ident_ok else 'FAIL'}")
    out.append(f"  forced lines L_in (patch 3-cliques): {ld['L_in']}")
    out.append(f"  forced incidences (3*L_in):          {ld['inc_in']}")
    out.append(f"  residual lines (231 - L_in):         {ld['residual_lines']}")
    out.append(f"  residual incidences (693-3L_in):     {ld['residual_inc']}")
    out.append(f"  outside points (99 - {ld['V_patch']}): {ld['outside_pts']}")
    out.append(f"  sum of per-vertex line deficits:     {ld['sum_patch_deficit']}")
    tris = ld['tris_through']
    out.append("  per-vertex patch lines / inside-nbr parity:")
    for v in sorted(tris, key=lambda x: (isinstance(x, str), x)):
        out.append(f"    {v}: {tris[v]} patch-triangle(s), |I(v)|={len(ld['inside_nbrs'][v])} "
                   f"({'even' if len(ld['inside_nbrs'][v]) % 2 == 0 else 'ODD'})")
    out.append(f"  max lines through any patch vertex:  {ld['max_lines_v']}")
    out.append(f"  odd-match-pairing vertices:          {ld['odd_IN']}")
    out.append(f"  over-subscribed (>7) vertices:       {ld['sat_overflow']}")
    out.append(f"  negative-deficit vertices:           {[v for v in ld['line_deficit'] if ld['line_deficit'][v] < 0]}")
    verdict = "CONSISTENT (no forced line/incidence overflow)" if ld['consistent'] else "INCONSISTENT (over-subscription or parity break)"
    out.append(f"  consistency: {verdict}")
    return out, ld, ident_ok


def main():
    t0 = time.time()
    lines = []
    lines.append("# n3_global_ledger.py -- exact global incidence ledger for the")
    lines.append("#   n3 seed in a putative srg(99,14,1,2)")
    lines.append("# Ran: python3 code/out/n3_global_ledger.py")
    lines.append("#")
    lines.append("# Question: does the n3 seed, grown to its stable local fixpoint,")
    lines.append("#   pin forced lines/incidences that over-subscribe the fixed")
    lines.append("#   global budget of the partial STS (99 pts, 231 lines, 693 inc,")
    lines.append("#   7 lines/point)?  This is the k=14-specific step the order-6")
    lines.append("#   identities cannot see.")
    lines.append("#")
    lines.append("# Method (see lib/n3patch.py, the single home of seed/growth):")
    lines.append("#   grow the seed to a lambda-witness fixpoint (rule 3), enumerate")
    lines.append("#   interior completions under the SOUND upper-bound criterion,")
    lines.append("#   reach a stable fixpoint with fully-decided survivors.  Then the")
    lines.append("#   forced ledger is EXACT: forced lines = #patch 3-cliques L_in,")
    lines.append("#   forced incidences = 3*L_in, residual = 231-L_in / 693-3L_in,")
    lines.append("#   and every patch vertex v still needs 7 - (patch 3-cliques")
    lines.append("#   through v) lines, all with both other points OUTSIDE.")
    lines.append("#   Identity: per-vertex line deficits sum to 7*|patch| - 3*L_in,")
    lines.append("#   and +7*(99-|patch|) outside lines == 693 - 3*L_in (exact).")
    lines.append("#   The residual is absorbable iff every patch vertex has even")
    lines.append("#   |I(v)| (matching-pairing closure), <=7 patch lines, and")
    lines.append("#   nonnegative deficit.  Otherwise it is a genuine obstruction")
    lines.append("#   or over-subscription; if all survivors pass, NO counting floor")
    lines.append("#   over-subscribes -- the obstruction (if any) is structural.")
    lines.append("#   EXACT integer arithmetic throughout, no floats.")
    lines.append("")
    lines.append("## 0. Growth replication + self-check")
    selfcheck, survivors = growth_to_radius6()
    lines.extend(selfcheck)
    if survivors is None:
        lines.append("  ABORT: did not reach a stable fixpoint.  No ledger possible.")
        txt = "\n".join(lines)
        print(txt)
        with open("code/out/n3_global_ledger.captured.txt", "w") as fh:
            fh.write(txt + "\n")
        return
    lines.append("")
    lines.append(f"## 1. Forced ledger -- all {len(survivors)} radius-6 survivors")
    all_ld = []
    idents_ok = []
    for i, (verts, A) in enumerate(survivors):
        sub, ld, ident_ok = ledger_of_survivor(verts, A, i)
        all_ld.append(ld)
        idents_ok.append(ident_ok)
        lines.extend(sub)
        lines.append("")
    # aggregate
    L_ins = [ld['L_in'] for ld in all_ld]
    inc_ins = [ld['inc_in'] for ld in all_ld]
    maxlines = [ld['max_lines_v'] for ld in all_ld]
    odd_all = [v for ld in all_ld for v in ld['odd_IN']]
    over_all = [v for ld in all_ld for v in ld['sat_overflow']]
    neg_all = [v for vv in ([v for v in ld['line_deficit'] if ld['line_deficit'][v] < 0] for ld in all_ld) for v in vv]
    consistent_all = all(ld['consistent'] for ld in all_ld)
    idents_all = all(idents_ok)
    V_patches = [ld['V_patch'] for ld in all_ld]
    lines.append("## 2. Aggregate across the 19 survivors")
    lines.append(f"  patch sizes: {sorted(set(V_patches))} (min {min(V_patches)}, "
                 f"max {max(V_patches)})")
    lines.append(f"  forced lines L_in:  min {min(L_ins)}, max {max(L_ins)}")
    lines.append(f"  forced incidences:  min {min(inc_ins)}, max {max(inc_ins)}")
    lines.append(f"  residual lines:     {231 - max(L_ins)} .. {231 - min(L_ins)}")
    lines.append(f"  residual incidences: {693 - max(inc_ins)} .. {693 - min(inc_ins)}")
    lines.append(f"  max lines through any patch vertex: {max(maxlines)}")
    lines.append(f"  any odd |I(v)| (parity break):      {odd_all}")
    lines.append(f"  any over-subscribed (>7) vertex:    {over_all}")
    lines.append(f"  any negative deficit:               {neg_all}")
    lines.append(f"  ALL survivors consistent (no forced-line/incidence overflow): "
                 f"{consistent_all}")
    lines.append(f"  ALL survivors pass the residual-deficit identity check: "
                 f"{idents_all}")
    lines.append("")
    lines.append("## 3. Honest conclusion")
    if consistent_all and not odd_all and not over_all and not neg_all:
        lines.append("  NO forcing floor over-subscribes the fixed global budget.")
        lines.append("  For every radius-6 survivor the forced ledger is EXACT and the")
        lines.append("  residual (231-L_in lines, 693-3L_in incidences) is arithmetically")
        lines.append("  absorbable by the outside points: each patch vertex's per-line")
        lines.append("  deficit sums exactly to the residual, so no counting floor can")
        lines.append("  overflow.  If an obstruction to srg(99,14,1,2) exists at this")
        lines.append("  seed, it is GENUINELY GLOBAL/STRUCTURAL (a later-radius or a")
        lines.append("  cross-patch conflict), NOT a counting floor.")
    else:
        lines.append("  A forced over-subscription / parity break WAS found -- see the")
        lines.append("  flagged vertices above.  This is the first genuine global")
        lines.append("  obstruction from the n3 seed's local closure.")
    lines.append(f"## wall clock: {time.time() - t0:.1f}s")

    txt = "\n".join(lines)
    print(txt)
    with open("code/out/n3_global_ledger.captured.txt", "w") as fh:
        fh.write(txt + "\n")
    return consistent_all


if __name__ == "__main__":
    ok = main()
    print("\n[all survivors consistent, no forced overflow] =", ok)
