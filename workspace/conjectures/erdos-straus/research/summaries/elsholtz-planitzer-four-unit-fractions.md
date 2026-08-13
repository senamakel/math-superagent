# Elsholtz & Planitzer, "Sums of four and more unit fractions and approximate parametrizations"

Source: https://arxiv.org/abs/2012.05984 (arXiv:2012.05984), published as
C. Elsholtz and S. Planitzer, Bull. Lond. Math. Soc. 53 (2021) 695–709.
Full text: `research/sources/elsholtz-planitzer-four-unit-fractions.html.full.md`
(arXiv HTML); landing page: `research/sources/elsholtz-planitzer-four-unit-fractions.full.md`.

## What it establishes (sourced, primary)

**Problem**: count representations of a rational m/n as a sum of four or more
unit fractions. This is the k ≥ 4 side of the `k/n = Σ 1/x_i` generalisation
(Sierpiński/Schinzel); its parametrisation machinery is the modern method for
the counting problems whose m = 4, k = 3 case is the Erdős–Straus equation.

**Main result (Theorem 1)**: new upper bounds on the number of representations
of m/n as a sum of 4 unit fractions, split into five regimes depending on the
size of m relative to n; the cases m small and m close to n are improved
specifically. Corollaries give bounds for k ≥ 5 terms.

**Method — "approximate parametrisations"**: rather than a complete
parametrisation of all solutions (the approach of Browning–Elsholtz and
Elsholtz–Tao, whose parametrisations have `2^(k-1) − k − 1` free parameters for
k-term sums), they fix only a subset of the parameters (a "defining set"); the
remaining parameters are then few (O_ε(n^ε)) up to divisor-function factors.
This keeps the counting bound while dramatically shrinking the search space —
the same strategy this run's ansatz search uses (fixing the shape, sweeping
only the parameters).

**Algorithmic content**: an outline for constructing **all** representations of
m/n as a sum of four unit fractions in expected time O_ε(n^ε) — the
computational reformulation of the same "solve by parametrisation, not by
searching n" principle.

## Relation to the library

- This closes the [ElPl20] gap that erdosproblems #242 cites for "representations
  for primes" background (the run's `bloom-elsholtz-egyptian-fractions-survey.md`
  cites the same authors' Proc. R. Soc. Edinb. A 150 (2020) result
  f(n) ≥ (log n)^{log 6 + o(1)} for almost all n — that paper is the *other*
  Elsholtz–Planitzer paper; this one is the four-or-more-terms counting paper).
- The parametrisation table for solutions of m/n in k terms (the 2^(k−1)−k−1
  parameter count) is the structural fact behind "the ansatz space is small":
  for k = 3, that is 4 − 3 − 1 = 0 free parameters... i.e. the 3-term solutions
  come from the two fixed Type I/II shapes of Elsholtz–Tao Prop 2.1/2.5; for
  k = 4 the parametrisation dimension jumps, which is why 4-term representations
  of 4/n are much easier than 3-term ones (any n has the greedy 4-term
  representation).

## Consequence for this run

The paper is context for why the run's target (3-term covering identities for
n ≡ 1 mod 840) is hard: 3-term solutions have only the two rigid Type I/II
shapes, whereas 4-term decompositions are parametrised by a growing family.
The **approximate parametrisation** idea is directly usable: an ansatz search
over the small parameter set (a,b,c,d / a,b,d in Elsholtz–Tao's notation) with
the divisor congruences relaxed to approximate forms could prune the space the
same way. No new theorem about the six open classes is claimed here.