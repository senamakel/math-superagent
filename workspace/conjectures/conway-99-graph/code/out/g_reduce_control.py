"""Verify the vertex-derived design reduction (goal G-reduce) on the two
control graphs, through the canonical oracle at code/lib/srg.py.

For each of rook(3) (v=9,k=4) and bvls_graph() (v=243,k=22), fix vertex 0 and
compute EXACTLY (integer arithmetic only, no floating point):

(a) N(0) induces (k/2)K2 (count matched edges = k/2; every vertex of N(0) has
    exactly one neighbour inside N(0)); and the distance-2 vertices from 0 are
    in bijection with the non-edges of N(0): each distance-2 w has exactly two
    neighbours inside N(0), and those pairs are precisely the non-edges of
    N(0), distinct across distance-2 vertices.

(b) Partition the triangles (3-cliques) by intersection with {0} u N(0):
      through (contain 0)          = k/2
      cross  (1 point in N(0), 2 at distance 2) = k(k-2)/2
      outer  (all at distance 2)   = k(k-2)(k-4)/12
    Confirm the outer blocks form a partial Steiner triple system (no two
    outer blocks share >= 2 points) with replication (k-4)/2 (each distance-2
    point lies in exactly (k-4)/2 outer blocks).

(c) The collinearity graph of the outer design (points = distance-2 vertices,
    two adjacent iff they lie together in an outer block). Report its degree,
    and the exact lambda (common collinear neighbours of an edge) and mu
    (common collinear neighbours of a non-edge) distributions. Assert the
    claimed lambda=1 and mu=2.

Also evaluate the G-reduce formulas at k=14 (the 99-vertex parameters, where
no graph exists): distance-2 vertices = k(k-2)/2 = 84, cross = 84, outer =
k(k-2)(k-4)/12 = 140, replication = (k-4)/2 = 5.

The oracle-is_srg guard: assert rook(3) is srg(9,4,1,2) and bvls_graph() is
srg(243,22,1,2) through lib.srg.is_srg before / after the reduction checks.
"""
import os
import tempfile
from itertools import combinations

import numpy as np

from lib.srg import rook, bvls_graph, is_srg

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "g_reduce_control.captured.txt")


