#!/usr/bin/env python3
"""Event-gap analysis for the edge-sliding (rightmost-2 depth) prediction.

Structural prediction under test (Rule-90 interior consequence; the apex fold
of the block lemma, which is PROVED: within a {0,2} block the halved entries
evolve as XOR = Rule 90 = Pascal mod 2).  During an erosion run (no (2,4)-
events since the last event or since row 1) starting at row K with run-start
block length b_K, let

    D = distance from the block edge (column b_K) to its rightmost 2
      = b_K - max{ i <= b_K : A_K[i] == 2 }        (D = 0 iff edge is 2).

Claim (edge-sliding, the PROVED core after the block lemma + step law): the
edge x_k = A_k[b_k] is 0 for all K <= k < K+D and is 2 exactly at k = K+D.
Reason: at depth d the edge value is the XOR of the halved entries in columns
b_K-d .. b_K (window slides left); while the window sits inside the all-0 tail
right of the rightmost 2 the XOR is 0; at d = D the window's only 1 is the
rightmost 2 (binomial weight 1).  Two empirical consequences, which this run
measures:
  (P2) if the intruder at row K+D is 4 (y-pinning), the event fires EXACTLY
       at K+D, i.e. the run's wait W = E - K equals D;
  (G)  inter-event gaps = waits + 1 follow the run-start rightmost-2-depth
       distribution (not memoryless geometric).

Null for (G): memoryless geometric — events i.i.d. Bernoulli(p) per eligible
row, p = pooled event rate 0.585 (random families) / 0.373 (primes).  A
geometric on {1,2,...} has sd/mean = sqrt(1-p) < 1 always; observed gap
sd/mean above that supports the structured-wait alternative.

The proof core P1 (edge == 0 before K+D, == 2 at K+D) MUST hold for every
run: an event before K+D, or a nonzero edge in the 0-window, would refute the
proved consequence (block lemma + step law), not merely the prediction.

Uses:
  - code/out/conditional_rate_records.jsonl  (220 records; events_pos per seq)
  - code/out/blocks_depth1000.json           (prime b-series -> event rows)
  - event_rate.event_rate_sweep._gaps        (single source of truth for gaps)

Parts:
  A. gap distribution at k>=11 from the records: histogram, mean, median, max,
     sd, sd/mean, var/mean; geometric MLE fit + chi-square GOF + simulated
     P(sd/mean >= observed | geometric(p_hat)); per-family gap stats.
  B. regenerate the 118 survivors (D=400, W=200000, same seeds/families):
     verify events_pos == records; per-run edge-sliding test: D (rightmost-2
     depth of run-start block), edge profile (0 on [K,K+D), 2 at K+D), y at
     K+D (pinning), event timing category (hit/early/late-unpinned/late-2),
     waits; gaps grouped by run-start b.
  C. primes: event rows from blocks_depth1000 b-series (event at row k iff
     b_{k+1} >= b_k), verified against the recorded 60-row list; prime gap
     distribution vs geometric(0.373) null; regenerate prime rows D=161
     (sieve 2e7) for run-start blocks; same per-run test.
  D. verdict.

Complexity: O(#seqs * D * W) time, O(W) per worker (14 workers to bound
memory: <= ~140 MB per worker worst case).  118 seqs at D=400,W=2e5 across
14 workers ~ 60-70 s; primes 161 rows of 1.27e6 ~ 6 s single process.
"""
import json
import math
import random
import time

import numpy as np

from lib.gilbreath import primes_up_to
from lib.parallel import parallel_map, workers

import event_rate.event_rate_sweep as SWEEP

RECORDS = "code/out/conditional_rate_records.jsonl"
BLOCKS = "code/out/blocks_depth1000.json"
D, W = 400, 200_000


def make_a0(fam, seed, W=W):
    rng = np.random.default_rng(seed)
    gaps = SWEEP._gaps(fam, rng, W - 2)
    a0 = np.empty(W, dtype=np.int64)
    a0[0] = 2
    a0[1] = 3
    a0[2:] = 3 + np.cumsum(gaps)
    return a0


