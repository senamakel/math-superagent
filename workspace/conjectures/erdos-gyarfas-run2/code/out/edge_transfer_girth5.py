"""Chord-deletion good-chord search on the girth-5 danger region (n=10, 11).

Background: the earlier scan (edge_transfer_worstcase.py) found no worst case
for n<=8 because every delta>=3 graph there has girth<=4 and hence a 4-cycle,
making every chord good. The genuine danger is girth>=5, which needs n>=10
(Petersen, the (3,5)-cage, is the smallest 3-regular girth-5 graph).

A deletable chord e=ab of H := G-e (deletable = H 2-connected and delta(H)>=2)
is GOOD iff
    C(H) contains a power of two (4,8,16,...)        [H already has a 2^k-cycle]
  OR
    H has a simple a-b path of length 2^k - 1 (3,7,15,...)
                                       [that path + e is a 2^k-cycle of G].
Worst case = a graph with NO good deletable chord.

STRUCTURAL FACT used and cross-checked: if G itself has a power-of-two cycle of
length 2^k, then EVERY deletable chord is good (a 2^k-cycle either avoids e, so
it lies in H, or passes through e, so cycle - e is an a-b path of length 2^k-1
in H); conversely a good chord certifies a power-of-two cycle in G. Hence a bad
graph is exactly a graph with NO power-of-two cycle. For girth>=5 on n<=11 the
only possible power-of-two cycle length is 8 (C4 forbidden by girth, C16 needs
16+ vertices), so the whole scan reduces to: does every 2-connected delta>=3
girth-5 graph on n=10,11 have an 8-cycle? This reproduces the n<=12 rung.

The script still runs the full per-chord good definition (for Petersen, giving
the requested report of cycle lengths), and for the enumeration tests each graph
for a power-of-two cycle, running the full per-chord report on any bad graph.

Generation: lib.girth5_gen (C5-seeded open-ear decomposition, girth-pruned,
WL-hash + VF2 dedup). This is complete for min-degree>=3 girth-5 graphs below
the Moore-bound floor (n<=11): such a graph has a 5-cycle and an open ear
decomposition from it, and adding ears only adds edges so no girth-5 graph is
ever pruned.
"""
import time
import networkx as nx
from lib.girth5_gen import generate_2connected_girth_atleast5, min_degree, girth
from lib.erdos_gyarfas import all_cycles, powers_of_two_up_to, cycles_by_length


def to_adj(G):
    return {v: set(G.neighbors(v)) for v in G.nodes()}


def has_ab_path_of_len(adj, a, b, target_lens):
    """True iff a simple a-b path of length in target_lens exists."""
    seen = {a}

    def dfs(cur, pl):
        for nbr in adj[cur]:
            if nbr == b:
                if pl + 1 in target_lens:
                    return True
            elif nbr not in seen:
                seen.add(nbr)
                if dfs(nbr, pl + 1):
                    return True
                seen.remove(nbr)
        return False

    return dfs(a, 0)


def power_of_two_lens(adj, n):
    """Power-of-two cycle lengths present among cycles of the graph."""
    targets = powers_of_two_up_to(n)
    return {len(c) for c in all_cycles(adj) if len(c) in targets}


def chord_report_full(G, n):
    """Full per-chord good-chord scan. Returns (all_good, details).
    details: for each deletable chord a list of (a,b,result-string), plus the
    graph's cycle-length set and the bad chord's a-b path-length set."""
    targets_cycles = {k for k in powers_of_two_up_to(n) if 4 <= k <= n}
    targets_paths = {k - 1 for k in targets_cycles}  # 3,7,15,...
    details = []
    all_good = True
    bad_chord = None
    for a, b in G.edges():
        H = G.copy()
        H.remove_edge(a, b)
        if not (nx.is_biconnected(H) and min_degree(H) >= 2):
            continue  # not a deletable chord
        Ha = to_adj(H)
        cl = power_of_two_lens(Ha, n)
        if cl & targets_cycles:
            details.append((a, b, "C(H) has 2-power"))
            continue
        if has_ab_path_of_len(Ha, a, b, targets_paths):
            details.append((a, b, "a-b path 2^k-1"))
            continue
        all_good = False
        bad_chord = (a, b)
        # record G-e cycle lengths and the bad chord's a-b path lengths
        path_lens = sorted({l for l in ab_path_lengths(Ha, a, b)})
        details.append((a, b, "NOT GOOD"))
    return all_good, details, bad_chord


