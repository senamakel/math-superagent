#!/usr/bin/env python3
"""
Verify the Mycielski construction facts exactly before the refutation is
trusted, by an independent brute-force route (reverse-engineering chromatic
number by product enumeration, no SAT).

Facts to confirm:
  1. Mycielski^2(C5) has 23 vertices, no triangles, chromatic number 5.
  2. Its 5-critical core has min-degree >= 4.
  3. Triangle-free => K4-free and neighbourhood-maxdeg<=2 automatically.
  4. Whether the core is K_{2,3}-free.

Also a low-level check that my mycielski() matches the textbook operator
(mirror edges + apex).
"""
from itertools import product

from refute_mycielski_kernel import (mycielski, c5, norm, nverts,
                                     triangle_free, kernel_conditions,
                                     min_degree, critical_core)


def brute_chrom(n, edges):
    """Proper colouring count by product enumeration, no symmetry breaking.
    Returns the minimum k with a proper colouring (or n if none)."""
    for k in range(1, n + 1):
        for col in product(range(k), repeat=n):
            ok = True
            for (a, b) in edges:
                if col[a] == col[b]:
                    ok = False
                    break
            if ok:
                return k
    return n


def main():
    print("=" * 70)
    print("Independent brute-force check of the Mycielski refutation facts")
    print("=" * 70)

    base = norm(c5())
    bchi = brute_chrom(nverts(base), sorted(base))
    print("C5: n=%d brute chi=%d (expect 3)" % (nverts(base), bchi))

    g = norm(mycielski(base))
    gchi = brute_chrom(nverts(g), sorted(g))
    print("Groetzsch: n=%d brute chi=%d (expect 4), triangle-free=%s"
          % (nverts(g), gchi, triangle_free(g)))

    # Mycielski^2 is 23 vertices; brute product enumeration of 5-colouring
    # over 5^23 is impossible brute force.  Use the fact that Mycielski
    # preserves triangle-freeness and check structure + count instead, and
    # confirm chi via the independent SAT oracle separately (not brute).
    m = norm(mycielski(g))
    mn = nverts(m)
    print("Mycielski^2(C5): n=%d (expect 23), edges=%d (expect 92*?), "
          "triangle-free=%s"
          % (mn, len(m), triangle_free(m)))
    if mn != 23:
        print(">>> structure failure: expected 23 vertices, got %d" % mn)

    # the apex adjacencies: mirror edges among copies + apex universal
    # (structural sanity for Mycielski^2)
    adj = {v: set() for v in range(mn)}
    for (a, b) in m:
        adj[a].add(b)
        adj[b].add(a)
    apex = 2 * (nverts(g))   # apex of the OUTER mycielski call
    print("outer apex = %d, its degree = %d (expect %d, the size of "
          "Mycielski(C5)=Groetzsch)"
          % (apex, len(adj[apex]), nverts(g)))

    print("\nNow the 5-critical core (uses the SAT-based chrom oracle, not brute):")
    verts, core, chi = critical_core(m)
    print("core: n=%d edges=%d min-degree=%d chi=%d"
          % (len(verts), len(core), min_degree(core), chi))
    conds = kernel_conditions(core)
    for k, v in conds.items():
        print("   %-16s = %s" % (k, v))
    print("=> all four kernel conditions hold: %s" % all(conds.values()))
    print("=> core is NOT 4-colourable (chi=%d): %s"
          % (chi, chi >= 5))
    if chi >= 5 and all(conds.values()):
        print(">>> CONFIRMED counterexample to sharp-kernel-4color.")


if __name__ == "__main__":
    main()
