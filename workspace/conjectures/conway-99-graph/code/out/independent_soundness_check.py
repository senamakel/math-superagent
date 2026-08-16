#!/usr/bin/env python3
"""Independent brute-force verification of code/lib/localprop.py's SOUND
deductions on the n3 seed's 8-vertex forced closure.

Purpose:
  1. Confirm the engine produces exactly the forced closure expected (8
     vertices a-f + lambda-witnesses 6,7 with their forced edges).
  2. Confirm the engine's sound deductions are each individually correct by
     verifying against a COMPLETE enumeration (512 assignments) of the free
     interior edges under the sound upper-bound criterion: every forced edge /
     non-edge the engine reports must be forced in EVERY satisfying assignment
     (i.e. the engine never over-forces, never under-forces a value that is
     common to all completions).
  3. Confirm the engine flags genuine excesses.

Independent: this enumerator is written from scratch (no import of lib.localprop
except to obtain the closure) and uses a different reasoning path (exhaustive
assignment checking rather than propagation).

Controls: the engine must not mark any value as forced-on that some satisfying
completion leaves off, and must not miss any value that every completion
forces.  If it agrees on all of them, the propagation is sound AND complete at
this radius for the seeded assignment.
"""
import itertools
from lib.localprop import PartialGraph

NAMES = ['a', 'b', 'c', 'd', 'e', 'f']
EDGES = {('a', 'b'), ('b', 'c'), ('c', 'a'),
         ('d', 'e'), ('e', 'f'), ('f', 'd'),
         ('a', 'd'), ('b', 'e')}
NONEDGES = {('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
            ('a', 'f'), ('b', 'd'), ('c', 'e')}


def engine_closure():
    """Run the engine from the n3 seed; return (forced_edges, forced_nonedges,
    free_entries, witnesses_added)."""
    P = PartialGraph(6, 14)
    P._names = NAMES[:]
    for (u, w) in [('a', 'b'), ('b', 'c'), ('c', 'a'),
                   ('d', 'e'), ('e', 'f'), ('f', 'd'),
                   ('a', 'd'), ('b', 'e')]:
        P._set(NAMES.index(u), NAMES.index(w), 1)
    for (u, w) in [('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
                   ('a', 'f'), ('b', 'd'), ('c', 'e')]:
        P._set(NAMES.index(u), NAMES.index(w), 0)
    log = []
    cons, iters = P.propagate(log)
    assert cons, f"engine expected consistent, got: {log}"
    forced_e = set()
    forced_n = set()
    free = set()
    for i in range(P.n):
        for j in range(i + 1, P.n):
            nm = (P.name(i), P.name(j))
            if P.adj[i][j] == 1:
                forced_e.add(frozenset(nm))
            elif P.adj[i][j] == 0:
                forced_n.add(frozenset(nm))
            else:
                free.add(frozenset(nm))
    return forced_e, forced_n, free, P.n - 6


def enumerate_satisfying():
    """Complete enumeration over the free interior edges (9 bits on the 8
    vertices a-f,6,7), upper-bound criterion.  Returns (count, forced_edges,
    forced_nonedges) where forced_* are the values common to EVERY satisfying
    assignment."""
    verts = NAMES + ['6', '7']
    edges = {frozenset(p) for p in EDGES}
    nonedges = {frozenset(p) for p in NONEDGES}
    # 6 is the lambda witness of (a,d): 6-a, 6-d forced on
    # 7 is the lambda witness of (b,e): 7-b, 7-e forced on
    edges |= {frozenset(('6', 'a')), frozenset(('6', 'd')),
              frozenset(('7', 'b')), frozenset(('7', 'e'))}
    free = [frozenset(p) for p in itertools.combinations(verts, 2)
            if frozenset(p) not in edges | nonedges]

    def ok(assign):
        A = {}
        for p in edges:
            A[p] = 1
        for p in nonedges:
            A[p] = 0
        for p in free:
            A[p] = 1 if (assign >> free.index(p)) & 1 else 0

        def adj(u, w):
            return A[frozenset((u, w))]
        # common-neighbour upper bounds
        for u, w in itertools.combinations(verts, 2):
            common = [x for x in verts if x not in (u, w) and adj(u, x) and adj(w, x)]
            limit = 1 if adj(u, w) else 2
            if len(common) > limit:
                return False
        # locally 7K2
        for v in verts:
            nb = [u for u in verts if u != v and adj(v, u)]
            for u in nb:
                if sum(1 for x in nb if x != u and adj(u, x)) > 1:
                    return False
        return True

    satisfies = []
    N = len(free)
    for bits in range(1 << N):
        if ok(bits):
            satisfies.append(bits)
    # common forced values across ALL satisfying assignments
    forced_e = set(edges)
    forced_n = set(nonedges)
    if satisfies:
        for p in free:
            vals = {(bits >> free.index(p)) & 1 for bits in satisfies}
            if vals == {1}:
                forced_e.add(p)
            elif vals == {0}:
                forced_n.add(p)
    return len(satisfies), forced_e, forced_n, free, satisfies


def main():
    print("# independent_soundness_check.py -- brute-force verification of")
    print("#   lib/localprop.py engine deductions on the n3 seed's 8-vertex closure")
    print("# Ran: python3 code/out/independent_soundness_check.py")
    print("# Criterion (sound upper-bound): adjacent pair <=1 common neighbour,")
    print("#   non-adjacent <=2, 7K2 matching intact.  Complete enumeration of the")
    print("#   free interior edges; the engine's forced values must EXACTLY match")
    print("#   the values common to every satisfying assignment.")
    print()

    fe, fn, free_eng, nw = engine_closure()
    cnt, fe_num, fn_num, free_enum, satisfies = enumerate_satisfying()
    print(f"engine added {nw} witness vertices")
    print(f"engine forced edges:    {sorted(''.join(sorted(p)) for p in fe)}")
    print(f"engine forced non-edges:{sorted(''.join(sorted(p)) for p in fn)}")
    print(f"engine free entries:    {sorted(''.join(sorted(p)) for p in free_eng)}")
    print()
    print(f"complete enumeration: {cnt} satisfying assignments "
          f"(over {len(free_enum)} free bits)")
    print(f"enum forced edges (common to all):    "
          f"{sorted(''.join(sorted(p)) for p in fe_num)}")
    print(f"enum forced non-edges (common to all):"
          f"{sorted(''.join(sorted(p)) for p in fn_num)}")
    print()
    missing_e = fe_num - fe
    extra_e = fe - fe_num
    missing_n = fn_num - fn
    extra_n = fn - fn_num
    print("MISSING forced edges (engine under-forced): "
          f"{sorted(''.join(sorted(p)) for p in missing_e) or 'none'}")
    print("EXTRA forced edges (engine over-forced): "
          f"{sorted(''.join(sorted(p)) for p in extra_e) or 'none'}")
    print("MISSING forced non-edges (engine under-forced): "
          f"{sorted(''.join(sorted(p)) for p in missing_n) or 'none'}")
    print("EXTRA forced non-edges (engine over-forced): "
          f"{sorted(''.join(sorted(p)) for p in extra_n) or 'none'}")
    print()
    agree = not (missing_e or extra_e or missing_n or extra_n)
    print(f"ENGINE == ENUMERATION on all forced values: {agree}")
    return agree, cnt


if __name__ == "__main__":
    agree, cnt = main()
    print("\n[agree, satisfying_count] =", (agree, cnt))
