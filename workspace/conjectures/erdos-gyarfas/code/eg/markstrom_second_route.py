"""Second-route cross-check of the Markström graph reconstruction.

Loads the graph two independent ways:
  1. graph6   -> nx.from_graph6_bytes
  2. edgelist -> build Graph from the 0-indexed edge list

and evaluates every claimed invariant with TWO independent cycle-length
implementations side by side (exactly the code from brute.py, imported, not
re-typed):
  * oracle = lib.cycle_oracle.oracle   (from-scratch DFS enumeration)
  * brute  = brute.oracle              (nx.simple_cycles on bidirected
                                        graph, filter len >= 3)

Expected cycle-length set:
    {3,5,6,7} U {9,10,...,24}   (4 and 8 absent, 16 present)

Checks per route: min degree 3, edge count 36, planarity, node-connectivity 3.
Prints every check for both routes with a final MATCH/FAIL.
"""
import networkx as nx

from brute import oracle as brute_oracle
from lib.cycle_oracle import oracle as oracle_fn

EDGE_LIST = "/workspace/code/out/markstrom_reconstruction/markstrom.edgelist"
GRAPH6 = "/workspace/code/out/markstrom_reconstruction/markstrom.graph6"

# --- load both routes ---
g6 = open(GRAPH6).read().strip()
G_g6 = nx.from_graph6_bytes(g6.encode())

G_el = nx.Graph()
G_el.add_nodes_from(range(24))
with open(EDGE_LIST) as f:
    for line in f:
        a, b = line.split()
        G_el.add_edge(int(a), int(b))

print("graph6  decodes to n =", G_g6.number_of_nodes(),
      "edges =", G_g6.number_of_edges())
print("edgelist gives    n =", G_el.number_of_nodes(),
      "edges =", G_el.number_of_edges())
print("graph6 graph == edgelist graph:", nx.utils.graphs_equal(G_g6, G_el))

# expected cycle profile: {3,5,6,7} U {9..24}
expected_lens = frozenset({3, 5, 6, 7}) | set(range(9, 25))

all_ok = True

def check(label, got, expected):
    global all_ok
    ok = got == expected
    all_ok &= ok
    print(f"  {label:14s} got={got}  expected={expected}  "
          f"-> {'MATCH' if ok else 'FAIL'}")
    return ok

for name, G in [("graph6", G_g6), ("edgelist", G_el)]:
    print(f"\n=== route: {name} ===")
    o_min, o_lens = oracle_fn(G)          # lib/cycle_oracle (DFS)
    b_min, b_lens = brute_oracle(G)       # brute.py (nx.simple_cycles)

    print("-- min degree --")
    check("oracle", o_min, 3)
    check("brute.py", b_min, 3)

    print("-- cycle-length set --")
    check("oracle lens ", frozenset(o_lens), expected_lens)
    check("brute lens  ", frozenset(b_lens), expected_lens)
    print("    oracle profile:", o_lens)

    print("-- power-of-two flags (4, 8 absent; 16 present) --")
    for k in (2, 3, 4):
        L = 2 ** k
        o_pres = L in o_lens
        b_pres = L in b_lens
        exp = (L == 16)
        print(f"  length {L:2d}: oracle={o_pres} brute={b_pres} "
              f"expected_present={exp} -> "
              f"{'MATCH' if o_pres == b_pres == exp else 'FAIL'}")
        all_ok &= (o_pres == b_pres == exp)

    print("-- edge count --")
    check("edges", G.number_of_edges(), 36)
    check("vertices", G.number_of_nodes(), 24)

    print("-- planarity (networkx) --")
    plan = nx.check_planarity(G)[0]
    print(f"  planar={plan}  expected=True  -> {'MATCH' if plan else 'FAIL'}")
    all_ok &= plan

    print("-- node-connectivity (networkx) --")
    nc = nx.node_connectivity(G)
    check("node-conn", nc, 3)

print("\n" + ("ALL MATCH" if all_ok else "AT LEAST ONE FAIL"))