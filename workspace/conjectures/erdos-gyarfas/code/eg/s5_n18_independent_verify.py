"""Independent verification of the n=18 non-3-connected S5 survivors.

First route (in s5_identification.py): articulation-based test — G is
3-connected iff G-v is connected and articulation-free for every v.
This route: networkx.node_connectivity == 3, a max-flow based exact vertex
connectivity computation — a completely different algorithm. If it finds the
same 3 graphs non-3-connected on the full n=18 S5 class, the earlier count
is confirmed by an independent implementation.

Also analyses the structure of the three extras: 2-separator adjacency, the
two components left after removing the separator, and whether each component
is Petersen-like (the identification's failure mode is 2-sums / amalgams of
smaller girth-5 cubic graphs).
"""
import subprocess, time
import networkx as nx
from collections import Counter

from lib.cycles import cycle_lengths


def geng_lines(n):
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return [l.strip() for l in proc.stdout.splitlines() if l.strip()]


def structure(g6):
    """Return (g6, degseq, 2-separator, components-after-removal, per-comp
    info) for a non-3-connected graph, or None if it is 3-connected."""
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    if nx.node_connectivity(G) == 3:
        return None
    # find a 2-separator: pair {a,b} whose removal disconnects
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            H = G.copy()
            H.remove_node(nodes[i]); H.remove_node(nodes[j])
            if not nx.is_connected(H):
                a, b = nodes[i], nodes[j]
                comps = list(nx.connected_components(H))
                info = []
                for c in comps:
                    sub = G.subgraph(c | {a, b})
                    info.append({
                        'comp_size': len(c),
                        'comp_internal_edges': sub.number_of_edges(),
                        'edges_to_a': sum(1 for x in c if G.has_edge(x, a)),
                        'edges_to_b': sum(1 for x in c if G.has_edge(x, b)),
                        'comp_min_degree': min(d for _, d in sub.degree()
                                               if _ in c or True)
                    })
                return {
                    'g6': g6, 'separator': (a, b),
                    'separator_adjacent': G.has_edge(a, b),
                    'components': comps,
                    'component_info': info,
                    'degseq': sorted(d for _, d in G.degree()),
                    'cycle_lengths': sorted(cycle_lengths(G))
                }
    return None


def main():
    n = 18
    print(f"Independent check: node_connectivity == 3 on all S5({n}) graphs", flush=True)
    lines = geng_lines(n)
    print(f"S5(18) = {len(lines)}", flush=True)
    t0 = time.time()
    non3 = []
    for i, g6 in enumerate(lines):
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if nx.node_connectivity(G) != 3:
            non3.append(g6)
        if (i + 1) % 100000 == 0:
            print(f"  checked {i+1}/{len(lines)}  ({time.time()-t0:.0f}s)", flush=True)
    print(f"non-3-connected by node_connectivity: {len(non3)}  "
          f"(s5_identification.py found 3)  ({time.time()-t0:.0f}s)", flush=True)
    print("match:", sorted(non3) == sorted(
        ['Q????B?g?oA_GgOc?h?QGZ?AR??',
         'Q????B?g?oA_GgOc?h?QGZ?AR?G',
         'Q???C@?G?oA_@aA`[?@B?RSAQo?']))
    for g6 in non3:
        st = structure(g6)
        print()
        print("graph6:", st['g6'])
        print("  degseq:", st['degseq'])
        print("  2-separator:", st['separator'], "adjacent:", st['separator_adjacent'])
        for ci, info in enumerate(st['component_info']):
            print(f"  component {ci}: size {info['comp_size']} "
                  f"internal edges {info['comp_internal_edges']} "
                  f"edges->a {info['edges_to_a']} edges->b {info['edges_to_b']}")
        print("  cycle lengths:", st['cycle_lengths'])

    # degrees of the separator in each graph
    for g6 in non3:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        a, b = 16, 17
        print(f"{g6}: deg(16)={G.degree(16)} deg(17)={G.degree(17)} "
              f"edge(16,17)={G.has_edge(16,17)}")


if __name__ == "__main__":
    main()