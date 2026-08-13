#!/usr/bin/env python3
"""CHT 2026 Theorem 1.6(iii): right-half {0,d}-block scan on the real primes.

Directive 35 item 1.  Theorem 1.6(iii) (verbatim from the source): there does
NOT exist m in 1..M, 2^{M-m} < d <= 2^{M-m+1}, i <= 2 R_{m-1},
k >= R_m - 3 R_{m-1}, and N' <= j <= N-i-k, with
a(i,j), ..., a(i,j+k-1) in {0,d}.  So the {0,d}-block obstruction is confined
to columns j >= N' — the RIGHT HALF — with d >= 2 and depth i <= 2 R_{m-1}.

The run's own leading {0,2} block sits at columns j = 1..b (far left), so it
never violates (iii); the question the scan answers: does the right half of
the REAL prime array contain long {0,d}-blocks with d >= 2, and how do the
observed lengths compare against the CHT thresholds R_m - 3 R_{m-1}?

Coordinates (CHT, arXiv:2607.08712): row 0 = a_n = (p_{n+2}-p_{n+1})/2 - 1
for n = 1..N with N = W-2 (W primes); later rows by absolute differences.
The run's triangle A_k satisfies A_{i+1}[j] = 2*a(i,j) for j >= 1, i >= 1,
so a {0,d}-block in CHT row i is a {0,2d}-block in run row i+1; d = 1 (run
{0,2}) is OUTSIDE (iii) and reported separately for contrast.  Also
b_k = leading {0,1}-prefix length of CHT row k-1 for k >= 2 (b_1 = number of
leading a_n = 0), which gives an oracle cross-check against the stored
block-profile records.

Method per row: compress to the nonzero entries; a maximal {0,d}-block is
the span between the nonzero neighbours of a maximal equal-run of value d
(d >= 2) in the compressed sequence.  Pure zero-runs are excluded (axiom (ii)
covers those).  O(width) per row, one row live at a time.

Complexity: time O(D*W) elementwise int64 ops, space O(W) (sieve bytearray +
one row + masks); no exponential anything, no triangle stored.  Sieve is the
same numpy/bytearray construction as code/pattern_finder/giants_6e8.py.

Oracle checks run before the scan:
  1. naive longest-{0,d}-run (expand around each d position) vs the compressed
     method on 200 random small rows, all d in 2..8, random start columns;
  2. b_k cross-check against blocks_depth1000.json (2e7 run) and
     giants_6e8.json (6e8 run): b_list[j] must equal record b[j+1], and
     b_1 = leading-zero count of row 0;
  3. CHT-vs-run halving: A_{i+1}[j] == 2*a(i,j) for j >= 1 on the first 3
     rows over the first 10^5 primes of the sieve.

Usage:  python3 scan_right_half_0d.py LIMIT DEPTH TAG
  (TAG in {2e7, 6e8} selects the b-profile oracle file)
"""
import json
import os
import sys
import time
from math import isqrt

import numpy as np

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out")
ORACLES = {
    "2e7": os.path.join(OUT_DIR, "blocks_depth1000.json"),
    "6e8": os.path.join(OUT_DIR, "pattern_finder_outputs", "giants_6e8.json"),
}


def longest_run(mask):
    """Length of the longest run of True in a boolean numpy array."""
    if mask.size == 0 or not mask.any():
        return 0
    m = mask.view(np.int8)
    d = np.concatenate(([0], m, [0]))
    dd = np.diff(d)
    sd = np.flatnonzero(dd == 1)
    ed = np.flatnonzero(dd == -1)
    return int((ed - sd).max())


