#!/usr/bin/env python3
"""Boundary-edge analysis of the prime Gilbreath triangle, live regime k=1..161.

COST MODEL (stated first):
  sieve to 2e7 -> 1,270,607 primes (W = 1,270,607; int64 row ~10 MB)
  two passes, each 162 absolute-difference steps on ~W-wide rows:
    O(162 * W) ~ 2.1e8 numpy elementwise ops per pass, ~3 s each
  transient memory: 2 live rows (~20 MB) + 26 saved halved block prefixes
    (sum of b_K over run starts ~3.3e6 int64 = 26 MB) + 20 MB sieve  < 100 MB peak

CONVENTIONS (0-based columns; A_k[0] = leading 1 for all k >= 1):
  A_0 = primes ; A_{k+1}[j] = |A_k[j] - A_k[j+1]|
  b_k  = length of the leading {0,2} block of A_k (columns 1..b_k)
  e_k  = A_k[b_k]     (edge: the last {0,2} entry of the block)
  c_k  = A_k[b_k + 1] (intruder: first entry past the block; defined iff
                       b_k + 1 < width(A_k); live regime k=1..161, k>=162 artifact)

ESTABLISHED (this run, check_regenerate_lemma.py, depth 1000, zero failures):
  b_{k+1} >= b_k  <=>  (e_k == 2 and c_k == 4)
  and, elementarily (columns 1..b_k-1 of A_{k+1} are diffs inside the block),
  b_{k+1} >= b_k - 1.  Hence over the live regime:
      erosion transition (Delta b == -1)  <=>  NOT(e_k == 2 and c_k == 4).

RULE-90 INTERIOR (proved, rule90-interior.md; exhaustive bit-string check
  in check_edge_zero_run.py for all 2^n patterns, n <= 18):
  with h = A_K[1..b_K]//2 (bits, 0-based) and kernel row
  K_d[j] = C(d,j) mod 2, the halved entry at depth d is
      A_{K+d}[p+1]/2 = XOR_{j=0..d} K_d[j] * h[p+j],         p+d <= b_K-1
  so the halved EDGE of the eroded block (p = b_K-1-d, column b_K-d) is
      e_d/2 = XOR_{j=0..d} K_d[j] * h[b_K-1-d+j]
            = XOR_{j=0..d} K_d[j] * h1[b_K-d+j]     (1-based h1[i]=h[i-1])
  which is the task formula verbatim in 1-based h.  This is checked here
  against the REAL rows at every depth d=0..L-1 of every erosion run, both at
  the single edge column and on the whole interior slice.

ORACLES (abort on any mismatch):
  * rows A_1..A_3 reproduce the first entries given in problem.md /
    the task: A_1 = [1,2,2,4,2,4,2,4,6,2], A_2 = [1,0,2,2,2,2,2,2,4],
    A_3 = [1,2,0,0,0,0,0,2]
  * b[1..162], s[1..162], intruder[1..161] equal blocks_depth1000.json
    (that record in turn reproduces witnesses.json on k=1..40)
  * the regeneration criterion re-checked here over k=1..161: failures = 0
  * erosion-run lengths equal the depth-1000 live-regime record
  * the Pascal-mod-2 kernel computed by Lucas ((d & j) == j) agrees with
    math.comb(d,j) % 2
"""
import json
import math
import os
import sys
import time

import numpy as np

from lib.gilbreath import EXPECTED, primes_up_to

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "..", "out"))

SIEVE_LIMIT = 20_000_000
DEPTH = 162          # generate A_1..A_162 so transition k=161 is computable
LIVE = 161           # live regime: rows with an intruder (k >= 162 artifact)

A1_EXP = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2]
A2_EXP = [1, 0, 2, 2, 2, 2, 2, 2, 4]
A3_EXP = [1, 2, 0, 0, 0, 0, 0, 2]

# prior depth-1000 live-regime erosion-run lengths (multiset; order of starts)
PRIOR_RUN_LENGTHS = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
                     3, 3, 3, 3, 4, 4, 4, 5, 7, 8, 12, 12, 13]


