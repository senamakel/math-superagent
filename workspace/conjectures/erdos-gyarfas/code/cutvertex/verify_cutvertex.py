"""Machine-verify the cut-vertex lobe clauses of the run's new
Cut-Vertex Characterization theorem, plus the oracle's worked examples.

Theorem clauses under test (v is a cut vertex of a graph G; C_1..C_k are the
components of G-v; lobe L_i = induced subgraph of G on C_i ∪ {v}):

  (a) Every simple cycle of G lies entirely inside a single lobe.  A cycle
      avoiding v lives inside one connected component; a cycle through v must
      use its two v-edges into the SAME component (else the v-free path inside
      the cycle would connect two lobes), so it too lies in one lobe.  Hence
        cycle_lengths(G) == union_i cycle_lengths(L_i).
  (b) If G has no power-of-two cycle then no lobe has one  (a lobe's cycles
      are G's cycles, so pow2(L_i) ⊆ pow2(G)).
  (c) Every vertex of a component C_i has all its neighbours inside its own
      lobe:  d_{L_i}(w) == d_G(w)  for every w in C_i  (each L_i is an induced
      subgraph, so this holds for any cut vertex; load-bearing nonetheless).

Constructions:
  I.  Worked examples: K4 {3,4}, K3,3 {4,6}, cube Q3 {4,6,8}, Petersen
      {5,6,8,9} — assert the oracle reproduces them exactly.
  II. Two lobes at a cut vertex: Petersen+K4, K4+K4 (each lobe from a small
      cubic graph H with vertex x removed, v reconnected to N_H(x)).
  III.Three lobes at one central cut vertex: 3x Petersen, 3x prism, and a
      Petersen+prism+K4 mix.
  IV. Random graphs given a forced cut vertex: two-lobe and three-lobe random
      inner graphs, several seeds.

Every cycle enumerated exactly with lib.cycle_oracle.all_simple_cycles and
cross-checked against networkx simple_cycles.  Pure exact integer arithmetic.

Complexity: cycle enumeration is the small-instance oracle (rule 9),
exponential by design — the largest graph here is the 33-vertex 3x Petersen
glue plus random two/three-lobe graphs of modest size; purely a verification.
"""
import random
import networkx as nx

from lib.cycle_oracle import oracle, all_simple_cycles

POWERS_OF_TWO = {2 ** k for k in range(2, 10)}  # 4, 8, 16, 32, ...


def power_of_two(lengths):
    return sorted(p for p in POWERS_OF_TWO if p in lengths)


def nx_cycle_lengths(G):
    """Independent route #2: networkx simple_cycles on the directed view,
    length >= 3.  Must agree with lib.cycle_oracle."""
    return frozenset(
        len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3
    )


def build_lobe(H, x, offset):
    """Lobe from a base graph H and a distinguished vertex x: the lobe is
    (H - x) relabelled by +offset around the shared cut vertex v=0, with v=0
    joined to the relabelled neighbours of x.  Returns the lobe graph and the
    number of inner (non-v) vertices (= |V(H)| - 1).
    """
    L = nx.Graph()
    L.add_node(0)                       # v, shared by every lobe
    for a, b in H.edges():
        if a != x and b != x:
            L.add_edge(a + offset, b + offset)
    for nb in H[x]:
        L.add_edge(0, nb + offset)
    return L, H.number_of_nodes() - 1


def glue(lobes):
    """Union of lobes over the shared vertex v=0."""
    G = nx.Graph()
    for L in lobes:
        G.add_nodes_from(L.nodes())
        G.add_edges_from(L.edges())
    return G


def lobes_of(G, v):
    """Components C_i of G-v and the lobes L_i = G[C_i ∪ {v}]."""
    Gmv = nx.Graph(G)
    Gmv.remove_node(v)
    comps = list(nx.connected_components(Gmv))
    lobes = [G.subgraph(C | {v}).copy() for C in comps]
    return comps, lobes


