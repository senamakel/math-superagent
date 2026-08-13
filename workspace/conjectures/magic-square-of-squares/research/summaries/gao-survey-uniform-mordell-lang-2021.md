# Gao, "Recent developments of the Uniform Mordell–Lang Conjecture" (survey, arXiv:2104.03431)

Full text: `research/sources/gao-survey-uniform-mordell-lang-2021.full.md`
(arXiv:2104.03431, 2021, PDF).

## What it establishes

A survey (not new results) of the uniform Mordell–Lang program: DGH (Annals 2021),
Kühne (arXiv:2101.10272), GGK (arXiv:2105.15085) and their predecessors. It collects:
- the historical arc from Faltings' Mordell conjecture through Manin–Mumford,
  Bogomolov, and the uniform versions;
- the key technique components (Vojta's approach, height inequality, equidistribution);
- Conjecture 10.5'/the expected form of the "gap principle", and the known optimality
  examples (e.g. that for higher-dimensional subvarieties one cannot drop "X
  generates A" nor assert finiteness of uniformly-bounded cardinality);
- the citation web (DP07, Rémond, Yuan–Zhang adelic line bundles, …).

## Bearing on the magic-square-of-squares problem

This is the encyclopedic entry the run now holds for the uniform-Mordell-Lang body of
work feeding the adopted `uniform-height-bound-elliptic-ap` approach: it says what the
program's scope is (abelian varieties and curves of genus ≥ 2 embedded in Jacobians),
confirms the elliptic-curve case is treated by the prior quantitative results
(Rémond, David–Philippon) rather than by the new uniformity theorems, and is the
recommended first stop for anyone asking whether any uniform constant is effective.
Gao's survey also states (per GGK) that the only explicit-constant uniform ML results
are David–Philippon's for self-products of a single elliptic curve — the same DP07
lane identified in the GGK summary.

```claim
id: gao-survey-uniform-ml-scope
statement: "Gao's 2021 survey of the uniform Mordell–Lang conjecture: the DGH/Kühne/GGK
theorems give uniform bounds #C(F) ≤ c(g,d)^(1+ρ) for curves of genus ≥ 2 and,
in GGK, for subvarieties of abelian varieties, all with existential constants; the
only prior uniform-ML results with explicit constants are David–Philippon for
subvarieties of self-products of an elliptic curve; the elliptic-curve (genus 1) case
is otherwise handled by the classical quantitative results of Rémond."
hypotheses: none beyond the survey's scope statements
holds-here: yes (it fixes the landscape the uniform-height approach lives in)
evidence: asserted (survey statements, cross-checked against the primary texts GGK
and DGH now on disk)
bearing: encyclopedia anchor; confirms the only effective-constant lane is DP07, and
the genus-1 case is outside the new uniformity theorems
anchor: research/summaries/gao-survey-uniform-mordell-lang-2021.md
```