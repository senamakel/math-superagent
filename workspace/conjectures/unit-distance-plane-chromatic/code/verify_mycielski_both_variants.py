#!/usr/bin/env python3
"""
Close the construction-choice question.  Two textbook variants of "the
Mycielskian" circulate:
  (A) canonical/no-mirror: preserve G, add cross u_i--v_j & u_j--v_i, star
      w--u_i.  3|E| + n edges.  This is the run's kernel (M^2(C5)=23v/71e
      matches the captured verdict) and gives the Groetzsch graph
      Mycielski(C5)=11v/20e (a known catalogue value).
  (B) mirror variant: additionally u_i--u_j for each v_i--v_j edge.
      4|E| + n edges.
The verdict record has e=71 for M^2, so the run used (A).  This script shows
that the K2,3 obstruction is robust: BOTH variants of M^k(C5), k>=2, contain
a K2,3, so the conclusion (not unit-distance realizable) does not depend on
which standard construction is meant.
"""
import urllib.request  # noqa: F401  (unused; graph is constructed by code)


def mycielski_a(edges):
    n = max(max(e) for e in edges) + 1
    U = [n + i for i in range(n)]
    w = 2 * n
    out = set(edges)
    for (a, b) in edges:
        out.add(tuple(sorted((U[a], b))))
        out.add(tuple(sorted((U[b], a))))
    for i in range(n):
        out.add(tuple(sorted((U[i], w))))
    return {tuple(sorted(e)) for e in out}


def mycielski_b(edges):
    """Mirror variant: also add twin-to-twin edges u_i--u_j for v_i--v_j."""
    n = max(max(e) for e in edges) + 1
    U = [n + i for i in range(n)]
    w = 2 * n
    out = set(edges)                 # original
    out |= {tuple(sorted((U[a], U[b]))) for (a, b) in edges}  # mirror
    for (a, b) in edges:
        out.add(tuple(sorted((U[a], b))))
        out.add(tuple(sorted((U[b], a))))
    for i in range(n):
        out.add(tuple(sorted((U[i], w))))
    return {tuple(sorted(e)) for e in out}


def nv(edges):
    return max(max(e) for e in edges) + 1


def adj(edges):
    n = nv(edges)
    A = [set() for _ in range(n)]
    for a, b in edges:
        A[a].add(b)
        A[b].add(a)
    return A


def find_k23(edges):
    A = adj(edges)
    n = len(A)
    for a in range(n):
        for b in range(a + 1, n):
            c = A[a] & A[b]
            if len(c) >= 3:
                return (a, b, sorted(c))
    return None


def c5():
    return {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}


print("Groetzsch graph fact:  Mycielski(C5) is the well-known Groetzsch graph.")
print("Catalogue value: 11 vertices, 20 edges, triangle-free, chi=4.\n")

for name, mu in (("A no-mirror (run's kernel)", mycielski_a),
                 ("B mirror variant", mycielski_b)):
    print("=== variant %s ===" % name)
    m = c5()
    for k in range(4):
        if k > 0:
            m = mu(m)
        e = len(m)
        res = find_k23(m)
        print("  M^%-2d |V|=%-3d |E|=%-4d  K2,3-free=%s  %s"
              % (k, nv(m), e, res is None,
                 res if res is None else (res[0], res[1], res[2][:4])))
    print()