def evolve(a0, D):
    """Per-row records (k=1..D): (k, b, x, y, ev) + rows stashed only at
    run starts (row 1 and rows after an event row).  O(D*W) time, O(W) + a
    few stashed rows of memory."""
    cur = a0
    recs = []
    rows_at = {}
    for k in range(1, D + 1):
        row = np.abs(cur[:-1] - cur[1:])
        width = row.shape[0]
        sel = row[1:]
        m = (sel == 0) | (sel == 2)
        if m.all():
            b = sel.shape[0]
        else:
            b = int(np.argmax(~m))
        elig = (b >= 1 and b + 1 < width)
        if elig:
            x = int(row[b])
            y = int(row[b + 1])
            ev = (x == 2 and y == 4)
            recs.append((k, b, x, y, ev))
        else:
            recs.append((k, b, None, None, False))
        if k == 1 or (len(recs) >= 2 and recs[-2][4]):
            rows_at[k] = row.copy()
        cur = row
    return recs, rows_at


def _run_task(task):
    """Pool shim: parallel_map hands over the whole item, not unpacked args."""
    fam, seed = task
    return run_test(fam, seed)


def rightmost2_depth(row, b):
    """D = distance from the block edge (1-based column b) to the rightmost
    entry == 2 within columns 1..b.  None if the block has no 2."""
    blk = row[1:b + 1]
    twos = np.nonzero(blk == 2)[0]
    if twos.size == 0:
        return None
    p_max = int(twos[-1]) + 1          # 1-based column of rightmost 2
    return b - p_max


def run_test(fam, seed):
    """Full per-run edge-sliding test for one (family, seed)."""
    a0 = make_a0(fam, seed)
    recs, rows_at = evolve(a0, D)
    # runs: K = 1 or event row + 1, E = next event row (or None)
    runs = []
    K = 1
    for k, b, x, y, ev in recs:
        if ev:
            runs.append((K, k))
            K = k + 1
    details = []
    for (K, E) in runs:
        bK = recs[K - 1][1]                     # run-start block length
        rowK = rows_at[K]
        d = rightmost2_depth(rowK, bK)
        # edge profile rows K..min(E, K+d): (k, x)
        prof = []
        end = min(E, K + d) if d is not None else E
        for kk in range(K, end + 1):
            prof.append((kk, recs[kk - 1][2]))
        # intruder at the predicted row K+d (if <= D and exists)
        y_pred = None
        if d is not None and K + d <= D:
            r = recs[K + d - 1]
            y_pred = r[3]
        details.append({
            "K": K, "E": E, "bK": bK, "D": d, "wait": E - K,
            "pred": (None if d is None else K + d),
            "y_pred": y_pred,
            "prof": prof,
            "events_pos_all": [k for k, b, x, y, ev in recs if ev],
        })
    return {
        "family": fam, "seed": seed,
        "events_pos": [k for k, b, x, y, ev in recs if ev],
        "n_runs": len(runs),
        "run_details": details,
    }


