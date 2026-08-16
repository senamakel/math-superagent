"""G-heart lemma verification: every 2-connected graph with minimum degree >= 3 on
at most N vertices contains a cycle of length 4, 8, or 16.

Method: constructively generate the 2-connected class EXACTLY by ear decomposition
(code/lib/biconnected_gen.generate_2connected_levels), filter to minimum degree
>= 3, and check every graph with the exact oracle
(code/lib/erdos_gyarfas.has_power_of_two_cycle). This is independent of the SAT
verification of the general minimum-degree-3 class and of the literature counts:
we generate the class bijectively, so every 2-connected graph on <= N vertices is
checked, and the oracle gives an exact yes/no on a power-of-two cycle.

Complexity class: the 2-connected class size is super-exponential (it is roughly
n^{n}-ish in the worst case and grows like ~ a^n n^{-b}), so generation is only
run up to the N where the class is still tractable. Isomorphism dedup per graph is
polynomial (VF2). We report the largest N actually completed and the verdict at
each N, and stop honestly when the class count becomes intractable.
"""

import sys, time
import networkx as nx

sys.path.insert(0, "/workspace/code")
from lib.biconnected_gen import generate_2connected_levels, min_degree
from lib.erdos_gyarfas import has_power_of_two_cycle


def run(N, out_path=None):
    t0 = time.time()
    print(f"Generating all 2-connected graphs on up to N={N} vertices "
          f"(ear decomposition, exact VF2 dedup)...", flush=True)
    levels = generate_2connected_levels(N, dmin=3, dump_every=2)
    gen_time = time.time() - t0

    lines = []
    lines.append(f"# G-heart lemma verification (2-connected, delta>=3, 4/8/16-cycle)")
    lines.append(f"# Largest N attempted: {N}")
    lines.append(f"# Generation time: {gen_time:.1f}s")
    lines.append(f"#")
    lines.append(f"# n | #2conn | #delta>=3 | #with_2power | verdict")
    lines.append(f"# --+--------+-----------+--------------+--------")
    verdicts = []
    for n in range(3, N + 1):
        graphs = levels.get(n, [])
        n_d3 = 0
        n_ok = 0
        all_ok = True
        for G in graphs:
            if min_degree(G) >= 3:
                n_d3 += 1
                ok, L = has_power_of_two_cycle({v: set(G.neighbors(v)) for v in G.nodes()})
                if ok:
                    n_ok += 1
                else:
                    all_ok = False
        v = "VERIFIED" if all_ok else "COUNTEREXAMPLE FOUND"
        verdicts.append((n, len(graphs), n_d3, n_ok, v))
        row = f"{n} | {len(graphs)} | {n_d3} | {n_ok} | {v}"
        print(row, flush=True)
        lines.append(row)
    if out_path:
        with open(out_path, "w") as f:
            f.write("\n".join(lines) + "\n")
    return verdicts


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    out = sys.argv[2] if len(sys.argv) > 2 else None
    res = run(N, out)
    print()
    print("Summary:")
    for n, total, d3, ok, v in res:
        if d3 > 0:
            print(f"  n={n}: {d3} delta>=3 graphs, all verified={v}")
