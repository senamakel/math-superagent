#!/usr/bin/env python3
"""Exact |S(n)|/n trajectory for the prime input, cumulative and windowed.

For the prime gap-parity fold T(n,d) (Lucas-submask XOR, d in [2,n-1]):
    nu2(n) = #{ d in [2,n-1] : T(n,d) = 1 }
    S(n)   = n - 2 - 2*nu2(n)   (sum of (-1)^{T(n,d)} over d in [2,n-1])

Streams n = 50..N one at a time via the per-n O(n log n) submask-product SOS
transform (lib.supply_fold.s_sos) — never materialises an O(n^2) triangle —
storing the exact S(n) values, then reports three objects:

  (a) CUMULATIVE running max of |S(m)|/m over m in [50, n] — MONOTONE
      non-decreasing by construction, pinned by the first spike (n=53,
      |S|/n = 15/53 = 0.283); it can only rise thereafter. Answers only
      whether any large-n n beats the small-n spike.
  (b) TRAILING-WINDOW max of |S(m)|/m over m in [max(50, n-W), n] for a
      window W — the diagnostic that actually tests whether LARGE-n
      excursions |S(n)|/n decay toward 0: a shrinking recent-window max
      shows large-n |S|/n stays small.
  (c) pointwise |S(n)|/n at checkpoints for context.

Goal: does large-n |S(n)|/n keep decaying toward 0 beyond n=4000 (supporting
nu2/n -> 1/2 pointwise), or does it plateau or recur?

All arithmetic exact (Python ints); only ratios are floats. s_sos is
cross-checked against the direct oracle s_direct at the top.

Usage: python track_smax.py [N] [W]     (defaults N=30000, W=2000)
"""
import sys
import os
import time
from collections import deque

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 2000   # trailing window

    # oracle cross-check: s_sos == s_direct on primes, small n
    h_check = h_string(N + 2)
    for n in range(4, 201):
        Sd, od = s_direct(n, h_check)
        Ss, os_ = s_sos(n, h_check)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    print(f"oracle cross-check: s_sos == s_direct on n=4..200 (primes): OK")

    h = h_string(N + 2)
    assert len(h) >= N, len(h)

    CHECK = [1000, 5000, 10000, 20000, 30000, 40000, 50000]
    checkpoints = [c for c in CHECK if c <= N]

    t0 = time.time()
    Svals = {}
    absS_over_n = {}
    for n in range(50, N + 1):
        _, ones = s_sos(n, h)
        S = n - 2 - 2 * ones
        Svals[n] = S
        absS_over_n[n] = abs(S) / n
    elapsed = time.time() - t0
    print(f"streamed n=50..{N} (per-n s_sos) in {elapsed:.1f}s; reached n={N}")

    # (a) cumulative running max (monotone)
    cum_max_ratio = {}
    cum_max_absS = {}
    best_arg = {}
    cr, ca, barg = 0.0, 0, None
    for n in range(50, N + 1):
        r = absS_over_n[n]
        a = abs(Svals[n])
        if r > cr:
            cr, barg = r, (n, a)
        if a > ca:
            ca = a
        cum_max_ratio[n] = cr
        cum_max_absS[n] = ca
        best_arg[n] = barg

    # (b) trailing-window max over [max(50,n-W), n] via monotone deque on ratios
    win_max = {}
    dq = deque()
    for n in range(50, N + 1):
        lo = max(50, n - W)
        while dq and dq[0] < lo:
            dq.popleft()
        r = absS_over_n[n]
        while dq and absS_over_n[dq[-1]] <= r:
            dq.pop()
        dq.append(n)
        win_max[n] = absS_over_n[dq[0]]

    lines = []
    lines.append("SMAX: |S(n)|/n trajectory for prime input, S(n)=n-2-2*nu2(n)")
    lines.append(f"streamed n=50..{N}, trailing window W={W}; s_sos crossed vs direct on n=4..200")
    lines.append("")
    lines.append("Checkpoint reports:")
    lines.append(f"  n        |S(n)|/n    cum-max|S|/n  cum-max|S|   win-max[W={W}]  argmax|S|/n (m,|S|)")
    for n in checkpoints:
        point = absS_over_n[n]
        nu2 = (n - 2 - Svals[n]) // 2
        lines.append(f"  {n:6d}   {point:8.6f}   {cum_max_ratio[n]:8.6f}   "
                     f"{cum_max_absS[n]:8d}   {win_max[n]:8.6f}   {best_arg[n]}"
                     f"   (S={Svals[n]}, nu2={nu2})")
    lines.append("")
    lines.append("Trajectory at every n in [50,N]:  n  pointwise|S|/n  cum  win")
    for n in range(50, N + 1):
        lines.append(f"  {n:6d}   {absS_over_n[n]:8.6f}   {cum_max_ratio[n]:8.6f}   {win_max[n]:8.6f}")

    text = "\n".join(lines)
    for line in text.splitlines()[:16]:
        print(line)

    outdir = os.path.join(os.path.dirname(__file__), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    outname = f"smax_trajectory_N{N}_W{W}.txt"
    with open(os.path.join(outdir, outname), "w") as f:
        f.write(text + "\n")
    print(f"\nfull trajectory written to code/out/{outname}")


if __name__ == "__main__":
    main()
