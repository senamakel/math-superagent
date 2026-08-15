#!/usr/bin/env python3
"""Exhaustive machine check that the two's-complement carry bridge
(3-state MSB comparator x 2-state LSB borrow-subtractor, a-b = a+~b+1)
equals |a-b| for ALL 0<=a,b<2^14.

The transducer is implemented here as the exact boolean bit-steps (comparator
MSB-first, then borrow chain LSB-first), vectorized over batches of the (a,b)
grid with numpy uint8. The independent reference is numpy's |a-b| on the same
batch. Two different routes to the same value, over the full 2^28 grid.

Also cross-checks lib.carry.absdiff_transducer (the per-pair reusable
function) against Python's int-abs on a random subset.

Cost: 2^28 pairs, m=14 bits, batched; runs in well under a minute, one batch
of arrays live at a time.
"""
import numpy as np
from lib.carry import absdiff_transducer

M = 14
N = 1 << M          # 16384
TOTAL = N * N       # 2^28
GRID = 64           # 64x64 = 4096 pairs per tile


def bits_lsb_matrix(values, m):
    """Shape (m, len(values)) uint8 array of LSB-first bits of values."""
    v = np.asarray(values, dtype=np.uint64)
    out = np.empty((m, v.size), dtype=np.uint8)
    for i in range(m):
        out[i] = (v >> i) & 1
    return out


def transducer_batch(a_arr, b_arr, m):
    """Vectorized composed transducer over equal-length arrays a_arr, b_arr.
    Returns |a-b| for each pair as uint64 (= the exact integer)."""
    a = np.asarray(a_arr, dtype=np.uint64)
    b = np.asarray(b_arr, dtype=np.uint64)
    n = a.size
    Ab = bits_lsb_matrix(a, m)
    Bb = bits_lsb_matrix(b, m)
    gt = np.zeros(n, dtype=np.uint8)   # a > b
    lt = np.zeros(n, dtype=np.uint8)   # b > a
    for i in range(m - 1, -1, -1):
        x = Ab[i]
        y = Bb[i]
        gt |= (x > y) & ~(gt | lt)
        lt |= (y > x) & ~(gt | lt)
    # magnitude: larger minus smaller via two's-complement X + ~Y + 1 borrow
    # chain (a subtraction borrow = an addition carry).
    X = np.where(lt == 1, b, a)          # larger operand
    Y = np.where(lt == 1, a, b)          # smaller operand
    Xb = bits_lsb_matrix(X, m)
    Yb = bits_lsb_matrix(Y, m)
    out = np.zeros(n, dtype=np.uint64)
    c = np.zeros(n, dtype=np.uint8)
    for i in range(m):
        s = Xb[i] + (1 - Yb[i]) + c
        out |= (s.astype(np.uint64) & 1) << i
        c = (s >= 2).astype(np.uint8)
    return out


def reference_batch(a_arr, b_arr):
    return np.abs(np.asarray(a_arr, dtype=np.int64)
                  - np.asarray(b_arr, dtype=np.int64))


def main():
    mismatches = 0
    first = None
    for a_start in range(0, N, GRID):
        a_rows = np.arange(a_start, min(a_start + GRID, N),
                           dtype=np.uint64)
        for b_start in range(0, N, GRID):
            b_cols = np.arange(b_start, min(b_start + GRID, N),
                               dtype=np.uint64)
            aa = np.repeat(a_rows, b_cols.size)
            bb = np.tile(b_cols, a_rows.size)
            got = transducer_batch(aa, bb, M)
            ref = reference_batch(aa, bb)
            bad = np.flatnonzero(got != ref)
            if bad.size:
                mismatches += int(bad.size)
                if first is None:
                    i = int(bad[0])
                    first = (int(aa[i]), int(bb[i]), int(got[i]), int(ref[i]))

    rng = np.random.default_rng(0)
    sub_a = rng.integers(0, N, 4000)
    sub_b = rng.integers(0, N, 4000)
    lib_bad = 0
    for x, y in zip(sub_a, sub_b):
        if absdiff_transducer(int(x), int(y), M) != abs(int(x) - int(y)):
            lib_bad += 1

    print("two's-complement carry bridge |a-b| exhaustive check")
    print("m=%d bits, grid 0<=a,b<%d = %d (a,b) pairs" % (M, N, TOTAL))
    print("vectorized transducer == numpy |a-b|: %s" % (
        "ALL %d MATCH" % TOTAL if mismatches == 0
        else "MISMATCHES=%d" % mismatches))
    if first:
        print("  first mismatch a=%d b=%d transducer=%d true=%d" % first)
    print("per-pair lib.carry.absdiff_transducer vs int-abs on 4000 random "
          "pairs: %d mismatches" % lib_bad)
    ok = (mismatches == 0 and lib_bad == 0)
    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    main()
