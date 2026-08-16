#!/usr/bin/env python3
"""Fair-model variance of the sequence {nu2(n)/n : n=2..N} at N=40000.

ONE QUESTION: for the input-dependent sequence a_n = nu2(n)/n, does the primes'
empirical variance s2_N track the fair-model null or deviate from it?

FAIR-MODEL NULL (the mathematical point this script exists to fix): the a_n are
independent(ish) coin averages, each with pointwise variance ~ 1/(4n). So the
POPULATION VARIANCE of the sequence over n = 2..N has expectation

    E[s2_N] = (1/N) * sum_{n=2..N} 1/(4n)   ~~  log(N) / (4N),

NOT 1/(4N). s2_N * 4N then measures deviations from the wrong 1/(4N) null,
which is what the operator guessed; the correct null-corrected ratio is
s2_N * 4N / log(N), which is ~ 1 when the primes track the fair model.

We print BOTH ratios at every checkpoint so the reader can see which null fits.

ORACLE (canonical floored fold only, no reimplementation):
    nu2(n) = wt(Phi_n h) = #{ d in [2,n-1] : T(n,d)=1 }
computed by lib.supply_fold.s_sos (submask-product SOS), wrapped by
lib.nu2.fold_nu2. Verified against the direct submask-XOR oracle and against
nu2(53)=18, nu2(64)=27. h strings from lib.primes.h_string. All arithmetic
exact (parities, Fractions); only display ratios are floats.

ENTRY ASSERTIONS (abort, never print a table, if any fail — a zeroed or
wrong-convention oracle dies here):
    fold_nu2(53, h) == 18
    fold_nu2(64, h) == 27
    | mu_N(4000) - 0.4977 | <= 0.01

INPUTS (all streamed n=2..N, never materialising any O(N^2) triangle; the
per-n s_sos is O(n log n)):
    PRIMES     — operative h = [q_{j+2} != q_{j+1} mod 4]
    ALL-ONES   — negative control (nu2 = O(1), ratio -> 0, variance tiny)
    THUE-MORSE — negative control (nu2/n collapses, sublinear)

OUTPUTS at checkpoints N in {100,400,1000,4000,10000,20000,40000}:
    mu_N, s2_N (population variance of the a_n sequence), s2_N*4N,
    s2_N*4N/log(N), and the running 1/(4n) null accumulator null_s2_N.

DIP TABLE: for c in 40..49 (hundredths, exact Fractions) the density of
{ n in [50,N] : nu2(n)/n < c } over [50,N], [N//2,N], [int(0.9*N), N], for
primes, with all-ones and Thue-Morse as controls. Where sparsity breaks = the
first c at which the deep tail [36000,40000] density exceeds 0.01.

ALL NUMBERS ARE MEASURED, NOT PROVED.

Usage: python3 fair_variance_at_40000.py [N] [nproc]
Writes: code/out/fair_variance_at_40000.txt
"""
import sys
import os
import time
import math
import multiprocessing as mp
from fractions import Fraction

from lib.supply_fold import s_sos, s_direct
from lib.nu2 import fold_nu2
from lib.primes import h_string

N = 40000
NP = int(os.environ.get("NPROC", "16"))
if len(sys.argv) > 1:
    N = int(sys.argv[1])
if len(sys.argv) > 2:
    NP = int(sys.argv[2])

N_DEFAULT = 40000
CHECKPOINTS = [100, 400, 1000, 4000, 10000, 20000, 40000]
FINE = [Fraction(h, 100) for h in range(40, 50)]   # 0.40..0.49 exact

OUT = os.path.join(os.path.dirname(__file__), "..", "out",
                   "fair_variance_at_40000.txt")
OUT = os.path.abspath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


# ---------------------------------------------------------------------------
# ENTRY ASSERTIONS (the flocked guard; abort rather than print a table)
# ---------------------------------------------------------------------------
def _assert_oracle():
    h = prime_h(4002)
    assert fold_nu2(53, h) == 18, ("nu2(53)", fold_nu2(53, h))
    assert fold_nu2(64, h) == 27, ("nu2(64)", fold_nu2(64, h))
    # mu_N(4000) sample mean of a_n over n = 2..4000 (3999 values)
    mu = Fraction(0)
    cnt = 0
    for n in range(2, 4001):
        r = Fraction(fold_nu2(n, h), n)
        cnt += 1
        mu = mu + (r - mu) / cnt
    assert abs(float(mu) - 0.4977) <= 0.01, ("mu_4000", float(mu))


