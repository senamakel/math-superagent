"""Independently count nonisomorphic 2-connected graphs on n vertices (small n),
to check the ear-decomposition generator's counts (1,1,4,19,121 for n=3..7).

A graph is 2-connected iff removal of any single vertex leaves it connected
(and it has >=3 vertices). We enumerate all graphs on n labelled vertices that
are 2-connected, then deduplicate by a brute-force canonical label.

Brute force over all n-choose-2 edge subsets; exponential by design, small n only.
"""
from itertools import combinations

def canonical(n, edges):
    """lexicographically smallest upper-triangular adjacency string over all perms."""
    best = None
    for p in permutations(range(n)):
        bits = []
        for a in range(n):
            for b in range(a+1, n):
                u, v = p[a], p[b]
                bits.append((min(u,v), max(u,v)) in edges)
        s = "".join("1" if b else "0" for b in bits)
        if best is None or s < best:
            best = s
    return best

def is_2connected(n, edges):
    if n < 3:
        return False
    # build adjacency
    adj = {i: set() for i in range(n)}
    for (u, v) in edges:
        adj[u].add(v); adj[v].add(u)
    # check connected after removing each single vertex
    for r in range(n):
        # BFS in G - r
        seen = set()
        # start at any vertex != r
        starts = [v for v in range(n) if v != r]
        if not starts:
            return False
        stack = [starts[0]]
        seen.add(starts[0])
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y != r and y not in seen:
                    seen.add(y); stack.append(y)
        if len(seen) != n - 1:
            return False
    return True

from itertools import permutations

for n in range(3, 8):
    V = list(range(n))
    all_e = list(combinations(V, 2))
    classes = set()
    for mask in range(1 << len(all_e)):
        edges = set()
        for i, e in enumerate(all_e):
            if (mask >> i) & 1:
                edges.add(e)
        if is_2connected(n, edges):
            classes.add(canonical(n, edges))
    print(f"n={n}: {len(classes)} nonisomorphic 2-connected graphs")
