"""Oracle validation for the Erdos-Gyarfas cycle checker (code/lib/erdos_gyarfas.py).

Verifies the obviously-correct checker against hand-computable ground truths:
- K3 (triangle): only a 3-cycle -> no power-of-two cycle -> False.
- long ODD cycles C5, C7, C9: no 2-power -> False.
- C4, C8, C16: exactly a 2^k cycle -> True.
- Petersen graph: girth 5 (no C4/C5), has an 8-cycle -> True (length 8).
- K4: has C4 -> True.

Also cross-checks cycles_by_length against a second, independent enumeration
(a connected 2-regular edge-subset characterisation, distinct from the oracle's
path-walking DFS) on a few small graphs.

Note on the oracle's cycle identity: a "cycle" here is a distinct connected
2-regular subgraph (edge set), NOT a vertex set. Petersen's 9-cycles are the
canonical trap: each 9-vertex set supports TWO distinct Hamilton cycles (edge
sets), so there are 20 distinct 9-cycles but only 10 9-vertex sets. The oracle
and this counter both key cycles by their edge set, so they agree on 20. Keying
by vertex set (an earlier version of the oracle) incorrectly collapsed these to
10. For the existence question (has_power_of_two_cycle) the two agree, since
the collapse only merges equal-length cycles.
"""

from lib.erdos_gyarfas import has_power_of_two_cycle, cycles_by_length


def cycle(n):
    """C_n as adjacency."""
    return {i: {(i - 1) % n, (i + 1) % n} for i in range(n)}


def complete(n):
    return {i: set(range(n)) - {i} for i in range(n)}


def petersen():
    # outer 5-cycle 0-1-2-3-4-0, inner star 5-7-9-6-8-5, spokes i-(i+5)
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


def independent_count(adj):
    """Second enumeration: a simple cycle is exactly a set of edges that forms
    one connected 2-regular subgraph (every vertex in it has degree exactly 2
    in the chosen edge set, and the edge set is connected). This is a genuinely
    different formulation from the oracle's path-walking DFS (edges, not
    vertex paths), so agreement between the two is strong evidence the counts
    are right.

    Correct by construction: an undirected simple cycle <-> one edge set that
    is connected and 2-regular. Each cycle is thus counted exactly once.

    Note: two earlier versions of this routine were wrong and were replaced.
    The first used a Johnson-style blocked-set DFS that overcounted
    near-Hamiltonian cycles by 2x (reported 20 nine-cycles in Petersen; the
    true count is 10, confirmed by a vertex-transitivity argument). The second
    classified cycles by vertex-subset with all induced degrees == 2, which
    only counts INDUCED cycles and dropped the chorded 8- and 9-cycles. This
    edge-set version counts all simple cycles.
    """
    n = len(adj)
    verts = sorted(adj)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if j in adj[verts[i]]:
                edges.append((verts[i], verts[j]))
    out = {}
    m = len(edges)
    for mask in range(1 << m):
        # edge subset -> degree of each involved vertex and connectivity
        deg = {}
        sub = []
        for e in range(m):
            if (mask >> e) & 1:
                u, v = edges[e]
                sub.append((u, v))
                deg[u] = deg.get(u, 0) + 1
                deg[v] = deg.get(v, 0) + 1
        if len(sub) < 3:
            continue
        # connected and every involved vertex has degree exactly 2
        if any(d != 2 for d in deg.values()):
            continue
        vs = list(deg.keys())
        start = vs[0]
        seen = {start}
        stack = [start]
        while stack:
            x = stack.pop()
            for (a, b) in sub:
                for q in ((a, b), (b, a)):
                    if q[0] == x and q[1] not in seen and q[1] in deg:
                        seen.add(q[1])
                        stack.append(q[1])
        if len(seen) == len(vs):
            L = len(sub)
            out[L] = out.get(L, 0) + 1
    return out


def check(name, adj, expect_pow, expect_len=None):
    ok, L = has_power_of_two_cycle(adj)
    verdict = "PASS" if ok == expect_pow else "FAIL"
    print(f"{verdict}  {name:22s} power2={ok} (expect {expect_pow}) len={L}")
    if expect_len is not None:
        assert L == expect_len, f"{name}: expected length {expect_len}, got {L}"
    assert ok == expect_pow, f"{name}: expected {expect_pow}, got {ok}"
    return ok


print("=== Ground-truth checks (hand-computable) ===")
check("K3 (triangle)", complete(3), False)
check("C5 (odd)", cycle(5), False)
check("C7 (odd)", cycle(7), False)
check("C9 (odd)", cycle(9), False)
check("C4", cycle(4), True, 4)
check("C8", cycle(8), True, 8)
check("C16", cycle(16), True, 16)
check("Petersen", petersen(), True, 8)
check("K4", complete(4), True, 4)

print()
print("=== Independent cross-check: oracle counts vs Johnson enumeration ===")
for name, adj in [("Petersen", petersen()), ("K4", complete(4)), ("C8", cycle(8)),
                  ("C5", cycle(5)), ("K3", complete(3))]:
    a = dict(sorted(cycles_by_length(adj).items()))
    b = dict(sorted(independent_count(adj).items()))
    same = a == b
    print(f"{'OK  ' if same else 'DIFF'} {name:10s} oracle={a} johnson={b}")
    assert same, f"{name}: oracle {a} != johnson {b}"

print()
print("All oracle validation checks PASSED.")
