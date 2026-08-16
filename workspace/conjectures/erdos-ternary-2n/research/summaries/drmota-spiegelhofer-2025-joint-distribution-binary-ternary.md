# Drmota & Spiegelhofer 2025 — Joint distribution of binary and ternary digit sums

**Source:** Michael Drmota, Lukas Spiegelhofer, "The joint distribution of binary and
ternary digits sums", arXiv:2501.00850 (2025). Full text:
`research/sources/drmota-spiegelhofer-2025-joint-pdf.full.md`.

## What it establishes

**Context.** `s_q(n)` = base-`q` digit sum = minimal number of powers of `q`
needed to represent `n`. A `(p,q)`-*collision* is an `n` with `s_p(n)=s_q(n)`.
`(s_2(n),s_3(n))` are each asymptotically normal with means `(1/2)log_2 N` and
`log_3 N`, many standard deviations apart.

**Theorem 1.2 (main).** For every `δ > 0` there is `K_0` such that for every pair
`(k1,k2)` with `k1,k2 ≥ K0` and mutually comparable (`k1 ≥ δ k2`, `k2 ≥ δ k1`),
there exists `n` with `s_2(n)=k1` and `s_3(n)=k2`. That is, the pair
`(s_2(n),s_3(n))` attains *almost all* values in `N^2` (asymptotic density).

**Corollary 1.1.** For any positive integers `a,b`, `a·s_2(n)=b·s_3(n)` has
infinitely many solutions `n`.

**Gives (quasi-)equidistribution.** Theorem 1.1 gives a multivariate normal /
local-limit statement for `(s_2(3^K n), s_3(n))`. Specialising recovers
Spiegelhofer 2023's infinitesimal collision result, Drmota's 2001 local theorem,
and the La Bretèche–Stoll–Tenenbaum density result `{s_p(n)/s_q(n)}` dense in `R^+`.

**Equivalent reformulation via valuations.** The paper records the important
equivalence chain:
`s_2(n)=s_3(n) ⟺ ν_2(n!) = 2·ν_3(n!) ⟺ 12^k || n! for some k ⟺ ℓ_12(n!) ∈ {1,5,7,11}`.
So the collision problem equals the base-12 last-significant-digit problem for
`n!`. (Deshouillers–Jelinek–Spiegelhofer showed every digit in `{1..11}` occurs
infinitely often as `ℓ_12(n!)`.)

## Implications for this run

This is the leading edge of the digit-sum literature on the base-2↔base-3
interface that the symbolic-invariant / carry-transducer route depends on. It
sharpens Spiegelhofer 2023 from "infinitely many collisions" to "almost all
`(s_2,s_3)` pairs occur". It does **not** bear directly on the Erdős ternary
conjecture itself (that is about the *digits of `2^n`*, not about which `n` are
collisions), but it is the correct modern reference for the joint
distribution/collision phenomenon the run's transducer statistic would exploit,
and its `ν_2(n!)=2ν_3(n!)` equivalence is a clean reformulation of the
base-2↔base-3 digit-sum relationship.

Status: sourced (primary).

```claim
id: DS-JOINT-DISTRIBUTION-S2-S3
statement: (Drmota & Spiegelhofer, arXiv:2501.00850, Theorem 1.2) For every
  delta > 0 there is K_0 such that for every (k1,k2) with k1,k2 >= K_0 and
  mutually comparable (k1 >= delta k2, k2 >= delta k1), there exists n with
  s_2(n)=k1 and s_3(n)=k2. So (s_2(n),s_3(n)) attains almost all values in N^2.
hypotheses: s_q = base-q digit sum; comparability k1,k2 both >= K0 and within
  a factor 1/delta of each other.
holds-here: yes -- the base-2/base-3 digit-sum interface is what the run's
  symbolic-invariant route works through; as(a2)=b(s3) has infinitely many
  solutions for all a,b>=1 (Cor 1.1).
status: asserted-by-source (primary text held verbatim).
bearing: sharpest current statement on the joint distribution of digit sums in
  the run's target interface. Does NOT address the Erdos ternary conjecture
  about digits of 2^n itself; it is the background against which a carry or
  digit-sum invariant on 2^n would be measured. Records the equivalence
  s_2(n)=s_3(n) iff nu_2(n!)=2 nu_3(n!) iff 12^k || n! for some k.
anchor: research/summaries/drmota-spiegelhofer-2025-joint-distribution-binary-ternary.md
```

