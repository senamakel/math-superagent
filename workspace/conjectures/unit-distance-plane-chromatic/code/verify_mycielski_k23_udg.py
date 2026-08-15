#!/usr/bin/env python3
"""
Confirm M^k(C5) (k = 2,3,4) is NOT unit-distance realizable, as a direct
consequence of the sharp-kernel K2,3-freeness lemma.

Method and the mathematical fact it rests on:
  The run's certified structural lemma (code/out/sharp_nbhd_cert.captured.txt)
  states: EVERY unit-distance graph is K2,3-free.  Proof: if u,w are distinct
  vertices at squared distance d^2>0, then the set {x : |x-u|=|x-w|=1} is the
  intersection of two unit circles centred d apart, which is empty or two
  points; hence any two vertices share at most 2 common neighbours, so no
  K2,3 subgraph (which needs two vertices sharing >=3 common neighbours)
  occurs.  This is a pure geometry/exact-algebra fact -- it involves NO
  colouring oracle and NO chromatic-number computation.

  Therefore: K2,3-free is NECESSARY for unit-distance realizability.  If some
  M^k(C5) contains a K2,3 subgraph, it cannot be realized as a unit-distance
  graph, regardless of its chromatic number and independent of any
  colouring test.

  The Mycielski construction used here is the correct textbook version
  (Rudnicki--Stewart 2011, Mycielski 1955): original vertices v_i, a twin
  u_i per vertex, a root w; edges = E(G) + {u_i u_j : v_i v_j in E(G)} is NOT
  included (standard version has NO twin-to-twin edges) + {u_i v_j, u_j v_i :
  v_i v_j in E(G)} (cross) + {w u_i}.  Total = |E| + 2|E| + n = 3|E| + n.
  For C5 (n=5,|E|=5): Mycielski(C5)=Groetzsch 3*5+5=20 edges, 11 vertices;
  Mycielski^2(C5): 3*20+11=71 edges, 23 vertices.  These match the captured
  verdict (n=23 e=71), so this IS the construction the run's kernel used.

  M^{k+1} contains M^k as an induced subgraph on the original-vertex subset
  (the construction keeps every edge of G among the original vertices), so a
  K2,3 found in M^2 is still present in M^3 and M^4: the obstruction
  propagates by containment, no per-level re-hunt needed (though we verify
  each level independently anyway).

Complexity: graph construction O(n+m); K2,3 scan is O(n^2 * deg) worst case
with n <= 3*2^4-1 = 47, trivial.  No exponential work, no colouring solver.
"""
from itertools import combinations


def norm(edges):
    return {tuple(sorted(e)) for e in edges}


def mycielski(edges):
    """Correct textbook Mycielskian: original + twins + root, cross edges,
    star.  3|E| + n edges total (no twin-to-twin mirror edges)."""
    edges = norm(edges)
    n = max(max(e) for e in edges) + 1
    U = [n + i for i in range(n)]
    w = 2 * n
    out = set()
    out |= edges                       # original edges kept
    for (a, b) in edges:               # cross: u_i--v_j, u_j--v_i
        out.add(tuple(sorted((U[a], b))))
        out.add(tuple(sorted((U[b], a))))
    for i in range(n):                 # star: w--u_i
        out.add(tuple(sorted((U[i], w))))
    return norm(out)


def nverts(edges):
    return max(max(e) for e in edges) + 1 if edges else 0


def adj_lists(edges):
    n = nverts(edges)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def find_k23(edges):
    """Find (a, b, [three common neighbours]) with a<b, or None."""
    adj = adj_lists(edges)
    n = len(adj)
    for a in range(n):
        for b in range(a + 1, n):
            common = adj[a] & adj[b]
            if len(common) >= 3:
                return (a, b, sorted(common)[:3])
    return None


def contains_k23(edges):
    return find_k23(edges) is not None


def c5():
    return norm({(i, (i + 1) % 5) for i in range(5)})


