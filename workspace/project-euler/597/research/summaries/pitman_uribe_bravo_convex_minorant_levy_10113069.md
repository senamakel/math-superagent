# Pitman & Uribe Bravo, "The convex minorant of a Lévy process" — summary

<!-- source: https://arxiv.org/pdf/1011.3069 | J. Pitman, G. Uribe Bravo, Ann. Probab. 40(4):1636–1674 (2012); arXiv:1011.3069, DOI 10.1214/11-AOP658 -->

Full text at `research/sources/pitman_uribe_bravo_convex_minorant_levy_10113069.full.md` (86k chars).

## What the source establishes

(VERIFIED by download from arXiv:1011.3069 — this is the genuine paper, cited
as arXiv:1011.3069 in ECP 2011 and in the survey.)

A unified rigorous theory of the **greatest convex minorant (GCM)** of a Lévy
process X with continuous distributions (hypothesis (CD)):

- **Stick-breaking construction (Theorem 1):** with (U_i) iid uniform on (0,t)
  independent of X, the excursion intervals successively discovered have
  lengths distributed like the associated uniform stick-breaking process L —
  giving an explicit construction of the GCM on [0,t] (and [0,∞)).
- **Excursions above the minorant form a Poisson point process (Corollary 2):**
  up to an independent exponential time T of parameter θ, the point process
  Ξ_T with atoms at (length, increment) of excursion intervals is a PPP with
  explicit intensity; Ξ_∞ likewise (Corollary 3) under liminf X_t/t framing.
- **Poisson–Dirichlet(1) (main corollary):** the ranked lengths of excursions
  of a Lévy process with continuous distributions above its convex minorant
  on [0,1] have the **Poisson–Dirichlet distribution with parameter 1** — the
  same universal law as the cycle lengths of a uniform random permutation.
- Theorem 3 (path-transform invariance of (U,X) ↔ (d−g, X^U)); Theorem 6
  (Abramson–Pitman 2011): convergence of the random-walk minorants.
- Bridges Spitzer/Andersen fluctuation theory (1950s) to the excursion/PPP
  framework; interval-partition and PD structure.

## Bearing on PE597

This is the canonical primary source for the GCM face/excursion structure the
run uses for the **pure (no-finish) race** (`cm-composition-distribution`):
P(GCM has k faces) = S1(n,k)/n!, and the ranked cluster/excursion lengths have
the Poisson–Dirichlet(1) law = cycle lengths of a uniform random permutation —
the universal law MJMS derive for ballistic aggregation via the convex
minorant. It supplies the rigorous excursion-theoretic backbone (PPP of
excursions, stick-break construction, PD(1) universality).

It does NOT cover the finite-finish-line torpids model (boundary-free walk on a
fixed interval, no absorbing finish); and the run's verified refutation
`torpids-parity-not-gcm-functional` shows the torpids parity is not a function
of the GCM composition anyway. A warm-up source, not the answer to p(13,1800).

## Provenance / correction

This file is the corrected version. An earlier run mis-fetched arXiv:1011.6296
(an unrelated optics paper) under the same descriptive name; that wrong file
was replaced by a correction pointer at
`research/sources/pitman_uribe_bravo_convex_minorant_levy.full.md`.
Read THIS (…_10113069) file for the genuine paper.

## Consistency with the run's record

Consistent with the survey (`research/torpids_parity_ballistic_aggregation_survey.md`,
claim `cm-composition-distribution`). No contradiction.