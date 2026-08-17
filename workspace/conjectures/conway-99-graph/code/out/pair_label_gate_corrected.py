"""Corrected admissibility gate for the pair-labeling-84-vertex reduction.

The on-disk gate (research_pair_label_gate.py) passed the outer pair rules
EXACTLY on both controls but reported 'inner' violations on every (a,u) pair —
16 on rook(3), 4840 on bvls. That is a code bug, not a refutation: it counts
`cont = sum(t in outer if A[a,t] and t in pu)` where `pu` is the pair-label
(a 2-subset of the neighbour set N), so `t in pu` is FALSE for every outer
vertex t (outer vertices never equal an element of N's label set) and cont is
always 0. The intended inner-outer rule counts outer neighbours of the *pair
of a* whose LABEL contains a. This file re-tests the inner rule correctly.

Rules under test (forced-structure-reduction / Keramatipour pair-rule, Sec 4):
  (edge)    two outer u~w with s=|P_u & P_w| in {0,1}: common OUTER nbrs = 1-s
  (nonedge) two outer u!~w:                          common OUTER nbrs = 2-s
  (inner)   inner a in N, outer u with label P_u:
              if a in P_u:  #{outer nbrs of u' whose label contains a} plus the
                            witness shared with u  => exactly 1 (u' adj to a)
              if a not in P_u: [m(a) in P_u] + #{outer nbrs of a containing a} = 2
where m(a) = matched partner of a inside the 7K2 matching N(0).
"""
import itertools
import numpy as np
from lib.srg import is_srg, rook, bvls_graph


def run(name, A, v, k, lam, mu):
    ok, msg = is_srg(A, v, k, lam, mu)
    assert ok, f"{name}: oracle says {msg}"
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    for fixed in (0, 1, n // 2, n - 1):
        report = gate_at(A, fixed)
        print(f"[{name}] root {fixed}: {report}")


def gate_at(A, zero):
    n = A.shape[0]
    k = int(A[zero].sum())
    N = [i for i in range(n) if A[zero, i] == 1]
    # build 7K2 matching of N(0)
    matching, remaining = [], set(N)
    while remaining:
        a = min(remaining)
        remaining.discard(a)
        b = [c for c in N if c != a and A[a, c] == 1]
        # lambda=1 => every N-neighbour has exactly 1 inside N-neighbour
        assert len(b) == 1
        b = b[0]
        assert b in remaining
        remaining.discard(b)
        matching.append(tuple(sorted((a, b))))
    # outer vertices, label = non-matching pair
    outer = [i for i in range(n) if i != zero and A[zero, i] == 0]
    pair_of = {}
    for u in outer:
        ps = tuple(sorted(x for x in N if A[u, x] == 1))
        pair_of[u] = ps
        assert tuple(sorted(ps)) not in matching

    # (edge)/(nonedge) outer pair rule
    bad_e, bad_ne = [], []
    for i, u in enumerate(outer):
        for j, w in enumerate(outer):
            if i >= j:
                continue
            s = len(set(pair_of[u]) & set(pair_of[w]))
            common = sum(1 for t in outer if A[u, t] == 1 and A[w, t] == 1)
            want = (1 - s) if A[u, w] else (2 - s)
            if common != want:
                (bad_e if A[u, w] else bad_ne).append((i, j, s, common, want))

    # (inner) corrected inner-outer rule
    mate = {}
    for a, b in matching:
        mate[a], mate[b] = b, a
    bad_in = []
    # labels contains predicate cached
    labels = {t: set(pair_of[t]) for t in outer}
    for a in N:
        for u in outer:
            pu = labels[u]
            # outer t with a in label(t) AND t adjacent to u (outer neighbour of
            # u in H whose label carries a): the common-neighbour contribution
            # over the outer set for the pair {a,u}.
            cont = sum(1 for t in outer
                       if A[u, t] == 1 and a in labels[t])
            if a in pu:
                want = 1
            else:
                want = 2 - (1 if mate[a] in pu else 0)
            if cont != want:
                bad_in.append((a, u, "in" if a in pu else "out", cont, want))
    tot = len(bad_e) + len(bad_ne) + len(bad_in)
    return (f"k={k}, M={len(outer)} outer, pair-bijection OK, "
            f"edge-viol={len(bad_e)} nonedge-viol={len(bad_ne)} "
            f"inner-viol={len(bad_in)} => {'ALL RULES HOLD' if tot == 0 else f'{tot} VIOL'}")


if __name__ == "__main__":
    print("rook(3) = srg(9,4,1,2):")
    run("rook", rook(3), 9, 4, 1, 2)
    print()
    print("bvls_graph() = srg(243,22,1,2):")
    run("bvls", bvls_graph(), 243, 22, 1, 2)
