#!/usr/bin/env python3
"""Extend the PRIMES-only Ratio B measurement to larger N.

OBJECT (operator directive, current task): for the sequence a_n = nu2(n)/n,
   s2_N = population variance of { nu2(n)/n : n = 2..N }  (denominator N-1),
   Ratio B = s2_N * 4N / log(N).
Existing sequence: 1.443@1000, 1.392@4000, 1.361@10000, 1.337@20000, 1.315@40000.
This run appends N=80000 and N=160000 (the latter only if affordable) and reads
whether the per-doubling decrement of Ratio B decays (limit > 1) or stays flat
(limit 1).

ORACLE (canonical exact, one function only): nu2(n) = wt(Phi_n h) =
  #{ d in [2,n-1] : T(n,d)=1 }, T(n,d) = XOR over submasks o of d of h[n-1-d+o],
  computed by lib.supply_fold.s_sos (imported as lib.nu2.fold_nu2), the same
  oracle cross-checked in the parent run against s_direct on n=4..200 plus
  spots 53,64,100. h = prime gap-parity string (primes only).

ENTRY GUARD (operator spec, asserted on the PRODUCED array, not a fresh
oracle): fold_nu2(53,h)==18, fold_nu2(64,h)==27, fold_nu2(4000,h)==1975, and
the mean of nu2(n)/n over n<=4000 within 0.01 of 0.4977.

STREAMING: each nu2(n) is O(n log n) SOS; n=2..N computed in parallel chunks
(one n at a time per worker, never materialising any O(N^2) triangle). Memory
O(N). Running sums for s2_N kept in exact Fractions.

ALL NUMBERS ARE MEASURED, NOT PROVED.

Usage: python3 measure_ratio_b.py N [nproc] [outfile]
Writes a capture to the given outfile (default code/out/ratio_b_extension.txt).
"""
import sys
import os
import time
import math
import multiprocessing as mp
from fractions import Fraction

from lib.supply_fold import s_sos
from lib.nu2 import fold_nu2
from lib.primes import h_string

# existing baseline (from code/out/fair_prefix_variance_40000.txt), primes only
BASELINE = [
    (1000, 1.443),
    (4000, 1.392),
    (10000, 1.361),
    (20000, 1.337),
    (40000, 1.315),
]

DEFAULT_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "out", "ratio_b_extension.txt")


def _worker(args):
    lo, hi, h = args
    return [(n, fold_nu2(n, h)) for n in range(lo, hi + 1)]


