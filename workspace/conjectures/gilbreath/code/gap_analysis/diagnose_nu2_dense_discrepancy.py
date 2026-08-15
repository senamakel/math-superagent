#!/usr/bin/env python3
"""Diagnose why code/out/nu2_dense.txt (from nu2_dense_transfer.py) records
different nu2 values than the task's d[2:-1] convention (reconcile_nu2w /
nu2_vs_gap_parity / linearization_verify).

Task convention (the one being verified):  diag = [rows[k][n-k] for k in rng(n)]
tail = diag[2:-1]; walk back while in {0,2}; nu2 = count of 2s.
Dense-file convention: incremental diagonal D via nu2_dense_transfer.py built as
  D=[P[0]]; for n: newD[0]=P[n-1]; newD[k]=|newD[k-1]-D[k-1]|; then
  cycle_and_nu2(D) from lib.rightdiag.py:
  body = diag[:-1]; i=len(body); while i>2 and body[i-1] in {0,2}: i-=1; cyc=body[i:].

Report both for n in {50,100,200,400,800,1600,3200,3999} and their difference.
Also test whether cycle_and_nu2(diag_task_convention) reproduces reconcile's
values (26,42,...) -- i.e. whether the discrepancy is in the DIAGONAL build
(incremental vs rows[k][n-k]) or in the nu2 extraction convention.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2

BOUND = 60_000
TRI_N = 4001
SPARSE = [50, 100, 200, 400, 800, 1600, 3200, 3999]


def task_nu2(d, n):
    tail = d[2:-1]
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    return tail[i:].count(2)


def main():
    P = primes_up_to(BOUND)
    rows = [P[:TRI_N + 2]]
    for k in range(1, TRI_N):
        prev = rows[-1]
        rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])

    # replicate nu2_dense_transfer.py's incremental diagonal + cycle_and_nu2
    D = [P[0]]
    dense_record = {}
    for n in range(1, TRI_N + 1):
        if n >= 2:
            newD = [0] * n
            newD[0] = P[n - 1]
            for k in range(1, n):
                newD[k] = abs(newD[k - 1] - D[k - 1])
            D = newD
        _, nu2 = cycle_and_nu2(D)
        dense_record[n] = nu2

    print("%-6s %-8s %-8s %-8s %-8s" % (
        "n", "task(d[2:-1])", "dense(incrD)", "cyc(diag)", "dense-file"))
    dense_file = {}
    with open("code/out/nu2_dense.txt") as f:
        for line in f:
            parts = line.split()
            dense_file[int(parts[0])] = int(parts[1])
    for n in SPARSE:
        d = [rows[k][n - k] for k in range(n)]       # task diag
        t = task_nu2(d, n)                            # task convention
        dc = dense_record[n]                          # dense-transfer incr diag
        # cycle_and_nu2 on the TASK diag (same extraction, different diag build)
        tc = cycle_and_nu2(d)[1]
        df = dense_file.get(n, "?")
        print("%-6d %-8d %-8d %-8d %-8s" % (n, t, dc, tc, df))


if __name__ == "__main__":
    main()
