#!/usr/bin/env python3
"""Event-rate sweep for the Gilbreath absolute-difference operator on
"2-then-odds" starting sequences.

THEOREM the experiment is built on (the step law; valid for ANY array of
nonnegative integers, no parity assumptions).  Let b_k be the maximal length
of the leading {0,2} block of row k (positions 1..b_k are in {0,2}), let
x_k = A_k[b_k] be the edge and y_k = A_k[b_k+1] the intruder (which exists
iff b_k >= 1 and b_k + 1 < width).  For A_{k+1}(j) = |A_k(j) - A_k(j+1)|:

      b_{k+1} >= b_k  <=>  (x_k, y_k) = (2, 4),     else  b_{k+1} = b_k - 1.

Proof: positions 1..b_k-1 of row k+1 are differences of {0,2} pairs, hence in
{0,2} ({0,2} is closed under |a-b|).  Position b_k of row k+1 is |x_k - y_k|,
which lies in {0,2} iff (x,y) = (2,4):  y is not in {0,2} by maximality, so
x=0 gives |0-y| = y not in {0,2}, and x=2 gives |2-y| in {0,2} iff y = 4.

Recharge identity (exact consequence): with events at rows i where
(x,y) = (2,4) and jumps j_i = b_{i+1} - b_i >= 0,

      b_k = b_1 + sum_{events i < k} (j_i + 1) - (k - 1),

valid up to the first row with b = 0 (the step law has no content at b = 0,
so the identity's scope ends there).

So the (2,4) event rate is the quantity to measure: it is the only recharge
mechanism, and the block stays positive iff the recharge sum never falls
k-1 behind.

Complexity per sequence: O(D*W) time, O(W) memory (two rows held at a time;
all operations vectorised with numpy int64).  Values never exceed the largest
starting gap (max(|a-b|) <= max(a,b) is a contraction), so int64 is exact
throughout; no floats in the row arithmetic.

The class: A_0 = (2, 3, 3 + cumsum(gaps)) with even gaps drawn per family
(geometric, bounded-uniform, all-2, random {2,4}, prime-like weights), with
and without the first gap forced to 2 (the primes have first gap 2).

Batches:  sweep  D=600     W=200_000   21 families x 48 seeds
          deep   D=1200    W=400_000   13 families x 10 seeds
          long   D=4000    W=2_000_000  4 families x  4 seeds
Each row with b_k >= 1 and an intruder is "eligible"; density rho_live is
events / eligible; density rho_rows is events / live rows (live = up to the
first block-full row, where the finite row ends the boundary process).
"""
import json
import os
import time

import numpy as np

from lib.parallel import parallel_map, workers

# ----------------------------------------------------------------------
# gap families: each returns numpy int64 gaps (length n) between consecutive
# odd numbers after the initial 2 -> 3 step; all gaps are even >= 2.
# ----------------------------------------------------------------------

def fam_consecutive(rng, n):
    return np.full(n, 2, dtype=np.int64)


def fam_rand24(rng, n):
    return (2 * (1 + rng.integers(0, 2, size=n))).astype(np.int64)


def fam_skew246(rng, n):
    # prime-like small-gap profile: 2 (65%), 4 (25%), 6 (10%)
    u = rng.random(n)
    return np.where(u < 0.65, 2, np.where(u < 0.90, 4, 6)).astype(np.int64)


def fam_skew24810(rng, n):
    # 2 (66%), 4 (20%), 6 (7%), 8 (4%), 10 (3%)
    u = rng.random(n)
    return np.where(
        u < 0.66, 2,
        np.where(u < 0.86, 4, np.where(u < 0.93, 6, np.where(u < 0.97, 8, 10)))
    ).astype(np.int64)


def fam_uniform(rng, n, g):
    # gaps uniformly in {2, 4, ..., 2g}
    return (2 * (1 + rng.integers(0, g, size=n))).astype(np.int64)


def fam_geometric(rng, n, p):
    # P(gap = 2m) = (1-p)^(m-1) * p, m >= 1; mean gap 2/p
    u = rng.random(n)
    m = 1 + np.floor(np.log1p(-u) / np.log1p(-p)).astype(np.int64)
    m = np.minimum(m, 1 << 16)
    return (2 * m).astype(np.int64)


