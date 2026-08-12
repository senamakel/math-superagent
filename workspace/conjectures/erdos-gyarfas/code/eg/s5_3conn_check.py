"""Sanity-check is_3connected on Petersen (3-connected, girth 5, n=10) and
re-check n=15 survivors (all 149 should be 3-connected if S5 = A366224 holds
structurally)."""
import subprocess, networkx as nx
from lib.cycles import min_degree

def bfs_girth(G):
    from collections import deque
    best = None
    for s in G.nodes():
        dist = {s: 0}
        parent = {s: -1}
        q = deque([s])
        while q:
            v = q.popleft()
            for w in G.neighbors(v):
                if w not in dist:
                    dist[w] = dist[v] + 1
                    parent[w] = v
                    q.append(w)
                elif parent[v] != w and parent[w] != v:
                    L = dist[v] + dist[w] + 1
                    if best is None or L < best:
                        best = L
    return best

def is_3connected(G):
    nodes = list(G.nodes())
    if len(nodes) < 4:
        return False
    for u in nodes:
        H = G.copy()
        H.remove_node(u)
        art = list(nx.articulation_points(H))
        if not nx.is_connected(H) or art:
            return False
    return True

# Petersen: standard cubic graph, 3-connected, girth 5
P = nx.petersen_graph()
print("Petersen 3-connected?", is_3connected(P), "girth", bfs_girth(P))

# n=15: all 149 girth>=5 survivors must be 3-connected
cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", "15"]
proc = subprocess.run(cmd, capture_output=True, text=True)
bad = 0
n_graphs = 0
for g6 in proc.stdout.splitlines():
    g6 = g6.strip()
    if not g6:
        continue
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    if min_degree(G) < 3:
        continue
    n_graphs += 1
    if bfs_girth(G) is None or bfs_girth(G) < 5:
        continue
    if not is_3connected(G):
        bad += 1
        print("NOT 3CONN at n=15:", g6)
print(f"n=15: {n_graphs} total mindeg3, {bad} non-3-connected girth>=5 survivors")