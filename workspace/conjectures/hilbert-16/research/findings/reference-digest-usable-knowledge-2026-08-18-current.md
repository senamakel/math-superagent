# Reference digest: usable knowledge (2026-08-18)

## Scope and object
H16.2 asks whether the supremum H(n) of isolated periodic-orbit counts for planar polynomial vector fields of degree at most n is finite. The relevant analytic object is the displacement function (Poincare return map minus identity), not a numerical phase portrait. The run must not claim H(n)<∞ or H(2)=4.

## Source-backed findings

1. **DRR/Roussarie reduction.** The quadratic problem is reduced to finite cyclicity of a conventional catalogue of 121 graphics/limit-periodic sets in the compactified family (DRR 1994; echoed by Ilyashenko 2002 and RSZ/RR 2015). Shan's thesis reports 125, so the count convention is unresolved. A minimal obstruction to uniformity is an infinite-cyclicity non-elementary nilpotent/degenerate graphic. Sources: `primary-rousseau-shan-zhu-nilpotent-saddle-graphics-2015-v1.full.md`, `primary-roussarie-rousseau-2015-center-graphics.full.md`, `primary-panazzolo-rousseau-limit-periodic-sets-v1.full.md`.

2. **Concrete quadratic status.** RSZ 2015 proves finite cyclicity for named nilpotent saddle graphics I^1_12 and I^1_13. Roussarie–Rousseau 2015 fully proves I^1_14, but for I^1_6b, H^3_13 and DI_2b proves only boundary limit-periodic-set results. The full I^1_6b case contains coupled configurations with four second-type Dulac maps and is explicitly not reduced to a single equation. Thus the boundary result cannot be promoted to full finite cyclicity without a new uniform displacement-function argument. DGR and related DRR papers settle several elementary/pp/degenerate subfamilies; Huzak's DF_2a slow-divergence result is for a different family and cannot be transferred automatically.

3. **Elementary restricted class.** Ilyashenko–Yakovenko/Kaloshin establish finite cyclicity for elementary polycycles in generic finite-parameter families, with explicit exponential-scale estimates; Kaleda–Shchurov gives an estimate polynomial in parameter number when the number of elementary vertices is fixed. The essential hypotheses are elementary singularities/nonzero eigenvalues and genericity. Nilpotent/degenerate graphics, the main quadratic obstruction, are excluded.

4. **Tangential/Abelian rung.** Binyamini–Novikov–Yakovenko prove a constructive double-exponential zero bound for Abelian integrals over nonsingular ovals in polynomial Hamiltonian perturbations, of the form 2^(2^(O(n^61))). Binyamini–Dor give an explicit bound linear in deg(omega) with exp-plus dependence on deg(H). Novikov–Yakovenko give module/Picard–Fuchs structure; Gavrilov and Grau–Manosas–Villadelprat provide special Chebyshev/Petrov results. These bounds concern first-order Hamiltonian displacement (Abelian integrals), not arbitrary nonlinear compositions of Dulac maps, so they do not imply H(2)<∞.

5. **Pointwise finiteness and its caveat.** Écalle and Ilyashenko sources attribute individual analytic-field finiteness, while Bamón gives individual quadratic finiteness. Yeung 2024–25 challenges a proof step for non-hyperbolic polycycles. This is a contradiction about proof completeness/status, not a disproof of the finiteness theorem. It also does not supply coefficient-uniformity.

6. **Calibration constraints.** The library records H(2)>=4, M(2)=3 (Bautin), H(3)>=13, H(4)>=28, M(3)>=11, and H(n) growing at least on the order of n^2 log n. Any proposed upper bound must pass these tests. Slow-fast Lienard constructions disprove the classical sharp Lins–de Melo–Pugh count; this is a warning against sharp-count arguments.

7. **Recent/unverified proposals.** Lu 2026 claims local uniform finite cyclicity of H^3_14 in a five-parameter unfolding. Exact algebraic/Bautin identities in its finite core were independently checked, but analytic root uniqueness, domain completeness, and the uniform zero theorem remain unchecked; the preprint is unrefereed. Pedregal's variational H16 claim is unrefereed and fails the smooth/analyticity test prima facie. Buzzi–Novaes refute a different closed-form upper-bound proposal using the n^2 log n lower growth.

## Sources that do not help directly
Landing pages, bibliographic records, citation-graph files, and mismatched captures establish provenance only. Panazzolo–Rousseau classifies limit-periodic sets but does not prove cyclicity. Abelian-integral/Picard–Fuchs sources solve only the tangential problem. Pedregal and Buzzi–Novaes are critique/dead-end evidence, not positive H16.2 proofs. Yeung challenges Ilyashenko's proof but does not disprove finiteness. Lu's checked algebraic identities do not establish its analytic theorem. Broken canard/landing captures cannot support exact numerical claims.

## Contradictions to recalled memory
- RR 2015 did **not** fully close all four named center graphics: only I^1_14 is fully closed; I^1_6b, H^3_13 and DI_2b have boundary-set results.
- DRR/RSZ/RR use 121 graphics, while Shan reports 125.
- Older sources treat individual analytic finiteness as settled; Yeung's recent claim makes the proof completeness contested.
- H(2)=4 and H(n)<∞ remain unsupported.

Memory-server persistence was unavailable during this run; this file is the durable local fallback and should be re-submitted to memory when the service recovers.