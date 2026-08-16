#!/usr/bin/env python3
"""n3_grow_radius.py -- at what radius does the n3 seed stop extending?

EXACT GROWTH RULE (the SOUND rule; steering directive; this is implemented
verbatim, no hand-rolled saturation, no solver):

  A patch is an exact +1/0/-1 partial adjacency matrix (materialised
  vertices): +1 adjacent, 0 non-adjacent, -1 unknown, symmetric, zero
  diagonal.  Seed = six vertices a,b,c,d,e,f; T1={a,b,c}, T2={d,e,f} are two
  disjoint triangles; the join is EXACTLY two cross edges a-d and b-e; the
  other seven cross pairs {c,f,a,e,b,f,c,d,a,f,b,d,c,e} are non-adjacent.

  The ONLY things that may decide entries (all SOUND for lambda=1, mu=2,
  locally-7K2):
    (1) lambda-excess: an ADJACENT pair with >=2 common neighbours inside the
        patch -> CONTRADICTION (record the excess witness).
    (2) mu-excess:     a NON-ADJACENT pair with >=3 common neighbours inside
        the patch -> CONTRADICTION.
    (3) lambda-force:  an ADJACENT pair (i,j) with EXACTLY 0 common
        neighbours inside the patch must have its UNIQUE lambda-witness
        outside the patch; materialise ONE new witness vertex w with w-i=1
        and w-j=1 (fresh label).  Sound: the pair's unique common neighbour
        cannot lie inside the patch, so a single fresh outside vertex is
        forced.
    (4) 7K2:           for vertex v, if a neighbour u of v is adjacent to
        another neighbour w of v, then u (and w) are non-adjacent to every
        OTHER neighbour of v (matching).  If u is adjacent to two distinct
        neighbours of v -> CONTRADICTION.
    (5) degree:        no vertex may exceed 14 established neighbours; if it
        does, that radius's assignment dies.

  We do NOT materialise mu-witnesses for non-adjacent pairs (their mu=2
  deficit is satisfiable by the ~91 outside vertices), and we never force
  a-v=0 AND b-v=0 (the sound 7K2-only clause is NOT both).  Only EXCESSES are
  contradictions; disk-adjacency, is what this file decides exactly.

  GROWTH: radius 0 = the 6 seed vertices (all 15 pairs decided, 0 free bits).
  Radius 1 = apply rule (3) closure once to radius 0: the two seeded edges
  a-d and b-e each have 0 interior common neighbours, so a distinct witness
  is materialised for each -> 8 vertices.  Then enumerate ALL assignments of
  the undecided pairs among the 8 vertices and count those satisfying (1)(2)
  (4)(5).  For radius r+1 (r>=1): for EACH distinct surviving assignment at
  radius r, grow the patch by applying rule (3) to a FIXPOINT (materialise a
  fresh witness for every adjacent pair that still has 0 interior common
  neighbours, re-applying (4)(5) between additions) -- this is the ONLY thing
  that grows the patch.  Then enumerate ALL assignments of the still-undecided
  pairs among ALL materialised vertices and count survivors under (1)-(5).

SOUNDNESS ARGUMENT: every bit this rule decides (rule 3 materialisation, and
the checks) is a logical consequence of (lambda=1, mu=2, locally-7K2) applied
to decided +1/0 entries ONLY.  Deficits (fewer common neighbours than needed)
are never contradictions because the remaining ~91 vertices can supply them, so
only excesses can kill an assignment.  We never force both endpoints of a
saturated pair off, which was the unsoundness in code/lib/localprop.py's
saturation branch.  A nonzero survivor count therefore PROVES the seed extends
to that radius under the sound criterion; a zero at some radius would be the
first genuine local obstruction.

STOP conditions: (a) a radius with ZERO survivors -> report the excess
witness (genuine local obstruction); (b) free-bit count > 2^20 (~1M
assignments) -> report as the complete-enumeration boundary; (c) a 9-minute
wall clock; or (d) a stable fixpoint with survivors and free bits <= 2^20,
from which no further radius grows (seed extends forever locally).

Oracle function: self-contained upper-bound oracle in this file (the SOUND
criterion; NOT the shared localprop saturation engine).  Self-check: radius 1
MUST reproduce the established result (8 vertices, 2 satisfying assignments)
before any larger radius is trusted.
"""
import itertools
import time

DEGREE = 14
SEED = ['a', 'b', 'c', 'd', 'e', 'f']
EDGES = {('a', 'b'), ('b', 'c'), ('c', 'a'),
         ('d', 'e'), ('e', 'f'), ('f', 'd'),
         ('a', 'd'), ('b', 'e')}