def check_clauses(name, G, v, want_cut=True):
    """Check clauses (a),(b),(c) for cut vertex v of G.  Returns (all_ok, dict)."""
    print(f"=== {name}")
    n, m = G.number_of_nodes(), G.number_of_edges()
    degs = [d for _, d in G.degree()]
    print(f"  n, m, min/max degree: {n}, {m}, {min(degs)}/{max(degs)}")

    comps, lobes = lobes_of(G, v)
    is_cut = len(comps) >= 2
    print(f"  d(v)={dict(G.degree())[v]}  |G-v components|={len(comps)}  "
          f"cut vertex={is_cut}")
    if want_cut and not is_cut:
        print("  FAIL: v is not a cut vertex (cannot test lobe structure)")
        return False, {}

    # --- independent cycle-set agreement -------------------------------
    _, mine = oracle(G)
    mine_set = set(mine)
    theirs = nx_cycle_lengths(G)
    agree = mine_set == theirs
    print(f"  cycle_oracle == nx.simple_cycles: {agree}")
    if not agree:
        print("    oracle-only:", sorted(mine_set - theirs))
        print("    nx-only    :", sorted(theirs - mine_set))

    # --- clause (a): every simple cycle inside a single lobe ------------
    comp_index = {}
    for i, C in enumerate(comps):
        for u in C:
            comp_index[u] = i
    cycles = all_simple_cycles(G)
    a_ok = True
    for c in cycles:
        verts = list(c)
        # component indices of all vertices other than v
        idxs = [comp_index[u] for u in verts if u != v]
        same_lobe = len(set(idxs)) == 1        # all non-v vertices in one component
        if same_lobe:
            pass
        else:
            a_ok = False
            print(f"    FAIL(a): cycle {c} spans components {idxs}")
        if v in verts:
            # A simple cycle through v uses exactly two edges of the cycle
            # incident to v (v appears once): equivalently v has exactly two
            # neighbours on the cycle.  Clause (a) for a v-cycle then holds
            # iff all its non-v vertices lie in ONE component (so both
            # v-edges go into the same lobe).
            vn = sum(1 for u in verts if G.has_edge(v, u))
            if len(set(idxs)) == 1 and vn == 2:
                pass
            else:
                a_ok = False
                print(f"    FAIL(a): v-cycle {verts} vn={vn} "
                      f"components={set(idxs)}")
    # union consequence: cycle_lengths(G) == union_i cycle_lengths(L_i)
    lobe_sets = [set(oracle(L)[1]) for L in lobes]
    union = set().union(*lobe_sets) if lobe_sets else set()
    union_holds = mine_set == union
    if not union_holds:
        a_ok = False
        print("    FAIL(a-union): G-only:", sorted(mine_set - union),
              " union-only:", sorted(union - mine_set))
    print(f"  clause (a) every simple cycle in a single lobe: "
          f"{'PASS' if a_ok and union_holds else 'FAIL'}")
    print(f"    G cycle set: {sorted(mine_set)}")
    for i, (C, L) in enumerate(zip(comps, lobes)):
        print(f"    lobe{i} ({len(L)} vtx, |C|={len(C)}) cycles: "
              f"{sorted(set(oracle(L)[1]))}  pow2: {power_of_two(set(oracle(L)[1]))}")

    # --- clause (b): G no pow2 cycle  ==>  no lobe has one ---------------
    g_pow2 = set(power_of_two(mine_set))
    b_ok = True
    if not g_pow2:
        for i, L in enumerate(lobes):
            lp = set(oracle(L)[1]) & POWERS_OF_TWO
            if lp:
                b_ok = False
                print(f"    FAIL(b): G pow2-free but lobe{i} has pow2 {sorted(lp)}")
    # stronger general form (always checkable): lobe pow2 cycles are G cycles
    all_lobe_pow2_in_G = all(
        (set(oracle(L)[1]) & POWERS_OF_TWO) <= g_pow2 for L in lobes
    )
    b_ok = b_ok and all_lobe_pow2_in_G
    print(f"  clause (b) pow2-free G => pow2-free lobes (and lobe-pow2 ⊆ G-pow2): "
          f"{'PASS' if b_ok else 'FAIL'}")
    print(f"    G pow2 cycles: {sorted(g_pow2)}")

    # --- clause (c): d_{L_i}(w) == d_G(w) for every w in C_i -------------
    c_ok = True
    for i, (C, L) in enumerate(zip(comps, lobes)):
        for w in C:
            if L.degree(w) != G.degree(w):
                c_ok = False
                print(f"    FAIL(c): w={w} in C_{i} d_L={L.degree(w)} d_G={G.degree(w)}")
    print(f"  clause (c) d_L(w)==d_G(w) for every w in every C_i: "
          f"{'PASS' if c_ok else 'FAIL'}")

    all_ok = agree and a_ok and union_holds and b_ok and c_ok and is_cut
    print(f"  => {'PASS' if all_ok else 'FAIL'}")
    print()
    return all_ok, {"agree": agree, "a": a_ok, "union": union_holds,
                    "b": b_ok, "c": c_ok, "cut": is_cut}


