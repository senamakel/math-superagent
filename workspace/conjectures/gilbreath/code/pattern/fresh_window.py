#!/usr/bin/env python3
"""Fresh-window attack on the pattern conjectures + exact erosion-track check.

Conjectures suggested by genuine rows k=1..161 (b = leading {0,2} block
length, y = intruder = first entry past the block):
  C1  b(k) >= 7 for all k >= 2            (falsifier: first k>=2 with b<=6)
  C2  y(k) in {4,6,8,10,12,14} for every row with a visible intruder
        (falsifier: first y not in that set)
  C3  genuine erosion runs (consecutive b(k+1)=b(k)-1) have length <= 13
        (falsifier: first run of length 14)
These were all suggested by rows k=1..161. This run computes FURTHER genuine
rows (fresh sieve to 10^9, ~50.8M primes -> honest window ~9x wider) and
checks every conjecture against the fresh terms only (k >= 162).

Also verifies exactly, over every erosion step in the computed window:
  E1  track recurrence: x' = |p-x|, y' = y - 2*[x==2]  (p = second-to-last
        block entry, x = last block entry, y = intruder at the row above)
  E3  regeneration iff (x == 2 and y == 4)   (boundary lemma, re-checked)
Exact integer arithmetic (uint32 rows; differences of primes < 10^9 exact).
Oracle: rows k=1..40 must match witnesses.json b and s; refuse otherwise.
Memory: sieve 1GB (freed after primes), rows ~203MB each, peak ~1.6GB.
Cost: O(K*W) vectorized, W ~ 5e7, K <= 260.
"""
import json
import sys
import time

import numpy as np

LIMIT = 1_000_000_000
D_MAX = 260


