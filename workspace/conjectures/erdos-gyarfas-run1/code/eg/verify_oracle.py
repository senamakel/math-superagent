"""Verify the shelved oracle lib.cycles on the worked examples, then re-run the
survivor computation for the EG verification bound.

Part 1 — worked examples, all through `from lib.cycles import ...` (the single
compute core of the run; nothing is re-implemented here):
  K4, K3,3, Petersen, cube Q3  ->  min_degree, girth, exact cycle-length set,
  has_power_of_two_cycle, each compared against hand-known values (printed as
  MATCH / MISMATCH). Hand-known answers, stateable without a computer:
    K4:       deg 3, girth 3, lengths {3,4},        pow2 True  (4)
    K3,3:     deg 3, girth 4, lengths {4,6},        pow2 True  (4)
    Petersen: deg 3, girth 5, lengths {5,6,8,9},    pow2 True  (8)
    cube Q3:  deg 3, girth 4, lengths {4,6,8},      pow2 True  (4,8)

Part 2 — survivor computation for n=10..16, the exact class a counterexample
would have to live in: connected, min degree >= 3, C4-free (a C4 is itself a
power-of-two cycle, so `nauty-geng -q -c -f -d3 n` loses no counterexample —
same '-f' route lib.egcheck.mindeg3_no_power2_from_geng uses). For every
survivor the exact bounded-DFS predicate lib.egcheck.has_cycle_of_length(G, 8)
decides whether an exact 8-cycle is present (polynomial: depth fixed at 8,
never exponential in n). A graph in this class with NO 8-cycle would be an EG
counterexample outright (it already lacks 4 and 8), so
missing_exact_8cycle == 0 at every n proves computationally:
    no counterexample on n<=16.

Expected counts (prior run, code/eg/survivor_sequences.md and
check_no8_n16.py): 5, 9, 57, 503, 6059, 91433, 1655659 survivors, zero missing
an 8-cycle. The 16-term is the slow one (~145 s).

Save stdout with:  cd code && python eg/verify_oracle.py | tee eg/verify_oracle.out.txt
"""

import subprocess

import networkx as nx

from lib.cycles import min_degree, girth, cycle_lengths, has_power_of_two_cycle
from lib.egcheck import has_cycle_of_length

# (name, graph, expected min_degree, expected girth, expected cycle lengths,
#  expected has_power_of_two_cycle)  -- values stateable by hand, no computer.
WORKED = [
    ("K4",       nx.complete_graph(4),        3, 3, {3, 4},    True),
    ("K3,3",     nx.complete_bipartite_graph(3, 3), 3, 4, {4, 6}, True),
    ("Petersen", nx.petersen_graph(),         3, 5, {5, 6, 8, 9}, True),
    ("cube Q3",  nx.hypercube_graph(3),       3, 4, {4, 6, 8}, True),
]


def worked_examples():
    print("=== worked examples through lib.cycles ===")
    all_ok = True
    for name, G, edeg, egir, elens, epow in WORKED:
        deg = min_degree(G)
        gir = girth(G)
        lens = cycle_lengths(G)
        pow2 = has_power_of_two_cycle(G)
        ok = (deg == edeg and gir == egir and lens == elens and pow2 == epow)
        all_ok &= ok
        print(f"{name:9s} min_degree={deg} girth={gir} "
              f"cycle_lengths={sorted(lens)} has_power_of_two_cycle={pow2} "
              f"{'MATCH' if ok else 'MISMATCH'}")
    print(f"worked examples: {'ALL MATCH' if all_ok else 'FAILED'}")
    return all_ok


def survivor_computation():
    print()
    print("=== survivor computation: connected min-degree>=3, C4-free, n=10..16 ===")
    grand_survivors = 0
    grand_missing8 = 0
    for n in range(10, 17):
        # Same native C4-free generation route as
        # lib.egcheck.mindeg3_no_power2_from_geng(n, lines_from='-f').
        proc = subprocess.run(
            ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)],
            capture_output=True, text=True, check=True,
        )
        survivors = 0
        missing8 = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            survivors += 1
            if not has_cycle_of_length(G, 8):
                missing8 += 1
        grand_survivors += survivors
        grand_missing8 += missing8
        print(f"n={n}: C4free_min_deg3_survivors={survivors} "
              f"missing_exact_8cycle={missing8}")
    print(f"total: survivors={grand_survivors} missing_exact_8cycle={grand_missing8}")
    return grand_missing8


def main():
    ok = worked_examples()
    missing8 = survivor_computation()
    print()
    if ok and missing8 == 0:
        print("conclusion: no counterexample on n<=16  "
              "(every C4-free min-degree>=3 graph on n=10..16 contains an "
              "exact 8-cycle, so none avoids all power-of-two lengths)")
    else:
        print("conclusion: CHECK FAILED — see per-n lines above")


if __name__ == "__main__":
    main()