def gap_stats_list(gaps, label):
    if not gaps:
        print(f"    {label:<14} n/a")
        return {}
    n = len(gaps)
    mean = sum(gaps) / n
    sd = (sum((g - mean) ** 2 for g in gaps) / (n - 1)) ** 0.5
    med = sorted(gaps)[n // 2]
    out = {"n": n, "mean": mean, "sd": sd, "median": med,
           "max": max(gaps), "sd/mean": sd / mean, "var/mean": sd * sd / mean}
    print(f"    {label:<14} n={n:>5} mean={mean:7.3f} median={med:>3} "
          f"max={max(gaps):>4} sd={sd:6.3f} sd/mean={sd / mean:5.3f} "
          f"var/mean={sd * sd / mean:5.3f}")
    return out


def geo_sim_dispersion(gaps, phat, seed=12345, reps=5000):
    """Fraction of geometric(phat) samples of the same size with
    sd/mean >= observed sd/mean."""
    n = len(gaps)
    mm = sum(gaps) / n
    sd = (sum((g - mm) ** 2 for g in gaps) / (n - 1)) ** 0.5
    ratio = sd / mm
    rng = random.Random(seed)
    cnt = 0
    lp = math.log(1 - phat)
    for _ in range(reps):
        gs = [int(math.log(u) / lp) + 1 for u in
              (rng.random() for _ in range(n))]
        m2 = sum(gs) / n
        v2 = sum((g - m2) ** 2 for g in gs) / (n - 1)
        if (v2 ** 0.5) / m2 >= ratio:
            cnt += 1
    return cnt, reps, ratio


def chi2_geometric(hist, n, phat):
    """Chi-square GOF vs geometric, merging the tail so expected >= 5."""
    mx = max(hist)
    merged = []
    buf_lo = None
    buf_e = 0.0
    buf_o = 0
    for g in range(1, mx + 1):
        e = n * phat * (1 - phat) ** (g - 1)
        if buf_lo is None:
            buf_lo = g
        buf_e += e
        buf_o += hist.get(g, 0)
        if buf_e >= 5.0:
            merged.append((buf_lo, g, buf_o, buf_e))
            buf_lo = None
            buf_e = 0.0
            buf_o = 0
    if buf_lo is not None:
        lg, ug, lo, le = merged[-1]
        merged[-1] = (lg, ug, lo + buf_o, le + buf_e)
    chi = sum((o - e) ** 2 / e for (_, _, o, e) in merged)
    df = len(merged) - 2
    from scipy.stats import chi2 as chi2mod
    p = chi2mod.sf(chi, df) if df > 0 else float("nan")
    return chi, df, p, merged


def main():
    t0 = time.time()
    records = [json.loads(l) for l in open(RECORDS)]
    surv = [r for r in records if r["first_b0"] is None or r["first_b0"] > 10]
    print("=" * 100)
    print("PART A  GAP DISTRIBUTION AT k>=11 FROM RECORDS")
    print("=" * 100)
    print(f"  records: {len(records)}, survivors: {len(surv)}, "
          f"total events_post: {sum(r['events_post'] for r in surv)}")

    def gaps_of(rs):
        g = []
        for r in rs:
            p = [k for k in r["events_pos"] if k >= 11]
            g.extend(b - a for a, b in zip(p, p[1:]))
        return g

    gaps = gaps_of(surv)
    n = len(gaps)
    mean = sum(gaps) / n
    sd = (sum((g - mean) ** 2 for g in gaps) / (n - 1)) ** 0.5
    med = sorted(gaps)[n // 2]
    mx = max(gaps)
    print(f"  pooled: {gap_stats_list(gaps, 'pooled') if False else ''}"
          f"n={n} mean={mean:.3f} median={med} max={mx} sd={sd:.3f}")
    print(f"  sd/mean = {sd / mean:.4f}   var/mean = {sd * sd / mean:.4f}")
    phat = 1.0 / mean
    print(f"  geometric null with p_hat = 1/mean = {phat:.4f} "
          f"(matches pooled event rate 0.585):")
    print(f"    mean {1 / phat:.4f}, null sd/mean = sqrt(1-p) = "
          f"{math.sqrt(1 - phat):.4f}  (< 1 always for geometric)")
    print(f"    observed sd/mean {sd / mean:.4f} vs null {math.sqrt(1 - phat):.4f}"
          f"  -> ratio {sd / mean / math.sqrt(1 - phat):.2f}x over geometric")
    from collections import Counter
    hist = Counter(gaps)
    print("  gap histogram:", " ".join(f"{g}:{hist[g]}" for g in sorted(hist)))
    chi, df, pg, merged = chi2_geometric(hist, n, phat)
    print(f"  chi-square GOF vs geometric: chi2={chi:.3f} df={df} "
          f"p={pg:.4f}")
    print("    merged cells:", "; ".join(
        f"[{a}-{b}] obs {o} exp {e:.1f}" for a, b, o, e in merged))
    cnt, reps, ratio = geo_sim_dispersion(gaps, phat)
    print(f"  simulation P(sd/mean >= {ratio:.3f} | geom({phat:.3f})) = "
          f"{cnt}/{reps} = {cnt / reps:.4f}")
    # per-sequence count overdispersion (reproduce recorded 1.86)
    ev = [r["events_post"] for r in surv if r["elig_post"] > 0]
    m = sum(ev) / len(ev)
    v = sum((x - m) ** 2 for x in ev) / (len(ev) - 1)
    print(f"  per-sequence events_post count: mean {m:.2f}, "
          f"var/mean = {v / m:.2f} (recorded 1.86)")
    fams = sorted({r["family"] for r in surv})
    print("  per-family k>=11 gaps:")
    for fam in fams:
        sel = [r for r in surv if r["family"] == fam]
        gap_stats_list(gaps_of(sel), fam)

    # ---- PART B: regenerate survivors, verify, edge-sliding test ----
    print()
    print("=" * 100)
    print("PART B  REGENERATE SURVIVORS -> EDGE-SLIDING TEST")
    print("=" * 100)
    tasks = [(r["family"], r["seed"]) for r in surv]
    nw = min(workers(), 14)          # bound memory: <=~140 MB/worker
    print(f"  {len(tasks)} sequences, {nw} workers, ~60-70 s wall",
          flush=True)
    def _run(task):
        fam, seed = task
        return run_test(fam, seed)
    res = parallel_map(_run_task, tasks, label="edge-sliding",
                       space="survivor seqs", count=nw)
    rmap = {(r["family"], r["seed"]): r for r in surv}
    verr = 0
    for z in res:
        if rmap[(z["family"], z["seed"])]["events_pos"] != z["events_pos"]:
            verr += 1
            print(f"  MISMATCH {z['family']}@{z['seed']}")
    print(f"  events_pos vs records: "
          f"{'PASS ' + str(len(res) - verr) + '/' + str(len(res))}"
          if verr == 0 else f"  FAIL {verr}")

    agg = {"runs": 0, "D0": 0, "Dge1": 0, "no2": 0, "hit": 0, "early": 0,
           "late_unpin": 0, "late2": 0, "prof_ok": 0, "prof_bad": 0,
           "y_pred4": 0}
    waits_all, ds_all, extras = [], [], []
    gap_by_b = {}
    for z in res:
        for rd in z["run_details"]:
            agg["runs"] += 1
            d = rd["D"]
            if d is None:
                agg["no2"] += 1
                continue
            ds_all.append(d)
            if d == 0:
                agg["D0"] += 1
            else:
                agg["Dge1"] += 1
            # edge profile check: x == 0 on [K, min(E,K+D)-1], x == 2 at
            # min(E, K+D)
            prof = rd["prof"]
            end = min(rd["E"], rd["pred"])
            ok = True
            for (kk, xk) in prof:
                if kk < end and xk != 0:
                    ok = False
                elif kk == end and xk != 2:
                    ok = False
            if ok:
                agg["prof_ok"] += 1
            else:
                agg["prof_bad"] += 1
                if agg["prof_bad"] <= 5:
                    print(f"    PROFILE FAIL {z['family']}@{z['seed']} "
                          f"run K={rd['K']} E={rd['E']} D={d} "
                          f"prof={prof[:20]}")
            E, pred = rd["E"], rd["pred"]
            if E < pred:
                agg["early"] += 1
            elif E == pred:
                agg["hit"] += 1
                agg["y_pred4"] += 1
                if rd["y_pred"] != 4:
                    print(f"    INCONSISTENT hit with y_pred={rd['y_pred']} "
                          f"{z['family']}@{z['seed']} K={rd['K']}")
            else:  # E > pred
                if rd["y_pred"] == 4:
                    agg["late2"] += 1      # refutation: pinned but late
                else:
                    agg["late_unpin"] += 1
                extras.append(E - pred)
            waits_all.append(rd["wait"])
            b = rd["bK"]
            key = ("b<10" if b < 10 else "b10-99" if b < 100
                   else "b100-999" if b < 1000 else "b1000-99999"
                   if b < 100000 else "b>=1e5")
            grp = gap_by_b.setdefault(key, [0, 0, 0, 0, 0])  # n,hit,early,late
            grp[0] += 1
            if E < pred:
                grp[3] += 1
            elif E == pred:
                grp[1] += 1
            else:
                grp[4] += 1
    n_ev = agg["hit"] + agg["early"] + agg["late_unpin"] + agg["late2"]
    n_det = agg["hit"] + agg["early"] + agg["late2"] + agg["late_unpin"]
    print(f"  runs: {agg['runs']} = {agg['D0']} D0 + {agg['Dge1']} D>=1 "
          f"+ {agg['no2']} no-2-in-block")
    print(f"  event timing: hit (E==K+D) {agg['hit']}, early (E<K+D) "
          f"{agg['early']}, late-unpinned (E>K+D, y!=4 at K+D) "
          f"{agg['late_unpin']}, late-2 (E>K+D, y==4 at K+D — refutes) "
          f"{agg['late2']}")
    if n_ev:
        print(f"  hit-rate over runs with a 2: {agg['hit']}/{n_det} "
              f"= {agg['hit'] / n_det:.3f}")
    print(f"  y-pinning at K+D: {agg['y_pred4']}/{agg['runs'] - agg['no2']} "
          f"= {agg['y_pred4'] / max(1, agg['runs'] - agg['no2']):.3f} "
          f"of runs with a 2")
    print(f"  edge profile (0 before K+D, 2 at K+D): {agg['prof_ok']} ok, "
          f"{agg['prof_bad']} bad")
    print(f"  early count {agg['early']} + late-2 count {agg['late2']} + "
          f"profile-bad {agg['prof_bad']} = the refutation budget "
          f"(must be 0 for the proved core)")
    if ds_all:
        ds_all.sort()
        print(f"  D (rightmost-2 depth) dist: n={len(ds_all)} "
              f"min={ds_all[0]} median={ds_all[len(ds_all) // 2]} "
              f"max={ds_all[-1]} mean={sum(ds_all) / len(ds_all):.3f}")
        print("  D histogram:", " ".join(
            f"{g}:{sum(1 for x in ds_all if x == g)}"
            for g in sorted(set(ds_all))))
    gap_stats_list(waits_all, "waits W")
    gapsB = [w + 1 for w in waits_all]
    gap_stats_list(gapsB, "gaps(=W+1)")
    if extras:
        extras.sort()
        print(f"  late extra time E-(K+D): n={len(extras)} "
              f"min={extras[0]} median={extras[len(extras) // 2]} "
              f"max={extras[-1]} mean={sum(extras) / len(extras):.2f}")
    print("  runs by run-start b (n, hit, early, late) and gap stats:")
    for key in sorted(gap_by_b):
        n0, h, e, l, l2 = gap_by_b[key]
        print(f"    {key:<12} n={n0:>4} hit={h:>3} ({h / n0:.3f}) "
              f"early={e:>3} late={l + l2:>3}")
        gb = []
        for z in res:
            for rd in z["run_details"]:
                if rd["D"] is None:
                    continue
                kk = ("b<10" if rd["bK"] < 10 else "b10-99" if rd["bK"] < 100
                      else "b100-999" if rd["bK"] < 1000
                      else "b1000-99999" if rd["bK"] < 100000 else "b>=1e5")
                if kk == key:
                    gb.append(rd["wait"] + 1)
        gap_stats_list(gb, key + " gaps")

    # ---- PART C: primes ----
    print()
    print("=" * 100)
    print("PART C  PRIMES: events, gaps, edge-sliding test")
    print("=" * 100)
    bj = json.load(open(BLOCKS))
    bs = bj["b"]
    ev_rows = [i + 1 for i in range(len(bs) - 1)
               if bs[i + 1] >= bs[i] and i + 1 <= 161]
    rec60 = [1, 2, 3, 4, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 22, 23, 26, 34,
             38, 47, 48, 49, 50, 51, 56, 57, 62, 63, 64, 68, 72, 75, 76, 79,
             80, 86, 91, 94, 96, 110, 111, 112, 125, 126, 128, 129, 130, 131,
             132, 134, 135, 136, 138, 141, 142, 143, 146, 159, 160, 161]
    print(f"  b-series events (rows<=161): {len(ev_rows)}; matches recorded "
          f"60-row list: {ev_rows == rec60}")
    pg = [b - a for a, b in zip(ev_rows, ev_rows[1:])]
    gap_stats_list(pg, "prime gaps")
    print(f"  geometric null p=0.3727: mean={1 / 0.3727:.3f}, "
          f"sd/mean={math.sqrt(1 - 0.3727):.3f} ({pg and 0 or ''}"
          f"null always < 1)")
    print("  prime gap histogram:", " ".join(
        f"{g}:{sum(1 for x in pg if x == g)}" for g in sorted(set(pg))))
    if len(pg) >= 20:
        hh = Counter(pg)
        chi2p, dfp, pp, mergedp = chi2_geometric(hh, len(pg), 0.3727)
        print(f"  chi-square GOF vs geometric(0.373): chi2={chi2p:.3f} "
              f"df={dfp} p={pp:.4f}   (merged cells: "
              + "; ".join(f"[{a}-{b}] obs{o} exp{e:.1f}"
                          for a, b, o, e in mergedp) + ")")
        cntp, repsp, ratiop = geo_sim_dispersion(pg, 0.3727)
        print(f"  simulation P(sd/mean >= {ratiop:.3f} | geom(0.373)) = "
              f"{cntp}/{repsp} = {cntp / repsp:.4f}")
    else:
        print("  (too few gaps for GOF/simulation)")
    # regenerate prime rows for run-start blocks
    print("  regenerating prime rows (sieve 2e7, D=161)...", flush=True)
    primes = primes_up_to(20_000_000)
    a0 = np.array(primes, dtype=np.int64)
    recs_p, rows_at_p = evolve(a0, 161)
    ev_p = [k for k, b, x, y, ev in recs_p if ev]
    print(f"  regenerated prime events: {len(ev_p)}; matches b-series: "
          f"{ev_p == ev_rows}")
    runs_p = []
    K = 1
    for k, b, x, y, ev in recs_p:
        if ev:
            runs_p.append((K, k, recs_p[K - 1][1]))
            K = k + 1
    print(f"  prime runs: {len(runs_p)}")
    phit = pe = pl = pl2 = 0
    pD = []
    pwait = []
    pprof_bad = 0
    for (K, E, bK) in runs_p:
        rowK = rows_at_p[K]
        d = rightmost2_depth(rowK, bK)
        if d is None:
            continue
        pD.append(d)
        pwait.append(E - K)
        y_pred = recs_p[K + d - 1][3] if K + d <= 161 else None
        # profile check
        ok = True
        end = min(E, K + d)
        for kk in range(K, end + 1):
            xk = recs_p[kk - 1][2]
            if kk < end and xk != 0:
                ok = False
            elif kk == end and xk != 2:
                ok = False
        if not ok:
            pprof_bad += 1
        if E < K + d:
            pe += 1
        elif E == K + d:
            phit += 1
        else:
            if y_pred == 4:
                pl2 += 1
            else:
                pl += 1
    npr = phit + pe + pl + pl2
    print(f"  prime run test (n={npr}): hit (E==K+D) {phit} "
          f"({phit / npr:.3f}), early {pe}, late-unpinned {pl}, "
          f"late-2 {pl2}; profile-bad {pprof_bad}")
    if pD:
        pD.sort()
        print(f"  prime D dist: n={len(pD)} min={pD[0]} "
              f"median={pD[len(pD) // 2]} max={pD[-1]} "
              f"mean={sum(pD) / len(pD):.3f}")
        print("  prime D histogram:", " ".join(
            f"{g}:{sum(1 for x in pD if x == g)}" for g in sorted(set(pD))))
    gap_stats_list(pwait, "prime waits")
    gap_stats_list([w + 1 for w in pwait], "prime gaps(=W+1)")

    # ---- verdict ----
    print()
    print("=" * 100)
    print("PART D  VERDICT")
    print("=" * 100)
    ref_budget = agg["early"] + agg["late2"] + agg["prof_bad"]
    print(f"  (1) Proved core (edge 0 before K+D, 2 at K+D, no early "
          f"events): refutation budget = {ref_budget} over {agg['runs']} "
          f"random-family runs"
          f" + {pprof_bad} profile-bad over {npr} prime runs")
    print(f"  (2) y-pinning at K+D: "
          f"{agg['y_pred4']}/{agg['runs'] - agg['no2']} random, "
          f"prime: events hit {phit}/{npr} exactly at K+D")
    print(f"  (3) gap dispersion verdict: random sd/mean "
          f"{sd / mean:.3f} vs geometric null {math.sqrt(1 - phat):.3f}; "
          f"prime sd/mean printed above in PART C.  A geometric process "
          f"always has sd/mean = sqrt(1-p) < 1; observed values above that "
          f"are the overdispersion the edge-sliding prediction explains.")
    print(f"  wall time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()