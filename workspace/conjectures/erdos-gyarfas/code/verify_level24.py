"""Independent verification of the level-24 census claim.

Census (code/out/expansion_census/level_24_results.txt) states:
    n=24  classes=58713  avoidsC4=807  avoidsC4C8=1

This script re-reads level_24_classes.txt (58713 canonical graph6 strings),
and for each class independently checks, using lib.cycle_oracle's
has_cycle_of_length (exact DFS with early termination):
  - min degree = 3 and cubic (the family is cubic)
  - contains a C4?  contains a C8?
  - full cycle-length set for the single C4,C8-free graph, to confirm it is
    the Markström graph (HoG 51419) with the known signature {3,5,6,7,9..24},
    and that C16 is present (so it is not an EG counterexample).

Society: the claim being verified is a counting claim over an exhaustive
catalogue; this is the second route (the census itself is the first).
"""
import sys
import time
import networkx as nx

sys.path.insert(0, "/workspace/code")  # noqa: import cycle_oracle as in run
from lib.cycle_oracle import has_cycle_of_length, minimum_degree, \
    distinct_cycle_lengths

CLASSES = "/workspace/code/out/expansion_census/level_24_classes.txt"
MARKSTROM_G6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"


def load_classes(path):
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def main():
    cl = load_classes(CLASSES)
    n = len(cl)
    print(f"loaded {n} classes from {CLASSES}")
    assert n == 58713, f"expected 58713 classes, got {n}"

    n_cubic = n_notcubic = 0
    n_no4 = 0
    n_no48 = 0
    no48_graphs = []
    t0 = time.time()
    for i, g6 in enumerate(cl):
        G = nx.from_graph6_bytes(g6.encode())
        degs = set(dict(G.degree()).values())
        if degs == {3}:
            n_cubic += 1
        else:
            n_notcubic += 1
        if not has_cycle_of_length(G, 4):
            n_no4 += 1
            if not has_cycle_of_length(G, 8):
                n_no48 += 1
                no48_graphs.append(g6)
        if (i + 1) % 10000 == 0:
            dt = time.time() - t0
            print(f"  ... {i+1}/{n} in {dt:.1f}s "
                  f"(no4={n_no4} so far, no48={n_no48} so far)")
    dt = time.time() - t0
    print(f"\nscan of {n} classes done in {dt:.1f}s")
    print(f"cubic: {n_cubic}, non-cubic: {n_notcubic}")
    print(f"avoids C4: {n_no4}")
    print(f"avoids C4 and C8: {n_no48}")

    for g6 in no48_graphs:
        G = nx.from_graph6_bytes(g6.encode())
        lens = sorted(distinct_cycle_lengths(G))
        print(f"\n  C4,C8-free graph: {g6}")
        print(f"  min degree {minimum_degree(G)}, cycle lengths {lens}")
        print(f"  is Markström graph6: {g6 == MARKSTROM_G6}")
        print(f"  has C16: {16 in lens}")


if __name__ == "__main__":
    main()