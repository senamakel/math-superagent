"""Identify the unique C4,C8-free member of the K4-expansion family at n=24,
and compare it against the Markstrom graph (HoG 51419)."""
import sys
import networkx as nx
from networkx import Graph

MARK = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"

def has_c4(G):
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        u = nodes[i]
        for j in range(i+1, len(nodes)):
            v = nodes[j]
            if len(set(G[u]) & set(G[v])) >= 2:
                return True
    return False

def has_c8(G):
    adj = {u: set(G[u]) for u in G}
    nodes = list(G)
    def search(s):
        def dfs(cur, used, depth):
            if depth == 7:
                return s in adj[cur]
            for nb in adj[cur]:
                if nb not in used:
                    used.add(nb)
                    if dfs(nb, used, depth+1):
                        return True
                    used.remove(nb)
            return False
        return dfs(s, {s}, 0)
    for s in nodes:
        if search(s):
            return True
    return False

def canon(G):
    return nx.to_graph6_bytes(G, header=False).decode().strip()

# scan the census
path = "/workspace/code/out/expansion_census/level_24_classes.txt"
found = []
with open(path) as f:
    for ln in f:
        ln = ln.strip()
        if not ln:
            continue
        H = nx.from_graph6_bytes(ln.encode())
        if not has_c4(H) and not has_c8(H):
            found.append(ln)

print("C4,C8-free members at n=24 in census:", len(found))
for g in found:
    print("  ", g)

# compare to Markstrom
M = nx.from_graph6_bytes(MARK.encode())
mcanon = canon(nx.convert_node_labels_to_integers(M))
print("Markstrom canonical:", mcanon)
for g in found:
    print("matches Markstrom:", g == mcanon)
