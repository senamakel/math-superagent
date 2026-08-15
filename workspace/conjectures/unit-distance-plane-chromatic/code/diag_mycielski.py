#!/usr/bin/env python3
"""
Independent check of the correct textbook Mycielski construction and whether
a genuine Mycielski^2(C5) 5-critical core satisfies the four sharp-kernel
conditions.  Kept separate from the (suspected broken) refute script so the
correct-construction facts can be pinned down.

Standard Mycielski(G): G on v_1..v_n shape vertices, add copies u_1..u_n, and
apex w.
  * keep edges of G                                   (|E|)
  * u_i u_j in E(G)  ->  edge u_i u_j                 (|E|, mirror)
  * u_i v_j in E(G)  ->  edges u_i v_j and u_j v_i    (2|E|, cross)
  * w u_i for all i                                   (n)
Total = |E| + |E| + 2|E| + n = 4|E| + n.
For C5: 4*5+5 = 25 edges, 11 vertices.
"""
from lib.satcolor import is_k_colorable


def norm(edges):
    return {tuple(sorted(e)) for e in edges}


def mycielski(edges):
    n = max(max(e) for e in edges) + 1
    V = range(n)
    U = [n + i for i in range(n)]
    w = 2 * n
    E = norm(edges)
    out = set(E)
    # cross: u_i v_j  (for each edge v_i v_j): u_i adj v_j and u_j adj v_i
    for (a, b) in E:
        out.add(tuple(sorted((U[a], b))))
        out.add(tuple(sorted((U[b], a))))
    # star: apex w adjacent to every u_i
    for i in V:
        out.add(tuple(sorted((U[i], w))))
    return out


def nverts(edges):
    return max(max(e) for e in edges) + 1


def triangle_free(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    for a in adj:
        for b in adj[a]:
            if b in adj and (adj[a] & adj[b]):
                return False
    return True


def min_degree(edges):
    n = nverts(edges)
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return min(deg)


def is_k_col(edges, k):
    n = nverts(edges)
    return is_k_colorable(sorted(edges), k, n)[0]


def chrom(edges):
    n = nverts(edges)
    for k in range(1, n + 1):
        if is_k_col(edges, k):
            return k
    return n


def kernel_conditions(edges):
    n = nverts(edges)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    conds = {}
    conds['deg>=4'] = all(len(adj[v]) >= 4 for v in range(n))
    k4 = False
    for a in range(n):
        for b in range(a + 1, n):
            if b not in adj[a]:
                continue
            for c in range(b + 1, n):
                if c in adj[a] and c in adj[b]:
                    for d in range(c + 1, n):
                        if d in adj[a] and d in adj[b] and d in adj[c]:
                            k4 = True
    conds['K4-free'] = not k4
    k23 = any(len(adj[a] & adj[b]) >= 3
              for a in range(n) for b in range(a + 1, n))
    conds['K23-free'] = not k23
    nbmax = 0
    for v in range(n):
        nb = sorted(adj[v])
        for i in range(len(nb)):
            d = sum(1 for j in range(len(nb)) if j != i and nb[j] in adj[nb[i]])
            nbmax = max(nbmax, d)
    conds['nbhd-maxdeg<=2'] = nbmax <= 2
    return conds


def critical_core(edges):
    """Greedy vertex-delete while chi stays 5, leaving a 5-critical subgraph."""
    eset = norm(edges)
    verts = set(range(nverts(eset)))
    chi = chrom(eset)
    while True:
        removed = False
        for v in sorted(verts):
            rest = verts - {v}
            idx = {u: i for i, u in enumerate(sorted(rest))}
            sub = {(idx[a], idx[b]) for (a, b) in eset
                   if a in idx and b in idx}
            if chrom(sub) >= chi:
                verts = rest
                eset = sub
                removed = True
                break
        if not removed:
            break
    return verts, eset, chi


def main():
    # C5
    c5 = norm({(i, (i + 1) % 5) for i in range(5)})
    print("C5: n=%d e=%d chi=%d triangle-free=%s"
          % (nverts(c5), len(c5), chrom(c5), triangle_free(c5)))

    # Groetzsch = Mycielski(C5)
    g = norm(mycielski(c5))
    print("Mycielski(C5): n=%d e=%d chi=%d triangle-free=%s"
          % (nverts(g), len(g), chrom(g), triangle_free(g)))

    # Mycielski^2(C5)
    m = norm(mycielski(g))
    print("Mycielski^2(C5): n=%d e=%d chi=%d triangle-free=%s"
          % (nverts(m), len(m), chrom(m), triangle_free(m)))

    # 5-critical core of Mycielski^2(C5)
    verts, core, chi = critical_core(m)
    print("\n5-critical core: n=%d e=%d min-degree=%d chi=%d"
          % (len(verts), len(core), min_degree(core), chi))
    conds = kernel_conditions(core)
    for k, v in conds.items():
        print("   %-16s = %s" % (k, v))
    print("=> all four kernel conditions: %s" % all(conds.values()))


if __name__ == "__main__":
    main()
