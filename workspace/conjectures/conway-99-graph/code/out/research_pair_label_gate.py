"""Admissibility gate for approach pair-labeling-84-vertex (candidate #2).

For any srg(v,k,1,2) fix vertex 0 with N(0) a perfect matching of k/2 edges.
Claim: (a) every outer vertex has exactly 2 neighbours in N(0); (b) outer
vertices are in bijection with the C(k,2)-k/2 non-matching pairs of N(0);
(c) the outer-outer induced graph H is (k-2)-regular on M = C(k,2)-k/2
vertices; (d) the pair-adjacency rule (forced-structure-reduction preprint
Sec. 4): for outer u,v with labels P_u,P_v and s=|P_u∩P_v| in {0,1},
  if u~v then the number of common OUTER neighbours equals 1-s,
  else equals 2-s;
and for inner a, outer u: if a in P_u then exactly one outer neighbour of u
contains a; if a not in P_u then [m(a) in P_u] + #{outer neighbours of u
containing a} = 2, where m(a) is the matched partner of a.

Checks (a)-(d) exactly on both controls rook(3)=srg(9,4,1,2) and
bvls_graph()=srg(243,22,1,2) through lib.srg. Exact integer arithmetic only.
"""
import itertools
import numpy as np
from lib.srg import is_srg, rook, bvls_graph


def matching_pairs(N_list):
    """N_list = list of neighbours of 0; N(0) induces a perfect matching.
    Return the k/2 matched 2-subsets."""
    k = len(N_list)
    Nset = set(N_list)
    pairs = []
    remaining = set(N_list)
    while remaining:
        a = min(remaining)
        remaining.discard(a)
        # partner: the unique neighbour of a within N(0)
        b = None
        for c in N_list:
            if c != a and c != 0 and c in remaining and a in adj_set.get(c, set()):
                # need actual adjacency; use the graph
                pass
        # simpler: partner = unique vertex in N(0) adjacent to a
        partner = [c for c in N_list if c != a and A[a, c] == 1]
        assert len(partner) == 1, f"a={a} has {len(partner)} neighbours in N(0)"
        b = partner[0]
        assert b in remaining
        remaining.discard(b)
        pairs.append(tuple(sorted((a, b))))
    return pairs


def run(name, A, v, k, lam, mu):
    ok, msg = is_srg(A, v, k, lam, mu)
    assert ok, f"{name}: oracle says {msg}"
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    for fixed in (0, 1, n // 2, n - 1):  # several roots for robustness
        report = gate_at(A, fixed)
        print(f"[{name}] root {fixed}: {report}")


def gate_at(A, zero):
    n = A.shape[0]
    k = int(A[zero].sum())
    N = [i for i in range(n) if A[zero, i] == 1]
    assert len(N) == k
    # lambda=1 => N(0) induces a perfect matching: every neighbour has exactly
    # one neighbour inside N(0)
    for a in N:
        inside = sum(1 for b in N if A[a, b] == 1)
        assert inside == 1, f"root {zero}: neighbour {a} has {inside} inside-neighbours"

    # (a) outer vertices have exactly 2 neighbours in N(0)
    outer = [i for i in range(n) if i != zero and A[zero, i] == 0]
    for u in outer:
        cnt = sum(1 for a in N if A[u, a] == 1)
        assert cnt == 2, f"root {zero}: outer {u} has {cnt} neighbours in N(0)"

    # (b) bijection with non-matching pairs
    pairs = []
    remaining = set(N)
    matching = []
    while remaining:
        a = min(remaining)
        remaining.discard(a)
        b = [c for c in N if c != a and A[a, c] == 1]
        assert len(b) == 1
        b = b[0]
        assert b in remaining
        remaining.discard(b)
        matching.append(tuple(sorted((a, b))))
    M = k // 2
    all_pairs = set(itertools.combinations(N, 2))
    nonmatch = sorted(all_pairs - set(matching))
    assert len(nonmatch) == k * (k - 1) // 2 - k // 2, (
        f"root {zero}: expected {k*(k-1)//2 - k//2} non-matching pairs, got {len(nonmatch)}")
    # map each outer vertex to its pair
    pair_of = {}
    for u in outer:
        ns = tuple(sorted(a for a in N if A[u, a] == 1))
        pair_of[u] = ns
        assert ns in set(nonmatch), f"root {zero}: outer {u} labelled by matched pair {ns}?"
    assert len(set(pair_of.values())) == len(outer) == len(nonmatch), (
        f"root {zero}: pair bijection failed ({len(set(pair_of.values()))} distinct labels "
        f"for {len(outer)} outer vertices, {len(nonmatch)} expected)")

    # (c) outer-outer graph H is (k-2)-regular
    Hadj = np.zeros((len(outer), len(outer)), dtype=np.int64)
    oidx = {u: i for i, u in enumerate(outer)}
    degs = []
    for i, u in enumerate(outer):
        d = 0
        for j, w in enumerate(outer):
            if A[u, w] == 1:
                Hadj[i, j] = 1
                d += 1
        degs.append(d)
    assert all(d == k - 2 for d in degs), (
        f"root {zero}: outer degrees {sorted(set(degs))} vs expected {k-2}")

    # (d) pair-adjacency rule: common OUTER neighbours
    Av = dict()  # (i,j) -> bool inside H
    for i, u in enumerate(outer):
        for j, w in enumerate(outer):
            Av[(i, j)] = bool(A[u, w])
    matching_set = set(matching)
    bad_edge, bad_nonedge = [], []
    for i, u in enumerate(outer):
        for j, w in enumerate(outer):
            if i >= j:
                continue
            s = len(set(pair_of[u]) & set(pair_of[w]))
            assert s in (0, 1), f"root {zero}: pairs share {s} elements"
            common = sum(1 for t in outer if A[u, t] == 1 and A[w, t] == 1)
            want = 1 - s if Av[(i, j)] else 2 - s
            if common != want:
                (bad_edge if Av[(i, j)] else bad_nonedge).append((i, j, s, common, want))
    # inner-outer rule
    bad_inner = []
    mate = {}
    for a, b in matching:
        mate[a] = b
        mate[b] = a
    for a in N:
        for u in outer:
            pu = set(pair_of[u])
            cont = sum(1 for t in outer if A[a, t] == 1 and t in pu)
            if a in pu:
                want = 1
                if cont != want:
                    bad_inner.append((a, u, "in", cont, want))
            else:
                want = 2 - (1 if mate[a] in pu else 0)
                if cont != want:
                    bad_inner.append((a, u, "out", cont, want))
    n_bad = len(bad_edge) + len(bad_nonedge) + len(bad_inner)
    return (f"k={k}, M={len(outer)} outer, H {k-2}-regular OK, pair-bijection OK, "
            f"pair-rule violations edge={len(bad_edge)} nonedge={len(bad_nonedge)} "
            f"inner={len(bad_inner)} => {'ALL RULES HOLD' if n_bad == 0 else f'{n_bad} VIOLATIONS'}")


if __name__ == "__main__":
    print("rook(3) = srg(9,4,1,2):")
    run("rook", rook(3), 9, 4, 1, 2)
    print()
    print("bvls_graph() = srg(243,22,1,2):")
    run("bvls", bvls_graph(), 243, 22, 1, 2)