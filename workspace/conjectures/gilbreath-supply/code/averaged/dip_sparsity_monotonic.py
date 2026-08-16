#!/usr/bin/env python3
"""SUPPLY averaged-push capture — FINE dip-sparsity sweep at N=40000.

QUESTION being measured (GOAL priority 1, dip sparsity): for the prime
gap-parity string h (h[j] = ((q_{j+2}-q_{j+1})/2) mod 2), with the Lucas
submask fold

    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o]
    nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }   = wt(Phi_n h),

is the set { n : nu2(n)/n < c } SPARSE (empty / density -> 0 as the tail
window slides right)? We measure the REAL dip density over a FINE sweep of c
in 0.40, 0.41, ..., 0.49 (step 0.01) in three windows — full [50,N], half
[N//2,N], tail [int(0.9*N), N] — plus the min of nu2(n)/n over each tail/
window, and report exactly WHERE sparsity breaks:
    - the largest c for which the tail window contains NO dips (empty tail),
    - the exact c at which the tail dip density first turns positive.

FLOORED ORACLE (the fix that de-vacuates this script): every nu2(n) comes from
lib.supply_fold.s_sos(n, h[:n]) — the submask-PRODUCT SOS transform, which the
library cross-checks against the direct submask-XOR oracle s_direct on
n=4..200 and spots 53,64,100. This is the CANONICAL floored fold used by
chebyshev_second_moment.py. The VACUOUS path (literal geometric suffix) gives
nu2(n)=0 for every n and is explicitly rejected: two top-of-file assertions
guard against a zeroed oracle —
    assert nu2(53) == 18          (the real value; liberty d in [2,52])
    assert |mu_4000 - 0.4977| <= 0.01
so a literal-suffix (identically-0) oracle aborts immediately instead of
quietly reporting vacuous density-1 everywhere.

FLOAT-TRAP SAFETY: every threshold c is built as Fraction(hundredths, 100)
with integer hundredths (40..49), and every comparison is Fraction(nu2[n], n)
< c in exact rational arithmetic. n=145 has nu2(145)/145 = 58/145 = 0.4
exactly; using float 0.40 = 0.40000000000000002220 would wrongly swallow it.
Nothing here is a float until the display ratios at the end.

STREAMING: nu2[] is computed in STAGE 1 in parallel over n (each n independent,
O(n log n) SOS per n), never materialising any O(N^2) triangle; memory is
O(N) (one int array). Exact Fractions for all reductions; only display ratios
are floats.

NEGATIVE CONTROLS (both MUST fail, i.e. dips dense, NOT sparse):
  - ALL-ONES h: nu2 = O(1), ratio -> 0, tail dip density 1.0 (vacuous).
  - THUE-MORSE h: nu2/n collapses ~0.27 -> ~0.011, tail density ~1.0.
These show sparsity of the fine sweep is specific to the prime h.

ALL NUMBERS ARE MEASURED, NOT PROVED.

Usage: python3 dip_sparsity_monotonic.py [N] [nproc] [ctrlN]
Writes: code/out/dip_sparsity_monotonic.txt
"""
import sys
import os
import time
import multiprocessing as mp
from fractions import Fraction

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string
from lib.nu2 import fold_nu2
from lib.nu2_guard import assert_supply_guard, scene_header

# FINE sweep: c = hundredths/100 for hundredths in 40..49, exact Fractions.
FINE = [Fraction(h, 100) for h in range(40, 50)]   # 0.40,0.41,...,0.49
MU0 = Fraction("0.4977")          # reference mu_4000 (measured ~0.4973)
TOL = Fraction(1, 100)            # within 0.01


