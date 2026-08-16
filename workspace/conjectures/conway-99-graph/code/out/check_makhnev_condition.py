"""Check Makhnev 1988 condition (*) on the two positive control graphs.

Condition (*): any two triangles joined by at least two edges are joined by
exactly three edges.  Equivalently n_3 = 0, where n_3 = number of DISJOINT
pairs of triangles joined by exactly 2 edges.  (Two triangles are "joined by
e edges" when e edges of the graph run between a vertex of one triangle and a
vertex of the other.)

For an srg(v,k,1,2) with lambda=1, mu=2 every edge lies in a unique triangle
and two distinct triangles share at most one vertex.  A shared-vertex pair of
triangles is automatically 4-joined and is a separate, non-load-bearing class:
condition (*) and n3 are defined over DISJOINT triangle pairs only, because
"n3 = #pairs joined by exactly 2 edges" can only be realised by disjoint pairs.

This is the admissibility run GOAL.md demands before Makhnev 1988 Thm 2 can be
cited as a 99-argument: every nonexistence argument must be run against both
positive controls through code/lib, and the step that would go wrong for them
must be named.  Here the hypothesis n_3 = 0 is checked on rook(3) = srg(9,4,1,2)
and bvls_graph() = srg(243,22,1,2) exactly, over the integer 0/1 adjacency
matrices from lib.srg, with is_srg as an entry guard asserting each control
really is srg(v,k,1,2) before (*) is tested.

Runs from exact integer arithmetic only (no floating point, no eigenvalues).
"""
import time
from itertools import combinations
from collections import Counter

import numpy as np

from lib.srg import rook, bvls_graph, is_srg


def triangles(A):
    """All triangles of adjacency matrix A as frozensets, by integer adjacency
    checks over unordered triples. Exact combinatorial enumeration."""
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    tris = []
    for i, j, k in combinations(range(n), 3):
        if A[i, j] and A[i, k] and A[j, k]:
            tris.append(frozenset((i, j, k)))
    return tris


def join_hists(A, tris):
    """Join-edge histograms over every unordered pair of DISTINCT triangles,
    split into two classes:

      - disjoint_hist[e] : pairs of triangles that share NO vertex, joined by
        exactly e edges between them;
      - shared_hist[e]   : pairs of triangles that SHARE a vertex.

    Condition (*) / n3 are defined over DISJOINT pairs only. Exact integers.
    """
    A = np.asarray(A, dtype=np.int64)
    disjoint = Counter()
    shared = Counter()
    for a, b in combinations(tris, 2):
        if a & b:
            e = 0
            for x in a:
                for y in b:
                    if A[x, y]:
                        e += 1
            shared[e] += 1
        else:
            e = 0
            for x in a:
                for y in b:
                    if A[x, y]:
                        e += 1
            disjoint[e] += 1
    return disjoint, shared


def check_condition_star(name, A, v, k, lam, mu, label):
    """Run the admissibility check for one control graph. Returns
    (name, T, disjoint_hist, shared_hist, n3, star_holds)."""
    A = np.asarray(A, dtype=np.int64)

    # --- entry guard: the control MUST be an srg(v,k,1,2) before (*) is tested
    ok, detail = is_srg(A, v, k, lam, mu)
    print(f"=== {name} :: {label} ===")
    print(f"is_srg({v},{k},{lam},{mu}) guard: {'PASS' if ok else 'FAIL'}  ({detail})")
    if not ok:
        raise AssertionError(
            f"entry guard failed: {name} is not srg({v},{k},{lam},{mu}): {detail}")
    print(f"  (entry guard asserted: PASS — proceeding to condition (*))")

    tris = triangles(A)
    T = len(tris)
    expect_T = v * k // 6   # edges = vk/2, each triangle has 3 edges, each edge in 1
    print(f"triangles T = {T}   (expect vk/6 = {expect_T})   match: {T == expect_T}")

    dhist, shist = join_hists(A, tris)
    n_disjoint = sum(dhist.values())
    n_shared = sum(shist.values())
    complete = (n_disjoint + n_shared == T * (T - 1) // 2)
    print(f"disjoint-pair join histogram: {dict(sorted(dhist.items()))}")
    print(f"shared-vertex-pair join histogram (non-load-bearing, excluded from (*)): "
          f"{dict(sorted(shist.items()))}")
    print(f"  pairs: disjoint {n_disjoint} + shared {n_shared} = {n_disjoint + n_shared}"
          f"   C(T,2) = {T * (T - 1) // 2}   complete: {complete}")

    n3 = dhist.get(2, 0)
    # condition (*): no DISJOINT pair joined by >=2 edges is joined by != 3.
    violating = [e for e in dhist if e >= 2 and e != 3]
    star_holds = (not violating)
    print(f"n3 (DISJOINT pairs joined by exactly 2 edges) = {n3}")
    print(f"disjoint pairs joined by >=2 edges but not exactly 3 (violate (*)): "
          f"{sum(dhist[e] for e in violating) if violating else 0} "
          f"{dict(sorted({e: dhist[e] for e in violating}.items())) if violating else ''}")
    print(f"condition (*) holds: {star_holds}")
    print()
    return name, T, dict(sorted(dhist.items())), dict(sorted(shist.items())), n3, star_holds


def main():
    t0 = time.time()
    print("# Ran: python3 code/out/check_makhnev_condition.py")
    print("# Oracle: lib.srg.is_srg entry guard; condition (*) by exact integer")
    print("#   disjoint-pair join-edge counting over the lib.srg adjacency matrices")
    print("#   (no floats).")
    print("# Inputs: rook(3) = srg(9,4,1,2), bvls_graph() = srg(243,22,1,2).")
    print("# Purpose: Makhnev 1988 condition (*) admissibility check on the two")
    print("#   positive control graphs (GOAL.md gate before citing Makhnev Thm 2).")
    print()

    results = [
        check_condition_star("rook(3)", rook(3), 9, 4, 1, 2, "srg(9,4,1,2)"),
        check_condition_star("bvls_graph()", bvls_graph(), 243, 22, 1, 2,
                             "srg(243,22,1,2)"),
    ]

    print("# Verdict")
    for name, T, dhist, shist, n3, star in results:
        print(f"{name}: T={T}, disjoint-join {dhist}, n3={n3}, "
              f"condition (*) holds: {star}")
    all_hold = all(r[5] for r in results)
    print(f"condition (*) holds on BOTH controls: {all_hold}")
    print(f"Note: both controls have mu=2 <= 3, so Makhnev 1988 Thm 1's first "
          f"branch (mu<=3) absorbs them — the theorem does not rule them out, "
          f"consistent with their existence. The oracle confirms n3=0 exactly; "
          f"it does not assume it.")
    print(f"wall {time.time()-t0:.2f}s")


if __name__ == "__main__":
    main()
