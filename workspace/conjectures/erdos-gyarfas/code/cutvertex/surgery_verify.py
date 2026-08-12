"""Verify the surgery identities behind the run's new cut-vertex exclusion
theorem, by exact computation with lib.cycle_oracle.all_simple_cycles (the
exact multiset of simple-cycle lengths).

The theorem handles a glue of k lobes onto a central cut vertex v.  These
scripts check the surgery moves that delete v and reconnect the lobes with
cross edges, i.e. the moves that would be needed to build a smaller
power-of-two-free graph from a counterexample -- each move must FAIL to
preserve the power-of-two-free invariant, which is precisely what these
identities record.

Base graphs (each 3-regular): K4, triangular prism, Petersen, and one random
connected cubic graph (networkx random_regular_graph(3,8)), chosen small so
brute-force simple-cycle enumeration stays cheap.  For each base B, copies of
B (disjoint relabellings) are glued to a central vertex v.

  CASE A (k>=3 lobes, all single-edge):  G = v + 3 copies, v-u_i (one edge
      into each copy).  H = G - v + {u1u2, u1u3}.
      Assert (i) H simple, (ii) |V(H)| = |V(G)| - 1, (iii) min_deg(H) >= 3,
      (iv) every simple cycle of H is also a simple cycle of G (vertex-set
      multiset: each H-cycle's vertex set occurs among G-cycles).
      Structural reason (iv) holds: the two cross edges u1u2,u1u3 share u1,
      so any simple cycle using a cross edge would have to revisit u1 or use
      a cross edge twice -- impossible; hence every H-cycle is internal to a
      single copy, i.e. one of B's cycles, all of which survive in G.

  CASE B (k=2, (1,2)):  G = B1 + B2 + v, v adjacent to exactly one vertex x of
      B1 and two vertices y1,y2 of B2 (so d(v)=3).  H = G - v + {xy1, xy2}.
      Assert H simple, n(H)=n(G)-1, min_deg(H) >= 3, and the cycle-LENGTH
      MULTISET of H EQUALS that of G exactly.
      Structural reason: G's v-cycles are {v,y1,...,y2} with length |P|+2 for
      each simple y1-y2 path P in B2; H's cross-cycles are {x,y1,...,y2} with
      the same |P|+2.  Internal B-cycles are identical in both.  This is a
      length-preserving bijection, so the length multisets are equal.

  CASE C (k=2, (2,2)):  G = two copies, v adjacent to x1,x2 in B1 and
      y1,y2 in B2 (d(v)=4).  Confirm G itself has NO cycle using edges into
      both lobes (no cross-cycle: the only connection between the lobes is v,
      and a simple cycle through v can use its two v-edges into only one
      copy).  Then H1 = G - v + {x1y1, x2y2}.  Assert H1 simple, n(H1)=n(G)-1,
      min_deg(H1) >= 3, and every H1-cycle is either a G-cycle (vertex set
      present among G's cycles) or a cross-cycle whose length equals
      |P1| + |P2| + 2, where P1 is an x1-x2 path in B1 and P2 a y1-y2 path in
      B2.  The length formula is verified on every cross-cycle found by
      extracting the two copy-paths from the cycle's vertex sequence.

Every cycle is enumerated exactly with lib.cycle_oracle.all_simple_cycles
(canonical-start DFS; the cross-check against networkx is in the oracle's own
self-test).  Purely a verification -- the enumeration is the small-instance
oracle (rule 9), exponential by design; the largest graph here is the 3-copy
glue of ~30 vertices.
"""
import collections
import random

import networkx as nx

from lib.cycle_oracle import all_simple_cycles


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def min_deg(G):
    return min(G.degree(), key=lambda kv: kv[1])[1]


def copy_edges(base, offset):
    """Edges of base relabelled by +offset (each copy occupies a disjoint
    integer range starting at 'offset')."""
    return [(a + offset, b + offset) for a, b in base.edges()]


def is_simple_edge_list(edges):
    """True iff no self-loop and no parallel edge among the list."""
    seen = set()
    for a, b in edges:
        if a == b:
            return False
        k = frozenset((a, b))
        if k in seen:
            return False
        seen.add(k)
    return True


def length_counter(G):
    return collections.Counter(len(c) for c in all_simple_cycles(G))


def vertex_sets(G):
    return {frozenset(c) for c in all_simple_cycles(G)}


def in_range(label, off, n):
    return off <= label < off + n


# ---------------------------------------------------------------------------
# CASE A
# ---------------------------------------------------------------------------

