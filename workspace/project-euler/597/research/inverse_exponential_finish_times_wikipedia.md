# Inverse (reciprocal) distribution — the distribution of finish times — Wikipedia "Inverse distribution"

<!-- source: https://en.wikipedia.org/wiki/Inverse_distribution | converted from HTML -->

## What the source establishes

For a positive random variable X with density f(x) and CDF F(x), the distribution
of the reciprocal Y = 1/X is:

- CDF: G(y) = P(Y ≤ y) = P(X ≥ 1/y) = 1 − F(1/y), for y > 0.
- density: g(y) = (1/y²) · f(1/y).

Specializing to X ~ Exp(λ): the **inverse (reciprocal) exponential** Y = 1/X has

- density  g(y) = λ/y² · e^(−λ/y),  y > 0
- CDF     G(y) = e^(−λ/y)
- finite raw moments E[Y^k] exist only for k < 1 (mean and variance do **not**
  exist); quantile G⁻¹(p) = −λ/ln(p).

Note the reciprocal transform is applied to a *single* random variable; it is the
simplest case of a ratio distribution (degenerate numerator).

## Implication for PE 597 — this CORRECTS the standing "clocks" brief

Boat j's **finish time** is T_j = (L − p_j)/v_j, where v_j ~ Exp(1). Since v_j is
exponential, each finish time T_j = c_j/v_j is an **inverse-exponential** random
variable with scale c_j = L − p_j: density (c_j/t²)e^(−c_j/t).

The crucial structural consequence: **finish events are NOT competing exponential
clocks.** The hazard of T_j is

    h_j(t) = f(t)/(1−F(t)) = (c_j/t²) / (1 − e^(−c_j/t)),

which is *not constant* in t (it behaves like c_j/t² for small t and is large for
small t). Therefore the "next finish wins with probability λ_j/Σλ" product-of-rate-
ratios picture in context.md applies to the *bump* dynamics only if a bump time can
be re-expressed as an exponential clock — that is the genuinely open piece — but it
does **not** by itself give an exact product form over the whole chronology, because
finish times are inverse-exponential (non-constant hazard). The memoryless property
belongs to the *speeds* v_j, not to the induced finish times 1/v_j.

So the library now states exactly what the finish-time distribution is, why it breaks
the naive "all clocks are exponential" reduction, and what the remaining derivation
(bump-rate + finish-hazard mixed chronology) must overcome. That pinpointing is what
was previously left vague in context.md's "pinning down what the clocks are" gap.