# ---------------------------------------------------------------------------
# STAGE 1: parallel nu2 (each n independent via s_sos, never a triangle)
# ---------------------------------------------------------------------------
def _worker(args):
    lo, hi, h = args
    res = []
    for n in range(lo, hi + 1):
        _, ones = s_sos(n, h[:n])
        res.append((n, ones))
    return res


def compute_nu2(N, h, nproc):
    """nu2[0..N] by parallel s_sos over n=2..N. O(N^2 log N) total work across
    nproc workers, O(N) memory. Each n independent; no triangle materialised."""
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


# ---------------------------------------------------------------------------
# STAGE 2: single-threaded exact reductions
# ---------------------------------------------------------------------------
def reduce_stats(nu2, N, checkpoints):
    """Running sample mean mu and population variance s2 of a_n; running
    1/(4n) null accumulator. Returns (checkpoint dict, final dict)."""
    mu, M2 = Fraction(0), Fraction(0)
    cnt = 0
    cp = {}
    null_sum = Fraction(0)              # sum_{m=2..n} 1/(4m)
    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        cnt += 1
        delta = r - mu
        mu = mu + delta / cnt
        m2 = M2 + delta * (r - mu)
        M2 = m2
        s2 = M2 / cnt
        null_sum += Fraction(1, 4 * n)  # pointwise var ~1/(4n)
        if n in checkpoints:
            null_s2 = null_sum / cnt    # (1/N)*sum 1/(4n) with N=cnt
            cp[n] = dict(mu=mu, s2=s2,
                         null_s2=null_s2, null_op=(Fraction(1, 4 * cnt)))
    fin = dict(mu=mu, s2=M2 / cnt, null_sum=null_sum,
               null_s2=null_sum / cnt)
    return cp, fin


