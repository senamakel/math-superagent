"""Verify code/lib/cycles.py against hand cases.

Checks min_degree and cycle_lengths on K4, K3,3, the cube Q3, and the
Petersen graph, whose answers are known without a computer. The expected
values are stated independently below, then compared against what the
oracle returns. Prints literal per-case results.
"""

from lib.cycles import min_degree, cycle_lengths

import networkx as nx


def graph_from_edges(n, edges):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return G


# --- hand-constructed graphs, edges stated independently ---
K4 = graph_from_edges(4, [
    (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
])  # complete graph on 4: every vertex degree 3

K33 = graph_from_edges(6, [
    (0, 3), (0, 4), (0, 5),
    (1, 3), (1, 4), (1, 5),
    (2, 3), (2, 4), (2, 5),
])  # complete bipartite K_{3,3}: every vertex degree 3

# cube Q3: the 8 cube-corner/edge graph
Q3 = graph_from_edges(8, [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 6),
    (3, 7),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7),
])

# Petersen graph: the standard 10-vertex / 15-edge cubic graph
# outer 5-cycle 0-1-2-3-4-0, inner 5-cycle 5-7-9-6-8-5, spokes i-(5+i)
Petersen = graph_from_edges(10, [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
    (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
    (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
])

CASES = [
    ("K4",        K4,        3, {3, 4}),
    ("K3,3",      K33,       3, {4, 6}),
    ("cube Q3",   Q3,        3, {4, 6, 8}),
    ("Petersen",  Petersen,  3, {5, 6, 8, 9}),
]

all_ok = True
for name, G, exp_min_deg, exp_lengths in CASES:
    got_min = min_degree(G)
    got_lengths = cycle_lengths(G)
    ok_min = got_min == exp_min_deg
    ok_len = got_lengths == exp_lengths
    all_ok = all_ok and ok_min and ok_len
    print(f"=== {name} ===")
    print(f"  min_degree      expected {exp_min_deg}  got {got_min}  "
          f"{'MATCH' if ok_min else 'MISMATCH'}")
    print(f"  cycle_lengths   expected {sorted(exp_lengths)}  got "
          f"{sorted(got_lengths)}  {'MATCH' if ok_len else 'MISMATCH'}")
    print()

print("ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED")