def prime_h(n):
    """h[j] = [r_{j+2} != r_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


def verify_oracle(h, spots=(53, 64, 100)):
    """s_sos == s_direct on n=4..200 and at the given spots."""
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
# STAGE 1: parallel nu2 (exact, per-n s_sos)
# ---------------------------------------------------------------------------

def _worker(args):
    lo, hi, h = args
    res = []
    for n in range(lo, hi + 1):
        res.append((n, fold_nu2(n, h)))
    return res


def compute_nu2(N, h, nproc):
    """nu2[] indexed 0..N by parallel s_sos over n=2..N. O(N^2 log N) total
    work split across nproc workers, O(N) memory."""
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


def mu_N(nu2, N):
    """mu_N = (1/N) * sum_{n=2..N} nu2(n)/n, exact Fraction."""
    s = Fraction(0)
    for n in range(2, N + 1):
        s += Fraction(nu2[n], n)
    return s / N


# ---------------------------------------------------------------------------
# STAGE 2: exact fine dip sweeps (single pass over nu2[])
# ---------------------------------------------------------------------------

def fine_dips(nu2, N, fine):
    """For each window (full/half/tail) and each exact c in `fine`, count
    { n in window : Fraction(nu2[n], n) < c }. Also min of nu2/n over each
    window. Returns (dip_table, window_min, tail_first_positive, tail_last_empty)
    where dip_table[(rname,c)] = (count, width, density_float), window_min maps
    rname -> exact Fraction min, tail bootstraps are reported separately.

    O(N * |fine|) time, exact arithmetic."""
    windows = [("full", 50, N), ("half", N // 2, N),
               ("tail", int(0.9 * N), N)]
    dip = {}
    wmin = {}
    tail_first_positive = None     # smallest c in `fine` with a tail dip
    tail_last_empty = None         # largest c in `fine` with tail dip count 0
    for (rname, lo, hi) in windows:
        cnt_by_c = {c: 0 for c in fine}
        mn = None
        for n in range(lo, hi + 1):
            r = Fraction(nu2[n], n)
            if mn is None or r < mn:
                mn = r
            for c in fine:
                if r < c:
                    cnt_by_c[c] += 1
        wmin[rname] = mn
        width = hi - lo + 1
        if rname == "tail":
            for c in fine:
                if cnt_by_c[c] == 0:
                    tail_last_empty = c
                else:
                    if tail_first_positive is None:
                        tail_first_positive = c
        for c in fine:
            cnt = cnt_by_c[c]
            dip[(rname, c)] = (cnt, width, cnt / width if width else 0.0)
    return dip, wmin, tail_first_positive, tail_last_empty


def format_capture(label, N, fine, nu2, elapsed):
    L = []
    L.append(f"=== {label} : N = {N}  (streamed {elapsed:.1f}s) ===")
    dip, wmin, tail_first, tail_last = fine_dips(nu2, N, fine)
    L.append("FINE dip density { n : nu2(n)/n < c } per window and c:")
    L.append("   c     full-dens   half-dens   tail-dens   tail-count/width"
             "   (min over tail)")
    for c in fine:
        _, _, dfull = dip[("full", c)]
        _, _, dhalf = dip[("half", c)]
        cnt_t, w_t, dtail = dip[("tail", c)]
        L.append(f"  {float(c):.2f}   {dfull:.6f}   {dhalf:.6f}   "
                 f"{dtail:.6f}     {cnt_t:5d}/{w_t:5d}"
                 f"     ({float(wmin['tail']):.6f})")
    L.append(f"window min of nu2(n)/n: full={float(wmin['full']):.6f}  "
             f"half={float(wmin['half']):.6f}  tail={float(wmin['tail']):.6f}")
    L.append(f"SPARSITY BREAK (tail window):")
    if tail_last is not None:
        L.append(f"  largest c whose tail window is EMPTY of dips = "
                 f"{float(tail_last):.2f}  ({tail_last})")
    else:
        L.append(f"  largest c whose tail window is EMPTY of dips = "
                 f"NONE  (tail has dips at every c in sweep)")
    if tail_first is not None:
        L.append(f"  exact c where tail dip density first turns positive = "
                 f"{float(tail_first):.2f}  ({tail_first})")
    else:
        L.append(f"  exact c where tail dip density first turns positive = "
                 f"NONE  (tail empty of dips at every c in sweep)")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------

def run_capture(N, h, label, nproc, out_lines):
    t0 = time.time()
    nu2 = compute_nu2(N, h, nproc)
    out_lines.append(f"[{label}] STAGE1 parallel nu2 (n=2..{N}) in "
                     f"{time.time()-t0:.1f}s (nproc={nproc})")
    if label == "PRIMES":
        # the two agreed assertions, computed from the SAME nu2 stream
        assert nu2[53] == 18, f"nu2(53) = {nu2[53]} != 18  (zeroed oracle?)"
        mu = mu_N(nu2, 4000)
        assert abs(mu - MU0) <= TOL, \
            f"mu_4000 = {float(mu):.6f} not within 0.01 of 0.4977 (zeroed oracle?)"
        out_lines.append(f"[PRIMES] assertion nu2(53)==18 OK; mu_4000="
                         f"{float(mu):.6f} (within 0.01 of 0.4977) OK")
    out_lines.append(format_capture(label, N, FINE, nu2, time.time() - t0))
    return nu2


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    CtrlN = int(sys.argv[3]) if len(sys.argv) > 3 else 4000

    out = []
    t_start = time.time()

    # mandatory entry guard (directive 11/12)
    assert_supply_guard(N)
    out.append("[guard] assert_supply_guard(%d): nu2(53)==18, nu2(64)==27, "
               "primes mu_4000 within 0.01 of 0.4977 — canonical oracle OK" % N)

    # oracle cross-check on primes at the top
    h_check = prime_h(N + 2)
    verify_oracle(h_check)
    out.append("oracle: s_sos == s_direct on n=4..200 and spots 53,64,100 "
               "(prime h): OK")
    out.append(scene_header('PRIMES-dip-sparsity',
                            'lib.nu2.fold_nu2=lib.supply_fold.s_sos', 2, N))

    # primes at full ceiling
    hP = prime_h(N + 1)
    run_capture(N, hP, "PRIMES", nproc, out)

    # negative controls at CtrlN
    for lab, hsrc in [("ALL-ONES h (neg control, must fail: vacuous)",
                       all_ones_h),
                      ("THUE-MORSE h (neg control, must fail)", thue_morse_h)]:
        hC = hsrc(CtrlN)
        run_capture(CtrlN, hC, lab, min(nproc, CtrlN), out)

    text = "\n".join(out) + "\n"
    text += f"TOTAL runtime: {time.time()-t_start:.1f}s; exact ceiling N={N}\n"
    print(text)

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "dip_sparsity_monotonic_fixed.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
