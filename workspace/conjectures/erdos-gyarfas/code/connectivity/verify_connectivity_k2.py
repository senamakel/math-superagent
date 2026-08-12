"""Machine-verify the cut-vertex lobe cycle-set lemma for k=2 split types.

Lemma under test
----------------
Let G be glued from lobes L1, L2 that share only the cut vertex v; each lobe
Li = Ci ∪ {v} where Ci is a component of G - v and v's edges into Ci are
included.  Then EVERY simple cycle of G lies inside a single lobe, so

    cycle_lengths(G) == cycle_lengths(L1) ∪ cycle_lengths(L2).

Why a simple cycle cannot cross lobes: to leave one lobe and enter the other a
cycle would have to pass through v twice (the only connection between Ci and Cj
is v), repeating v.  A simple cycle through v must therefore use two DISTINCT
v-edges into the SAME lobe, and all its other edges stay in that lobe.  So
every simple cycle lives in L1 or in L2.

The two v-edges into one component must be DISTINCT (otherwise the only way in
and out of that lobe is the same edge, and going in and out on the same edge
would tread that edge twice — impossible in a simple cycle).  That is exactly
why the degree split types are constrained: v may have two edges into a
component only if they are distinct.

Cases built here (all k=2, sharing a single cut vertex v):
  A. type (1,2):  Markström lobe (1 edge to v) + Petersen lobe (2 edges to v).
                   d(v) = 3.
  B. type (2,2):  two prism lobes (triangular prism, 3-regular), each with
                   2 edges to v (to two distinct vertices).  d(v) = 4.
                   Checks delta >= 3 at every non-v vertex.
  C. type (2,2)  the "two-lobe" closed walk that DOES exist: go into L1, back
                   through v, into L2, back through v.  It has length
                   (path1) + (path2) + 4 = 2 + 2 + 4 = 8 and visits v three
                   times, so it repeats v and is NOT a simple cycle.  We print
                   the walk verbatim and confirm length 8 is absent from the
                   simple-cycle set of G.

In every case we assert cycle_lengths(G) == cycle_lengths(L1) ∪ cycle_lengths(L2)
using TWO independent enumerations:
  * lib.cycle_oracle.all_simple_cycles  (canonical-start DFS)
  * networkx.simple_cycles              (on the directed view)
and report whether both agree and whether the union assertion passes.

Complexity: enumerating every simple cycle is the small-instance oracle
(rule 9) — exponential in the worst case by design; the largest graph here is
the 25-vertex Markström+Petersen glue (cycle set = union of the two lobes),
small enough for exhaustive enumeration.  Purely a verification, not method.
"""
import networkx as nx

from lib.cycle_oracle import oracle

MARKSTROM_EDGES = [
    (0, 1), (0, 2), (0, 3), (1, 18), (1, 19), (2, 21), (2, 22), (3, 20),
    (3, 23), (4, 6), (4, 10), (4, 12), (5, 6), (5, 9), (5, 11), (6, 12),
    (7, 8), (7, 13), (7, 14), (8, 10), (8, 17), (9, 11), (9, 15), (10, 17),
    (11, 16), (12, 16), (13, 14), (13, 15), (14, 19), (15, 18), (16, 21),
    (17, 20), (18, 19), (19, 14), (20, 23), (21, 22), (22, 23), (23, 20),
]

MARKSTROM = "Markström graph (HoG 51419), 3-regular, cycle set {3,5,6,7,9..24}"
PETERSEN = "Petersen graph, 3-regular, cycle set {5,6,8,9}"
PRISM = "triangular prism, 3-regular, cycle set {3,4,5,6}"


def nx_cycle_lengths(G):
    """Independent route #2: networkx simple_cycles on the directed view."""
    return frozenset(
        len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3
    )


def build_lobe(inner_edges, touched, offset, v=0):
    """Lobe Li = (inner graph relabelled by +offset, on vertices >=1) plus the
    cut vertex v=0 connected to the (relabelled) touched vertices."""
    L = nx.Graph()
    L.add_node(v)                       # v = 0, shared by every lobe
    for (a, b) in inner_edges:
        L.add_edge(a + offset, b + offset)
    for t in touched:
        L.add_edge(v, t + offset)
    return L


def glue(lobes):
    """Union of lobes over the shared vertex v=0."""
    G = nx.Graph()
    for L in lobes:
        G.add_nodes_from(L.nodes())
        G.add_edges_from(L.edges())
    return G


