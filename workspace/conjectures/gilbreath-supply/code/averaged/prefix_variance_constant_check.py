#!/usr/bin/env python3
"""TASK 2 — THE CONSTANT CHECK: prefix variance s2_N of nu2(n)/n for the
primes vs the FAIR-MODEL (uniform random h) prediction.

Hypothesis under test: the empirical prefix variance

    s2_N = (1/(N-1)) * sum_{n=2..N} (nu2(n)/n - mu_N)^2

decays like the fair-model (uniform random h) prediction. For uniform h the
per-n value nu2(n) is (in the naive independent-cell model) Binomial(n-2,1/2),
so per-n Var(nu2(n)/n) ~ 1/(4n); a naive prefix-average over n then suggests
~ (ln N)/(4N). BUT the nu2(n) windows overlap in h, so the true fair prefix
variance may differ from that naive curve. This script lets the Monte Carlo
settle the actual fair value and compares the primes to it.

Three printed numbers per checkpoint for the primes (part a):
    s2_N              exact (Fractions -> float)
    s2_N * 4 * N      the "4*s2_N*N" curve
    s2_N * 4 * N / ln(N)

Part (b) Monte Carlo:
    ~30 independent uniform-random h strings of length ~4100, exact s_sos per
    n, s2_N at the same checkpoints, averaged over trials -> mean fair s2_N.
    Prints primes_s2 / fair_s2 at each N.

Comparator:
    per-n variance 1/(4n) (NaiveBinom curve, printed at n = each N).

All numbers are MEASURED, not proved. nu2(53)==18 asserted before trusting the
oracle (against the literal submask-XOR oracle).

Signature: python3 prefix_variance_constant_check.py [Ntrials] [nproc]
Writes code/out/prefix_variance_constant_check.txt
"""
import sys
import os
import time
import math
import random
import multiprocessing as mp
from fractions import Fraction

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string

CHECKPOINTS = [100, 400, 1000, 2000, 4000]
TRIALS = 30
LENGTH = 4100


def prime_h(n):
    return h_string(n + 1)[:n]


def uniform_h(n, rng):
    return [1 if rng.random() < 0.5 else 0 for _ in range(n)]


def assert_oracle():
    """nu2(53)==18 and s_sos==s_direct on a spread of n, prime h.
    Returns the n=53 nu2 value."""
    h = prime_h(4200)
    # 53
    Sd, od = s_direct(53, h[:53])
    Ss, os_ = s_sos(53, h[:53])
    assert od == 18 and os_ == 18 and Sd == Ss, (od, os_, Sd, Ss)
    for n in (8, 16, 32, 64, 100, 128, 256):
        Sd, od = s_direct(n, h[:n])
        Ss, os_ = s_sos(n, h[:n])
        assert od == os_ and Sd == Ss, (n, od, os_, Sd, Ss)
    return od  # od here is the last loop value, n=256


def prefix_s2(nu2, N):
    """s2_N = population variance of {nu2(n)/n : n=2..N}, exact Fractions.
    Returns (mu_N, s2_N) as Fractions, plus count."""
    S1 = Fraction(0)
    S2 = Fraction(0)
    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        S1 += r
        S2 += r * r
    cnt = N - 1
    mu = S1 / cnt
    s2 = S2 / cnt - mu * mu
    return mu, s2, cnt


def compute_all_nu2(maxN, h):
    """nu2[0..maxN] via exact s_sos, one n at a time, O(N log N) memory O(N).
    Single-threaded; used inside each worker for one h string."""
    nu2 = [0] * (maxN + 1)
    for n in range(2, maxN + 1):
        _, ones = s_sos(n, h[:n])
        nu2[n] = ones
    return nu2


def _worker(seed):
    """One fair-model trial: uniform h, exact s2_N at each checkpoint."""
    rng = random.Random(seed)
    h = uniform_h(LENGTH, rng)
    nu2max = max(CHECKPOINTS)
    hmax = h[:nu2max]
    # reduce to max needed length (can't reuse full LENGTH window slice per n)
    nu2 = [0] * (nu2max + 1)
    for n in range(2, nu2max + 1):
        _, ones = s_sos(n, hmax[:n])
        nu2[n] = ones
    res = {}
    for N in CHECKPOINTS:
        mu, s2, cnt = prefix_s2(nu2, N)
        res[N] = (float(mu), float(s2))
    return res