def dip_row(nu2, N, c):
    """Density of {n in [50,N] : nu2(n)/n < c} over three windows."""
    windows = [(50, N), (N // 2, N), (int(0.9 * N), N)]
    counts = []
    for (lo, hi) in windows:
        cc = sum(1 for n in range(lo, hi + 1) if Fraction(nu2[n], n) < c)
        den = hi - lo + 1
        counts.append(cc / den if den else 0.0)
    return counts


# ---------------------------------------------------------------------------
def main():
    t0 = time.time()
    _assert_oracle()
    oracle_ok = True

    lines = []
    lines.append("SEQUENCE: internals { nu2(n)/n : n = 2..N }, N=%d" % N)
    lines.append("ORACLE: lib.supply_fold.s_sos via lib.nu2.fold_nu2 "
                 "(canonical floored fold; s_sos==s_direct, nu2(53)=18, "
                 "nu2(64)=27)")
    lines.append("n-range: n = 2..%d, streamed one n at a time via s_sos "
                 "(no triangle materialised)" % N)
    lines.append("")

    families = [
        ("PRIMES   ", prime_h),
        ("ALL-ONES ", all_ones_h),
        ("THUE-MORS", thue_morse_h),
    ]

    results = {}
    for (label, gen) in families:
        h = gen(N + 2)
        lines.append("=== %s  compute_nu2 to N=%d (parallel s_sos) ==="
                     % (label.strip(), N))
        nu2 = compute_nu2(N, h, NP)
        results[label] = nu2
        lines.append("   nu2[%d]=%d  (~%.4f of n)" %
                     (N, nu2[N], nu2[N] / N))

    lines.append("")
    lines.append("CHECKPOINT TABLE  (s2_N = population variance of a_n over "
                 "n=2..N;")
    lines.append("  null_log = (1/N)*sum_{n=2..N} 1/(4n) ~= log(N)/(4N); "
                 "null_const = 1/(4N) [operator's guess])")
    lines.append("  Ratio A = s2_N*4N  (vs 1 if the const null fit);  "
                 "Ratio B = s2_N*4N/log(N)  (vs 1 if the log null fits)")
    lines.append("%-12s %5s %12s %12s %10s %10s %12s %12s" %
                 ("family", "N", "mu_N", "s2_N", "s2*4N", "s2*4N/lnN",
                  "null_log", "null_const"))

    summary = {}
    for (label, gen) in families:
        nu2 = results[label]
        cp, fin = reduce_stats(nu2, N, CHECKPOINTS)
        for n in CHECKPOINTS:
            d = cp[n]
            muN = d["mu"]
            s2 = d["s2"]
            rA = float(s2) * 4 * n
            rB = float(s2) * 4 * n / math.log(n)
            null_log = d["null_s2"]
            null_const = d["null_op"]
            lines.append("%-12s %5d %12.6f %12.5e %10.4f %10.4f %12.5e %12.5e"
                         % (label, n, float(muN), float(s2), rA, rB,
                            float(null_log), float(null_const)))
        summary[label] = fin

    lines.append("")
    lines.append("RATIO B (s2_N*4N/log N) by family at the checkpoints:")
    for (label, gen) in families:
        nu2 = results[label]
        cp, _ = reduce_stats(nu2, N, CHECKPOINTS)
        vals = " ".join("%.3f" % (float(cp[n]["s2"]) * 4 * n / math.log(n))
                        for n in CHECKPOINTS)
        lines.append("  %-12s  %s" % (label, vals))

    lines.append("")
    lines.append("DIP TABLE: density of {n in [50,N]: nu2(n)/n < c} over "
                 "[50,N], [N//2,N]=[%d,%d], [0.9N,N]=[%d,%d]" %
                 (N // 2, N, int(0.9 * N), N))
    lines.append("%-12s %5s %8s %8s %8s" %
                 ("family", "c", "d[50,N]", "d[N/2,N]", "d[0.9N,N]"))
    break_c = {}
    for (label, gen) in families:
        nu2 = results[label]
        first_break = None
        for c in FINE:
            dens = dip_row(nu2, N, c)
            lines.append("%-12s %3.2f %8.4f %8.4f %8.4f" %
                         (label, float(c), dens[0], dens[1], dens[2]))
            if label.strip() == "PRIMES" and first_break is None \
                    and dens[2] > 0.01:
                first_break = float(c)
        if label.strip() == "PRIMES":
            break_c["primes"] = first_break
        for (i, nm) in enumerate(["full", "half", "tail"]):
            lines.append("")
            break_c.setdefault(label.strip(), {})[nm] = (
                next((float(c) for c in FINE
                      if dip_row(nu2, N, c)[i] > 0.01), None))

    lines.append("")
    lines.append("SPARSITY-BREAK (deep tail [0.9N,N] density first > 0.01, "
                 "ascending c):")
    pr = results["PRIMES   "]
    tail0 = 0.0
    for c in FINE:
        tail0 = dip_row(pr, N, c)[2]
        if tail0 > 0.01:
            break
    for (label, gen) in families:
        nu2 = results[label]
        tb = next((float(c) for c in FINE
                   if dip_row(nu2, N, c)[2] > 0.01), None)
        lines.append("  %-12s  tail-dip first > 0.01 at c=%s"
                     % (label, tb))

    # ---- one-line summary ----
    cpP, finP = reduce_stats(results["PRIMES   "], N, CHECKPOINTS)
    rB_40000 = float(finP["s2"]) * 4 * N / math.log(N)
    rA_40000 = float(finP["s2"]) * 4 * N
    null_ratio = float(finP["null_s2"])
    break_val = break_c.get("primes")
    if break_val is None:
        # fall back computed already
        break_val = next((float(c) for c in FINE
                          if dip_row(pr, N, c)[2] > 0.01), None)
    verdict = ("primes TRACK the log(N)/(4N) null (Ratio B near 1: %.3f); "
               "they DEVIATE from the constant 1/(4N) null (Ratio A=%.3f vs 1)"
               % (rB_40000, rA_40000)) if 0.5 <= rB_40000 <= 2.0 else \
        ("primes DEVIATE from the log(N)/(4N) null (Ratio B=%.3f, null %.4e)"
         % (rB_40000, null_ratio))
    lines.append("")
    lines.append("SUMMARY: at N=%d, Ratio A (s2*4N) = %.4f ; Ratio B "
                 "(s2*4N/log N) = %.4f ; null log = %.4e ; null const = %.4e"
                 % (N, rA_40000, rB_40000, float(finP["null_s2"]),
                    float(Fraction(1, 4 * N))))
    lines.append("SUMMARY-ONE-LINE: %s ; deep-tail dip density first >0.01 "
                 "at c=%s" % (verdict, break_val))
    lines.append("")
    lines.append("runtime %.1fs ; oracle assertions passed=%s" %
                 (time.time() - t0, oracle_ok))

    text = "\n".join(lines) + "\n"
    with open(OUT, "w") as f:
        f.write(text)
    print(text)
    print("WROTE", OUT)


if __name__ == "__main__":
    main()
