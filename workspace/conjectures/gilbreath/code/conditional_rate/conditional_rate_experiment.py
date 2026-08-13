#!/usr/bin/env python3
"""Conditional-rate experiment: isolate the asymptotic (k>10) (2,4)-event rate
from the g_0 startup transient in the 2-then-odds Gilbreath class.

This is TASKS.md item 1 (Directive 16), the single blocking task.  It answers:
is the post-startup regeneration rate combinatorial (Route A, family-
independent) or input-dependent (Route B, family-dependent)?

THEOREM the experiment rests on (the step law, valid for ANY array of
nonnegative integers).  Let b_k be the maximal length of the leading {0,2}
block of row k (positions 1..b_k are in {0,2}), x_k = A_k[b_k] the edge and
y_k = A_k[b_k+1] the intruder (exists iff b_k >= 1 and b_k+1 < width):

      b_{k+1} >= b_k  <=>  (x_k, y_k) = (2, 4),     else  b_{k+1} = b_k - 1.

So a "regeneration event" at row k is exactly (A_k[b_k]==2 and A_k[b_k+1]==4)
on an eligible row, and the event rate is the ONLY recharge mechanism.  The
question is whether that rate, measured conditional on survival past row 10
(which the sweep showed kills 100% of startup deaths: no sequence surviving
row 10 died up to D=4000), is the same across gap families.

Null hypothesis (Route A): the post-10 event rate is a combinatorial constant
lambda_hat shared by all families; departures are sampling noise.  Test:
Pearson homogeneity X^2 = sum_f (E_f - lambda_hat * R_f)^2 / (lambda_hat * R_f)
with pooled lambda_hat = sum E_f / sum R_f, df = n_families - 1, p-value from
scipy.stats.chi2.  Small p -> rates differ -> Route B (family-dependent).

Also reported: per-sequence mean +/- sd of rho_post10 (the complement needed
because with huge R_f even tiny family differences make X^2 significant),
the inter-event row-gap distribution at k>=11, an overdispersion diagnostic
(var/mean of per-sequence event counts; ~1 under a single Poisson law),
and the prime reference run with the same machinery.

Complexity per sequence: O(D*W) time, O(W) memory (one row at a time, numpy
int64, exact — values never exceed the largest starting gap, so int64 is
exact throughout; no floats in row arithmetic).  The 20-seed x 11-family run
is ~200-250 s single-core, under 2 min across 26 workers; the pure-Python
oracle cross-check (2 pairs, Part 3) is the only serial heavy part (~2 min).

Parts:
  0. oracle: sieve primes, generate rows A_1..A_5, assert equality with the
     problem.md table exactly; print PASS/FAIL.
  1. sniff code/out/event_rate_stats.jsonl: per-row event positions present?
     (No: only aggregates -> print the fallback string -> run Part 2 fresh.)
  2. new run: every stored family with >=5 survivors x 20 fresh seeds
     (seed=10000+i), D=400, W=200000, parallel via lib.parallel.  Per-sequence
     events/eligible split k<=10 vs k>=11, event row positions, first_b0.
     Condition on survival past row 10; per-family pooled rho_post10 and
     per-sequence mean+/-sd; Pearson X^2; inter-event gaps pooled + per family.
  3. oracle cross-check: numpy vs pure-Python on 2 (family, seed) pairs;
     events_post, elig_post, first_b0 must match.
  Then the prime reference: same machinery, sieve 2e6 (D=161) and sieve 2e7
  (D=161, verifies the recorded 60 events / 161 live rows = 0.373).
"""
import json
import os
import time

import numpy as np
from scipy.stats import chi2

from lib.gilbreath import primes_up_to, rows_generator
from lib.parallel import parallel_map, workers

# gap families reused from the sweep (single source of truth for sampling)
import event_rate.event_rate_sweep as SWEEP

STORED = "code/out/event_rate_stats.jsonl"
RECORDS = "code/out/conditional_rate_records.jsonl"

# problem.md worked rows, exactly as given in the task instruction
EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4],
    3: [1, 2, 0, 0, 0, 0, 0, 2],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2],
}


