"""The oracle edge: exhaustive check that no small graph with min degree >=3
lacks a power-of-two cycle.

Uses nauty-geng to enumerate every connected min-degree-3 graph on n vertices
(up to isomorphism) and the exact cycle-length oracle to test the
Erdős–Gyárfás predicate. This is the brute-force verification bound; it is not
a proof, but it tells us exactly where exhaustive generation stops being the
method. Run at small n because cycle enumeration is exponential.
"""

from lib.cycles import (
    _geng_graph6,
    report_delta3_no_power2,
)


def main():
    print("Counts of connected min-degree>=3 graphs by order (nauty-geng):")
    counts = {}
    for n in range(4, 9):
        lines = _geng_graph6(n)
        counts[n] = len(lines)
        print(f"  n={n}: {len(lines)} graphs")
    print()

    print("Searching for a min-degree>=3 graph with NO power-of-two cycle:")
    for n, max_lines in [(4, None), (5, None), (6, None), (7, None), (8, None)]:
        seen, exs = report_delta3_no_power2(n)
        print(f"  n={n}: checked {seen} min-deg-3 graphs, "
              f"{'FOUND ' + str(len(exs)) + ' counterexamples' if exs else 'none found'}")
        if exs:
            print(f"    counterexamples: {exs[:5]}")

    print()
    print("done")


if __name__ == "__main__":
    main()
