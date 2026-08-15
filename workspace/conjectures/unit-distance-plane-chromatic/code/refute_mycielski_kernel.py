#!/usr/bin/env python3
"""
Attack the sharp-kernel-4color / S-universe-4color conjecture:

  Every graph on <= N vertices with min-degree >= 4, K4-free, K_{2,3}-free,
  and every vertex-neighbourhood inducing max degree <= 2  is 4-colourable.

Planned refutation via the classic triangle-free 5-chromatic graph:
  Mycielski^2(C5).  Mycielski preserves triangle-freeness; Mycielski raises
  chromatic number by 1; C5 has chi 3 => Mycielski(C5)=Groetzsch has chi 4
  (11 vertices), Mycielski^2(C5) has chi 5 (23 vertices).
  Triangle-freeness implies: K4-free (true), and neighbourhood-maxdeg<=2
  (an edge among two neighbours of v forms triangle v-x-y: FALSE, so actually
  triangle-free => neighbourhood is an independent set, maxdeg 0 <= 2).  So
  the ONLY kernel condition such a graph can violate is K_{2,3}-freeness.

  If the 5-critical core of Mycielski^2(C5) satisfies all four kernel
  conditions, it is a member of C_23 that is not 4-colourable =>
  COUNTEREXAMPLE to sharp-kernel-4color at N=23.

All checks use the independent exact chromatic oracle (lib.critoracle) and the
calibrated SAT oracle (lib.satcolor).  Finite object construction, no search.
"""
from lib.satcolor import is_k_colorable as satcolor_k
from lib.critoracle import chrom, is_k_colorable as critoracle_k


def mycielski(edges):
    """Mycielski(G): for each v add a copy v'; add apex r universal to all
    copies.  Edges: keep G; add v'~r for all v; add u'~v' for each edge u~v
    of G (i.e. copy-adjacency mirrors G)."""
    n = max(max(e) for e in edges) + 1
    old = list(range(n))
    new = [n + i for i in range(n)]
    r = 2 * n
    eset = set(edges)
    adj = {v: set() for v in old}
    for (a, b) in edges:
        adj[a].add(b)
        adj[b].add(a)
    for v in old:
        eset.add((new[v], r))
        for u in adj[v]:
            if u > v:
                eset.add((new[v], new[u]))
    return eset


def c5():
    return {(i, (i + 1) % 5) for i in range(5)}


def norm(edges):
    eset = set(frozenset(e) for e in edges)
    return {tuple(sorted(e)) for e in eset}


def nverts(edges):
    return max(max(e) for e in edges) + 1


def triangle_free(edges):
    adj = {}
    for (a, b) in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    for a in adj:
        for b in adj[a]:
            if b in adj and (adj[a] & adj[b]):
                return False
    return True


def kernel_conditions(edges):
    n = nverts(edges)
    adj = [set() for _ in range(n)]
    for (a, b) in edges:
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
    k23 = False
    for a in range(n):
        for b in range(a + 1, n):
            if len(adj[a] & adj[b]) >= 3:
                k23 = True
    conds['K23-free'] = not k23
    nbmax = 0
    for v in range(n):
        nb = sorted(adj[v])
        for i in range(len(nb)):
            d = sum(1 for j in range(len(nb)) if j != i
                    and nb[j] in adj[nb[i]])
            nbmax = max(nbmax, d)
    conds['nbhd-maxdeg<=2'] = nbmax <= 2
    return conds


def min_degree(edges):
    n = nverts(edges)
    adj = [0] * n
    for (a, b) in edges:
        adj[a] += 1
        adj[b] += 1
    return min(adj)


def critical_core(edges):
    """Greedy vertex-delete while chi stays 5, leaving a 5-critical subgraph."""
    verts = set(range(nverts(edges)))
    eset = set(norm(edges))
    chi = chrom(nverts(edges), eset)
    while True:
        removed = False
        for v in sorted(verts):
            rest = verts - {v}
            idx = {u: i for i, u in enumerate(sorted(rest))}
            sub = {(idx[a], idx[b]) for (a, b) in eset
                   if a in idx and b in idx}
            if chrom(len(rest), sub) >= chi:
                verts = rest
                eset = sub
                removed = True
                break
        if not removed:
            break
    return verts, eset, chi


def main():
    print("=" * 70)
    print("Refutation: sharp-kernel-4color at N=23 via Mycielski^2(C5)")
    print("=" * 70)

    base = norm(c5())
    print("\nC5: n=%d, chi=%d, triangle-free=%s"
          % (nverts(base), chrom(5, base), triangle_free(base)))

    g = norm(mycielski(base))   # Groetzsch
    gn = nverts(g)
    print("Mycielski(C5)=Groetzsch: n=%d, edges=%d, chi=%d, triangle-free=%s"
          % (gn, len(g), chrom(gn, g), triangle_free(g)))

    m = norm(mycielski(g))      # Mycielski^2(C5)
    mn = nverts(m)
    print("Mycielski^2(C5): n=%d, edges=%d, chi=%d, triangle-free=%s"
          % (mn, len(m), chrom(mn, m), triangle_free(m)))

    # 5-critical core
    verts, core, chi = critical_core(m)
    print("\n5-critical core: n=%d, edges=%d, min-degree=%d, chi=%d"
          % (len(verts), len(core), min_degree(core), chi))
    conds = kernel_conditions(core)
    for k, v in conds.items():
        print("   %-16s = %s" % (k, v))

    sat4, _ = satcolor_k(sorted(core), 4, len(verts))
    print("   4-colourable (SAT oracle) = %s" % sat4)
    crit4 = critoracle_k(len(verts), sorted(core), 4)
    print("   4-colourable (critoracle) = %s" % crit4)

    if not crit4 and all(conds.values()):
        print("\n>>> COUNTEREXAMPLE CONFIRMED:")
        print(">>> The 5-critical core of Mycielski^2(C5), a graph on %d" % len(verts))
        print(">>> vertices, satisfies ALL FOUR kernel conditions (min-deg>=4,")
        print(">>> K4-free, K23-free, nbhd-maxdeg<=2) yet is NOT 4-colourable.")
        print(">>> => sharp-kernel-4color is FALSE at N=%d." % len(verts))
    else:
        print("\nNo counterexample: some kernel condition failed, or it is")
        print("4-colourable.  Which conditions failed:", conds)


if __name__ == "__main__":
    main()
