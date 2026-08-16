#!/usr/bin/env python3
"""SUPPLY averaged push — one consolidated streaming capture at the N=40000
ceiling (task chebyshev-second-moment-density1, directive 8/9).

PURPOSE (GOAL priority 1): turn the measured rising mean M(N) of nu2(n)/n into
a *measured* density-1 lower bound for nu2(n)/n via the second moment, and
answer the monotonicity / dip-sparsity questions at the full ceiling.

Object: nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 } = wt(Phi_n h), T the depth-d
submask-XOR fold cell over F2 of the prime gap-parity switch string
h[j] = [q_{j+2} != q_{j+1} mod 4].

Method: NO O(n^2) triangle is ever materialised. The expensive per-n fold
value nu2(n) (O(n log n) submask-product SOS via lib.supply_fold.s_sos,
cross-checked against the direct oracle s_direct on n=4..200 and spots
53,64,100) is computed in STAGE 1 in parallel over n (each n independent), and
the exact results reduced single-threaded in STAGE 2. Memory is O(N): a single
nu2[] integer array, never a triangle. All arithmetic exact (parities and
Fractions); only display ratios are floats.

Three inputs:
  PRIMES      — the operative h, the only one asserted about.
  ALL-ONES    — negative control: nu2 = O(1), mean 0, var 0, vacuous Chebyshev.
  THUE-MORSE  — negative control: MUST FAIL the density-1 bound (lower tail
                does NOT empty).

ALL NUMBERS ARE MEASURED, NOT PROVED.

Usage: python3 chebyshev_second_moment.py [N] [nproc]
"""
import sys
import os
import time
import math
import multiprocessing as mp
from fractions import Fraction

import sympy as sp

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string
from lib.nu2_guard import assert_supply_guard, scene_header

MIN_X = [50, 1000, 10000, 30000]


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


def verify_oracle(h, spots=(53, 64, 100)):
    """s_sos == s_direct on n=4..200 and at the given spots (primes h)."""
    for n in range(4, 201):
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    for n in spots:
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    return True


# ---------------------------------------------------------------------------
# STAGE 1: parallel nu2 computation (exact, per-n s_sos)
# ---------------------------------------------------------------------------

def _worker(args):
    """Compute nu2 for every n in [lo, hi] for a fixed h string."""
    lo, hi, h = args
    res = []
    for n in range(lo, hi + 1):
        _, ones = s_sos(n, h[:n])
        res.append((n, ones))
    return res


