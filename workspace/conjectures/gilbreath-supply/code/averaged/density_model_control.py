#!/usr/bin/env python3
"""TASK A — density-matched model control for the averaged SUPPLY fold.

Question: the prime switch-bit h[j] = [q_{j+2} != q_{j+1} mod 4] has an
averaged mean M(N) = (1/N) sum_{n=2..N} nu2(n)/n that rises to ~0.4973 at
N=4000. Does that rising signal survive a *density-matched* random model? I.e.
is it special to the primes, or is it the fold's generic value for balanced
strings?

Controls:
  * primes  h : the real object.
  * Bernoulli(p) with p = measured prime switch density (~0.597) — random
    strings with the SAME 1-density as the primes.
  * Bernoulli(0.5) — balanced random strings.
  * Thue-Morse (h[j] = popcount(j) mod 2) — deterministic, density 1/2, but
    the ONE balanced family whose fold mean provably -> 0.

This cannot be done by enumeration of all strings (that is the adversary); it
is a Monte Carlo estimate over a handful of random trials, which is legitimate
— the claim being tested is the generic (averaged) value of the fold on random
inputs, and randomness is used only to sample that generic value, not to
search for a counterexample.

Method: every nu2(n) via the O(n log n) submask-product SOS fold
(lib.supply_fold.s_sos), exact integers. Verified below against the literal
submask-XOR oracle s_direct at several n. M(N) = (1/N) sum_{n=2..N} nu2(n)/n.

Arithmetic exact; only ratios/means/stds are float.
"""
import os
import random
from fractions import Fraction

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string
from lib.nu2 import fold_nu2
from lib.nu2_guard import assert_supply_guard, scene_header


SAMPLES = [100, 500, 1000, 2000, 4000]


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 1)


def ber_h(n, p, rng):
    return [1 if rng.random() < p else 0 for _ in range(n)]


def thue_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


def mean_at_n(h, N):
    """M(N) = (1/N) sum_{n=2..N} nu2(n)/n, exact Fraction, then float."""
    total = Fraction(0)
    for n in range(2, N + 1):
        total += Fraction(fold_nu2(n, h), n)
    return float(total / N)


def verify_oracle():
    """fold_nu2 (SOS) vs s_direct (literal submask XOR) on the prime h."""
    r = []
    # prime h through index N
    from lib.primes import mod4_string
    h = prime_h(70)
    lines = []
    for n in [4, 8, 16, 32, 64]:
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        fold = fold_nu2(n, h)
        ok = (Sd == Ss == (n - 2 - 2 * fold)) and (od == os_ == fold)
        lines.append(f"  n={n:3d}  s_direct={od}  s_sos={os_}  fold_nu2={fold}  "
                     f"agree={ok}")
    return lines


def run_task_a(out):
    # --- density of prime switch bits (Task A preamble) ---
    hn = 4000
    hfull = prime_h(hn)
    ones = sum(hfull)
    dens = ones / hn
    seg = hfull[50:hn]
    dens50 = sum(seg) / len(seg) if seg else 0.0
    out.append("=" * 70)
    out.append("TASK A — density-matched model control (averaged fold mean)")
    out.append("=" * 70)
    out.append("PRIME switch-bit density (measured)")
    out.append(f"  ones(h[0..{hn-1}]) = {ones}  density over full length = {dens:.4f}")
    out.append(f"  density over [50,{hn}) = {dens50:.4f}")
    out.append(f"  (prompt guessed ~0.575; actual measured = {dens:.4f})")
    out.append("")

    p = ones / hn   # measured prime switch density, used for the matched model

    # --- oracle verification ---
    out.append("VERIFY fold_nu2 (SOS) == s_direct (literal oracle) on prime h")
    out.extend(verify_oracle())
    out.append("")

    # --- prime M(N) (deterministic) ---
    out.append("PRIME  M(N) = (1/N) sum_{n=2..N} nu2(n)/n   (exact via s_sos)")
    primeM = {}
    for N in SAMPLES:
        primeM[N] = mean_at_n(prime_h(N + 1), N)
        out.append(f"  M({N:5d}) = {primeM[N]:.4f}")
    out.append("")

    # --- Thue-Morse (deterministic, density 1/2) ---
    out.append("THUE-MORSE  M(N)  (density 1/2 but fold mean -> 0)")
    thueM = {}
    for N in SAMPLES:
        thueM[N] = mean_at_n(thue_h(N + 1), N)
        out.append(f"  M({N:5d}) = {thueM[N]:.4f}")
    out.append("")

    # --- random models ---
    NUM_TRIALS = 20
    out.append(f"RANDOM MODELS: {NUM_TRIALS} independent trials per model;")
    out.append("  each trial = one fresh Bernoulli string of length 4001, all")
    out.append("  sample points read from the same string (prefix-consistent).")
    out.append(f"  Bernoulli(p) with p = measured prime density = {p:.4f}")
    out.append(f"  Bernoulli(0.5) balanced control.")
    out.append("  Per N: mean over trials, spread min/max, sample std (numpy, 1ddof).")
    out.append("")

    import numpy as np
    rng = random.Random(12345)
    trials_p = {N: [] for N in SAMPLES}
    trials_5 = {N: [] for N in SAMPLES}

    # Interleave both models per trial so the total wall time stays bounded:
    # 20 trials x 2 models x ~3.6s (full 4000 fold) ~= 145s.
    for t in range(NUM_TRIALS):
        hp = ber_h(4001, p, rng)
        h5 = ber_h(4001, 0.5, rng)
        for N in SAMPLES:
            trials_p[N].append(mean_at_n(hp, N))
            trials_5[N].append(mean_at_n(h5, N))

    out.append(f"{'N':>6} {'primeM':>8} {'Ber(p) mean':>11} {'std':>7} "
               f"{'min':>7} {'max':>7} | {'Ber(0.5) mean':>13} {'std':>7} "
               f"{'min':>7} {'max':>7} | {'ThueM':>7}")
    for N in SAMPLES:
        vp = np.array(trials_p[N])
        v5 = np.array(trials_5[N])
        out.append(
            f"{N:>6} {primeM[N]:>8.4f} {vp.mean():>11.4f} {vp.std(ddof=1):>7.4f} "
            f"{vp.min():>7.4f} {vp.max():>7.4f} | "
            f"{v5.mean():>13.4f} {v5.std(ddof=1):>7.4f} {v5.min():>7.4f} "
            f"{v5.max():>7.4f} | {thueM[N]:>7.4f}")

    out.append("")
    out.append(f"Trials used: {NUM_TRIALS} (total run kept within ~600s; "
               f"prime/thue deterministic, no trials).")
    return out


def main():
    assert_supply_guard(4000)
    out = run_task_a([])
    out.insert(0, scene_header('PRIMES-density-model-control',
                               'lib.nu2.fold_nu2=lib.supply_fold.s_sos', 2, 4000))
    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "density_model_control.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
