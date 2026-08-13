#!/usr/bin/env python3
"""code/rule90_test/depth_vs_minima.py

Test the Rule-90 / powers-of-2 depth prediction against the block-length data
(TASKS.md item 3; thread research/threads/rule90-regeneration.md).

Result the test rests on (PROVED in this run, research/notes/rule90-interior.md):
within any {0,2} block the halved entries evolve under XOR = Wolfram Rule 90 =
Pascal mod 2, and at depth d = 2^j every binom(2^j, m) is odd, so the halved
entry at that depth is the XOR of a whole width-(d+1) window of the block's bit
pattern; a window of all-1 XOR regenerates an all-2 stretch.  The falsifiable
prediction tested here: the depths of block-length minima and of expansion
events, measured from the start of the current block regime, land at or near
powers of two (2^j or 2^j +/- 1).

Data: code/out/blocks_depth1000.json (exact integers, sieve 2e7, D = 1000).
b[k-1] = length of the leading {0,2} block of row k, k = 1..1000.  Every row
index of interest lies inside this record, so no rows are regenerated.

Definitions:
  local minimum    maximal equal-value run [p..q] of b strictly below its two
                   outer neighbours (row 1 and row D count as open ends); the
                   block first reaches the new minimum value at row p.
  origin prev_min     depth = k - p'   (p' = FIRST row of previous min run)
  origin last_minval  depth = k - q'   (q' = LAST row of previous min run,
                   i.e. the row where the block was last at its minimal value)
  origin absolute     depth = k - 1
  expansion event     transition R-1 -> R with b[R-1] - b[R-2] = mag > 0,
                   tested at thresholds >= median positive jump and >= 1000.
  match               |depth - 2^j| <= tol for some j >= 0, tol in {0,1,2,4}.

36 hypothesis variants = 3 origins x 4 tolerances x 3 thresholds, fanned out
with code/lib/parallel.py across the 28-CPU box.  O(D) time and O(D) space per
variant, D = 1000: the cost scales with the record length, never with a search
bound.

Outputs: this program writes code/out/rule90_depth_test.notes.md (the
match/mismatch tables) and everything printed is captured to
code/out/rule90_depth_test.captured.txt by the caller.
"""

from __future__ import annotations

import json
import os
from statistics import median

from lib.parallel import workers, parallel_map, announce

DATA = "code/out/blocks_depth1000.json"
NOTES = "code/out/rule90_depth_test.notes.md"
ORIGINS = ("prev_min", "last_minval", "absolute")
TOLS = (0, 1, 2, 4)


def load_record(path=DATA):
    with open(path) as fh:
        return json.load(fh)


def nearest_pow2(d):
    """(2^j, j, |d - 2^j|) for the power of two nearest d; ties -> smaller."""
    best = None
    j = 0
    while j < 20:
        p = 1 << j
        dist = abs(d - p)
        if best is None or dist < best[2]:
            best = (p, j, dist)
        if p >= d and p - d >= best[2]:
            break
        j += 1
    return best


def near_pow2(d, tol):
    """True iff d >= 1 and |d - 2^j| <= tol for some j >= 0."""
    if d is None or d <= 0:
        return False
    j = 0
    while j < 20:
        p = 1 << j
        if abs(d - p) <= tol:
            return True
        if p > d + tol:
            return False
        j += 1
    return False


def local_min_runs(b):
    """Maximal equal-value runs [p..q] (1-based rows) strictly below their two
    outer neighbours; boundaries count as open.  Returns [(p, q, value)] in
    increasing row order."""
    n = len(b)
    runs = []
    i = 0
    while i < n:
        j = i
        while j + 1 < n and b[j + 1] == b[i]:
            j += 1
        p, q = i + 1, j + 1
        left_ok = (p == 1) or (b[p - 2] > b[p - 1])
        right_ok = (q == n) or (b[q] > b[q - 1])
        if left_ok and right_ok:
            runs.append((p, q, b[i]))
        i = j + 1
    return runs


def regime_depths(mins, origin):
    """(k, v, depth) for every local-min run after the first; k = first row of
    the run, depth = k - ref where ref is the first (prev_min) or last
    (last_minval) row of the previous run."""
    out = []
    for idx in range(1, len(mins)):
        p, q, v = mins[idx]
        prev_p, prev_q, _ = mins[idx - 1]
        ref = prev_p if origin == "prev_min" else prev_q
        out.append((p, v, p - ref))
    return out


def expansion_events(b, threshold):
    """(R, mag) for rows R where the block grew by mag = b[R-1]-b[R-2] >=
    threshold (R in 2..len(b))."""
    return [
        (R, b[R - 1] - b[R - 2])
        for R in range(2, len(b) + 1)
        if b[R - 1] - b[R - 2] >= threshold
    ]


