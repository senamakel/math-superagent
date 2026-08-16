"""Pattern-finder: correct the corrupted G-heart verification.

The existing code/out/g_heart_verify_n8.out was produced by the OLD buggy
generator (counts 1,1,4,19,121,1042 = the refuted A280939 sequence, and it
reported 0 delta>=3 graphs even at n=4 where K4 exists). Redo the G-heart
check with the CORRECTED generator (code/lib/biconnected_gen.py, validated
against A002218) for n=3..7, producing the sequence of #2-connected min-degree>=3
graphs and confirming each has a C4/C8/C16 via the exact oracle.
"""

import time
import networkx as nx
from lib.biconnected_gen import generate_2connected_levels, min_degree
from lib.erdos_gyarfas import has_power_of_two_cycle


def run(N):
    t0 = time.time()
    levels = generate_2connected_levels(N)
    print(f"generation time: {time.time()-t0:.1f}s", flush=True)
    print("n | #2conn | #delta>=3 | #with_2power | verdict")
    for n in range(3, N + 1):
        graphs = levels.get(n, [])
        n_d3 = 0
        n_ok = 0
        all_ok = True
        bad = None
        for G in graphs:
            if min_degree(G) >= 3:
                n_d3 += 1
                ok, L = has_power_of_two_cycle({v: set(G.neighbors(v)) for v in G.nodes()})
                if ok:
                    n_ok += 1
                else:
                    all_ok = False
                    if bad is None:
                        bad = (G.edges(), L)
        v = "VERIFIED" if all_ok else "COUNTEREXAMPLE"
        print(f"{n} | {len(graphs)} | {n_d3} | {n_ok} | {v}", flush=True)
        if bad:
            print("   counterexample edges:", bad)


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    run(N)