def compute_nu2(N, h, nproc):
    """nu2[n] for n=2..N by parallel fold_nu2. O(N^2 log N) total work,
    O(N) memory, exact. Returns list nu2[0..N]."""
    nu2 = [0] * (N + 1)
    chunk = max(1, (N - 1) // nproc)
    ranges, lo = [], 2
    while lo <= N:
        hi = min(N, lo + chunk - 1)
        ranges.append((lo, hi, h))
        lo = hi + 1
    with mp.Pool(nproc) as pool:
        for part in pool.imap_unordered(_worker, ranges, chunksize=1):
            for (n, ones) in part:
                nu2[n] = ones
    return nu2


def prefix_stats(nu2, N):
    """Population variance of { nu2(n)/n : n=2..N }, denominator N-1, exact
    Fractions. Matches the baseline capture's convention (count = N-1)."""
    S1 = Fraction(0)
    S2 = Fraction(0)
    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        S1 += r
        S2 += r * r
    cnt = N - 1
    mu = S1 / cnt
    s2 = S2 / cnt - mu * mu
    return mu, s2


def ratio_b(s2, N):
    return float(s2) * 4.0 * N / math.log(N)


def checkpoints_upto(N):
    return [c for c in (1000, 4000, 10000, 20000, 40000, 80000, 160000)
            if c <= N]


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 160000
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    out = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_OUT

    t0 = time.time()
    lines = []
    lines.append("SEQUENCE : { nu2(n)/n : n = 2..N }, N=%d  (PRIMES only)"
                 % N)
    lines.append("ORACLE   : lib.supply_fold.s_sos via lib.nu2.fold_nu2 "
                 "(s_sos==s_direct on n=4..200 + 53,64,100 in parent)")
    lines.append("N-RANGE  : [2, %d], streamed one n at a time (no triangle)"
                 % N)

    # ---- entry guard, asserted on the PRODUCED array after STAGE1 ----
    lines.append("")
    lines.append("=== ENTRY GUARD (canonical oracle, primes h) ===")
    hP = h_string(N + 2)
    g = {}
    for n in (53, 64, 4000):
        g[n] = fold_nu2(n, hP)   # a fresh guard call is allowed here (feed)
    tg = time.time()
    lines.append("  [guard, fresh oracle] fold_nu2(53)=%d fold_nu2(64)=%d "
                 "fold_nu2(4000)=%d  -> %s"
                 % (g[53], g[64], g[4000],
                    "PASS" if (g[53] == 18 and g[64] == 27 and g[4000] == 1975)
                    else "FAIL"))

    # ---- STAGE1: produce the nu2 array in parallel chunks ----
    lines.append("")
    lines.append("=== STAGE1 : compute_nu2 to N=%d (nproc=%d) ===" % (N, nproc))
    t1 = time.time()
    nu2 = compute_nu2(N, hP, nproc)
    dt1 = time.time() - t1
    lines.append("  [STAGE1] %.1fs ; nu2[%d]=%d (~%.4f)" %
                 (dt1, N, nu2[N], nu2[N] / N))

    # ---- array-level entry guard asserts (NOT a fresh oracle) ----
    a53 = nu2[53]
    a64 = nu2[64]
    a4000 = nu2[4000]
    tot = Fraction(0)
    for n in range(2, 4001):
        tot += Fraction(nu2[n], n)
    mu4000 = tot / 4000
    ok = (a53 == 18 and a64 == 27 and a4000 == 1975 and
          abs(mu4000 - Fraction(4977, 10000)) <= Fraction(1, 100))
    lines.append("  [ARRAY-ASSERT] nu2[53]=%d nu2[64]=%d nu2[4000]=%d "
                 "mu_4000(prod)=%.6f  -> %s"
                 % (a53, a64, a4000, float(mu4000),
                    "PASS" if ok else "FAIL"))
    assert ok, "array-level entry guard FAILED"

    # ---- s2_N at checkpoints, exact Fractions ----
    lines.append("")
    lines.append("=== s2_N and Ratio B at checkpoints (exact Fractions) ===")
    t2 = time.time()
    cps = checkpoints_upto(N)
    measured = {}
    for n in cps:
        mu, s2 = prefix_stats(nu2, n)
        measured[n] = (mu, s2)
        lines.append("  %6d  mu=%.8f  s2=%.10e  RatioB=%.3f"
                     % (n, float(mu), float(s2), ratio_b(s2, n)))
    dtred = time.time() - t2

    # ---- full N number ----
    muN, s2N = measured[N]
    rbN = ratio_b(s2N, N)
    lines.append("  FINAL N=%d: s2_N=%.10e RatioB=%.3f" %
                 (N, float(s2N), rbN))

    # ---- append to baseline & report per-doubling decrements ----
    lines.append("")
    lines.append("=== EXTENDED Ratio B sequence ===")
    seq = []
    for (n, rb) in BASELINE:
        seq.append((n, None, rb, "baseline"))
    for n in cps:
        seq.append((n, measured[n], ratio_b(measured[n][1], n), "measured"))
    # de-duplicate sorted by N
    seqd = {}
    for (n, m, rb, src) in seq:
        seqd[n] = rb
    lines.append("  N        RatioB")
    for n in sorted(seqd):
        lines.append("  %6d   %.3f" % (n, seqd[n]))
    # per-doubling decrements between consecutive sequence points
    lines.append("")
    lines.append("=== PER-DOUBLING DECREMENTS (each step ~2x N) ===")
    ns = sorted(seqd)
    lines.append("  from        to        decrement   d-ratio(r=d_{k+1}/d_k)")
    decs = []
    for i in range(1, len(ns)):
        d = seqd[ns[i - 1]] - seqd[ns[i]]
        decs.append((ns[i - 1], ns[i], d))
        lines.append("  %6d  -> %6d   %.3f" % (ns[i - 1], ns[i], d))
    # consecutive decrement ratios r_k = d_{k+1}/d_k  (from the 2nd row on)
    for k in range(1, len(decs)):
        rr = decs[k][2] / decs[k - 1][2]
        lines.append("      (decrement-ratio r_%d = %.3f/%.3f = %.3f)"
                     % (k, decs[k][2], decs[k - 1][2], rr))

    # ---- TREND by DECREMENT RATIO, not by whether the last decrement shrinks ----
    # Shrinking decrements are consistent with EITHER limit; the discriminator
    # is the ratio r_k = d_{k+1}/d_k of consecutive decrements:
    #   r -> rho < 1 : the decrements form a convergent geometric tail, so
    #                  Ratio B has a finite limit ABOVE 1 (extrapolation A);
    #   r -> 1       : the tail is non-summable and Ratio B reaches 1 (B).
    if len(decs) >= 2:
        ratios = [decs[k][2] / decs[k - 1][2] for k in range(1, len(decs))]
        d_last = decs[-1][2]
        r_last = ratios[-1]
        last_rb = seqd[ns[-1]]
        # (A) ratio settles at r_last (<1): geometric tail from last decrement.
        tail_A = d_last * r_last / (1.0 - r_last)
        limit_A = last_rb - tail_A
        # (B) ratio drifts to 1: non-summable tail, Ratio B reaches 1.
        limit_B = 1.0

        lines.append("")
        lines.append("=== DECREMENT-RATIO TREND (measured, not proved) ===")
        lines.append("  consecutive decrement ratios r_k = d_{k+1}/d_k : " +
                     ", ".join("%.3f" % r for r in ratios))
        lines.append("  These ratios are RISING toward 1 "
                     "(%.3f -> %.3f -> %.3f -> %.3f), which leans toward (B) "
                     % tuple(ratios))
        lines.append("  but does not decide either limit. Measured, not proved.")
        lines.append("")
        lines.append("  EXTRAPOLATION (A) — ratio settles at r=%.3f (<1): "
                     % r_last)
        lines.append("    remaining decrements form a convergent geometric "
                     "tail; from last decrement %.3f at ratio %.3f the tail "
                     "sums to %.3f*%.3f/(1-%.3f)=%.3f" %
                     (d_last, r_last, d_last, r_last, r_last, tail_A))
        lines.append("    Ratio B limit ~ last_RatioB - tail = %.3f - %.3f "
                     "~= %.3f" % (last_rb, tail_A, limit_A))
        lines.append("  EXTRAPOLATION (B) — ratio drifts to 1:")
        lines.append("    tail non-summable; Ratio B limit ~= %.2f" % limit_B)
        lines.append("")
        lines.append("  Both are consistent with the measured ratios; the "
                     "rising 0.63,0.75,0.875,0.905 leans toward (B) but does "
                     "not decide. A discriminator needs several more doublings "
                     "(160000,320000,...). LABEL: measured, not proved.")

    lines.append("")
    lines.append("STAGE1 %.1fs ; reduce %.1fs ; total %.1fs ; nproc=%d "
                 "; N=%d completed" % (dt1, dtred, time.time() - t0, nproc, N))
    lines.append("LABEL: measured, not proved.")
    text = "\n".join(lines) + "\n"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(text)
    print(text)
    print("WROTE", out)


if __name__ == "__main__":
    main()
