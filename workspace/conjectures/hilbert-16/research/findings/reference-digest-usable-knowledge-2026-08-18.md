# Reference-library digest: usable knowledge for H16.2

Memory indexing was unavailable during this digest; this file is the durable local fallback. `remember_memory` was attempted and failed with a memory-service health timeout. The source-backed entries below should be re-submitted when the service recovers.

## Core object and reduction

**DRR 1994; Ilyashenko 2002; Panazzolo–Rousseau 2017.** The target is the uniform Hilbert number H(n), the supremum of isolated periodic-orbit counts for polynomial planar fields of degree at most n. Roussarie's compactification reduces the quadratic uniform problem to finite cyclicity of limit-periodic sets/graphics; the conventional catalogue has 121 entries, while Shan's thesis reports 125, so the exact reconciliation is unresolved. Panazzolo–Rousseau classify algebraic limit-periodic sets topologically as compact connected semialgebraic subsets of the sphere of dimension 0 or 1, but do not prove finite cyclicity. A minimal obstruction to H(2)<∞ is therefore an infinite-cyclicity compactified graphic, particularly a nilpotent/degenerate one.

**Implication:** do not treat topology/classification as a zero bound. The object to control is the displacement/return-map germ near each graphic.

## Elementary and selected graphic results

**Ilyashenko–Yakovenko 2000; Kaloshin 2000.** Generic finite-parameter families with elementary polycycles have finite cyclicity. Kaloshin gives an explicit exponential-scale bound (recorded locally as 2^(25k^2)); the hypotheses are elementary/nonzero-eigenvalue singularities and generic finite-parameter families. This does not cover nilpotent or degenerate graphics.

**DGR 2002.** Seven named elementary quadratic graphics are finite-cyclic, with explicit bounds 2 or 3 under stated saddle-ratio/centrality hypotheses: H^3_4, H^3_5, H^3_6, I^2_14a, I^2_15a, I^2_15b, I^2_27.

**Zhu–Rousseau 2002; Rousseau–Shan–Zhu 2015.** Blow-up of nilpotent unfoldings, first/second Dulac maps, normal forms, and derivation–division yield restricted finite-cyclicity results. RSZ 2015 proves I^1_12 and I^1_13. RR 2015 fully proves I^1_14, but only proves boundary limit-periodic sets for I^1_6b, H^3_13, and DI_2b; the full four-second-type-Dulac I^1_6b problem remains open in the held corpus.

**Dumortier–Ilyashenko–Rousseau 2002; Dumortier–Rousseau 2009.** Saddle-node normal-form/blow-up machinery and derivation–division close further classes. DR 2009 treats degenerate graphics with lines of singularities and gives explicit bounds for DF1a/DF2a, while identifying a non-desingularizable obstruction later addressed for DF2a by Huzak 2018. The analytic/non-flat normal-form step is precisely where a smooth-only argument would fail.

## Analytic boundary

**Écalle 1990; Ilyashenko; Mourtada–Moussu 1997.** These sources support the analytic/quasianalytic machinery behind individual finiteness and Dulac-map zero control, but the unrestricted primary proof material is limited in the local corpus. Yeung 2024/25 claims a gap in Ilyashenko's non-hyperbolic ordering-of-asymptotics step, with an explicit FC^{1,1} counterexample; it does not disprove the theorem, and hyperbolic cases are not challenged. Llibre et al. 2024 reports that the community treats general Dulac finiteness as under review. Bamón 1986 and Romanovskii independently support pointwise finiteness for each quadratic field.

**Implication:** report individual finiteness as contested in proof status, not as a uniform theorem. Any proposed proof must identify the analytic/quasianalytic step; finite Taylor/asymptotic data alone is insufficient.

## Abelian/Picard–Fuchs rung

**Binyamini–Novikov–Yakovenko 2010.** For nonsingular compact ovals of polynomial Hamiltonians and polynomial perturbation 1-forms, the number of isolated Abelian-integral zeros has an explicit doubly-exponential degree bound (the source states a bound of the form 2^(2^(O(n^61)))); this yields a corresponding bound for limit cycles born in non-conservative first-order Hamiltonian perturbations. It excludes critical/nonsmooth levels and conservative perturbations.

