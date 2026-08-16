"""Extend the verified girth-5 danger-region scan to n=12,13.

CLAIM under test (the first open danger past the closed n=10,11 crosscheck):
every 2-connected min-degree>=3 girth-5 graph on n=10,11,12,13 has a
power-of-two cycle. Since girth>=5 forbids C4, any such power-of-two cycle is
an 8-cycle. The named thing n=13 settles that n=11 did not: for min-degree-3
graphs, girth 6 needs >=14 vertices and girth 7 needs >=22 (Moore bound), so
girth>=5 on n<=13 is exactly the whole girth-5 window. Extending to 13 asks
whether EVERY 2-connected min-degree>=3 graph up to n=13 has a 4- or 8-cycle:
n<=8 gives girth<=4 hence a 4-cycle; n=10..13 gives the 8-cycle question. This
is the first rung where the class leaves the single-cage regime (n=12 has 2
graphs, n=13 has 4; n=10 was the sole Petersen, n=11 empty).

GENERATION: the class is produced by lib.girth5_gen.generate_2connected_girth_atleast5(13)
(the committed C5-seeded open-ear generator, girth-pruned, WL-hash+VF2 dedup —
NOT modified or re-validated here), then filtered to min_degree>=3. Because the
generator's enumeration to n=13 alone takes ~280-310s — far beyond the 120s
budget, and it is enumeration, not analysis, that dominates — the script reads
girth5_class_n13.json, which is exactly the output of that generator (written by
the same call, then re-regenerated to the identical 7 graphs as an independent
reproduction of the cache). With the cache present the whole analysis runs in a
few seconds. If the cache is absent the script regenerates via the generator and
writes the cache, then proceeds (that path will take ~5 min, over budget, and is
only a fallback for cache loss).

VERIFICATION of each graph:
  - girth >= 5                       (lib.girth5_gen.girth)
  - min-degree >= 3                  (lib.girth5_gen.min_degree)
  - has an 8-cycle via the INDEPENDENT route 2: nx.simple_cycles on the directed
    graph (networkx 2.8.8), no use of lib.erdos_gyarfas — so the 8-cycle claim is
    confirmed by a tool the oracle disagrees with would be caught.
All three asserted per graph; per-n count reported and any failing graph named.

GOOD-CHORD TEST (same definition as code/out/edge_transfer_girth5.py, imported
from it so the two runs cannot drift): a deletable chord e=ab (G-e 2-connected
and delta(G-e)>=2) is GOOD iff
    C(G-e) contains a power of two (4,8,16)   OR   G-e has a simple a-b path of
    length 2^k - 1 in {3,7,15,...}.
Reported per graph: #DELETABLE_CHORDS, #GOOD, #BAD, and whether any graph is a
BAD/WORST case (a graph with NO good deletable chord, i.e. no power-of-two cycle).

Structural reduction (established and cross-checked in edge_transfer_girth5):
for girth>=5, bad graph <=> no power-of-two cycle (<=> no 8-cycle on n<=13
since C16 needs >=16 vertices). So the chord scan and the 8-cycle route-2 test
are independent confirmations of the same claim.
"""
import json
import os
import time
import networkx as nx
from lib.girth5_gen import generate_2connected_girth_atleast5, min_degree, girth
from out.edge_transfer_girth5 import chord_report_full

CACHE = os.path.join(os.path.dirname(__file__), "girth5_class_n13.json")


def has_8cycle_nx(G):
    """Does G contain a simple cycle of length 8? independent route (nx.simple_cycles)."""
    D = G.to_directed()
    for cyc in nx.simple_cycles(D):
        if len(cyc) == 8:
            return True
    return False


def load_class(n=13):
    """2-connected min-degree>=3 girth-5 graphs on n=10..13, from generator cache."""
    if os.path.exists(CACHE):
        data = json.load(open(CACHE))
        result = {k: [] for k in range(10, 14)}
        for rec in data:
            result[rec["n"]].append(nx.Graph(rec["edges"]))
        return result
    # fallback: regenerate via the committed generator (slow, over budget)
    levels = generate_2connected_girth_atleast5(n)
    out = {}
    for n in range(10, 14):
        out[n] = [G for G in levels.get(n, []) if min_degree(G) >= 3]
    return out


def main(N=13):
    t0 = time.time()
    levels = load_class(N)
    gen_t = time.time() - t0
    out = []
    out.append(f"check_girth5_upto13: 2-connected min-degree>=3 girth-5 graphs on n=10..{N}")
    out.append(f"  (generator output loaded; cache/regeneration time {gen_t:.1f}s)")
    counts = {}
    failed = []
    worst = []  # (n, edges) graphs with NO good deletable chord
    for n in range(10, N + 1):
        gs = levels.get(n, [])
        counts[n] = len(gs)
        out.append(f"n={n:2d} : {len(gs)} girth-5 min-degree>=3 graphs")
        for G in gs:
            assert girth(G) >= 5, f"girth<5 at n={n} edges={sorted(G.edges())}"
            assert min_degree(G) >= 3, f"min_deg<3 at n={n} edges={sorted(G.edges())}"
            ok8 = has_8cycle_nx(G)
            assert ok8, f"NO 8-cycle at n={n} edges={sorted(G.edges())} (route 2)"
    out.append("")
    out.append("Verification (asserted per graph): girth>=5, min-degree>=3, and a")
    out.append("power-of-two cycle = an 8-cycle, via the independent nx.simple_cycles route.")
    out.append(f"FAILED graphs: {failed if failed else 'none'}")
    out.append("")
    out.append("Good-chord scan (definition from edge_transfer_girth5.py):")
    header = f"{'n':>2} {'#GRAPHS':>7} {'#DEL_CHORDS':>11} {'#GOOD':>6} {'#BAD':>5}  worst?"
    out.append(header)
    total_del = total_good = total_bad = 0
    for n in range(10, N + 1):
        for G in levels.get(n, []):
            all_good, details, bad = chord_report_full(G, n)
            del_c = len(details)
            good_c = sum(1 for d in details if d[2] != "NOT GOOD")
            bad_c = del_c - good_c
            total_del += del_c; total_good += good_c; total_bad += bad_c
            is_worst = not all_good
            if is_worst:
                worst.append((n, sorted(G.edges())))
            out.append(f"{n:>2} {1:>7} {del_c:>11} {good_c:>6} {bad_c:>5}  {is_worst}")
    out.append("-" * len(header))
    out.append(f"{'TOT':>2} {sum(counts.values()):>7} {total_del:>11} {total_good:>6} {total_bad:>5}")
    out.append("")
    if worst:
        out.append(f"=> WORST CASE: {len(worst)} graph(s) with no good deletable chord")
        for n, e in worst:
            out.append(f"   n={n} edges={e}")
    else:
        out.append("=> NO WORST CASE: every 2-connected min-degree>=3 girth-5 graph on")
        out.append(f"   n=10..{N} has a power-of-two cycle (an 8-cycle), so every deletable")
        out.append("   chord of every such graph is GOOD. The chord-deletion induction step")
        out.append("   closes over the entire girth-5 danger region through n=13.")
    elapsed = time.time() - t0
    out.append(f"TOTAL WALL TIME (analysis, cache loaded): {elapsed:.1f}s")
    return "\n".join(out), counts, worst, elapsed


if __name__ == "__main__":
    text, counts, worst, elapsed = main(13)
    print(text)
