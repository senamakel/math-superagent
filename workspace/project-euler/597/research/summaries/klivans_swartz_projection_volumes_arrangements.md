# Klivans & Swartz, "Projection volumes of hyperplane arrangements" (arXiv:1001.5095, 2010)

Source URL: https://arxiv.org/abs/1001.5095 (full text at `research/sources/klivans_swartz_projection_volumes_arrangements.full.md`).

## What it establishes

For any finite real hyperplane arrangement A in R^d, the **average projection volumes of the maximal cones (regions)** are exactly the coefficients of the characteristic polynomial of A. Specifically (settling the Drton–Klivans conjecture): for each k, the sum over regions C of the spherical volume of points projecting into the interior of a k-dimensional face of C equals a multiple of |coef of t^(r−d+k)| in χ_A(t). Consequence: the angle sums of a zonotope are given by the characteristic polynomial of the order dual of the intersection lattice of the arrangement.

## Bearing on PE597

This is the standard reference for the *aggregate* statement "the collection of regions, weighted by projection/volume data, is encoded by the characteristic polynomial without enumerating the regions themselves." Shape-wise that is what the run's parity needs — p(n,L) is a signed sum of region (simplex-section) volumes on the torpids parity arrangement — and a charpoly-level formula would beat region enumeration. **But the hypotheses and the statistic do not transfer directly:** Klivans–Swartz aggregates unweighted (±1) projection volumes, whereas the torpids parity sum requires a sign weight −1 per odd-parity cell, which is not what the average-projection-volume statistic carries. So this is a named, citable model for "region statistics from the intersection lattice / characteristic polynomial," not a solver of the finite-finish parity. Pointer + adjacent machinery, with no region-by-region enumeration needed for the *average* case; the run's signed case is not covered.

## Cross-references

- Kabluchko 2020 (arXiv:2008.06719) gives the affine counterpart (chamber-projection identities from the charpoly).
- Stanley IAS/PCMI notes carry Zaslavsky's theorem (region counts from χ_A) — same "arrangement statistic from lattice" theme.
- Postnikov–Stanley / Bernardi / Fishel: braid-deformation region counts; the run established the torpids arrangement is none of these.

```claim
id: arrangement-projection-volume-charpoly
statement: For any finite real hyperplane arrangement A in R^d, the average projection volumes of its maximal cones (regions) are given by the coefficients of the characteristic polynomial of A (settling the Drton–Klivans conjecture); equivalently the region-collection, weighted by projection-volume data, is encoded by χ_A without enumerating regions.
hypotheses: finite real hyperplane arrangement; (unweighted) average projection volumes over regions.
holds-here: unchecked — the torpids parity sum needs a SIGN weight (−1 per odd-parity cell) over simplex-section volumes, which this average-projection-volume statistic does not carry.
status: sourced (arXiv:1001.5095)
bearing: named, primary evidence that "an aggregate of cell data is a characteristic-polynomial statistic, no region enumeration"; a model for any charpoly-based route to the parity sum, not the parity answer.
anchor: Klivans & Swartz, arXiv:1001.5095
```

```claim
id: affine-chamber-projection-profile-charpoly
statement: For a finite collection of affine hyperplanes in R^d, for each k the number of chambers P with metric-projection dimension dim(x,P)=k is independent of x (off a Lebesgue null set) and equals |k-th coefficient of the characteristic polynomial| of the arrangement.
hypotheses: finite affine arrangement in R^d; Lebesgue-generic x.
holds-here: unchecked — the torpids arrangement is affine (hyperplanes (L−p_j)/v_j and 40(j−i)/(v_i−v_j) cut into the simplex) but the statistic counted (projection dimension) is not the parity/sign weight and the relevant measure is simplex-section volume, not spherical projection measure.
status: sourced (arXiv:2008.06719)
bearing: the affine-chamber analogue of Klivans–Swartz; supports "chamber-aggregate statistics from the characteristic polynomial" as a route principle, not the parity itself.
anchor: Kabluchko, arXiv:2008.06719
```
