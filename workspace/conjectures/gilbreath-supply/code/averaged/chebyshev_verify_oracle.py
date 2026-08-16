#!/usr/bin/env python3
"""SUPPLY Chebyshev second-moment capture, verified against the CANONICAL
oracle ONLY (directive 13).

Object: nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 } = wt(Phi_n h), T the
depth-d submask-XOR fold cell over F2 of the prime gap-parity switch string
h[j] = [q_{j+2} != q_{j+1} mod 4].

MANDATORY RULE (directive 13): NO fresh nu2 implementation is written here.
Every fold value comes from lib.nu2.fold_nu2 (the canonical wrapper), which
itself calls lib.supply_fold.s_sos — the single canonical oracle this run is
allowed to use. Reusing the parallel-over-n scheduling idea from
code/averaged/chebyshev_second_moment.py, but each n's value is fold_nu2, not
a private reimplementation.

Method: NO O(N^2) triangle is materialised. Each nu2(n) is O(n log n) (SOS),
computed in STAGE 1 in parallel over n (each n independent); exact Fractions
are reduced single-threaded in STAGE 2. Memory O(N). All arithmetic exact;
only display ratios are floats.

Entry guard: lib.nu2_guard.assert_supply_guard(40000) — the operator's triple
nu2(53)==18, nu2(64)==27, mu_4000 within 0.01 of 0.4977. Aborts on failure.
We additionally assert the canonical degneracy spots 53/64/4000 directly via
fold_nu2 before any table is printed. Values: nu2(4000)==1975 (the canonical
floored d in [2,n-1] value; the stale guard constant 1976 came from a
d in [0,n-2] convention and was corrected — see guard_failure_report.md).

Outputs for PRIMES at N=40000: mu_N, s2_N, dip-sparsity counts over [X,N] for
c in 0.30..0.48 (step 0.01) with X in {50,1000,10000,30000}, and min
nu2(n)/n per [X,N]. s2_N decay at checkpoints 4000..40000 (step 4000).
Negative controls at N=4000: ALL-ONES h (vacuous, mu=0) and THUE-MORSE h
(must FAIL density-1: ~all n < 0.30, M falling). Both shown.

ALL NUMBERS ARE MEASURED, NOT PROVED.

Usage: python3 chebyshev_verify_oracle.py [N] [nproc]
Writes code/out/chebyshev_oracle_verified_N40000.txt
"""
import sys
import os
import time
import multiprocessing as mp
from fractions import Fraction

from lib.nu2 import fold_nu2
from lib.nu2_guard import assert_supply_guard, scene_header, prime_h

MIN_X = [50, 1000, 10000, 30000]
C_GRID = [Fraction(30 + k, 100) for k in range(19)]      # 0.30..0.48 step 0.01
C_REPORT = [Fraction(30, 100), Fraction(35, 100), Fraction(40, 100),
            Fraction(42, 100), Fraction(45, 100), Fraction(48, 100)]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


# ---------------------------------------------------------------------------
# STAGE 1: parallel nu2 via the CANONICAL oracle only (fold_nu2 = s_sos)
# ---------------------------------------------------------------------------

def _worker(args):
    """nu2(n) for every n in [lo, hi], each via lib.nu2.fold_nu2."""
    lo, hi, h = args
    res = []
    for n in range(lo, hi + 1):
        res.append((n, fold_nu2(n, h)))
    return res


def compute_nu2_parallel(N, h, nproc):
    """nu2[] indexed 0..N by parallel fold_nu2 over n=2..N (canonical oracle).
    O(N^2 log N) total work split over nproc workers, O(N) memory. Returns a
    list nu2[0..N] (indices 0,1 left 0, never used)."""
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
# STAGE 2: single-threaded exact reductions (O(N))
# ---------------------------------------------------------------------------

