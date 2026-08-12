"""Census of the K4-triangle-expansion family (Markström's construction), v2.

Uses nauty-labelg to obtain a canonical form for deduplication of isomorphism
classes -- this is the exact, standard tool (the installed networkx 2.8.8 has
no canonical_label; labelg canonical form is the nauty certificate).

Start from K4. A single "expansion" replaces one degree-3 vertex v by a
triangle x,y,z, attaching the three neighbours of v to x,y,z in one of the 6
bijections. Each step adds 2 vertices and keeps the graph cubic, so from n=4
after k steps n = 4 + 2k.

At each size we report the number of isomorphism classes in the family, how
many avoid a C4, and how many avoid both C4 and C8. The Markström graph is the
known planar cubic member built this way on 24 vertices avoiding C4 and C8.

Exponential oracle: the branching grows with the class count; bounded to the
small n reachable in budget. Verification census, not the method.
"""
import subprocess
import sys
import itertools
import networkx as nx

from lib.cycle_oracle import oracle


def canonical_labelg(G):
    """Return the nauty canonical graph6 string for G (exact canonical form)."""
    s = nx.to_graph6_bytes(G, header=False).decode().strip()
    proc = subprocess.run(["nauty-labelg", "-q"], input=s + "\n",
                          capture_output=True, text=True)
    out = proc.stdout.strip().splitlines()
    return out[0] if out else s


def expand(G):
    """All graphs obtainable from cubic G by one vertex-into-triangle expansion
    (list of graphs, not yet deduplicated by iso within this expansion)."""
    from networkx import Graph
    results = []
    for v in list(G.nodes()):
        nbrs = list(G[v])
        base = list(G.nodes()) + ["x", "y", "z"]
        for perm in itertools.permutations(nbrs):
            H = Graph()
            H.add_nodes_from(base)
            for u, w in G.edges():
                if u == v or w == v:
                    continue
                H.add_edge(u, w)
            x, y, z = "x", "y", "z"
            H.add_edges_from([(x, y), (y, z), (x, z)])
            for nb, tri in zip(perm, [x, y, z]):
                H.add_edge(nb, tri)
            H.remove_node(v)
            results.append(H)
    return results


def dedup(reps):
    """Dedup list of graphs by nauty canonical form; return canonical strings."""
    canon = set()
    for H in reps:
        canon.add(canonical_labelg(H))
    return canon


def main(maxn):
    G = nx.complete_graph(4)
    canon = {canonical_labelg(G)}
    n = 4
    print(f"n=4  classes=1  avoidsC4=False  avoidsC4C8=False", flush=True)
    while n < maxn:
        # expand every current class
        pool = []
        for c in canon:
            H = nx.from_graph6_bytes(c.encode())
            pool.extend(expand(H))
        canon = dedup(pool)
        n += 2
        classlist = []
        avoids_c4 = 0
        avoids_both = 0
        for c in canon:
            H = nx.from_graph6_bytes(c.encode())
            dseq = [d for _, d in H.degree()]
            assert set(dseq) == {3} and len(H) == n, (len(H), dseq)
            lens = oracle(H)[1]
            if 4 not in lens:
                avoids_c4 += 1
            if 4 not in lens and 8 not in lens:
                avoids_both += 1
            classlist.append(c)
        print(f"n={n}  classes={len(canon)}  avoidsC4={avoids_c4}  "
              f"avoidsC4C8={avoids_both}", flush=True)
        sys.stdout.flush()


if __name__ == "__main__":
    maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    main(maxn)
