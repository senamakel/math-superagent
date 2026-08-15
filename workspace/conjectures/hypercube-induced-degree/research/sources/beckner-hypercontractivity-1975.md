# William Beckner, "Inequalities in Fourier Analysis" (Annals of Mathematics, 1975)

Source URL: https://doi.org/10.2307/1970980
Retrieved via `read_sources` (server-side); direct download blocked by the
network boundary (JSTOR host unreachable from the run).

Paper: William Beckner, *Inequalities in Fourier Analysis*, Annals of
Mathematics 102 (1975), no. 1, 159–182.

## What this source establishes

The canonical **hypercontractive** (sharp norm-contraction) inequalities for
the Gaussian and Boolean settings. For functions on the Boolean cube / under
semigroups (heat flows), Beckner's inequalities relate L^p norms of functions
before and after applying a noise/smoothing (Ornstein–Uhlenbeck / Bernoulli)
semigroup in a dimension-free, sharp way. Concretely this is the inequality
`||T_ρ f||_q <= ||f||_p` for ρ² <= (p-1)/(q-1) (in the Boolean/Gaussian
setting), which is the engine behind bounding Boolean-function norms and
influences on {−1,1}^n when a function is expressed via its Fourier–Walsh
coefficients.

Consequences used throughout the influence theory: sharp norm inequalities for
truncated/low-degree Fourier expansions; controls on mass between L^p spaces
under the semigroup; quantitative relations between a function's Fourier
spectrum and its edge sensitivity / stability on the cube.

## Why it is here

This is the deepest Fourier-analytic *technique* in the influence/Boolean-function
side of the library. The KKL maximum-influence bound — one of the four
"classical techniques" the problem.md obstruction names — rests on
hypercontractivity; Beckner 1975 is its primary source (Kahn–Kalai–Linial 1988
cite Beckner directly). It bounds **average** quantities (influences, norms,
total sensitivity): a consequence relation between Fourier mass and
edge-sensitivity, not a bound on maximum internal degree D(S). It therefore
confirms the obstruction that the Fourier/influence class of tools cannot reach
f(n) — it quantifies averages — while supplying the sharpest available
statement of that technique for the cube.

## Claim block

```claim
id: beckner-hypercontractivity-1975
statement: Sharp hypercontractive inequalities hold for the Boolean/Gaussian
  semigroups: e.g. ||T_ρ f||_q <= ||f||_p for ρ^2 <= (p-1)/(q-1). These give
  norm-contraction bounds that relate a Boolean function's L^p norms, its
  Fourier–Walsh spectrum, and its influences / edge sensitivity on the cube.
hypotheses: functions on the Boolean cube / Gaussian space under the heat-flow
  semigroup; 1 <= p <= q.
holds-here: yes — this is the technique underlying KKL (influence bound), but
  the quantities it bounds (norms, influences, total sensitivity) are averages,
  not the maximum internal degree D(S).
status: asserted-by-source (Beckner 1975, read via read_sources; primary).
bearing: primary source of hypercontractivity behind KKL / influence route;
  confirms the influence class of tools bounds averages and cannot reach f(n).
falsifies: a counterexample to the stated norm-contraction inequality.
anchor: https://doi.org/10.2307/1970980
```