def worked_examples():
    """Task 1: reproduce the oracle's worked examples."""
    print("=" * 72)
    print("TASK 1 — oracle worked examples")
    print("=" * 72)
    cases = {
        "K4": (nx.complete_graph(4), {3, 4}),
        "K3,3": (nx.complete_bipartite_graph(3, 3), {4, 6}),
        "cube Q3": (nx.hypercube_graph(3), {4, 6, 8}),
        "Petersen": (nx.petersen_graph(), {5, 6, 8, 9}),
    }
    all_ok = True
    for name, (G, expected) in cases.items():
        got = oracle(G)
        ok = set(got[1]) == expected and got[0] == 3
        all_ok &= ok
        print(f"  {name:10s} min_deg={got[0]} cycles={got[1]} "
              f"expected={sorted(expected)} -> {'MATCH' if ok else 'MISMATCH'}")
    print()
    return all_ok


def main():
    results = {}
    all_ok = True

    ok = worked_examples()
    results["T1 worked examples"] = ok
    all_ok &= ok

    print("=" * 72)
    print("TASK 2 — cut-vertex lobe clauses")
    print("=" * 72)

    K4 = nx.complete_graph(4)
    Pet = nx.petersen_graph()
    prism = nx.Graph()
    prism.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5),
                          (3, 4), (3, 5), (4, 5)])

    # --- II. two lobes at a cut vertex ---------------------------------
    for name, (H1, H2, x1, x2) in {
        "IIa 2 lobes: Petersen + K4": (Pet, K4, 0, 0),
        "IIb 2 lobes: K4 + K4": (K4, K4, 0, 0),
        "IIc 2 lobes: prism + prism": (prism, prism, 0, 0),
    }.items():
        L1, n1 = build_lobe(H1, x1, 1)
        L2, n2 = build_lobe(H2, x2, 1 + n1)
        G = glue([L1, L2])
        ok, _ = check_clauses(name, G, 0)
        results[name] = ok
        all_ok &= ok

    # --- III. three lobes at one central cut vertex ---------------------
    for name, (Hs, xs) in {
        "IIIa 3 lobes: 3x Petersen": ([Pet, Pet, Pet], [0, 0, 0]),
        "IIIb 3 lobes: 3x prism": ([prism, prism, prism], [0, 0, 0]),
        "IIIc 3 lobes: Petersen+prism+K4": ([Pet, prism, K4], [0, 0, 0]),
    }.items():
        off, lobes = 1, []
        for H, x in zip(Hs, xs):
            L, n_in = build_lobe(H, x, off)
            lobes.append(L)
            off += n_in
        G = glue(lobes)
        ok, _ = check_clauses(name, G, 0)
        results[name] = ok
        all_ok &= ok

    # --- IV. random graphs with a forced cut vertex ----------------------
    rng = random.Random(20250602)
    for t in range(4):
        # two random lobes, random sizes and edge densities
        k1 = rng.randint(4, 8)
        k2 = rng.randint(4, 8)
        p = rng.uniform(0.4, 0.8)
        H1 = nx.gnp_random_graph(k1, p, seed=rng)
        H2 = nx.gnp_random_graph(k2, p, seed=rng)
        while not H1.number_of_edges(): H1 = nx.gnp_random_graph(k1, p, seed=rng)
        while not H2.number_of_edges(): H2 = nx.gnp_random_graph(k2, p, seed=rng)
        L1, n1 = build_lobe(H1, 0, 1)
        L2, n2 = build_lobe(H2, 0, 1 + n1)
        G = glue([L1, L2])
        ok, _ = check_clauses(f"IV-rnd{t} 2 lobes (rand k={k1},{k2}, p≈{p:.2f})",
                              G, 0)
        results[f"IV-rnd{t} 2 lobes"] = ok
        all_ok &= ok
    for t in range(3):
        ks = [rng.randint(4, 7) for _ in range(3)]
        p = rng.uniform(0.4, 0.8)
        off, lobes = 1, []
        for k in ks:
            H = nx.gnp_random_graph(k, p, seed=rng)
            while not H.number_of_edges():
                H = nx.gnp_random_graph(k, p, seed=rng)
            L, n_in = build_lobe(H, 0, off)
            lobes.append(L)
            off += n_in
        G = glue(lobes)
        ok, _ = check_clauses(f"IV-rnd{t} 3 lobes (rand ks={ks}, p≈{p:.2f})",
                              G, 0)
        results[f"IV-rnd{t} 3 lobes"] = ok
        all_ok &= ok

    print("=" * 72)
    for k, v in results.items():
        print(f"  {k:38s} -> {'PASS' if v else 'FAIL'}")
    print("=" * 72)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
