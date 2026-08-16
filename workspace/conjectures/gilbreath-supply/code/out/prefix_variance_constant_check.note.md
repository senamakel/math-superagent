# Prefix variance of nu2/n follows the fair-model law, primes above

Result of the constant check (directive): does s2_N — the prefix variance of
nu2(n)/n over n ≤ N — track the fair-model (uniform random h) prediction?

## Measurement (exact s_sos, checked nu2(53)==18)

| N | primes s2_N | s2_N·4N/lnN | fair mean s2 (30 trials) | primes/fair |
|---|---|---|---|---|
| 100  | 0.0165951  | 1.441 | 0.011863 | 1.399 |
| 400  | 0.0054576  | 1.457 | 0.004029 | 1.355 |
| 1000 | 0.0024916  | 1.443 | 0.001875 | 1.329 |
| 2000 | 0.0013445  | 1.415 | 0.001033 | 1.302 |
| 4000 | 0.0007216  | 1.392 | 0.000562 | 1.283 |

Both scale like ~lnN/(4N): primes s2·4N/lnN ≈ 1.39, fair ≈ 1.08 (the naive
(lnN)/(4N) underestimates the fair value because overlapping nu2 windows
inflate it, settled by Monte Carlo). Primes sit ABOVE the fair-model variance
by 1.28–1.40× across N, ratio drifting toward 1. The per-n fair variance is
exactly (n−2)/(4n²) ≈ 1/(4n), from Binomial(n−2,1/2).

The primes' variance exceeds the uniform-string prediction by ~30% at N=4000 —
the wrong direction for a concentration argument — but is of the same order.
This is a modest excess, not a structural deviation.

## The consequence for the density-1 step

s2_N → 0 is NOT prime-specific: the fair model has the same law. "Variance
vanishes" is the fold's generic behaviour on any input, so a GOAL priority-1
argument driven by a decaying variance cannot separate the primes from a
uniform string. What *does* separate the primes: mean ≈ 0.4977 sits ON the
random 1/2 prediction, whereas all-ones (kernel) gives mean 0 and Thue-Morse
gives mean decaying to 0. The distinguishing content of the primes is that their
mean is at the fair value, and the whole difficulty is that they are not known
to be non-adversarial for the fold.

## Negative controls

All-ones: nu2≡0, variance 0, vacuous. Thue-Morse: variance and mean decay
(the fold is sublinear), so its variance also vanishes — confirming that variance
decay alone carries no information about the density-1 form.

```claim
id: prefix-variance-fair-model-law
statement: The empirical prefix variance s2_N of nu2(n)/n over n ≤ N decays
  like ~ln N/(4N) for the primes (s2*4N/ln N ≈ 1.39–1.46 across N=100..4000,
  exactly measured) AND for the fair model (uniform random h, mean s2*4N/ln N
  ≈ 1.08 over 30 trials). The per-n fair variance is exactly (n−2)/(4n²) from
  Binomial(n−2,1/2). Primes sit ABOVE the fair-model variance by 1.28–1.40×
  across N, ratio drifting toward 1. So s2_N → 0 is generic to the fold, not
  a prime-specific signal: a density-1 argument built on a vanishing second
  moment cannot separate the primes from a uniform string.
hypotheses: fold convention d∈[2,n−1]; s_sos==s_direct checked n=4..200 and
  spots; nu2(53)==18 asserted; 30 Monte Carlo trials of uniform h length 4100,
  exact arithmetic; measured ratios.
holds-here: yes, measured to N=4000 (primes) and N=4000 (fair trials).
status: measured-not-proved
bearing: reframes GOAL priority 1 — the CHEBYSHEV bound is generic (any input
  with vanishing variance gets it); the prime-specific content is only the
  MEAN being at 1/2, and the difficulty is that the primes are not known to be
  non-adversarial for the fold. Reconciles with fair-model-exact-binomial
  (PROVED): uniform h gives wt(Phi_n h) ~ Binomial(n−2,1/2), so SUPPLY holds
  for random h with probability 1 − exp(−cn) by Chernoff.
anchor: code/out/prefix_variance_constant_check.txt (table);
  code/averaged/prefix_variance_constant_check.py
```
