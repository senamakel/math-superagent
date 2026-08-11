# Summary — Dirichlet distribution and its exponential/gamma derivation

Source: Wikipedia "Dirichlet distribution". URL:
https://en.wikipedia.org/wiki/Dirichlet_distribution
Full text: `research/L0/dirichlet_distribution_wikipedia.full.md`
(+ complete text at `…full.full.md`).

## Statement

Dirichlet(α) on the K−1 simplex has density
(1/B(α))·∏_i x_i^{α_i−1}, where B(α)=∏Γ(α_i)/Γ(Σα_i).

Key construction (aggregation / Gamma property): if Z_i ~ Gamma(shape α_i,
rate 1) are independent and W = Σ Z_i, then

    (Z_1/W, …, Z_K/W) ~ Dirichlet(α_1,…,α_K),

independent of W. Consequences used here:

- **Normalized iid Exp(1) are uniform on the simplex.** K iid Exp(1) are
  Gamma(1,1); dividing by their sum gives Dirichlet(1,…,1), i.e. the *uniform*
  density on the K−1 simplex (each marginal density (K−1)!(1−x)^{K−2}).
- Mean E[X_i]=α_i/Σα; for α=(1,…,1) the components are exchangeable.

## Why it bears on Torpids

The race outcome (which bump happens before which, who reaches the finish
first) is **invariant under common scaling of all speeds** — multiplying every
v_j by a constant c>0 scales every event time by 1/c without changing any
bump/bump or bump/finish ordering. Hence the outcome depends only on the speed
*direction* v/Σv. Since the direction of iid Exp(1) speeds is uniform on the
simplex (Dirichlet(1,…,1)), the probability of any parity event equals the
simplex volume of the angle-region over which it occurs. This is the exact
integration target: p(n,L) = uniform-simplex measure of the event, reducing
"integrate over Exp speeds" to "measure a polytope/simplex region".