**Binyamini–Dor 2011; Novikov–Yakovenko; Gavrilov; GMV.** Picard–Fuchs/Petrov-module structure and Chebyshev criteria provide sharper or special-family results, including bounds linear in deg(ω) with exp-plus dependence on deg(H), and exact ECT criteria under separated-Hamiltonian/involution hypotheses. None applies directly to a nonlinear composition of four Dulac maps in I^1_6b without a new uniform representation theorem.

**Implication:** Abelian-integral methods are a valid weakened target, not a solution of full H16.2. GMV's ECT theorem cannot be cited for the complete I^1_6b displacement unless all separated-Hamiltonian, balance, Wronskian, small-o, and parameter-uniform hypotheses are first proved.

## Calibration and negative evidence

**Bautin 1952.** For quadratic systems, the local cyclicity of a single focus/center is M(2)=3 under all coefficient variations. This is not H(2): globally, H(2)≥4. The canonical focus chart and Lyapunov quantities are the correct exact algebraic calibration for a Bautin oracle.

**Galias–Tucker 2022.** Rigorous adaptive interval arithmetic proves the Songling quadratic system has exactly four cycles at widely separated scales. This certifies H(2)≥4 and demonstrates why un-certified numerical integration is inadequate.

**Christopher–Lloyd 1995; Gasull–Santana 2024; Llibre et al. 2024.** The known lower block is H(2)≥4, H(3)≥13, H(4)≥28, and asymptotic growth at least order n² log n. Gasull–Santana also state H(n+1)≥H(n)+1 and conditional structural-stability facts, but no upper bound. Any quadratic-order general upper formula is impossible.

**DPR/Liénard sources.** Slow–fast/canard constructions defeat the classical Lins–de Melo–Pugh sharp Liénard count (degree 6/7 distinctions are source-dependent; the held Llibre–Zhang survey credits the degree-6 four-cycle case separately from DPR's n≥7 result). This is a warning/test, not an H(2) upper-bound result.

**Pedregal 2021; Buzzi–Novaes 2024.** Pedregal claims quartic H(n) bounds and H(2)=4, but is unrefereed and its variational argument does not use analytic return-map structure, failing the smooth test prima facie. Buzzi–Novaes refute a separate quadratic closed-form proposal using the n²log n lower growth. Neither establishes H16.2.

**Lu 2026.** The preprint claims local uniform finite cyclicity for H^3_14 in a five-parameter quadratic unfolding. The workspace independently checked finite algebraic/Bautin identities only; the analytic remainder, root uniqueness, domain completeness, and zero theorem are not machine-checked. Treat as asserted-by-source, not established.

## Sources that do not help directly

- Landing pages, bibliographic records, captcha pages, and mismatched captures establish provenance only. In particular the local Kaleda–Shchurov file is a content mismatch; the local DPR file is a record page; the IOP GMV digest is captcha-only; the Ilyashenko AMS page is bibliographic/landing-level.
- Panazzolo–Rousseau gives topology, not cyclicity.
- BNY/Binyamini–Dor/Novikov–Yakovenko/Gavrilov/GMV address tangential Hamiltonian perturbations, not arbitrary nonlinear DRR displacement compositions.
- Pedregal and Buzzi–Novaes are critique/dead-end evidence; Yeung challenges a proof but does not disprove finiteness; Lu's verified algebraic core does not establish its analytic theorem.
- The 2024 Christopher–Li–Torregrosa source is a book TOC: it catalogues a unified weak-H16 n=2 chapter but does not expose its proof.

## Contradictions to recalled memory

1. RR 2015 did not fully close all four named center graphics: I^1_14 is full; I^1_6b, H^3_13 and DI_2b have boundary-only results.
2. The catalogue count is conventionally 121 but Shan reports 125; no authoritative reconciliation is held.
3. Older sources state Dulac finiteness as settled; Yeung 2024/25 and Llibre 2024 report a live proof-status challenge. This is a contradiction about proof completeness/status, not a counterexample to the theorem.
4. H(2)=4, H(3)≥13, and H(n)≈n²log n are lower/status claims only; no source establishes H(2)<∞ or H(2)=4.

## Exact next use

The most defensible partial result is not a conjecture claim: formalize the displacement-function/cyclicity definition and a restricted theorem (elementary or selected graphic) in Lean, while preserving the verified Bautin identities and exact interval-oracle evidence. The full I^1_6b four-Dulac closure remains blocked by the missing analytic two-equation zero theorem.