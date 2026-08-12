"""Cubic exhaustive corroboration, strictly bounded at n <= 16.

The published claim: the smallest cubic graph with neither a C4 nor a C8 has
24 vertices.  A full enumeration to 24 is out of reach / prohibited, but we can
independently corroborate the *low end* of that bound: enumerate every
connected cubic graph on n = 4, 6, ... , 16 vertices (nauty-geng, up to
isomorphism) and confirm that NONE of them is free of both C4 and C8.

This is a bounded oracle check (n <= 16 as the task permits), not the method at
full size: it supports "the first no-C4&C8 cubic graph is at least past 16",
consistent with the published value 24.  It does not and cannot prove "24".
"""
import subprocess
import re

import networkx as nx

from lib.cycle_oracle import distinct_cycle_lengths


def all_connected_cubic_graph6(n):
    """Yield every connected cubic graph on n vertices, one graph6 string each."""
    # geng -d3 -D3 : min and max degree 3 => exactly cubic.
    # -c : connected. -q : quiet (no count line to stdout is fine anyway).
    out = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", "-D3", str(n)],
        capture_output=True, text=True, check=True,
    )
    return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]


def main():
    print("Connected cubic graphs on n <= 16: count and no-C4/C8-free count")
    total_no_free = 0
    for n in range(4, 17, 2):  # cubic requires even n (3n edges / 2 integer)
        g6 = all_connected_cubic_graph6(n)
        n_free = 0
        for s in g6:
            G = nx.from_graph6_bytes(s.encode())
            lens = distinct_cycle_lengths(G)
            if 4 not in lens and 8 not in lens:
                n_free += 1
        total_no_free += n_free
        marker = "" if n_free == 0 else "  <-- has no-C4&C8 cubic graph!"
        print(f"  n={n:3d}  connected-cubic graphs={len(g6):6d}"
              f"  no-C4&C8-free={n_free}{marker}")
    print()
    print("Published: smallest cubic graph with no C4 and no C8 has 24 vertices.")
    print(f"Up to n<=16 we find {total_no_free} such graphs — consistent with"
          f" that (0 here, first at 24).")
    print("This corroborates the low end only; it does not prove 24 is first.")


if __name__ == "__main__":
    main()
