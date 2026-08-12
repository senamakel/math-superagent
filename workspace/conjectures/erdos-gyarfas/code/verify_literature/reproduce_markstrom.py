"""Standalone reproduction of the Markström extremal-cycle data.

Fresh independent verification route for the Erdős–Gyárfás literature, using
the run's exact cycle oracle (lib.cycle_oracle) and a from-scratch all-simple-
cycles enumeration.

Part (1): re-verify the four hand-checkable cycle sets against the oracle's
distinct_cycle_lengths:
    K4       -> cycles {3,4}
    K3,3     -> cycles {4,6}
    cube Q3  -> cycles {4,6,8}
    Petersen -> cycles {5,6,8,9}

Part (2): the Markström graph (House of Graphs id 51419, "Markstroem Graph"),
a cubic graph on 24 vertices that the literature asserts has no cycles of
length 4 or 8 but does contain a cycle of length 16 (a power of two), and
indeed has cycles of lengths {3,5,6,7,9..24}.  We reconstruct it from the
adjacency list published by House of Graphs and check, with the oracle's full
simple-cycle enumeration, exactly which powers of two (4,8,16,32) are present
or absent, and the full cycle-length set.

Why this needs no exhaustive search: the note's Table 3 gives only COUNTS of
the four 24-vertex graphs (24->4, 26->23, 28->251) and a figure of drawings —
no edge lists.  The single explicitly-named member of the family, the planar
Markström graph, has a published edge list here, so we verify that one graph
directly.  A full enumeration of 24-vertex cubic graphs with no C4/C8 would be
the exhaustive route (and is prohibited at this size); it is not needed to
verify the one explicit graph.

Output matches published claims iff:
  - Markström graph is cubic with 24 vertices, degree 3 everywhere;
  - cycle-length set contains NO 4 and NO 8, but CONTAINS 16;
  - length set == {3,5,6,7,9,...,24} (the MathWorld claim).
"""
import sys
import networkx as nx

from lib.cycle_oracle import all_simple_cycles, distinct_cycle_lengths, minimum_degree

# --- Part (1): the four hand-checkable graphs -------------------------------
# (name, graph builder, expected (min_deg, cycle lengths))
KNOWN = [
    ("K4",       nx.complete_graph(4),              (3, frozenset({3, 4}))),
    ("K3,3",     nx.complete_bipartite_graph(3, 3), (3, frozenset({4, 6}))),
    ("cube Q3",  nx.hypercube_graph(3),             (3, frozenset({4, 6, 8}))),
    ("Petersen", nx.petersen_graph(),               (3, frozenset({5, 6, 8, 9}))),
]

# --- Markström graph: House of Graphs id 51419, adjacency list (24 vertices)
MARKSTROM_ADJ = [
    [1,2,3],[0,18,19],[0,21,22],[0,20,23],[6,10,12],[6,9,11],[4,5,12],
    [8,13,14],[7,10,17],[5,11,15],[4,8,17],[5,9,16],[4,6,16],[7,14,15],
    [7,13,19],[9,13,18],[11,12,21],[8,10,20],[1,15,19],[1,14,18],
    [3,17,23],[2,16,22],[2,21,23],[3,20,22],
]


def build_markstrom():
    G = nx.Graph()
    G.add_nodes_from(range(24))
    for u, nbrs in enumerate(MARKSTROM_ADJ):
        for v in nbrs:
            G.add_edge(u, v)
    return G


def powers_of_two_present(lengths):
    """Which powers of two (up to 64) are present / absent in the length set."""
    present = {2 ** k for k in range(2, 7)}  # 4, 8, 16, 32, 64
    return {p for p in present if p in lengths}, {p for p in present if p not in lengths}


def main():
    print("=" * 74)
    print("Part (1): re-verify the four hand-checkable cycle sets with the oracle")
    print("=" * 74)
    ok1 = True
    for name, G, (exp_deg, exp_lens) in KNOWN:
        deg = minimum_degree(G)
        lens = distinct_cycle_lengths(G)
        listed = {len(c) for c in all_simple_cycles(G)}
        match = (deg == exp_deg and lens == exp_lens and listed == lens)
        ok1 &= match
        print(f"  {name:10s} min_deg={deg} cycles={sorted(lens)}"
              f"  expected={sorted(exp_lens)}  -> {'MATCH' if match else 'MISMATCH'}")
    print("  Part (1) result:", "ALL MATCH" if ok1 else "MISMATCHES PRESENT")

    print()
    print("=" * 74)
    print("Part (2): Markström graph (HoG 51419) — cubic, no C4, no C8, has C16")
    print("=" * 74)
    G = build_markstrom()
    n = G.number_of_nodes()
    degs = sorted(d for _, d in G.degree())
    deg = minimum_degree(G)
    lens = distinct_cycle_lengths(G)
    listed = {len(c) for c in all_simple_cycles(G)}
    assert listed == lens, "oracle distinct-cycle-lengths disagrees with enumeration"

    pow_present, pow_absent = powers_of_two_present(lens)
    L = sorted(lens)

    print(f"  vertices={n}  cubic(deg==3 everywhere): {all(d == 3 for d in degs)}"
          f"  min_deg={deg}")
    print(f"  cycle lengths = {L}")
    print(f"  C4 present: {4 in lens}   C8 present: {8 in lens}   "
          f"C16 present: {16 in lens}   C32 present: {32 in lens}")
    print(f"  powers of two present: {sorted(pow_present)}"
          f"   absent: {sorted(pow_absent)}")

    # MathWorld claim: cycles of lengths 3,5,6,7 and 9..24, none of 4 or 8.
    expected = set(range(3, 25)) - {4, 8}
    mathworld_match = (lens == expected)
    print(f"  MathWorld cycle profile {{3,5,6,7,9..24}}: {'MATCH' if mathworld_match else 'MISMATCH'}")
    if not mathworld_match:
        only_in_ours = lens - expected
        only_in_theirs = expected - lens
        print(f"    only in ours: {sorted(only_in_ours)}"
              f"   only in MathWorld: {sorted(only_in_theirs)}")

    no_c4c8 = (4 not in lens) and (8 not in lens)
    has_c16 = 16 in lens
    claim_match = (n == 24 and all(d == 3 for d in degs)
                   and no_c4c8 and has_c16 and mathworld_match)

    print()
    print("  Published claim: 24 vertices, cubic, no C4 and no C8, all contain C16;")
    print("                   the (planar) Markström graph has cycle profile {3,5,6,7,9..24}.")
    print("  Reproduction result:", "MATCHES PUBLISHED CLAIM" if claim_match
          else "DOES NOT MATCH PUBLISHED CLAIM")
    print()
    print("Part (1) result:", "ALL MATCH" if ok1 else "MISMATCHES PRESENT")
    return 0 if (ok1 and claim_match) else 1


if __name__ == "__main__":
    sys.exit(main())
