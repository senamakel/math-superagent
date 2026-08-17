"""Refute or confirm Keramatipour Lemma 3.4.1: the Paley(9) pattern is present
in the Berlekamp-van Lint-Seidel graph srg(243,22,1,2).

Paley(9) pattern (Definition 12): for every vertex v and every two matched edges
{v1,v2},{v3,v4} of N(v) (the neighbourhood is a perfect matching 7K2), the induced
subgraph on the 9 vertices
    P_v = { v, v1,v2,v3,v4, (v1,v3), (v1,v4), (v2,v3), (v2,v4) }
is a Paley(9) graph (= rook(3) = srg(9,4,1,2)), where (a,b) is the common
neighbour of non-adjacent a,b that is NOT v.

This is an exactly checkable finite claim on the 243-vertex graph:
  243 vertices x C(7,2)=21 pairs of matching edges = 5103 configurations,
each on 9 vertices. Exact integer arithmetic via lib.srg.is_srg on the induced
subgraph against (9,4,1,2).

If even ONE configuration is not Paley(9), Lemma 3.4.1 is refuted -> the
Paley(9) pattern does NOT hold in BvLS.

Run: python3 code/out/paley9_pattern_check.py  (exact, no floats)
"""
import sys
import numpy as np
sys.path.insert(0, "/workspace/code") if False else None
from lib.srg import bvls_graph, is_srg


def paley9_pattern_check():
    A = bvls_graph()
    n = A.shape[0]
    stars = {v: set(int(x) for x in np.flatnonzero(A[v])) for v in range(n)}

    total_cfgs = 0
    failures = []  # (v, edge1, edge2, induced_is_srg, detail)

    for v in range(n):
        nbrs = stars[v]
        # perfect matching edges in N(v): each neighbour has exactly one common
        # neighbour inside N(v) (lambda=1 on edges of N(v)); build the edges.
        matching = []
        used = set()
        for x in sorted(nbrs):
            if x in used:
                continue
            # common neighbours of v (fixed) and x inside N(v): lambda=1 -> one
            common = [y for y in nbrs if y != x and A[x, y] == 1]
            # the unique matched partner is the common neighbour of v,x lying in N(v)
            # (v,x are adjacent so they share exactly ONE common neighbour (lambda=1))
            cn = [y for y in nbrs if y != x and A[x, y] == 1]
            # but x's neighbours in N(v) IS its matching partner exactly
            partner = cn
            if len(partner) == 1:
                p = partner[0]
                matching.append((x, p))
                used.add(x); used.add(p)
            else:
                raise RuntimeError(f"v={v} x={x} partner count {len(partner)}")

        if len(matching) != 7:
            raise RuntimeError(f"v={v}: matching has {len(matching)} edges, need 7")

        # pair up matching edges
        for i1 in range(len(matching)):
            for i2 in range(i1 + 1, len(matching)):
                e1 = matching[i1]  # {v1,v2}
                e2 = matching[i2]  # {v3,v4}
                v1, v2 = e1
                v3, v4 = e2
                total_cfgs += 1

                def cn_pair(a, b):
                    """common neighbours of non-adjacent a,b; exactly 2 (mu=2)."""
                    c = [x for x in range(n) if A[a, x] and A[b, x]]
                    return c

                # (a,b) = common neighbour of a,b other than v (for a,b non-adjacent
                # to each other, both in different matching edges).
                verts = {v, v1, v2, v3, v4}
                for pair in [(v1, v3), (v1, v4), (v2, v3), (v2, v4)]:
                    a, b = pair
                    cns = cn_pair(a, b)
                    # v is a common neighbour of a,b (all in N(v)); filter it out
                    others = [c for c in cns if c != v]
                    if len(others) != 1:
                        failures.append(("cn-count", v, e1, e2, a, b, len(others)))
                        continue
                    verts.add(others[0])
                if len(verts) != 9:
                    failures.append(("size", v, e1, e2, len(verts)))

                # build induced subgraph on verts
                V = list(verts)
                idx = {x: t for t, x in enumerate(V)}
                sub = np.zeros((9, 9), dtype=np.int64)
                for x in V:
                    for y in V:
                        if x != y and A[x, y]:
                            sub[idx[x], idx[y]] = 1
                ok, det = is_srg(sub, 9, 4, 1, 2)
                if not ok:
                    failures.append(("not-paley9", v, e1, e2, det))

    return total_cfgs, failures


if __name__ == "__main__":
    total, fails = paley9_pattern_check()
    print(f"total Paley(9)-pattern configurations checked on bvls: {total}")
    if not fails:
        print("ALL configurations are Paley(9): Lemma 3.4.1 CONFIRMED (checked).")
    else:
        print(f"FAILURES: {len(fails)}")
        for f in fails[:10]:
            print("  ", f)
        print("Lemma 3.4.1 REFUTED: the Paley(9) pattern does NOT hold in BvLS.")