def main():
    t0 = time.time()
    sieve = bytearray(b"\x01") * LIMIT
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i < LIMIT:
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((LIMIT - 1 - i * i) // i) + 1)
        i += 1
    primes = np.nonzero(np.frombuffer(sieve, dtype=np.uint8))[0].astype(np.uint32)
    del sieve
    W = int(len(primes))
    print(f"sieve: {W} primes below {LIMIT} in {time.time() - t0:.1f}s", flush=True)

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    want_b = [e["block"] for e in wit["block_profile_first_40"]]
    want_s = [e["second"] for e in wit["block_profile_first_40"]]

    row = primes
    b_list, s_list, y_list, x_list = [], [], [], []
    er_states = []      # per erosion transition k-1->k: (k, p, x, y, x_act, y_act, y_pred)
    Kgen = None
    t1 = time.time()
    for k in range(1, D_MAX + 1):
        prev = row
        row = np.where(prev[:-1] >= prev[1:], prev[:-1] - prev[1:],
                       prev[1:] - prev[:-1])
        if int(row[0]) != 1:
            print("leading entry != 1 at k=", k)
            sys.exit(1)
        s = int(row[1])
        sel = row[1:]
        in02 = (sel == 0) | (sel == 2)
        if bool(in02.all()):
            blk = int(len(sel))
            y = None
            x = None
        else:
            blk = int(np.argmax(~in02))
            x = int(sel[blk - 1])
            y = int(sel[blk])
        b_list.append(blk)
        s_list.append(s)
        y_list.append(y)
        x_list.append(x)
        if s not in (0, 2):
            print(f"CONJECTURE DEAD: s={s} at k={k}")
            sys.exit(1)
        if k >= 2:
            b_prev = b_list[k - 2]          # block length of row k-1
            d = blk - b_prev
            if d == -1:
                # erosion transition k-1 -> k: uses last two block entries and
                # the intruder of row k-1 (row `prev`, length W-(k-1)).
                # prev block = prev[1..b_prev]; x = prev[b_prev], y = prev[b_prev+1]
                if b_prev + 1 < len(prev):  # y visible in prev
                    p = int(prev[b_prev - 1])
                    xp = int(prev[b_prev])
                    yp = int(prev[b_prev + 1])
                    # row k has block length b_prev-1: new last block entry at
                    # position b_prev-1, new intruder at position b_prev
                    x_act = int(row[b_prev - 1])
                    y_act = int(row[b_prev])
                    y_pred = yp - (2 if xp == 2 else 0)
                    er_states.append((k, p, xp, yp, x_act, y_act, y_pred))
        if k == 40:
            if b_list != want_b or s_list != want_s:
                print("ORACLE MISMATCH at k=40: got b[:40]=", b_list)
                sys.exit(1)
        if y is None:                      # block covers whole finite window
            Kgen = k
            break
    t_rows = time.time()

    print(f"rows computed to k={len(b_list)} in {t_rows - t1:.1f}s; "
          f"Kgen (first full-window row) = {Kgen}", flush=True)
    assert b_list[:40] == want_b and s_list[:40] == want_s, "oracle mismatch"
    K = len(b_list)
    b = b_list
    print(f"oracle ok k=1..40; genuine rows: k=1..{K - 1}")

    fresh = [(k + 1, b[k], s_list[k], y_list[k]) for k in range(161, K - 1)]
    print(f"\nfresh genuine rows k=162..{K - 1}: n={len(fresh)}")
    print("  k, b, s, y:")
    for t in fresh:
        print("   ", t)

    # ---- C1: b >= 7 for k >= 2 over genuine rows (k=2..K-1)
    viol1 = [(k + 1, b[k]) for k in range(1, K - 1) if b[k] <= 6]
    fresh1 = [(k + 1, b[k]) for k in range(161, K - 1) if b[k] <= 6]
    print(f"\nC1 b>=7 (k>=2): all-genuine violations={viol1}, "
          f"fresh-only violations={fresh1}")

    # ---- C2: intruder in {4,...,14}
    yv = [(k + 1, y_list[k]) for k in range(K - 1) if y_list[k] is not None]
    viol2 = [(k, y) for (k, y) in yv if y not in (4, 6, 8, 10, 12, 14)]
    fresh2 = [(k, y) for (k, y) in yv if k >= 162]
    print(f"C2 y in {{4..14}}: violations={viol2}; "
          f"n fresh rows with intruder={len(fresh2)}, "
          f"fresh y values={sorted(set(y for _, y in fresh2))}")

    # ---- erosion runs, genuine only (transitions k=1..K-2)
    diffs = [b[i + 1] - b[i] for i in range(K - 2)]
    runs = []
    cur, start = 0, None
    for i, dd in enumerate(diffs):
        kk = i + 1                       # transition kk -> kk+1
        if dd == -1:
            if cur == 0:
                start = kk
            cur += 1
        else:
            if cur:
                runs.append((start, cur))
            cur = 0
    if cur:
        runs.append((start, cur))
    lens = [L for _, L in runs]
    print(f"\nC3 erosion runs (genuine): n={len(runs)}, "
          f"lengths={lens}, max={max(lens)}")
    fresh3 = [r for r in runs if r[0] >= 162]
    print(f"C3 fresh-only runs (start k>=162): {fresh3}")
    viol3 = [(s_, L) for (s_, L) in runs if L >= 14]
    print(f"C3 violations (L>=14): {viol3}")

    # ---- E1: track recurrence over every recorded erosion step
    bad1x = [st for st in er_states if st[4] != abs(st[2] - st[1])]
    bad1y = [st for st in er_states if st[5] != st[6]]
    print(f"\nE1 track: erosion steps={len(er_states)}, "
          f"x failures={len(bad1x)}, y failures={len(bad1y)}")
    if bad1y[:3]:
        print("  y failures:", bad1y[:3])

    # ---- E3: regen iff (x==2 and y==4) at row k-1, over k=2..K-1
    reg_fail = []
    for k in range(2, K):
        if y_list[k - 2] is not None:            # intruder visible at row k-1
            pred = (x_list[k - 2] == 2 and y_list[k - 2] == 4)
            obs = (b_list[k - 1] - b_list[k - 2]) >= 0
            if pred != obs:
                reg_fail.append((k - 1, pred, obs, x_list[k - 2],
                                 y_list[k - 2], b_list[k - 2], b_list[k - 1]))
    print(f"E3 regen iff (x==2,y==4): rows checked={K - 2}, failures={reg_fail}")

    out = {
        "LIMIT": LIMIT, "W": int(W), "Kgen": K, "genuine_rows": K - 1,
        "fresh_rows_ge_162": len(fresh),
        "C1_viol": viol1, "C2_viol": viol2, "C3_viol": viol3,
        "erosion_run_lengths": lens,
        "E1_steps": len(er_states), "E1_fail_x": len(bad1x),
        "E1_fail_y": len(bad1y), "E3_fail": reg_fail,
    }
    with open("code/out/fresh_window.json", "w") as f:
        json.dump(out, f)
    print("\nwrote code/out/fresh_window.json")


if __name__ == "__main__":
    main()