def part0_oracle():
    """Sieve primes < 60, generate A_1..A_5, compare with problem.md exactly."""
    primes = primes_up_to(60)
    gen = rows_generator(primes, 5)
    next(gen)                      # A_0
    rows = [next(gen) for _ in range(5)]
    ok = True
    print("=" * 100)
    print("PART 0  ORACLE: prime rows A_1..A_5 vs problem.md table")
    print("=" * 100)
    for k in range(1, 6):
        got = [int(v) for v in rows[k - 1][:10]]
        match = got == EXPECTED[k]
        ok = ok and match
        print(f"  A_{k} = {got}  match={match}")
    print(f"  {'PASS' if ok else 'FAIL'}")


def stored_survivor_families(path=STORED, min_surv=5):
    """Count stored sequences with first_b0 None per family; keep >= min."""
    counts = {}
    with open(path) as f:
        for line in f:
            s = json.loads(line)
            if s["first_b0"] is None:
                counts[s["family"]] = counts.get(s["family"], 0) + 1
    return {fam: n for fam, n in sorted(counts.items()) if n >= min_surv}


def part1_sniff(path=STORED):
    """If the stored JSONL has per-row event positions, condition on them;
    else print the fallback string and let Part 2 run fresh."""
    print("=" * 100)
    print("PART 1  SNIFF code/out/event_rate_stats.jsonl keys")
    print("=" * 100)
    with open(path) as f:
        first = json.loads(f.readline())
    keys = sorted(first.keys())
    print(f"  keys: {keys}")
    per_row = [k for k in keys if "pos" in k or "event_rows" in k
               or "per_row" in k or "events_at" in k]
    if per_row:
        print(f"  per-row event positions present: {per_row} -> "
              "computing conditional stats from stored data")
        return True
    print("  per-row event positions present: none")
    print("  stored aggregates not conditionable on k>10")
    # context: unconditional survivor rates from stored data, for reference
    fam_rates = {}
    n_lines = 0
    with open(path) as f:
        for line in f:
            s = json.loads(line)
            n_lines += 1
            if s["first_b0"] is None and s["eligible"]:
                r = fam_rates.setdefault(s["family"], [0, 0])
                r[0] += s["events"]
                r[1] += s["eligible"]
    print("  stored survivor rates (unconditional, all rows):")
    for fam in sorted(fam_rates):
        e, el = fam_rates[fam]
        print(f"    {fam:<16} {e:>5} events / {el:>6} eligible "
              f"= {e/el:.4f}")
    print(f"  ({n_lines} stored sequences total)")
    return False


# ----------------------------------------------------------------------
# measurement: one row at a time, O(W) memory, exact int64
# ----------------------------------------------------------------------

def measure_conditional(cur, D):
    """Evolve numpy int64 row `cur` for D steps; record per-row events.

    Returns a dict carrying events_pos (row indices k>=1 where the (2,4)
    event fired), elig_rows, splits k<=10 vs k>=11, first_b0, trunc_k.
    """
    events_pos = []
    elig_rows = []
    first_b0 = None
    trunc_k = None
    b_series = []
    for k in range(1, D + 1):
        row = np.abs(cur[:-1] - cur[1:])
        width = row.shape[0]
        sel = row[1:]
        m = (sel == 0) | (sel == 2)
        if m.all():
            b = sel.shape[0]
            if trunc_k is None:
                trunc_k = k
        else:
            b = int(np.argmax(~m))
        b_series.append(b)
        elig = (b >= 1 and b + 1 < width)
        if elig:
            elig_rows.append(k)
            if row[b] == 2 and row[b + 1] == 4:
                events_pos.append(k)
        if b == 0 and first_b0 is None:
            first_b0 = k
        cur = row
    return {
        "D": D,
        "first_b0": first_b0,
        "trunc_k": trunc_k,
        "events_le10": sum(1 for k in events_pos if k <= 10),
        "elig_le10": sum(1 for k in elig_rows if k <= 10),
        "events_post": sum(1 for k in events_pos if k >= 11),
        "elig_post": sum(1 for k in elig_rows if k >= 11),
        "events_pos": events_pos,
        "elig_rows_le10": [k for k in elig_rows if k <= 10],
        "b_min": min(b_series),
        "b1": b_series[0],
    }


def make_a0(fam, seed, W):
    rng = np.random.default_rng(seed)
    gaps = SWEEP._gaps(fam, rng, W - 2)
    a0 = np.empty(W, dtype=np.int64)
    a0[0] = 2
    a0[1] = 3
    a0[2:] = 3 + np.cumsum(gaps)
    return a0