def longest_0d_blocks(row, start_col, d_min, d_max):
    """Maximal {0,d}-blocks of row[start_col:] with d_min <= d <= d_max.

    Returns a list of (length, d, lo, hi), longest first; lo,hi are absolute
    0-based column indices in row.  Every returned block contains at least
    one d (it is the span of a maximal equal-run of d in the compressed
    nonzero sequence), so pure zero-blocks are excluded — axiom (ii) of
    Theorem 1.6 covers those separately.
    """
    out = []
    seg = row[start_col:]
    n = seg.size
    if n <= 0:
        return out
    nz = np.flatnonzero(seg)
    if nz.size == 0:
        return out
    vals = seg[nz]
    ch = np.flatnonzero(np.diff(vals) != 0)
    starts = np.concatenate(([0], ch + 1))
    ends = np.concatenate((ch, [vals.size - 1]))
    for s, e in zip(starts.tolist(), ends.tolist()):
        d = int(vals[s])
        if not (d_min <= d <= d_max):
            continue
        lo = (int(nz[s - 1]) + 1) if s > 0 else 0
        hi = (int(nz[e + 1]) - 1) if e < nz.size - 1 else n - 1
        out.append((hi - lo + 1, d, lo + start_col, hi + start_col))
    out.sort(key=lambda t: t[0], reverse=True)
    return out


def naive_longest_0d_exact(row, start_col, d):
    """Independent oracle: longest interval in row[start_col:] all of whose
    entries lie in {0,d} and containing at least one d (expand around each d
    position).  Pure Python, O(width * #d-positions)."""
    seg = row[start_col:]
    best = 0
    for p in np.flatnonzero(seg == d).tolist():
        lo = p
        while lo > 0 and seg[lo - 1] in (0, d):
            lo -= 1
        hi = p
        while hi < seg.size - 1 and seg[hi + 1] in (0, d):
            hi += 1
        if hi - lo + 1 > best:
            best = hi - lo + 1
    return best


def oracle_naive(trials=200, width=60, seed=12345):
    rng = np.random.default_rng(seed)
    for t in range(trials):
        w = int(rng.integers(5, width))
        row = rng.integers(0, 9, size=w)
        sc = int(rng.integers(0, w))
        blocks = longest_0d_blocks(row, sc, 2, 8)
        by_d = {}
        for b in blocks:
            by_d.setdefault(b[1], b[0])
        for d in range(2, 9):
            naive = naive_longest_0d_exact(row, sc, d)
            got = by_d.get(d, 0)
            if got != naive:
                print(f"NAIVE MISMATCH trial {t} row={row.tolist()} sc={sc} "
                      f"d={d} compressed={got} naive={naive}")
                return False
    return True