def check_case(name, L1, L2, G):
    print(f"=== {name}")
    print(f"  n(G), m(G)          : {G.number_of_nodes()}, {G.number_of_edges()}")
    degs = [d for _, d in G.degree()]
    print(f"  min/max degree(G)   : {min(degs)}, {max(degs)}")
    nonv = [d for u, d in G.degree() if u != 0]
    # d(v) counted within G
    d_v = dict(G.degree())[0]
    print(f"  degree of v (=0)    : {d_v}")
    print(f"  min degree, non-v   : {min(nonv)}  (>= 3 check: {min(nonv) >= 3})")

    # two independent enumerations of the glued cycle set
    _, mine = oracle(G)          # lib.cycle_oracle
    mine_set = set(mine)
    theirs = nx_cycle_lengths(G)
    agree = mine_set == theirs
    print(f"  cycle_oracle == nx.simple_cycles : {agree}")
    if not agree:
        print("    oracle-only:", sorted(mine_set - theirs))
        print("    nx-only    :", sorted(theirs - mine_set))

    # per-lobe cycle sets (each lobe = C_i ∪ {v})
    _, l1 = oracle(L1)
    _, l2 = oracle(L2)
    set1, set2 = set(l1), set(l2)
    union = set1 | set2

    gift = set(mine_set)                     # G's cycle lengths, oracle route
    union_holds = gift == union
    print(f"  cycle_lengths(G) == union of lobe sets : {union_holds}")
    if not union_holds:
        print("    G-only   :", sorted(gift - union))
        print("    union-only:", sorted(union - gift))
    print(f"  lobe1 cycle set : {sorted(set1)}")
    print(f"  lobe2 cycle set : {sorted(set2)}")
    print(f"  G    cycle set  : {sorted(gift)}")
    print()

    both_agree = agree and union_holds
    # second body verifies equality too (belt-and-braces)
    union_holds_nx = theirs == union
    print(f"  union assertion via nx route        : {union_holds_nx}")
    return both_agree and union_holds_nx


def prism_edges():
    return [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5),
            (3, 4), (3, 5), (4, 5)]


def main():
    results = {}
    all_ok = True

    # ---------- A. type (1,2): Markström lobe (1 edge) + Petersen (2) -------
    n1 = 24
    L1 = build_lobe(MARKSTROM_EDGES, touched=[0], offset=1)          # v--Markström
    L2 = build_lobe(nx.petersen_graph().edges(), touched=[0, 1],
                    offset=1 + n1)                    # v--Petersen via 2 edges
    G = glue([L1, L2])
    okA = check_case("A. k=2 type (1,2): Markström(1 edge) + Petersen(2 edges)",
                     L1, L2, G)
    results["A (1,2) Markström+Petersen"] = okA
    all_ok &= okA

    # ---------- B. type (2,2): two prism lobes, 2 edges each, d(v)=4 -------
    Pr = prism_edges()                            # 6 vertices
    L1 = build_lobe(Pr, touched=[0, 4], offset=1)   # v-0, v-4 (distinct)
    L2 = build_lobe(Pr, touched=[0, 4], offset=1 + 6)
    G = glue([L1, L2])
    okB = check_case("B. k=2 type (2,2): two prism lobes, 2 distinct edges each",
                     L1, L2, G)
    results["B (2,2) two prisms"] = okB
    all_ok &= okB

    # ---------- C. the both-lobes closed walk is NOT a simple cycle -------
    print("=== C. the length-(path1+path2+4) closed walk through v is not "
          "a simple cycle")
    # In each prism lobe, v=0 is adjacent to inner vertices 0 and 4.
    # Shortest inner path 0 -> 4 in the prism (length 2):
    prism = nx.Graph(Pr)
    p1 = nx.shortest_path(prism, 0, 4)     # [0, mid, 4]
    off1, off2 = 1, 1 + 6
    a1, mid1, a2 = (p1[0] + off1, p1[1] + off1, p1[2] + off1)
    b1, mid2, b2 = (p1[0] + off2, p1[1] + off2, p1[2] + off2)
    closed_walk = [0, a1, mid1, a2, 0, b1, mid2, b2, 0]
    walk_len = len(closed_walk) - 1
    print(f"  shortest inner path 0->4 in prism : {p1}  (length {len(p1)-1})")
    print(f"  closed walk (vertices, v=0): {closed_walk}")
    print(f"  closed walk length : {walk_len} "
          f"(= {len(p1)-1}+{len(p1)-1}+4 = {2*(len(p1)-1)+4})")
    v_count = closed_walk.count(0)
    print(f"  v=0 appears {v_count} times -> repeats v -> "
          f"NOT a simple cycle: {v_count > 1}")
    # both-lobes walk verification: every step is an edge
    G = glue([build_lobe(Pr, [0, 4], 1), build_lobe(Pr, [0, 4], 7)])
    all_edges = [(closed_walk[i], closed_walk[i + 1])
                 for i in range(len(closed_walk) - 1)]
    steps_edges = all(G.has_edge(u, w) for u, w in all_edges)
    print(f"  every walk step is an edge of G     : {steps_edges}")
    # is its length in the simple-cycle set of G?  (must be ABSENT)
    _, mine = oracle(G)
    lens = set(mine)
    print(f"  {walk_len} in G's simple-cycle set        : {walk_len in lens} "
          f"(must be False: walk repeats v)")
    print(f"  G's simple-cycle set  : {sorted(lens)}")
    absent_ok = (walk_len not in lens) and (v_count > 1) and steps_edges
    results["C both-lobes walk excluded"] = absent_ok
    all_ok &= absent_ok
    print()

    print("=" * 72)
    for k, v in results.items():
        print(f"  {k:38s} -> {'PASS' if v else 'FAIL'}")
    print("=" * 72)
    print("ALL CLASSES PASS (both enumerations agree, union assertion holds, "
          "closed-walk excluded)" if all_ok else
          "SOME CLASS FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