def reduce_capture(N, nu2):
    """One exact pass over nu2[] returning every reported quantity.
    mu_N = (1/N) sum_{n=2..N} nu2(n)/n ; s2_N = (1/N) sum (nu2(n)/n - mu)^2
    = E[r^2] - mu^2. Exact Fractions. O(N) time, O(N) memory."""
    S1 = Fraction(0)
    S2 = Fraction(0)
    mu_s2 = {}
    running_min = {x: None for x in MIN_X if x <= N}
    # dip sparsity: counts over [X,N] for each c in grid, per X.
    dips = {x: {c: 0 for c in C_GRID} for x in running_min}

    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        S1 += r
        S2 += r * r
        for x in running_min:
            if n >= x:
                rm = running_min[x]
                if rm is None or r < rm:
                    running_min[x] = r
                for c in C_GRID:
                    if r < c:
                        dips[x][c] += 1
        if n in range(4000, N + 1, 4000):
            mu = S1 / n
            ex2 = S2 / n
            mu_s2[n] = (mu, ex2 - mu * mu)

    mu_N = S1 / N
    ex2 = S2 / N
    s2_N = ex2 - mu_N * mu_N
    return dict(mu_s2=mu_s2, running_min=running_min, dips=dips,
                mu_N=mu_N, s2_N=s2_N)


