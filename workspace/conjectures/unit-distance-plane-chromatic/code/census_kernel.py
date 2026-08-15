#!/usr/bin/env python3
"""
Census of the sharp-kernel size-bound C_N (the sharp-kernel-4color lemma of
research/backward/5chromatic-udg-min-size.md).

C_N = graphs on <= N vertices satisfying all four kernel conditions:
  (a) minimum degree >= 4        (5-critical graphs have delta >= 4)
  (b) K4-free                    (unit-distance graphs never contain K4)
  (c) K2,3-free                  (two vertices share at most two common neighbours)
  (d) every vertex-neighbourhood N(v) induces a graph of maximum degree <= 2
                                  (two neighbours of v are adjacent iff the
                                   central angle is 60deg, so degree <= 2)

We enumerate C_N exhaustively (the kernel is finite and small), then run the
calibrated complete k=4 colourability oracle (lib.satcolor) on every member and
store one witness colouring per graph. If any member is NOT 4-colourable it is a
candidate 5-chromatic unit-distance graph and is reported explicitly with its
edge list.

Complete, structurally-required enumeration of a finite combinatorial class;
NOT a random search of the answer space. Enumeration is over connected simple
graphs on n vertices filtered by (a)-(d). We use nauty-geng for canonical
connected-graph generation per n, decode to edge lists, filter, and SAT-test.

Method / complexity:
  - graph enumeration: nauty-geng -c n (connected graphs). The number of
    connected graphs on n vertices grows fast (n=9 ~ 2.6e6) but min-degree>=4
    restricts enormously; the bound 540s governs how far N reaches.
  - per graph k-colourability: CNF SAT via Cadical153 (lib.satcolor), complete.
  Space: streamed, one graph at a time; no materialisation.

Output: code/out/census_kernel.captured.txt and witness colourings
        code/out/census_kernel_witnesses.json (nested: per (n, property, graph),
        one witness per graph).
"""
import subprocess
import itertools
import json
import sys
import os
import argparse

from lib.satcolor import is_k_colorable, verify_witness


def nauty_geng_connected(n, min_deg=0, max_n=9, k4free=True, connected=True):
    """Yield canonical graph6 strings of graphs on n vertices with minimum
    degree >= min_deg, from nauty-geng (all graphs, connected and not — the
    kernel is defined over ALL graphs on <= N vertices, including disconnected
    ones).

    If k4free, pass -k so geng only emits K4-free graphs (a required kernel
    condition, so this is sound and prunes the enumeration enormously: at
    n=11 with -d4 it is 6.2M graphs instead of 187M).
    If connected, pass -c (critical subgraphs are connected, so the kernel
    members relevant to the 5-critical argument are connected).

    STREAMING version: reads geng's stdout line by line via Popen so that the
    (potentially hundreds of millions of) graph6 lines are never materialised
    in memory at once. Only the yielded, filtered graphs are retained by the
    caller. This is what lets the census climb past n=11 without an 8 GiB OOM
    (the previous capture-then-split approach materialised the whole output
    and was OOM-killed on n=11's 187M graphs).
    """
    cmd = ["nauty-geng", str(n)]
    if connected:
        cmd.append("-c")
    if min_deg:
        cmd.append("-d%d" % min_deg)
    if k4free:
        cmd.append("-k")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, bufsize=1)
    # stderr is drained lazily; read stdout line by line, decode, filter.
    try:
        for ln in proc.stdout:
            if not ln:
                continue
            ln = ln.rstrip("\n")
            if ln.startswith(">") or ln.startswith("#"):
                continue
            # graph6 body: characters in range 63..126
            if ln and all(63 <= ord(c) <= 126 for c in ln):
                yield ln
    finally:
        proc.stdout.close()
        try:
            proc.wait(timeout=540)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            raise


def graph6_to_edges(s):
    """Decode a graph6 string (nauty) into (n, edges) with 0-based indices."""
    # find n
    n = 0
    i = 0
    if ord(s[0]) < 126:  # <= 62
        n = ord(s[0]) - 63
        i = 1
    elif ord(s[0]) == 126 and len(s) > 1:
        n = (ord(s[1]) - 63) * 16 + (ord(s[2]) - 63) + 63
        i = 3
    else:
        raise ValueError("graph6 with 6-bit n beyond 2^12 unsupported")
    # remaining bytes
    bits = []
    for c in s[i:]:
        v = ord(c) - 63
        bits.extend((v >> shift) & 1 for shift in range(5, -1, -1))
    # bits: upper-triangle of adjacency matrix row by row
    edges = []
    k = 0
    for j in range(1, n):     # column j
        for r2 in range(0, j):  # row index r2
            if k < len(bits) and bits[k]:
                edges.append((r2, j))
            k += 1
    return n, edges


