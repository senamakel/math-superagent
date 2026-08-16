"""Find the 'worst case' for the chord-deletion induction
(research/approaches/edge-deletion-2adic-transfer.md) on the committed
2-connected delta>=3 class, n <= 8.

A deletable chord of a 2-connected delta>=3 graph G is an edge e = ab such that
H := G - e is 2-connected and delta(H) >= 2 (Lemma A guarantees one exists).

A chord e = ab is GOOD (the induction step closes) iff
    C(H) contains a power of two (4, 8, 16, ...)          [H already has a 2^k cycle]
  OR
    H has a simple a-b path of length 2^k - 1 (3, 7, 15, ...)
                                                 [that path + e is a 2^k cycle of G]

WORST CASE = a graph in the class with NO good deletable chord. For such a graph
the single chord-deletion step cannot establish a power-of-two cycle, so it names
what the next lemma must handle.

STRUCTURAL FACT this script relies on (and cross-checks, see below): if G has a
power-of-two cycle of length 2^k, then EVERY deletable chord of G is good --
a 2^k-cycle either avoids e (so it lies in H and C(H) contains 2^k) or passes
through e (so cycle minus e is an a-b path in H of length 2^k-1). Hence a bad
graph is exactly a graph with NO power-of-two cycle. By the Moore bound, any
delta>=3 graph on <=8 vertices has girth <= 4, hence a 4-cycle, so no bad graph
is expected up to n=8. The scan checks this on the full per-chord definition and
flags any disagreement with the direct no-power-of-two-cycle check.

Runs on the committed generator path (lib.biconnected_gen_hash), NOT ad-hoc
regeneration. Expected wall time ~40s (generation ~27s + checks ~12s).
"""
import networkx as nx
from lib.biconnected_gen_hash import generate_2connected_levels_hash
from lib.erdos_gyarfas import all_cycles


def min_degree(G):
    return min(dict(G.degree()).values()) if G.number_of_nodes() > 0 else 0


def adj_of(G):
    return {v: set(G.neighbors(v)) for v in G.nodes()}


def power_of_two_lens(adj):
    """Set of power-of-two cycle lengths among cycles of the graph (4,8,16,...)."""
    return {len(c) for c in all_cycles(adj) if len(c) >= 4 and (len(c) & (len(c) - 1)) == 0}


def has_ab_path_of_len(adj, a, b, target_lens):
    """True iff there is a simple a-b path whose length is in target_lens."""
    seen = {a}
    pl = 0

    def dfs(cur):
        nonlocal pl
        for nbr in adj[cur]:
            if nbr == b and pl + 1 in target_lens:
                return True
            if nbr not in seen:
                seen.add(nbr)
                pl += 1
                if dfs(nbr):
                    return True
                pl -= 1
                seen.remove(nbr)
        return False

    return dfs(a)


def good_chord(G):
    """Return (a, b, reason) for the first good deletable chord, or None."""
    pw_cycle = {4}
    n = G.number_of_nodes()
    # powers of two (4,8,16,...) != n, and 2^k - 1 (3,7,15,...) in H (<= n-1 edges)
    target_cycles = {k for k in (4, 8, 16, 32) if k <= n}
    target_paths = {k - 1 for k in target_cycles}  # lengths 3,7,15,...
    for a, b in G.edges():
        H = G.copy()
        H.remove_edge(a, b)
        if not (nx.is_biconnected(H) and min_degree(H) >= 2):
            continue  # not a deletable chord in the Lemma-A sense
        Ha = adj_of(H)
        if power_of_two_lens(Ha) & target_cycles:
            return (a, b, "C(H) has a power-of-two cycle")
        if has_ab_path_of_len(Ha, a, b, target_paths):
            return (a, b, f"a-b path of length 2^k-1 in H")
    return None


def main(N=8):
    levels = generate_2connected_levels_hash(N)
    bad_graphs = []  # (n, edges, direct_no_pow2)
    n_graphs = 0
    direct_mismatch = 0
    counts = {}
    for n in range(3, N + 1):
        cnt = 0
        for G in levels.get(n, []):
            if min_degree(G) < 3:
                continue
            cnt += 1
            n_graphs += 1
            Ga = adj_of(G)
            # direct check: does G itself have a power-of-two cycle?
            direct_no_pow2 = not bool(power_of_two_lens(Ga) & {k for k in (4, 8, 16, 32) if k <= n})
            gc = good_chord(G)
            if gc is None:
                bad_graphs.append((n, sorted(G.edges()), direct_no_pow2))
                # if direct says G HAS a power-of-two cycle but no good chord, my
                # structural fact is wrong -- that needs reporting.
                if not direct_no_pow2:
                    direct_mismatch += 1
                    print(f"  !! MISMATCH n={n}: G has 2^p cycle but no good chord",
                          sorted(G.edges()))
            else:
                if direct_no_pow2:
                    # G has no power-of-two cycle yet a good chord exists: also a
                    # contradiction of the structural fact (should be impossible).
                    direct_mismatch += 1
                    print(f"  !! MISMATCH n={n}: G has no 2^p cycle but good chord {gc}",
                          sorted(G.edges()))
        counts[n] = cnt

    out_lines = []
    out_lines.append("edge_transfer_worstcase: 2-connected delta>=3 class, n <= 8 (committed generator)")
    for n in range(3, N + 1):
        out_lines.append(f"  n={n}: {counts[n]} graphs")
    out_lines.append(f"TOTAL graphs scanned: {n_graphs}")
    out_lines.append(f"Graphs with NO good deletable chord (worst cases): {len(bad_graphs)}")
    if bad_graphs:
        smallest = min(n for n, _, _ in bad_graphs)
        out_lines.append(f"SMALLEST n with a worst-case graph: n={smallest}")
        for n, edges, dp2 in bad_graphs:
            tag = "G has a power-of-two cycle" if not dp2 else "G has NO power-of-two cycle"
            out_lines.append(f"  n={n} edges={edges}  [{tag}]")
    else:
        out_lines.append("=> No worst case in the verified range: every graph has a good")
        out_lines.append("   deletable chord, so the chord-deletion step closes on ALL of")
        out_lines.append("   n<=8. (Consistent with Moore bound: every delta>=3 graph on")
        out_lines.append("   <=8 vertices has girth <=4, hence a 4-cycle.)")
    out_lines.append(f"Structural-fact mismatches (per-chord vs direct): {direct_mismatch}")
    print("\n".join(out_lines))
    return bad_graphs, direct_mismatch, counts, out_lines


if __name__ == "__main__":
    main()
