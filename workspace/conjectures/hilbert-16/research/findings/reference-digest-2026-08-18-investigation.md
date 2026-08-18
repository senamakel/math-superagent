# Reference-library digest for the H16.2 investigation

Memory indexing was unavailable, so this file is the durable local fallback. It records source-backed findings and implications, with evidence class distinguished from proof.

## Core frame

- **DRR/Roussarie reduction** — DRR companion papers and Panazzolo–Rousseau/Belotto–Espín classify the relevant compactified limit-periodic-set types and frame quadratic H16.2 as finite cyclicity of a graphic catalogue. A failure of uniform finiteness would manifest as an infinite-cyclicity compactified limit-periodic set, most plausibly a non-elementary nilpotent/degenerate graphic. The conventional catalogue is 121; Shan reports 125. The raw DRR article and a complete modern row-by-row ledger are not held, so this status is sourced but not a complete census.

- **Panazzolo–Rousseau/Belotto–Espín** (`research/sources/primary-panazzolo-rousseau-limit-periodic-sets-v1.full.md`, arXiv:1702.04965) actually proves a topological characterization: compactified limit periodic sets of polynomial families are topologically equivalent to compact connected semialgebraic subsets of the sphere of dimension 0 or 1/empty interior, and conversely such sets can be realized. Proposition 1.2 restricts them to singular points, periodic orbits, polycycles, or degenerate limit cycles. It does not prove finite cyclicity; its implication here is classification of where a counterexample must live, not an upper bound.

## Restricted finite-cyclicity results

- **Ilyashenko–Yakovenko / Kaloshin** (`primary-ilyashenko-yakovenko-elementary-polycycles-2000.full.md`, `primary-kaloshin-elementary-polycycles.html.full.md`) establish Hilbert–Arnold/local finite cyclicity for generic finite-parameter families with elementary singularities/polycycles. The weight-bearing conditions are nonzero/nondegenerate elementary singularities and genericity. Kaloshin supplies an exponential-scale estimate (the library records 2^(25k^2)); Kaleda–Shchurov supplies a fixed-vertex polynomial-in-parameter estimate. These results do not cover nilpotent or degenerate graphics. They show why the displacement-function zero problem is tractable for elementary Dulac maps and why the open target is outside those hypotheses.

- **Dumortier–Guzmán–Rousseau (2002)** (`dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`) proves explicit cyclicity bounds for seven named elementary quadratic graphics: H^3_4,H^3_5,H^3_6,I^2_27,I^2_14a,I^2_15a,I^2_15b, with bounds 2 or 3 (H^3_6 has ≤2 when r(0)≠1 and ≤3 when r(0)=1). The method uses normal forms and transition maps. It does not cover triple-point/line-of-zeros degenerate graphics.

- **Zhu–Rousseau (2002)** (`zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md`) defines finite cyclicity precisely (uniform N and neighborhoods in the family) and proves machinery for codimension-3 nilpotent saddle/elliptic graphics: family blow-up, first/second Dulac maps, nonzero higher derivatives of regular transitions, and generalized derivation–division. This is directly relevant to displacement zeros, but only for the stated nilpotent classes/hypotheses.

- **Dumortier–Ilyashenko–Rousseau (2002)** (`dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full.md`) gives saddle-node normal forms and finite-cyclicity criteria. The analytic germ is orbitally equivalent to a polynomial normal form (with finite-smooth unfolding equivalence); for lips ensembles a regular transition with first nonzero derivative of order n yields cyclicity ≤n, with further cases (including malignant frown/spadesuit and four even-multiplicity saddle-nodes) finite. The analyticity/non-flatness outside the stable manifold is the step that defeats the smooth-test objection; purely C∞ asymptotics alone are insufficient.

- **Roussarie–Rousseau (2015)** (`primary-roussarie-rousseau-2015-center-graphics.full.md`) proves full finite cyclicity of I^1_14. For the other triple-nilpotent-at-infinity center graphics I^1_6b, H^3_13, DI_2b it proves only the boundary limit-periodic sets, explicitly warning that this is not enough for full graphic cyclicity because the blow-up produces additional limit-periodic sets. Thus these are not closed by that paper.

- **Rousseau–Shan–Zhu (2015)** (`drr-nilpotent-saddle-graphics-2015-arxiv.full.md`) supplies additional named nilpotent-saddle closures; it does not provide a complete DRR census. The library's safe statement is “several named classes closed,” not “all remaining graphics closed.”

## Analytic/tangential rung

- **Binyamini–Novikov–Yakovenko (2010)** (`primary-binyamini-novikov-yakovenko-abelian-integrals-2010.full.md`, arXiv:0808.2952) explicitly bounds zeros of Abelian integrals over nonsingular ovals and hence limit cycles born in small nonconservative perturbations of polynomial Hamiltonian systems. The general explicit bound is doubly exponential in the degree (recorded as 2^(2^(O(n^61)))). The proof uses the regular Gauss–Manin connection and quasiunipotent monodromy. It excludes critical/nonsmooth ovals and says nothing about arbitrary nonlinear compositions of Dulac maps.

