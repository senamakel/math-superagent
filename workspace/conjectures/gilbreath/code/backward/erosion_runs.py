#!/usr/bin/env python3
"""Extract every erosion run (maximal stretch of rows with b_{k+1} = b_k - 1)
from a Gilbreath prime triangle, and verify the REG-intruder-drains claim.

For each erosion run we report (all exact ints):
    y_0  : intruder A_k(b_k+1) at the run's first row
    y_f  : intruder at the run's last row (the row where erosion stops)
    flips: number of erosion steps in the run where the edge A_k(b_k) == 2
    d    : run length = number of erosion transitions
    b    : initial block length b_k0
    nonzero: whether the leading block A_k(1..b_k) at the run's last row
             contains a value != 0 (i.e. contains a 2)

Checks (must be zero violations):
  (i)   drain-law identity: flips == (y_0 - y_f)/2 on every run
  (ii)  REG-intruder-drains: y_f == 4 with b >= 1 and nonzero block in
        every run (target; equals y_f==4 && nonzero-block && b>=1)

The generator uses numpy (exact int64; entries in these prime triangles
stay bounded by the max prime gap, well within int64) and keeps one row
alive at a time: O(depth x width) time, O(width) memory.
"""
import json
import sys
import numpy as np


def primes_bool_sieve(n):
    """numpy boolean sieve up to n; returns boolean array is_prime[0..n]."""
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    lim = int(n ** 0.5)
    for p in range(2, lim + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return sieve


def row_iter_from_bool(sieve):
    """Yield successive rows as numpy int64 arrays (row = |prev[i]-prev[i+1]|).
    sieve must be the boolean array over [0..N] of primes. First row = primes."""
    idx = np.nonzero(sieve)[0].astype(np.int64)
    row = idx
    yield row
    while len(row) > 1:
        row = np.abs(row[:-1] - row[1:])
        yield row


def extract_rows_gen(sieve, depth):
    """Yields dicts {b, edge, intruder, nonzero} for rows 0..depth inclusive.
    Uses b from the {0,2} leading block, edge = A_k(b_k), intruder = A_k(b_k+1),
    nonzero = block A_k(1..b_k) contains a nonzero entry."""
    gen = row_iter_from_bool(sieve)
    for k in range(depth + 1):
        row = next(gen)
        body = row[1:]
        # leading block: vectorised count of consecutive entries in {0,2}
        valid = (body == 0) | (body == 2)
        if valid.size == 0:
            bad = np.zeros(0, dtype=bool)
        else:
            bad = ~valid
        first_bad = np.argmax(bad) if bad.size and np.any(bad) else body.size
        b = int(first_bad)
        edge = int(row[b])     # block is nonempty (b>=1 always in this data)
        intr = row[b + 1] if b + 1 < len(row) else None
        # nonzero block: any entry in row[1:b+1] != 0
        if b >= 1:
            nr = int(np.any(row[1:b + 1] != 0))
        else:
            nr = 0
        yield {"b": int(b), "edge": int(edge), "intruder": intr,
               "nonzero": nr}


def extract_erosion_runs(rows):
    """rows = list of dicts from extract_rows_gen. Returns list of runs."""
    n = len(rows)
    runs = []
    k = 0
    while k < n - 1:
        # only consider runs while an intruder exists (real regime);
        # once the block reaches the right edge there is no intruder to drain
        if (rows[k + 1]["b"] == rows[k]["b"] - 1
                and rows[k]["intruder"] is not None
                and rows[k + 1]["intruder"] is not None):
            # start of an erosion run at transition k->k+1
            k0 = k
            d = 0
            while (k0 + d < n - 1
                   and rows[k0 + d + 1]["b"] == rows[k0 + d]["b"] - 1
                   and rows[k0 + d + 1]["intruder"] is not None):
                d += 1
            kf = k0 + d  # last row of the run (erosion stops here)
            run = {
                "k0": k0, "kf": kf, "d": d,
                "y0": rows[k0]["intruder"],
                "yf": rows[kf]["intruder"],
                "b0": rows[k0]["b"],
                "b_final": rows[kf]["b"],
                "nonzero": rows[kf]["nonzero"],
                # flips: edge==2 over the d erosion steps rows k0..k0+d-1
                "flips": sum(1 for i in range(k0, k0 + d) if rows[i]["edge"] == 2),
            }
            runs.append(run)
            # run occupied transitions k0..kf-1; start next scan after kf
            k = kf
        else:
            k += 1
    return runs


def check_runs(runs, label):
    drain_viol = [r for r in runs if r["flips"] != (r["y0"] - r["yf"]) / 2]
    target_viol = [r for r in runs if not (r["yf"] == 4 and r["b_final"] >= 1
                                           and r["nonzero"] == 1)]
    print(f"== {label} ==")
    print(f"  runs: {len(runs)}")
    print(f"  drain-law violations (flips != (y0-yf)/2): {len(drain_viol)}")
    print(f"  REG-intruder-drains violations (yf!=4 or b_final<1 or zero block): "
          f"{len(target_viol)}")
    if drain_viol:
        for r in drain_viol[:10]:
            print("   DRAIN-VIOL", r)
    if target_viol:
        for r in target_viol[:10]:
            print("   TARGET-VIOL", r)
    if runs:
        maxy0 = max(r["y0"] for r in runs)
        maxyf = max(r["yf"] for r in runs)
        maxflip = max(r["flips"] for r in runs)
        reach4 = sum(1 for r in runs if r["yf"] == 4)
        print(f"  max intruder y0 over runs: {maxy0}")
        print(f"  max final intruder yf over runs: {maxyf}")
        print(f"  max edge-2 flip count over runs: {maxflip}")
        print(f"  runs reaching yf=4: {reach4} / {len(runs)}")
        all_y0_le14 = all(r["y0"] <= 14 for r in runs)
        print(f"  all y0 <= 14: {all_y0_le14}")
        if all_y0_le14:
            print(f"  (=> every run needs at most {maxflip} edge-2 flips)")
    print()
    return drain_viol, target_viol, runs


def main():
    # --- depth-1000 record (sieve 2e7): real regime while intruder exists ---
    sieve = primes_bool_sieve(20_000_000)
    rows = list(extract_rows_gen(sieve, 1000))
    # oracle: my rows[i] = A_i ; record ref[i] = A_{i+1}
    ref = json.load(open("code/out/blocks_depth1000.json"))
    n = len(ref["b"])
    b_ok = all(rows[i + 1]["b"] == ref["b"][i] for i in range(n))
    int_ok = all((rows[i + 1]["intruder"] == ref["intruder"][i])
                 for i in range(n))
    print(f"oracle: reproduce blocks_depth1000 b: {b_ok}  intruder: {int_ok}")
    # runs over A_1..A_247 (indices 1..247), real regime = while intruder exists
    runs = extract_erosion_runs(rows[:248])
    check_runs(runs, "depth-1000 record (sieve 2e7), A_1..A_247")

    # --- 6e8 giants record, real regime A_1..A_247 ---
    try:
        s6 = primes_bool_sieve(600_000_000)
    except MemoryError:
        print("sieve 6e8 MemoryError -> skipped")
        s6 = None
    if s6 is not None:
        rows6 = list(extract_rows_gen(s6, 247))
        runs6 = extract_erosion_runs(rows6[:248])
        check_runs(runs6, "6e8 giants record, A_1..A_247")

    # --- 1e9 giants record, real regime A_1..A_247 ---
    try:
        s9 = primes_bool_sieve(1_000_000_000)
    except MemoryError:
        print("sieve 1e9 MemoryError -> skipped")
    else:
        rows9 = list(extract_rows_gen(s9, 247))
        runs9 = extract_erosion_runs(rows9[:248])
        check_runs(runs9, "1e9 giants record, A_1..A_247")


if __name__ == "__main__":
    main()