def main():
    print("=" * 72)
    print("M^k(C5) unit-distance realizability via K2,3-freeness lemma")
    print("=" * 72)

    # Re-verify the leaf lemma statement numerically is a theorem, but the
    # real content: K2,3-free is necessary for UDG (sharp_nbhd_cert PASS).
    print("\n[lemma]  K2,3-free is NECESSARY for unit-distance realizability")
    print("  source: code/out/sharp_nbhd_cert.captured.txt (ALL CERTIFICATES PASS)")
    print("  content: two unit circles meet in <=2 points => any two UDG")
    print("           vertices share <=2 common neighbours => no K2,3.")
    print("  NOTE: geometric theorem; involves NO colouring oracle.")

    # Build M^0..M^4 where M^k = Mycielskian applied k times to C5.
    levels = [c5()]
    for _ in range(4):
        levels.append(norm(mycielski(levels[-1])))
    print("\n[build]  textbook Mycielski (3|E|+n per step, no twin-mirror)")
    print("  %-5s %-6s %-7s %-6s" % ("M^k", "|V|", "|E|", "chi"))
    expected = {0: 3, 1: 4, 2: 5, 3: 6, 4: 7}
    for k in range(5):
        n = nverts(levels[k])
        e = len(levels[k])
        print("  M^%-4d %-6d %-7d  %s" % (k, n, e, expected[k]))

    # Independent edge-count cross-check via recurrence + closed form
    # (each Mycielski step: V -> 2V+1, |E| -> 3|E| + V)
    print("\n[counts cross-check]")
    vv, ee = 5, 5
    for k in range(0, 5):
        if k > 0:
            ee, vv = 3 * ee + vv, 2 * vv + 1
        closed_V = 6 * (2 ** k) - 1   # V_{k+1}=2V_k+1 with V_0=5 => 6*2^k-1
        print("  M^%d: V=%d,  edge-recurrence |E|=%d" % (k, vv, ee))
        assert vv == closed_V, "vertex-count mismatch"

    # Find explicit K2,3 in M^2, M^3, M^4 (the k>=2 claimed levels)
    print("\n[K2,3 hunt] explicit subgraph (a, b, [3 common neighbours]):")
    for k in (0, 1, 2, 3, 4):
        cur = levels[k]
        k23 = find_k23(cur)
        ok = k23 is not None
        print("  M^%-4d K2,3-free? %-5s  explicit subgraph: %s"
              % (k, "NO" if ok else "yes", k23))
        if k == 2 and k23 is not None:
            a, b, common = k23
            eset = levels[k]
            print("     M^2 K2,3 cross-edges (all six must be present):")
            for c in common:
                assert tuple(sorted((a, c))) in eset, "edge a-c missing"
                assert tuple(sorted((b, c))) in eset, "edge b-c missing"
                print("        {a=%d,%s=c%d} and {b=%d,c=%d}  (both present)"
                      % (a, "", c, b, c))
            print("     => vertex %d and vertex %d share %d common "
                  "neighbours %s"
                  % (a, b, len(common), common))

    # Show M^1 (Groetzsch) for contrast -- is IT K2,3-free?
    g = levels[1]
    print("\n[contrast] Groetzsch = Mycielski(C5)=M^1: |V|=%d |E|=%d, "
          "K2,3-free=%s"
          % (nverts(g), len(g), not contains_k23(g)))
    if not contains_k23(g):
        print("  => Groetzsch is K2,3-free (as a UDG it would not be")
        print("     disqualified by this lemma; the obstruction starts at M^2).")

    # CONSEQUENCE statement
    print("\n" + "=" * 72)
    print("CONCLUSION")
    print("=" * 72)
    print("M^k(C5) for k = 2, 3, 4 (Mycielskian applied k times) each contain")
    print("an explicit K2,3 subgraph.")
    print("Since EVERY unit-distance graph is K2,3-free (certified geometric")
    print("lemma, sharp_nbhd_cert), the kernel disqualification of M^k(C5)")
    print("IS a direct consequence of the K2,3-freeness lemma: no colouring")
    print("oracle, SAT solver, or chromatic-number computation is involved.")
    print("The obstruction does NOT depend on any colouring assumption.")


if __name__ == "__main__":
    main()