def primes_idx(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    r = isqrt(limit)
    for i in range(2, r + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((limit - i * i) // i) + 1)
    buf = np.frombuffer(sieve, dtype=np.uint8)
    idx = np.nonzero(buf[2:])[0].astype(np.int64) + 2
    del sieve, buf
    return idx


def scan(limit, depth, tag):
    t0 = time.time()
    idx = primes_idx(limit)
    W = int(len(idx))
    N = W - 2                      # number of normalized gaps a_1..a_N
    Np = N // 2                    # N' = floor(N/2) (1-based column threshold)
    sc = Np - 1                    # 0-based first column of the right half
    gaps = np.abs(np.diff(idx))    # gaps[0]=1, gaps[j]=p_{j+2}-p_{j+1} for j>=1
    row0 = gaps[1:] // 2 - 1       # a_n for n = 1..N  (gaps[1:] has N entries)
    amax = int(row0.max())
    M = max(1, (amax - 1).bit_length())
    d_max = 2 ** M                 # (iii) controls d in [2, 2^M]
    L = longest_run(row0 == 0)
    R0 = 100 * L * (8 ** M)
    R1 = 100 * L * (8 ** (2 * M))
    T1 = R1 - 3 * R0
    rec = {"limit": limit, "W": W, "N": N, "Nprime": Np, "depth": depth,
           "amax": amax, "M": M, "L": L, "R0": R0, "T1": T1,
           "d_max_controlled": d_max}
    print(f"sieve {limit}: W={W} N={N} N'={Np} in {time.time()-t0:.1f}s")
    print(f"amax={amax} -> M={M}, L={L}, R_0={R0} (log10 {math.log10(R0):.1f}), "
          f"T_1=R_1-3R_0={T1} (log10 {math.log10(T1):.1f})")

    # --- oracle 3: CHT vs run halving on the first 10^5 primes ---
    small = idx[:100000]
    small_gaps = np.abs(np.diff(small))
    ch0 = small_gaps[1:] // 2 - 1
    ch1 = np.abs(np.diff(ch0))
    ch2 = np.abs(np.diff(ch1))
    # run rows A_2, A_3, A_4: A_k[j] = 2*CHT row k-1, j>=1
    run1 = small_gaps  # A_1
    run2 = np.abs(np.diff(run1))
    run3 = np.abs(np.diff(run2))
    run4 = np.abs(np.diff(run3))
    ok_map = (np.array_equal(run2[1:], 2 * ch1[:run2.size - 1]) or
              np.array_equal(run2[1:], 2 * ch1[:len(run2) - 1])) and \
             np.array_equal(run3[1:], 2 * ch2[:len(run3) - 1]) and \
             np.array_equal(run4[1:], 2 * np.abs(np.diff(ch2))[:len(run4) - 1])
    print(f"oracle halving A_{'{i+1}'}[j]=2*a(i,j) on first 1e5 primes: {ok_map}")
    rec["oracle_halving"] = bool(ok_map)

    # --- row loop: one row live at a time ---
    cur = row0
    best = {"A": None, "B": None, "C": None}   # cat A: 2<=d<=2^M, B: d>=2, C: d==1
    row_best_A = []
    b_list = []
    for i in range(depth + 1):
        if cur.size > sc:
            blocks = longest_0d_blocks(cur, sc, 1, 10 ** 9)
            for b in blocks:
                cat = "A" if 2 <= b[1] <= d_max else ("B" if b[1] >= 2 else "C")
                c = best[cat]
                if c is None or b[0] > c[0]:
                    best[cat] = (b[0], b[1], i, b[2], b[3])
            ab = [b for b in blocks if 2 <= b[1] <= d_max]
            if ab:
                row_best_A.append((i, ab[0][0], ab[0][1], ab[0][2], ab[0][3]))
            else:
                row_best_A.append((i, 0, 0, -1, -1))
        else:
            row_best_A.append((i, 0, 0, -1, -1))
        # leading {0,1} prefix of CHT row i (i >= 1) = b_{i+1} (run's block)
        if i >= 1:
            m = (cur == 0) | (cur == 1)
            b_list.append(int(m.size) if m.all() else int(np.argmax(~m)))
        if i < depth:
            cur = np.abs(np.diff(cur))
        if i % 50 == 0:
            print(f"row {i}: {time.time()-t0:.0f}s", flush=True)
    rec["best_overall"] = {k: v for k, v in best.items()}
    row_best_A.sort(key=lambda t: t[1], reverse=True)
    rec["row_best_A_top"] = row_best_A[:15]
    rec["row_best_A_count"] = len(row_best_A)
    rec["rows_with_A_block"] = sum(1 for r in row_best_A if r[1] > 0)

    # --- b-profile oracle cross-check ---
    jb = json.load(open(ORACLES[tag]))["b"]
    b1 = longest_run(row0 == 0)          # b_1 = leading zeros of a_n
    mism = []
    if jb and b1 != jb[0]:
        mism.append((1, b1, jb[0]))
    for j in range(min(len(b_list), len(jb) - 1)):
        if b_list[j] != jb[j + 1]:
            mism.append((j + 2, b_list[j], jb[j + 1]))
    print(f"oracle b-profile: b_1={b1} record={jb[0] if jb else None}; "
          f"mismatches over rows 2..{min(depth, len(jb))}: {mism}")
    rec["b_oracle_mismatches"] = mism
    rec["b1"] = b1
    rec["time_s"] = round(time.time() - t0, 1)
    return rec


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 600_000_000
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    tag = sys.argv[3] if len(sys.argv) > 3 else "6e8"
    print("oracle naive (compressed vs expand-around-d, 200 random rows):",
          oracle_naive(), flush=True)
    rec = scan(limit, depth, tag)
    print("\n=== RESULTS ===")
    print(json.dumps(rec, indent=1))
    out_json = os.path.join(OUT_DIR, f"cht_right_half_0d_scan_{tag}.json")
    with open(out_json, "w") as f:
        json.dump(rec, f, indent=1)
    print(f"wrote {out_json}")


if __name__ == "__main__":
    main()