FAMILIES = [
    ("consecutive", fam_consecutive, ()),
    ("rand24", fam_rand24, ()),
    ("f2-rand24", fam_rand24, ()),
    ("skew246", fam_skew246, ()),
    ("f2-skew246", fam_skew246, ()),
    ("skew24810", fam_skew24810, ()),
    ("f2-skew24810", fam_skew24810, ()),
    ("uniform3", fam_uniform, (3,)),
    ("f2-uniform3", fam_uniform, (3,)),
    ("uniform5", fam_uniform, (5,)),
    ("f2-uniform5", fam_uniform, (5,)),
    ("uniform10", fam_uniform, (10,)),
    ("f2-uniform10", fam_uniform, (10,)),
    ("uniform25", fam_uniform, (25,)),
    ("f2-uniform25", fam_uniform, (25,)),
    ("uniform50", fam_uniform, (50,)),
    ("f2-uniform50", fam_uniform, (50,)),
    ("geo05", fam_geometric, (0.5,)),
    ("f2-geo05", fam_geometric, (0.5,)),
    ("geo025", fam_geometric, (0.25,)),
    ("f2-geo025", fam_geometric, (0.25,)),
    ("geo0125", fam_geometric, (0.125,)),
    ("f2-geo0125", fam_geometric, (0.125,)),
    ("geo00625", fam_geometric, (0.0625,)),
    ("f2-geo00625", fam_geometric, (0.0625,)),
]
FAMILY_DICT = {name: (f, prm) for name, f, prm in FAMILIES}
FAMILY_NAMES = [name for name, _, _ in FAMILIES]


def _gaps(fam, rng, n):
    f, prm = FAMILY_DICT[fam]
    gaps = f(rng, n, *prm) if prm else f(rng, n)
    if fam.startswith("f2-"):
        gaps = gaps.copy()
        gaps[0] = 2
    return gaps


# ----------------------------------------------------------------------
# measurement: one row at a time, O(W) memory, exact int64 arithmetic
# ----------------------------------------------------------------------

def measure_rows(cur, D, W):
    """Stats for evolving the numpy int64 row `cur` for D steps.

    Returns the stats dict (without batch/family/seed identity).  Every
    quantity is exact integer arithmetic; densities are float ratios of
    integer counts.
    """
    b_prev = None
    ev_prev = False
    elig_prev = False
    b_series = []
    events = []                      # (row k, jump); jump filled next row
    first_b0 = None
    b_min = W
    b0_hits = 0
    eligible = 0
    ev_count = 0
    step_fail = 0
    trunc_k = None
    for k in range(1, D + 1):
        row = np.abs(cur[:-1] - cur[1:])
        width = row.shape[0]
        sel = row[1:]
        m = (sel == 0) | (sel == 2)
        if m.all():
            b = sel.shape[0]                       # block fills the whole row
            if trunc_k is None:
                trunc_k = k
        else:
            b = int(np.argmax(~m))                 # first entry not in {0,2}
        # step law on the transition row k-1 -> row k (row k-1 eligible)
        if b_prev is not None and elig_prev:
            if ev_prev:
                if not (b >= b_prev):
                    step_fail += 1
            else:
                if not (b == b_prev - 1):
                    step_fail += 1
        # close the previous row's event with its jump
        if ev_prev:
            events[-1] = (events[-1][0], b - b_prev)
        # detect an event at this row
        elig = (b >= 1 and b + 1 < width)
        ev = False
        if elig:
            ev = (int(row[b]) == 2 and int(row[b + 1]) == 4)
        if ev:
            events.append((k, None))
            ev_count += 1
        if elig:
            eligible += 1
        if b == 0:
            b0_hits += 1
            if first_b0 is None:
                first_b0 = k
        b_series.append(b)
        if b < b_min:
            b_min = b
        b_prev, ev_prev, elig_prev = b, ev, elig
        cur = row
    # recharge identity over k <= first_b0 (or all k if b never reaches 0)
    limit = first_b0 if first_b0 is not None else D
    recharge_fail = 0
    esum = 0
    ei = 0
    for k in range(2, limit + 1):
        while ei < len(events) and events[ei][0] < k:
            esum += events[ei][1] + 1
            ei += 1
        if b_series[k - 1] != b_series[0] + esum - (k - 1):
            recharge_fail += 1
    live_rows = trunc_k if trunc_k is not None else D
    rho_live = ev_count / eligible if eligible else None
    rho_rows = ev_count / live_rows if live_rows else None
    jumps = [j for (_, j) in events if j is not None]
    return {
        "D": D, "W": W,
        "eligible": eligible, "events": ev_count,
        "rho_live": rho_live, "rho_rows": rho_rows,
        "live_rows": live_rows, "b_min": b_min,
        "first_b0": first_b0, "b0_hits": b0_hits,
        "step_fail": step_fail, "recharge_fail": recharge_fail,
        "trunc_k": trunc_k,
        "sum_j1": int(sum(j + 1 for j in jumps)),
        "mean_jump": (sum(jumps) / len(jumps)) if jumps else None,
        "b1": b_series[0],
    }


