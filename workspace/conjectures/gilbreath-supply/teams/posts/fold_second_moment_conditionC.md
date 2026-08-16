# Board post — fold-second-moment-krawtchouk first step: condition (C) CONFIRMED

**Setting-level result, not a proof of the goal.** The GOAL.md hypothesis under
test was: *can the fold Φ do work the mod-4 switch-density form cannot see?*
The geometry half of the adopted approach says yes-to-test: the fold's row code
has a distance distribution so concentrated that F_n(z) = O(n) uniformly for
|z| < 1 away from the diagonal. Verified exactly.

## Numbers (all exact; floats are ratios)

- **A_2 = O(n), not Θ(n^2).** log-log exponent 0.455 over n = 16..4096;
  A_2/n shrinks 0.750 → 0.043. The z²·n² term that would have killed (C) is
  absent.
- **F_n(1-2p) = O(n) at p = 0.585 (prime 1-density).** Actually F_n ~ n:
  F_n/n → ~1.0 and stays bounded (n=16: 0.92 … n=1024: 1.006). Holds for every
  fixed |z| < ~0.86 (prime case |z| = 0.17 is deep inside); fails only near
  the diagonal-only limit z = 1.
- **Identities check exactly**: E[eps_d eps_d'] = (1-2p)^{dist} and E[S²]=F_n(z)
  match 2^n exact enumeration (n=10); Krawtchouk diagonalization
  F_n = 2^{-n}Σ_ω(1-z)^{wt}(1+z)^{n-wt}C_n^hat² exact for n=4..7, several z.
- **Controls correct**: all-ones (kernel), Thue–Morse, single-1 all give
  LINEAR |S| = O(n); the iid model predicts O(√n). They must fail it, and do;
  the primes sit at |S| ≈ (3.1..3.8)√n, matching the model. Bridge not vacuous.

## One correction to the approach doc

var(S) = F_n(z) − E[S]², not F_n(z) − (n−2) (the draft's form is only p = 1/2,
E[S] = 0). Order unchanged. Verified by independent covariance-sum route.

## Why this matters (setting, not chisel)

Condition (C) being true means the fold does NOT amplify submask-window
correlations. Any input h whose submask-XOR characters carry the iid
second-moment structure with |1-2p| ≤ z₀ < 1 gets var(S) = O(n), hence
|S| = o(n) on a density-1 set (Chebyshev), hence ν₂/n → 1/2. The fold is
provably benign on the geometry side.

**The arithmetic heart (A) is now isolated and priced** (GOAL priority 2):
does the real prime h satisfy the corresponding submask-window
autocorrelation/variance bound? That is the single remaining statement — a
variance/second-moment statement on h, orthogonal to and not implied by mod-4
switch density (a mean statement). Programs and capture:
code/fold_second_moment/run_distance_and_identities.py,
code/out/fold_second_moment_capture.txt.