NONEDGES = {('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
            ('a', 'f'), ('b', 'd'), ('c', 'e')}
BIT_CAP = 1 << 20
WALL_CLOCK_SEC = 9 * 60


def _fresh_label(used):
    i = 0
    while 'W%02d' % i in used:
        i += 1
    return 'W%02d' % i


def seed():
    """Radius-0 seed: the 6 named vertices, all 15 pairs decided."""
    verts = list(SEED)
    A = {}
    for u in verts:
        A[(u, u)] = 0
    for (u, v) in EDGES:
        A[(u, v)] = A[(v, u)] = 1
    for (u, v) in NONEDGES:
        A[(u, v)] = A[(v, u)] = 0
    return verts, A


def undecided_pairs(verts, A):
    return [(verts[i], verts[j]) for i in range(len(verts))
            for j in range(i + 1, len(verts))
            if (verts[i], verts[j]) not in A]


def add_witness(verts, A, i, j):
    """Rule (3): materialise a fresh witness w adjacent to i and to j."""
    w = _fresh_label(set(verts))
    nverts = list(verts) + [w]
    nA = dict(A)
    nA[(w, w)] = 0
    nA[(w, i)] = nA[(i, w)] = 1
    nA[(w, j)] = nA[(j, w)] = 1
    return nverts, nA


def upper_ok(verts, A):
    """SOUND upper-bound criterion over the materialised patch.

    (1) adjacent pairs: <=1 common neighbour; (2) non-adjacent: <=2;
    (4) locally-7K2: each N(v) a partial matching, i.e. no neighbour of v is
        established-adjacent to two distinct neighbours of v; (5) degree <=14.
    Returns (ok, witness_text).  ONLY excesses are contradictions.
    """
    idx = {v: i for i, v in enumerate(verts)}
    n = len(verts)
    # adjacency lookup with defaults: unknown is False for counting purposes
    def adj(u, w):
        return A.get((u, w), 0)
    for u, w in itertools.combinations(verts, 2):
        common = [x for x in verts if x != u and x != w and adj(u, x) and adj(w, x)]
        limit = 1 if adj(u, w) else 2
        if len(common) > limit:
            return False, (f"pair {u}{w} {'ADJ' if adj(u,w) else 'NONADJ'} has "
                           f"{len(common)} common neighbours (limit {limit})")
    for v in verts:
        nbrs = [u for u in verts if u != v and adj(v, u)]
        if len(nbrs) > DEGREE:
            return False, (f"vertex {v} degree {len(nbrs)} > {DEGREE}")
        # every established neighbour must be a partial-matching element:
        # no neighbour u of v adjacent to two distinct neighbours of v
        for u in nbrs:
            paired = [w for w in nbrs if w != u and adj(u, w)]
            if len(paired) > 1:
                return False, (f"7K2: neighbour {u} of {v} adjacent to "
                               f"two neighbours {paired}")
    return True, "ok"


def closure_rule3(verts, A):
    """Apply rule (3) to a fixpoint, re-checking (4),(5)/(1),(2) excesses
    between additions.  Returns (new_verts, new_A, grew).  Grows ONLY by
    lambda-witness materialisation; mu-witness deficits are NOT materialised.
    """
    nverts, nA = list(verts), dict(A)
    while True:
        grew = False
        # (1),(2) excesses kill this whole patch assignment now
        ok, wit = upper_ok(nverts, nA)
        if not ok:
            return nverts, nA, 'excess'
        # find adjacent pairs with 0 interior common neighbours
        for i, j in itertools.combinations(nverts, 2):
            if not nA.get((i, j), 0):
                continue
            common = [x for x in nverts
                      if x != i and x != j
                      and nA.get((i, x), 0) and nA.get((j, x), 0)]
            if len(common) == 0:
                nverts, nA = add_witness(nverts, nA, i, j)
                grew = True
                break  # restart scan; new vertices could create new edges
        if not grew:
            return nverts, nA, 'ok'


def assignments(verts, A):
    """All assignments of undecided pairs, each decoded as (verts, A')."""
    free = undecided_pairs(verts, A)
    lim = 1 << len(free)
    if lim > BIT_CAP:
        return None
    out = []
    for bits in range(lim):
        nA = dict(A)
        for k, (u, w) in enumerate(free):
            nA[(u, w)] = nA[(w, u)] = (bits >> k) & 1
        out.append((bits, nA))
    return out


def main():
    t0 = time.time()
    lines = []
    lines.append("# n3_grow_radius.py -- at what radius does the n3 seed stop")
    lines.append("#   extending in a lambda=1, mu=2, locally-7K2 graph?")
    lines.append("# Ran: python3 code/out/n3_grow_radius.py")
    lines.append("# GROWTH RULE (SOUND; steering directive): the patch is an exact")
    lines.append("#   +1/0/-1 partial adjacency matrix over materialised vertices.")
    lines.append("#   Radius 0 = 6 seed vertices (0 free bits).  Radius 1 = apply")
    lines.append("#   rule (3) closure once to radius 0: a-d and b-e each have 0")
    lines.append("#   interior common neighbours -> one witness each (8 verts), then")
    lines.append("#   enumerate all assignments of undecided pairs, count survivors.")
    lines.append("#   Radius r+1 (r>=1): for each survivor, apply rule (3) to a")
    lines.append("#   FIXPOINT (materialise a fresh witness for every adjacent pair")
    lines.append("#   with 0 interior common neighbours), then enumerate all")
    lines.append("#   assignments of the still-undecided pairs and count survivors.")
    lines.append("#   Rule (3) is the ONLY thing that grows the patch.  Rules")
    lines.append("#   (1) lambda-excess ADJ<=1 (2) mu-excess NONADJ<=2 (4) 7K2")
    lines.append("#   (5) degree<=14 are CHECKS; only EXCESSES are contradictions.")
    lines.append("#   Deficits are satisfiable by the ~91 outside vertices; we do")
    lines.append("#   NOT materialise mu-witnesses and never force a-v=0 AND b-v=0")
    lines.append("#   (the unsound localprop saturation branch).")
    lines.append("# Oracle: self-contained sound upper-bound oracle (upper_ok) in")
    lines.append("#   this file -- NOT the shared localprop saturation engine.")
    lines.append("# Search space: radius r enumerates the complete product of all")
    lines.append("#   free interior bits over the materialised patch; a survivor")
    lines.append("#   count is exact (complete enumeration), no floats.")
    lines.append("# Stop: zero survivors (genuine local obstruction, give witness),")
    lines.append("#   or free bits > 2^20 (bit boundary), or wall clock, or a stable")
    lines.append("#   fixpoint from which no further radius grows.")
    lines.append("")
    lines.append("## Self-check (radius 1 MUST reproduce 8v, 2 survivors)")
    lines.append("")

    # ---------- radius 0 ----------
    verts, A = seed()
    r0_free = len(undecided_pairs(verts, A))
    lines.append("### Radius 0")
    lines.append(f"  vertices: 6 ({''.join(verts)}); interior pairs decided: "
                 f"all 15; free interior bits: {r0_free}")
    lines.append(f"  survivors under sound criterion: 1 (the seed itself)")
    lines.append("")

    # ---------- radius 1 ----------
    v1, A1, res1 = closure_rule3(verts, A)
    if res1 == 'excess':
        raise RuntimeError("radius-1 closure should not exceed on seed")
    if v1 is None:
        raise RuntimeError("radius-1 closure should not exceed on seed")
    # closure_rule3 fixpoint on radius 0: both a-d and b-e witness -> but note
    # it runs to a fixpoint; check result has exactly the a-d,b-e witnesses.
    r1_free = len(undecided_pairs(v1, A1))
    asg1 = assignments(v1, A1) if (1 << r1_free) <= BIT_CAP else None
    survivors1 = 0
    if asg1 is not None:
        # canonicalise each survivor: keep (labels, decided-A)
        r1 = []
        seen = set()
        for bits, aA in asg1:
            ok, wit = upper_ok(v1, aA)
            if ok:
                survivors1 += 1
                canon = tuple(sorted((u, w, aA.get((u, w)))
                                     for u, w in itertools.combinations(v1, 2)))
                if canon not in seen:
                    seen.add(canon)
                    r1.append((bits, aA))
        lines.append("### Radius 1")
        lines.append(f"  from radius 0, rule (3) closure materialised: "
                     f"{len(v1) - 6} witness(es)")
        lines.append(f"  vertices: {len(v1)}; free interior bits: {r1_free} "
                     f"(enumerated {1 << r1_free})")
        lines.append(f"  survivors under sound criterion: {survivors1}")
        lines.append("  ##### (MUST be 2 to trust larger radii) #####")
        lines.append("")
        # show the two survivor witness-diff for the record
        for i, (bits, aA) in enumerate(r1):
            free_vals = {''.join(sorted(p)): aA[p] for p in undecided_pairs(v1, A1)}
            lines.append(f"    survivor {i}: {free_vals}")
        lines.append("")
    else:
        lines.append("### Radius 1")
        lines.append(f"  vertices: {len(v1)}; free interior bits: {r1_free} > 2^20 "
                     f"(cannot enumerate)")
        lines.append("")
        r1 = []

    # ---------- radius >= 2 : iterate to a stable fixpoint ----------
    lines.append("## Radii 2+ (rule (3) closure to fixpoint, then exact count)")
    lines.append("  From each survivor at radius r, apply rule (3) to a fixpoint;")
    lines.append("   then enumerate all undecided pairs among all materialised")
    lines.append("   vertices and count exact survivors (degrees are checks only).")
    lines.append("  A radius whose survivors add NO new vertices (and none die) is")
    lines.append("   a stable fixpoint: the seed extends locally to every radius.")
    lines.append("")
    stop_reason = None
    stop_kind = None
    if r1:
        # each frontier element: (verts, A) -- a survivor configuration at the
        # current radius, living on its own vertex set.
        frontier = [(v1, aA) for (_, aA) in r1]
        rad = 1
        while True:
            rad += 1
            if time.time() - t0 > WALL_CLOCK_SEC:
                stop_reason = f"wall clock {WALL_CLOCK_SEC}s reached at radius {rad}"
                stop_kind = 'wall'
                break
            next_frontier = []
            max_free = 0
            max_vert = 0
            grew_any = False
            lines.append(f"### Radius {rad}")
            for i, (verts, aA) in enumerate(frontier):
                nv, nA, res = closure_rule3(verts, aA)
                if res == 'excess':
                    lines.append(f"  survivor {i}: closure hit an EXCESS -- "
                                 f"this survivor dies at radius {rad}.")
                    continue
                grew = len(nv) > len(verts)
                grew_any = grew_any or grew
                nfree = len(undecided_pairs(nv, nA))
                max_vert = max(max_vert, len(nv))
                max_free = max(max_free, nfree)
                new_w = len(nv) - len(verts)
                if (1 << nfree) > BIT_CAP:
                    lines.append(f"  survivor {i}: +{new_w} witness, verts={len(nv)}, "
                                 f"free bits={nfree} > 2^20 -> enum stops.")
                    stop_reason = "free bits > 2^20 at radius %d" % rad
                    stop_kind = 'bit'
                    break
                cnt = 0
                expl = None
                for _, a2 in assignments(nv, nA):
                    ok, wit = upper_ok(nv, a2)
                    if ok:
                        cnt += 1
                        next_frontier.append((nv, a2))
                    elif expl is None:
                        expl = wit
                lines.append(f"  survivor {i}: +{new_w} witness, verts={len(nv)}, "
                             f"free bits={nfree}, survivors={cnt}"
                             + (f"  [excess witness: {expl}]" if cnt == 0 else ""))
                if cnt == 0:
                    stop_reason = (f"radius {rad} survivor {i} ZERO survivors "
                                   f"(genuine local obstruction); excess: {expl}")
                    stop_kind = 'zero'
                    break
            if stop_kind:
                break
            lines.append(f"  ---- radius {rad}: {len(next_frontier)} survivor(s), "
                         f"max vertices {max_vert}, max free bits {max_free}")
            if not next_frontier:
                stop_reason = f"radius {rad} zero survivors (obstruction)"
                stop_kind = 'zero'
                break
            if not grew_any:
                stop_reason = (f"radius {rad} is a STABLE FIXPOINT: no survivor "
                               f"materialises a witness, none died; seed extends "
                               f"locally to every radius (free bits {max_free} "
                               f"<= 2^20, no excess)")
                stop_kind = 'fixpoint'
                break
            frontier = next_frontier
    else:
        lines.append("  (no radius-1 survivors to grow -- would be an obstruction)")
        stop_reason = "radius-1 has zero survivors"
        stop_kind = 'zero'
    lines.append("")
    lines.append("## STOP / boundary")
    lines.append("  " + (stop_reason or "no stop condition reached"))
    lines.append("  (stop kind: %s)" % (stop_kind or 'none'))
    lines.append("")
    lines.append("## Interpretation")
    lines.append("  A nonzero survivor count at a radius PROVES the seed extends to")
    lines.append("  that radius under the sound criterion (complete enumeration).")
    lines.append("  A zero would be the first genuine local obstruction.  A stable")
    lines.append("  fixpoint that keeps adding no vertices means the seed extends")
    lines.append("  locally to every radius (no local obstruction, ever).")
    lines.append("  This is a LOCAL statement: it neither proves nor disproves the")
    lines.append("  global existence of srg(99,14,1,2).")
    lines.append(f"## wall clock: {time.time() - t0:.1f}s")

    txt = "\n".join(lines)
    print(txt)
    with open("code/out/n3_grow_radius.captured.txt", "w") as fh:
        fh.write(txt + "\n")
    return survivors1


if __name__ == "__main__":
    s = main()
    print("\n[radius-1 survivors] =", s, "(must be 2)")
