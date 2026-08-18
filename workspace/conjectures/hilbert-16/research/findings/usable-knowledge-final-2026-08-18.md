# Scholar delivery: usable knowledge from the H16.2 reference library

The problem is the uniform statement `H(n)<∞` for polynomial planar vector fields, where `H(n)` is the supremum of the number of isolated periodic orbits at degree at most `n`. The mathematical object for bifurcation work is the displacement function `D=T-id` on a transversal. A zero of `D` is a candidate periodic orbit; finite cyclicity is a parameter-uniform bound on such zeros near a limit-periodic set.

## What the primary sources establish

### Structural reduction

**Belotto da Silva–Espín Buendía / Panazzolo–Rousseau**, arXiv:1702.04965 (`research/sources/primary-panazzolo-rousseau-limit-periodic-sets-v1.full.md`), proves a topological classification of limit-periodic sets for polynomial families: after compactification they are topologically equivalent to compact connected semialgebraic subsets of the sphere of dimension 0 or 1 and empty interior; conversely such sets can be realized. Its Proposition 1.2 restricts a limit-periodic set to a singular point, periodic orbit, polycycle, or degenerate limit cycle. **Implication:** an infinite-cyclicity counterexample must occur in this compactified limit-set framework, but this source proves no cyclicity bound.

**DRR and later quadratic companions** establish the working quadratic reduction to finite cyclicity of a conventional 121-graphic list. The raw 1994 paper is not held unrestricted; Shan's thesis reports 125, so the exact current ledger is unresolved. **Implication:** do not claim a complete graphic inventory from the library; use named primary results only.

### Elementary and nilpotent cyclicity

**Ilyashenko–Yakovenko** (`primary-ilyashenko-yakovenko-elementary-polycycles-2000.full.md`) and **Kaloshin** (`primary-kaloshin-elementary-polycycles.html.full.md`) solve the Hilbert–Arnold/local problem for generic finite-parameter families under elementary-polycycle hypotheses. The library records Kaloshin's explicit exponential-scale estimate `2^(25 k^2)` and Kaleda–Shchurov's fixed-number-of-vertices polynomial-in-parameter estimate. The crucial hypotheses are elementary/nondegenerate singularities and genericity. **Implication:** this settles an important restricted class of displacement germs, but excludes nilpotent and degenerate graphics.

**Dumortier–Guzmán–Rousseau 2002** (`dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`) gives explicit cyclicity bounds for seven elementary quadratic graphics: `H^3_4,H^3_5,H^3_6,I^2_27,I^2_14a,I^2_15a,I^2_15b`; the bounds are 2 or 3, with `H^3_6` bounded by 2 if the limiting ratio is not 1 and 3 if it is 1. The proof works with normal forms and transition maps. **Implication:** these are exact, Lean-friendly restricted targets, not evidence for all quadratic systems.

**Zhu–Rousseau 2002** (`zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md`) defines finite cyclicity with explicit parameter and Hausdorff neighborhoods, and develops the family blow-up, first/second Dulac maps, higher-derivative transition criterion, and generalized derivation–division for codimension-3 nilpotent saddle/elliptic graphics. **Implication:** it supplies the correct displacement-function machinery and hypotheses for several nilpotent classes; it does not settle every degenerate graphic.

**Dumortier–Ilyashenko–Rousseau 2002** (`dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full.md`) proves saddle-node normal forms and finite-cyclicity criteria for specified lips ensembles and related graphics. A nonzero derivative of order `r` of a regular transition gives cyclicity at most `r` in the stated setup; other stated saddle-node configurations are finite. Analyticity/non-flatness outside the stable manifold is the essential input. **Implication:** a purely smooth asymptotic argument would fail the problem's smooth test; the proof must identify its analytic/quasianalytic step.

**Roussarie–Rousseau 2015** (`primary-roussarie-rousseau-2015-center-graphics.full.md`) proves full finite cyclicity of `I^1_14`, but only boundary limit-periodic sets for `I^1_6b`, `H^3_13`, and `DI_2b`; the source explicitly says boundary control is insufficient because blow-up creates additional limit sets. **Implication:** the earlier memory “all four center graphics closed” is wrong. These three remain partial, not closed.

### Abelian-integral route

**Binyamini–Novikov–Yakovenko 2010** (`primary-binyamini-novikov-yakovenko-abelian-integrals-2010.full.md`) gives a constructive double-exponential bound (recorded as `2^(2^(O(n^61)))`) for zeros of Abelian integrals over nonsingular ovals, hence for limit cycles from small nonconservative perturbations of polynomial Hamiltonian fields. It uses the regular Gauss–Manin connection and quasiunipotent monodromy; critical/nonsmooth levels and arbitrary nonlinear Dulac compositions are excluded.

