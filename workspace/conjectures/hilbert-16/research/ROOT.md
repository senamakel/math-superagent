# Reference-library root: Hilbert 16.2

## Scope and object
The target is the uniform Hilbert number
\[
H(n)=\sup\{\#\text{ isolated periodic orbits of }X=(P,Q):P,Q\in\mathbb R[x,y],\ \max(\deg P,\deg Q)\le n\}.
\]
The open conjecture is `H(n)<∞` for every `n≥2`; the quadratic case remains open. The object for bifurcation arguments is the displacement function (Poincare return map minus identity), not a numerical phase portrait.

## Minimal counterexample structure
The DRR/Roussarie compactification framework says that a failure of uniform finiteness would be witnessed by a limit-periodic set in the compactified quadratic family whose cyclicity is infinite. The 121-graphic reduction in the held DRR companions makes the relevant minimal obstruction a graphic/polycycle, especially a non-elementary graphic through nilpotent or degenerate singularities. This is a sourced reduction, not a proof of the conjecture.

## Current verification boundary
- Individual polynomial/analytic fields: finiteness of limit cycles is attributed to Écalle–Ilyashenko in the held Ilyashenko source, but proof completeness is contested by Yeung 2024–25; do not silently treat the contested proof as unqualified.
- Uniform quadratic problem: still open; the held DRR companions state reduction to 121 graphics. The library records 88 closed in the RSZ-era count, plus the separately proved `(I^1_14)` closure in Roussarie–Rousseau 2015 (89 by this run's arithmetic), with `(I^1_6b),(H^3_13),(DI_2b)` boundary-only and `(H^3_14)` closed locally by Lu 2026 under the full five-parameter source-normalized quotient unfolding. Shan's held 2013 thesis names 11 degenerate graphics still open at that stage: `DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5`. No complete post-2020 graphic-by-graphic ledger is established.
- Elementary polycycles in generic finite-parameter smooth families are settled: `E(k)≤2^(25 k^2)` (Kaloshin), and with `n` elementary singular vertices `E(n,k)≤(2^(5n^2)+20n) k^(3n)` (Kaleda–Shchurov). These do not cover nilpotent/degenerate graphics.
- Abelian-integral (infinitesimal/tangential) problem is settled constructively: Binyamini–Novikov–Yakovenko give a double-exponential explicit bound; Binyamini–Dor give an explicit bound linear in `deg ω` with explicit dependence on `deg H` (their theorem uses `exp^+` notation). This only controls first-order/Hamiltonian perturbations, not full H16.2.

## At least three restricted classes settled
1. Elementary polycycles in generic `k`-parameter `C^∞` families: finite cyclicity, with Kaloshin's explicit bound and Kaleda–Shchurov's fixed-vertex polynomial-in-`k` bound. Hypotheses: elementary singularities, generic family.
2. Several elementary quadratic graphics: DRR 1994 proves cyclicity at most 1 or 2 for 33 listed graphics, with five under generic conditions; DGR 2002 settles seven graphics surrounding a focus/center (`H^3_4,H^3_5,H^3_6,I^2_{14a},I^2_{15a},I^2_{15b},I^2_{27}`) under their stated quadratic-family setup.
3. Abelian integrals for polynomial Hamiltonian perturbations: BNY's uniform constructive zero count for nonsingular ovals; Binyamini–Dor's refinement is explicit and linear in the perturbation-form degree. Hypotheses: Hamiltonian polynomial, polynomial 1-form, nonsingular compact level ovals, first-order/tangential perturbation.
4. Hyperbolic polycycle multiplicity: Dukov 2023 gives a separate linear-in-number-of-saddles result for multiplicity, not a complete general cyclicity theorem; retained as adjacent restricted evidence.
5. The labelled quadratic semihyperbolic hemicycle `H^3_14`: Lu 2026 proves local uniform finite cyclicity in a fixed annular neighborhood for the full five-parameter source-normalized quotient unfolding. This is local and existential, not a global H(2) proof.

## Main obstruction and why standard approaches do not finish
The elementary-polycycle theory relies on nonzero eigenvalues and genericity. Nilpotent/degenerate graphics require sectorial normal forms, blow-ups, Dulac/transition-map asymptotics, and an analytic or quasianalytic zero theorem. A formal/asymptotic expansion alone fails the smooth test (Dulac's historical error): analyticity must enter in the step that makes the displacement germ determined or gives a uniform zero bound. Pointwise finiteness also does not imply a coefficient-uniform bound.

## Library status
Primary/scholarly sources now held for orientation and restricted results include:
- `research/sources/encyclopedia-hilbert16-wikipedia.full.md` (encyclopedic orientation; not primary evidence).
- `research/sources/kaloshin-hilbert-arnold-2001.full.md`.
- `research/sources/kaleda-shchurov-elementary-polycycles-2011.full.md`.
- `research/sources/binyamini-dor-uniform-petrov-khovanskii-2011.full.md` and `binyamini-dor-nonlinearity-2012.full.md`.
- `research/sources/ilyashenko-centennial-history-hilbert-16.full.md` (canonical survey).
- `research/sources/rousseau-roussarie-center-graphics-nilpotent.full.md`.
- `research/sources/lu-h14-3-2026.full.md`.
- DRR/DGR/Rousseau-Zhu and related full texts already present under `research/sources/`.

## Boundaries and unresolved gaps
The exact current graphic-by-graphic DRR ledger is not established; the source corpus has inconsistent 121/125 catalogue counts. The full proof of any claim that closes the remaining degenerate graphics is not machine-checked here. Lu 2026 is held and read at its abstract and theorem statement: it establishes only local uniform finite cyclicity for labelled `H^3_14`, not a complete DRR closure. The next library work should target the precise DRR status ledger or a primary source for the current best Abelian-integral special-family bounds, and then update `research/REQUESTS.md` before broad searching resumes.

All claims above are `asserted-by-source` unless a local Lean certificate or exact capture says otherwise. No claim here proves `H(n)<∞` or `H(2)=4`.
