#!/usr/bin/env python3
"""n3_seed_consistency_ub.py -- SOUND local-consistency oracle for the n3 seed,
using the UPPER-BOUND criterion (the only one arc-consistency may soundly
conclude), not exact-within-patch equality.

Correct criterion for local consistency of a partial patch:
  * lambda = 1 : an ADJACENT pair may have AT MOST ONE common neighbour
    (a 2nd is a defect that no outside vertex can undo).
  * mu    = 2 : a NON-ADJACENT pair may have AT MOST TWO common neighbours in
    the patch (a 3rd is a defect); a deficit (0 or 1 or 2 needed) is satisfiable
    by outside vertices, so it is NOT a contradiction.
  * locally 7K2.

This is exactly what a sound arc-consistency propagator (with 'choose the
outside vertex' as a free option) can conclude.  A satisfying assignment is a
certificate that the n3 seed is locally consistent; its absence would be a real
local obstruction.  Complete enumeration over the free interior edges (a tiny
fixed patch), exact integers.
"""
import itertools


NAMES = ['a', 'b', 'c', 'd', 'e', 'f']
EDGES = {('a', 'b'), ('b', 'c'), ('c', 'a'),
         ('d', 'e'), ('e', 'f'), ('f', 'd'),
         ('a', 'd'), ('b', 'e')}
NONEDGES = {('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
            ('a', 'f'), ('b', 'd'), ('c', 'e')}


def closure():
    edges = {frozenset(p) for p in EDGES}
    nonedges = {frozenset(p) for p in NONEDGES}
    for w, (u, v) in [('6', ('a', 'd')), ('7', ('b', 'e'))]:
        edges.add(frozenset((w, u)))
        edges.add(frozenset((w, v)))
    return edges, nonedges


def all_pairs(verts):
    return [frozenset(p) for p in itertools.combinations(verts, 2)]


def completion_ub_ok(edges, nonedges, assignment, verts):
    A = {p: 0 for p in all_pairs(verts)}
    for p in edges:
        A[p] = 1
    for p in nonedges:
        A[p] = 0
    for p, v in assignment.items():
        A[p] = v

    def adj(u, w):
        return A[frozenset((u, w))]

    for u, w in itertools.combinations(verts, 2):
        common = [x for x in verts if x not in (u, w) and adj(u, x) and adj(w, x)]
        limit = 1 if adj(u, w) else 2
        if len(common) > limit:
            return False
    for v in verts:
        nb = [u for u in verts if u != v and adj(v, u)]
        if nb:  # only neighbours that have an in-patch partner need checking
            for u in nb:
                partners = [x for x in nb if x != u and adj(u, x)]
                if len(partners) > 1:
                    return False
    return True


def main():
    edges, nonedges = closure()
    verts = sorted(NAMES + ['6', '7'])
    known = set(edges) | set(nonedges)
    free = [p for p in all_pairs(verts) if p not in known]
    lim = 1 << len(free)
    lines = []
    lines.append("# n3_seed_consistency_ub.py -- SOUND upper-bound local-consistency")
    lines.append("#   oracle for the n3 seed (lambda=1 <=1 CN, mu=2 <=2 CN)")
    lines.append("# Ran: python3 code/out/n3_seed_consistency_ub.py")
    lines.append("# Criterion: an ADJACENT pair must have <=1 common neighbour in the")
    lines.append("#   patch; a NON-adjacent pair <=2; deficits are satisfiable by the")
    lines.append("#   ~91 outside vertices.  This is the ONLY criterion arc-consistency")
    lines.append("#   may soundly conclude.  Complete enumeration of %d free bits (%d" % (len(free), lim))
    lines.append("#   assignments), exact, no floats.")
    lines.append("# Engine: self-contained sound oracle (NOT the shared over-forcing")
    lines.append("#   engine, whose saturation branch is known-soundness-broken).")
    lines.append("")
    lines.append("## Forced closure (8 vertices: a-f + witnesses 6,7)")
    lines.append("  fixed edges (%d):  %s" % (len(edges), sorted(''.join(sorted(p)) for p in edges)))
    lines.append("  fixed non-edges (%d): %s" % (len(nonedges), sorted(''.join(sorted(p)) for p in nonedges)))
    lines.append("  free interior pairs (%d): %s" % (len(free), sorted(''.join(sorted(p)) for p in free)))
    lines.append("")
    lines.append("## Result")
    count = 0
    example = None
    for bits in range(lim):
        assignment = {}
        for k, p in enumerate(free):
            assignment[p] = (bits >> k) & 1
        if completion_ub_ok(edges, nonedges, assignment, verts):
            count += 1
            if example is None:
                example = assignment
    if count:
        lines.append("  satisfiable assignments under the upper-bound criterion:  %d" % count)
        lines.append("  => the n3 seed IS locally consistent (no forced 2nd/3rd common")
        lines.append("     neighbour, matching intact).")
        if example is not None:
            pairs = sorted(''.join(sorted(p)) + '=' + str(example[p]) for p in example)
            lines.append("  example assignment: " + ", ".join(pairs))
        lines.append("  => the shared engine's VERDICT 'CONTRADICTION' for this seed is")
        lines.append("     an ARTIFACT of its over-forcing saturation branch, NOT a")
        lines.append("     sound local obstruction.  The seed extends locally.")
    else:
        lines.append("  NO assignment satisfies the upper-bound criterion: the seed is")
        lines.append("  genuinely locally inconsistent (a real local obstruction).")
    lines.append("")
    lines.append("## What this settles (and does not)")
    lines.append("  Settles the local-closure question of task `kill-n3-ge1-case`: the")
    lines.append("  2-edge-joined disjoint triangle pair is locally consistent in a")
    lines.append("  lambda=1/mu=2/locally-7K2 graph (or not).  It does NOT settle")
    lines.append("  global existence of srg(99,14,1,2): an 8-vertex patch is not the")
    lines.append("  graph, and consistency here neither proves nor disproves it.")
    txt = "\n".join(lines)
    print(txt)
    with open("code/out/n3_seed_consistency_ub.captured.txt", "w") as fh:
        fh.write(txt + "\n")
    return count


if __name__ == "__main__":
    c = main()
    print("\n[satisfiable upper-bound assignments] =", c)
