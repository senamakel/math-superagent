"""Independent check of the Mycielski edge-count transition.

The library notes (oeis-mycielski-catalogue-check claim; scholar-digest) state
the transition as (v,e) -> (2v+1, 4e+v), and simultaneously cite the values
C5=(5,5), M(C5)=(11,20), M^2(C5)=(23,71). 4*5+5 = 25 != 20, so this is an
internal inconsistency.  Compute the TRUE Mycielski edge count from the
construction and see which closed form the terms match.

Mycielski construction of G = (V,E), n=|V|, m=|E|:
  vertices: V, plus twin u_i per vertex, plus apex w
  edges:    E, plus for each edge v_i v_j the two cross edges u_i v_j, u_j v_i,
            plus the apex star w u_i for every twin.
=> |V'| = 2n+1, |E'| = m + 2m + n = 3m + n.
"""
import networkx as nx
from itertools import combinations


def mycielski_edgecount(n, edges):
    """Return (V', E') counts of the Mycielski graph built from the n-vertex
    graph whose edges are the edge list `edges` (0-indexed vertex labels)."""
    # vertices 0..n-1 originals, n..2n-1 twins (twin of i is n+i), 2n apex
    E = set()
    for (a, b) in edges:
        E.add((a, b))                      # original
        E.add((n + a, b))                  # cross u_a - v_b
        E.add((n + b, a))                  # cross u_b - v_a
    for i in range(n):
        E.add((2 * n, n + i))              # apex star
    return 2 * n + 1, len(E)


def c5():
    return 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]


def main():
    # build the chain from C5
    n, edges = c5()
    chain = []
    for k in range(5):
        chain.append((n, len(edges)))
        n, edges = mycielski_edgecount(n, edges)

    print("Mycielski chain (v, e) from C5:")
    for k, t in enumerate(chain):
        print(f"  M{k} (M^k(C5)): {t}")

    print("\nOEIS A122695 expects edges 0,0,1,5,20,71,236,755")
    print("   -> M(C5)=20, M^2(C5)=71, M^3(C5)=236")
    print("   -> our computed e =", [t[1] for t in chain[:4]], "...")

    # Test both candidate transitions from the (5,5) seed on vertices.
    v, e = 5, 5
    print("\nvertices via (2v+1):", [v := 2*v+1 for _ in range(4)])
    v, e = 5, 5
    ee3 = []
    for _ in range(4):
        v, e = 2*v+1, 3*e + v_old_after  # placeholder guard
    # redo cleanly:
    v, e = 5, 5
    ee3 = [(5,5)]
    for _ in range(4):
        v, e = 2*v+1, 3*e + (v-1)//2   # v here is OLD v (before update)
        ee3.append((v,e))
    v, e = 5, 5
    ee4 = [(5,5)]
    for _ in range(4):
        v, e = 2*v+1, 4*e + (v-1)//2
        ee4.append((v,e))

    print("(2v+1, 3e+v) chain:", ee3)
    print("(2v+1, 4e+v) chain:", ee4)
    match3 = all(a[1]==b[1] for a,b in zip(chain[:5], ee3[:5]))
    match4 = all(a[1]==b[1] for a,b in zip(chain[:5], ee4[:5]))
    print("\nDoes 3e+v reproduce the computed edge counts?", match3)
    print("Does 4e+v reproduce the computed edge counts?", match4)


if __name__ == "__main__":
    main()
