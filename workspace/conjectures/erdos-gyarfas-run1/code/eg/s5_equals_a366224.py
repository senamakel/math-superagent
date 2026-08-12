"""Test the S5 = A366224 coincidence: count connected min-degree>=3 girth>=5
graphs at n=15,16 (A366224 predicts 149, 1670) and check whether every such
survivor is 3-connected (which would explain the identification with the
3-connected girth>=5 sequence)."""
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
    """Exactly 3-vertex-connected: connected and no 2-vertex separator."""
    if not nx.is_connected(G):
        return False
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            H = G.copy()
            H.remove_node(nodes[i])
            H.remove_node(nodes[j])
            if not nx.is_connected(H):
                return False
    return True

def count(n):
    cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    surv = 0
    not3con = 0
    for g6 in proc.stdout.splitlines():
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if min_degree(G) < 3:
            continue
        g = bfs_girth(G)
        if g is not None and g >= 5:
            surv += 1
            if not is_3connected(G):
                not3con += 1
                print(f"  n={n}: girth>=5 but NOT 3-connected: {g6}", flush=True)
    print(f"n={n}: girth>=5_survivors={surv}  (A366224 predicts 149@15, 1670@16)  non_3connected={not3con}", flush=True)

if __name__ == "__main__":
    for n in [15, 16]:
        count(n)