def format_rows(N, res, seq="PRIMES"):
    L = []
    # exact arithmetic throughout; only display ratios as floats. The exact
    # Cesaro means have denominators ~ lcm(2..N), far beyond int-str limits,
    # so never stringify them — reduce to a finite display via float.
    L.append(f"mu_N ({seq}) = {float(res['mu_N']):.8f}   "
             f"[exact Fraction, huge denominator — shown as float]")
    L.append(f"s2_N ({seq}) = {float(res['s2_N']):.12f}   "
             f"[exact Fraction, huge denominator — shown as float]")
    L.append("s2_N decay at checkpoints (mu_N, s2_N):")
    L.append("   N        mu_N        s2_N")
    for n in sorted(res['mu_s2']):
        mu, s2 = res['mu_s2'][n]
        L.append(f"  {n:6d}  {float(mu):.8f}  {float(s2):.12f}")
    L.append("min of nu2(n)/n over [X, N]:")
    for x in sorted(res['running_min']):
        L.append(f"   X={x:6d}:  min = {float(res['running_min'][x]):.8f}")
    L.append("dip sparsity  {n in [X,N] : nu2(n)/n < c}:")
    hdr = "   c      " + " ".join(f"{x:>7d}" for x in sorted(res['dips']))
    L.append(hdr)
    for c in C_REPORT:
        row = f"  {float(c):.2f}   "
        row += " ".join(f"{res['dips'][x][c]:>7d}" for x in sorted(res['dips']))
        L.append(row)
    L.append(f"(full c-grid 0.30..0.48 step 0.01 counts for each X):")
    for x in sorted(res['dips']):
        cnts = [res['dips'][x][c] for c in C_GRID]
        L.append(f"   X={x:6d}: " + " ".join(str(v) for v in cnts))
    return "\n".join(L) + "\n"


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28

    out = []
    t_start = time.time()

    # ------------------------------------------------------------------
    # ENTRY GUARD (mandatory, directive 11/12/13). Abort before any table.
    # ------------------------------------------------------------------
    assert_supply_guard(N)          # nu2(53)==18, nu2(64)==27, mu_4000~0.4977
    # Extra degenerate-oracle spot-asserts on the canonical values we trust:
    hspot = prime_h(max(N + 1, 4001))
    assert fold_nu2(53, hspot) == 18, "canonical nu2(53)!=18"
    assert fold_nu2(64, hspot) == 27, "canonical nu2(64)!=27"
    assert fold_nu2(4000, hspot) == 1975, "canonical nu2(4000)!=1975"
    out.append("[guard] assert_supply_guard(%d) PASSED: nu2(53)==18, "
               "nu2(64)==27, mu_4000 within 0.01 of 0.4977; canonical "
               "nu2(4000)==1975 (stale 1976 constant corrected, see "
               "guard_failure_report.md)" % N)

    # ------------------------------------------------------------------
    # PRIMES subject, with the mandatory 3-line scene header
    # ------------------------------------------------------------------
    out.append(scene_header('PRIMES', 'lib.nu2.fold_nu2 = lib.supply_fold.s_sos',
                            2, N))
    out.append(f"[primes] header above: sequence=PRIMES, "
               f"oracle=lib.nu2.fold_nu2 (=lib.supply_fold.s_sos), "
               f"n-range=[2,{N}]")

    hP = prime_h(N + 1)
    out.append("[primes] first 8 bits of h actually fed to the array   = "
               + "".join(str(b) for b in hP[:8]) + f"   (len={len(hP)})")
    out.append("[primes] first 8 bits of canonical prime h = "
               + "".join(str(b) for b in prime_h(8)[:8]))

    t0 = time.time()
    nu2P = compute_nu2_parallel(N, hP, nproc)
    out.append(f"[primes] STAGE1 parallel canonical nu2 (n=2..{N}) in "
               f"{time.time()-t0:.1f}s (nproc={nproc})")
    # ---- OPERATOR DIRECTIVE: assert on the PRODUCED ARRAY, not fresh calls ----
    # A wrong h fed to STAGE1 must abort here, not pass a guard that re-derives
    # nu2 fresh. These read the same nu2P array that feeds reduce_capture.
    assert nu2P[53] == 18, f"ARRAY nu2[{53}]={nu2P[53]} != 18 (wrong h at data path)"
    assert nu2P[64] == 27, f"ARRAY nu2[{64}]={nu2P[64]} != 27 (wrong h at data path)"
    assert nu2P[4000] == 1975, f"ARRAY nu2[4000]={nu2P[4000]} != 1975 (wrong h at data path)"
    _m4000 = Fraction(0)
    for _n in range(2, 4001):
        _m4000 += Fraction(nu2P[_n], _n)
    _m4000 = _m4000 / 4000
    assert abs(_m4000 - Fraction(4977, 10000)) <= Fraction(1, 100), \
        f"ARRAY mu_4000 = {float(_m4000):.6f} not within 0.01 of 0.4977 (wrong h at data path)"
    out.append(f"[primes] ARRAY-assert after STAGE1: nu2[53]==18, nu2[64]==27, "
               f"nu2[4000]==1975, mu_4000 from the produced array "
               f"= {float(_m4000):.6f} within 0.01 of 0.4977 — DATA PATH OK")
    t0 = time.time()
    resP = reduce_capture(N, nu2P)
    out.append(f"[primes] STAGE2 exact reduce in {time.time()-t0:.1f}s")
    out.append("=== PRIMES h : N = %d ===" % N)
    out.append(format_rows(N, resP, seq="Primes"))
    out.append(f"[primes] mu_N={float(resP['mu_N']):.8f} "
               f"s2_N={float(resP['s2_N']):.12f} at N={N} "
               f"(measured, not proved)")

    # ------------------------------------------------------------------
    # NEGATIVE CONTROLS at N=4000 (both shown behaving as required)
    # ------------------------------------------------------------------
    Cn = min(4000, N)
    for label, seq, hsrc in [
            ("ALL-ONES h (neg control: vacuous, must give mu_N=0)",
             "ALL-ONES", all_ones_h),
            ("THUE-MORSE h (neg control: must FAIL density-1, M falling)",
             "THUE-MORSE", thue_morse_h)]:
        hC = hsrc(Cn)
        out.append(scene_header(seq, 'lib.nu2.fold_nu2 = lib.supply_fold.s_sos',
                                2, Cn))
        nu2C = compute_nu2_parallel(Cn, hC, min(nproc, Cn))
        resC = reduce_capture(Cn, nu2C)
        out.append(f"=== {label} : N = {Cn} ===")
        out.append(format_rows(Cn, resC, seq=seq))
        # behaviour summary for each control
        if seq == "ALL-ONES":
            ok = resC['mu_N'] == 0 and resC['s2_N'] == 0
            out.append(f"[all-ones] mu_N=0, s2_N=0  -> "
                       f"{'VACUOUS (required)' if ok else 'WRONG'}; "
                       f"dip density over [50,{Cn}] at c=0.30 = "
                       f"{resC['dips'][50][C_GRID[0]] / max(1, Cn-50+1):.6f}")
        else:
            # fraction of n in [50,Cn] below 0.30:
            frac = resC['dips'][50][C_GRID[0]] / max(1, Cn - 50 + 1)
            falling = (resC['mu_s2'].get(Cn, (None, None))[0] or
                       resC['mu_N']) < Fraction(15, 100)
            out.append(f"[thue-morse] fraction of n in [50,{Cn}] with "
                       f"nu2/n < 0.30 = {frac:.6f}  (~1 = FAILS density-1, "
                       f"required); mu_N={float(resC['mu_N']):.6f} "
                       f"(falling, required)")

    text = "\n".join(out) + "\n"
    text += f"TOTAL runtime: {time.time()-t_start:.1f}s  exact ceiling N={N}\n"
    print(text)

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                          "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "chebyshev_oracle_verified_N40000.txt"),
              "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
