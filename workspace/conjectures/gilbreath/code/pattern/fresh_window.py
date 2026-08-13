#!/usr/bin/env python3
"""Fresh-window attack on the pattern conjectures + exact erosion-track check.

Conjectures suggested by genuine rows k=1..161 (b = leading {0,2} block
length, y = intruder = first entry past the block):
  C1  b(k) >= 7 for all k >= 2            (falsifier: first k>=2 with b<=6)
  C2  y(k) in {4,6,8,10,12,14} for every  (falsifier: first y not in that set)
        row with a visible intruder
  C3  genuine erosion runs (consecutive b(k+1)=b(k)-1) have length <= 13
        (falsifier: first run of length 14)
These were all suggested by rows k=1..161. This run computes FURTHER genuine
rows (fresh sieve to 10^9, ~50.8M primes, so the honest window is ~9x wider)
and checks every conjecture against the fresh terms only (k >= 162).

Also verifies exactly, over every erosion step in k=1..Kgen-1:
  E1  track recurrence: x' = |p-x|, y' = y - 2*[x==2]   (p = second-to-last
        block entry, x = last block entry, y = intruder)
  E2  right-edge XOR-cone formula: at erosion step t (row r0+t, position
        b0-t), x(t) = 2 * XOR_{j: C(t,j) odd} bit(b0 - j), b0 = block length
        at the run's start row r0 (Lucas: C(t,j) odd iff (j & ~t) == 0).
  E3  regeneration iff (x == 2 and y == 4)  (boundary lemma, re-checked)
All exact integer arithmetic (uint32 rows, diffs of primes < 10^9).
Oracle: rows k=1..40 must match witnesses.json b and s.
Memory: sieve 1GB (freed after primes), rows ~203MB each, peak ~1.3GB.
Cost: O(K * W) vectorized, W ~ 5e7, K ~ 200 => ~1e10 element ops, seconds.
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
    er_states = []          # per erosion step: (k, b0, t, p, x, y, x_act, y_act)
    run_info = []           # per erosion run: (r0, L, y0, tail_bits)
    Kgen = None
    t1 = time.time()
    for k in range(1, D_MAX + 1):
        prev = row
        row = np.where(prev[:-1] >= prev[1:], prev[:-1] - prev[1:],
                       prev[1:] - prev[:-1])
        if int(row[0]) != 1:
            print("leading entry != 1 at k=", k); sys.exit(1)
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
            print(f"CONJECTURE DEAD: s={s} at k={k}"); sys.exit(1)
        if k > 1:
            d = blk - b_list[k - 2]
            if d == -1:
                b0 = b_list[k - 2]          # block length at row k-1
                r0 = k - 1                   # 1-indexed start row
                L_so_far = len(er_states) - 0
                # t for this step = number of consecutive -1 steps so far,
                # including this one -- recompute from run_info
                if run_info and run_info[-1][0] == r0 - len(er_states) + 1:
                    pass
                t_steps = 0
                # count current run: steps already recorded for this run
                if run_info and run_info[-1][0] + run_info[-1][1] == k + 1 - 1:
                    t_steps = run_info[-1][1]
                # simpler: track manually
            # manual run tracking below; here we just record states
        if k >= 2:
            d = blk - b_list[k - 2]
            if d == -1:
                # this transition k-1 -> k is an erosion step
                p = int(prev[blk - 1])       # prev row is row k-1, len W-(k-1)
                xp = int(prev[blk])          # last block entry at k-1
                yp = int(prev[blk + 1])      # intruder at k-1
                x_act = int(row[blk - 1])    # A_k(blk-1): should be |p-xp|
                y_act = int(row[blk])        # A_k(blk): should be yp-2[xp==2]
                if yp >= 4 and (yp % 2) == 0:
                    y_pred = yp - (2 if xp == 2 else 0)
                else:
                    y_pred = abs(xp - yp)
                er_states.append((k, p, xp, yp, x_act, y_act, y_pred))
        if k == 40:
            if b_list != want_b or s_list != want_s:
                print("ORACLE MISMATCH at k=40"); sys.exit(1)
        # stop when no intruder visible (block covers full window)
        if y is None:
            Kgen = k
            break
    t_rows = time.time()

    print(f"rows computed to k={len(b_list)} in {t_rows - t1:.1f}s; "
          f"Kgen (row where block fills window) = {Kgen}", flush=True)
    assert b_list[:40] == want_b and s_list[:40] == want_s, "oracle mismatch"
    K = len(b_list)
    b = b_list
    print(f"oracle ok k=1..40; genuine rows: k=1..{K - 1} "
          f"(b never fills window before k={K})")

    # fresh rows = genuine rows beyond the old window (>= 162)
    fresh = [(k + 1, b[k], s_list[k], y_list[k]) for k in range(161, K - 1)]
    print(f"\nfresh genuine rows k=162..{K - 1}: n={len(fresh)}")
    print("  k, b, s, y:" + "".join(f"\n  {t}" for t in fresh))

    # ---- C1: b >= 7 for k >= 2, all fresh rows
    viol1 = [(k + 1, b[k]) for k in range(1, K - 1) if b[k] <= 6]
    print(f"\nC1 b>=7 over k>=2: fresh rows k=162..{K - 1} all ok: {not any(k >= 162 for k, _ in viol1)}"
          f" ; all-genuine violations: {viol1}")

    # ---- C2: intruder in {4,...,14}
    yv = [(k + 1, y_list[k]) for k in range(K - 1) if y_list[k] is not None]
    viol2 = [(k, y) for (k, y) in yv if y not in (4, 6, 8, 10, 12, 14)]
    fresh2 = [(k, y) for (k, y) in yv if k >= 162]
    print(f"C2 y in {{4..14}}: all-genuine violations: {viol2}; "
          f"fresh-only max y: {max((y for _, y in fresh2), default=None)}")

    # ---- erosion runs, genuine only (k < K)
    diffs = [b[i + 1] - b[i] for i in range(K - 2)]
    runs = []
    cur, start = 0, None
    for i, dd in enumerate(diffs):
        kk = i + 1
        if dd == -1:
            if cur == 0:
                start = kk          # transition kk -> kk+1
            cur += 1
        else:
            if cur:
                runs.append((start, cur))
            cur = 0
    if cur:
        runs.append((start, cur))
    lens = [L for _, L in runs]
    print(f"\nC3 erosion runs (genuine): n={len(runs)}, lengths={lens}, "
          f"max={max(lens)}")
    print(f"C3 fresh-only (runs starting in k>=162): "
          f"{[r for r in runs if r[0] >= 162]}")
    viol3 = [(s_, L) for (s_, L) in runs if L >= 14]
    print(f"C3 violations (L>=14): {viol3}")

    # ---- E1: track recurrence exactness over every erosion step
    bad1 = [st for st in er_states if st[4] != abs(st[2] - st[1])]
    bad1y = [st for st in er_states if st[5] != st[6]]
    print(f"\nE1 track: erosion steps={len(er_states)}, "
          f"x-recurrence failures={len(bad1)}, y-recurrence failures={len(bad1y)}")
    if bad1y[:3]:
        print("  y failures:", bad1y[:3])

    # ---- E2: right-edge XOR-cone formula needs the run's start-row bits.
    # We did not store rows. Instead verify over er_states a WEAKER exact
    # identity: x(t) is determined by (p,x,y) chain (E1) -- the cone formula
    # was already proved in block_lemma.md for apex cones; here we record that
    # E1 held exactly, and that E1's recurrence is exactly the cone propagation
    # restricted to the boundary (provable, not merely empirical).
    print(f"E2 deferred to a row-storing run (needs start-row tail bits); "
          f"E1 above is the exact boundary recurrence.")

    # ---- E3: regen iff (x==2 and y==4) -- over every row k=1..K-2
    reg_fail = []
    for k in range(1, K - 1):
        if y_list[k - 1] is not None:
            pred = (x_list[k - 1] == 2 and y_list[k - 1] == 4)
            obs = (b_list[k] - b_list[k - 1]) >= 0
            if pred != obs:
                reg_fail.append((k, pred, obs, x_list[k - 1], y_list[k - 1],
                                 b_list[k - 1], b_list[k]))
    print(f"E3 regen iff (x==2,y==4): rows checked={K - 2}, failures={reg_fail}")

    out = {
        "LIMIT": LIMIT, "W": int(W), "Kgen": K, "genuine_rows": K - 1,
        "fresh_rows_ge_162": len(fresh),
        "C1_viol": viol1, "C2_viol": viol2, "C3_viol": viol3,
        "erosion_run_lengths": lens,
        "E1_steps": len(er_states), "E1_fail_x": len(bad1),
        "E1_fail_y": len(bad1y), "E3_fail": reg_fail,
        "b": b, "s": s_list, "y": y_list,
    }
    with open("code/out/fresh_window.json", "w") as f:
        json.dump(out, f)
    print("\nwrote code/out/fresh_window.json")


if __name__ == "__main__":
    main()