def run_seq_conditional(args):
    """(family, seed) with module-level D, W -> measured record (numpy)."""
    fam, seed = args
    a0 = make_a0(fam, seed, RUN_W)
    m = measure_conditional(a0, RUN_D)
    m.update(family=fam, seed=seed, W=RUN_W)
    return m


def run_seq_conditional_pure(args):
    """Pure-Python reimplementation of run_seq_conditional (oracle)."""
    fam, seed = args
    rng = np.random.default_rng(seed)
    gaps = [int(g) for g in SWEEP._gaps(fam, rng, RUN_W - 2)]
    a0 = [2, 3]
    s = 3
    for g in gaps:
        s += g
        a0.append(s)
    cur = a0
    events_pos = []
    elig_rows = []
    first_b0 = None
    trunc_k = None
    b_series = []
    for k in range(1, RUN_D + 1):
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
        b_series.append(b)
        elig = (b >= 1 and b + 1 < width)
        if elig:
            elig_rows.append(k)
            if row[b] == 2 and row[b + 1] == 4:
                events_pos.append(k)
        if b == 0 and first_b0 is None:
            first_b0 = k
        cur = row
    return {
        "family": fam, "seed": seed, "D": RUN_D, "W": RUN_W,
        "first_b0": first_b0, "trunc_k": trunc_k,
        "events_le10": sum(1 for k in events_pos if k <= 10),
        "elig_le10": sum(1 for k in elig_rows if k <= 10),
        "events_post": sum(1 for k in events_pos if k >= 11),
        "elig_post": sum(1 for k in elig_rows if k >= 11),
        "events_pos": events_pos,
        "elig_rows_le10": [k for k in elig_rows if k <= 10],
        "b_min": min(b_series),
        "b1": b_series[0],
    }


# ----------------------------------------------------------------------
# analysis
# ----------------------------------------------------------------------

def inter_event_gaps(records):
    """Row gaps between consecutive events at k>=11, one list per sequence."""
    gaps = []
    for r in records:
        p = [k for k in r["events_pos"] if k >= 11]
        gaps.extend(b - a for a, b in zip(p, p[1:]))
    return gaps


