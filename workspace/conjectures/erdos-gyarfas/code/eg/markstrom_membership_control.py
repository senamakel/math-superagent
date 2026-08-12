"""Positive control for markstrom_membership.py reverse-contraction.

Take K4, do one forward vertex-into-triangle expansion, then run the same
reverse BFS: it must reach K4. This validates the inverse operation is exact.
"""
import networkx as nx
from networkx import Graph
from markstrom_membership import membership, contractible, contract


def expand(G, v):
    nbrs = list(G[v])
    import itertools
    H = Graph()
    base = list(G.nodes()) + ["x", "y", "z"]
    H.add_nodes_from(base)
    for u, w in G.edges():
        if u == v or w == v:
            continue
        H.add_edge(u, w)
    for e in [(x, y) for x, y in [("x", "y"), ("y", "z"), ("x", "z")]]:
        H.add_edge(*e)
    for nb, tri in zip(nbrs, ["x", "y", "z"]):
        H.add_edge(nb, tri)
    H.remove_node(v)
    return H


if __name__ == "__main__":
    K4 = nx.complete_graph(4)
    K4 = nx.relabel_nodes(K4, {i: str(i) for i in K4.nodes()})
    # expand vertex "3" (degree 3 in K4)
    E = expand(K4, "3")
    print("expanded: ", E.number_of_nodes(), "nodes", E.number_of_edges(), "edges")
    print("cubic:", set(dict(E.degree()).values()))
    best, seen, levels = membership(E)
    print("reverse BFS reaches K4:", best is not None, "depth:", best)
    print("distinct inverse graphs:", len(seen))
    assert best is not None and best == 1, "positive control FAILED"
    print("POSITIVE CONTROL PASSED: forward expansion reverses to K4")