def case_a(base):
    """Return (G, H, info) and a list of (label, ok) assertions."""
    n = base.number_of_nodes()
    offs = [1, 1 + n, 1 + 2 * n]

    ge = []
    for off in offs:
        ge += copy_edges(base, off)
    for off in offs:                       # v = 0 -> u_i (vertex 0 of copy i)
        ge.append((0, off))
    G = nx.Graph()
    G.add_edges_from(ge)

    u1, u2, u3 = offs
    he = [e for e in ge if 0 not in e]     # G - v
    he += [(u1, u2), (u1, u3)]             # + cross edges
    H = nx.Graph()
    H.add_edges_from(he)

    res = {}
    res["(i) H simple"] = is_simple_edge_list(he)
    res["(ii) |V(H)| = |V(G)| - 1"] = (H.number_of_nodes()
                                       == G.number_of_nodes() - 1)
    res["(iii) min_deg(H) >= 3"] = min_deg(H) >= 3

    gsets = vertex_sets(G)
    h_cycles = all_simple_cycles(H)
    bad = [c for c in h_cycles if frozenset(c) not in gsets]
    res["(iv) every H-cycle is a G-cycle (vertex set)"] = (len(bad) == 0
                                                           and len(h_cycles) > 0)

    info = {"nG": G.number_of_nodes(), "nH": H.number_of_nodes(),
            "min_degH": min_deg(H), "#cycH": len(h_cycles),
            "#cycG": len(all_simple_cycles(G)),
            "cross_cycles_in_H": sum(1 for c in h_cycles
                                     if frozenset(c) & {u2, u3} and u1 in c
                                     and len(set(c) & {u1, u2, u3}) > 1)}
    return G, H, res, info


# ---------------------------------------------------------------------------
# CASE B
# ---------------------------------------------------------------------------

def case_b(base):
    n = base.number_of_nodes()
    off1, off2 = 1, 1 + n

    ge = copy_edges(base, off1) + copy_edges(base, off2)
    x = off1                              # vertex 0 of copy1 (single touch)
    y1, y2 = off2, off2 + 1               # vertices 0,1 of copy2 (two touches)
    ge += [(0, x), (0, y1), (0, y2)]      # d(v) = 3, type (1,2)
    G = nx.Graph()
    G.add_edges_from(ge)

    he = [e for e in ge if 0 not in e]    # G - v
    he += [(x, y1), (x, y2)]              # cross edges
    H = nx.Graph()
    H.add_edges_from(he)

    res = {}
    res["H simple"] = is_simple_edge_list(he)
    res["|V(H)| = |V(G)| - 1"] = (H.number_of_nodes() == G.number_of_nodes() - 1)
    res["min_deg(H) >= 3"] = min_deg(H) >= 3
    # cycle-length multiset equality
    cG, cH = length_counter(G), length_counter(H)
    res["cycle-LENGTH multiset H == G"] = (cG == cH)

    info = {"nG": G.number_of_nodes(), "nH": H.number_of_nodes(),
            "min_degH": min_deg(H),
            "#cycG": sum(cG.values()), "#cycH": sum(cH.values()),
            "G_lengths": sorted(cG), "H_lengths": sorted(cH)}
    return G, H, res, info


# ---------------------------------------------------------------------------
# CASE C
# ---------------------------------------------------------------------------