**Binyamini–Dor 2011** (`primary-binyamini-dor-uniform-petrov-khovanskii-2011.full.md`) makes the Petrov–Khovanskii bound explicit and linear in `deg ω`, with `exp+` dependence on `deg H`. Novikov–Yakovenko gives the module/Picard–Fuchs organization; Gavrilov and GMV give special Petrov/Chebyshev criteria. **Implication:** this is a solved tangential rung and a possible weakened Lean target. GMV does not cover the complete `I^1_6b` four-Dulac displacement: a new uniform separated-Hamiltonian representation and all CT/balance/small-o hypotheses would be needed.

### Pointwise finiteness and the analytic warning

**Écalle/Ilyashenko** are the classical sources for pointwise finiteness of an individual analytic/polynomial field, but not for a coefficient-uniform bound. **Yeung 2024/25** (`yeung-ilyashenko-finiteness-gap.full.md`) does not disprove that theorem; it challenges completeness of Ilyashenko's non-hyperbolic proof. The claimed counterexample shows the logarithmic asymptotic class is not closed/orderable in the required way (`k2' k1 - k1' k2` leaves the class). Hyperbolic cases are not challenged in the held summary. **Implication:** the pointwise theorem must be labelled “classically established but proof status contested in the semi-hyperbolic case,” and the exact analytic/quasianalytic step is a live issue. This contradicts an unqualified recalled claim that the proof is settled, not the theorem itself.

### Bautin and lower-bound calibration

**Bautin 1952** (`bautin-1952-full.pdf.full.md`) proves the local result `M(2)=3`: at most three small-amplitude cycles can bifurcate from a quadratic focus/center under coefficient variation, and an example with three exists. This is not `H(2)`. It supplies the canonical focus chart and Lyapunov-quantity/Bautin-ideal computation.

The held lower-bound sources support `H(2)≥4`, `H(3)≥13`, `M(3)≥11`, and Christopher–Lloyd/Han–Li growth of order at least `n^2 log n`; therefore a general quadratic-order upper bound is impossible. Slow–fast/Liénard constructions (Dumortier–Panazzolo–Roussarie) refute the classical sharp Lins–de Melo–Pugh count for degree at least 6. These are calibration and falsification constraints, not upper-bound proofs.

### Recent claims and failed approaches

**Lu 2026**, arXiv:2607.13785 (`lu-h14-3-hemicycle-html.full.md`), claims a local uniform finite-cyclicity theorem for `H^3_14` in a fixed annular collar and the full five-parameter unfolding, exactly the graphic RR 2015 left fully open. Local exact checks verify only the finite algebraic/Bautin identities. The analytic remainder, root uniqueness, domain completeness, specialization argument, and uniform zero theorem are not machine-checked; the preprint is unrefereed. **Implication:** asserted-by-source only, not a closure of the DRR program or H16.2.

**Pedregal 2021** (`pedregal-variational-h16-full.md`) claims a quartic degree-only bound and `H(2)=4`. It does not use analyticity/quasianalyticity of the return map, so it fails the required smooth test in the same structural way as Dulac's historical error; it is an unverified negative example, not a solution. **Buzzi–Novaes 2024** refutes a separate closed-form proposal by the `n^2 log n` lower growth. The recalled statements `H(n)<∞` and `H(2)=4` must therefore remain unproved.

## Sources that do not help directly

Landing pages, Crossref/bibliographic records, encyclopedia/Wikipedia/MathWorld pages, and mismatched captures establish provenance or orientation only. Panazzolo–Rousseau classifies topology but does not prove finite cyclicity. BNY/Binyamini–Dor/Novikov–Yakovenko/Gavrilov/GMV concern first-order Hamiltonian perturbations, not arbitrary nonlinear compositions of Dulac maps. Pedregal and Buzzi–Novaes are critique/dead-end evidence, not positive theorems. Yeung challenges proof completeness but does not disprove pointwise finiteness. Lu's abstract page is provenance only; the full preprint remains unrefereed. The captured file named `llibre-zhang-lienard-conjecture-survey.full.md` is an unrelated power-grid paper and must not be used for Liénard claims.

## Contradictions to recalled memory

1. RR 2015 fully closes only `I^1_14`; `I^1_6b`, `H^3_13`, and `DI_2b` have boundary-only results.
2. The conventional DRR count is 121 while Shan reports 125; no reconciliation is held.
3. Individual finiteness is a classical theorem claim, but the non-hyperbolic Ilyashenko proof is contested by Yeung.
4. Lu's checked algebraic core is not Lu's analytic theorem.
5. `M(2)=3` is local Bautin cyclicity and must not be confused with global `H(2)≥4` or conjectural `H(2)=4`.

## Reusable partial-result target

A defensible next step is not a claim on full H16.2. It is a restricted displacement-function theorem: formalize the definition of finite cyclicity and the normal-form/derivation–division finite core for one named nilpotent or saddle-node class, or formalize a Bautin ideal membership and its exact certificate. Any such result must state the parameter neighbourhood, transversal/displacement germ, analytic hypothesis, and the source's excluded regimes. The unresolved library requests remain: a complete 121-row status ledger, an authoritative comparison of newer structural-stability results with uniform H16.2, and the best current special-family Abelian zero bound.