- **Binyamini–Dor (2011)** (`primary-binyamini-dor-uniform-petrov-khovanskii-2011.full.md`) makes the Abelian-integral bound explicit and linear in deg(ω), with exp-plus dependence on deg(H). It remains a first-order/tangential Hamiltonian result, not full H16.2. **Novikov–Yakovenko**, **Gavrilov**, and **Grau–Mañosas–Villadelprat** provide module/Picard–Fuchs and special Chebyshev criteria, but GMV's hypotheses are separated Hamiltonian ovals and first-order Abelian-integral families; the held audit says they do not cover the complete I^1_6b four-Dulac displacement without a new uniform representation and verification of all CT/balance hypotheses.

## Individual finiteness and the analytic gap

- **Écalle and Ilyashenko** are the classical sources for pointwise finiteness of limit cycles for an individual analytic/polynomial field, while explicitly not yielding a coefficient-uniform H(n) bound. **Yeung (2024 preprint / 2025 peer-reviewed version)** does not disprove the theorem; it claims a gap in the Ilyashenko proof for semi-hyperbolic/non-hyperbolic polycycles: the logarithmic asymptotic class is not closed/orderable as required, with an explicit failure such as k2'k1−k1'k2 not belonging to the claimed class. Hyperbolic cases remain unchallenged in the held summary. This contradicts an unqualified “pointwise finiteness proof settled” memory only at proof-status level, not as a theorem-disproof.

## Bautin, lower bounds, and calibration

- **Bautin (1952)** (`bautin-1952-full.pdf.full.md`) proves the local quadratic-focus result M(2)=3: at most three small-amplitude cycles can bifurcate from a quadratic focus/center under coefficient variation, and exhibits three. This is local, not H(2). It supplies the canonical focus chart and Lyapunov-quantity/Bautin-ideal target for exact computation.
- Rigorous literature records H(2)≥4 (Shi/Chen–Wang; Galias–Tucker provides a rigorous verification calibration), H(3)≥13, M(3)≥11, and Christopher–Lloyd/Han–Li growth H(n) asymptotically at least order n² log n. Therefore quadratic-order global upper-bound proposals are impossible; H(2)=4 remains conjectural.
- **Dumortier–Panazzolo–Roussarie** slow–fast/Liénard constructions disprove the classical Lins–de Melo–Pugh sharp count for degree ≥6 (n=5 remains open in the held survey). They are a mandatory stress test for any sharp count, not an upper-bound proof.

## Recent claims and negative evidence

- **Lu (arXiv:2607.13785, unrefereed)** claims local uniform finite cyclicity for H^3_14 in a fixed annular collar and full five-parameter unfolding, exactly the case RR 2015 left fully open. The finite algebraic/Bautin identities were independently checked locally, but the analytic remainder/root-uniqueness, domain completeness, specialization, and uniform zero theorem are not machine-checked. Therefore this is asserted-by-source, not an established closure or proof of H16.2.
- **Pedregal (arXiv:2103.07193, unrefereed)** claims a quartic degree-only upper bound and H(2)=4 using a variational/Morse/Bezout argument. It never supplies the analytic/quasianalytic return-map step required by the smooth test, so it is a negative example/obstruction, not a result. The earlier Llibre–Pedregal attempt reported a counting mistake. **Buzzi–Novaes (2024)** refute a different closed-form proposal via the n²log n lower-growth constraint.

## Sources that do not help directly

Landing pages, Crossref records, bibliographic entries, encyclopedia/MathWorld/Wikipedia pages, and mismatched captures provide provenance or orientation only; they cannot support exact theorem statements. Panazzolo–Rousseau is structural, not cyclicity. Abelian-integral/Picard–Fuchs/Gavrilov/GMV sources do not apply to arbitrary nonlinear Dulac compositions without an additional reduction. Pedregal and Buzzi–Novaes are critique/dead-end evidence. Yeung is a proof-status challenge, not a disproof. Lu's abstract page is provenance only; the full preprint remains unrefereed. The accidentally captured `llibre-zhang-lienard-conjecture-survey.full.md` is unrelated power-grid material and must not be cited for Liénard claims.

## Contradictions to recalled memory

1. RR 2015 does not fully close all four named center graphics: only I^1_14 is fully closed; I^1_6b, H^3_13 and DI_2b have boundary-set results only.
2. DRR/RSZ/RR use 121 graphics, while Shan reports 125; no authoritative reconciliation is held.
3. “Individual finiteness is settled” must be qualified: Yeung challenges completeness of Ilyashenko's non-hyperbolic proof, though no theorem disproof is established.
4. The run's local Lu algebra checks support only finite identities, not Lu's analytic theorem or a finite cyclicity bound.
5. M(2)=3 is local Bautin cyclicity and must not be confused with global H(2)≥4 or the open conjecture H(2)=4.
