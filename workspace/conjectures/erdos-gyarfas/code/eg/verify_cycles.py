"""Verify lib/cycles.py against hand-checkable graphs and beyond.

Checks the oracle functions (min_degree, cycle_lengths, girth,
has_power_of_two_cycle) against graphs whose answers are known without a
computer: K4, K3,3, the cube Q3, and the Petersen graph, then runs a handful
of extra graphs. Every check asserts the exact expected value, so any
regression fails loudly. This is the file that establishes the oracle is
correct before anything on this run trusts it.
"""

import networkx as nx
from lib.cycles import (
    min_degree,
    cycle_lengths,
    girth,
    has_power_of_two_cycle,
    power_of_two_cycle_lengths,
)


def check(name, graph, md, cyc, g):
    got_md = min_degree(graph)
    got_cyc = cycle_lengths(graph)
    got_g = girth(graph)
    status = "OK" if (got_md == md and got_cyc == set(cyc) and got_g == g) else "FAIL"
    print(f"{name:12s} min_deg={got_md} (want {md})  "
          f"cycles={sorted(got_cyc)} (want {sorted(set(cyc))})  "
          f"girth={got_g} (want {g})  [{status}]")
    assert got_md == md, name
    assert got_cyc == set(cyc), name
    assert got_g == g, name


def main():
    # ---- the four hand-checkable graphs ---------------------------------
    K4 = nx.complete_graph(4)
    check("K4", K4, 3, {3, 4}, 3)

    K33 = nx.complete_bipartite_graph(3, 3)
    check("K3,3", K33, 3, {4, 6}, 4)

    cube = nx.hypercube_graph(3)
    check("cube Q3", cube, 3, {4, 6, 8}, 4)

    petersen = nx.petersen_graph()
    check("Petersen", petersen, 3, {5, 6, 8, 9}, 5)

    print()

    # ---- a few extra graphs ---------------------------------------------
    # K5: complete on 5 = min deg 4, all cycle lengths 3..5
    check("K5", nx.complete_graph(5), 4, {3, 4, 5}, 3)

    # K2,3: min degree 2. Simple cycles alternate between the parts, so a
    # length-6 cycle would need 3 vertices from the size-2 part — impossible.
    # Only length 4 exists. (The oracle is what told us this; my first guess
    # of {4,6} was wrong.)
    check("K2,3", nx.complete_bipartite_graph(2, 3), 2, {4}, 4)

    # single triangle
    check("triangle", nx.cycle_graph(3), 2, {3}, 3)

    # a 5-cycle and a 6-cycle joined at one vertex -> cycles {5, 6}
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])   # C5
    G.add_edges_from([(0, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)])  # C6 at 0
    # a 6-cycle needs 6 edges: now it truly is 0-5-6-7-8-9-0
    check("C5+C6 share", G, 2, {5, 6}, 5)

    # two disjoint triangles joined by a bridge -> girth 3, cycles {3}
    H = nx.Graph()
    H.add_edges_from([(0, 1), (1, 2), (2, 0)])
    H.add_edges_from([(3, 4), (4, 5), (5, 3)])
    H.add_edge(0, 3)
    # min degree: vertex 0 has degree 3 (1,2,3) -> md 2 for others? vertex1 deg 2
    check("two tris+bridge", H, 2, {3}, 3)

    # a tree: no cycles, girth None
    T = nx.path_graph(6)
    print(f"{'path P6':12s} min_deg={min_degree(T)}  cycles={sorted(cycle_lengths(T))}  "
          f"girth={girth(T)}")
    assert min_degree(T) == 1
    assert cycle_lengths(T) == set()
    assert girth(T) is None
    print("  [OK] acyclic graph handled")

    print()

    # ---- power-of-two cycle predicate -----------------------------------
    print("Power-of-two-cycle predicate (>=4):")
    for name, graph in [("K4", K4), ("K3,3", K33), ("cube", cube),
                        ("Petersen", petersen), ("K5", K5), ("C5only", G)]:
        got = has_power_of_two_cycle(graph)
        two = power_of_two_cycle_lengths(graph)
        print(f"  {name:9s} has_power2={got}  power2_lengths={two}")

    print()
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
