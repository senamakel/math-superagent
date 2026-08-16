# Pattern-finder: the fold operates on the primes as a generic-balanced input

What the data says about the structure of `ν₂(n) = wt(Φ_n h)` and its
deviation `S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)}`, where `ν₂(n) = (n−2−S(n))/2`.

All numerics are exact integer/ratio computations of the SOS fold
(`lib.supply_fold.s_sos`, checked against the brute submask-XOR oracle on
`n=4..60` and reproducing problem.md's `ν₂(4000)/4000`). Inputs: primes,
iid random h, Thue–Morse, sparse-random, near-kernel strings.

## The central structural finding

**The primes sit in the generic-good class of the fold: `ν₂/(n−2)` ≈ 1/2.**

Measured fold-cell density `ν₂(n)/(n−2)`, mean over the last half of
`n ∈ [2,N]`, `N=1500`:

| input | mean fold-density | at N |
|---|---|---|
| primes | 0.5004 | 0.5174 |
| random iid | 0.4997 | 0.5060 |
| random p=0.15 | 0.4844 | 0.4933 |
| Thue–Morse | **0.0666** | 0.0120 |

The primes deviate from 1/2 by no more than a random string does; Thue–Morse
collapses (sublinear), as its known `ν₂/n → 0 (0.27→0.011)` already foreshadowed.
Consequence: *the error term in* `ν₂(n) ≈ (n−2)/2 − S(n)/2` *is what decides
SUPPLY, and it sits at* `|S| ≈ O(√n)` *for the primes.*

## S(n) is mean-reverting with √n-scale fluctuations

- `std(S(n))/√n ≈ 1.0` constant over every 500-bin from 300..4000 (0.95–1.05);
- `|S(n)| ≤ 3.8√n` uniformly (tight band 3.1–3.8, no growth) through `n=6000`;
- `max |S(n)|/n ≈ 0.14` at N=6000 — `S = o(n)` at √n rate;
- increments `S(n+1)−S(n)` are *not* ±2 (std ≈ 65), so S is **mean-reverting**,
  not a growing random walk — it oscillates near 0;
- no constant-coefficient linear recurrence (order ≤ 6 over 100 terms), not
  polynomial. It is microscopically unstructured.

**Generic, not prime-arithmetic.** iid random h gives the identical bound
(`max|S|/√n = 3.99` vs primes 3.82 at N=6000). So the √n/CLT bound is a
property of the fold on unstructured input — the primes' only needed property
is *being unstructured enough* that the fold doesn't collapse. That is a far
weaker arithmetic input than positive mod-4 switch density (which requires
specific correlation structure).

## What drives the collapse — density of 1s, not automaticity

Control map (N=800, `max|S|/n` over [300,N]):

| input | max|S|/n |
|---|---|
| random p=0.01 | 0.843 |
| random p=0.15 | 0.474 |
| single 1 (near kernel) | 0.993 |
| rare defect 1/997 | 0.996 |
| random p≥0.2 | ≤ 0.23 |
| random p=0.3–0.6 | 0.14–0.23 |
| **primes** | **0.14** |

Sparse h collapses (close to the kernel, which is the period-2/sparse boundary);
at 1-density ≥ ~0.2 the fold is generically good. This is why the earlier
"2-automatic collapses" framing was wrong: Thue–Morse collapses, but so does a
single isolated 1 — the driver is sparsity/proximity to the kernel, not
2-automaticity per se.

**The prime gap-parity string has 1-density ≈ 0.585** (stable, N≤20000), well
inside the good regime.

## Candid structural claim (weak-input route, GOAL priority 4)

A second-moment / variance bound on the submask-XOR transforms of `h` that
gives `var(S(n)) = o(n²)` — equivalently `|S(n)| = o(n)` — would settle SUPPLY
with any `c < 1/2`, since `ν₂(n) = (n−2−S(n))/2`. Empirically the primes give
`|S| = O(√n)`, and this is the *generic* fold behaviour on balanced input, so
the needed arithmetic input is plausibly much weaker than positive switch
density. This is measurement, not a theorem; the open step is the second-moment
bound on `h` (G-var / G-weak-input).

## Status and evidence classes

- √n scaling of `S(n)`, mean-reversion, fold-density 0.5 for primes: **measured
  exactly** over n ≤ 6000. Not a proof for all n.
- Density-1/tail shape (`ν₂/n < 0.42` has 6 fixed violating n, count constant
  as N grows → density → 0): **measured**, primes, n ≤ 4000.
- Generic/prime-arithmetic split via random control: **measured**, strong
  support that the √n bound is fold-generic, not prime arithmetic.
- No recurrence/polynomial structure on `S(n)` or `ν₂(n)`: **exact** over the
  terms supplied (labels them as conjectural for continuation).