def event_depth(R, mins, origin):
    """Depth of event row R from the most recent local-min run before it."""
    ref = None
    for (p, q, _v) in mins:
        if p < R:
            ref = p if origin == "prev_min" else q
        else:
            break
    return None if ref is None else R - ref


def _variant(params):
    """One hypothesis variant: (b, mins, origin, tol, threshold) -> stats."""
    b, mins, origin, tol, threshold = params
    D = len(b)
    depths = [d for (_k, _v, d) in regime_depths(mins, origin) if _k < D]
    min_hits = sum(1 for d in depths if near_pow2(d, tol))
    events = expansion_events(b, threshold)
    ev_hits = 0
    ev_abs_hits = 0
    for (R, _mag) in events:
        d = R - 1 if origin == "absolute" else event_depth(R, mins, origin)
        ev_hits += 1 if near_pow2(d, tol) else 0
        ev_abs_hits += 1 if near_pow2(R - 1, tol) else 0
    return {
        "origin": origin, "tol": tol, "threshold": threshold,
        "min_hits": min_hits, "min_total": len(depths),
        "events": len(events), "ev_hits": ev_hits,
        "ev_abs_hits": ev_abs_hits,
    }


def main():
    rec = load_record()
    b = rec["b"]
    D = rec["D"]
    assert D == 1000 and len(b) == D, (D, len(b))

    report = []

    def emit(line=""):
        print(line)
        report.append(line)

    mins = local_min_runs(b)
    gen_mins = [r for r in mins if r[0] < D]
    n_workers = workers()

    emit("# Rule-90 depth prediction vs block-length minima — exact numbers")
    emit()
    emit(f"data: D={D}, sieve_limit={rec['sieve_limit']}, "
         f"num_primes={rec['num_primes']}, first_bad={rec['first_bad']}, "
         f"oracle_agree_first_40={rec['oracle_agree_first_40']}")
    emit(f"workers: {n_workers} (of {os.cpu_count()} CPUs)")
    emit()
    emit(f"local-min runs (p, q, b_k): "
         f"{[(p, q, v) for (p, q, v) in mins]}")
    emit(f"runs: {len(mins)} total; {len(gen_mins)} genuine — the row-{D} run "
         f"is a finite-width artifact (from row 163 the block fills the sieve "
         f"row and erodes one column per row; intruder is None there)")

    # ---- minima match/mismatch tables -------------------------------------
    for origin in ("prev_min", "last_minval"):
        ref_name = "first" if origin == "prev_min" else "LAST"
        emit()
        emit(f"--- origin {origin}: depth = k - ({ref_name} row of previous "
             f"min run) ---")
        emit(f"{'k':>4} {'b_k':>9} {'ref':>6} {'d':>5} {'2^j':>4} {'j':>2} "
             f"{'dist':>4} {'tol1':>4} {'tol0':>4}")
        for idx, (p, q, v) in enumerate(mins):
            if idx == 0:
                continue
            ref = mins[idx - 1][0] if origin == "prev_min" else mins[idx - 1][1]
            d = p - ref
            np = nearest_pow2(d)
            tag = "   (artif.)" if p == D else ""
            emit(f"{p:>4} {v:>9} {ref:>6} {d:>5} {np[0]:>4} {np[1]:>2} "
                 f"{np[2]:>4} {'Y' if np[2] <= 1 else 'N':>4} "
                 f"{'Y' if np[2] == 0 else 'N':>4}{tag}")

    # ---- depth hit counts ---------------------------------------------------
    emit()
    emit("=== depth hit counts (genuine minima only, k < D: 26 depths; the "
         "first run has no reference) ===")
    for origin in ORIGINS:
        depths = [d for (_k, _v, d) in regime_depths(gen_mins, origin)]
        parts = [f"origin {origin:>4}:"]
        for tol in TOLS:
            hits = sum(1 for d in depths if near_pow2(d, tol))
            parts.append(f"tol{tol}: {hits}/{len(depths)}")
        emit("  " + "  ".join(parts))
    d_prev = [d for (_k, _v, d) in regime_depths(gen_mins, "prev_min")]
    d_last = [d for (_k, _v, d) in regime_depths(gen_mins, "last_minval")]
    emit(f"  genuine depths prev_min:    {d_prev}")
    emit(f"  genuine depths last_minval: {d_last}")
    h0 = sum(1 for d in d_prev if near_pow2(d, 0))
    h1 = sum(1 for d in d_prev if near_pow2(d, 1))
    emit(f"  comparability with the prior run: prev_min counts with the "
         f"degenerate k=1 depth-0 entry appended (never a hit): tol0 {h0}/27, "
         f"tol1 {h1}/27 — reproduces code/out/rule90_depth_test.captured.txt "
         f"(10/27, 21/27) and rule90_depth_null.json (21/27)")

    # ---- baseline ------------------------------------------------------------
    emit()
    emit("=== baseline: uniform over the observed genuine depth range "
         "(fraction of integer values near a power of two) ===")
    for origin in ORIGINS:
        depths = [d for (_k, _v, d) in regime_depths(gen_mins, origin)]
        lo, hi = min(depths), max(depths)
        for tol in TOLS:
            near_vals = [v for v in range(lo, hi + 1) if near_pow2(v, tol)]
            obs = sum(1 for d in depths if near_pow2(d, tol))
            emit(f"  {origin:>4} tol={tol}: baseline "
                 f"{len(near_vals)}/{hi - lo + 1} "
                 f"({100.0 * len(near_vals) / (hi - lo + 1):.0f}%)  observed "
                 f"{obs}/{len(depths)} ({100.0 * obs / len(depths):.0f}%)")

    # ---- expansion events ----------------------------------------------------
    jumps = expansion_events(b, 1)
    mags = [m for (_R, m) in jumps]
    med = median(mags)
    emit()
    emit(f"=== expansion events: {len(jumps)} positive jumps; mag min "
         f"{min(mags)}, median {med}, max {max(mags)}; >=1000: "
         f"{sum(1 for m in mags if m >= 1000)}")
    thresholds = sorted({1, med, 1000})
    emit(f"thresholds used: {thresholds}")
    for thr in (med, 1000):
        evs = expansion_events(b, thr)
        emit()
        emit(f"--- events with mag >= {thr} ---")
        emit(f"{'R':>4} {'mag':>8} {'d_pm':>5} {'2^j':>4} {'dst':>4} {'t1':>3}"
             f" {'d_lm':>5} {'2^j':>4} {'dst':>4} {'t1':>3}"
             f" {'d_abs':>5} {'2^j':>4} {'dst':>4} {'t1':>3}")
        for (R, mag) in evs:
            dp = event_depth(R, mins, "prev_min")
            dl = event_depth(R, mins, "last_minval")
            da = R - 1
            np_p, np_l, np_a = nearest_pow2(dp), nearest_pow2(dl), nearest_pow2(da)
            emit(f"{R:>4} {mag:>8} {dp:>5} {np_p[0]:>4} {np_p[2]:>4} "
                 f"{'Y' if np_p[2] <= 1 else 'N':>3}"
                 f" {dl:>5} {np_l[0]:>4} {np_l[2]:>4} "
                 f"{'Y' if np_l[2] <= 1 else 'N':>3}"
                 f" {da:>5} {np_a[0]:>4} {np_a[2]:>4} "
                 f"{'Y' if np_a[2] <= 1 else 'N':>3}")

    # ---- parallel variants ---------------------------------------------------
    variants = [(b, mins, origin, tol, thr)
                for origin in ORIGINS for tol in TOLS for thr in thresholds]
    announce("rule90-depth variants", f"{len(variants)} variants x D={D}",
             n_workers if len(variants) > 1 else 1)
    results = parallel_map(_variant, variants, label="rule90-depth",
                           space=f"{len(variants)} variants", count=n_workers)
    emit()
    emit(f"=== variant table (parallel across {n_workers} workers) ===")
    emit(f"{'origin':>11} {'tol':>3} {'thr':>6} {'minH/tot':>9} {'ev':>4} "
         f"{'evH':>4} {'rate':>6} {'evAbsH':>7}")
    for r in results:
        rate = (f"{100.0 * r['ev_hits'] / r['events']:.0f}%"
                if r["events"] else "-")
        emit(f"{r['origin']:>11} {r['tol']:>3} {r['threshold']:>6} "
             f"{r['min_hits']}/{r['min_total']:>5} {r['events']:>4} "
             f"{r['ev_hits']:>4} {rate:>6} {r['ev_abs_hits']:>7}")

    # ---- cross-check against the established regeneration criterion ----------
    s = rec["s"]
    intr = rec["intruder"]
    ok = tot = 0
    fails = []
    for (R, _mag) in jumps:
        pre_row = R - 1  # 1-based row before the expansion
        c = intr[pre_row - 1]
        if c is None:
            continue
        tot += 1
        if s[pre_row - 1] == 2 and c == 4:
            ok += 1
        else:
            fails.append((R, s[pre_row - 1], c))
    emit()
    emit("=== cross-check: positive jumps vs the established regeneration "
         "criterion (edge==2 and intruder==4 at the pre-transition row) ===")
    emit(f"  {ok}/{tot} pre-rows satisfy it; {len(fails)} failures: {fails}")

    with open(NOTES, "w") as fh:
        fh.write("\n".join(report) + "\n")
    print(f"\nwrote {NOTES}")


if __name__ == "__main__":
    main()