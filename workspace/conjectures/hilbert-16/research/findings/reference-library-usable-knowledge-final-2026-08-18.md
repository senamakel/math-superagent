# Reference-library usable knowledge — H16.2

Memory indexing was unavailable, so this file is the durable local fallback. It records source-backed claims, implications, non-helpful sources, and contradictions against recalled context.

## What the sources establish and imply

### DRR/Roussarie and compactification
DRR (1994) and successor papers frame the quadratic uniform problem through finite cyclicity of compactified limit-periodic graphics; the conventional count is 121. Shan's thesis reports 125, with no authoritative reconciliation in this library. Panazzolo–Rousseau classify compactified limit-periodic sets topologically and identify singular points, periodic orbits, polycycles, and degenerate cycles as the possible objects, but prove no finite-cyclicity bound. **Implication:** an honest minimal counterexample to uniform finiteness would be an infinite-cyclicity graphic, most plausibly a nilpotent or degenerate one. The target is the full displacement germ, not a phase portrait.

### Elementary polycycles
Ilyashenko–Yakovenko/Kaloshin establish finite cyclicity for elementary polycycles in generic finite-parameter families; the recorded Kaloshin estimate is exponential-scale (2^(25 k^2)), while Kaleda–Shchurov gives a fixed-vertex polynomial-in-parameter estimate. The hypotheses carrying the result are elementary/nonzero-eigenvalue singularities and genericity. **Implication:** elementary graphics are a settled restricted class, but these theorems do not transfer to nilpotent/degenerate DRR graphics. They also show where analyticity/quasianalyticity and genericity enter displacement zero-counting.

### Named quadratic graphics
Dumortier–Guzmán–Rousseau (2002) settles seven named elementary quadratic graphics. Zhu–Rousseau and Rousseau–Shan–Zhu settle selected nilpotent classes, including I^1_12 and I^1_13. Roussarie–Rousseau (2015) fully settles I^1_14, but only proves boundary limit-periodic-set cyclicity for I^1_6b, H^3_13, and DI_2b. The full I^1_6b problem includes coupled four second-type Dulac maps and remains open in the held corpus. **Implication:** the reusable method is normal form + blow-up + Dulac/transition maps + analytic zero theorem; a finite algebraic truncation or toy germ cannot close the missing coupled remainder.

### Abelian integrals/Picard–Fuchs
Binyamini–Novikov–Yakovenko give an explicit doubly-exponential zero bound of the form 2^(2^(O(n^61))) for Abelian integrals over nonsingular compact ovals of polynomial Hamiltonians. Binyamini–Dor refine this to an explicit bound linear in deg(omega), with exp-plus dependence on deg(H). Novikov–Yakovenko, Gavrilov, and GMV provide module/Picard–Fuchs/Petrov-module and special Chebyshev machinery. **Implication:** this settles a tangential/first-order Hamiltonian rung only. It does not bound arbitrary nonlinear compositions of Dulac maps; applying it to I^1_6b requires a new representation theorem plus verification of all hypotheses uniformly.

### Individual finiteness and analytic caution
Écalle/Ilyashenko sources attribute pointwise finiteness for individual analytic/polynomial fields, but Yeung (2024 preprint and 2025 publication) challenges completeness of the non-hyperbolic Ilyashenko proof. This is a proof-status dispute, not a disproof of the finiteness theorem. **Implication:** pointwise finiteness cannot be promoted to coefficient-uniform H(n) finiteness. Any valid proof must use analytic, quasianalytic, resurgent, or algebraic structure at the step that controls the full displacement germ; formal asymptotics alone fails the smooth test.

### Bautin and lower bounds
Bautin's primary result gives local quadratic-focus cyclicity M(2)=3, not global H(2). Rigorous constructions establish H(2)>=4; the library records H(3)>=13, H(4)>=28, M(3)>=11, and lower growth of order n^2 log n. **Implication:** H(2)=4 remains conjectural, and any proposed general upper bound of quadratic order is impossible. Torregrosa's cubic work already reaches twelve small-amplitude cycles, so a twelfth-cycle target is stale.

### Recent claims and critiques
Lu (arXiv:2607.13785, unrefereed) claims local uniform finite cyclicity for H^3_14. The workspace independently checked finite Bautin/algebraic identities only; root uniqueness, domain completeness, analytic remainder control, specialization, and the uniform zero theorem remain unchecked. **Implication:** Lu is a target for verification, not an established closure. Pedregal's variational global claim is unrefereed and prima facie fails the smooth/analyticity test; Buzzi–Novaes refute a separate closed-form proposal using n^2 log n growth.

## Sources that do not help directly

Landing pages, Crossref/bibliographic records, captcha pages, encyclopedias, and mismatched captures establish provenance or orientation only. Panazzolo–Rousseau is structural classification, not a cyclicity theorem. Abelian/Picard–Fuchs/Gavrilov/GMV papers address tangential Hamiltonian perturbations, not arbitrary nonlinear DRR displacement functions. Pedregal and Buzzi–Novaes are critique/dead-end evidence, not positive proofs. Yeung challenges proof completeness but does not disprove finiteness. Lu's abstract and independently checked algebraic core do not establish its analytic theorem. The Christopher–Li–Torregrosa book capture is a contents record, not an independently read proof. The file named `llibre-zhang-lienard-conjecture-survey.full.md` is an unrelated power-grid paper and must not support Liénard claims.

## Contradictions with recalled memory

1. Roussarie–Rousseau (2015) did not fully close all four named center graphics: I^1_14 is full; I^1_6b, H^3_13, and DI_2b have boundary-only results.
2. The DRR catalogue count is conventionally 121 versus Shan's 125; unresolved.
3. “Individual finiteness is settled” requires a proof-status qualification because Yeung challenges the non-hyperbolic Ilyashenko proof.
4. The Lu algebraic checks do not establish Lu's analytic finite-cyclicity theorem.
5. M(2)=3 is local and distinct from H(2)>=4 and the open conjecture H(2)=4.

## Formalisation boundary

Mathlib supplies polynomial fields via `MvPolynomial (Fin 2) ℝ`, total-degree bounds, ODE integral-curve predicates, and set cardinality. It lacks packaged notions of limit cycle, return/displacement map, Dulac function, polycycle/graphic, finite cyclicity, Bautin ideal, Abelian integral, and Lyapunov quantities. `Statement.lean` can state H16.2 with a hand-defined periodic-orbit isolation predicate, but the conjecture remains a deliberate `sorry`; this is a formalisation finding, not evidence for the conjecture.