def main():
    TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    out = []
    t0 = time.time()
    out.append("=" * 78)
    out.append("TASK 2 — THE CONSTANT CHECK: prefix variance s2_N of nu2(n)/n")
    out.append("        primes vs FAIR-MODEL (uniform random h)")
    out.append("=" * 78)

    # --- oracle assertion ---
    a53 = assert_oracle()
    out.append(f"oracle: nu2(53)==18 asserted (got {a53} for n=256 loop tail; "
               f"n=53 assert passed), s_sos==s_direct on n in {{8,16,32,64,100,"
               f"128,256}}: OK")

    # --- part (a): primes, deterministic, exact ---
    out.append("")
    out.append("(a) PRIMES (deterministic, exact s_sos)")
    out.append("    s2_N = pop-var of {nu2(n)/n : n=2..N};  mu_N its mean")
    hP = prime_h(max(CHECKPOINTS) + 1)
    pnu2 = [0] * (max(CHECKPOINTS) + 1)
    for n in range(2, max(CHECKPOINTS) + 1):
        _, ones = s_sos(n, hP[:n])
        pnu2[n] = ones
    out.append(f"  {'N':>6} {'mu_N':>10} {'s2_N':>14} {'s2_N*4*N':>12} "
               f"{'s2_N*4*N/lnN':>14} {'1/(4N)':>10}")
    prime_s2 = {}
    for N in CHECKPOINTS:
        mu, s2, cnt = prefix_s2(pnu2, N)
        s2f = float(s2)
        lnN = math.log(N)
        out.append(f"  {N:>6} {float(mu):>10.6f} {s2f:>14.8f} "
                   f"{s2f*4*N:>12.6f} {s2f*4*N/lnN:>14.6f} {1/(4*N):>10.7f}")
        prime_s2[N] = s2f

    # --- part (b): fair-model Monte Carlo ---
    out.append("")
    out.append(f"(b) FAIR-MODEL Monte Carlo: {TRIALS} independent uniform h "
               f"strings, length {LENGTH}, exact s_sos")
    out.append(f"    nproc={nproc}")
    t1 = time.time()
    with mp.Pool(nproc) as pool:
        results = list(pool.imap(_worker, range(TRIALS), chunksize=1))
    dt = time.time() - t1

    fair_s2 = {N: [] for N in CHECKPOINTS}
    for r in results:
        for N in CHECKPOINTS:
            fair_s2[N].append(r[N][1])

    import numpy as np
    out.append(f"  ({time.time()-t0:.0f}s elapsed, Monte Carlo block {dt:.0f}s)")
    out.append(f"  {'N':>6} {'fair mean s2':>14} {'fair std':>10} "
               f"{'fair s2*4*N':>13} {'primes/fair':>12} {'fair 1/(4N)':>12}")
    for N in CHECKPOINTS:
        v = np.array(fair_s2[N])
        fm = v.mean()
        fstd = v.std(ddof=1)
        ratio = prime_s2[N] / fm
        out.append(f"  {N:>6} {fm:>14.8f} {fstd:>10.8f} {fm*4*N:>13.6f} "
                   f"{ratio:>12.4f} {1/(4*N):>12.7f}")

    # summary line
    N_last = CHECKPOINTS[-1]
    ratio_last = prime_s2[N_last] / float(np.array(fair_s2[N_last]).mean())
    verdict = ("above" if ratio_last > 1.2 else
               ("below" if ratio_last < 0.8 else "on"))
    out.append("")
    out.append(f"SUMMARY: at N={N_last} primes_s2/fair_s2 = {ratio_last:.3f} "
               f"=> primes sit {verdict} the fair-model (uniform h) variance.")
    out.append("LABEL: measured, not proved.")

    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "prefix_variance_constant_check.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
