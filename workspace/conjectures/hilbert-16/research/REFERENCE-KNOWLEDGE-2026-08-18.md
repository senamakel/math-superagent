# Reference-library knowledge extraction

Memory service was unavailable (repeated timeout/409), so this file is the durable local fallback.

## Source-backed findings

- **H16.2 / DRR:** H(n) is the supremum of isolated periodic-orbit counts for planar polynomial fields of degree ≤n. Uniform finiteness remains open, including H(2). DRR/Roussarie compactification reduces the quadratic case to finite cyclicity of a conventional 121-graphic catalogue; Shan reports 125, an unresolved convention/count discrepancy. A minimal obstruction is an infinite-cyclicity compactified limit-periodic graphic, especially a non-elementary nilpotent/degenerate graphic. Source: DRR 1994; Ilyashenko 2002; RSZ/RR 2015. URL anchor: http://hdl.handle.net/1942/3763.

- **Elementary polycycles:** Kaloshin and Ilyashenko–Yakovenko give finite cyclicity for elementary polycycles in generic finite-parameter families; Kaloshin gives exponential-scale explicit estimates. Kaleda–Shchurov gives polynomial-in-parameter estimates when the number of elementary vertices is fixed. The weight-bearing hypotheses are elementary/nonzero-eigenvalue singularities and genericity; these results do not cover nilpotent/degenerate graphics. Sources: https://arxiv.org/html/math/0010174; DOI https://doi.org/10.1090/S1061-0022-2011-01158-6.

- **Quadratic restricted graphics:** DGR 2002 proves finite cyclicity for seven named elementary quadratic graphics. RSZ 2015 closes named nilpotent graphics I¹₁₂ and I¹₁₃. RR 2015 fully closes I¹₁₄ but only boundary limit-periodic sets for I¹₆b, H³₁₃ and DI₂b. No source held here closes the full I¹₆b four-second-type-Dulac problem; the paper explicitly leaves the coupled non-boundary case for future work.

- **Abelian-integral rung:** Binyamini–Novikov–Yakovenko give an explicit double-exponential zero bound, 2^(2^(O(n^61))), for Abelian integrals over nonsingular ovals with bounded degrees. Binyamini–Dor give an explicit bound linear in deg ω with exp-plus dependence on deg H. Novikov–Yakovenko provide module/Picard–Fuchs structure; Gavrilov and GMV provide special Hamiltonian/Chebyshev results. These apply to first-order/tangential Hamiltonian perturbations, not arbitrary nonlinear compositions of Dulac maps. Sources: https://arxiv.org/html/0808.2952; https://arxiv.org/html/1108.1846.

- **Individual finiteness:** Écalle–Ilyashenko sources attribute finiteness of limit cycles for individual analytic polynomial fields, but Yeung 2024–25 challenges completeness of Ilyashenko’s proof in the non-hyperbolic case. This is a proof-status contradiction, not a disproof of the theorem. Source: https://arxiv.org/abs/2402.12506.

- **Lower bounds and tests:** Rigorous quadratic constructions establish H(2)≥4; Bautin gives local quadratic-focus cyclicity M(2)=3. The library records H(3)≥13 and H(n)≳n²log n (Christopher–Lloyd/Han–Li), so any quadratic-order general upper bound is impossible. Slow–fast Liénard constructions refute the classical sharp Lins–de Melo–Pugh count. These are calibration constraints, not an upper-bound route.

- **Recent claims:** Lu 2026 claims local uniform finite cyclicity of H³₁₄. The workspace independently checked only the finite algebraic/Bautin identities; analytic root uniqueness, domain completeness, and the uniform zero theorem remain unchecked, and the preprint is unrefereed. Pedregal’s variational claim is unrefereed and fails the required smooth/analyticity test prima facie; Buzzi–Novaes refute a separate closed-form proposal using the n²log n lower growth.

## Sources that do not help directly

Landing pages, bibliographic records, and mismatched captures establish provenance only and cannot support exact theorem statements. Panazzolo–Rousseau classifies compactified limit-periodic sets structurally but does not prove finite cyclicity. BNY/Binyamini–Dor/Novikov–Yakovenko/Gavrilov/GMV address the tangential or special Hamiltonian problem, not full H16.2. Pedregal and Buzzi–Novaes are useful as critique/dead-end evidence, not positive proof. Yeung challenges proof completeness but does not disprove finiteness. Lu’s verified algebraic core does not establish its analytic theorem.

## Contradictions to recalled memory

RR 2015 did not fully close all four named center graphics: only I¹₁₄ is fully closed; I¹₆b, H³₁₃ and DI₂b have boundary-set results only. The conventional DRR count is 121, while Shan reports 125. Classical individual finiteness is treated as settled in older surveys, but Yeung’s recent gap claim makes proof completeness contested. H(2)=4 and H(n)<∞ remain unsupported.
