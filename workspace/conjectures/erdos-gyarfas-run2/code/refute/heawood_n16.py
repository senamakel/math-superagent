"""Refutation probe for the settled rung R-delta3-n16-three-targets:
every delta>=3 graph on <=16 vertices has a 4/8/16-cycle.

The sharpest candidate counterexample is a girth-6 cubic graph on <=16
vertices (girth 6 kills the 4-cycle; n<=16 kills the 16-cycle), so the whole
rung rests on whether such a graph has an 8-cycle. The smallest cubic girth-6
graph is the Heawood graph (n=14, the (3,6)-cage). If Heawood has no 8-cycle,
R-delta3-n16-three-targets is FALSE.

Also probe the other small cages / bipartite cubic graphs on <=16 vertices and
the Petersen case for the n<=12 rung.
"""
from lib.erdos_gyarfas import has_power_of_two_cycle, cycles_by_length


def heawood():
    """The Heawood graph: incidence graph of the Fano plane. 14 vertices,
    cubic, bipartite, girth 6."""
    # points 0..6, lines 7..13.  line i is {i, i+1, i+3} mod 7.
    adj = {v: set() for v in range(14)}
    for i in range(7):
        for p in ((i) % 7, (i + 1) % 7, (i + 3) % 7):
            adj[i].add(7 + p)
            adj[7 + p].add(i)
    return adj


def petersen():
    adj = {i: set() for i in range(10)}
    outer = [0, 1, 2, 3, 4]
    for a, b in zip(outer, outer[1:] + outer[:1]):
        adj[a].add(b); adj[b].add(a)
    inner = [5, 7, 9, 6, 8]
    for a, b in zip(inner, inner[1:] + inner[:1]):
        adj[a].add(b); adj[b].add(a)
    for i in range(5):
        adj[i].add(i + 5); adj[i + 5].add(i)
    return adj


def girth(adj):
    from collections import deque
    best = float("inf")
    for s in adj:
        dist = {s: 0}; parent = {s: None}; dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1; parent[v] = u; dq.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


for name, G in [("Heawood", heawood()), ("Petersen", petersen())]:
    n = len(G)
    deg = sorted(len(nb) for nb in G.values())
    has, L = has_power_of_two_cycle(G)
    cl = cycles_by_length(G)
    targets = {k: cl.get(k, 0) for k in (4, 8, 16)}
    print(f"{name}: n={n} deg={deg[0]}..{deg[-1]} girth={girth(G)}")
    print(f"   has 4/8/16-cycle: {has} (returned len {L})   counts={targets}")
    print(f"   -> {'REFUTES n<=16 rung' if not has else 'consistent with rung'}")
