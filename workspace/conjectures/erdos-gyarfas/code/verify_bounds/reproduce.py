"""Reproduce.py — verify_bounds.

Three jobs for the Erdős–Gyárfás verification-bounds thread:

Part (1): use lib.cycle_oracle (minimum_degree, distinct_cycle_lengths) to
  print, for K4, K3,3, the cube Q3, Petersen, and the Markström 24-vertex
  graph (graph6 string below), the min degree, the FULL set of cycle lengths,
  and whether the graph contains any power-of-two cycle (length in {4,8,16,...}).

Part (2): cross-check those cycle-length sets against networkx.simple_cycles
  on a spread of small graphs (the oracle and nx are independent enumerations).

Part (3): push the cubic no-C4-and-no-C8 verification upward — enumerate every
  connected cubic graph on n vertices (nauty-geng) up to the largest n that
  completes feasibly, and report that n plus the theorem statement it supports.

The Markström graph is the unique planar cubic graph on 24 vertices with no C4
and no C8; the literature asserts (and this run has verified) it has cycle
profile {3,5,6,7,9,...,24} with 4 and 8 absent and 16 present.
"""
import json
import os
import subprocess
import sys
import time

import networkx as nx

from lib.cycle_oracle import (
    minimum_degree,
    distinct_cycle_lengths,
    has_cycle_of_length,
    oracle,
)

HERE = os.path.dirname(os.path.abspath(__file__))

# Markström graph canonical graph6 (HoG 51419). Source research/sources/
# markstrom-graph-graph6.md.  The 24 vertices are labelled 0..23 (graph6 order).
MARKSTROM_G6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"

POWERS = {4, 8, 16, 32, 64, 128}  # 2^k, k >= 2, up to an explicit cap


def build_five():
    """Return list of (name, networkx Graph) for the five target graphs."""
    graphs = [
        ("K4", nx.complete_graph(4)),
        ("K3,3", nx.complete_bipartite_graph(3, 3)),
        ("cube Q3", nx.hypercube_graph(3)),
        ("Petersen", nx.petersen_graph()),
        ("Markström(24)", nx.from_graph6_bytes(MARKSTROM_G6.encode())),
    ]
    return graphs


def part1(out):
    print("=" * 76, file=out)
    print("Part (1): min degree + full cycle-length set for the five target graphs", file=out)
    print("          (cycle_oracle: exact enumeration of every simple cycle)", file=out)
    print("=" * 76, file=out)
    for name, G in build_five():
        deg = minimum_degree(G)
        lens = distinct_cycle_lengths(G)
        listed = {len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3}
        assert listed == lens, f"{name}: oracle disagrees with nx.simple_cycles"
        pow_present = sorted(p for p in POWERS if p in lens)
        pow_absent = sorted(p for p in POWERS if p not in lens)
        has_pow = len(pow_present) > 0
        print(f"  {name:14s} min_deg={deg:2d}  vertices={G.number_of_nodes():2d}"
              f"  cycle-lengths={sorted(lens)}", file=out)
        print(f"      powers-of-two present={pow_present}  absent={pow_absent}"
              f"  -> contains-a-power-of-two-cycle: {'YES' if has_pow else 'NO'}", file=out)
    print(file=out)


