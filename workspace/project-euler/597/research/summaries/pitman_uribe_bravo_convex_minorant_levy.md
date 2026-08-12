# Pitman & Uribe Bravo, "The convex minorant of a Lévy process" — summary

<!-- source: https://arxiv.org/pdf/1011.6296 | Jim Pitman, Gerónimo Uribe Bravo, Ann. Probab. 40(4):1636–1674 (2012); arXiv:1011.6296 -->

Full text at `research/sources/pitman_uribe_bravo_convex_minorant_levy.full.md` (25k chars).

## What the source establishes

A unified rigorous theory of the **greatest convex minorant (GCM)** of a Lévy
process with continuous distributions, on both finite and infinite time
horizons.

- Explicit constructions of the GCM on [0,1] (and beyond) via independent
  random sampling times from a uniform stick-breaking process; a second
  construction via a path transformation tied to excursion intervals.
- The **excursions of the process above its convex minorant** form a Poisson
  point process (up to an independent exponential time); equality with the
  construction of Kendall (1990) and the stick-breaking/Poisson–Dirichlet
  connection.
- **Excursion lengths (ranked) follow the Poisson–Dirichlet distribution with
  parameter 1** for Lévy processes with continuous distributions on [0,1] —
  the same universal law as the cycle lengths of a uniform random permutation.
- Bridges combinatorial fluctuation theory of random walks
  (Andersen 1950–54; Spitzer 1956) to the modern excursion/Poisson–Dirichlet
  framework.

## Bearing on PE597

This is the canonical primary source for the GCM face/excursion structure the
run uses for the **pure (no-finish) race**:
`cm-composition-distribution` claims P(GCM has k faces) = S1(n,k)/n! = cycle
composition of a uniform random permutation, and the Poisson–Dirichlet(1) law
of ranked excursion lengths is exactly the ranked-cluster-size law MJMS derive
for ballistic aggregation via the convex minorant. It supplies the rigorous
excursion-theoretic backbone (Poisson point process of excursions, stick-break
construction, PD(1) universality) behind the pure-race identification.

It does NOT cover the finite-finish-line torpids model: the GCM structure
applies to a boundary-free walk on a fixed interval with no absorbing finish;
the run's verified refutation `torpids-parity-not-gcm-functional` shows the
parity of the finite race is not a function of the GCM composition anyway.
A warm-up source, not the answer.

## Consistency with the run's record

Consistent with the survey (`research/torpids_parity_ballistic_aggregation_survey.md`
claim `cm-composition-distribution`), which cites it (`ecp.v16-1648` is the
pitman-uribe-bravo offprint link; `20-ejp497` is the related EJ/pitman line).
No contradiction.