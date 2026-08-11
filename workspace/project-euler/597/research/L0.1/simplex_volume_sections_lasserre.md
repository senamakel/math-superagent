# Volume of slices and sections of the simplex in closed form — Lasserre (digest)

<!-- source: https://hal.science/hal-01095071/document | Jean-Bernard Lasserre, Optimization Letters 9(7):1263–1269 (2015), HAL hal-01095071 -->

Reader for the full text at `research/L0.1/simplex_volume_sections_lasserre.full.md`
(full PDF: https://hal.science/hal-01095071/document).

## What the source establishes
For the canonical simplex Δ = {x ∈ R^n : e^T x ≤ 1}, any a ∈ S^{n−1}, t ∈ R, it
gives **closed-form Lebesgue volumes** of the section Θ(a,t) = Δ∩{a^T x ≤ t} and
the slice S(a,t)=Δ∩{a^T x = t}. Proof via Laplace transform of x↦e^{−s(a^T x)} over
Δ. The section volume is a piecewise polynomial of degree n in t (slice: n−1),
with breakpoints from the a_i, explicitly including degenerate coincident weights.
Direct proof, no univariate B-spline detour. General lesson: simplex/hypercube
volumes decouple under Laplace transforms.

## Why it bears on PE 597 (Torpids)
[[dirichlet_distribution_wikipedia.full]] (sealed in [[L0.0]]) shows normalized iid
Exp(1) speeds are uniform on the simplex, so p(n,L) is the uniform-simplex measure
of the parity region — a finite union of sub-simplices cut by linear inequalities
a^T x ⋛ c. Lasserre supplies named, proven machinery for each such cut as a
closed-form piecewise-polynomial volume, giving an **exact rational** route to the
10-dp target p(13,1800), which MC cannot resolve (memory.md: bias ≤ ~3e-4).

## Limits
Gives single-section/slice volumes; assembling the full parity region from these
cuts is problem-specific, not covered here.
