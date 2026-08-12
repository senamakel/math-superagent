"""Monte Carlo sanity check for Project Euler 493.

Setup: 70 balls, 7 colours x 10 each. Draw 20 balls without replacement,
record the number of distinct colours present. Average over many trials and
compare against the exact expected value.

Exact value derivation: for one fixed colour, the chance it is ABSENT from the
draw is C(60,20)/C(70,20) (pick the 20 balls that are not this colour from the
60 balls of the other colours). So the probability a given colour is present is
1 - C(60,20)/C(70,20). Linearity of expectation over the 7 indicator variables
gives E[distinct] = 7*(1 - C(60,20)/C(70,20)).
"""

import math
import random

N_TRIALS = 2_000_000
SEED = 493


def exact_value():
    """E[number of distinct colours] by linearity of expectation (exact)."""
    p_absent = math.comb(60, 20) / math.comb(70, 20)
    return 7.0 * (1.0 - p_absent)


def simulate(trials, seed):
    rng = random.Random(seed)
    total = 0.0
    total_sq = 0.0
    for _ in range(trials):
        draw = rng.sample(range(70), 20)
        colours = {b // 10 for b in draw}
        d = len(colours)
        total += d
        total_sq += d * d
    return total, total_sq


def main():
    exact = exact_value()
    total, total_sq = simulate(N_TRIALS, SEED)

    mean = total / N_TRIALS
    var = total_sq / N_TRIALS - mean * mean
    # Standard error of the mean = sample sd / sqrt(n)
    std_err = math.sqrt(max(var, 0.0) / N_TRIALS)

    diff = mean - exact
    # number of standard errors the estimate sits from the exact value
    z = diff / std_err if std_err > 0 else float("inf")

    print(f"Exact expected value          : {exact:.10f}")
    print(f"Monte Carlo mean (n={N_TRIALS}): {mean:.10f}")
    print(f"Sample standard error of mean : {std_err:.6f}")
    print(f"Difference (MC - exact)       : {diff:.6f}")
    print(f"Number of SEs from exact      : {z:.3f}")
    print(f"Mean to 4 d.p.                : {mean:.4f}")

    within = abs(z) <= 3.0  # a few standard errors
    status = "within" if within else "OUTSIDE"
    print(f"\nThe Monte Carlo mean is {status} a few standard errors of the exact value.")
    if not within:
        print("WARNING: estimate and exact value disagree beyond expected noise.")


if __name__ == "__main__":
    main()
