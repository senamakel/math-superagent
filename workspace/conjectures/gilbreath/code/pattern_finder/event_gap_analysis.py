#!/usr/bin/env python3
"""Event-gap analysis for the edge-sliding (rightmost-2 depth) prediction.

Structural prediction under test (Rule-90 interior consequence, PROVED core:
within a {0,2} block the halved entries evolve as XOR / Rule 90 / Pascal mod 2,
block lemma).  During an erosion run (no (2,4)-events since the last event or
since row 1) starting at row K with run-start block length b_K, let

    D = distance from the block edge (position b_K) to its rightmost 2
      = b_K - max{ i <= b_K : A_K[i] == 2 }      (D = 0 iff edge is 2).

Claim (edge-sliding): the edge x_k = A_k[b_k] is 0 for all K <= k < K+D and is
2 exactly at k = K+D.  Reason: at depth d the edge value is the XOR of the
initial halved entries in columns b_K-d .. b_K (window slide left); while the
window sits inside the all-0 tail right of the rightmost 2 the XOR is 0, and
at d = D the window's only 1 is the rightmost 2 (binomial weight 1).  Under
y=4 pinning (intruder == 4 at row K+D) the event fires exactly at K+D, i.e.
the run's wait W = E - K equals D (inter-event gap = D + 1).

Null: memoryless geometric — events i.i.d. Bernoulli(p) per eligible row,
p = pooled rate 0.585 (random families) / 0.373 (primes).  Gap sd/mean =
sqrt(1-p) < 1 for geometric on {1,2,...}; observed sd/mean well above that
supports the structured-wait alternative (waits = depths of rightmost 2s:
a few small scales, not geometric).

Uses:
  - code/out/conditional_rate_records.jsonl  (220 records; events_pos per seq)
  - code/out/blocks_depth1000.json           (prime b-series -> event rows)
  - event_rate.event_rate_sweep._gaps        (single source of truth for gaps)

Parts:
  A. gap distribution at k>=11 from the records: histogram, mean, median, max,
     sd, sd/mean, var/mean; geometric MLE fit + chi-square GOF + simulated
     dispersion p-value (null sd/mean = sqrt(1-p_hat) < 1).
  B. regenerate the 118 survivors (D=400, W=200000, same seeds/families):
     verify events_pos == records; per-run edge-sliding test (run-start block
     rightmost-2 depth D vs actual event row E; edge profile x_k == 0 on
     [K, min(E,K+D)) and x at min(E,K+D) == 2).  Group by run-start b.
  C. primes: event rows from blocks_depth1000 b-series (event at k iff
     b[k] >= b[k-1]); verify vs the recorded 60-row list; regenerate prime
     rows D=161 (sieve 2e7) for run-start blocks; same per-run test; prime
     gap distribution vs geometric(0.373) null.
  D. verdict: is the overdispersion consistent with edge-sliding (waits =
     rightmost-2 depths, D>=1 across runs, event at K+D when y pinned) or
     with a plain memoryless geometric process?

Complexity: O(#seqs * D * W) row arithmetic, O(W) per worker; 118 seqs at
D=400,W=2e5 across 26 workers ~ 35 s; primes 161 rows of 1.27e6 ~ 5 s.
"""
import json
import math
import os
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
    """Return per-row (k=1..D): b, edge x, intruder y, event flag, and the
    FULL ROW at each row (rows are cheap: D rows of width W ~ 400*200000,
    kept only as int64 lists... memory: D*W*8 = 640 MB per sequence — TOO
    BIG.  Instead return rows only via a callback-free structure: we need the
    run-start rows only; record them inside."""
    cur = a0
    recs = []          # per row: (k, b, x, y, ev)
    rows_at = {}       # row k -> full row (as list), only for run starts
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
            if ev:
                # run start is row after this event; we will need the row
                # there, which is the NEXT row — recorded below via a flag
                pass
        else:
            recs.append((k, b, None, None, False))
        # stash rows only at potential run starts: k == 1, and k == event+1
        if k == 1 or (len(recs) >= 2 and recs[-2][4]):
            rows_at[k] = row.copy()
        cur = row
    return recs, rows_at


