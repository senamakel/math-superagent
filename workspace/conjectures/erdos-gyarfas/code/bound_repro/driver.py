"""bound_repro/driver.py — reproduce Royle's n<=15 no-power-of-two-cycle bound.

For each n in 10..15 (then 16, 17 only if each n finishes in under 120 s):
  * enumerate every connected min-degree-3 C4-free graph via
        nauty-geng -f -d3 -c <n>
    (graph6, one per line, up to isomorphism) — exactly the family Royle's
    makeg scan covers (min degree 3, no C4);
  * for each graph, graph6 -> networkx, then run a *depth-bounded DFS* looking
    for a simple cycle of length 8 (and length 16 too at n >= 16).  These are
    the only power-of-two cycle lengths possible: the family is C4-free by
    construction and 32 > 17 >= any n here.

Detector: `has_simple_cycle_length(G, L)` is a from-scratch canonical-start,
depth-bounded DFS (a simple path of length at most L, closing edge back to
the cycle's minimum vertex, canonical start so each cycle is found once when
the search starts at that cycle's minimum vertex).  It is written here
independently of the oracle, then cross-checked against
lib.cycle_oracle.has_cycle_of_length on ~200 uniformly sampled graphs spread
across all processed n: every sampled verdict for C8 (and C16 at n >= 16)
must agree.

Expected (reproduces the published n <= 15 bound):
    #without-any-power-of-2-cycle == 0 for every n.

Outputs (under code/out/bound_repro/):
    counts.txt              n, #graphs, #with-C8, #without-any-power-of-2-cycle, seconds
    oracle_crosscheck.txt   the detector-vs-oracle agreement report

Complexity: enumeration is the sized brute-force oracle (exponential in the
graph count; NO4 grows super-exponentially ~ K*3^n*(n-10)!) — never the method
at larger n.  Per-graph detection is O(#simple paths of length <= L) with
early termination, depth-bounded.  Detector-vs-oracle agreement on samples is
what lets us trust the depth-bounded DFS over the whole generation, where
calling the full oracle on every graph would be prohibitive.
"""
import json
import os
import random
import subprocess
import time

import networkx as nx

from lib.cycle_oracle import has_cycle_of_length

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "out", "bound_repro"))
POWERS_CHECKED = (8, 16)  # C4 ruled out by geng -f; 32 > any n here
SAMPLE_PER_N = 34          # -> ~204 samples across n=10..15 (>= 200 target)


def has_simple_cycle_length(G, L):
    """True iff G has a simple cycle of length exactly L (L >= 3).

    Independent depth-bounded DFS: each cycle is reported from its *minimum*
    vertex, and only vertices >= start are visited, so a cycle of length L is
    found exactly once — when the search starts at that cycle's minimum
    vertex.  Depth never exceeds L, giving early termination.  Written from
    scratch, then cross-checked against lib.cycle_oracle.has_cycle_of_length.
    """
    if L < 3:
        return False
    adj = {u: list(G[u]) for u in G}
    for start in sorted(G):
        visited = {start}

        def dfs(cur, depth):
            for nb in adj[cur]:
                if nb == start:
                    if depth + 1 == L:
                        return True
                elif depth + 1 < L and nb >= start and nb not in visited:
                    visited.add(nb)
                    if dfs(nb, depth + 1):
                        return True
                    visited.remove(nb)
            return False

        if dfs(start, 0):
            return True
    return False


def no_power_of_two_C8C16(G, n):
    """True iff G has no C8 and (at n >= 16) no C16 — i.e. no power-of-two
    cycle at all among the lengths that are attainable here."""
    for L in POWERS_CHECKED:
        if L <= n and has_simple_cycle_length(G, L):
            return False
    return True


def enumerate_c4free_min3(n):
    """Every connected min-degree-3 C4-free graph6 string on n vertices."""
    proc = subprocess.run(
        ["nauty-geng", "-f", "-d3", "-c", str(n)],
        capture_output=True, text=True, check=True,
    )
    return [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]