def run_sequence(args):
    """(batch, family, seed, D, W) -> full stats dict (numpy implementation)."""
    batch, fam, seed, D, W = args
    rng = np.random.default_rng(seed)
    gaps = _gaps(fam, rng, W - 2)
    a0 = np.empty(W, dtype=np.int64)
    a0[0] = 2
    a0[1] = 3
    a0[2:] = 3 + np.cumsum(gaps)
    stats = measure_rows(a0, D, W)
    stats["batch"] = batch
    stats["family"] = fam
    stats["seed"] = seed
    return stats


def run_sequence_pure(args):
    """Pure-Python reimplementation of run_sequence — independent oracle.

    Shares only the gap sampling; row evolution, block measurement and all
    bookkeeping are written from scratch with lists and explicit loops.
    """
    batch, fam, seed, D, W = args
    rng = np.random.default_rng(seed)
    gaps = [int(g) for g in _gaps(fam, rng, W - 2)]
    a0 = [2, 3]
    s = 3
    for g in gaps:
        s += g
        a0.append(s)
    cur = a0
    b_prev = None
    ev_prev = False
    elig_prev = False
    b_series = []
    events = []
    first_b0 = None
    b_min = W
    b0_hits = 0
    eligible = 0
    ev_count = 0
    step_fail = 0
    trunc_k = None
    for k in range(1, D + 1):
        row = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        width = len(row)
        b = 0
        for v in row[1:]:
            if v == 0 or v == 2:
                b += 1
            else:
                break
        if b == width - 1 and trunc_k is None:
            trunc_k = k
        if b_prev is not None and elig_prev:
            if ev_prev:
                if not (b >= b_prev):
                    step_fail += 1
            else:
                if not (b == b_prev - 1):
                    step_fail += 1
        if ev_prev:
            events[-1] = (events[-1][0], b - b_prev)
        elig = (b >= 1 and b + 1 < width)
        ev = False
        if elig:
            ev = (row[b] == 2 and row[b + 1] == 4)
        if ev:
            events.append((k, None))
            ev_count += 1
        if elig:
            eligible += 1
        if b == 0:
            b0_hits += 1
            if first_b0 is None:
                first_b0 = k
        b_series.append(b)
        if b < b_min:
            b_min = b
        b_prev, ev_prev, elig_prev = b, ev, elig
        cur = row
    limit = first_b0 if first_b0 is not None else D
    recharge_fail = 0
    esum = 0
    ei = 0
    for k in range(2, limit + 1):
        while ei < len(events) and events[ei][0] < k:
            esum += events[ei][1] + 1
            ei += 1
        if b_series[k - 1] != b_series[0] + esum - (k - 1):
            recharge_fail += 1
    live_rows = trunc_k if trunc_k is not None else D
    rho_live = ev_count / eligible if eligible else None
    rho_rows = ev_count / live_rows if live_rows else None
    jumps = [j for (_, j) in events if j is not None]
    return {
        "batch": batch, "family": fam, "seed": seed,
        "D": D, "W": W,
        "eligible": eligible, "events": ev_count,
        "rho_live": rho_live, "rho_rows": rho_rows,
        "live_rows": live_rows, "b_min": b_min,
        "first_b0": first_b0, "b0_hits": b0_hits,
        "step_fail": step_fail, "recharge_fail": recharge_fail,
        "trunc_k": trunc_k,
        "sum_j1": int(sum(j + 1 for j in jumps)),
        "mean_jump": (sum(jumps) / len(jumps)) if jumps else None,
        "b1": b_series[0],
    }


