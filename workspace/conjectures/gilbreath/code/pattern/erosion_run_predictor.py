#!/usr/bin/env python3
"""Erosion-run closed-form predictor, tested against the real prime rows.

Model (every component already established by this run):
  - rule90 interior (proved): at erosion depth d from run-start row K with
    halved block bits u[1..n] (n = b_K), row K+d's edge bit is
        edgebit_d = XOR_{j subseteq d} u[n-d+j]
    (Lucas: binom(d,j) odd iff j is a bitwise submask of d).
  - drain law (theorem, from |x-y| at the intruder position): the intruder at
    row K+d is  y_{K+d} = max(4, y_K - 2 * #{t < d : edgebit_t = 1}).
  - step law (theorem): row k is an event row (b_{k+1} >= b_k) iff
    (x_k, y_k) = (2, 4), i.e. iff edgebit_{k-K} = 1 and y_k = 4.
  Predicted next event row after K:
        K + d*,  d* = min{ d >= 1 : edgebit_d = 1 and y_{K+d} = 4 }.
  If no such d (block runs out), the model predicts extinction (no event).

Compared against the actual next event row from the regenerated b record.
The regenerated b[1..161] is cross-checked against the stored genuine record.

Run:  timeout 540 python3 code/pattern/erosion_run_predictor.py 2>&1 |
       tee code/out/erosion_run_predictor.captured.txt
"""
import json
import sys

sys.setrecursionlimit(10000)

from lib.gilbreath import primes_up_to, block_profile  # noqa: E402

SIEVE_LIMIT = 20_000_000
DEPTH = 162          # rows A_0 (primes) .. A_162; live regime is k <= 161


def diff_row(row):
    return [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]


def main():
    primes = primes_up_to(SIEVE_LIMIT)
    W = len(primes)
    print(f"sieve <= {SIEVE_LIMIT}: {W} primes; depth {DEPTH}")

    # ---- generate rows one at a time, keep A_{k-2}, A_{k-1} only ----
    b = [None] * (DEPTH + 1)          # b[k] = block length of row k (k>=1)
    b[0] = None
    p2 = primes                        # A_0
    p1 = diff_row(p2)                  # A_1
    b[1] = block_profile(p1)

    # edgebit_0 = u[n-1] = x_K/2 ; cnt starts there (drain counts row K)
    runs = []                          # list of dicts

    for k in range(2, DEPTH + 1):
        Ak = diff_row(p1)              # A_k
        b[k] = block_profile(Ak)
        d_now = b[k] - b[k - 1]        # diff at transition (k-1) -> k
        d_prev = b[k - 1] - b[k - 2] if k >= 3 else +1   # (k-2) -> (k-1)
        if d_now == -1 and d_prev != -1:
            K = k - 1                  # run starts at row K; row A_K = p1
            n = b[K]
            u = [p1[i] // 2 for i in range(1, n + 1)]    # block bits
            runs.append({
                'K': K, 'n': n,
                'x': p1[n], 'y': p1[n + 1], 'u': u,
            })
        p2, p1 = p1, Ak

    # ---- cross-check b[1..161] against the stored genuine record ----
    stored = json.load(open('code/out/genuine_sequences.json'))
    sb = stored['b']
    ok = all(b[k] == sb[k - 1] for k in range(1, 162))
    print(f"regenerated b[1..161] == stored genuine record: {ok}")

    # ---- model prediction for each run ----
    for r in runs:
        K, n, yK = r['K'], r['n'], r['y']
        u = r['u']
        cnt = u[n - 1]                 # edgebit_0 (row K's own edge)
        dstar = None
        for d in range(1, n):          # d up to n-1 (block must survive d rows)
            s = 0
            sub = d
            while True:                # all submasks of d: odd binom indices
                s ^= u[n - d - 1 + sub]
                if sub == 0:
                    break
                sub = (sub - 1) & d
            y_d = yK - 2 * cnt
            if y_d < 4:
                y_d = 4
            if s == 1 and y_d == 4:
                dstar = d
                break
            cnt += s
        r['dstar'] = dstar
        r['pred_event'] = K + dstar if dstar is not None else None
        # actual first event row after K (diff >= 0)
        act = None
        for kp in range(K + 1, DEPTH):
            if b[kp + 1] - b[kp] >= 0:
                act = kp
                break
        r['act_event'] = act
        r['match'] = (r['pred_event'] == act)

    # ---- report ----
    n_run = len(runs)
    n_match = sum(1 for r in runs if r['match'])
    print(f"live erosion runs detected: {n_run}; predicted next-event row "
          f"matches actual: {n_match}/{n_run}")
    print("K   n(b_K)   y_K x_K  runlen  d*  pred_event  act_event  match")
    for r in runs:
        runlen = r['act_event'] - r['K'] if r['act_event'] else None
        print(f"{r['K']:4d} {r['n']:9d} {r['y']:3d} {r['x']:2d} "
              f"{runlen:6} {r['dstar']:6} {r['pred_event']:11} "
              f"{r['act_event']:10}  {r['match']}")
    if n_match == n_run:
        print("EROSION-RUN MODEL: zero failures over all live runs")
    else:
        bad = [r['K'] for r in runs if not r['match']]
        print(f"EROSION-RUN MODEL: MISMATCHES at run starts {bad}")

    # ---- derived sequences for the record ----
    # s (second entries) at powers of two
    sj = json.load(open('code/out/blocks_depth1000.json'))
    s1000 = sj['s']
    print("s at k = 2^j: " + ", ".join(
        f"k={2**j}:{s1000[2**j - 1]}" for j in range(0, 10)))
    # erosion run lengths + inter-event gaps (recomputed)
    gaps = []
    runlens = []
    i = 1
    while i <= 161:
        if b[i + 1] - b[i] >= 0:
            gaps.append(b[i + 1] - b[i])
            i += 1
        else:
            L = 0
            while i + L <= 161 and b[i + L + 1] - b[i + L] == -1:
                L += 1
            runlens.append(L)
            i += L
    print(f"erosion run lengths (live): {runlens}")
    print(f"inter-event jumps (live, incl stalls): {gaps}")

    # local minima of b over k=1..161 (strict: b[k]<b[k-1], b[k]<=b[k+1])
    mins = []
    for k in range(2, 161):
        if b[k] < b[k - 1] and b[k] <= b[k + 1]:
            mins.append((k, b[k]))
    print(f"local minima of b, k=1..161: {[(k, v) for k, v in mins]}")
    print("local-minima b values:",
          [v for _, v in mins])


if __name__ == '__main__':
    main()