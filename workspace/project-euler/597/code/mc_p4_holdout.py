#!/usr/bin/env python3
"""Independent high-sample Monte Carlo estimate of p(4,L) at held-out L values.

Task: for each L in {2200, 2600, 3200}, draw N = 2e6 iid speed vectors
v = [expovariate(1.0) for _ in range(4)] (the problem's Exp(1) speeds), get the
race parity from brute.outcome_parity(4, L, v), and report the even fraction
with binomial standard error. Purpose: an independent, from-scratch estimate of
p(4,L) at three points held out of the exact-data set, to check against exact
rational values (computed separately; NOT assumed here).

Self-check: before the held-out points the driver runs an anchor at L=1800,
whose exact value 166802/317985 ~= 0.5245593 is in the library
(code/out/exact_p4_extra.json, code/p4_fit_analysis.py P4 dict). If the MC
estimate is within ~3 SE of it, the driver path is validated end to end.

Usage:  python3 mc_p4_holdout.py [N] [seed]
Defaults: N=2_000_000 per L, seed=20240607.
"""
import math
import random
import sys

from brute import outcome_parity

ANCHOR = (1800, 166802, 317985)  # (L, num, den) exact p(4,L) from library


def mc(n, L, N, seed):
    """Even-parity fraction over N iid Exp(1) speed vectors (exact draws)."""
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, v) == 0:
            even += 1
    return even / N


def report(label, L, phat, N, exact=None):
    se = math.sqrt(phat * (1.0 - phat) / N)
    line = (f"{label}: n=4 L={L}  p_hat={phat:.10f}  SE={se:.6f}  "
            f"95% CI=[{phat-1.96*se:.6f},{phat+1.96*se:.6f}]")
    if exact is not None:
        diff = phat - exact
        line += f"  |diff|/SE={abs(diff)/se:.2f} (exact={exact:.10f})"
    print(line)
    return phat, se


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20240607

    # --- self-check at a known exact value -------------------------------
    L0, num, den = ANCHOR
    phat0 = mc(4, L0, N // 10, seed)
    report("anchor", L0, phat0, N // 10, exact=num / den)

    # --- the three held-out points, full sample count ---------------------
    results = {}
    for i, L in enumerate([2200, 2600, 3200]):
        phat, se = report("holdout", L, mc(4, L, N, seed + 1000 * i), N)
        results[L] = {"p_hat": phat, "se": se, "N": N}

    print("\nSummary (independent MC, no exact values used in estimation):")
    for L in results:
        r = results[L]
        print(f"  p(4,{L}) = {r['p_hat']:.10f} +/- {r['se']:.6f}")


if __name__ == "__main__":
    main()