def main():
    os.makedirs(OUT, exist_ok=True)
    counts_path = os.path.join(OUT, "counts.txt")
    xcheck_path = os.path.join(OUT, "oracle_crosscheck.txt")

    counts_lines = []
    xcheck_lines = []
    xcheck_lines.append("Detector (depth-bounded DFS) vs lib.cycle_oracle.has_cycle_of_length")
    xcheck_lines.append("graph6  n  idx  L  detector  oracle  ->  AGREE/MISMATCH")
    total_sampled = 0
    total_mismatch = 0

    rng = random.Random(20250714)

    def run_n(n, hard_budget=None):
        nonlocal total_sampled, total_mismatch
        t0 = time.time()
        g6_list = None
        try:
            g6_list = enumerate_c4free_min3(n)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"nauty-geng failed at n={n}: {e}") from e
        t_gen = time.time() - t0
        if hard_budget is not None and t_gen > hard_budget:
            counts_lines.append(f"{n}, {len(g6_list)}, _skipped_, _skipped_, {t_gen:.1f}")
            xcheck_lines.append(f"n={n}: generation took {t_gen:.1f}s > "
                                f"{hard_budget:.1f}s budget — skipped")
            return False

        # Parse graph6 lines, decoding any graph6 bytes into networkx graphs.
        graphs = []
        for s in g6_list:
            s = s.strip()
            if not s:
                continue
            try:
                graphs.append(("", nx.from_graph6_bytes(s.encode())))
            except Exception:
                # graph6 is ASCII; keep the raw line as the key for reporting.
                graphs.append((s, nx.from_graph6_bytes(s.encode())))

        n_have_c8 = 0
        n_no_pow2 = 0
        t_check = time.time()
        for _, G in graphs:
            if has_simple_cycle_length(G, 8):
                n_have_c8 += 1
                continue  # has a power-of-two cycle already
            if n >= 16 and has_simple_cycle_length(G, 16):
                continue
            n_no_pow2 += 1  # neither C8 nor C16 -> no power-of-two cycle here
        t_check = time.time() - t_check

        # Cross-check detector vs oracle on a uniform sample across indices.
        idx_pool = list(range(len(graphs)))
        sample = rng.sample(idx_pool, min(SAMPLE_PER_N, len(idx_pool)))
        for i in sample:
            s, G = graphs[i]
            for L in POWERS_CHECKED:
                if L > n:
                    continue
                det = has_simple_cycle_length(G, L)
                ora = has_cycle_of_length(G, L)
                total_sampled += 1
                agree = (det == ora)
                if not agree:
                    total_mismatch += 1
                xcheck_lines.append(
                    f"{s or 'g6'} {n:2d} {i:5d} {L:2d}  {int(det)}       {int(ora)}"
                    f"      -> {'AGREE' if agree else 'MISMATCH'}")

        counts_lines.append(
            f"{n}, {len(graphs)}, {n_have_c8}, {n_no_pow2}, "
            f"{t_gen + t_check:.1f}")
        return True

    # n=10..15 always
    for n in range(10, 16):
        finished = run_n(n)
    # n=16..17 only if each n (generation) finishes in under 120 s
    for n in (16, 17):
        ok = run_n(n, hard_budget=120.0)
        if not ok:
            break

    xcheck_lines.append(f"\nTOTAL sampled verdicts: {total_sampled}, "
                        f"mismatches: {total_mismatch}")
    xcheck_lines.append("-> ALL AGREE" if total_mismatch == 0
                        else "-> MISMATCHES PRESENT (FAIL)")
    if total_mismatch:
        raise SystemExit(f"cross-check FAILED: {total_mismatch} mismatch(es)")

    with open(counts_path, "w") as f:
        f.write("# n, #graphs, #with-C8, #without-any-power-of-2-cycle, seconds\n")
        f.writelines(ln + "\n" for ln in counts_lines)
    with open(xcheck_path, "w") as f:
        f.writelines(ln + "\n" for ln in xcheck_lines)

    print(f"[wrote {counts_path}]")
    print(f"[wrote {xcheck_path}]")


if __name__ == "__main__":
    main()
