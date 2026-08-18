# Refutation: bare `k−1` zero bound from center-ideal division

## Target attacked

The current weakened rung `R-center-ideal-zero-division` assumes a displacement expansion
\[
\Delta(z;\lambda)=\sum_{i=1}^k a_i(\lambda)m_i(z)(1+h_i(z;\lambda)),
\]
with coefficients in the center ideal \(\langle L_4,L_6,L_8\rangle\), generalized monomials from the vertex asymptotic classes, and uniformly small remainders \(h_i=o(1)\). The proposed inference is a `k−1` zero bound.

## Smallest structural obstruction

The first obstruction is **cancellation plus an uncontrolled oscillatory remainder**, already at \(k=2\):
\[
 m_1=m_2=1,\qquad a_1=1,\ a_2=-1,
\]
\[
 h_1=0,\qquad h_2(x)=e^{-1/x^2}\sin(1/x),\qquad 0<x<1.
\]
Then
\[
 \Delta(x)=h_1-h_2=-e^{-1/x^2}\sin(1/x)
\]
has exact zeros \(x_n=1/(\pi n)\), infinitely many, while \(k-1=1\). Every finite jet of \(h_2\) at \(0^+\) vanishes, and \(h_2=o(1)\), so finite Taylor/asymptotic data and smallness do not control the exact zero set. This is the minimal \(k=2\) instance of the mechanism the executed artifact `code/out/i6b_transseries_counterexample.captured.txt` already certifies symbolically (flat remainder \(e^{-1/x}\sin(1/x)\) with all tested jets zero).

This is an abstract germ counterexample, **not** a counterexample inside the quadratic \(H^{3}_{14}\) family. It also uses coincident monomials. If “monomials determined by asymptotic classes” is intended to require pairwise distinct ordered classes, this particular witness is excluded; that is precisely a missing hypothesis that must be stated rather than assumed.

A distinct-class variant has the same mechanism: take \(m_1=1,m_2=x\), \(a_1=1,a_2=-c\), and \(h_1(x)=r(x)\sin(1/x)\), \(h_2=0\), where \(r(x)=1/\log(1/x)\to0\). Near the crossover \(x\approx1/c\), the rapidly oscillating remainder can create arbitrarily many sign changes as \(c\to\infty\), unless a uniform coefficient-separation/zero-transfer theorem is imposed. This variant is a hand construction/diagnostic here, not claimed as an executed certificate.

## Mechanical checks and their limits

- Existing executed artifact `code/out/i6b_transseries_counterexample.captured.txt` verifies the same finite-truncation versus flat oscillatory-remainder mechanism symbolically (exact derivatives/limits through the reported order), but its nonzero leading term masks the zeros; it is evidence against the reduction, not a dynamical counterexample.
- New oracle `code/refute/center_ideal_kminus1_oracle.py` encodes the sharper `k=2` cancellation witness and exact zeros. It was written but could not be executed in this API session because no shell/run tool is exposed; therefore its output is **unverified**, not reported as a checked computation.
- Required finite-model attack: `find_counterexample` on `code/refute/center_ideal_zero_division.p` returned `undecided; SZS status: none reported`. This is not evidence for the claim: the TPTP problem uses uninterpreted schematic functions and does not faithfully encode real asymptotics or zero sets.

## Verdict

**Refuted as an implication of the stated bare expansion and `o(1)` remainder data.** No counterexample to Lu’s actual quadratic-vector-field theorem was found or claimed. The verified algebraic fact that higher focal quantities lie in the center ideal does not provide a Chebyshev space or a zero bound.

## Exact missing analytic condition

The proof must add, and verify uniformly over the compact parameter box:

1. **A common exact function class:** all composed second-type Dulac maps and remainders must lie in a specified parameter-uniform quasianalytic/Noetherian (or equivalent controlled transseries) algebra closed under composition, restriction, differentiation and the center-ideal division.
2. **A zero-transfer theorem:** the actual functions \(m_i(1+h_i)\), not their finite asymptotic truncations, must satisfy a uniform derivation–division bound or an ECT/Chebyshev Wronskian certificate on every parameter stratum.
3. **Nonidentity and coefficient separation:** on every nonzero projective parameter direction, the divided displacement must not vanish identically; cancellations between the leading coefficient vector and remainder terms must be excluded or separately resolved. Distinct asymptotic classes must be stated explicitly if required.
4. **Uniform domains and itinerary completeness:** one common physical collar/domain and an exhaustive finite composition of Dulac/regular transition maps, with uniform remainder estimates, are needed before compactness can turn local bounds into a parameter-uniform bound.

`h_i=o(1)` in `C^k`, finite jets, or property-J asymptotics alone is insufficient because flat oscillatory germs survive all such finite data.

## Search frame

The abstract witness lies in the space of analytic/smooth germs with finite-jet and small-remainder constraints, outside any published exhaustive sweep of the 121 DRR graphics. The TPTP model search reached no finite model for the deliberately schematic encoding; it did not search the actual quadratic family.
