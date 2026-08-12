"""Naive oracle demo and worked-example harness for Erdos-Gyarfas.

This file uses to be a third, independent copy of the DFS cycle-length oracle
(alongside lib/oracle.py and lib/cycles.py) plus the hand-built worked examples.
Under consolidation the compute-cores now import from the single shelved
definition `lib.cycles` (via the adjacency-list convenience layer lib/oracle),
so every answer on this run comes from one code path. This file keeps its
other job: building the hand-worked graphs (K4, K3,3, Petersen, cube Q3) and
printing the oracle's answer for each, the verification demo of the run.

The graphs are built by hand so the answers can be stated independently of any
library; the values match what lib/cycles.py returns (see also
code/verify_cycles.py and code/eg/hand_dfs_check.py).

Exact integer arithmetic; no floating point anywhere. The cycle-length
enumeration (inside lib/cycles) is exponential in the worst case, so this is
only for the small worked examples, not the verification bound.
"""

from __future__ import annotations

from lib.oracle import (
    minimum_degree,
    cycle_lengths,
    powers_of_two_cycle_lengths,
    from_graph6,
)


def has_power_of_two_cycle(cycle_lengths_set, min_k=2):
    """Whether any cycle length is a power of two (2^k, k >= min_k)."""
    return bool(powers_of_two_cycle_lengths(cycle_lengths_set, min_k))


def report(adj, name):
    """Print the oracle's answer for one graph and return (deg, lengths)."""
    deg = minimum_degree(adj)
    lens = cycle_lengths(adj)
    powlens = powers_of_two_cycle_lengths(lens)
    print(f"{name}: min degree = {deg}, cycle lengths = {sorted(lens)}, "
          f"power-of-two cycle lengths = {sorted(powlens)}")
    return deg, lens, powlens


# ---------------------------------------------------------------------------
# The worked examples, built by hand so the answers can be stated independently
# of any library.
# ---------------------------------------------------------------------------
def run_here():
    import networkx as nx

    # K4: complete graph on {0,1,2,3}.
    K4 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    report(K4, "K4")

    # K3,3: complete bipartite parts {0,1,2} and {3,4,5}.
    K33 = [[3, 4, 5], [3, 4, 5], [3, 4, 5], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    report(K33, "K3,3")

    # Petersen graph: outer 5-cycle 0-1-2-3-4-0, inner 5-cycle 5-6-7-8-9-5,
    # spokes i-(i+5).
    P = [[] for _ in range(10)]
    for i in range(5):
        P[i].append((i + 1) % 5)
        P[(i + 1) % 5].append(i)
    for i in range(5):
        j = 5 + ((i + 2) % 5)   # pentagram step: inner 5,7,9,6,8
        P[5 + i].append(j)
        P[j].append(5 + i)
    for i in range(5):
        P[i].append(i + 5)
        P[i + 5].append(i)
    report(P, "Petersen")

    # Cube Q3: binary strings of length 3, adjacent if Hamming distance 1.
    Q = [[] for _ in range(8)]
    for a in range(8):
        for b in range(a + 1, 8):
            if (a ^ b).bit_count() == 1:
                Q[a].append(b)
                Q[b].append(a)
    report(Q, "cube Q3")

    # Also exercise the graph6 path: K4 in graph6 is "C~" (from nauty). Check
    # it agrees with the hand-built K4 above.
    print("graph6 K4:", report(from_graph6("C~"), "K4[g6]"))


if __name__ == "__main__":
    run_here()
