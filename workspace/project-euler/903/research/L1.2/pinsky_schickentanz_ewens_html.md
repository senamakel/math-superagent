# Inversions under Ewens sampling, with and without a prescribed number of fixed points

Authors: Ross G. Pinsky, Dominic T. Schickentanz. arXiv:2510.20654v2 [math.PR/math.CO],
submitted 23 Oct 2025, revised 17 Nov 2025.
URL: https://arxiv.org/abs/2510.20654 (full text: https://arxiv.org/html/2510.20654v2)

Companion abstract/front page: `research/pinsky_schickentanz_ewens_inversions.md` (+ `.full.md`). (The top of this note can be truncated because the E-file with the full bibliographic record is under the 1000-token cap; the substantive content is long but each section is short.)
This file is the summary of the full HTML text; the complete text is at
`research/pinsky_schickentanz_ewens_html.full.md`.

## What the source establishes

The paper gives **exact** formulas for the probability that a specific pair
(i,j), i<j, is an inversion under the Ewens sampling distribution P_θ^(n) on S_n
(proportional to θ^{number of cycles}), and under that distribution **conditioned
on the permutation having exactly m fixed points**. The uniform distribution is the
case θ = 1; the derangement/cyclic cases are θ → 0.

1. **Unconditioned pair-inversion probability** (Thm 1a, eq 1.1):
   P_θ^(n)((i,j) inverted) =
   n(n−2(j−i)+1) / [2(θ+n−1)] − (n−1)(n−2(j−i)) / [2(θ+n−2)].
   Depends on the pair only through the gap j−i — link-translation-invariant and
   **affine in the gap** — the same structural feature as the run's empirical
   f_n(k) = A_n + (k−1)B_n. For θ=1 (uniform) it reduces to 1/2; for θ=0 it is
   1/2 + (j−i−1)/[(n−1)(n−2)], the single-cycle (rotation) case.

2. **Fixed-point-conditioned pair-inversion probability** (Prop 10a, eq 3.2):
   an exact closed form for P_θ^(n)((i,j) inverted | #fixed points = m), expressed
   as a five-term combination of ratios P_θ^(n−2)(#fixed = m−1,m,m+1,m+2) /
   P_θ^(n)(#fixed = m), each term affine in the gap j−i. The unconditional
   expected inversion count (eq 3.3) follows by summing over gaps.

3. **Fixed-point count** (Prop 4): exact
   P_θ^(n)(#fixed = m) = [n! θ^m / (m! θ^(n))] Σ_{k=0}^{n−m} (−θ)^k θ^(n−m−k)/(k!(n−m−k)!),
   with θ^(r) the rising factorial. Gives the D_{n,m} probabilities needed to
   evaluate Prop 10a.

4. **Asymptotics** (Thm 5, 8, 9): as n→∞ the conditional pair probability is
   1/2 − (m−1)(j−i)/n² − (m²−3m−θ+2)/(2n²) + O(n⁻³) (so the O(n) leading term
   depends only on m, not θ); as θ→∞ the limits depend only on parities; as θ→0
   only on whether m = n−2. The θ=1 (uniform) n→∞ asymptotics match the prior
   uniform-with-m-fixed-points paper [Pin25 = arXiv:2505.02058].

## What it implies for this problem (Project Euler 903)

The run's core open step is closed forms for A_n, B_n in f_n(k) = A_n + (k−1)B_n,
which memory.md/verify_red.py show are the only inputs still needed for
Q(n) = (n!)^2 + A_n·S(n) + (B_n/2)·T(n). The empirical gap-linearity was already
backed by Campion-Loth et al. (per-conjugacy-class inversion probability, affine
in gap and depending only on n, a_1=#fixed points, a_2=#2-cycles; research/
conjugacy_class_statistics_body*). Pinsky–Schickentanz is a **second, fully
independent and complete exact derivation of the same gap-affine, fixed-point-
driven mechanism**, for the *uniform* case θ=1 (which is the case Q(n) sums over).
Concretely:

- The exact fixed-point-conditioned pair-inversion formula (Prop 10a, θ=1) is a
  per-gap, per-m (fixed-point count) closed form directly usable to sum over
  cycle types, an alternative route to A_n and B_n.
- The θ=0 (rotation/cyclic) closed form
  P_0^((n))((i,j) inverted) = 1/2 + (j−i−1)/[(n−1)(n−2)] gives the exact small-
  exponent inversion structure that f_n(k) aggregates.
- It confirms translation-invariance (gap-only dependence) and gap-affineness are
  *proved theorems*, not only empirical patterns.

## Caveats (recorded so nobody over-claims)

- The paper treats the *inversion statistic of a single random permutation*, i.e.
  counts inversions of π (equivalently of its one-line/cycle form) — NOT the run's
  specific quantity of summing Lehmer/factoradic ranks over the cyclic subgroup
  {π^i} of one π, nor inversion counts of powers π^k across k. So it is a
  mechanism-level and route-level source for A_n, B_n, not a direct computation of
  Q(n). The still-open summations (over cycle types, and over the rank statistic
  inside a cyclic subgroup) remain the run's own work.
- The direct "sum of ranks over the cyclic subgroup" statistic is not addressed
  by any source located so far; that remains the genuinely novel core.
