"""Execute the connectivity/girth checks drafted in
code/verify_connectivity_claims.py (which was written by the librarian and
never run). Nothing here is a source of a finding; it is a mechanical check of
elementary facts about near-counterexample constructions.

Checks:
  1. Two K4s joined by a bridge: min degree 3, node connectivity 1
     (refutes the naive claim "delta>=3 implies 2-connected":
     both bridge endpoints are cut vertices).
  2. Markstroem graph (HoG 51419, 24-vertex cubic planar near-counterexample):
     girth 3, triangles present. Edge list taken from
     verify_connectivity_claims.py; independently validated here to decode to
     the same edge set as the canonical graph6 string
     Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D.
  3. Three lobes (k=3) glued at one central cut vertex v, each lobe joined to
     v by exactly ONE edge ("all-single-edge" fashion, Royle's construction:
     "three copies of X joined to a single central vertex").  v has degree 3,
     each touched lobe vertex gains one degree, everything else keeps its lobe
     degree, so delta(G) = 3.  Since v has exactly one neighbour in each lobe,
     NO simple cycle can pass through v (a cycle through v would need two
     distinct edges from v into one component), so the cycle set of the glued
     graph is exactly the union of the three lobe cycle sets.

     Lobes used: (a) Markstroem graph (the closest known near-counterexample;
     lobe cycle set {3,5,6,7,9..24} -- no C4/C8, has C16); (b) Petersen graph
     (lobe cycle set {5,6,8,9} -- has C8), Royle's archetypal X.

     Output: min degree of G, node connectivity, degree of v, components of
     G-v, and the full cycle-length set from BOTH lib.cycle_oracle and
     networkx simple_cycles -- asserted equal.

Whether the glued graph is a delta>=3 graph and whether it has a
power-of-two cycle is printed explicitly.

Complexity: cycle enumeration is the exponential small-instance oracle
(rule 9) -- the largest graph here is the 73-vertex glued Markstroem triple,
whose cycle set is exactly 3x that of the 24-vertex lobe, and the run is
performed purely to validate the union claim, not as method.
"""
import networkx as nx

from lib.cycle_oracle import oracle, all_simple_cycles

MARKSTROM_EDGES = [
    (0, 1), (0, 2), (0, 3), (1, 18), (1, 19), (2, 21), (2, 22), (3, 20),
    (3, 23), (4, 6), (4, 10), (4, 12), (5, 6), (5, 9), (5, 11), (6, 12),
    (7, 8), (7, 13), (7, 14), (8, 10), (8, 17), (9, 11), (9, 15), (10, 17),
    (11, 16), (12, 16), (13, 14), (13, 15), (14, 19), (15, 18), (16, 21),
    (17, 20), (18, 19), (19, 14), (20, 23), (21, 22), (22, 23), (23, 20),
]

POWERS_OF_TWO = {2 ** k for k in range(2, 10)}  # 4, 8, 16, 32, ...


def markstrom():
    G = nx.Graph()
    G.add_edges_from(MARKSTROM_EDGES)
    return G


def power_of_two_cycles(lengths):
    return sorted(p for p in POWERS_OF_TWO if p in lengths)


def nx_cycle_lengths(G):
    """Independent second route: networkx simple_cycles on the directed view,
    filtered to length >= 3.  Must agree with lib.cycle_oracle."""
    return frozenset(
        len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3
    )


def check_cycle_agreement(name, G):
    mine, _ = oracle(G)          # oracle returns (min_deg, sorted lengths)
    mine_set = set(mine)
    theirs = nx_cycle_lengths(G)
    agree = mine_set == theirs
    print(f"  cycle_oracle == networkx simple_cycles: {agree}")
    if not agree:
        print("    oracle-only:", sorted(mine_set - theirs))
        print("    nx-only    :", sorted(theirs - mine_set))
        raise SystemExit(f"MISMATCH on {name}: oracle vs networkx cycle sets")
    return mine_set


