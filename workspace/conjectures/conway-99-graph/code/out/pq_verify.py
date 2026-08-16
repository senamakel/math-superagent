"""Adopted-but-never-run first step of approach pq-2-6-2-classification.

Pin the partial-quadrangle reformulation onto the four controls. A lambda=1 SRG
is (conditionally) the collinearity graph of a partial quadrangle PQ(s,t,mu):
the 3-cliques (triangles) are the lines, a line has s+1 = 3 points so s = 2, and
the axioms are (a) diamond-free (no two lines share more than one point; no two
triangles share an edge), (b) each point on exactly t+1 lines, (c) every pair of
non-collinear (= non-adjacent) points meets in exactly mu common collinear
neighbours. For lambda=1 the mu common collinear neighbours of a non-adjacent
pair coincide with its mu common neighbours (a common neighbour z adjacent to x
always shares a triangle with x, since the edge xz lies in a unique triangle),
so axiom (c) reduces to the ordinary SRG mu count.

Expected (s,t,mu) on the four controls, and what 99 sits at:
    rook(3)  srg(9,4,1,2)    -> (2,1,2)   t+1 = k/2 = 2 -> t = 1
    doily     srg(15,6,1,3)   -> (2,2,3)   t+1 = 3 -> t = 2
    GQ(2,4)   srg(27,10,1,5)  -> (2,4,5)   t+1 = 5 -> t = 4
    bvls      srg(243,22,1,2) -> (2,10,2)  t+1 = 11 -> t = 10
    (hypothetical 99)         -> (2,6,2)   t+1 = 7 -> t = 6  (sits between t=1, t=10)

Exact integer arithmetic throughout. Everything re-derived from the adjacency
matrix; no floats.
"""
import time

import numpy as np

from lib.srg import is_srg, rook, doily, gq24_graph, bvls_graph


def triangles(A):
    """All 3-cliques of the 0/1 adjacency matrix A as a set of frozensets.

    Enumerate by pivoting on each vertex i and scanning pairs of its neighbours
    (j,k) that are adjacent to each other. Each triangle found 3 times; the set
    dedupes. Exact integer, O(sum_v deg(v)^2) time, O(#triangles) space.
    """
    n = A.shape[0]
    Aadj = A.astype(bool)
    tris = set()
    for i in range(n):
        nb = [j for j in range(n) if Aadj[i, j]]
        for a in range(len(nb)):
            for b in range(a + 1, len(nb)):
                j, k = nb[a], nb[b]
                if Aadj[j, k]:
                    tris.add(frozenset((i, j, k)))
    return tris


def partial_quadrangle_axioms(A):
    """Check the three partial-quadrangle axioms on the triangle-lines and report (s,t,mu).

    Treat the triangles of A as the lines of a partial linear space (s+1 = 3
    points per line, so s = 2). Returns dict with booleans diamond_ok (a),
    replicate_ok + t (b), mu_ok + mu (c), plus the list of lines-through counts.
    """
    n = A.shape[0]
    Aadj = A.astype(bool)
    Aint = Aadj.astype(np.int64)
    tris = triangles(A)
    T = sorted(map(tuple, sorted(tris)))  # deterministic order

    # (a) diamond-free: no two distinct lines (triangles) share more than one
    # point. Two triangles sharing 2 points share an edge; every edge in a
    # triangle is its unique triangle iff each edge belongs to exactly one
    # triangle. Both statements are the same; check line-line intersections
    # directly (cheap on pairs of triangles).
    diamond_ok = True
    shared_edge_dup = 0
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            inter = len(set(T[i]) & set(T[j]))
            if inter > 1:
                diamond_ok = False
                shared_edge_dup += 1
    # also: each point lies on lines; line count (b)
    lines_thru = [0] * n
    for tri in T:
        for v in tri:
            lines_thru[v] += 1
    distinct_counts = sorted(set(lines_thru))
    replicate_ok = len(distinct_counts) == 1
    t_plus_1 = distinct_counts[0] if distinct_counts else 0
    t = t_plus_1 - 1
    s = 2

    # (c) every non-collinear (= non-adjacent) pair has exactly mu common
    # collinear neighbours = mu common neighbours (argued above); count common
    # neighbours over non-adjacent pairs and require it constant.
    A2 = Aint @ Aint  # A2[x,y] = number of common neighbours of x,y (exact int)
    I = np.eye(n, dtype=np.int64)
    off = ~I.astype(bool)
    nonadj = (~Aadj) & off
    nonadj_vals = A2[nonadj]
    mu_ok = len(set(nonadj_vals.tolist())) == 1
    mu = int(nonadj_vals[0])

    return {
        "triangles": len(T),
        "diamond_ok": diamond_ok,
        "shared_edge_dups": shared_edge_dup,
        "lines_thru_distinct": distinct_counts,
        "replicate_ok": replicate_ok,
        "s": s, "t": t,
        "mu_ok": mu_ok, "mu": mu,
    }