def compute_nu2_parallel(N, h, nproc):
    """Return nu2[] list indexed 0..N (nu2[0]=nu2[1]=0) by parallel s_sos over
    n=2..N. O(N^2 log N) total work split over nproc workers, O(N) memory."""
    nu2 = [0] * (N + 1)
    chunk = max(1, (N - 1) // nproc)
    ranges = []
    lo = 2
    while lo <= N:
        hi = min(N, lo + chunk - 1)
        ranges.append((lo, hi, h))
        lo = hi + 1
    with mp.Pool(nproc) as pool:
        for part in pool.imap_unordered(_worker, ranges, chunksize=1):
            for (n, ones) in part:
                nu2[n] = ones
    return nu2


# ---------------------------------------------------------------------------
# STAGE 2: single-threaded exact reductions over the nu2[] array (O(N))
# ---------------------------------------------------------------------------

def reduce_capture(N, nu2, checkpoints, var_points, eps_list):
    """Single exact pass over nu2[] computing every reported quantity.
    Returns a dict of results. O(N) time."""
    # running mean M(N) and prefix sums, exact
    M = [Fraction(0)] * (N + 1)
    S1 = Fraction(0)
    S2 = Fraction(0)
    mon_viol = 0
    prev_M = None
    mu_s2 = {}
    # running min over [X,N]
    min_x = [x for x in MIN_X if x <= N]
    running_min = {x: None for x in min_x}

    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        S1 += r
        S2 += r * r
        M[n] = S1 / n
        if prev_M is not None and M[n] < prev_M:
            mon_viol += 1
        prev_M = M[n]
        for x in running_min:
            if n >= x:
                rm = running_min[x]
                running_min[x] = r if (rm is None or r < rm) else rm
        if n in var_points:
            mu = S1 / n
            ex2 = S2 / n
            mu_s2[n] = (mu, ex2 - mu * mu)

    # below-bound tallies: {Np: {eps: (count, frac)}}
    below_bound = {}
    for Np in var_points:
        if Np > N:
            continue
        mu = mu_s2[Np][0]
        row = {}
        for eps in eps_list:
            thr = mu - eps
            cnt = sum(1 for k in range(2, Np + 1) if Fraction(nu2[k], k) < thr)
            row[eps] = (cnt, Fraction(cnt, Np - 1))
        below_bound[Np] = row

    return dict(M=M, mon_viol=mon_viol, mu_s2=mu_s2,
                running_min=running_min, below_bound=below_bound)


def format_results(res, N, label, var_points, eps_list, checkpoints, nu2):
    L = []
    r = res
    L.append(f"=== {label} : N = {N} ===")
    L.append("(1) M(N) = (1/N) sum_{n=2..N} nu2(n)/n  at checkpoints:")
    L.append("   N        M(N)        nu2(N)/N")
    for c in checkpoints:
        if c <= N:
            L.append(f"  {c:6d}  {float(r['M'][c]):.8f}   "
                     f"{float(Fraction(nu2[c], c)):.8f}")
    viol = r['mon_viol']
    L.append(f"monotonicity violations (M(N) < M(N-1)) over N=3..{N}: "
             f"count = {viol}  density = {viol/max(1, N-2):.6f}")

    L.append(f"(2) dip sparsity at N = {N}:  {{n in range : nu2(n)/n < c}}")
    thresh = [0.30, 0.35, 0.40, 0.42, 0.45, 0.48]
    ranges = [("full", 50, N), ("half", N // 2, N), ("tail", int(0.9 * N), N)]
    L.append("   c     range       count    width    density")
    for (rname, lo, hi) in ranges:
        for c in thresh:
            cf = Fraction(int(round(c * 100)), 100)
            cnt = sum(1 for k in range(lo, hi + 1) if Fraction(nu2[k], k) < cf)
            w = hi - lo + 1
            L.append(f"  {c:.2f}  {rname:6s}  {cnt:8d}  {w:6d}  {cnt/w:.6f}")
    L.append("min of nu2(n)/n over [X, N]:")
    for x in MIN_X:
        if x <= N and r['running_min'][x] is not None:
            L.append(f"   X={x:6d}:  min = {float(r['running_min'][x]):.8f}")

    L.append("(3)+(4) exact variance s2_N, mu_N, std, Chebyshev density bound:")
    for Np in var_points:
        if Np > N:
            continue
        mu, s2 = r['mu_s2'][Np]
        std = (s2 ** Fraction(1, 2)) if s2 >= 0 else Fraction(0)
        for eps in eps_list:
            cnt, frac = r['below_bound'][Np][eps]
            bound = float(s2) / float(eps) ** 2 if eps != 0 else float('nan')
            L.append(f"  N={Np:5d}  mu={float(mu):.6f}  s2={float(s2):.8f} "
                     f"std={float(std):.6f}  eps={float(eps):.2f}  "
                     f"#{'<mu-eps'}={cnt:7d}  Cheb={bound:9.4f}  "
                     f"real-below={float(frac):.6f}")
    L.append("   ---- fair-variance ratio & theoretical decoupled-random"
             " reference ----")
    L.append("   Np      mu_N      s2_N      s2*4Np  s2*4Np/lnNp "
             "  theo_decoupled   theo*4Np  theo*4Np/lnNp  meas/theo")
    for Np in var_points:
        if Np > N:
            continue
        mu, s2 = r['mu_s2'][Np]
        lnNp = math.log(Np)
        meas_4N = float(s2) * 4.0 * Np
        meas_4N_ln = meas_4N / lnNp
        # theoretical decoupled-random prediction
        #   s2 ~ (1/Np) * sum_{n=2..Np} (n-2)/(4 n^2), exact rational
        S = sum(sp.Rational(n - 2, 4 * n * n) for n in range(2, Np + 1))
        theo = S / Np
        theo_4N = float(theo) * 4.0 * Np
        theo_4N_ln = theo_4N / lnNp
        ratio = float(s2) / float(theo)
        L.append(f"  {Np:5d} {float(mu):.6f} {float(s2):.8f} {meas_4N:8.4f} "
                 f"{meas_4N_ln:9.3f} {float(theo):.8f} {theo_4N:8.4f} "
                 f"{theo_4N_ln:9.3f} {ratio:7.3f}")
    return "\n".join(L) + "\n"


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    var_points = list(range(4000, N + 1, 4000))
    checkpoints = [100, 1000, 5000, 10000, 20000, 30000, 40000]
    eps_list = [Fraction(5, 100), Fraction(10, 100),
                Fraction(15, 100), Fraction(20, 100)]

    out = []
    t_start = time.time()

    # mandatory entry guard: abort if the canonical oracle is degenerate
    assert_supply_guard(N)
    out.append("[guard] assert_supply_guard(%d): nu2(53)==18, nu2(64)==27, "
               "primes mu_4000 within 0.01 of 0.4977 — canonical oracle OK" % N)

    h_check = prime_h(N + 2)
    verify_oracle(h_check)
    out.append(f"oracle cross-check: s_sos == s_direct on n=4..200 and spots "
               f"53,64,100 (prime h): OK")

    # primes: stage1 parallel + stage2 reduce
    hP = prime_h(N + 1)
    out.append(scene_header('PRIMES', 'lib.nu2.fold_nu2=lib.supply_fold.s_sos',
                            2, N))
    t0 = time.time()
    nu2P = compute_nu2_parallel(N, hP, nproc)
    out.append(f"[primes] STAGE1 parallel nu2 (n=2..{N}) in "
               f"{time.time()-t0:.1f}s (nproc={nproc})")
    t0 = time.time()
    resP = reduce_capture(N, nu2P, checkpoints, var_points, eps_list)
    out.append(f"[primes] STAGE2 exact reduce in {time.time()-t0:.1f}s")
    out.append(format_results(resP, N, "PRIMES h", var_points, eps_list,
                              checkpoints, nu2P))

    # negative controls at N=4000
    Cn = min(4000, N)
    for label, hsrc in [("ALL-ONES h (neg control: mean 0, var 0, vacuous)",
                         all_ones_h),
                        ("THUE-MORSE h (neg control: must FAIL density-1)",
                         thue_morse_h)]:
        hC = hsrc(Cn)
        nu2C = compute_nu2_parallel(Cn, hC, min(nproc, Cn))
        resC = reduce_capture(Cn, nu2C, checkpoints, var_points, eps_list)
        out.append(format_results(resC, Cn, label,
                                  [p for p in var_points if p <= Cn], eps_list,
                                  [c for c in checkpoints if c <= Cn], nu2C))

    text = "\n".join(out) + "\n"
    text += f"TOTAL runtime: {time.time()-t_start:.1f}s;  exact ceiling reached: N={N}\n"
    print(text)

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "chebyshev_second_moment_N40000.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
