#!/usr/bin/env python3
"""Independent re-sample (S=8000, fresh RNG) of the fraction nu2/n>=0.40 at
weights around the reported first_typical for the third-pass column, to check
the threshold is not a 1-sigma fluke of a single S=4000 sample."""
import sys
import numpy as np
from weights.linear_supply_threshold_extend import batch_sos_ones
from scholar.threshold_limit_run import ExactMean

n = int(sys.argv[1])
first = int(sys.argv[2])
em = ExactMean(n)
for w in [first - 1, first, first + 1]:
    S = 8000
    rng = np.random.default_rng(999983 + 7919 * n + w)
    hb = np.zeros((S, n), dtype=np.int8)
    for i in range(S):
        pos = rng.choice(n, size=w, replace=False)
        hb[i, pos] = 1
    nu2 = batch_sos_ones(n, hb)
    frac = np.count_nonzero(nu2 / n >= 0.40) / S
    mean = float(em.mean_as_float(w))
    print(f"n={n} w={w} w/n={w/n:.5f} exact_mean={mean:.4f} frac(S=8000)={frac:.4f}")