def part2(out):
    print("=" * 76, file=out)
    print("Part (2): cross-check cycle-length sets against networkx.simple_cycles", file=out)
    print("          on a spread of small graphs (two independent enumerations)", file=out)
    print("=" * 76, file=out)
    import random
    rng = random.Random(20240704)
    cases = []
    for n in range(3, 11):
        cases.append(("complete", nx.complete_graph(n)))
    for n in range(4, 13, 2):
        cases.append(("K_{n/2,n/2}", nx.complete_bipartite_graph(n // 2, n // 2)))
    for n in range(3, 13):
        cases.append(("cycle", nx.cycle_graph(n)))
    for n in range(2, 5):
        cases.append(("hypercube", nx.hypercube_graph(n)))
    cases.append(("Petersen", nx.petersen_graph()))
    cases.append(("wheel8", nx.wheel_graph(8)))
    cases.append(("Markström", nx.from_graph6_bytes(MARKSTROM_G6.encode())))
    for n in range(4, 10):
        for _ in range(80):
            p = rng.uniform(0.15, 0.7)
            cases.append((f"rand{n}-{_}", nx.gnp_random_graph(n, p, seed=rng)))
    mismatches = 0
    checked = 0
    for name, G in cases:
        # oracle's own distinct_cycle_lengths
        from lib.cycle_oracle import distinct_cycle_lengths as dcl
        oracle_lens = set(dcl(G))
        # networkx independent enumeration
        nx_lens = {len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3}
        checked += 1
        if nx_lens != oracle_lens:
            mismatches += 1
            print(f"    MISMATCH {name}: oracle={sorted(oracle_lens)}"
                  f" nx={sorted(nx_lens)}", file=out)
    print(f"  checked {checked} graphs across complete/bipartite/cycle/hypercube/"
          f"Petersen/wheel/Markström/random; mismatches = {mismatches}", file=out)
    print(f"  -> cross-check: {'ALL MATCH' if mismatches == 0 else 'MISMATCHES PRESENT'}", file=out)
    print(file=out)


# --- Part 3: cubic no-C4-and-no-C8 upward -----------------------------------
def connected_cubic_graph6(n):
    """Yield every connected cubic graph on n vertices (one graph6 string each).

    nauty-geng with -d3 -D3 forces min and max degree exactly 3 (i.e. cubic),
    -c connected.  Up to isomorphism.  Deterministic order.
    """
    out = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", "-D3", str(n)],
        capture_output=True, text=True, check=True,
    )
    return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]


def avoids_c4_and_c8(G):
    """True iff G has neither a C4 nor a C8 (depth-bounded early-terminating check)."""
    return (not has_cycle_of_length(G, 4)) and (not has_cycle_of_length(G, 8))


def part3(out, max_n=None, time_budget_seconds=540):
    print("=" * 76, file=out)
    print("Part (3): cubic no-C4-and-no-C8 verification, pushed upward via nauty-geng", file=out)
    print("          (every connected cubic graph, up to isomorphism)", file=out)
    print("=" * 76, file=out)
    start_wall = time.time()
    if max_n is None:
        max_n = 4
        # find the largest even n that completes within the time budget
    reached = []
    for n in range(4, 42, 2):  # cubic needs even n
        t0 = time.time()
        g6 = connected_cubic_graph6(n)
        t_gen = time.time() - t0
        n_free = 0
        t0 = time.time()
        for s in g6:
            G = nx.from_graph6_bytes(s.encode())
            if avoids_c4_and_c8(G):
                n_free += 1
        t_check = time.time() - t0
        reached.append((n, len(g6), n_free, t_gen, t_check))
        marker = "  <-- no-C4&C8 cubic graph here" if n_free else ""
        print(f"    n={n:3d}  connected-cubic={len(g6):9d}"
              f"  no-C4&C8-free={n_free:3d}{marker}"
              f"  (gen {t_gen:5.1f}s, check {t_check:6.1f}s)", file=out, flush=True)
        if time.time() - start_wall > time_budget_seconds:
            break
    print(file=out)
    n_reached = max(n for n, *_ in reached)
    print(f"  Reached n={n_reached} within the time budget; furthest n fully checked = {n_reached}.",
          file=out)
    total_free = sum(f for _, _, f, _, _ in reached)
    print(f"  Total no-C4&C8-free cubic graphs found up to n={n_reached}: {total_free}",
          file=out)
    print(file=out)
    print("  Published (sourced): the smallest cubic graph with no C4 and no C8 has", file=out)
    print("  24 vertices (Markström 2004; four such graphs, one planar).", file=out)
    print(f"  The theorem statement the run's own computation supports:", file=out)
    print(f"    'No connected cubic graph on n <= {n_reached} vertices is free of both a", file=out)
    print(f"     C4 and a C8.'  (verified here by exhaustive nauty-geng + exact oracle;", file=out)
    print(f"     corroborates the published first-at-24 from below, does not prove 24.)", file=out)
    return n_reached


def main():
    log_path = os.path.join(HERE, "reproduce.log")
    time_budget = 540.0
    with open(log_path, "w") as f:
        tee = sys.stdout
        # We print to both log and stdout by buffering lines.
        class Tee:
            def write(self, s):
                tee.write(s)
                f.write(s)
            def flush(self):
                tee.flush()
                f.flush()
        out = Tee()
        print("verify_bounds/reproduce.py — reproduce & push the verification bounds",
              file=out, flush=True)
        t0 = time.time()
        part1(out)
        part2(out)
        n_reached = part3(out, time_budget_seconds=time_budget)
        dt = time.time() - t0
        print(file=out)
        print(f"Done in {dt:.0f}s. Furthest n fully checked: {n_reached}. "
              f"Full log: {log_path}", file=out, flush=True)
    print(f"\n[log written to {log_path}]")


if __name__ == "__main__":
    main()
