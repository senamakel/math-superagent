"""G-heart lemma verification: every 2-connected graph with minimum degree >= 3
on at most N vertices contains a cycle of length 4, 8, or 16.

Method:
  1. Generate the 2-connected class exactly by ear decomposition, deduplicated
     by WL-hash bucket + exact VF2 within a bucket
     (code/lib/biconnected_gen_hash.generate_2connected_levels_hash). Its counts
     match OEIS A002218 (1,1,3,10,56,468,7123 for n=3..8), so generation is
     complete and dedup is exact.
  2. Filter to minimum degree >= 3.
  3. Check every such graph with the exact oracle
     (code/lib/erdos_gyarfas.has_power_of_two_cycle), which reproduces every
     worked example in problem.md.

This is independent of the SAT verification of the general minimum-degree-3
class: we generate the class bijectively and oracle-check every graph, so every
2-connected delta>=3 graph on <= N vertices is decided exactly on whether it
has a 4/8/16 cycle.

NOTE: the previous g_heart_verify_n8.out (counts 1,1,4,19,121,1042) came from
the corrupt layer_by_layer generator and its VERIFIED verdicts must not be
trusted. This program is the replacement.

Complexity: the 2-connected class is super-exponential, so generation stops at
the largest N whose class is tractable. We fix N at the largest value that
finishes well under the timeout and report the verdict at each n plus the reach.
"""
import time
import networkx as nx

from lib.biconnected_gen_hash import generate_2connected_levels_hash, min_degree
from lib.erdos_gyarfas import has_power_of_two_cycle


def run(N, out_path=None):
    t0 = time.time()
    levels = generate_2connected_levels_hash(N)
    gen_time = time.time() - t0

    lines = [
        "# G-heart lemma verification: every 2-connected delta>=3 graph on <=N vertices",
        "# has a cycle of length 4, 8, or 16 (power of two, k>=2).",
        f"# Largest N reached: {N}",
        f"# Generation time: {gen_time:.1f}s",
        "#",
        "# n | #2conn | #delta>=3 | #with_2power | verdict",
        "# --+--------+-----------+--------------+--------",
    ]
    print(f"Largest N reached: {N}  (gen {gen_time:.1f}s)")
    verdicts = []
    any_counter = False
    for n in range(3, N + 1):
        graphs = levels.get(n, [])
        n_d3 = 0
        n_ok = 0
        all_ok = True
        first_bad = None
        for G in graphs:
            if min_degree(G) >= 3:
                n_d3 += 1
                ok, L = has_power_of_two_cycle({v: set(G.neighbors(v)) for v in G.nodes()})
                if ok:
                    n_ok += 1
                else:
                    all_ok = False
                    if first_bad is None:
                        first_bad = sorted(G.nodes())
        v = "VERIFIED" if all_ok else "COUNTEREXAMPLE FOUND"
        if not all_ok:
            any_counter = True
        verdicts.append((n, len(graphs), n_d3, n_ok, v))
        row = f"{n} | {len(graphs)} | {n_d3} | {n_ok} | {v}"
        print(row, flush=True)
        lines.append(row)
    if first_bad is not None:
        lines.append(f"# Example counterexample vertex set: {first_bad}")
    if out_path:
        with open(out_path, "w") as f:
            f.write("\n".join(lines) + "\n")
    return verdicts, any_counter


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    out = sys.argv[2] if len(sys.argv) > 2 else None
    res, any_counter = run(N, out)
    print()
    print("Summary:", "COUNTEREXAMPLE FOUND" if any_counter else "all delta>=3 2-connected graphs on <=N vertices VERIFIED to contain a 4/8/16 cycle")