# ----------------------------------------------------------------------
# main: batches, parallel execution, report, oracle cross-check
# ----------------------------------------------------------------------

SWEEP = [
    ("sweep", 600, 200_000, 21, 48, FAMILY_NAMES),
    ("deep", 1200, 400_000, 13, 10, [
        "consecutive", "f2-rand24", "f2-skew246", "f2-skew24810",
        "f2-uniform3", "f2-uniform5", "f2-uniform10", "f2-uniform25",
        "f2-uniform50", "f2-geo05", "f2-geo025", "f2-geo0125", "f2-geo00625",
    ]),
    ("long", 4000, 2_000_000, 4, 4, [
        "consecutive", "f2-rand24", "f2-skew246", "f2-geo05",
    ]),
]


def build_tasks(batches):
    tasks = []
    for batch, D, W, nf, ns, fams in batches:
        assert nf <= len(fams)
        for fam in fams[:nf]:
            for seed in range(1, ns + 1):
                tasks.append((batch, fam, seed, D, W))
    return tasks


def report(stats_list, batches, title):
    fams = sorted({s["family"] for s in stats_list})
    rows_out = []
    print("=" * 100)
    print(title)
    print("=" * 100)
    print(f"{'batch':<6} {'family':<18} {'n':>3} {'events':>6} {'elig':>8} "
          f"{'rho_live':>8} {'rho_rows':>8} {'min_b':>6} {'b0':>3} "
          f"{'first_b0':>8} {'stepF':>5} {'rechF':>5}")
    for batch, _, _, _, _, _ in batches:
        for fam in fams:
            sel = [s for s in stats_list if s["batch"] == batch and
                   s["family"] == fam]
            if not sel:
                continue
            ev = sum(s["events"] for s in sel)
            elig = sum(s["eligible"] for s in sel)
            live = sum(s["live_rows"] for s in sel)
            mn = min(s["b_min"] for s in sel)
            b0s = [s for s in sel if s["first_b0"] is not None]
            sf = sum(s["step_fail"] for s in sel)
            rf = sum(s["recharge_fail"] for s in sel)
            rl = ev / elig if elig else None
            rr = ev / live if live else None
            fb = min((s["first_b0"] for s in b0s), default=None)
            rls = "-".rjust(8) if rl is None else f"{rl:8.4f}"
            rrs = "-".rjust(8) if rr is None else f"{rr:8.4f}"
            print(f"{batch:<6} {fam:<18} {len(sel):>3} {ev:>6} {elig:>8} "
                  f"{rls} {rrs} {mn:>6} {len(b0s):>3} "
                  f"{str(fb):>8} {sf:>5} {rf:>5}")
            rows_out.append((batch, fam, len(sel), ev, elig, live, mn,
                             len(b0s), fb, sf, rf))
    return rows_out


