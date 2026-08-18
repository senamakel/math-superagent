# Usable knowledge extracted from the H16.2 reference library

## Scope
The problem is the uniform conjecture `H(n)<∞` for polynomial planar vector fields, where `H(n)` is the supremum of isolated periodic-orbit counts at degree at most `n`. The working object is the displacement function `D=T-id` on a transversal. The library does not support claiming the conjecture.

## Source-backed findings and implications

1. **DRR/Roussarie reduction.** DRR and successor papers reduce the quadratic problem to finite cyclicity of compactified limit-periodic graphics; the conventional catalogue count is 121, while Shan reports 125, with no reconciliation in this library. Panazzolo–Rousseau classify possible compactified limit-periodic sets (singular points, periodic orbits, polycycles, degenerate cycles) but prove no cyclicity bound. Implication: a minimal counterexample would be an infinite-cyclicity graphic, most plausibly nilpotent/degenerate; the required theorem is a uniform zero bound for the full displacement germ.

2. **Restricted classes already settled.** Ilyashenko–Yakovenko/Kaloshin give finite cyclicity for generic finite-parameter families with elementary polycycles; the elementary/nonzero-eigenvalue and genericity hypotheses are essential. Kaloshin's recorded estimate is exponential-scale (`2^(25 k^2)`), and Kaleda–Shchurov supplies a fixed-vertex polynomial-in-parameter estimate. DGR 2002 settles seven named elementary quadratic graphics. These results do not cover nilpotent/degenerate graphics.

3. **Named quadratic graphics.** RSZ 2015 closes `I^1_12` and `I^1_13`; RR 2015 fully closes `I^1_14`, but gives only boundary limit-periodic-set cyclicity for `I^1_6b`, `H^3_13`, and `DI_2b`. The full `I^1_6b` non-boundary problem involves four second-type Dulac maps and a coupled two-equation displacement problem; no held source closes it. This is the most concrete displacement-function target in the library.

4. **Analytic pointwise finiteness.** Écalle/Ilyashenko sources attribute finiteness to each analytic/polynomial field, but not uniformly in coefficients. Yeung 2024/25 challenges completeness of the non-hyperbolic Ilyashenko proof; this is a proof-status contradiction, not a disproof. Any valid uniform argument must identify where analyticity/quasianalyticity enters; formal asymptotics alone fails the smooth test.

5. **Abelian/Picard–Fuchs rung.** Binyamini–Novikov–Yakovenko give a constructive double-exponential zero bound for Abelian integrals over nonsingular Hamiltonian ovals; Binyamini–Dor gives an explicit bound linear in `deg(ω)` with `exp+` dependence on Hamiltonian complexity. Novikov–Yakovenko, Gavrilov and GMV provide module/Picard–Fuchs/Petrov/Chebyshev machinery. These prove only the tangential/first-order Hamiltonian problem, not nonlinear compositions of Dulac maps. They are suitable restricted targets, not a solution of H16.2.

6. **Calibration.** Bautin's primary result is local quadratic-focus cyclicity `M(2)=3`, not global `H(2)`. Held sources support `H(2)≥4`, `H(3)≥13`, `H(4)≥28`, `M(3)≥11`, and lower growth of order `n^2 log n`; consequently a quadratic-order general upper bound is impossible. Slow-fast Liénard constructions refute classical sharp-count conjectures and are mandatory stress tests.

7. **Recent claims.** Lu 2026 claims local uniform finite cyclicity for `H^3_14`, the graphic RR left fully open. The workspace exact computations verify only finite Bautin/algebraic identities. They do not establish common analytic domains, exhaustive itineraries, center-ideal/Hadamard division, nonidentity, root uniqueness, or a uniform zero theorem; the preprint is unrefereed. Pedregal's variational claim is unrefereed and supplies no analyticity step, so it fails the smooth test prima facie. Buzzi–Novaes refute a separate closed-form proposal using `n^2 log n` growth.

## Sources that do not help directly
Landing pages, abstracts, bibliographic records, captcha captures, encyclopedia pages, and contaminated/mismatched files establish provenance or orientation only. Panazzolo–Rousseau is structural, not a zero bound. Abelian-integral sources do not control arbitrary nonlinear Dulac compositions. Pedregal and Buzzi–Novaes are critique/dead-end evidence, not positive proofs. Yeung critiques proof completeness but does not disprove pointwise finiteness. Lu's algebraic core is insufficient for its analytic theorem. The captured Christopher–Li–Torregrosa 2024 book is a contents record rather than a proof. `llibre-zhang-lienard-survey.full.md` is contaminated by an unrelated power-grid paper and must not be cited.

## Contradictions to recalled memory
- RR 2015 did not fully close all four named center graphics: only `I^1_14` is full; the other three are boundary-only.
- The catalogue count is 121 conventionally versus 125 in Shan.
- Classical individual finiteness is treated as settled by older sources, but Yeung's non-hyperbolic proof-gap claim makes completeness contested.
- `M(2)=3` is local, while `H(2)≥4`; neither implies `H(2)=4` or `H(2)<∞`.
- Lu's checked finite algebraic core is not the claimed analytic closure.

## Durable-storage failure
`remember_memory` and `relate_memory` were unavailable (health timeout/409) during this pass. This file is the durable local fallback; retry Cognee only after service recovery.