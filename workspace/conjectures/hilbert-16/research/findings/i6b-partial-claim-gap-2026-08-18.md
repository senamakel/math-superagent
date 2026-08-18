# I^1_6b: precise partial claim and remaining gap

## Claim supported by the held literature
For the boundary limit-periodic set produced by the family blow-up of the quadratic graphic I^1_6b, finite cyclicity is proved: on each invariant leaf `r rho = nu`, the displacement equation has finitely many zeros, with an explicit local bound in the Roussarie–Rousseau derivation–division analysis. This is only the boundary set, not the whole graphic.

The source is Roussarie–Rousseau, *Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems*, arXiv:1506.07104, Theorem 1.1 and the general discussion: the paper explicitly says that I^1_6b, H^3_13 and DI_2b have finite boundary-set cyclicity, while the other blown-up limit-periodic sets are not thereby settled. It also explicitly says that the I^1_6b non-boundary sets requiring four second-type Dulac maps lead, in the center case, to two equations in `(r1,rho1,r2,rho2)` with `r_i rho_i=nu_i`; no one-dimensional reduction is claimed.

## Exact hypotheses/results found
The derivation–division theorem (RR, Appendix II, Theorem 5.8) applies to a displacement function
`V = sum A_i(lambda) M_i (1+g_i)` on a sufficiently small product neighborhood, where `M_i=r^{a_i}rho^{b_i}omega^c` are general monomials without Omega factors, `g_i` are C^k-functions on monomials of order o(1), `A_i` are continuous, `k >= l`, and pairwise differences satisfy the non-resonance condition `(a_j^0-a_i^0)-(b_j^0-b_i^0) != 0`. Then either there are at most `l-1` isolated zeros on each connected leaf `r rho=nu`, or the displacement is identically zero.

For resonant integer exponents, RR Theorems 5.12 and 5.13 give separate bounds (at most 3 for integer `p != 1`, at most 2 for `p=1`) under the refined remainder hypotheses. In particular, Lemma 5.10 requires a remainder `r^alpha omega_alpha(1+O(r^delta))`; RR Remark 5.11 warns that replacing this by a generic `o(1)` factor is invalid because differentiation produces an uncontrolled `omega_alpha rho` term.

The first-type Dulac formula in Rousseau–Shan–Zhu (2015), Theorem 2.3, is explicit: for a blow-up saddle with `r dot=r`, `rho dot=-rho`, and the stated resonant normal forms, the map from `{rho=rho0}` to `{r=r0}` has the power/compensator form and a property-J remainder. The paper explicitly says only first-type maps are needed there. It does not supply a complete four-second-type formula for I^1_6b.

## Slow divergence and ECT: what is and is not licensed
A slow-divergence integral can certify a leading displacement/Melnikov coefficient in a slow-fast blow-up, but the held Huzak 2018 result is for the different DF2a geometry and does not transfer its hypotheses to I^1_6b. GMV's ECT theorem (Grau–Manosas–Villadelprat, 2008) is a sufficient criterion for Abelian integrals over ovals of separated Hamiltonians, requiring the stated balance/CT conditions and endpoint hypotheses. No held source identifies the complete I^1_6b four-map displacement with such an Abelian-integral family. Therefore ECT can be invoked only conditionally after an exact reduction and uniform Wronskian verification.

## Falsifier
The partial claim would be false if RR Theorem 1.1 did not include I^1_6b's boundary limit-periodic set, or if its Appendix-II hypotheses failed for the displayed displacement form. The broader extrapolation would be false if a source supplied a complete uniform second-type Dulac expansion and a finite-rank ECT/derivation–division reduction for every four-map I^1_6b stratum. No such source was found in the held library or the targeted searches.

## Sources
- https://arxiv.org/abs/1506.07104 (Roussarie–Rousseau 2015), especially Theorem 1.1, §3.2, Appendix II §§5.2–5.3.
- https://arxiv.org/abs/1502.00689 (Rousseau–Shan–Zhu 2015), §2.6 and Theorem 2.3.
- Huzak 2018, `research/sources/huzak-cyclicity-degenerate-df2a.full.md`.
- GMV 2008, `research/sources/grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md`.
