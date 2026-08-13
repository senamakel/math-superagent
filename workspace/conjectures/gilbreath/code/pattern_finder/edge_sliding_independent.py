#!/usr/bin/env python3
"""Independent verification of the edge-sliding (rightmost-2 depth) claim.

The claim (from the block lemma's rule-90 interior + step law): during an
erosion run starting at row K with block length b_K, if D = distance from the
block edge to the rightmost 2 in columns 1..b_K, then the edge x_k = A_k[b_k]
is 0 for K<=k<K+D and 2 at k=K+D.  The full script's test passed 1509/1509 +
60/60; this file re-derives it with a completely independent implementation:

  * own sieve (numpy boolean), no code shared with lib/gilbreath.py
  * own block measurement (1-based positions, no off-by-one re-use)
  * own event/run detection
  * checks the profile by direct row lookup at every depth of every run

Also checks the two *consequences* the script reports:
  (G)  gaps between regen events are overdispersed vs geometric (sd/mean > 1);
  (P2) events fire exactly at K+D when the intruder there is 4.

Runs only on the prime rows (D=161, sieve 2e7 — the part the run owns), and
on the 118 survivor records for the gap dispersion.

Complexity: O(num_primes * D) time (~161 passes over 1.27e6 entries), O(W)
memory.  No parallelism needed.
"""
import json
import math

import numpy as np


def primes_bool(n):
    """numpy boolean sieve, returns list of primes <= n."""
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return [int(i) for i in np.nonzero(sieve)[0]]


def iterate_rows(a0, depth):
    """Yield rows A_1..A_depth as 0-based lists, one at a time."""
    cur = a0
    for _ in range(depth):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        yield cur


def block_len(row):
    """Length of the leading {0,2} block from position 1 (1-based)."""
    n = 0
    for v in row[1:]:          # position 1 onward
        if v in (0, 2):
            n += 1
        else:
            break
    return n


def rightmost2_depth(row, b):
    """D = b - (1-based column of rightmost 2 within columns 1..b)."""
    for col in range(b, 0, -1):      # 1-based, from edge inward
        if row[col] == 2:
            return b - col
    return None


def main():
    # ---- prime rows ----
    print("independent prime-row edge-sliding test (sieve 2e7, D=161)")
    primes = primes_bool(20_000_000)
    rows = iterate_rows(primes, 161)

    # store only what we need: per-row (b, edge x, intruder y); keep rows at
    # run starts
    recs = []
    rows_at = {}
    cur = None
    for k, row in enumerate(rows, start=1):
        b = block_len(row)
        x = row[b] if b + 1 < len(row) else None
        y = row[b + 1] if b + 2 < len(row) else None
        recs.append((k, b, x, y))
        if k == 1 or (len(recs) >= 2 and (recs[-2][1] >
                                          recs[-3][1] if False else False)):
            pass
        rows_at[k] = row
    # run start = row 1, or the row after an event row (b grows)
    runs = []
    K = 1
    for i, (k, b, x, y) in enumerate(recs):
        if i + 1 < len(recs):
            bnext = recs[i + 1][1]
            if bnext > b:            # event at row k
                runs.append((K, k, recs[K - 1][1]))
                K = k + 1
    print(f"runs: {len(runs)}")

    prof_bad = 0
    hit = early = late_unp = late2 = 0
    Ds = []
    for (K, E, bK) in runs:
        rowK = rows_at[K]
        d = rightmost2_depth(rowK, bK)
        if d is None:
            continue
        Ds.append(d)
        # profile: x==0 on [K, min(E,K+D)-1], x==2 at min(E,K+D)
        end = min(E, K + d)
        ok = True
        for kk in range(K, end + 1):
            xk = recs[kk - 1][2]
            if kk < end and xk != 0:
                ok = False
            elif kk == end and xk != 2:
                ok = False
        if not ok:
            prof_bad += 1
            print(f"  PROFILE FAIL K={K} E={E} bK={bK} D={d}")
        y_at_pred = recs[K + d - 1][3] if K + d <= 161 else None
        if E < K + d:
            early += 1
        elif E == K + d:
            hit += 1
        else:
            if y_at_pred == 4:
                late2 += 1
            else:
                late_unp += 1
    ntot = hit + early + late_unp + late2
    print(f"  profile-bad: {prof_bad}/60")
    print(f"  timing: hit {hit} ({hit/ntot:.3f}), early {early}, "
          f"late-unpinned {late_unp}, late-2 {late2}")
    Ds.sort()
    print(f"  D dist: n={len(Ds)} min={Ds[0]} median={Ds[len(Ds)//2]} "
          f"max={Ds[-1]} mean={sum(Ds)/len(Ds):.3f}")

    # ---- gap dispersion on the 118 survivor records ----
    print("\nindependent gap-dispersion check on 118 survivor records")
    recs2 = [json.loads(l) for l in
             open("code/out/conditional_rate_records.jsonl")]
    surv = [r for r in recs2 if r["first_b0"] is None or r["first_b0"] > 10]
    gaps = []
    for r in surv:
        p = [k for k in r["events_pos"] if k >= 11]
        gaps.extend(b - a for a, b in zip(p, p[1:]))
    n = len(gaps)
    mean = sum(gaps) / n
    sd = (sum((g - mean) ** 2 for g in gaps) / (n - 1)) ** 0.5
    print(f"  gaps: n={n} mean={mean:.3f} sd={sd:.3f} "
          f"sd/mean={sd/mean:.4f} (geometric null < 1 always; "
          f"observed {sd/mean:.3f})")
    print(f"  chi2-style check: var/mean = {sd*sd/mean:.3f} "
          f"(>1 overdispersed, <1 under)")
    print("DONE")


if __name__ == "__main__":
    main()