def run_structure(recs, rows_at):
    """From per-row records, produce runs.  Each run: start K (row after
    previous event or 1), event row E (None if no event in run), run-start
    row A_K (numpy), rightmost-2 depth D of A_K's block, edge profile."""
    runs = []
    K = 1
    for k, b, x, y, ev in recs:
        if ev:
            rows = rows_at.get(K)
            runs.append((K, k, b, rows))
            K = k + 1
    # trailing run (no event): only meaningful if it is cut off by D; skip
    # (it has no event, so no wait to compare) — but record for completeness
    return runs


def rightmost2_depth(row, b):
    """D = distance from edge (position b, 1-based within row's {0,2} block
    at columns 1..b) to the rightmost entry == 2.  None if block has no 2."""
    blk = row[1:b + 1]
    twos = np.nonzero(blk == 2)[0]         # 0-based within block
    if twos.size == 0:
        return None
    p_max = int(twos[-1]) + 1              # 1-based column
    return b - p_max


def run_test(fam, seed):
    """Full per-run edge-sliding test for one sequence.  Returns dict."""
    a0 = make_a0(fam, seed)
    recs, rows_at = evolve(a0, D)
    events_rows = [k for (k, b, x, y, ev) in recs if ev]
    runs = run_structure(recs, rows_at)
    # events_pos in the SAME convention as records (1-based row indices)
    ev_pos = [r[0] for r in runs]          # each run ends at an event row
    out = {
        "family": fam, "seed": seed,
        "events_pos": ev_pos,
        "n_runs": len(runs),
        "run_details": [],
    }
    for (K, E, bK, rows) in runs:
        rowK = rows_at[K]
        b = bK
        d = rightmost2_depth(rowK, b)
        # edge profile within the run up to min(E, K+d):
        # x_k for k in [K, min(E,K+d)] from recs (k-1 index)
        # recs is 0-based list with column 0 = row 1
        prof = []
        end = min(E, K + d) if d is not None else E
        for kk in range(K, end + 1):
            xk = recs[kk - 1][2]
            prof.append((kk, xk))
        out["run_details"].append({
            "K": K, "E": E, "bK": b, "D": d, "wait": E - K,
            "pred": (None if d is None else K + d),
            "prof": prof,
        })
    return out


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
    var = sd ** 2
    med = sorted(gaps)[n // 2]
    mx = max(gaps)
    print(f"  pooled n={n} mean={mean:.4f} median={med} max={mx} "
          f"sd={sd:.4f}")
    print(f"  sd/mean = {sd / mean:.4f}   var/mean = {var / mean:.4f}")
    print(f"  geometric null (support {{1,2,...}}, p_hat=1/mean): "
          f"p_hat={1 / mean:.4f}, null sd/mean = sqrt(1-p) = "
          f"{math.sqrt(1 - 1 / mean):.4f}  (< 1 always)")
    from collections import Counter
    hist = Counter(gaps)
    print("  histogram (gap: count):",
          " ".join(f"{g}:{c}" for g, c in sorted(hist.items())))
    # chi-square GOF vs geometric, group tail so expected >= 5
    phat = 1.0 / mean
    groups = []
    exp_tail = 0.0
    obs_tail = 0
    done = False
    for g in range(1, mx + 1):
        e = n * phat * (1 - phat) ** (g - 1)
        if not done and e >= 5:
            groups.append((g, g, hist.get(g, 0), e))
            exp_tail += e - e  # noop
        elif not done:
            # accumulate into tail until >=5
            run = []
        # simpler: group tails
    # do it properly
    groups = []
    cur_exp = 0.0
    cur_obs = 0
    cur_lo = None
    chi = 0.0
    ng = 0
    # build list of (g, obs)
    seq = [(g, hist.get(g, 0)) for g in range(1, mx + 1)]
    i = 0
    merged = []
    buf = []
    buf_e = 0.0
    buf_o = 0
    for g, o in seq:
        e = n * phat * (1 - phat) ** (g - 1)
        buf.append((g, o))
        buf_e += e
        buf_o += o
        if buf_e >= 5.0:
            merged.append((buf[0][0], buf[-1][0], buf_o, buf_e))
            buf = []
            buf_e = 0.0
            buf_o = 0
    if buf:
        # merge leftover into last group
        lg, ug, lo, le = merged[-1]
        merged[-1] = (lg, ug, lo + buf_o, le + buf_e)
    chi = sum((o - e) ** 2 / e for (_, _, o, e) in merged)
    df = len(merged) - 2
    from scipy.stats import chi2 as chi2sf  # survival
    p_chi = chi2sf.sf(chi, df) if df > 0 else float("nan")
    print(f"  chi-square GOF vs geometric: {chi:.3f}, df={df}, "
          f"p={p_chi:.4f}  (groups: "
          + ";".join(f"[{a}-{b}] obs{o} exp{e:.1f}" for a, b, o, e in merged)
          + ")")
    # simulated dispersion p-value: sample geometric(p_hat) size n, count
    # sd/mean >= observed
    rng = random.Random(12345)
    reps = 5000
    cnt = 0
    for _ in range(reps):
        s = [rng.random() for _ in range(n)]
        # geometric on {1,2,...} with phat: g = floor(log(u)/log(1-phat)) + 1
        gs = [int(math.log(u) / math.log(1 - phat)) + 1 for u in s]
        m2 = sum(gs) / n
        v2 = sum((g - m2) ** 2 for g in gs) / (n - 1)
        if (v2 ** 0.5) / m2 >= sd / mean:
            cnt += 1
    print(f"  simulation: P(sd/mean >= {sd / mean:.3f} | geometric({phat:.3f}))"
          f" = {cnt}/{reps} = {cnt / reps:.4f}")
    # per-sequence count overdispersion (reproduce the 1.86 record)
    ev = [r["events_post"] for r in surv if r["elig_post"] > 0]
    m = sum(ev) / len(ev)
    v = sum((x - m) ** 2 for x in ev) / (len(ev) - 1)
    print(f"  per-sequence events_post: var/mean = {v / m:.2f} "
          f"(recorded 1.86)   mean={m:.2f}")
    # per-family gaps
    fams = sorted({r["family"] for r in surv})
    print("  per-family (k>=11):")
    for fam in fams:
        sel = [r for r in surv if r["family"] == fam]
        g = gaps_of(sel)
        if len(g) < 2:
            print(f"    {fam:<16} n/a")
            continue
        m2 = sum(g) / len(g)
        s2 = (sum((x - m2) ** 2 for x in g) / (len(g) - 1)) ** 0.5
        med2 = sorted(g)[len(g) // 2]
        print(f"    {fam:<16} n={len(g):>4} mean={m2:6.3f} "
              f"median={med2:>3} max={max(g):>3} sd/mean={s2 / m2:5.3f}")

    # ---- PART B: regenerate survivors, verify, edge-sliding test ----
    print()
    print("=" * 100)
    print("PART B  REGENERATE 118 SURVIVORS -> EDGE-SLIDING TEST")
    print("=" * 100)
    tasks = [(r["family"], r["seed"]) for r in surv]
    print(f"  {len(tasks)} sequences, {workers()} workers, ~35 s wall",
          flush=True)
    res = parallel_map(run_test, tasks, label="edge-sliding",
                       space="survivor seqs", count=workers())
    # verify events_pos vs records
    verr = 0
    rmap = {(r["family"], r["seed"]): r for r in surv}
    for z in res:
        rec = rmap[(z["family"], z["seed"])]
        if rec["events_pos"] != z["events_pos"]:
            verr += 1
            print(f"  MISMATCH {z['family']}@{z['seed']}: "
                  f"{len(rec['events_pos'])} vs {len(z['events_pos'])}")
    print(f"  events_pos verification vs records: "
          f"{'PASS (' + str(len(res) - verr) + '/' + str(len(res)) + ')' "
          f"if verr == 0 else 'FAIL ' + str(verr)}")
    # aggregate runs
    totals = {"n_runs": 0, "D0": 0, "Dge1": 0, "hit": 0, "late": 0,
              "early": 0, "no2": 0, "edge0_ok": 0, "edge0_bad": 0}
    waits = []
    ds = []
    by_b = {}
    for z in res:
        for rd in z["run_details"]:
            totals["n_runs"] += 1
            b = rd["bK"]
            key = ("b<10" if b < 10 else "b10-99" if b < 100
                   else "b100-999" if b < 1000 else "b1000-99999"
                   else "b>=1e5")
            grp = by_b.setdefault(key, [0, 0, 0, 0])  # n, hit, early, late
            Dv = rd["D"]
            if Dv is None:
                totals["no2"] += 1
                grp[0] += 1
                continue
            ds.append(Dv)
            if Dv == 0:
                totals["D0"] += 1
            else:
                totals["Dge1"] += 1
            E = rd["E"]
            pred = rd["pred"]
            # edge profile check: x_k == 0 for K..min(E,K+D)-1, x==2 at
            # min(E,K+D)
            prof = rd["prof"]
            end = min(E, pred)
            ok = True
            for (kk, xk) in prof:
                if kk < end:
                    if xk != 0:
                        ok = False
                elif kk == end:
                    if xk != 2:
                        ok = False
            if ok:
                totals["edge0_ok"] += 1
            else:
                totals["edge0_bad"] += 1
                if totals["edge0_bad"] <= 5:
                    print(f"    edge-profile FAIL: {z['family']}@{z['seed']} "
                          f"run K={rd['K']} E={E} D={Dv} prof={prof}")
            if E == pred:
                totals["hit"] += 1
                grp[1] += 1
            elif E < pred:
                totals["early"] += 1
                grp[2] += 1
            else:
                totals["late"] += 1
                grp[3] += 1
            waits.append(rd["wait"])
    print(f"  runs: {totals['n_runs']}, event-at-prediction hits "
          f"{totals['hit']}, early {totals['early']}, late {totals['late']}, "
          f"no-2-in-block {totals['no2']}")
    n_ev = totals["hit"] + totals["early"] + totals["late"]
    print(f"  D>=1 runs: {totals['Dge1']}, D==0: {totals['D0']}")
    if n_ev:
        print(f"  event row == K+D: {totals['hit']}/{n_ev} = "
              f"{totals['hit'] / n_ev:.3f}")
    print(f"  edge profile (0 on [K,min(E,K+D)), 2 at min(E,K+D)): "
          f"{totals['edge0_ok']} ok, {totals['edge0_bad']} bad of "
          f"{totals['edge0_ok'] + totals['edge0_bad']}")
    if ds:
        print(f"  D distribution: min {min(ds)} median "
              f"{sorted(ds)[len(ds) // 2]} max {max(ds)}; "
              f"mean {sum(ds) / len(ds):.3f}")
    print("  run-start b groups (n, hit, early, late):")
    for key in sorted(by_b):
        n0, h, e, l = by_b[key]
        print(f"    {key:<12} n={n0:>3} hit={h:>3} early={e:>3} "
              f"late={l:>3}  hit-rate={h / n0:.3f}")
    # waits vs D cross-tab for D>=1
    ctab = {}
    for z in res:
        for rd in z["run_details"]:
            if rd["D"] is not None and rd["D"] >= 1:
                ctab[(rd["D"], rd["wait"])] = ctab.get((rd["D"], rd["wait"]),
                                                       0) + 1
    print("  cross-tab (D, wait):")
    for (dd, ww) in sorted(ctab):
        print(f"    D={dd:<3} wait={ww:<3} count={ctab[(dd, ww)]}")

    # ---- PART C: primes ----
    print()
    print("=" * 100)
    print("PART C  PRIMES: events from b-series, gaps, run-start test")
    print("=" * 100)
    bj = json.load(open(BLOCKS))
    bs = bj["b"]
    ev_rows = [i + 1 for i in range(len(bs) - 1) if bs[i + 1] >= bs[i]
               and i + 1 <= 161]     # live regime
    rec60 = [1, 2, 3, 4, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 22, 23, 26, 34,
             38, 47, 48, 49, 50, 51, 56, 57, 62, 63, 64, 68, 72, 75, 76, 79,
             80, 86, 91, 94, 96, 110, 111, 112, 125, 126, 128, 129, 130, 131,
             132, 134, 135, 136, 138, 141, 142, 143, 146, 159, 160, 161]
    print(f"  b-series events (k<=161): {len(ev_rows)} — matches recorded 60: "
          f"{ev_rows == rec60}")
    pgaps = [b - a for a, b in zip(ev_rows, ev_rows[1:])]
    n = len(pgaps)
    m2 = sum(pgaps) / n
    s2 = (sum((g - m2) ** 2 for g in pgaps) / (n - 1)) ** 0.5
    med2 = sorted(pgaps)[n // 2]
    print(f"  prime event gaps: n={n} mean={m2:.3f} median={med2} "
          f"max={max(pgaps)} sd={s2:.3f} sd/mean={s2 / m2:.3f}")
    print(f"  geometric null p=0.373 (60/161): mean={1 / 0.373:.2f}, "
          f"null sd/mean={math.sqrt(1 - 0.373):.3f}")
    from collections import Counter
    print("  prime gap histogram:", " ".join(
        f"{g}:{c}" for g, c in sorted(Counter(pgaps).items())))
    # regenerate prime rows D=161 for run-start blocks
    print("  regenerating prime rows (sieve 2e7, D=161)...", flush=True)
    primes = primes_up_to(20_000_000)
    a0 = np.array(primes, dtype=np.int64)
    recs_p, rows_at_p = evolve(a0, 161)
    ev_p = [k for (k, b, x, y, ev) in recs_p if ev]
    print(f"  regenerated prime events: {len(ev_p)} — matches: {ev_p == ev_rows}")
    runs_p = []
    K = 1
    for k, b, x, y, ev in recs_p:
        if ev:
            runs_p.append((K, k, b))
            K = k + 1
    print(f"  prime runs: {len(runs_p)}")
    phit = pe_ = pl = 0
    pD = []
    pwait = []
    for (K, E, b) in runs_p:
        rowK = rows_at_p[K] if K in rows_at_p else None
        if rowK is None:
            # row K was not stashed? K is 1 or event+1 -> stashed
            print("  MISSING ROW", K)
            continue
        d = rightmost2_depth(rowK, b)
        if d is None:
            continue
        pD.append(d)
        pwait.append(E - K)
        if E == K + d:
            phit += 1
        elif E < K + d:
            pe_ += 1
        else:
            pl += 1
    npr = phit + pe_ + pl
    if npr:
        print(f"  prime run test: event==K+D: {phit}/{npr} = "
              f"{phit / npr:.3f}, early {pe_}, late {pl}")
    print(f"  prime wait stats: n={len(pwait)} mean={sum(pwait) / len(pwait):.3f}"
          f" median={sorted(pwait)[len(pwait) // 2]} max={max(pwait)}")
    if pD:
        print(f"  prime D stats: n={len(pD)} mean={sum(pD) / len(pD):.3f} "
              f"median={sorted(pD)[len(pD) // 2]} max={max(pD)} "
              f"min={min(pD)}")
    print(f"  wall time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()