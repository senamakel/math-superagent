"""Forced-vs-free census of the outer pair-label graph H on both controls.

For a fixed vertex 0, N(0)=7K2 matching, outer vertices = non-matching pairs.
The outer-pair rule (edge/nonedge) is fully determined by the intersection s of
the two pair labels, EXCEPT it depends on whether u~w. We ask: how much of the
adjacency of H is combinatorially FORCED by local degree/rule constraints, and
how much is genuinely free real structure.

We report, exhaustively over all outer pairs {u,w}:
  * the s-values present (share 0 or 1 elements) -- 2-element pairs never share
    2 because both are non-matching (no pair contains a matched edge).
  * the actual adjacency matrix of H restricted to outer vertices,
  * the density by s-value (fraction of adjacency among pairs sharing s),
  * whether the edge/nonedge counts per s are constant across roots.
This quantifies the "manual" freedom in H that the reduction must saturate.
"""
import numpy as np
from lib.srg import is_srg, rook, bvls_graph


def outer_census(A, zero):
    n = A.shape[0]
    k = int(A[zero].sum())
    N = [i for i in range(n) if A[zero, i] == 1]
    matching, remaining = [], set(N)
    while remaining:
        a = min(remaining)
        remaining.discard(a)
        b = [c for c in N if c != a and A[a, c] == 1]
        assert len(b) == 1
        b = b[0]
        remaining.discard(b)
        matching.append(tuple(sorted((a, b))))
    outer = [i for i in range(n) if i != zero and A[zero, i] == 0]
    pair = {u: frozenset(x for x in N if A[u, x] == 1) for u in outer}
    stats = {s: [0, 0] for s in (0, 1)}   # [edge cnt, total cnt] by s
    for i, u in enumerate(outer):
        for j, w in enumerate(outer):
            if i >= j:
                continue
            s = len(pair[u] & pair[w])
            stats[s][1] += 1
            stats[s][0] += int(A[u, w])
    return k, len(outer), stats, len(matching)


def run(name, A, v, k, lam, mu):
    ok, _ = is_srg(A, v, k, lam, mu)
    assert ok
    A = np.asarray(A, dtype=np.int64)
    for fixed in (0, 1, A.shape[0] // 2, A.shape[0] - 1):
        k_, M, stats, nm = outer_census(A, fixed)
        line = ", ".join(f"s={s}: edges {c[0]}/{c[1]} "
                         f"({100.0*c[0]/c[1]:.1f}%)" for s, c in sorted(stats.items()))
        tot_e = sum(c[0] for c in stats.values())
        tot = sum(c[1] for c in stats.values())
        print(f"[{name}] root {fixed}: k={k_}, M={M} outer, {nm} matched pairs | {line} "
              f"| total H-adj {tot_e}/{tot} = {100.0*tot_e/tot:.1f}%")


if __name__ == "__main__":
    print("rook(3):")
    run("rook", rook(3), 9, 4, 1, 2)
    print("bvls_graph():")
    run("bvls", bvls_graph(), 243, 22, 1, 2)
