# Reference digest: H16.2

Cognee `remember_memory` was unavailable (health timeout); this durable workspace note records the digest pending recovery.

## Core formulation
For polynomial planar fields `X=(P,Q)` with `max(deg P,deg Q)<=n`, a limit cycle is an isolated periodic orbit and `H(n)` is the supremum of their counts. The unresolved theorem is uniform finiteness `H(n)<∞`; pointwise finiteness and tangential bounds do not imply it.

## Sources that bear directly
- **DRR 1994** (JDE 110, 86–133; local summary): reduces quadratic uniform finiteness to finite cyclicity of 121 graphics/limit-periodic sets. Exact full row ledger is not held; the 121/125 discrepancy remains.
- **Roussarie–Rousseau 2015** (arXiv:1506.07104): finite cyclicity of `I^1_14`; only boundary limit-periodic sets for `I^1_6b`, `H^3_13`, `DI_2b`. Full `I^1_6b` non-boundary strata involve four second-type Dulac maps and a coupled two-equation displacement problem.
- **Rousseau–Shan–Zhu 2015** (arXiv:1502.00689): proves selected nilpotent-saddle graphics (`I^1_12`, `I^1_13`) using normal forms, blow-up, Dulac maps, and displacement functions; its stated first-type formulas do not supply the four second-type expansion needed for full `I^1_6b`.
- **Dumortier–Rousseau 2009**: treats degenerate `DF1a/DF2a`; slow-divergence integral after family blow-up controls cyclicity when nonzero. Huzak 2018 closes `DF2a`, but this does not transfer to `I^1_6b`.
- **Ilyashenko–Yakovenko/Kaloshin**: elementary polycycles in generic finite-parameter analytic/smooth families have finite cyclicity; Kaloshin supplies an explicit exponential-type estimate under elementary hypotheses. The elementary hypothesis is exactly what excludes the unresolved nilpotent/degenerate cases.
- **Écalle 1990; Ilyashenko finiteness sources**: individual analytic-field finiteness uses resurgent/accelero-summation or quasianalytic structure, not a uniform coefficient bound. **Yeung 2024/25** challenges completeness of Ilyashenko's proof (leading-term/asymptotic ordering issue in semi-hyperbolic alternant polycycles), but does not disprove the finiteness theorem. This contradiction must remain flagged.
- **Binyamini–Novikov–Yakovenko 2010**: explicit double-exponential bound for zeros of Abelian integrals from nonsingular ovals in small nonconservative polynomial Hamiltonian perturbations; this solves tangential H16 only. **Binyamini–Dor** sharpens dependence to linear in perturbation-form degree. These do not bound the nonlinear displacement or H(2).
- **Novikov–Yakovenko/Gavrilov/GMV**: Picard–Fuchs/Petrov modules and Chebyshev criteria provide the structural route for Abelian-integral zero counts, under their Hamiltonian/oval hypotheses; no implication to full H16.2 without a nonlinear reduction.
- **Bautin 1952**: local quadratic focus cyclicity `M(2)=3`, via the Bautin ideal. Workspace's exact finite algebraic core for Lu's `H^3_14` preprint is computationally checked (bridge identities, degree-4 and degree-6 Lyapunov identities), but this is not Lu's analytic theorem.
- **Shi/Chen–Wang; Li–Liu–Yang; Christopher–Lloyd/Han–Li; Prohens–Torregrosa**: lower calibrations `H(2)>=4`, `H(3)>=13`, `H(4)>=28`, and asymptotic growth at least order `n^2 log n`; `M(2)=3`, `M(3)>=11`. Any proposed upper bound must pass these tests.
- **DPR/Liénard**: slow-fast/canard constructions refute the Lins–de Melo–Pugh sharp Liénard conjecture (degree 6 already has four cycles; general lower constructions grow); this is a mandatory stress test for sharp counts, not a solution of H16.2.
- **Buzzi–Novaes 2024**: critiques a claimed global solution; quadratic closed-form upper candidates conflict with known lower growth. It does not solve H16.2.
- **Lu 2026, arXiv:2607.13785**: claims local uniform finite cyclicity for `H^3_14` in a five-parameter unfolding. The workspace independently checked only finite polynomial identities; root uniqueness, domain completeness, analytic remainder and zero theorem remain unverified, and the preprint is unrefereed. Treat as asserted/unverified, not closure.
- **Kaiser–Rolin–Speissegger/Speissegger**: o-minimal transition-map route would yield uniform finiteness if the required o-minimality of the full parametric transition-map language were proved; it is proved only in restricted non-resonant hyperbolic classes, so this is a route, not a solution.

## Sources that do not help as proof
Landing/record pages and citation-graph files establish bibliographic leads only, not theorem details; local summaries explicitly flag these. The broken Álvarez–Coll–De Maesschalck–Prohens capture cannot support a numerical claim. The contaminated file named `llibre-zhang-lienard-survey` is an unrelated German power-grid paper. Pedregal's unrefereed variational H16 claim fails the smooth/analyticity test prima facie and is not established. Numerical phase portraits are not certificates.

## Contradictions / cautions
1. Individual analytic finiteness is recorded as established in the classical literature, but Yeung claims a serious gap in Ilyashenko's proof; theorem truth and proof completeness must be distinguished.
2. DRR/RSZ/RR report 121 graphics, while Shan's thesis reports 125; no complete reconciled ledger is held.
3. RR 2015's partial closures must not be upgraded to full closures.
4. Lu's checked algebraic identities must not be upgraded to its analytic finite-cyclicity theorem.

## Partial result justified by the library
The problem is reduced to exact displacement-function finite-cyclicity statements for the remaining non-elementary DRR graphics. A concrete current target is the full `I^1_6b` four-second-type Dulac composition: the missing theorem requires parameter-uniform expansions, resonant/flat remainder control, and a zero theorem for the coupled displacement system. The library supplies no proof of that step, so the honest endpoint is a sharply specified obstruction, not a global bound.