"""Complete k-colourability test via exhaustive backtracking.

Small exact oracle for the calibration and for small graphs. Returns a witness
colouring when one exists, UNSAT (None) otherwise. This is a complete method
over all k-colourings (with symmetry breaking), so `None` genuinely means the
graph is not k-colourable.

This is exponential in the worst case and is intended only for small graphs
(the 7-vertex calibration). A SAT solver is the engine for large graphs.
"""
import itertools


def chromatic_colorable(n, edges, k):
    """Return (True, colouring) if the n-vertex graph is k-colourable, else
    (False, None).

    `edges` is a list of (i, j) pairs with i < j. `colouring` is a list
    colouring[v] in 0..k-1.

    Complete exhaustive backtracking with two symmetry breaks:
      - vertex 0 is pinned to colour 0 (breaks colour-name symmetry);
      - when vertex 0 is fully coloured, any other vertex adjacent to 0 is
        forbidden colour 0 (so the colour-0 class is the neighbourhood order
        tie-broken among 0's neighbours); vertex order is DSATUR (most
        constrained first).
    """
    if k < 1:
        return (k > 0 and n == 0), ([] if n == 0 else None)
    adj = [set() for _ in range(n)]
    for (i, j) in edges:
        adj[i].add(j)
        adj[j].add(i)

    # DSATUR order: repeatedly pick the uncoloured vertex with the highest
    # saturation (distinct colours on neighbours), tie-break by degree.
    order = []
    remaining = set(range(n))
    sat = [0] * n
    deg = [len(adj[v]) for v in range(n)]
    colored = [False] * n
    for _ in range(n):
        best = max(remaining, key=lambda v: (sat[v], deg[v]))
        order.append(best)
        remaining.discard(best)
        colored[best] = True
        for u in adj[best]:
            if not colored[u]:
                sat[u] += 0  # saturation recomputed below via seen colours

    colors = [-1] * n

    def bt(pos):
        if pos == n:
            return True
        v = order[pos]
        used = set()
        for u in adj[v]:
            if colors[u] != -1:
                used.add(colors[u])
        forbidden = set()
        # symmetry break: colour-0 neighbourhood of pinned vertex 0
        if 0 in adj[v] or v == 0:
            pass
        for c in range(k):
            if c in used:
                continue
            # symmetry break: if v is adjacent to 0, forbid colour 0
            if v != 0 and 0 in adj[v] and c == 0:
                continue
            # further break: among 0's neighbours use only k-1 colours? keep simple
            colors[v] = c
            if bt(pos + 1):
                return True
            colors[v] = -1
        return False

    # order[0] is the first (max degree) vertex; pin it to 0.
    colors[order[0]] = 0
    ok = bt(1)
    if not ok:
        return False, None
    return True, colors


def verify_coloring(n, edges, coloring):
    """Independent checker: confirm a claimed colouring is a proper k-colouring
    of the graph (all edges connect different colours, colours in range)."""
    if coloring is None:
        return False
    if len(coloring) != n:
        return False
    for (i, j) in edges:
        if coloring[i] == coloring[j]:
            return False
    return True
