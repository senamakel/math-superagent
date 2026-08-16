#!/usr/bin/env python3
"""TASK push-prefix-variance-null-40000 (directive 15/16): push the
like-for-like prefix-variance null — primes vs fair-model (uniform random h)
— to the N=40000 ceiling.

s2_N = population variance of {nu2(n)/n : n=2..N} (exact Fractions), the
prefix statistic. Part (a) primes (deterministic exact). Part (b) fair-model
Monte Carlo over TRIALS independent uniform-h strings. Both parallelised over
n / over (trial) so the 40000-ceiling sweep completes in this run.

Checkpoints include 10000, 20000, 40000 beyond the old 4000 ceiling.
Deliverable: primes_s2/fair_s2 at N=40000, and whether the ratio tends to 1,
to a constant above 1, or keeps falling from 1.283@4000.

Oracle: s_sos cross-checked against s_direct (literal submask-XOR); entry
assert nu2(53)==18. All numbers measured, not proved.

Signature: python3 push_prefix_variance_40000.py [TRIALS] [nproc]
Writes code/out/prefix_variance_null_40000.txt
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

CHECKPOINTS = [100, 400, 1000, 2000, 4000, 10000, 20000, 40000]
MAXN = 40000
TRIALS = 8
LENGTH = MAXN + 3

# global store of generated fair h arrays, inherited by forked workers
_HSTORE = {}
_PSTORE = {}


def prime_h(n):
    return h_string(n + 1)[:n]


def uniform_h(n, rng):
    return [1 if rng.random() < 0.5 else 0 for _ in range(n)]


def assert_oracle():
    """nu2(53)==18 and s_sos==s_direct on several n (prime h)."""
    h = prime_h(4200)
    for n in (8, 16, 32, 53, 64, 100, 128, 256):
        Sd, od = s_direct(n, h[:n])
        Ss, os_ = s_sos(n, h[:n])
        assert od == os_ and Sd == Ss, (n, od, os_, Sd, Ss)
        if n == 53:
            assert od == 18, (od,)
    return True


def _nu2_one(n, h_full):
    """nu2(n) from a shared h array (submask-product SOS)."""
    _, ones = s_sos(n, list(h_full[:n]))
    return n, ones


def _prime_n(n):
    _, ones = s_sos(n, list(_PSTORE[0][:n]))
    return n, ones


def sweep_parallel(h, maxN, nproc):
    """nu2[2..maxN] parallelised over n. h is a list length >= maxN."""
    global _PSTORE
    _PSTORE[0] = h
    with mp.Pool(nproc) as pool:
        res = pool.map(_prime_n, range(2, maxN + 1),
                       chunksize=max(1, maxN // (nproc * 8)))
    nu2 = [0] * (maxN + 1)
    for n, v in res:
        nu2[n] = v
    return nu2


def _trial_n(args):
    """(trial, n) -> nu2[n] for a pre-generated fair h in the global store.
    Uses fork inheritance of _HSTORE (Linux default start method)."""
    trial, n = args
    h = _HSTORE[trial]
    _, ones = s_sos(n, h[:n])
    return trial, n, ones


def prefix_s2(nu2, N):
    """s2_N = pop-var of {nu2(n)/n : n=2..N}, exact Fractions."""
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


def main():
    TRI = int(sys.argv[1]) if len(sys.argv) > 1 else TRIALS
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    out = []
    t0 = time.time()
    out.append("=" * 78)
    out.append("PUSH PREFIX-VARIANCE NULL TO N=40000 (directive 15/16)")
    out.append("prefix variance s2_N of nu2(n)/n: primes vs fair-model (uniform h)")
    out.append("=" * 78)

    assert_oracle()
    out.append(f"oracle: nu2(53)==18 asserted, s_sos==s_direct on "
               f"{{8,16,32,53,64,100,128,256}}: OK")

    # ---- part (a): primes, deterministic, parallel over n ----
    out.append("")
    out.append("(a) PRIMES (deterministic, exact s_sos, parallel over n)")
    hP = prime_h(MAXN + 1)
    ta = time.time()
    pnu2 = sweep_parallel(hP, MAXN, nproc)
    out.append(f"    prime sweep to {MAXN}: {time.time()-ta:.0f}s")
    p_mu = {}
    p_s2 = {}
    out.append(f"  {'N':>7} {'mu_N':>10} {'s2_N':>14} {'s2_N*4*N':>12} "
               f"{'s2_N*4*N/lnN':>14}")
    for N in CHECKPOINTS:
        mu, s2, _ = prefix_s2(pnu2, N)
        s2f = float(s2)
        lnN = math.log(N)
        p_mu[N] = float(mu)
        p_s2[N] = s2f
        out.append(f"  {N:>7} {float(mu):>10.6f} {s2f:>14.8f} "
                   f"{s2f*4*N:>12.6f} {s2f*4*N/lnN:>14.6f}")

    # ---- part (b): fair-model Monte Carlo, parallel over (trial, n) ----
    out.append("")
    out.append(f"(b) FAIR-MODEL Monte Carlo: {TRI} independent uniform h "
               f"strings, length {LENGTH}, exact s_sos")
    out.append(f"    nproc={nproc}")
    tb = time.time()
    global _HSTORE
    for t in range(TRI):
        rng = random.Random(1000 + t)
        _HSTORE[t] = uniform_h(LENGTH, rng)
    tasks = [(t, n) for t in range(TRI) for n in range(2, MAXN + 1)]
    with mp.Pool(nproc) as pool:
        results = list(pool.imap(_trial_n, tasks, chunksize=2048))
    out.append(f"    Monte Carlo block {time.time()-tb:.0f}s "
               f"(tot {time.time()-t0:.0f}s)")
    import numpy as np
    fair_nu2 = {t: [0] * (MAXN + 1) for t in range(TRI)}
    for trial, n, ones in results:
        fair_nu2[trial][n] = ones
    for t in range(TRI):
        _HSTORE.pop(t, None)   # release the big arrays promptly
    fair_s2 = {N: [] for N in CHECKPOINTS}
    fair_mu = {N: [] for N in CHECKPOINTS}
    for t in range(TRI):
        for N in CHECKPOINTS:
            mu, s2, _ = prefix_s2(fair_nu2[t], N)
            fair_s2[N].append(float(s2))
            fair_mu[N].append(float(mu))
    out.append(f"  {'N':>7} {'fair mean s2':>14} {'fair std':>10} "
               f"{'fair s2*4*N':>13} {'primes/fair':>12}")
    ratios = {}
    for N in CHECKPOINTS:
        v = np.array(fair_s2[N])
        fm = v.mean()
        fstd = v.std(ddof=1)
        ratio = p_s2[N] / fm
        ratios[N] = ratio
        out.append(f"  {N:>7} {fm:>14.8f} {fstd:>10.8f} {fm*4*N:>13.6f} "
                   f"{ratio:>12.4f}")

    N_last = CHECKPOINTS[-1]
    r = ratios[N_last]
    # trend across the last three checkpoints
    tr = [ratios[20000], ratios[40000]]
    falling = tr[1] < tr[0] - 0.02
    to_one = abs(tr[1] - 1.0) < 0.05
    out.append("")
    out.append(f"SUMMARY: at N={N_last} primes_s2/fair_s2 = {r:.3f} "
               f"(ratios 20000={ratios[20000]:.3f}, 40000={r:.3f})")
    if to_one:
        out.append("=> ratio ~ 1: primes asymptotically indistinguishable from "
                   "uniform for this statistic")
    elif falling:
        out.append("=> ratio still falling: excess is shrinking toward a "
                   "constant (converging from {:.3f}@20000 to {:.3f}@40000)"
                   .format(ratios[20000], r))
    else:
        verdict = "above 1" if r > 1.05 else "on"
        out.append(f"=> ratio holds {verdict} 1: a constant excess that does "
                   f"not shrink")
    out.append("LABEL: measured, not proved.")

    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "prefix_variance_null_40000.txt"), "w") as f:
        f.write(text)
    print("WROTE code/out/prefix_variance_null_40000.txt")


if __name__ == "__main__":
    main()
