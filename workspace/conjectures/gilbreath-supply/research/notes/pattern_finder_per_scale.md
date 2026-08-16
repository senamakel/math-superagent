# Pattern-finder: per-dyadic-scale decomposition of the fold's character sum

Role: pattern-recognition specialist. Everything below is exact integer/ratio
arithmetic over the computed ranges (N ≤ 9000, N=40000 JSON for S(n));
**nothing is a proof for all n.** Each finding is labeled measurement vs
identity. They are conjectures handed forward, not established theorems.

## Object

```
S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)},   T(n,d) = ⊕_{o⊆d} h[n−1−d+o]
ν₂(n) = (n−2−S(n))/2                  [exact identity, verified 2..40000]
```

Scale of a depth d: `g(d) = trailing_ones(d) = ν₂(d+1)` (the number of trailing
1-bits). Group the character sum by scale:

```
S_g(n) = Σ_{d in [2,n-1], g(d)=g} (−1)^{T(n,d)}
```

measured by direct submask enumeration (exact) over windows of n. The fold
matrix `Φ_n` reads h along the submask window of each d; the scale g is the
dyadic block size (separation 2^g) that depth reads at, per the verified
G-run-telescope.

## Finding 1 — the variance is fold-generic and g=0-dominated, NOT prime-specific

Mean of `S_g(n)²/n` over many windows, and its share of total `Σ S_g²/n`:

```
input            total S²/n     g=0       g=1       g>=2
primes           1.28/0.90*     54%       29%       17%
random p=0.585   1.93           54%       15%       31%
random p=0.5     1.23           40%       38%       22%
```
(*primes measured twice: total S²/n 1.2775 on n=500..6000, 0.8974 on n=2000..8500 —
  window dependence; the SHARE split is stable.)

**Reading.** The g=0 scale (adjacent mod-4 switch pairs — the switch-density
input) holds roughly half the variance, and this split is the SAME for the real
prime string and for random balanced strings. So the dominance of the switch-
density scale in the *variance* is a structural property of the fold, not an
arithmetic signature of the primes. It does **not** reopen the switch-density
dead end: variance at g=0 is claimed by all inputs equally.

## Finding 2 — the drift (mean) is ~0 at EVERY scale, including the switch scale

Mean of `S_g(n)/n` over windows:

```
input          g=0      g=1      g=2      g=3      ...   all scales
primes        +0.0001  -0.0027  +0.0022  -0.0002  ...   -0.0003
random p=.585 +0.0013  -0.0001  +0.0007  -0.0011  ...   +0.0024
```

**Reading.** Every scale's drift is essentially zero, for primes AND random —
including g=0 (the scale reading adjacent mod-4 differences, i.e. the switch
density). There is no measurable switch-density mean leaking through the fold's
`S(n)` drift.

## Control — can the fold's per-scale drift detect switch bias at all?

To interpret Finding 2, test whether a real switch-density bias in h shows up in
`S_0`:

```
switch params      1-density   mean S_0/n   mean S/n
balanced .5/.5      0.496       +0.0020      +0.0014
weak bias .6/.4     0.475       +0.0010      +0.0014
strong bias .8/.2   0.319       -0.0028      -0.0020
extreme .9/.1       0.177       +0.0089      +0.0362
```

Only the extreme case (1-density 0.177 — already the collapse regime) shows a
clear mean, and it is confounded by the low density. Moderate/strong switch bias
produces `S_0` mean `±0.003` — indistinguishable from the prime/random noise band.

**Consequence (honest):** the fold's per-scale drift is structurally cancelled —
it is NOT a clean readout of switch density. So Finding 2 does **not** let us
conclude "primes have no switch-density drift" — the fold cannot resolve switch
bias in `S_0` even when present. The switch-density barrier (ABGS, parity
barrier) lives in the MEAN of adjacent pairs, and the fold's `S_0` drift does not
transparently carry that mean. This is consistent with (but does not prove)
R-submask-sufficiency over R-switch-equivalence: the fold reads switch pairs
only at scale g=0, folds their variance generically, and does not turn the switch
mean into drift.

## What this adds to prior pattern reports

Prior reports established: (i) `E[S(n)²]≈n` per-index (plateau, K≈1 to
N=131072); (ii) heavy-tail sparsity (`max S²/n < 16`, ~0.2% of n above 9);
(iii) `|S(n)| ≤ 3.8√n` uniform; (iv) no 2-adic/recurrence/OEIS structure.

This report adds the **first per-scale decomposition** of the variance and mean:
- the g=0 share of variance is ~50% and fold-generic (new; prior notes only
  conjectured g=0 "carries a non-negligible fraction of the mass" — confirmed,
  but shown to be generic, so the martingale-note's worry that it is switch-
  density-specific is unfounded);
- the drift is ~0 at every scale including g=0 (new), with a control showing the
  fold cannot resolve switch bias — bounding how much Finding 2 can say.

## Finding 3 — the g=0 (switch-scale) variance is bounded for the primes

Directly measuring the dominant scale's variance:

```
windows                mean S_0^2/n    max S_0^2/n
n=900..6000 step300      0.31            ---
n=800..9000 step200      0.52            1.83 @ n=5800
```

`E[S_0²]/n` is bounded (mean 0.31-0.52, max ~1.8), matching the level of the
whole `E[S²]/n` (which holds ~half its ~1.0 mass at g=0). So **condition (A)
holds at the dominant switch scale for the primes** — empirically, no
unbounded drift at g=0.

But it is NOT pure count: the g=0 variance depends on the input density
(random p=0.5 → 0.18, p=0.585 → 0.25, p=0.3 → 0.62). The primes' value
(0.31-0.52) sits inside this bounded input-dependent range — the generic-fold
level for a balanced density, not an arithmetic signature and not an
obstruction.

## Status

All numerics are exact measurements over n ≤ 9000 (scale decompositions) and the
N=40000 JSON (S(n) plateau, already reported). None is a proof. The genuinely new
structural content is Finding 1 + 2 + the control: the fold's variance profile is
generic-fold, and its drift does not resolve the switch-density mean. These are
conjectures pointing toward R-submask-sufficiency (fold does work orthogonal to
switch density), but the honest reading is: the measurement cannot distinguish
"no switch-density signal in the primes' fold" from "the fold cannot resolve
switch-density signal from any input". Further work would need the g=0 variance
bound — `E[S_0²] = O(n)` for the primes — which, if provable from a submask
correlation input, is exactly condition (A) at the dominant scale.
