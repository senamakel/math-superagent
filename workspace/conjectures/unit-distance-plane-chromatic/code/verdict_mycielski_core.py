#!/usr/bin/env python3
"""
Final verdict witness: confirm the real Mycielski^2(C5) 5-critical-core facts
and locate an explicit K_{2,3} subgraph violating the sharp-kernel K2,3-free
condition.
"""
from lib.satcolor import is_k_colorable
from diag_mycielski import (mycielski, norm, nverts, chrom, triangle_free,
                            min_degree)


def c5():
    return norm({(i, (i + 1) % 5) for i in range(5)})


def find_k23(edges):
    n = nverts(edges)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    for a in range(n):
        for b in range(a + 1, n):
            common = adj[a] & adj[b]
            if len(common) >= 3:
                return (a, b, sorted(common)[:3])
    return None


def main():
    m = norm(mycielski(norm(mycielski(c5()))))   # Mycielski^2(C5)
    n = nverts(m)
    chi = chrom(m)
    print("Mycielski^2(C5): n=%d e=%d chi=%d triangle-free=%s min-degree=%d"
          % (n, len(m), chi, triangle_free(m), min_degree(m)))

    # 5-criticality: is every single-vertex deletion 4-colourable?
    def is_k(edges, k):
        return is_k_colorable(sorted(edges), k, nverts(edges))[0]

    all_crit = True
    for v in range(n):
        rem = norm({e for e in m if v not in e})
        idx = {u: i for i, u in enumerate(sorted(rem and
               set(range(nverts(rem))) or {0}))}
        # reindex
        vv = sorted({u for e in m for u in e if u != v})
        idx = {u: i for i, u in enumerate(vv)}
        sub = {(idx[a], idx[b]) for (a, b) in m if a != v and b != v}
        if not is_k(sub, 4):
            all_crit = False
            print("  NOT critical at v=%d (G-v not 4-colourable)" % v)
    print("is 5-critical (every G-v 4-colourable): %s" % all_crit)

    print("not 4-colourable: %s" % (not is_k(m, 4)))
    print("5-colourable: %s" % is_k(m, 5))

    k23 = find_k23(m)
    print("explicit K2,3 subgraph: %s  => K2,3-free = %s"
          % (k23, k23 is None))

    conds = {}
    adj = [set() for _ in range(n)]
    for a, b in m:
        adj[a].add(b)
        adj[b].add(a)
    conds['min-deg>=4'] = all(len(x) >= 4 for x in adj)
    conds['K4-free'] = not any(len(adj[a] & adj[b] & adj[c]) >= 1
                               for a in range(n) for b in range(a+1, n)
                               for c in range(b+1, n)
                               if b in adj[a] and c in adj[a] and c in adj[b])
    conds['K2,3-free'] = k23 is None
    nbmax = 0
    for v in range(n):
        nb = sorted(adj[v])
        nbmax = max(nbmax, max(
            (sum(1 for j in range(len(nb)) if j != i and nb[j] in adj[nb[i]])
             for i in range(len(nb))), default=0))
    conds['nbhd-maxdeg<=2'] = nbmax <= 2
    for k, v in conds.items():
        print("   %-16s = %s" % (k, v))
    print("=> all four kernel conditions: %s" % all(conds.values()))


if __name__ == "__main__":
    main()
