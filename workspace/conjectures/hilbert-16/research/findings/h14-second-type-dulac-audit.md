# Current research note: second-type Dulac endpoint audit

## Source-backed extraction

Rousseau–Shan–Zhu, arXiv:1502.00689, §2.6 (held at `research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md`) distinguishes first-type transitions `{r=r0} ↔ {rho=rho0}` from second-type transitions from `{ybar=y0}` to `{r=r0}` or `{rho=rho0}`. The paper explicitly says that its proof of the saddle graphic I^1_12/I^1_13 only needs first-type maps, so it does **not** provide the missing H^3_14 second-type calculation.

For the first-type map, its rational-resonance formula is
`D_i(ytilde,nu) = eta_i(nu) rho0^p (nu/nu0)^barsigma omega(nu/nu0,alpha_i) + (nu/nu0)^barsigma (ytilde + phi_i)`,
with `omega(x,alpha)=(x^(-alpha)-1)/alpha` for alpha != 0 and `-log x` at alpha=0; phi has a generalized-monomial remainder and property J. At a hyperbolic ratio one, the refined map has `x + alpha*x*omega(x,alpha) + phi`, and at a saddle-node the central transition is linear/exponentially small while the stable-center transition is flat. These are exact source statements, but they concern first-type/hyperbolic or saddle-node normal forms, not the H^3_14 second-type endpoint map.

Peran 2021 and Mardešić–Resman 2021 (held) independently support the structural warning that semi-/parabolic return maps can require logarithmic or iterated-log transseries and analytic/quasianalytic control. They do not identify the H^3_14 germ.

## Actual result of this attempt

The requested smallest open step is now sharply localized: derive, in the H^3_14 blown-up endpoint normal form, the second-type transition from the `ybar` section to the `r`/`rho` section, including its parameter-uniform remainder class and its restriction along the invariant foliation. Without this lemma one cannot legitimately apply derivation-division/Rolle to Lu's claimed displacement equation. The available source specifically says it did not need this map, so no source-backed conclusion about its exact transseries or applicability of Rolle is available.

## Attack status

- Claim that the H^3_14 second-type germ is a finite ordinary power-log expression: **unproved and vulnerable** to the iterated-log warning.
- Claim that the existing derivation-division argument applies: **unproved**, because the required endpoint map and uniform remainder hypotheses are absent.
- Smooth test: any successful route must use analytic/quasianalytic control of the actual germ, not just its formal asymptotic series.
- Uniformity test: source-local expansions must be uniform in the five unfolding parameters; pointwise endpoint expansions are insufficient.
- Counterexample hunt: the smallest obstruction is the resonant/semihyperbolic endpoint where the first-type formula has a compensator and where the literature's second-type formula was not needed. A finite Taylor or ordinary power-log truncation is therefore not accepted as a model.

This is a partial negative result, not a refutation of Lu's theorem.
