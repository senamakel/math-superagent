# Measurable density and the forbidden-distance problem — the upper-bound dichotomy

```approach
idea: Attack the upper-bound half (chi ≤ 6 versus chi ≥ 6) through the measurable and fractional chromatic numbers of the plane and the density of unit-distance-avoiding (1-avoiding) sets — the forbidden-distance problem — instead of through any tiling or lattice construction.
mechanism: A k-colouring of R^2 is a cover by k sets each avoiding distance 1, so for measurable colourings one colour class must have density ≥ 1/k. The supremum density δ of a measurable 1-avoiding set is therefore tied to the measurable chromatic number by χ_m ≥ 1/δ (and χ ≥ χ_m). This is a different lever from the closed torus/Meyer tiling lines: it is an integral-geometry / density statement, attacked through the forbidden-distance problem (Erdős), Larman–Rogers-type bounds, and Delsarte linear programming for Euclidean avoidance/packing. Concretely: improving the upper bound on δ (or on χ_f(R^2), which is sandwiched below χ_m ≤ χ) would force χ_m ≥ 6 or even ≥ 7 by a pure density argument, while an explicit measurable 1-avoiding set of density ≥ 1/6 is a necessary ingredient for any measurable 6-colouring and would guide the colouring search.
status: refuted
killed-by: blocked-by-evidence-policy-and-density-too-weak — its first step (compile the known δ, χ_f(R²), χ_m(R²) bounds) is exactly the BLOCKED answer-tier survey recorded in research/REQUESTS.md row 2, so the step cannot be executed in this run. Its own speculation concedes the density lever fails: the known independence density δ of a measurable 1-avoiding set is far above 1/6, so χ_m ≥ 1/δ cannot force χ_m ≥ 6, and the line yields only a frontier survey, not a bound. It also cannot reach the lower bound χ ≥ 6 (already out of reach) nor the size bound. No adopted successor needed; the upper-bound frontier remains the (separate) tiling/margin problem.
first-step: Compile the exact known bounds — the best upper bound on the density of a measurable 1-avoiding set in R^2, and the known interval for χ_f(R^2) and χ_m(R^2), each with its primary source — then test whether the current δ-bound already implies χ_m ≥ 6 (it likely does not), and record the precise gap a 6-colouring or a χ ≥ 6 proof must close.
precedent: unchecked
speculation: Heavily speculative as a route to the bound: the known δ is far above 1/6, so the density argument alone cannot force χ_m ≥ 6 today. Its certain value is a precise, sourced frontier for χ_f/χ_m/χ and a named dichotomy (density vs. tiling) the run has not stated.
```

## Why this is not a closed line

- Not `flat-torus-periodic-6col` or `cut-and-project-meyer-6col` (closed): those are constructive tilings/lattice searches. This is a density / integral-geometry bound on measurable colourings — the *necessary* condition on colour-class density, not a tiling construction.
- Not `fractional-chromatic-lp-lower-bound` (adopted): that computes χ_f exactly for *finite* constructed graphs. This is about the *plane's* measurable/fractional chromatic number and the forbidden-distance density δ, a different (infinite, measure-theoretic) object.

Named mathematics: the forbidden-distance problem (Erdős), measurable chromatic number (Falconer), Larman–Rogers, Delsarte linear programming for Euclidean sets.

## What would falsify it

If the best known upper bound on δ is provably too weak to separate χ_m = 6 from χ_m = 5 (i.e., δ ≥ 1/5), then the density route cannot certify χ ≥ 6 and only yields the sourced frontier as its artifact. If a 1-avoiding set of density ≥ 1/6 is found without a full covering, that is a necessary ingredient but not a colouring — the line then needs the covering step it does not supply.
