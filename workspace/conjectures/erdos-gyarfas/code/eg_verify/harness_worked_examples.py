"""Harness reproducing the oracle's worked examples (Task 1).

Imports the exact cycle oracle from lib.cycle_oracle and prints min degree,
cycle-length set, and girth for the five reference graphs: K4, K3,3, the cube
Q3, Petersen, and the Markström graph loaded from its canonical graph6 string
(research/sources/markstrom-graph-graph6.md).  Asserts each equals the known
value:

    K4            -> min_deg 3, cycles {3, 4}
    K3,3          -> min_deg 3, cycles {4, 6}
    cube Q3       -> min_deg 3, cycles {4, 6, 8}
    Petersen      -> min_deg 3, cycles {5, 6, 8, 9}
    Markström     -> min_deg 3, cycles {3,5,6,7,9,10,...,24}
                     (no C4, no C8, yes C16)

Girth = shortest cycle length, computed from the same exact cycle-length set.
The Markström graph is a genuine test case for the oracle because it is not one
of the hand-checkable builtins: its expected profile comes from the literature
(MathWorld / House of Graphs), and C4 and C8 are absent while C16 is present.

Run:  python code/eg_verify/harness_worked_examples.py
"""
import networkx as nx

from lib.cycle_oracle import oracle

# Careful: girth is the *shortest* cycle length; for a connected min-deg-3
# graph the graph always contains cycles.  We read it off the exact cycle set.
def girth(G):
    lens = set(oracle(G)[1])
    return min(lens)


MARKSTROM_GRAPH6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"


def markstrom_from_graph6(s):
    return nx.from_graph6_bytes(s.encode())


def _expectations():
    return [
        ("K4", nx.complete_graph(4), frozenset({3, 4}), 3, 3),
        ("K3,3", nx.complete_bipartite_graph(3, 3), frozenset({4, 6}), 3, 4),
        ("cube Q3", nx.hypercube_graph(3), frozenset({4, 6, 8}), 3, 4),
        ("Petersen", nx.petersen_graph(), frozenset({5, 6, 8, 9}), 3, 5),
        ("Markström", markstrom_from_graph6(MARKSTROM_GRAPH6),
         frozenset({3, 5, 6, 7}) | frozenset(range(9, 25)), 3, 3),
    ]


def main():
    print("Task 1 — reproduce the oracle's worked examples (lib.cycle_oracle)\n")
    all_ok = True
    for name, G, exp_lens, exp_mindeg, exp_girth in _expectations():
        mindeg, lens = oracle(G)
        got_lens = frozenset(lens)
        got_girth = min(lens)
        ok_len = got_lens == exp_lens
        ok_deg = mindeg == exp_mindeg
        ok_gir = got_girth == exp_girth
        ok = ok_len and ok_deg and ok_gir
        all_ok &= ok
        status = "MATCH" if ok else "MISMATCH"
        absent4 = 4 not in got_lens
        absent8 = 8 not in got_lens
        present16 = 16 in got_lens
        extra = ""
        if name == "Markström":
            extra = (f"  [C4 absent={absent4}, C8 absent={absent8}, "
                     f"C16 present={present16}]")
        print(f"  {name:10s} min_deg={mindeg} cycles={sorted(got_lens)}"
              f" girth={got_girth}  -> {status}{extra}")
        if not ok:
            print(f"      expected: min_deg={exp_mindeg} cycles={sorted(exp_lens)}"
                  f" girth={exp_girth}")
    print()
    print("ALL MATCH" if all_ok else "MISMATCHES PRESENT")


if __name__ == "__main__":
    main()