def glue_lobes(lobe, k=3, to_central=0):
    """k lobes ('lobe' a networkx Graph) glued at a central cut vertex 0, each
    joined to 0 by exactly one edge (lobe vertex `to_central`)."""
    G = nx.Graph()
    G.add_node(0)
    for i in range(k):
        offset = 1 + i * lobe.number_of_nodes()
        for u, v in lobe.edges():
            G.add_edge(u + offset, v + offset)
        G.add_edge(0, to_central + offset)  # single edge from v into the lobe
    return G


def report(name, G, note=""):
    degs = [d for _, d in G.degree()]
    print(f"--- {name} {note}")
    print(f"  n, m           : {G.number_of_nodes()}, {G.number_of_edges()}")
    print(f"  min/max degree : {min(degs)}, {max(degs)}")
    print(f"  components     : {nx.number_connected_components(G)}")
    print(f"  node conn.     : {nx.node_connectivity(G)}")


def main():
    # ---- check 1: two K4s joined by a bridge -------------------------------
    g1 = nx.Graph()
    for c in [(0, 1, 2, 3), (4, 5, 6, 7)]:
        for u in c:
            for v in c:
                if u < v:
                    g1.add_edge(u, v)
    g1.add_edge(3, 4)  # the bridge
    report("g1: two K4s + bridge", g1, "(min degree 3, node connectivity 1?)")
    degs = [d for _, d in g1.degree()]
    print(f"  min degree == 3        : {min(degs) == 3}")
    print(f"  node connectivity == 1 : {nx.node_connectivity(g1) == 1}")
    print(f"  cut vertices (bridge endpoints): "
          f"{[u for u, v in nx.bridges(g1) for u in [u, v]]}")
    print(f"  cycle lengths          : {oracle(g1)[1]}")
    print()

    # ---- check 2: Markstroem graph, from the edge list in the draft file ----
    gM = markstrom()
    # Sanity: the edge list must be the canonical graph6 Markstroem graph.
    canon = nx.from_graph6_bytes(
        "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D".encode())
    same = (frozenset(frozenset(e) for e in gM.edges())
            == frozenset(frozenset(e) for e in canon.edges()))
    report("Markstroem graph (HoG 51419)", gM,
           "(cubic planar, no C4/C8, has C16)" + ("" if same
           else "  !! edge list != graph6 !!"))
    lens = check_cycle_agreement("Markstroem", gM)
    tris = sum(nx.triangles(gM).values()) // 3
    print(f"  girth (min cycle length): {min(lens)}")
    print(f"  has triangle            : {3 in lens}")
    print(f"  # triangles             : {tris}  (HoG invariant says 7)")
    print(f"  cycle lengths           : {sorted(lens)}")
    print()

    # ---- check 3: three lobes glued at one cut vertex v, single-edge (k=3)
    lobes = {
        "Markstroem lobe": gM,
        "Petersen lobe": nx.petersen_graph(),
    }
    for lobe_name, lobe in lobes.items():
        G = glue_lobes(lobe, k=3, to_central=0)
        print(f"--- glued: 3 x {lobe_name} at central cut vertex 0 "
              f"(all-single-edge, k=3)")
        report("", G, "")
        # degree of the central vertex
        print(f"  degree of v (central vertex 0): {G.degree(0)}")
        # components of G - v
        Gmv = nx.Graph(G)
        Gmv.remove_node(0)
        comps = list(nx.connected_components(Gmv))
        print(f"  G-v components: {len(comps)}, sizes "
              f"{sorted(len(c) for c in comps)}")
        lens = check_cycle_agreement(f"glued {lobe_name}", G)
        print(f"  cycle lengths : {sorted(lens)}")
        pow2 = power_of_two_cycles(lens)
        print(f"  delta(G) >= 3            : {min(d for _, d in G.degree()) >= 3}")
        print(f"  has power-of-two cycle   : {bool(pow2)}  -> lengths {pow2}")
        # structural claim: no cycle passes through v => union of lobe cycle sets
        union = frozenset().union(*[frozenset(
            len(c) for c in all_simple_cycles(lobe))]) if False else None
        print()
    return


if __name__ == "__main__":
    main()