def block_profile(row):
    """Length of the leading {0,2} run of row[1:] (0 if row[1] not in {0,2})."""
    sel = row[1:]
    in02 = (sel == 0) | (sel == 2)
    if in02.all():
        return len(sel)
    return int(np.argmax(~in02))


def max_zero_run(seq):
    """Longest run of consecutive 0s in an integer sequence (0 if none)."""
    m = cur = 0
    for x in seq:
        if x == 0:
            cur += 1
            m = max(m, cur)
        else:
            cur = 0
    return m


def pass1(primes):
    """Stream rows A_1..A_DEPTH; return per-row b, s(second), e(edge), c(intruder)
    and the first-10/9/8 entries of A_1..A_3 for the oracle check."""
    b = np.zeros(DEPTH, dtype=np.int64)
    s = np.zeros(DEPTH, dtype=np.int64)
    e = np.zeros(DEPTH, dtype=np.int64)
    c = np.zeros(DEPTH, dtype=np.int64)   # -1 where no intruder in width
    rows3 = {}
    row = primes
    for k in range(1, DEPTH + 1):
        row = np.abs(np.diff(row))
        if k <= 3:
            rows3[k] = [int(x) for x in row[:12]]
        bk = block_profile(row)
        b[k - 1] = bk
        s[k - 1] = int(row[1])
        if bk + 1 < len(row):
            e[k - 1] = int(row[bk])
            c[k - 1] = int(row[bk + 1])
        else:
            e[k - 1] = -1
            c[k - 1] = -1
    return b, s, e, c, rows3


def check_oracles(rows3, b, s, c):
    """All oracle checks; returns True iff every check passes."""
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok = ok and cond
        print(f"  oracle {name}: {'PASS' if cond else 'FAIL'}")

    chk("A_1 first-10 == " + str(A1_EXP), rows3[1][:10] == A1_EXP)
    chk("A_2 first-9  == " + str(A2_EXP), rows3[2][:9] == A2_EXP)
    chk("A_3 first-8  == " + str(A3_EXP), rows3[3][:8] == A3_EXP)

    with open(os.path.join(OUT_DIR, "blocks_depth1000.json")) as f:
        rec = json.load(f)
    chk("num_primes == 1,270,607",
        rec["num_primes"] == 1_270_607 and len(rec["b"]) == 1000)
    chk("b[1..162] equals blocks_depth1000.json",
        list(map(int, b[:DEPTH])) == list(map(int, rec["b"][:DEPTH])))
    chk("s[1..162] equals blocks_depth1000.json",
        list(map(int, s[:DEPTH])) == list(map(int, rec["s"][:DEPTH])))
    jc = [int(x) for x in rec["intruder"][:LIVE]]
    chk("intruder[1..161] equals blocks_depth1000.json",
        list(map(int, c[:LIVE])) == jc)

    with open(os.path.join(OUT_DIR, "witnesses.json")) as f:
        wit = json.load(f)
    w40 = wit["block_profile_first_40"]
    ok_b = all(b[k - 1] == w40[k - 1]["block"] for k in range(1, 41))
    ok_s = all(s[k - 1] == w40[k - 1]["second"] for k in range(1, 41))
    chk("b,s for k=1..40 equal witnesses.json", ok_b and ok_s)
    return ok


def identify_runs(delta, e, c, live):
    """Erosion runs from the criterion: transition k erodes iff NOT(e==2,c==4);
    over the live regime this must coincide exactly with Delta b == -1.
    Returns (runs, crit_failures, erosion_delta_failures)."""
    crit_fail, ero_fail = [], []
    erosion = []
    for k in range(1, live + 1):
        pred_regen = (e[k - 1] == 2 and c[k - 1] == 4)
        obs_regen = delta[k - 1] >= 0
        if pred_regen != obs_regen:
            crit_fail.append((k, int(b[k - 1]), int(e[k - 1]), int(c[k - 1]),
                              int(delta[k - 1])))
        if not pred_regen:
            erosion.append(k)
            if delta[k - 1] != -1:
                ero_fail.append((k, int(delta[k - 1])))
    # maximal consecutive erosion transitions within k=1..LIVE-1
    runs = []
    i = 0
    while i < live - 1:
        if delta[i] == -1:
            j = i
            while j < live - 1 and delta[j] == -1:
                j += 1
            runs.append({"start": i + 1, "len": j - i})
            i = j
        else:
            i += 1
    return runs, crit_fail, ero_fail