def vertex_condition_4(A):
    """Verify the 4-vertex condition / c7 and the vertex-level diamond-free facts.

    Returns dict:
      - c7_ok: the two common neighbours of any non-adjacent pair are mutually
        non-adjacent (alpha=beta=0).
      - neighbourhoods_union_of_cliques: each induced neighbourhood N(v) is a
        disjoint union of cliques (no induced P3 inside any neighbourhood).
      - no_K4e: no induced diamond anywhere (= no two triangles share an edge,
        which is the vertex-level diamond-free statement; recorded verbatim).
    """
    n = A.shape[0]
    Aadj = A.astype(bool)
    Aint = Aadj.astype(np.int64)
    I = np.eye(n, dtype=np.int64)
    off = ~I.astype(bool)

    A2 = Aint @ Aint
    nonadj = (~Aadj) & off

    # c7: for each non-adjacent pair (x,y), the common neighbours must be
    # pairwise non-adjacent. Since mu is tiny, check pairwise non-adjacency of
    # the common-neighbour set directly.
    c7_ok = True
    bad = 0
    xidx, yidx = np.nonzero(nonadj)
    for x, y in zip(xidx, yidx):
        cn = [i for i in range(n) if Aint[x, i] and Aint[y, i]]
        for a in range(len(cn)):
            for b in range(a + 1, len(cn)):
                if Aint[cn[a], cn[b]]:
                    c7_ok = False
                    bad += 1
    # (c7 needs only to look at each unordered non-adjacent pair once; the
    # loop over all (x,y) treats pairs twice, which only double-counts `bad`.)

    # neighbourhood disjoint union of cliques: for each v, induced N(v) has no
    # induced P3 (is a union of cliques).
    union_ok = True
    for v in range(n):
        nb = [i for i in range(n) if Aint[v, i]]
        sub = Aint[np.ix_(nb, nb)]
    # union of cliques iff no induced P3 iff for every edge (a,b) in sub,
    # the CLOSED neighbourhoods of a and b within nb are equal (a~c iff b~c
    # for every c != a,b). Compare (sub + I) rows so the edge endpoints are
    # counted symmetrically.
    closed = sub + np.eye(len(nb), dtype=np.int64)
    for a in range(len(nb)):
        for b in range(a + 1, len(nb)):
            if sub[a, b]:
                if not np.array_equal(closed[a], closed[b]):
                    union_ok = False
    return {"c7_ok": c7_ok, "c7_bad_pairs": bad, "union_of_cliques_ok": union_ok}


def no_K4e(A):
    """Global no-induced-diamond check == no two triangles share an edge.

    A diamond (K4 - e) is exactly two triangles sharing a common edge, so
    diamond-free (already checked as axiom (a)) is equivalent to no induced
    K4-e. Re-derived independently here by scanning each edge's triangles.
    """
    Aadj = A.astype(bool)
    n = A.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if not Aadj[i, j]:
                continue
            # common neighbours throught the edge ij -> triangles on ij
            cn = [k for k in range(n) if Aadj[i, k] and Aadj[j, k]]
            if len(cn) > 1:
                return False, (i, j, cn)
    return True, None