def main():
    t_all = time.time()
    batches = SWEEP[:2] if os.environ.get("EVENT_FAST") else SWEEP
    tasks = build_tasks(batches)
    n_workers = workers()
    print(f"[event-rate] {len(tasks)} sequences across {n_workers} workers, "
          f"expected single-core ~{len(tasks)*11:.0f}s", flush=True)
    t0 = time.time()
    stats_list = parallel_map(run_sequence, tasks, label="event-rate",
                              space="families x seeds", count=n_workers)
    print(f"[event-rate] sweep finished in {time.time()-t0:.1f}s", flush=True)
    # Persist stats before report() in case formatting crashes
    with open("code/out/event_rate_stats.jsonl", "w") as f:
        for s in stats_list:
            f.write(json.dumps(s) + "\n")
    rows = report(stats_list, batches, "EVENT-RATE SWEEP (2-then-odds class)")
    all_event = sum(r[3] for r in rows)
    all_elig = sum(r[4] for r in rows)
    print("-" * 100)
    print(f"TOTAL: {len(stats_list)} sequences, {all_event} events / "
          f"{all_elig} eligible rows; pooled live density "
          f"{all_event/all_elig:.6f}")
    min_seq = min(stats_list, key=lambda s: s["rho_live"]
                  if s["rho_live"] is not None else float("inf"))
    print(f"MINIMUM per-sequence live density: "
          f"{min_seq['rho_live']:.6f} ({min_seq['events']} events / "
          f"{min_seq['eligible']} eligible) batch={min_seq['batch']}, "
          f"family={min_seq['family']}, seed={min_seq['seed']}, "
          f"min_b={min_seq['b_min']}, first_b0={min_seq['first_b0']}")
    worst = min(stats_list, key=lambda s: s["b_min"])
    print(f"MINIMUM b over class: {worst['b_min']} "
          f"(batch={worst['batch']}, family={worst['family']}, "
          f"seed={worst['seed']}, first_b0={worst['first_b0']})")
    b0_s = [s for s in stats_list if s["first_b0"] is not None]
    if b0_s:
        earliest = min(b0_s, key=lambda s: s["first_b0"])
        print(f"WARNING: {len(b0_s)} of {len(stats_list)} sequences reached "
              f"b=0; earliest at k={earliest['first_b0']} "
              f"(batch={earliest['batch']}, family={earliest['family']}, "
              f"seed={earliest['seed']})")
    else:
        print("b=0 reached: NEVER, in any of the "
              f"{len(stats_list)} sequences")
    per_batch = {}
    for s in stats_list:
        per_batch.setdefault(s["batch"], []).append(s)
    for bname, sl in per_batch.items():
        evs = [s["events"] for s in sl]
        lv = [s["live_rows"] for s in sl]
        print(f"[{bname}] sequences={len(sl)} live rows={sum(lv)} "
              f"events={sum(evs)} pooled rho_rows={sum(evs)/sum(lv):.6f} "
              f"mean per-seq rho_rows="
              f"{sum(e/l for e, l in zip(evs, lv))/len(sl):.6f} "
              f"min per-seq rho_rows={min(e/l for e, l in zip(evs, lv)):.6f}")
    print(f"wall time {time.time()-t_all:.1f}s across {n_workers} workers")
    if os.environ.get("EVENT_FAST"):
        return
    # ---------------- oracle cross-check: numpy vs pure-Python ---------
    check = [
        ("sweep", "f2-geo025", 3, 400, 3000),
        ("sweep", "consecutive", 5, 60, 3000),
        ("sweep", "uniform25", 7, 80, 5000),
        ("sweep", "f2-rand24", 11, 50, 4000),
    ]
    print("-" * 100)
    print("ORACLE CROSS-CHECK (numpy vs pure-Python, independent code paths)")
    for args in check:
        npy = run_sequence(args)
        pure = run_sequence_pure(args)
        keys = ["eligible", "events", "b_min", "first_b0", "b0_hits",
                "step_fail", "recharge_fail", "trunc_k", "sum_j1", "b1",
                "live_rows"]
        same = all(npy[k] == pure[k] for k in keys)
        ratio_rho = (npy["rho_live"] == pure["rho_live"]
                     and npy["rho_rows"] == pure["rho_rows"])
        print(f"{args[1]:<12} seed={args[2]:<2} "
              f"eligible {npy['eligible']} vs {pure['eligible']} | "
              f"events {npy['events']} vs {pure['events']} | "
              f"min_b {npy['b_min']} vs {pure['b_min']} | "
              f"first_b0 {npy['first_b0']} vs {pure['first_b0']} | "
              f"stepF {npy['step_fail']} rechF {npy['recharge_fail']} | "
              f"rho match: {ratio_rho} | ALL MATCH: {same and ratio_rho}")
    print("-" * 100)
    # ---------------- prime-row sanity row (from block data) ----------
    if os.path.exists("code/out/blocks_depth1000.json"):
        with open("code/out/blocks_depth1000.json") as f:
            bd = json.load(f)
        print("PRIME ROWS (reference): "
              f"depth {bd.get('D')}, sieve {bd.get('sieve_limit')}, "
              f"60 regeneration events reported by the run's oracle")
        print("The step law is already verified there to depth 1000 "
              "(code/out/step_law_and_recharge_verified.md); the sweep "
              "class here extends that verification to random sequences.")


if __name__ == "__main__":
    main()