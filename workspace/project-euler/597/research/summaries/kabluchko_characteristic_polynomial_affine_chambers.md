# Kabluchko, "An identity for the coefficients of characteristic polynomials of hyperplane arrangements" (arXiv:2008.06719, 2020)

Source URL: https://arxiv.org/abs/2008.06719 (full text at `research/sources/kabluchko_characteristic_polynomial_affine_chambers.full.md`).

## What it establishes

For a finite collection of **affine** hyperplanes in R^d dissecting R^d into polyhedral chambers: for each k ∈ {0,…,d}, the number of chambers P for which the metric projection of a point x lands in the relative interior of a k-dimensional face of P — denoted dim(x,P) = k — is **independent of x** (except on a Lebesgue null set), and equals the absolute value of the k-th coefficient of the characteristic polynomial of the arrangement. In the special case of reflection arrangements this proves the Drton–Klivans conjecture.

## Bearing on PE597

This is the affine-chamber analogue of Klivans–Swartz (the run's parity arrangement is affine: hyperplanes (L−p_j)/v_j and 40(j−i)/(v_i−v_j), assigned to the simplex). It shows that an aggregate "profile" of the chambers — here the distribution of projection-face dimensions — is a charpoly coefficient and does not require enumerating the chambers. **Caveat identical to Klivans–Swartz:** the statistic counted (projection dimension) is not the torpids sign/parity weight, and the volume is not the simplex-section volume the run needs; it is surface (spherical) projection measure. So it is the standard result that "chamber-aggregate statistics come from the characteristic polynomial," a named lead for any charpoly-based route to the parity sum, not itself the parity answer. No region enumeration is needed to get the *counts* it describes.

## Cross-references

- Klivans–Swartz arXiv:1001.5095 (central-arrangement projection volumes).
- Cites Lofano–Paolini arXiv:1809.02476 and Drton–Klivans PAMS 138(8) 2010.
- Stanley notes (Zaslavsky) for the region-count theme.
