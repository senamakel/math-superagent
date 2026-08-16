"""Mechanical check of the Gebendorfer preprint's abstract claim.

The abstract of Gebendorfer, "A Proof of the Erdős–Gyárfás Conjecture"
(https://doi.org/10.5281/zenodo.18232846) claims: for girth >= 5, an 8-cycle
exists via 'fold forcing'. Also its girth-3 dichotomy implies a 4- or 8-cycle
always appears. Together these imply every δ>=3 graph has a 4- or 8-cycle.

That is a mechanically checkable claim with a known refutation available in the
library: Exoo's G420 / the 78-vertex no-{4,8,16} cubic graph / Markström's
24-vertex cubic graphs with no C4 and C8. If any δ>=3 graph has no 4- or 8-cycle,
the 'forces a 4- or 8-cycle' reading of the preprint is wrong.

We test the specific claim 'girth >= 5 forces an 8-cycle' on the small
cage-like graphs we can build: the Petersen graph (girth 5, cubic). If Petersen
has no 8-cycle, the girth>=5 => 8-cycle claim is false. (Petersen has girth 5
and is a minimal counterexample to the 'girth>=5 forces 8-cycle' claim if it
has no C8.)
"""

from lib.erdos_gyarfas import has_power_of_two_cycle, cycles_by_length


def petersen():
    # Standard Petersen graph: outer 5-cycle, inner 5-cycle, spokes.
    adj = {i: set() for i in range(10)}
    for i in range(5):
        adj[i].add((i + 1) % 5)
        adj[(i + 1) % 5].add(i)
        j = 5 + i
        adj[i].add(j)
        adj[j].add(i)
        adj[5 + i].add(5 + ((i + 2) % 5))
        adj[5 + ((i + 2) % 5)].add(5 + i)
    return adj


def girth(adj):
    # BFS from each vertex; first back-edge gives a cycle.
    from collections import deque
    n = len(adj)
    best = float("inf")
    for s in adj:
        dist = {s: 0}
        parent = {s: None}
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    dq.append(v)
                elif parent[u] != v:
                    cand = dist[u] + dist[v] + 1
                    if cand < best:
                        best = cand
    return best


def octahedral_core():  # not needed
    pass


if __name__ == "__main__":
    G = petersen()
    print("girth:", girth(G))
    has, ln = has_power_of_two_cycle(G)
    print("has 4/8/16-cycle:", has, ln)
    cl = cycles_by_length(G)
    print("cycles by length (4,8,16):", {k: cl.get(k, 0) for k in (4, 8, 16)})
    print("claims: Petersen has an 8-cycle? ->", 8 in cl and cl[8] > 0)
