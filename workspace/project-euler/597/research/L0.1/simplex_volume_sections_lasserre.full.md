# Volume of slices and sections of the simplex in closed form — Lasserre

<!-- source: https://hal.science/hal-01095071/document | Jean-Bernard Lasserre, Optimization Letters 9(7):1263–1269 (2015), HAL hal-01095071 -->
Full text (PDF): https://hal.science/hal-01095071/document

## What the source establishes

For the canonical simplex Δ = {x ∈ R^n : e^T x ≤ 1} (e = vector of ones), and a
vector a ∈ S^{n−1}, t ∈ R, it gives **closed-form Lebesgue volumes** of the
*section*

    Θ(a,t) = Δ ∩ { x : a^T x ≤ t }

and the *slice*

    S(a,t) = Δ ∩ { x : a^T x = t }.

Method: the Laplace transform of x ↦ e^{−s(a^T x)} over Δ is evaluated, and the
result reads off a piecewise-polynomial volume in t. The volume of Θ(a,t) is a
piecewise polynomial of degree n in t, and of S(a,t) degree n−1, with breakpoints
determined by the a_i. The paper gives a direct, simple proof (no univariate
B-spline detour, the earlier route of Curry–Schoenberg / Micchelli), and handles
degenerate cases where some weights a_i coincide. It also notes the general lesson
that simplex (and hypercube) volumes decouple cleanly under Laplace transforms.

## Why this bears on PE 597 (Torpids)

The library already establishes (see [[dirichlet_distribution_wikipedia.full]],
sealed in [[L0.0]]) that the normalized iid Exp(1) speeds are uniform on the
standard simplex, so p(n,L) is the **uniform-simplex measure (volume) of a parity
region** — a union of sub-simplices cut by linear inequalities of the form
a^T x ⋛ c. Lasserre supplies the named, proven machinery to turn such a region
into a **closed-form piecewise-polynomial volume** rather than a numeric
integration or an enumeration: each linear condition a^T x ≤ t against the simplex
is exactly his Θ(a,t) section, and the parity region decomposes into finitely many
such sections. Combined with the exact recursion of [[L0.0]] this is the route to a
finite **exact rational** evaluation of p(n,L) → the 10-dp target p(13,1800), which
MC cannot resolve (memory.md says any true bias ≤ ~3e-4).

## Limits
- Provides section/slice volumes of a simplex under linear cuts; the run still must
  assemble the parity region as a finite set of such cuts (and subtract/combine the
  allowed sub-simplices), which is problem-specific and not in the paper.
