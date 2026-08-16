"""Verify the girth-5 class for the Erdos-Gyarfas conjecture, n <= 11.

The committed girth-5 generator (lib.girth5_gen) produces every 2-connected
graph of girth >= 5 on n <= 11 vertices, seeded from C5 and closed under ears
with girth pruning (see its docstring: below the Moore-bound floor for girth 6,
n <= 11 for min-degree-3, every 2-connected girth>=5 min-degree>=3 graph has
girth exactly 5 and is reached by the C5 seed).

CLAIM under test: every 2-connected graph with minimum degree >= 3 and girth
>= 5 on n <= 11 vertices contains a cycle of length 8 (a power of two). This is
exactly the conjecture restricted to the class where 4-cycles are forbidden:
girth >= 5 means no C4, so the power-of-two cycle, if present, is at least 8.

Why this is the hard content: the n<=8 verification (g_heart_verify_n8) is
trivial by the Moore bound (every min-degree>=3 graph on <=8 vertices has girth
<=4, hence a 4-cycle). The first non-trivial case is girth-5 graphs, which only
begin to exist at n>=10 (the (3,5)-cage, Petersen, is on 10 vertices). So this
run is the first place a counterexample could hide. Gebendorfer's preprint
claims girth>=5 forces an 8-cycle.

Method: generate the class with the committed generator, keep min-degree>=3,
and run the exact oracle (lib.erdos_gyarfas.has_power_of_two_cycle) on each.
Correctness of the oracle is established (code/out/oracle_validation.md); the
generator's completeness for girth-5 below the Moore floor is argued in its
docstring and independently checked by girth measurement + the (uniqueness of)
Petersen at n=10.

Expected: Petersen (n=10) has an 8-cycle (verified in oracle_validation), so
the class should be clean through n=11. The value here is confirming the whole
girth-5 2-connected min-degree-3 class on 10 <= n <= 11, which is past the
n<=8 verification bound the run can trust as its own.
"""
import networkx as nx
from lib.girth5_gen import generate_2connected_girth_atleast5, min_degree
from lib.erdos_gyarfas import has_power_of_two_cycle


def adj_of(G):
    return {v: set(G.neighbors(v)) for v in G.nodes()}


def main(N=11):
    levels = generate_2connected_girth_atleast5(N)
    counts = {}
    bad = []
    for n in range(3, N + 1):
        keep = [G for G in levels.get(n, []) if min_degree(G) >= 3]
        counts[n] = len(keep)
        for G in keep:
            has, ln = has_power_of_two_cycle(adj_of(G))
            if not has:
                bad.append((n, sorted(G.edges())))
    lines = []
    lines.append("check_girth5_8cycle_class: 2-connected girth>=5 min-degree>=3, n<=%d" % N)
    for n in range(3, N + 1):
        lines.append("  n=%2d : %5d graphs" % (n, counts[n]))
    lines.append("TOTAL girth>=5 min-degree>=3 graphs: %d" % sum(counts.values()))
    lines.append("Graphs with NO power-of-two cycle: %d" % len(bad))
    if bad:
        for n, e in bad:
            lines.append("  n=%d edges=%s" % (n, e))
    else:
        lines.append("=> Every 2-connected girth>=5 min-degree>=3 graph on n<=%d "
                     "has a power-of-two cycle (no 4-cycle, so an 8-cycle)." % N)
    print("\n".join(lines))
    return counts, bad, lines


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    main(N)