def case_c(base):
    n = base.number_of_nodes()
    off1, off2 = 1, 1 + n

    ge = copy_edges(base, off1) + copy_edges(base, off2)
    x1, x2 = off1, off1 + 1               # two touches in copy1
    y1, y2 = off2, off2 + 1               # two touches in copy2
    ge += [(0, x1), (0, x2), (0, y1), (0, y2)]   # d(v) = 4, type (2,2)
    G = nx.Graph()
    G.add_edges_from(ge)

    # --- confirm G has no cross-cycle (cycle using edges into both lobes) ---
    cross = False
    for c in all_simple_cycles(G):
        verts = set(c) - {0}
        if verts and not (verts <= set(range(off1, off1 + n)) or
                          verts <= set(range(off2, off2 + n))):
            cross = True
            break
    res0 = {"G has NO cross-cycle": not cross}

    he = [e for e in ge if 0 not in e]    # G - v
    he += [(x1, y1), (x2, y2)]            # cross edges (disjoint pairs)
    H1 = nx.Graph()
    H1.add_edges_from(he)

    res = dict(res0)
    res["H1 simple"] = is_simple_edge_list(he)
    res["|V(H1)| = |V(G)| - 1"] = (H1.number_of_nodes()
                                   == G.number_of_nodes() - 1)
    res["min_deg(H1) >= 3"] = min_deg(H1) >= 3

    gsets = vertex_sets(G)
    cross_formula_ok = True
    cross_cycles = 0
    g_cycles = 0
    for c in all_simple_cycles(H1):
        uses_cross = any({a, b} <= {x1, y1} or {a, b} <= {x2, y2} or
                         {a, b} == {x1, y1} or {a, b} == {x2, y2}
                         for a, b in zip(c, c[1:] + c[:1]))
        # proper cross-edge detection: an H1 cycle edge is a cross edge iff
        # one endpoint in copy1 and the other in copy2
        def is_cross_edge(a, b):
            a1 = in_range(a, off1, n); a2 = in_range(a, off2, n)
            b1 = in_range(b, off1, n); b2 = in_range(b, off2, n)
            return (a1 and b2) or (a2 and b1)

        if frozenset(c) in gsets:
            g_cycles += 1
            continue
        # not a G-cycle: must be a cross-cycle and satisfy the length formula
        cross_cycles += 1
        if not any(is_cross_edge(a, b)
                   for a, b in zip(c, c[1:] + c[:1])):
            cross_formula_ok = False
            continue
        # extract the two copy-paths from the ordered vertex sequence
        # find the two cross edges as ordered consecutive pairs
        m = len(c)
        pos = [i for i in range(m)
               if is_cross_edge(c[i], c[(i + 1) % m])]
        if len(pos) != 2:
            cross_formula_ok = False
            continue
        i, j = pos
        # between edge i (c[i]->c[i+1]) and edge j (c[j]->c[j+1]): path1 from
        # c[i+1]..c[j], path2 from c[j+1]..c[i] (following order, mod m)
        path1 = [c[(i + 1 + t) % m] for t in range((j - i) % m)]
        path2 = [c[(j + 1 + t) % m] for t in range((i - j) % m)]
        P1_edges = (len(path1) - 1) if len(path1) else 0
        P2_edges = (len(path2) - 1) if len(path2) else 0
        if len(path1) == 0 or len(path2) == 0:
            cross_formula_ok = False
            continue
        if m != P1_edges + P2_edges + 2:
            cross_formula_ok = False
            continue
        # sanity: path1 all in one copy, path2 all in the other
        all1 = all(in_range(t, off1, n) for t in path1)
        all2 = all(in_range(t, off2, n) for t in path2)
        if not ((all1 and all2) or (all2 and all1)):
            cross_formula_ok = False

    res["every H1-cycle is G-cycle or cross-cycle with |P1|+|P2|+2"] = (
        cross_formula_ok and len(all_simple_cycles(H1)) > 0)

    info = {"nG": G.number_of_nodes(), "nH": H1.number_of_nodes(),
            "min_degH": min_deg(H1),
            "#cycG": len(all_simple_cycles(G)),
            "#cycH": len(all_simple_cycles(H1)),
            "#g_cycles_in_H": g_cycles, "#cross_cycles": cross_cycles,
            "touches": {"x1": x1, "x2": x2, "y1": y1, "y2": y2}}
    return G, H1, res, info


# ---------------------------------------------------------------------------
# base graphs
# ---------------------------------------------------------------------------

def prism():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3),
                      (0, 3), (1, 4), (2, 5)])
    return G


def random_cubic(n=8, seed=7):
    rng = random.Random(seed)
    cand = nx.random_regular_graph(3, n, seed=rng)
    # a component of a 3-regular graph is 3-regular and connected
    cc = max(nx.connected_components(cand), key=len)
    sub = cand.subgraph(cc).copy()
    return nx.convert_node_labels_to_integers(sub)


def run_case(base, case_name, fn, results, all_ok, out):
    out.append(f"  --- CASE {case_name} on {base_name(base)} ---")
    G, H, res, info = fn(base)
    case_ok = True
    for k, v in res.items():
        out.append(f"      [{'PASS' if v else 'FAIL'}] {k}")
        case_ok = case_ok and v
    out.append(f"      info: {info}")
    results[f"{case_name} / {base_name(base)}"] = case_ok
    all_ok = all_ok and case_ok
    return all_ok


def base_name(base):
    return base.graph.get("name", "?")


def main():
    out = []
    bases = [
        nx.complete_graph(4),
        prism(),
        nx.petersen_graph(),
        random_cubic(),
    ]
    for i, b in enumerate(bases):
        b.graph["name"] = ["K4", "triangular prism", "Petersen",
                           "random cubic n=8"][i]

    results = {}
    all_ok = True

    out.append("SURGERY IDENTITIES -- cut-vertex exclusion theorem\n")
    out.append("Bases: " + ", ".join(base_name(b) for b in bases) + "\n")

    for b in bases:
        out.append(f"=== Base: {base_name(b)} "
                   f"(n={b.number_of_nodes()}, m={b.number_of_edges()}) ===")
        all_ok = run_case(b, "A", case_a, results, all_ok, out)
        all_ok = run_case(b, "B", case_b, results, all_ok, out)
        all_ok = run_case(b, "C", case_c, results, all_ok, out)
        out.append("")

    out.append("=" * 70)
    for k, v in results.items():
        out.append(f"  {k:45s} -> {'PASS' if v else 'FAIL'}")
    out.append("=" * 70)
    out.append("OVERALL: " + ("ALL CASES PASS" if all_ok else "SOME CASE FAILED"))

    text = "\n".join(out)
    print(text)
    with open("code/out/cutvertex/surgery_verify.log", "w") as f:
        f.write(text + "\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
