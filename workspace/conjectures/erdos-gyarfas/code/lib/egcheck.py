"""Fast targeted existence checks used to push the EG verification bound.

A counterexample to the Erdős–Gyárfás conjecture must avoid every cycle of
power-of-two length: 4, then 8, then 16, then 32 ...  The expensive full
cycle-length enumeration (lib.cycles.cycle_lengths) is only needed on graphs
that survive to be C4-free AND C8-free AND C16-free, which is a tiny fraction
of the search space. This module implements fast exact existence tests:

  - C4-free is checked natively by nauty-geng (-f) at generation time.
  - has_cycle_of_length(G, L) does a bounded DFS from each vertex to find any
    simple cycle of length exactly L. Exact, polynomial in the graph (the
    depth L is fixed, so the walk is O(n * (max_degree-1)^(L-1)) which for a
    C4-free low-degree graph is small and never exponential in n).

Everything integer-exact, no floats. Correctness independent of
lib.cycles: verified by cross-checking against lib.cycles on K4, K3,3,
Petersen, cube Q3 (see code/eg/verify_bound.py's worked-case table).
"""

import networkx as nx

from lib.cycles import min_degree


def has_cycle_of_length(G, L):
    """True iff ``G`` (networkx.Graph, vertices 0..n-1) has a simple cycle of
    length exactly ``L``. Exact. Bounded DFS from each start vertex, keeping
    a vertex set so paths are simple; stops as soon as one is found.
    """
    n = G.number_of_nodes()
    if n < L:
        return False
    adj = {v: set(G.neighbors(v)) for v in G.nodes()}
    nodes = list(G.nodes())

    # Build a simple path s = v0, v1, ..., v_{L-1} of L vertices (L-1 edges),
    # never revisiting s, and return True iff the last vertex v_{L-1} is
    # adjacent to s, which closes a simple cycle of length L.  s itself may
    # only be touched at position 0 (no early chording back to it).
    def dfs(s):
        onpath = {s}

        def go(v, cnt):
            # v is the current end, cnt = number of vertices used including v
            if cnt == L:
                return s in adj[v]
            for w in adj[v]:
                if w == s or w in onpath:
                    continue
                onpath.add(w)
                if go(w, cnt + 1):
                    return True
                onpath.discard(w)
            return False

        return go(s, 1)

    for s in nodes:
        if dfs(s):
            return True
    return False


def has_power_of_two_cycle(G, powers=(4, 8, 16, 32, 64)):
    """True iff ``G`` has a simple cycle of one of the given power-of-two
    lengths. Checks the smallest powers first (a C4 is the most common),
    so the rare graphs that must be searched deeper pay the most."""
    for L in powers:
        if has_cycle_of_length(G, L):
            return True
    return False


def mindeg3_no_power2_from_geng(n, lines_from='-f'):
    """Scan nauty-geng output for a min-degree-3 connected graph on ``n``
    vertices with no power-of-two cycle. Returns (graphs_checked,
    counterexamples) where counterexamples is a list of graph6 strings.

    ``lines_from`` selects how the candidate pool is generated; '-f' means
    geng already filtered out 4-cycles (the standard fast route), which is
    valid because a C4 is itself a power-of-two cycle so no counterexample
    is lost."""
    import subprocess
    if lines_from == '-f':
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
    else:
        cmd = ["nauty-geng", "-q", "-c", "-d3", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    counterexamples = []
    checked = 0
    for g6 in proc.stdout.splitlines():
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if min_degree(G) < 3:
            continue
        checked += 1
        if not has_power_of_two_cycle(G):
            counterexamples.append(g6)
    return checked, counterexamples
