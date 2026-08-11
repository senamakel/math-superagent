#!/usr/bin/env python3
"""extend_f2.py — extend the trusted f_n(k) data to n=12 and n=13.

Uses the verified cycle-type decomposition method (f_n_method2 from
verify_f_method2.py), an independent exact-integer route that reproduces
extend_f.json rows n=2..11. Each row is
    f_n(k) = #{(pi,i): 0<=i<n!, (pi^i)(k) < (pi^i)(0)}  for k=1..n-1,
from which A_n = f_n(1) and B_n = f_n(2)-f_n(1).

Per-n wall gate: WALL_GATE seconds (~6 hours). If a single n exceeds the
gate it is abandoned (its partial progress is NOT trusted — only a completed
row is saved). Runs n=12 first; n=13 is attempted only after n=12 completes.

Saves incremental results to out/extend_f2.json as {n: [f(1),..,f(n-1)]} and
prints A_n, B_n and first/second differences (zero 2nd diff => exactly
arithmetic in k).

Run (background):  nohup python extend_f2.py > out/extend_f2.log 2>&1 &
"""
import itertools
import json
import math
import os
import time

from verify_f_method2 import f_n_method2

WALL_GATE = 6 * 3600      # ~6 hours per n
OUT_PATH = os.path.join("out", "extend_f2.json")


def load_existing():
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as fh:
            return json.load(fh)
    return {}


def save(data):
    os.makedirs("out", exist_ok=True)
    with open(OUT_PATH, "w") as fh:
        json.dump(data, fh)


def diffs(row):
    """First then second differences of a row (for the arithmetic check)."""
    d1 = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
    return d1, d2


def run_one(n):
    t0 = time.time()
    row = f_n_method2(n)
    return row, time.time() - t0


def main():
    data = load_existing()
    targets = [12, 13]
    for n in targets:
        if str(n) in data:
            print(f"n={n}: already present, skipping", flush=True)
            continue
        print(f"=== starting n={n} wall gate {WALL_GATE}s ===", flush=True)
        t_start = time.time()
        row = None
        try:
            row, dt = run_one(n)
        except Exception as exc:
            print(f"n={n}: EXCEPTION {exc!r}", flush=True)
            row = None
        elapsed = time.time() - t_start
        if row is None or elapsed > WALL_GATE:
            print(f"n={n}: ABANDONED (elapsed {elapsed:.1f}s > gate). "
                  f"Not saved.", flush=True)
            # per-n wall gate exceeded: do not attempt the next, larger n
            if n == 12:
                print("n=12 exceeded gate -> n=13 not attempted", flush=True)
            continue
        data[str(n)] = row
        save(data)
        A, B = row[0], row[1] - row[0]
        d1, d2 = diffs(row)
        print(f"n={n}: time {dt:.1f}s (wall {elapsed:.1f}s)", flush=True)
        print(f"  row = {row}", flush=True)
        print(f"  A_n = f(1)   = {A}", flush=True)
        print(f"  B_n = f(2)-f(1) = {B}", flush=True)
        print(f"  1st diff = {d1}", flush=True)
        print(f"  2nd diff = {d2}   (all zero => exactly arithmetic)",
              flush=True)
        # resume timing / next target immediately
    print("=== extend_f2.py done. out/extend_f2.json ==", flush=True)
    print(json.dumps(load_existing(), indent=2), flush=True)


if __name__ == "__main__":
    main()