def gap_stats(gaps, label):
    if not gaps:
        print(f"    {label:<16} n/a (fewer than 2 post-10 events)")
        return
    gaps = sorted(gaps)
    med = gaps[len(gaps) // 2]
    mean = sum(gaps) / len(gaps)
    print(f"    {label:<16} n={len(gaps):>4} mean={mean:8.2f} "
          f"median={med:>4} max={gaps[-1]:>5}")


def part2_run(fams):
    print("=" * 100)
    print(f"PART 2  FRESH RUN: families with >=5 stored survivors, "
          f"20 seeds each, D={RUN_D}, W={RUN_W}")
    print("=" * 100)
    print("  families used (stored survivor counts):")
    for fam, n in fams.items():
        print(f"    {fam:<16} {n:>3}")
    print(f"  seeds: 10000..10019  (seed = 10000 + i)")
    tasks = [(fam, seed) for fam in sorted(fams) for seed
             in range(10000, 10020)]
    n_workers = workers()
    est = len(tasks) * 7.0 / n_workers
    print(f"  {len(tasks)} sequences, {n_workers} workers, "
          f"~7 s/seq single-core -> ~{est:.0f} s wall (2 min budget)", flush=True)
    t0 = time.time()
    results = parallel_map(run_seq_conditional, tasks,
                           label="conditional-rate", space="families x seeds",
                           count=n_workers)
    print(f"  run finished in {time.time() - t0:.1f}s", flush=True)
    with open(RECORDS, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    return results


def part2_report(results):
    print("-" * 100)
    print("PART 2 REPORT  (conditioned on survival past row 10: "
          "first_b0 is None or first_b0 > 10)")
    print("-" * 100)
    cond = [r for r in results if r["first_b0"] is None or r["first_b0"] > 10]
    dead_late = [r for r in results if r["first_b0"] is not None
                 and r["first_b0"] > 10]
    surv_full = [r for r in results if r["first_b0"] is None]
    n_startup_dead = len(results) - len(cond)
    print(f"  total seeds: {len(results)} | survived row 10: {len(cond)} "
          f"| died k<=10: {n_startup_dead} | died k>10: {len(dead_late)} "
          f"| survived full D={RUN_D}: {len(surv_full)}")
    if dead_late:
        print("  late deaths (first_b0 in 11..D): "
              + ", ".join(f"{r['family']}@{r['seed']}:k={r['first_b0']}"
                          for r in dead_late))
    if n_startup_dead:
        print("  startup deaths (k<=10) per family: ", end="")
        from collections import Counter
        print(dict(Counter(r["family"] for r in results
                           if r["first_b0"] is not None
                           and r["first_b0"] <= 10)))

    fams = sorted({r["family"] for r in cond})
    print()
    print(f"  {'family':<16} {'n':>3} {'ev_post':>7} {'elig_post':>9} "
          f"{'rho_post10':>9} {'mean per-seq':>13} {'min-max':>13}")
    rows = []
    for fam in fams:
        sel = [r for r in cond if r["family"] == fam]
        E = sum(r["events_post"] for r in sel)
        R = sum(r["elig_post"] for r in sel)
        rates = [r["events_post"] / r["elig_post"] for r in sel
                 if r["elig_post"] > 0]
        rho = E / R if R else None
        if rates:
            mean = sum(rates) / len(rates)
            sd = (sum((x - mean) ** 2 for x in rates) / len(rates)) ** 0.5
            mns = f"{mean:.4f} +/- {sd:.4f}"
            mm = f"{min(rates):.4f}..{max(rates):.4f}"
        else:
            mns = "n/a"
            mm = "n/a"
        rs = "-" if rho is None else f"{rho:.6f}"
        print(f"  {fam:<16} {len(sel):>3} {E:>7} {R:>9} {rs:>9} "
              f"{mns:>13} {mm:>13}")
        rows.append((fam, len(sel), E, R))
    # demanded Pearson homogeneity test on families with elig_post > 0
    tot_E = sum(r[2] for r in rows)
    tot_R = sum(r[3] for r in rows)
    lam = tot_E / tot_R if tot_R else None
    usable = [r for r in rows if r[3] > 0]
    print()
    print(f"  POOLED lambda_hat = {tot_E} / {tot_R} = "
          f"{lam:.6f}  (families with elig_post>0: {len(usable)})")
    x2 = 0.0
    for fam, n, E, R in usable:
        exp = lam * R
        x2 += (E - exp) ** 2 / exp
        print(f"    {fam:<16} observed {E:>6}  expected {exp:8.2f}  "
              f"contrib {(E-exp)**2/exp:8.2f}")
    df = len(usable) - 1
    p = chi2.sf(x2, df)
    print(f"  Pearson X^2 = {x2:.3f}, df = {df}, "
          f"p = {p:.3e}  (scipy chi2 survival)")
    # overdispersion diagnostic on per-sequence post-10 event counts
    ev = [r["events_post"] for r in cond if r["elig_post"] > 0]
    if len(ev) > 1:
        m = sum(ev) / len(ev)
        var = sum((x - m) ** 2 for x in ev) / (len(ev) - 1)
        print(f"  overdispersion check: per-sequence events_post "
              f"var/mean = {var/m:.2f} (~1 under one Poisson law)")
    # inter-event row-gap distribution at k>=11
    print()
    print("  inter-event row-gap distribution at k>=11 "
          "(pooled + per family):")
    pooled = inter_event_gaps(cond)
    gap_stats(pooled, "pooled")
    for fam in fams:
        sel = [r for r in cond if r["family"] == fam]
        gap_stats(inter_event_gaps(sel), fam)
    print()
    print(f"  verdict: p = {p:.3e} -> "
          + ("family-dependent (Route B)" if p < 0.05
             else "family-independent (Route A, combinatorial)"))
    return p, lam, rows


def part3_crosscheck():
    print("=" * 100)
    print("PART 3  ORACLE CROSS-CHECK (numpy vs pure-Python, 2 pairs, "
          f"D={RUN_D}, W={RUN_W})")
    print("=" * 100)
    pairs = [("f2-skew246", 10007), ("geo05", 10003)]
    all_ok = True
    for fam, seed in pairs:
        npy = run_seq_conditional((fam, seed))
        pure = run_seq_conditional_pure((fam, seed))
        keys = ["events_post", "elig_post", "first_b0", "events_pos",
                "elig_le10", "events_le10", "trunc_k", "b_min", "b1"]
        ok = all(npy[k] == pure[k] for k in keys)
        all_ok = all_ok and ok
        print(f"  {fam:<12} seed={seed}: events_post {npy['events_post']} vs "
              f"{pure['events_post']} | elig_post {npy['elig_post']} vs "
              f"{pure['elig_post']} | first_b0 {npy['first_b0']} vs "
              f"{pure['first_b0']} | pos {npy['events_pos']} vs "
              f"{pure['events_pos']} | MATCH: {ok}")
    print(f"  {'ALL MATCH: PASS' if all_ok else 'FAIL'}")
    return all_ok


def prime_reference(sieve_limit, D):
    """Same machinery on the primes.  Returns (dict, record)."""
    primes = primes_up_to(sieve_limit)
    a0 = np.array(primes, dtype=np.int64)
    m = measure_conditional(a0, D)
    live_rows = m["trunc_k"] if m["trunc_k"] is not None else D
    all_events = len(m["events_pos"])
    overall = all_events / live_rows if live_rows else None
    return {
        "sieve_limit": sieve_limit, "num_primes": len(primes), "D": D,
        "first_b0": m["first_b0"], "trunc_k": m["trunc_k"],
        "live_rows": live_rows, "events": all_events,
        "overall_rate": overall,
        "events_post": m["events_post"], "elig_post": m["elig_post"],
        "rho_post10": (m["events_post"] / m["elig_post"]
                       if m["elig_post"] else None),
        "events_pos": m["events_pos"],
    }, m


def part_prime():
    print("=" * 100)
    print("PRIME REFERENCE  (same machinery, the actual primes)")
    print("=" * 100)
    for lim in (2_000_000, 20_000_000):
        t0 = time.time()
        p, _m = prime_reference(lim, 161)
        r10 = "-" if p["rho_post10"] is None else f"{p['rho_post10']:.6f}"
        print(f"  sieve {lim:>10}: {p['num_primes']} primes, D={p['D']}, "
              f"live rows={p['live_rows']} (trunc_k={p['trunc_k']}), "
              f"events={p['events']}, overall rate={p['overall_rate']:.4f} "
              f"({p['events']}/{p['live_rows']}), "
              f"rho_post10(k>=11)={r10} "
              f"[{time.time()-t0:.1f}s]")
        print(f"    event rows: {p['events_pos']}")
    print("  recorded reference (block data depth 1000): 60 events / "
          "161 live rows = 0.3727; the 2e7 line above checks it directly")


def main():
    t_all = time.time()
    part0_oracle()
    stored_cond = part1_sniff()
    fams = stored_survivor_families()
    if stored_cond:
        print("(stored per-row positions exist; conditional stats computed "
              "from them — Part 2 skipped)")
        return
    results = part2_run(fams)
    p, lam, rows = part2_report(results)
    ok3 = part3_crosscheck()
    part_prime()
    print("=" * 100)
    print("SUMMARY  (families used, n_workers, D, W, table, p, verdict, "
          "prime comparison)")
    print("=" * 100)
    print(f"  families used: {sorted(fams)}")
    print(f"  n_workers={workers()}  D={RUN_D}  W={RUN_W}  "
          f"seeds 10000..10019")
    print("  per-family table (conditioned on row-10 survival):")
    print(f"    {'family':<16} {'n':>3} {'ev_post':>7} {'elig_post':>9} "
          f"{'rho_post10':>9}")
    tot_E = tot_R = 0
    for fam, n, E, R in rows:
        rs = "-" if not R else f"{E/R:.6f}"
        print(f"    {fam:<16} {n:>3} {E:>7} {R:>9} {rs:>9}")
        tot_E += E
        tot_R += R
    print(f"    pooled lambda_hat = {tot_E/tot_R:.6f} "
          f"({tot_E}/{tot_R})")
    print(f"  Pearson X^2 p-value = {p:.3e}")
    print("  cross-check numpy vs pure-Python:", "PASS" if ok3 else "FAIL")
    print("  wall time", f"{time.time()-t_all:.1f}s")


RUN_D = int(os.environ.get("COND_D", 400))
RUN_W = int(os.environ.get("COND_W", 200_000))


if __name__ == "__main__":
    main()