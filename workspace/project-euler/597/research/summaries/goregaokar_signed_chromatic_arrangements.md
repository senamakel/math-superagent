# Goregaokar, "Interpreting the (signed) chromatic polynomial coefficients via hyperplane arrangements" (arXiv:2506.00941, 2025)

Source URL: https://arxiv.org/abs/2506.00941 (full text at `research/sources/goregaokar_signed_chromatic_arrangements.full.md`).

## What it establishes

Building on a recent result of Lofano and Paolini, expresses the **characteristic polynomial of a real hyperplane arrangement as a signed generating function over its regions**: for a generic point v, each region R contributes (−1)^{n−pdv(R)} t^{pdv(R)} where pdv(R) is the projection dimension of v onto R, so χ_A(t) = Σ_R (−1)^{n−pdv(R)} t^{pdv(R)}. Used to give an alternative proof of Greene–Zaslavsky's interpretation of the coefficients of the chromatic polynomial of a graph, generalized to signed graphs; for the braid arrangement the projection statistic has a combinatorial meaning (natural unit interval / graphical arrangements). v2 adds subarrangements of the Type B Coxeter arrangement and signed graphs.

## Bearing on PE597

This is the single most directly relevant standard result found for the parity problem, because it is exactly a **signed weighted sum over the regions of a hyperplane arrangement, evaluated from the characteristic polynomial without enumerating the regions**. The torpids parity is also a signed sum over cells (weight +1 / −1 by parity) of simplex-section volumes of an arrangement. So this paper is the canonical proof-of-concept that "a signed region-sum can be a structure constant (here χ_A's coefficients) rather than an enumeration." **Caveat:** the sign and weight here are tied to the projection-dimension statistic (−1)^{n−pdv(R)} and t^{pdv(R)}, not to the torpids parity sign or simplex-section volume; and the arrangements treated are graphical/braid realizations, not the inverse-speed torpids arrangement. It is the strongest named evidence that a charpoly-level signed cell-sum exists in principle for the parity, not a ready-made solver.

## Cross-references

- Kabluchko arXiv:2008.06719 (projection-dimension chamber counts = |charpoly coefficients|).
- Klivans–Swartz arXiv:1001.5095 (average projection volumes = coefficients).
- Aguiar–Bastidas–Mahajan arXiv:1902.07325 (characteristic elements from intrinsic volumes, signed face sums, Zaslavsky-type identities).
- Greene–Zaslavsky (chromatic-coefficient interpretation).
- Stanley IAS/PCMI notes (hyperplane arrangements).

```claim
id: charpoly-signed-region-generating-function
statement: For a real hyperplane arrangement A in R^n and a generic v, the characteristic polynomial satisfies χ_A(t) = Σ_R (−1)^{n−pdv(R)} t^{pdv(R)}, where pdv(R) is the projection dimension of v onto the region R — a signed, weighted sum over the regions evaluated from the characteristic polynomial without enumerating the regions.
hypotheses: real hyperplane arrangement; generic point v (off faces); projection-dimension statistic pdv(R).
holds-here: unchecked — the torpids parity sum is also a signed sum over cells (sign = parity) of simplex-section volumes, so this proves a signed region-sum can be charpoly-level in principle; but the sign/weight here are the projection-dimension ones, not the parity sign, and the arrangements treated are graphical/braid, not the inverse-speed torpids arrangement.
status: sourced (arXiv:2506.00941)
bearing: the strongest primary evidence that the parity (a signed cell-sum) could have a charpoly-level closed form; route-principle, not the answer.
anchor: Goregaokar 2025, arXiv:2506.00941 (via Lofano–Paolini arXiv:1809.02476)
```

```claim
id: characteristic-element-charpoly-linear-functional
statement: The characteristic polynomial of a real hyperplane arrangement is the evaluation of a characteristic element of the Tits algebra; aggregate sums over faces with signs/intrinsic volumes (Zaslavsky, Kung, Klivans–Swartz) are captured by such elements without enumerating regions.
hypotheses: real hyperplane arrangement; Tits algebra / characteristic elements; intrinsic-volume face data.
holds-here: unchecked — this is the algebra of "signed face-sums collapse to a charpoly object"; the torpids parity is exactly such a signed cell-sum, but the framework's examples are standard arrangements and intrinsic volumes, not the torpids inverse-speed arrangement or its parity weight.
status: sourced (arXiv:1902.07325)
bearing: the named algebra where a charpoly-level expression for the parity would live; route-principle for the exact p(n,L) reduction.
anchor: Aguiar, Bastidas & Mahajan 2019, arXiv:1902.07325
```
