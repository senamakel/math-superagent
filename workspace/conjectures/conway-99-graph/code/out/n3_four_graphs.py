"""Compute T = number of triangles and n3 = number of unordered triangle pairs
joined by exactly 2 cross-edges (the join-edge histogram) for the FOUR known
lambda=1 SRGs the run can build, plus re-check the (33,12,1,6) infeasibility.

graphs:
  rook(3)   = srg(9,4,1,2)      (3x3 rook's graph)
  doily()   = srg(15,6,1,3)     (GQ(2,2) collinearity graph = Kneser K(6,2))
  gq24_graph() = srg(27,10,1,5) (GQ(2,4) collinearity graph = O^-(6,2) polar space)
  bvls_graph() = srg(243,22,1,2) (Berlekamp-van Lint-Seidel graph)

All four pass lib.srg.is_srg on their own parameters in exact integer
arithmetic (entry guard). triangles() and join_hist() are the same exact
combinatorial routines as in code/out/n3_deduction_check.py.

n3 = number of unordered pairs of triangles joined by exactly 2 edges.
Reuses the existing triangles()/join_hist() logic verbatim.

The (33,12,1,6) infeasibility re-check imports the exact multiplicity-
integrality oracle srg_feasibility from code/out/check_srg33_12_1_6.py.

NO v=99 conclusion is drawn anywhere: the n3 values are computed facts about
the four named graphs only.
"""
import numpy as np
from itertools import combinations
from collections import Counter
from lib.srg import rook, doily, gq24_graph, bvls_graph, is_srg
from check_srg33_12_1_6 import srg_feasibility


def triangles(A):
    """List of all triangles (3-cliques) as frozensets, exact brute force."""
    n = A.shape[0]
    tris = []
    for i, j, l in combinations(range(n), 3):
        if A[i, j] and A[i, l] and A[j, l]:
            tris.append(frozenset((i, j, l)))
    return tris


def join_hist(A, tris):
    """Histogram: number of triangle pairs joined by exactly e edges."""
    n = A.shape[0]
    A = np.asarray(A)
    hist = Counter()
    for a, b in combinations(tris, 2):
        e = 0
        for x in a:
            for y in b:
                if A[x, y]:
                    e += 1
        hist[e] += 1
    return hist


def main():
    print("# Ran: python3 code/out/n3_four_graphs.py")
    print("# Oracle: exact integer common-neighbour / join-edge counting over lib.srg")
    print("#   adjacency matrices (no floats); entry guard = lib.srg.is_srg PASS on each.")
    print("# Inputs: the four known lambda=1 SRGs rook(3), doily, GQ(2,4), BvLS;")
    print("#   plus exact srg_feasibility re-check of (33,12,1,6).")
    print("# Computed only: T and n3 on the four named graphs + (33,12,1,6) feasibility.")
    print("# NO v=99 conclusion drawn. n3 values are facts about THESE graphs only.")
    print()

    cases = [
        ("rook(3)  srg(9,4,1,2)",   rook(3),       9, 4, 1, 2),
        ("doily    srg(15,6,1,3)",  doily(),       15, 6, 1, 3),
        ("GQ(2,4)  srg(27,10,1,5)", gq24_graph(),  27, 10, 1, 5),
        ("bvls     srg(243,22,1,2)", bvls_graph(), 243, 22, 1, 2),
    ]

    print("  graph            |  v   k | T (triangles) | n3 (pairs joined by exactly 2 edges)")
    print("  " + "-" * 80)
    results = {}
    for name, A, v, k, lam, mu in cases:
        A = np.asarray(A)
        ok, detail = is_srg(A, v, k, lam, mu)   # entry guard
        assert ok, f"ENTRY GUARD FAILED for {name}: {detail}"
        tris = triangles(A)
        T = len(tris)
        hist = join_hist(A, tris)
        n3 = hist.get(2, 0)
        total = sum(hist.values())
        results[name] = (T, n3, dict(sorted(hist.items())))
        exp_T = v * k // 6
        assert T == exp_T, f"{name}: T={T} but vk/6={exp_T}"
        assert total == T * (T - 1) // 2, f"{name}: histogram incomplete"
        print(f"  {name:16s} | {v:>3} {k:>2} | {T:>10}      | {n3:>6}    hist {dict(sorted(hist.items()))}")
    print()

    print("# (33,12,1,6) infeasibility re-check (exact multiplicity integrality):")
    res = srg_feasibility(33, 12, 1, 6)
    print(f"  srg(33,12,1,6): {res['verdict']} by {res['mechanism']}: {res['detail']}")
    print()

    print("# VERDICT on n3 >= 1 for the four known lambda=1 SRGs:")
    any_n3 = any(n3 >= 1 for (T, n3, h) in results.values())
    print("  known lambda=1 SRG with n3 >= 1:", any_n3)
    if not any_n3:
        print("  Both rook(3), doily, GQ(2,4), and BvLS have n3 = 0.")
        print("  (Note: these are n3=0, so they cannot REFUTE an n3>=1-forcing")
        print("  argument for a putative (99,14,1,2): none is a positive control.)")
    print("  NO v=99 conclusion is drawn from these n3 values.")
    # independently list the four (T,n3)
    print()
    print("# Four (T, n3) values:")
    for name, (T, n3, h) in results.items():
        print(f"  {name:16s}  T={T}, n3={n3}")


if __name__ == "__main__":
    main()