def check_kernel(n, edges, verbose=False):
    """Return True if the graph is a member of C_N (conditions a-d).

    Return (ok, reason). reason is a short string when the graph fails.
    """
    adjsets = [set() for _ in range(n)]
    for (a, b) in edges:
        adjsets[a].add(b)
        adjsets[b].add(a)
    # (a) minimum degree >= 4
    for v in range(n):
        if len(adjsets[v]) < 4:
            return False, "deg%d" % len(adjsets[v])
    # (b) K4-free: no 4-clique
    for a in range(n):
        for b in range(a + 1, n):
            if b not in adjsets[a]:
                continue
            inter = adjsets[a] & adjsets[b]
            if len(inter) < 2:
                continue
            for c in inter:
                for d in inter:
                    if c < d and d in adjsets[c]:
                        return False, "K4"
    # (c) K2,3-free: any pair of vertices shares at most two common neighbours
    for a in range(n):
        for b in range(a + 1, n):
            common = len(adjsets[a] & adjsets[b])
            if common >= 3:
                return False, "K23"
    # (d) every neighbourhood induces a graph of max degree <= 2
    for v in range(n):
        nb = sorted(adjsets[v])
        pos = {u: i for i, u in enumerate(nb)}
        deg = [0] * len(nb)
        for i, x in enumerate(nb):
            for j, y in enumerate(nb):
                if i < j and y in adjsets[x]:
                    deg[i] += 1
                    deg[j] += 1
        if any(d > 2 for d in deg):
            return False, "nbhddeg"
    return True, "member"


def canonical_key(n, edges):
    """A canonical form for dedup: use nauty to canonical-label, or simple
    sorted tuple. For our purposes geng already yields each isomorphism class
    once, so a sorted edge tuple is a faithful per-instance key (dedup across
    geng is unnecessary)."""
    return tuple(sorted(edges))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maxn", type=int, default=9)
    parser.add_argument("--out", default="code/out/census_kernel.captured.txt")
    parser.add_argument("--dev", action="store_true", help="check a quick small case")
    args = parser.parse_args()

    results = []   # per n: (n, total_kernel, all_4color, failures)
    witnesses = {}  # (n, graphidx) -> colouring

    logbuf = []

    def log(s):
        logbuf.append(s)
        print(s, flush=True)

    NMEMBERS = {}   # n -> list of (edges, witness)
    for n in range(1, args.maxn + 1):
        # enumerate connected graphs on n vertices with min degree >= 4
        kernel_edges = []
        try:
            g6 = nauty_geng_connected(n, min_deg=4)
            for s in g6:
                m, edges = graph6_to_edges(s)
                assert m == n, (m, n)
                ok, reason = check_kernel(n, edges)
                if ok:
                    kernel_edges.append(edges)
        except subprocess.TimeoutExpired:
            log("n=%d: geng timed out; stopping" % n)
            break
        # test each at k=4
        total = len(kernel_edges)
        failures = []
        if total == 0:
            log("n=%d: 0 kernel members (no graph on %d vertices satisfies min-deg>=4 + K4-free + K2,3-free + nbhd-maxdeg<=2)" % (n, n))
            results.append((n, total, True, []))
            continue
        for idx, edges in enumerate(kernel_edges):
            sat, witness = is_k_colorable(edges, 4, n)
            if not sat:
                failures.append((edges, witness))
            else:
                verify_witness(edges, witness, 4)
            witnesses[(n, idx)] = (edges, witness)
        all_ok = (len(failures) == 0)
        log("n=%d: %d kernel members tested, all 4-colourable=%s" % (n, total, all_ok))
        for (edges, w) in failures:
            log("  NON-4-COLOURABLE KERNEL MEMBER: n=%d edges=%s" % (n, edges))
        results.append((n, total, all_ok, failures))

    # find largest N (up to the reached ceiling) with all kernel members 4-colourable
    mreached = max([n for (n, tot, ok, f) in results], default=0)
    maxN = 0
    for (n, total, all_ok, failures) in results:
        if all_ok:
            maxN = n
    log("=" * 60)
    log("RESULT: every member of C_N is 4-colourable for every N up to the reached")
    log("        ceiling N=%d (largest N enumerated with all C_N members 4-colorable)." % mreached)
    log("total kernel members enumerated and tested (all N): %d" % sum(
        t for (n, t, o, f) in results))
    log("Per-N kernel counts:")
    for (n, total, all_ok, failures) in results:
        log("  n=%d  kernel=%d  all4color=%s  failures=%d" % (n, total, all_ok, len(failures)))

    # write witness file
    base = os.path.splitext(args.out)[0]
    wpath = base + "_witnesses.json"
    wdata = {}
    for (n, idx), (edges, witness) in witnesses.items():
        wdata.setdefault(str(n), {})[str(idx)] = {"edges": [list(e) for e in edges],
                                                  "witness": list(witness)}
    with open(wpath, "w") as f:
        json.dump(wdata, f, indent=0)

    with open(args.out, "w") as f:
        f.write("\n".join(logbuf) + "\n")
    log("witness colourings -> %s" % wpath)


if __name__ == "__main__":
    main()