def ab_path_lengths(adj, a, b):
    """Set of lengths of all simple a-b paths."""
    out = set()
    seen = {a}

    def dfs(cur, pl):
        for nbr in adj[cur]:
            if nbr == b:
                out.add(pl + 1)
            elif nbr not in seen:
                seen.add(nbr)
                dfs(nbr, pl + 1)
                seen.remove(nbr)

    dfs(a, 0)
    return out


def report_petersen():
    """Direct test of the Petersen graph, edge by edge."""
    G = nx.petersen_graph()
    n = G.number_of_nodes()
    out = []
    out.append("=== PETERSEN GRAPH (n=10, cubic, girth 5, the (3,5)-cage) ===")
    out.append(f"girth={girth(G)}, min_deg={min_degree(G)}, n={n}")
    cl = power_of_two_lens(to_adj(G), n)
    out.append(f"Petersen's own power-of-two cycle lengths present: {sorted(cl)}")
    all_good, details, bad = chord_report_full(G, n)
    deletable = [d for d in details]
    out.append(f"deletable chords tested: {len(deletable)} (2-connected & delta>=2 after deletion)")
    ngood = sum(1 for d in details if d[2] != "NOT GOOD")
    out.append(f"of which GOOD: {ngood}, NOT GOOD: {len(details)-ngood}")
    out.append(f"EVERY deletable chord of Petersen is good: {all_good}")
    if not all_good:
        out.append(f"!! BAD chord: {bad}")
        H = G.copy(); H.remove_edge(*bad)
        out.append(f"   G-e cycle lengths: {sorted(cycles_by_length(to_adj(H)).keys())}")
        out.append(f"   G-e has power-of-two: {sorted(power_of_two_lens(to_adj(H), n))}")
        out.append(f"   bad chord a-b path lengths: {sorted(ab_path_lengths(to_adj(H), *bad))}")
    return "\n".join(out)


def main(N=11):
    out = []
    out.append(report_petersen())
    out.append("")
    out.append("=== ENUMERATION: 2-connected min-degree>=3 girth-5 graphs, n=10,11 ===")
    t0 = time.time()
    levels = generate_2connected_girth_atleast5(N)
    out.append(f"generation time: {time.time()-t0:.1f}s")
    counts = {}
    worst = []  # (n, edges, cycle_lens, details)
    for n in (10, 11):
        graphs = [G for G in levels.get(n, []) if min_degree(G) >= 3]
        counts[n] = len(graphs)
        out.append(f"n={n}: {len(graphs)} 2-connected min-degree>=3 girth-5 graphs")
        for G in graphs:
            Ga = to_adj(G)
            cl = power_of_two_lens(Ga, n)
            if not cl:
                # no power-of-two cycle -> a bad graph (worst case of the induction)
                # run the full per-chord report for the record
                _, details, bad = chord_report_full(G, n)
                worst.append((n, sorted(G.edges()), sorted(cycles_by_length(Ga).keys()), details, bad))
    out.append("")
    if not worst:
        out.append("=> NO WORST CASE: every 2-connected min-degree>=3 girth-5 graph on n=10,11")
        out.append("   has a power-of-two cycle (an 8-cycle), so every deletable chord is good.")
        out.append("   The chord-deletion induction closes on the entire girth-5 danger region")
        out.append("   below the Moore-bound floor.")
    else:
        smallest = min(n for n, *_ in worst)
        out.append(f"=> WORST CASE EXISTS: smallest n={smallest}")
        for n, edges, clen, details, bad in worst:
            out.append(f"  n={n} edges={edges}")
            out.append(f"    cycle lengths of G: {clen}")
            out.append(f"    a bad (not-good) deletable chord: {bad}")
            if bad:
                H = nx.Graph(); H.add_edges_from(edges); H.remove_edge(*bad)
                out.append(f"    G-e cycle lengths: {sorted(cycles_by_length(to_adj(H)).keys())}")
                out.append(f"    bad chord's a-b path lengths: {sorted(ab_path_lengths(to_adj(H), *bad))}")
    out.append(f"TOTAL WALL TIME: {time.time()-t0:.1f}s")
    return "\n".join(out), worst, counts


if __name__ == "__main__":
    text, worst, counts = main()
    print(text)
