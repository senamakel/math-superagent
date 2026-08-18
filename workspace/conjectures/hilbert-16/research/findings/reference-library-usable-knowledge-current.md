# Source audit and implications for the open H16.2 attack

## Method
The library was read against `/workspace/problem.md` and the investigation objective. I treated primary/full-text records as theorem evidence, local exact captures as computational evidence, and landing pages or summaries as provenance only. The target is the uniform number H(n), but the working object is the displacement function D = return map minus identity near a limit-periodic set.

## Source-backed results that matter

### DRR/Roussarie compactification
DRR and successor papers reduce the quadratic uniform problem to finite cyclicity of compactified limit-periodic sets/graphics. The conventional count is 121; Shan's thesis reports 125, and the library has no authoritative reconciliation. Panazzolo–Rousseau classify limit-periodic sets topologically, but classification is not a zero bound. Therefore a minimal counterexample would be an infinite-cyclicity graphic in the compactified quadratic family, especially a nilpotent or degenerate graphic. This tells the attack exactly what must be bounded: zeros of the full displacement germ, not phase-portrait features.

### Elementary polycycles
Ilyashenko–Yakovenko and Kaloshin establish finite cyclicity for elementary polycycles in generic finite-parameter families; the recorded explicit Kaloshin bound is E(k) <= 2^(25 k^2). Kaleda–Shchurov supplies a bound polynomial in the parameter count when the number of elementary vertices is fixed. The hypotheses doing the work are elementary/nonzero-eigenvalue singularities and genericity. They do not cover nilpotent/degenerate graphics.

### Selected quadratic graphics
DGR 2002 settles seven named elementary quadratic graphics. Zhu–Rousseau and RSZ/RR settle selected nilpotent graphics, including I^1_12 and I^1_13; RR 2015 fully settles I^1_14. RR gives only boundary limit-periodic-set results for I^1_6b, H^3_13 and DI_2b. The full coupled I^1_6b four-second-type-Dulac displacement remains open in this corpus. Normal forms, blow-ups, Dulac maps, and derivation-division are the reusable machinery; the missing theorem is a uniform zero bound for the coupled remainder.

### Analytic finiteness
Écalle and Ilyashenko sources attribute finiteness of limit cycles for an individual analytic polynomial field. Yeung's 2024/25 work challenges completeness of Ilyashenko's non-hyperbolic proof, with an alleged failure in an ordering-of-asymptotics step. This is a contradiction about proof status, not a disproof of the theorem. It reinforces the smooth test: an asymptotic expansion alone cannot determine a return map. Individual finiteness is not uniform coefficient finiteness.

### Abelian/Picard–Fuchs rung
BNY gives an explicit doubly-exponential bound of the form 2^(2^(O(n^61))) for zeros of Abelian integrals over nonsingular compact ovals of polynomial Hamiltonians with polynomial perturbation forms. Binyamini–Dor gives an explicit bound linear in deg(omega), with exp-plus dependence on deg(H). Novikov–Yakovenko, Gavrilov and GMV provide module/Picard–Fuchs/Petrov-module and special Chebyshev criteria. These apply to first-order/tangential Hamiltonian perturbations, not arbitrary nonlinear compositions of Dulac maps. Their implication here is a valid restricted target, not a route to full H16.2 unless a new uniform representation theorem converts the target displacement into that class.

### Calibration and lower bounds
Bautin's primary result gives local quadratic-focus cyclicity M(2)=3. Rigorous interval work by Galias–Tucker certifies four globally separated cycles in a quadratic field, so H(2) >= 4. The library records H(3) >= 13, H(4) >= 28, and lower growth of order n^2 log n. Torregrosa 2024 already reports twelve cubic small-amplitude cycles; a twelfth-cycle target is therefore stale. Slow-fast Lienard constructions refute classical sharp count conjectures and must be used as a stress test, not as an upper-bound route.

### Recent claims and critiques
Lu 2026 claims local uniform finite cyclicity of H^3_14 in a five-parameter quadratic unfolding. Local exact code independently checks finite Bautin/algebraic identities only. Analytic root uniqueness, domain completeness, the remainder argument and the uniform zero theorem are not machine-checked; the preprint is unrefereed. Pedregal's variational H16.2 claim is unrefereed and prima facie fails the smooth test because it supplies no analytic/quasianalytic return-map step. Buzzi–Novaes refute a different closed-form H(n) proposal using n^2 log n growth.

## Sources that do not help directly
Landing pages, bibliographic records, captcha pages, and mismatched captures establish provenance only. Panazzolo–Rousseau supplies topology, not finite cyclicity. Abelian/Picard–Fuchs sources address tangential Hamiltonian perturbations, not arbitrary nonlinear DRR displacements. Pedregal and Buzzi–Novaes are critique/dead-end evidence. Yeung challenges proof completeness but does not disprove finiteness. Lu's checked algebraic core is insufficient for its analytic theorem. The Christopher–Li–Torregrosa 2024 book capture is a contents record, not a proof.

## Contradictions to recalled memory
- RR 2015 did not fully close all four named center graphics: I^1_14 is full; I^1_6b, H^3_13 and DI_2b have boundary-only results.
- The catalogue count is 121 conventionally versus 125 in Shan.
- Older sources treat Dulac finiteness as settled, while Yeung and Llibre report a live proof-status challenge.
- H(2)=4 and H(n)<infinity remain unproved; lower bounds must not be promoted to equalities.

## Usable next step
The strongest honest partial route is a restricted displacement theorem: formalize the displacement/cyclicity objects, retain the kernel-checked Bautin identities, and attack the actual missing analytic step for the coupled second-type Dulac maps. A toy polynomial germ or finite Taylor truncation does not test that step. Any successful argument must state where analyticity/quasianalyticity supplies uniform zero control and where parameter uniformity enters.
