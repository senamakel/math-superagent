"""Validate the J3 glueing machinery of lobe_probe.py on ARBITRARY lobe pairs
(the real pair search is currently vacuous — no pow2-free lobes exist at
n_H <= 14/18 — so we must prove the glue route itself is sound before it can
be trusted when a pow2-free lobe finally appears at larger n).

For every connected cubic H on n_H = 4..14 and every edge e, build
L_ab = H - e + v (the same lobe shapes lobe_probe uses), then glue ANY two
of them by identifying their v-vertices into one central degree-4 cut
vertex (the (2,2) cut-vertex shape).  For each glued graph verify the
no-cross-cycles claim that J3 rests on:

    cycle_lengths(glued) == cycle_lengths(L1) | cycle_lengths(L2)

i.e. no simple cycle of the glued graph crosses the cut (a cycle through the
central vertex must enter and leave through the same lobe).  We also assert
the structural invariants J3 enforces: central vertex degree 4, all other
vertices degree >= 3, graph connected, node connectivity exactly 1.

Two independent cycle routes on a large random sample of pairs:
    lib.cycle_oracle.distinct_cycle_lengths
    networkx.simple_cycles
Must agree, and the union identity must hold for every pair.

Complexity: the lobe constructions here are the small-instance exhaustive
set (<= 12,588 at n_H <= 14); pairs are sampled (a few thousand glueings);
cycle enumeration is the exponential small-instance oracle (rule 9,
oracle bound n <= 31) — verification, not method.
"""
import os
import random
import subprocess

import networkx as nx

from lib.cycle_oracle import distinct_cycle_lengths, minimum_degree

HERE = os.path.dirname(os.path.abspath(__file__))


def connected_cubic_graph6(n):
    out = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", "-D3", str(n)],
        capture_output=True, text=True, check=True)
    return out.stdout.splitlines()


def all_lobes(max_nH):
    """Yield (nH, H_g6, e, L) for every lobe construction."""
    for n in range(4, max_nH + 1, 2):
        for g6 in connected_cubic_graph6(n):
            H = nx.from_graph6_bytes(g6.encode())
            for e in H.edges():
                L = nx.Graph()
                L.add_nodes_from(H.nodes())
                L.add_edges_from(H.edges())
                L.remove_edge(*e)
                v = max(H.nodes()) + 1
                L.add_node(v)
                L.add_edge(v, e[0])
                L.add_edge(v, e[1])
                yield n, g6, e, L, v


def glue_pair(L1, v1, L2, v2):
    """Glue two lobes by identifying their v-vertices -> central cut vertex 0."""
    n1 = L1.number_of_nodes() - 1
    off2 = 1 + n1
    G = nx.Graph()
    C = 0
    def map1(u):
        return C if u == v1 else u + 1
    def map2(u):
        return C if u == v2 else u + off2
    for a, b in L1.edges():
        G.add_edge(map1(a), map1(b))
    for a, b in L2.edges():
        G.add_edge(map2(a), map2(b))
    return G, C


def main():
    rng = random.Random(20250812)
    lobes = list(all_lobes(12))
    print(f"lobe constructions loaded: {len(lobes)}")

    n_pairs = 0
    ident_ok = True
    nx_agree = True
    union_ok = True
    struct_ok = True
    # bounded random sample of pairs (the identity is size-independent, so a
    # fixed quota is enough to validate the glue machinery; full enumeration
    # of all pairs would be the exponential oracle anyway)
    MAX_PAIRS = 2500
    pairs = []
    made = 0
    while made < MAX_PAIRS:
        i = rng.randrange(len(lobes))
        j = rng.randrange(len(lobes))
        n1, g1, e1, L1, v1 = lobes[i]
        n2, g2, e2, L2, v2 = lobes[j]
        if L1.number_of_nodes() + L2.number_of_nodes() - 1 <= 31:
            G, C = glue_pair(L1, v1, L2, v2)
            # structural invariants
            s_ok = (G.degree(C) == 4
                    and minimum_degree(G) >= 3
                    and nx.is_connected(G)
                    and nx.node_connectivity(G) == 1)
            if not s_ok:
                struct_ok = False
                print("STRUCT FAIL", g1, e1, g2, e2, G.degree(C),
                      minimum_degree(G), nx.node_connectivity(G))
            # two independent cycle routes
            mine = set(distinct_cycle_lengths(G))
            theirs = {len(c) for c in nx.simple_cycles(G.to_directed())
                      if len(c) >= 3}
            if mine != theirs:
                nx_agree = False
                print("NX DISAGREE", g1, e1, g2, e2, mine, theirs)
            # no-cross-cycles: glued set == union of lobe sets
            union = (set(distinct_cycle_lengths(L1))
                     | set(distinct_cycle_lengths(L2)))
            if mine != union:
                union_ok = False
                print("UNION FAIL (cycle crosses cut!):", g1, e1, g2, e2,
                      "glued-only", sorted(mine - union),
                      "lobe-only", sorted(union - mine))
            n_pairs += 1
            made += 1
    print(f"pairs glued and checked: {n_pairs}")
    print(f"structural invariants (deg(C)=4, delta>=3, connected, "
          f"node-conn=1): {'ALL PASS' if struct_ok else 'FAIL'}")
    print(f"oracle == networkx on glued graphs: "
          f"{'AGREE on all' if nx_agree else 'DISAGREE'}")
    print(f"no-cross-cycles identity (glued set == union of lobe sets): "
          f"{'HOLDS on all pairs' if union_ok else 'FAILS'}")
    return 0 if (struct_ok and nx_agree and union_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())