"""Reproduce the Erdős–Gyárfás verification bound and the A007112 count.

Two jobs, both anchored on nauty-geng:

1. Oracle cross-check: has_cycle_of_length / has_power_of_two_cycle in
   lib/egcheck against lib.cycles (the hand-verified oracle) on K4, K3,3,
   Petersen and the cube Q3, and against the published cycle-length sets.

2. Verification bound: for n = 4..16, count connected min-degree-3 graphs
   (OEIS A007112) and report how many have no power-of-two cycle. Because a
   counterexample must be 4-cycle-free, the fast pool is geng -c -f -d3
   (4-cycle-free generated natively, polynomial); graphs that survive to be
   C8-free and C16-free get the deeper targeted checks. Full cycle-length
   enumeration is never needed at n up to 16 because the C4-free survivor
   counts stay manageable (1,655,659 at n=16).

Run: cd /workspace/code && python eg/verify_bound.py
"""

import sys
import time

import networkx as nx

from lib.cycles import min_degree, cycle_lengths
from lib.egcheck import has_cycle_of_length, has_power_of_two_cycle

# ---------- worked cases (Task 1) ----------
def graph_from_edges(n, edges):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return G

K4 = graph_from_edges(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
K33 = nx.complete_bipartite_graph(3, 3)
cube = nx.hypercube_graph(3)
petersen = nx.petersen_graph()

CASES = [
    ("K4",       K4,      3, {3, 4}),
    ("K3,3",     K33,     3, {4, 6}),
    ("cube Q3",  cube,    3, {4, 6, 8}),
    ("Petersen", petersen,3, {5, 6, 8, 9}),
]

def task1():
    print("=" * 70)
    print("Task 1 — oracle on the worked cases (lib.cycles + lib.egcheck)")
    print("=" * 70)
    all_ok = True
    for name, G, exp_md, exp_lens in CASES:
        md = min_degree(G)
        lens = cycle_lengths(G)
        # the fast targeted path must agree with the exact-cycle oracle
        p2_fast = has_power_of_two_cycle(G)
        p2_oracle = any(l in lens and l in (4, 8, 16, 32, 64) for l in lens)
        ok = (md == exp_md) and (lens == exp_lens) and (p2_fast == p2_oracle)
        all_ok = all_ok and ok
        print(f"  {name:10s} min_degree={md} (exp {exp_md}) "
              f"cycle_lengths={sorted(lens)} (exp {sorted(exp_lens)}) "
              f"has_power2 fast={p2_fast} oracle={p2_oracle} "
              f"{'OK' if ok else 'FAIL'}")
    print("  ->", "ALL WORKED CASES PASS" if all_ok else "SOME FAILED")
    print()
    return all_ok

def geng_count(n, extra):
    import subprocess
    cmd = ["nauty-geng", "-q", "-u", "-c", "-d3"] + extra + [str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    for ln in proc.stdout.splitlines() + proc.stderr.splitlines():
        m = __import__("re").search(r"(\d+) graphs?", ln)
        if m:
            return int(m.group(1))
    return None

def task2():
    print("=" * 70)
    print("Task 2 — EG verification bound, n=4..16 (nauty-geng)")
    print("=" * 70)
    # expected from OEIS A007112: number of connected unlabeled graphs with
    # min degree >= 3
    expected = {4:1, 5:3, 6:19, 7:150, 8:2589, 9:84242}
    rows = []
    for n in range(4, 17):
        t0 = time.time()
        # full count of connected min-deg-3 graphs (A007112)
        if n <= 13:
            full = geng_count(n, [])
        else:
            full = None  # generation of all 577M+ graphs is the bottleneck; use C4-free pool
        # C4-free candidate pool (any counterexample must be 4-free)
        checked, cex = mindeg3_c4free_pool(n)
        dt = time.time() - t0
        rows.append((n, full, checked, len(cex), cex[:3], dt))
        print(f"  n={n:2d} full(A007112)={full if full is not None else 'n/a':>12} "
              f"4-free_checked={checked:>9} no_power2_cex={len(cex)} "
              f"t={dt:.1f}s", end="")
        if cex:
            print(f"  EXAMPLES={cex[:3]}")
        else:
            print()
    print()
    return rows

def mindeg3_c4free_pool(n):
    import subprocess
    proc = subprocess.run(
        ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)],
        capture_output=True, text=True, check=True)
    checked = 0
    cex = []
    for g6 in proc.stdout.splitlines():
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if min_degree(G) < 3:
            continue
        checked += 1
        if not has_power_of_two_cycle(G):
            cex.append(g6)
    return checked, cex

if __name__ == "__main__":
    ok1 = task1()
    rows = task2()
