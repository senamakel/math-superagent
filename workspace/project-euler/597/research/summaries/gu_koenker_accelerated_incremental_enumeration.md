# Gu–Koenker arXiv:1811.03329 — CORRECTION: not a chamber-enumeration algorithm

Jiaying Gu, Roger Koenker, "Nonparametric maximum likelihood methods for binary response models with random coefficients", arXiv:1811.03329 (JASA 117, 2022). [[gu_koenker_accelerated_incremental_enumeration.full]]

## Correction (important)

CONTEXT.md describes this source as "Gu–Koenker accelerated incremental chamber enumeration" (arXiv:1811.03329) in the exact-volume/chamber tooling tier. **That is a mislabelling.** The paper is an **econometrics** paper about computing NPMLEs for binary-response models with random coefficients. It *uses* the geometry of hyperplane arrangements (regions of the arrangement = possible sign patterns of a linear classifier, so the NPMLE objective is refined over arrangement cells), but it does **not** propose a chamber-enumeration algorithm and contains no volume/enumeration method for arrangements. Do not cite it as a solver for the torpids arrangement. Its abstract-level relevance to PE597 is nil.

## What it actually establishes (sourced)

- NPMLE computation for single-index binary-response random-coefficient models is made tractable by exploiting that the likelihood is piecewise-constant over the cells of a hyperplane arrangement (the arrangement whose hyperplanes are the indifference curves of the linear predictor).
- Contrasted with the deconvolution estimator of Gautier–Kitamura (2013); applied to a Washington-DC modal-choice dataset.

## Hypotheses and whether they hold here

The econometric setting (random-coefficient binary response) is unrelated to the torpids bump/finish parity. The shared ingredient is only "a piecewise-constant objective over a hyperplane arrangement" — true here too, but the paper contributes no method that reduces the torpids arrangement's super-exponential cell count.

## Bottom line

Same verdict as Latte/Büeler: confirming that arrangement-cell structure underlies a piecewise problem does not make n=13 reachable. Keep the file only as provenance; do not treat it as part of the exact-volume tooling tier.
