"""Brute-force check of the Alon-Tarsi certificate direction across graphs.

A graph with an orientation D of max out-degree <= k-1 and EE(D) != EO(D)
(parity of Eulerian subdigraphs unbalanced) satisfies AT(G) <= k, hence is
k-choosable, hence k-colourable.  So a *certificate of non-k-colourability*
must NOT have such an orientation.  We test the candidate's calibration
predictions:
  - K4 (4-colourable): should have an unbalanced orientation with outdeg<=3.
  - K5 (NOT 4-colourable): should have NO such orientation (AT(K5)=5>4).
  - Moser spindle (4-colourable): should have an unbalanced orientation.
If K5 has no unbalanced orientation, the candidate's claimed use is inverted.
"""
from itertools import product

def eulerian_parity_diff(n, edges, outdeg):
    """Sum over all spanning subdigraph subsets of (-1)^(#edges selected),
    restricted to Eulerian subdigraphs (indeeg=outdeg at every vertex)."""
    total = 0
    m = len(edges)
    for mask in range(1 << m):
        # compute indeg/outdeg of selected arcs
        bal = True
        deg = [0] * n
        edgesel = []
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                edgesel.append((u, v))
        # selected arcs must form an Eulerian subdigraph: indeg(v)=outdeg(v)
        outd = [0] * n
        ind = [0] * n
        for u, v in edgesel:
            outd[u] += 1
            ind[v] += 1
        if all(outd[i] == ind[i] for i in range(n)):
            total += (-1) ** len(edgesel)
    return total

def complete_graph(n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j))
    return n, edges

def check(graph, maxout):
    """Return whether some orientation has max out-degree <= maxout and
    unbalanced eulerian parity (diff != 0)."""
    n, edges = graph
    m = len(edges)
    # each undirected edge gets one of two directions
    for orient in product([0, 1], repeat=m):
        outdeg = [0] * n
        directed = []
        for idx, (u, v) in enumerate(edges):
            if orient[idx] == 0:
                directed.append((u, v)); outdeg[u] += 1
            else:
                directed.append((v, u)); outdeg[v] += 1
        if max(outdeg) <= maxout:
            diff = eulerian_parity_diff(n, directed, outdeg)
            if diff != 0:
                return True, diff
    return False, 0

def moser_spindle_graph():
    # Moser spindle: 7 vertices, edges per the library (11 edges)
    # adjacency from the certified construction
    edges = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
    return 7, edges

if __name__ == "__main__":
    print("Checking Alon-Tarsi certificate DIRECTION for 4-colourability")
    print("=" * 60)
    for name, graph, maxout in [
        ("K4 (4-colourable)", complete_graph(4), 3),
        ("K5 (NOT 4-colourable, chi=5)", complete_graph(5), 3),
        ("Moser spindle (4-colourable)", moser_spindle_graph(), 3),
    ]:
        found, diff = check(graph, maxout)
        print(f"{name:42s} has unbalanced maxout<={maxout} orientation: {found}"
              f"{'  (diff=%d)'%diff if found else ''}")
    print()
    print("Predicted by candidate (if correct direction = non-colorable):")
    print("  K4: NONE   K5: YES   Moser: NONE")
    print("Predicted if ALON-TARSI = positive/choosability bound:")
    print("  K4: YES    K5: NO    Moser: YES")
