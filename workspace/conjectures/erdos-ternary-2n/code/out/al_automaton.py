#!/usr/bin/env python3
"""
Abram-Lagarias p-adic path set automaton for C(1,M_1,...,M_n).

Implements Algorithm A (presentation for C(1,M), M==1 mod 3) and
Algorithm B (label product for multiple M_i) from:
  W. Abram, J.C. Lagarias, "Intersections of multiplicative translates of
  3-adic Cantor sets", arXiv:1308.3133, Thm 1.6, Thm 3.1, Thm 3.3.

Vertices are carry states N (0 <= N <= M/2 for Algorithm A); a vertex tuple
(N_1,...,N_n) for the label product.  Edges labelled a in {0,1} allowed when
a + N_i == 0 or 1 (mod 3) for every component, moving to
  N_i' = floor((N_i + M_i * a)/3).

Methods here: build automaton, count states, count strongly connected
components, compute Perron eigenvalue b (dim_H = log_3 b).
"""

def algo_A(M):
    """Presentation (states, edges) for C(1,M) with M == 1 mod 3.
    Returns (states: dict int->id, edges: dict (state_id, a)->target_id).
    Right-resolving: at most one target per (state, label)."""
    assert M % 3 == 1, "Algorithm A requires M == 1 (mod 3)"
    states = {0: 0}          # vertex label -> id
    ids = {0: 0}
    next_id = 1
    edges = {}               # (sid, label) -> target_sid
    # worklist of vertex labels
    frontier = [0]
    while frontier:
        N = frontier.pop()
        sid = ids[N]
        for a in (0, 1):
            if (a + N) % 3 in (0, 1):           # criterion (3.2)
                Np = (N + M * a) // 3           # update (3.3)
                if Np not in ids:
                    ids[Np] = next_id
                    next_id += 1
                    frontier.append(Np)
                edges[(sid, a)] = ids[Np]
    # reverse map
    rev = {v: k for k, v in ids.items()}
    return ids, edges, rev


def algo_B(ms):
    """Label product of the presentations of C(1,M_i).
    ms: list of M_i, each == 1 mod 3.
    Returns (states tuple->id, edges (sid,label)->target_sid)."""
    single = [algo_A(m) for m in ms]

    # vertex tuple (N_1,...,N_n); each component label set
    init = tuple(0 for _ in ms)
    ids = {init: 0}
    next_id = 1
    edges = {}
    frontier = [init]
    while frontier:
        tup = frontier.pop()
        sid = ids[tup]
        # possible labels a
        for a in (0, 1):
            nt = []
            ok = True
            for j, (idsj, edgesj, revj) in enumerate(single):
                Nj = tup[j]
                if (a + Nj) % 3 not in (0, 1):
                    ok = False
                    break
                nt.append((Nj + ms[j] * a) // 3)
            if not ok:
                continue
            nt = tuple(nt)
            if nt not in ids:
                ids[nt] = next_id
                next_id += 1
                frontier.append(nt)
            edges[(sid, a)] = ids[nt]
    return ids, edges


def scc_count(n, edges):
    """Count strongly connected components among n vertices."""
    import sys
    sys.setrecursionlimit(100000)
    adj = [[] for _ in range(n)]
    for (s, a), t in edges.items():
        adj[s].append(t)
    # Tarjan
    index = [0]*n; low = [0]*n; on = [False]*n; stack = []
    comps = 0; idx = [0]
    def strong(v):
        idx[0] += 1
        index[v] = low[v] = idx[0]
        stack.append(v); on[v] = True
        for w in adj[v]:
            if index[w] == 0:
                strong(w); low[v] = min(low[v], low[w])
            elif on[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            nonlocal comps
            comps += 1
            while True:
                w = stack.pop(); on[w] = False
                if w == v: break
    for v in range(n):
        if index[v] == 0:
            strong(v)
    return comps


def perron_eigenvalue(n, edges):
    """Spectral radius (Perron eigenvalue) of adjacency matrix."""
    import numpy as np
    A = np.zeros((n, n))
    for (s, a), t in edges.items():
        A[s, t] += 1
    if n == 0:
        return 0.0
    vals = np.linalg.eigvals(A)
    return float(max(abs(v) for v in vals))


if __name__ == "__main__":
    # ---- Verification against the paper's worked examples ----
    # Example 3.2: C(1,7) -> 4 vertices, dim = log_3(phi)
    for M, expect in [(7, 4), (19, 8)]:
        ids, edges, rev = algo_A(M)
        n = len(ids)
        print(f"C(1,{M}): states={n} (paper: {expect})  "
              f"{'OK' if n == expect else 'MISMATCH'}")
    # Example 3.4: C(1,7,19) -> 6 vertices  (7,19 both ==1 mod 3)
    ids, edges = algo_B([7, 19])
    print(f"C(1,7,19): states={len(ids)} (paper: 6)  "
          f"{'OK' if len(ids) == 6 else 'MISMATCH'}")
    # C(1,4)=C(1,2^2): paper Table 5.2 dim 0.438018 => beta=phi=1.618
    ids, edges = algo_B([4])
    b = perron_eigenvalue(len(ids), edges)
    import math
    print(f"C(1,4): states={len(ids)} dim={math.log(b,3):.6f} "
          f"(paper 0.438018) {'OK' if abs(math.log(b,3)-0.438018)<1e-3 else '?'}")
    # C(1,16), C(1,64) even powers
    for M in [16, 64, 256]:
        ids, edges = algo_B([M])
        b = perron_eigenvalue(len(ids), edges)
        print(f"C(1,{M}): states={len(ids)} dim={math.log(b,3):.6f}")
    # C(1,2^8) per Table 5.2 dim 0.287416
    ids, edges = algo_B([256])
    b = perron_eigenvalue(len(ids), edges)
    print(f"C(1,256=2^8): dim={math.log(b,3):.6f} (paper 0.287416)")