def run_control(name, A, params, expected_tsm):
    v, k, lam, mu = params
    ok, msg = is_srg(A, v, k, lam, mu)
    print(f"--- {name}  srg({v},{k},{lam},{mu}) ---")
    print(f"  guard is_srg(v,k,lam,mu): {'PASS' if ok else 'FAIL'}  ({msg})")
    if not ok:
        print(f"  SKIPPED axioms (guard failed); expected (s,t,mu)={expected_tsm}")
        return
    r = partial_quadrangle_axioms(A)
    print(f"  triangles (lines): {r['triangles']}   (expected v*k/6 "
          f"= {v * k // 6})")
    print(f"  (a) diamond-free (no two lines share >1 pt): "
          f"{'PASS' if r['diamond_ok'] else 'FAIL  shared-edge dups=%d' % r['shared_edge_dups']}")
    print(f"  (b) lines through each point constant = {r['lines_thru_distinct']}: "
          f"{'PASS' if r['replicate_ok'] else 'FAIL'}")
    print(f"  (c) non-collinear pairs have mu={r['mu']} common collinear "
          f"neighbours constant: {'PASS' if r['mu_ok'] else 'FAIL'}")
    got = (r['s'], r['t'], r['mu'])
    match = got == expected_tsm
    print(f"  derived (s,t,mu) = {got}  expected {expected_tsm}: "
          f"{'MATCH' if match else 'MISMATCH'}")
    vc = vertex_condition_4(A)
    print(f"  4-vertex c7 (common nbrs of non-adj pair non-adj): "
          f"{'PASS' if vc['c7_ok'] else 'FAIL  bad pairs=%d' % vc['c7_bad_pairs']}")
    print(f"  each neighbourhood disjoint union of cliques: "
          f"{'PASS' if vc['union_of_cliques_ok'] else 'FAIL'}")
    k4e, where = no_K4e(A)
    print(f"  no induced K4-e (diamond): {'PASS' if k4e else 'FAIL at ' + str(where)}")
    all_pass = (ok and r['diamond_ok'] and r['replicate_ok'] and r['mu_ok']
                and match and vc['c7_ok'] and vc['union_of_cliques_ok'] and k4e)
    print(f"  ALL GUARDS + AXIOMS PASS: {all_pass}")
    print()
    return all_pass


def main():
    t0 = time.time()
    print("# Ran: python3 code/out/pq_verify.py")
    print("# Oracle: lib.srg.is_srg (exact integer common-neighbour counts via A@A) "
          "guards each control on its own parameters before any axiom is checked.")
    print("# Search space: the four controls' triangle-lines and pairwise "
          "intersections (6, 15, 45, 891 triangles), all common-neighbour and "
          "neighbourhood checks, exact; NO enumeration up to any bound. All four "
          "expected (s,t,mu): (2,1,2),(2,2,3),(2,4,5),(2,10,2); hypothetical "
          "(99,14,1,2) -> (2,6,2).")
    print()
    controls = [
        ("rook(3)", rook(3), (9, 4, 1, 2), (2, 1, 2)),
        ("doily", doily(), (15, 6, 1, 3), (2, 2, 3)),
        ("GQ(2,4)", gq24_graph(), (27, 10, 1, 5), (2, 4, 5)),
        ("bvls", bvls_graph(), (243, 22, 1, 2), (2, 10, 2)),
    ]
    results = []
    for name, A, params, exp in controls:
        results.append(run_control(name, A, params, exp))
    print("=" * 72)
    print("SUMMARY (s,t,mu):")
    for (name, A, params, exp), ok in zip(controls, results):
        print(f"  {name:10s} srg{params}  declared {exp}  all-pass={ok}")
    print(f"\nhypothetical (99,14,1,2) sits at (2, t=6, mu=2), between t=1 "
          f"(rook) and t=10 (bvls).")
    print(f"wall-clock: {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