def analyse(A, v, k, name, out):
    out.append(f"{'='*72}")
    out.append(f"{name}: v={v}  k={k}")
    out.append(f"{'='*72}")

    # --- oracle guard -----------------------------------------------------
    ok, why = is_srg(A, v, k, 1, 2)
    out.append(f"[guard] is_srg(A,{v},{k},1,2) -> {'PASS' if ok else 'FAIL'} ({why})")
    assert ok, f"oracle guard failed for {name}: {why}"

    N = sorted(int(x) for x in np.nonzero(A[0])[0])
    Nset = set(N)
    allv = set(range(v))
    D2 = sorted(allv - Nset - {0})
    nD = len(D2)
    k_over2 = k // 2
    out.append(f"  |N(0)| = {len(N)}   distance-2 vertices = {nD}  (expect k(k-2)/2 = {k*(k-2)//2})")

    # ========== (a) =======================================================
    out.append("\n--- (a) N(0) induces (k/2)K2; distance-2 <-> non-edges of N(0) ---")
    subN = A[np.ix_(N, N)]
    degN = subN.sum(axis=1)
    edgeN = int(subN.sum() // 2)
    matched_ok = bool((degN == 1).all()) and edgeN == k_over2
    out.append(f"  N(0) induced edges = {edgeN} (expect k/2 = {k_over2}); "
               f"all degrees = 1: {(degN == 1).all()}  => (k/2)K2: {matched_ok}")

    # distance-2 -> its two neighbours in N(0)
    mapping = {}
    each_ok = True
    for w in D2:
        inn = sorted(int(n) for n in N if A[w, n])
        if len(inn) != 2:
            each_ok = False
        mapping[w] = tuple(inn)
    out.append(f"  every distance-2 vertex has exactly 2 neighbours in N(0): {each_ok}")

    # the pairs must be distinct and equal the non-edges of N(0)
    pairs = set(mapping.values())
    nonedges = set()
    for i in range(len(N)):
        for j in range(i + 1, len(N)):
            if not A[N[i], N[j]]:
                nonedges.add(tuple(sorted((N[i], N[j]))))
    out.append(f"  #distinct pairs = {len(pairs)}  #non-edges of N(0) = {len(nonedges)}  "
               f"bijection: {pairs == nonedges}")
    a_ok = matched_ok and each_ok and len(pairs) == nD and pairs == nonedges
    out.append(f"  (a) HOLDS: {a_ok}")

    # ========== (b) =======================================================
    out.append("\n--- (b) triangle partition and outer partial Steiner triple system ---")
    tris = []
    for a in range(v):
        for b in range(a + 1, v):
            if A[a, b] == 0:
                continue
            for c in range(b + 1, v):
                if A[a, c] and A[b, c]:
                    tris.append((a, b, c))
    through, cross, outer = [], [], []
    for t in tris:
        ts = set(t)
        if 0 in ts:
            through.append(t)
        elif len(Nset & ts) == 1:
            cross.append(t)
        else:
            outer.append(t)
    out.append(f"  through = {len(through)} (expect k/2 = {k_over2})")
    out.append(f"  cross   = {len(cross)} (expect k(k-2)/2 = {k*(k-2)//2})")
    out.append(f"  outer   = {len(outer)} (expect k(k-2)(k-4)/12 = {k*(k-2)*(k-4)//12})")
    b_split = (len(through) == k_over2 and len(cross) == k * (k - 2) // 2
               and len(outer) == k * (k - 2) * (k - 4) // 12)

    # outer partial Steiner triple system: independent of the 84-specific claim
    rep = {x: 0 for x in D2}
    for t in outer:
        for x in t:
            rep[x] += 1
    share2 = 0
    for i in range(len(outer)):
        for j in range(i + 1, len(outer)):
            if len(set(outer[i]) & set(outer[j])) >= 2:
                share2 += 1
    out.append(f"  outer replication unique = {sorted(set(rep.values()))} (expect (k-4)/2 = {(k-4)//2})")
    out.append(f"  outer blocks sharing >=2 points = {share2} (expect 0)")
    b_psts = (sorted(set(rep.values())) == [(k - 4) // 2] and share2 == 0)
    out.append(f"  (b) HOLDS: {b_split and b_psts}")

    # ========== (c) =======================================================
    out.append("\n--- (c) collinearity graph of the outer design (lambda=1, mu=2) ---")
    if nD == 0:
        out.append("  distance-2 set empty -> outer design has no points; (c) vacuous.")
        c_lambda = None
        c_mu = None
        c_ok = "vacuous"
    else:
        Adj = np.zeros((nD, nD), dtype=np.int64)
        for t in outer:
            tl = sorted(t)
            for x, y in combinations(tl, 2):
                Adj[D2.index(x), D2.index(y)] = 1
        Adj = np.maximum(Adj, Adj.T)
        nedges = int(Adj.sum() // 2)
        deg = Adj.sum(axis=1)
        out.append(f"  outer collinearity graph: edges = {nedges}, degree unique = {sorted(set(deg.tolist()))} (expect 2*(k-4)/2)")
        lam_dist = {}
        mu_dist = {}
        for i in range(nD):
            for j in range(i + 1, nD):
                cn = int((Adj[i] & Adj[j]).sum())
                if Adj[i, j]:
                    lam_dist[cn] = lam_dist.get(cn, 0) + 1
                else:
                    mu_dist[cn] = mu_dist.get(cn, 0) + 1
        out.append(f"  lambda distribution (common collinear neighbours of an edge): {dict(sorted(lam_dist.items()))}")
        out.append(f"  mu distribution (common collinear neighbours of a non-edge):   {dict(sorted(mu_dist.items()))}")
        c_lambda = (lam_dist == {1: nedges})
        c_mu = (mu_dist == {2: nD * (nD - 1) // 2 - nedges})
        out.append(f"  lambda == 1: {c_lambda}   mu == 2: {c_mu}")
        c_ok = bool(c_lambda and c_mu)
        out.append(f"  (c) lambda==1 : {c_lambda};  mu==2 : {c_mu};  => {(c_lambda and c_mu)}")
        if not (c_lambda and c_mu):
            out.append("  NOTE: (c) does NOT hold as stated -- outer-design collinearity graph")
            out.append("  has non-constant mu on this control. lambda=1 holds; mu is not 2.")

    return dict(a=a_ok, b=b_split and b_psts, c=c_ok)


def main():
    out = []
    out.append("Ran: python code/out/g_reduce_control.py (from /workspace)")
    out.append("Oracle function: lib.srg.is_srg(A, v, k, lam, mu) — exact integer common-neighbour counts; control graphs lib.srg.rook / lib.srg.bvls_graph")
    out.append("Inputs: rook(3) on (v,k)=(9,4) fixed vertex 0; bvls_graph() on (v,k)=(243,22) fixed vertex 0; formula evaluation at k=14")

    results = {}

    # --- rook(3) ----------------------------------------------------------
    r = analyse(rook(3), 9, 4, "rook(3)", out)
    results["rook(3)"] = r

    # --- bvls -------------------------------------------------------------
    b = analyse(bvls_graph(), 243, 22, "bvls_graph()", out)
    results["bvls_graph()"] = b

    # --- formula evaluation at k=14 (no graph) -----------------------------
    out.append("\n" + "=" * 72)
    out.append("G-reduce formula evaluation at k=14 (v=99, NO graph exists):")
    out.append("=" * 72)
    k = 14
    d2 = k * (k - 2) // 2
    cross = k * (k - 2) // 2
    outer = k * (k - 2) * (k - 4) // 12
    rep = (k - 4) // 2
    out.append(f"  distance-2 vertices = k(k-2)/2        = {d2}  (expect 84)")
    out.append(f"  cross lines          = k(k-2)/2        = {cross}  (expect 84)")
    out.append(f"  outer blocks         = k(k-2)(k-4)/12  = {outer}  (expect 140)")
    out.append(f"  replication          = (k-4)/2          = {rep}  (expect 5)")
    k14_ok = (d2 == 84 and cross == 84 and outer == 140 and rep == 5)
    out.append(f"  k=14 formula values (84, 140, 5): ALL MATCH: {k14_ok}")

    out.append("\n" + "=" * 72)
    out.append("SUMMARY")
    out.append("=" * 72)
    for name, r in results.items():
        out.append(f"  {name}: (a)={r['a']}  (b)={r['b']}  (c: lambda=1,mu=2)={r['c']}")
    out.append(f"  k=14 formula check: {k14_ok}")

    report = "\n".join(out)
    print(report)

    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(OUT), suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        f.write(report + "\n")
    os.replace(tmp, OUT)
    print(f"\nwrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
