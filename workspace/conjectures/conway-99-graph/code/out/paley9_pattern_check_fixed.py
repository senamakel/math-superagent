"""Corrected check of Keramatipour Lemma 3.4.1: the Paley(9) local pattern.

Original code/out/paley9_pattern_check.py hardcoded len(matching)==7, which is
the 99-graph local structure (k=14 -> 7K2). For BvLS (243,22,1,2) the
neighbourhood of every vertex is a perfect matching on 22 vertices = 11 K2.

Pattern under test (Paley(9) pattern): for every vertex v and every two matched
edges {v1,v2},{v3,v4} of the perfect matching in N(v), the induced subgraph on
the 9 vertices
    P_v = { v, v1,v2,v3,v4, (v1,v3), (v1,v4), (v2,v3), (v2,v4) }
is a Paley(9) graph = rook(3) = srg(9,4,1,2), where (a,b) is the unique common
neighbour of the non-adjacent pair a,b that is not v.

This is an exactly checkable finite claim:
  rook(3):  9 vertices x C(2,2)=1 pair                = 9 configs
  BvLS:   243 vertices x C(11,2)=55 pairs             = 13365 configs
exact integer arithmetic via lib.srg.is_srg on induced subgraphs against
(9,4,1,2). No floats anywhere.

A FAILURE on BvLS refutes the pattern for the existing in-family member
(243,22,1,2): any 99-nonexistence argument built on the Paley(9) pattern would
then be refuted on arrival (like g-reduce). Success on BvLS leaves it a genuine
candidate local structure shared by the family.

Run: python3 code/out/paley9_pattern_check_fixed.py
"""
import numpy as np
from lib.srg import bvls_graph, rook, is_srg


def check(graph_builder, name):
    A = graph_builder()
    n = A.shape[0]
    stars = {v: set(int(x) for x in np.flatnonzero(A[v])) for v in range(n)}

    total_cfgs = 0
    failures = []  # (kind, v, e1, e2, detail)

    for v in range(n):
        nbrs = stars[v]
        # Perfect matching in N(v): each x in N(v) has exactly one neighbour in
        # N(v) (lambda=1 on edge v-x: the unique common neighbour of v,x).
        matching = []
        used = set()
        for x in sorted(nbrs):
            if x in used:
                continue
            cn = [y for y in nbrs if y != x and A[x, y] == 1]
            if len(cn) != 1:
                failures.append(("matching-degenerate", v, None, None,
                                 f"x={x} cn-in-N(v)={len(cn)}"))
                continue
            p = cn[0]
            matching.append((x, p))
            used.add(x)
            used.add(p)
        # no v-specific size assertion: matching size = k/2 is data
        if len(matching) * 2 != len(nbrs):
            failures.append(("matching-incomplete", v, None, None,
                             f"{len(matching)} edges on {len(nbrs)} nbrs"))

        for i1 in range(len(matching)):
            for i2 in range(i1 + 1, len(matching)):
                v1, v2 = matching[i1]
                v3, v4 = matching[i2]
                total_cfgs += 1

                verts = {v, v1, v2, v3, v4}
                for pair in ((v1, v3), (v1, v4), (v2, v3), (v2, v4)):
                    a, b = pair
                    cns = [c for c in range(n) if A[a, c] and A[b, c]]
                    others = [c for c in cns if c != v]
                    if len(others) != 1:
                        failures.append(("cn-count", v, (v1, v2), (v3, v4),
                                         f"pair {pair} has {len(others)} non-v "
                                         f"common neighbours"))
                        break
                    verts.add(others[0])
                if len(verts) != 9:
                    failures.append(("size", v, (v1, v2), (v3, v4), len(verts)))
                    continue

                V = list(verts)
                idx = {x: t for t, x in enumerate(V)}
                sub = np.zeros((9, 9), dtype=np.int64)
                for x in V:
                    for y in V:
                        if x != y and A[x, y]:
                            sub[idx[x], idx[y]] = 1
                ok, detail = is_srg(sub, 9, 4, 1, 2)
                if not ok:
                    failures.append(("not-paley9", v, (v1, v2), (v3, v4), detail))

    return name, n, total_cfgs, failures


if __name__ == "__main__":
    for builder, nm in ((lambda: rook(3), "rook(3)=srg(9,4,1,2)"),
                        (bvls_graph, "BvLS=srg(243,22,1,2)")):
        name, n, total, fails = check(builder, nm)
        print(f"[{name}] n={n} vertices, {total} Paley(9)-pattern "
              f"configurations checked")
        if not fails:
            print(f"[{name}] ALL configurations are Paley(9): "
                  f"Lemma 3.4.1 pattern CONFIRMED (checked).")
        else:
            print(f"[{name}] FAILURES: {len(fails)}")
            for f in fails[:10]:
                print("   ", f)