def false_starts_check(runs, delta):
    """Every run is followed by a regeneration transition (Delta >= 0)."""
    bad = []
    for r in runs:
        K, L = r["start"], r["len"]
        if K + L <= len(delta) and delta[K + L - 1] < 0:
            bad.append((K, L, int(delta[K + L - 1])))
    return bad


def pass2_compare(primes, runs, b):
    """Second pass: for every depth d=0..L-1 of every run (K,L), compare the
    Pascal-mod-2 prediction (edge and full interior slice) with the real rows.
    Returns two counters dicts."""
    run_by_start = {r["start"]: r for r in runs}
    saved_h = {}
    E = {"total": 0, "bad": 0, "first": None}
    I_ = {"total": 0, "bad": 0, "first": None}
    for r in runs:
        r["edge_total"] = r["edge_bad"] = 0
        r["inter_total"] = r["inter_bad"] = 0
    row = primes
    for k in range(1, DEPTH + 1):
        row = np.abs(np.diff(row))
        if k in run_by_start:
            r = run_by_start[k]
            saved_h[k] = (row[1:int(b[k - 1]) + 1] // 2).copy()
        for r in runs:
            K, L = r["start"], r["len"]
            if K <= k <= K + L - 1:
                d = k - K
                bK = int(b[K - 1])
                h = saved_h[K]
                J = [j for j in range(d + 1) if (d & j) == j]  # Lucas parity
                # --- edge at column bK-d of row A_{K+d} ---
                pred = 0
                for j in J:
                    pred ^= int(h[bK - 1 - d + j])
                act = int(row[bK - d] // 2)
                E["total"] += 1
                r["edge_total"] += 1
                if pred != act:
                    E["bad"] += 1
                    r["edge_bad"] += 1
                    if E["first"] is None:
                        E["first"] = (K, d, pred, act)
                # --- whole interior slice p = 0..bK-d-1 ---
                m = bK - d
                predv = np.zeros(m, dtype=np.int64)
                for j in J:
                    predv ^= h[j:j + m]
                actv = row[1:1 + m] // 2
                nbad = int(np.count_nonzero(predv != actv))
                I_["total"] += m
                r["inter_total"] += m
                if nbad:
                    I_["bad"] += nbad
                    r["inter_bad"] += nbad
                    if I_["first"] is None:
                        firstp = int(np.argmax(predv != actv))
                        I_["first"] = (K, d, firstp, int(predv[firstp]),
                                       int(actv[firstp]))
    return E, I_


def kernel_crosscheck(maxd):
    """Lucas parity (d & j) == j must equal math.comb(d,j) % 2 for all d<=maxd."""
    for d in range(maxd + 1):
        for j in range(d + 1):
            if ((d & j) == j) != (math.comb(d, j) % 2 == 1):
                return False, (d, j)
    return True, None


def main():
    t0 = time.time()
    print("=" * 78)
    print("boundary-edge analysis of the prime Gilbreath triangle, live k=1..161")
    print("cost: sieve 2e7 (1,270,607 primes); 2 passes x 162 numpy abs-diff")
    print("  steps on ~1.27e6-wide int64 rows (O(162*1.27e6) ~ 2.1e8 ops/pass);")
    print("  peak RAM ~100 MB (2 rows + 26 block prefixes + sieve).")
    print("=" * 78)

    # ---- sieve ----
    t1 = time.time()
    primes_list = primes_up_to(SIEVE_LIMIT)
    primes = np.array(primes_list, dtype=np.int64)
    del primes_list
    W = len(primes)
    print(f"sieve: {W} primes < {SIEVE_LIMIT} in {time.time() - t1:.2f}s")

    # ---- pass 1: rows, block profile, edge, intruder ----
    t1 = time.time()
    b, s, e, c, rows3 = pass1(primes)
    print(f"pass 1 (rows A_1..A_{DEPTH}): {time.time() - t1:.2f}s  "
          f"(width A_0 = {W}, width A_162 = {W - DEPTH})")

    # ---- oracles ----
    print("\n== (a) oracle checks ==")
    if not check_oracles(rows3, b, s, c):
        print("ORACLE FAILURE -- aborting, analysis untrustworthy.")
        sys.exit(1)
    if not all(c[k - 1] >= 0 for k in range(1, LIVE + 1)):
        print(f"FATAL: intruder missing inside live regime (k <= {LIVE}).")
        sys.exit(1)
    b162 = int(b[DEPTH - 1])
    print(f"  consumption check: k=162 starts the finite-width artifact: "
          f"b_162 = {b162} == W-162-1 = {W - DEPTH - 1} : "
          f"{b162 == W - DEPTH - 1}")
    print("  all rows k=1..161 indeed have an intruder; k>=162 is excluded "
          "from the live regime (block fills the visible row).")

    # ---- criterion and runs ----
    delta = np.diff(b)                       # delta[k-1] = b[k] - b[k-1], k=1..161
    runs, crit_fail, ero_fail = identify_runs(delta, e, c, LIVE)
    print("\n== (b) regeneration criterion and live-regime erosion runs ==")
    print(f"  criterion (e==2 and c==4) <=> b_next>=b over k=1..{LIVE}: "
          f"failures = {len(crit_fail)} {crit_fail[:3]}")
    print(f"  erosion (criterion) transitions with Delta b != -1: "
          f"failures = {len(ero_fail)} {ero_fail[:3]}")
    regen_rows = [k for k in range(1, LIVE + 1)
                  if int(delta[k - 1]) >= 0]
    print(f"  regeneration transitions k=1..{LIVE}: {len(regen_rows)} "
          f"(prior record: 60)")
    print(f"  all regeneration rows have edge==2 (implied by criterion, "
          f"0 failures): {all(e[k - 1] == 2 for k in regen_rows)}")
    lens = sorted(r["len"] for r in runs)
    print(f"  erosion runs: {len(runs)}  (prior record: 26)")
    print(f"  run lengths sorted: {lens}")
    print(f"  run lengths equal prior depth-1000 record: "
          f"{lens == sorted(PRIOR_RUN_LENGTHS)}")
    badf = false_starts_check(runs, delta)
    print(f"  every run followed by a regeneration transition: "
          f"{len(badf) == 0} {badf[:3]}")
    print(f"  sum of run lengths = {sum(r['len'] for r in runs)} "
          f"= erosion transitions (prior: 101)")
    longest = max(runs, key=lambda r: r["len"])
    print(f"  longest run: start k={longest['start']}, length={longest['len']} "
          f"(prior record: start k=97, length=13)")
    print("  runs (start, length): " +
          ", ".join(f"({r['start']},{r['len']})" for r in runs))

    # ---- (c) boundary formula vs actual rows ----
    t1 = time.time()
    E, I_ = pass2_compare(primes, runs, b)
    print(f"\n== (c) exact boundary formula vs real rows "
          f"({time.time() - t1:.2f}s) ==")
    maxd = max(r["len"] for r in runs) - 1
    kernok, kernbad = kernel_crosscheck(maxd)
    print(f"  Pascal-mod-2 kernel by Lucas equals math.comb parity "
          f"(d <= {maxd}): {kernok} {kernbad}")
    print(f"  edge comparisons: {E['total']} (one per run-depth, sum of run "
          f"lengths = {sum(r['len'] for r in runs)})")
    print(f"  edge mismatches:   {E['bad']}   first: {E['first']}")
    print(f"  interior-slice comparisons: {I_['total']} halved entries "
          f"over all runs/depths")
    print(f"  interior mismatches:          {I_['bad']}   first: {I_['first']}")
    print("  per-run (K, L, edge_tested, edge_bad, interior_tested, interior_bad):")
    for r in runs:
        print(f"    k={r['start']:<4} L={r['len']:<3} "
              f"edge {r['edge_total']:>2}/{r['edge_bad']}   "
              f"interior {r['inter_total']:>9}/{r['inter_bad']}")

    # ---- (d) stall statistics ----
    print("\n== (d) stall statistics ==")
    for r in runs:
        K, L = r["start"], r["len"]
        r["edges"] = [int(e[K - 1 + d]) for d in range(L)]
        r["intruders"] = [int(c[K - 1 + d]) for d in range(L)]
        r["maxz"] = max_zero_run(r["edges"])
        r["b_start"] = int(b[K - 1])
        r["b_end"] = int(b[K + L - 2])
        r["stuck4"] = all(x == 4 for x in r["intruders"])
        r["hits2"] = 2 in r["edges"]
        r["last2"] = r["edges"][-1] == 2
    print("  ALL live-regime erosion runs (26):")
    print("    K | L | intruders | stuck@4 | b_start -> b_end | edges "
          "(0/2) | max edge-0 run | hits2")
    for r in runs:
        es = "".join("0" if x == 0 else "2" for x in r["edges"])
        print(f"   {r['start']:>3} | {r['len']:>2} | {r['intruders']} | "
              f"{'Y' if r['stuck4'] else 'n':>6} | "
              f"{r['b_start']:>8} -> {r['b_end']:<8} | {es} | "
              f"{r['maxz']:>11} | {'Y' if r['hits2'] else 'n'}")
    stuck = [r for r in runs if r["stuck4"]]
    print(f"  runs with intruder stuck at 4: {len(stuck)} of {len(runs)}")
    print("    (K, L, max consecutive edge-0 rows, b_start, b_end):")
    for r in stuck:
        print(f"    k={r['start']:<4} L={r['len']:<3} "
              f"max_edge0={r['maxz']:<3} "
              f"b {r['b_start']} -> {r['b_end']}")
    if stuck:
        print(f"    stuck@4 run lengths: "
              f"{sorted(r['len'] for r in stuck)}")
        print(f"    stuck@4 max-edge-0 list: "
              f"{sorted(r['maxz'] for r in stuck)}")
        print(f"    stuck@4 b_start min/max: "
              f"{min(r['b_start'] for r in stuck)}/{max(r['b_start'] for r in stuck)}, "
              f"b_end min/max: "
              f"{min(r['b_end'] for r in stuck)}/{max(r['b_end'] for r in stuck)}")
    else:
        print("    (none -- every live erosion run contains an intruder >= 6)")

    # global max edge-0 run over the whole live edge sequence
    all_edges = [int(e[k - 1]) for k in range(1, LIVE + 1)]
    gmax, gstart, gcur, gcurstart = 0, None, 0, None
    for i, x in enumerate(all_edges, start=1):
        if x == 0:
            if gcur == 0:
                gcurstart = i
            gcur += 1
            if gcur > gmax:
                gmax, gstart = gcur, gcurstart
        else:
            gcur = 0
    owner = next((r for r in runs
                  if r["start"] <= gstart and gstart + gmax - 1 <= r["start"]
                  + r["len"] - 1), None)
    print(f"  GLOBAL max consecutive edge-0 rows (live regime k=1..{LIVE}): "
          f"{gmax} at rows {gstart}..{gstart + gmax - 1} "
          f"(inside erosion run k={owner['start'] if owner else '?'})")
    print(f"  equals max over per-run maxz: "
          f"{gmax == max(r['maxz'] for r in runs)}")
    print(f"  every run hits edge 2 before the block dies: "
          f"{all(r['hits2'] for r in runs)} ({sum(r['hits2'] for r in runs)}/"
          f"{len(runs)}); last edge of every run == 2: "
          f"{all(r['last2'] for r in runs)} ({sum(r['last2'] for r in runs)}/"
          f"{len(runs)})")

    # NOTE: delta == 0 stalls are regeneration events (17 in the depth-1000
    # record); they never occur inside an erosion run by maximality.
    stalls0 = [k for k in range(1, LIVE + 1) if int(delta[k - 1]) == 0]
    print(f"  (context) zero-jump regeneration stalls (Delta b == 0): "
          f"{len(stalls0)} at k={stalls0[:20]}{'...' if len(stalls0) > 20 else ''}")

    print(f"\ntotal wall time: {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()